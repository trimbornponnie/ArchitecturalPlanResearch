"""Download every drawing of one project into Projects/<Project Name>/Downloads/.

    Not run on its own in this kit: tools/fetch_guarded.py imports it and replaces download() with guard.py.
    python3 "tools/fetch_guarded.py" "Projects/Eames House/project.json"
        [--migrate-from <old root>]  move files an earlier layout already holds instead of fetching them
        [--pickup <folder>]          adopt hand-saved files from one more folder, e.g. %USERPROFILE%/Downloads

A file a person saved by hand (a host closed to scripts) is dropped into Projects/<Project Name>/Inbox/;
every run looks there first and moves it into Downloads/ when it is recognised by name, or for a PDF by
page count and title. Each file taken is logged in Inbox/_picked_up.txt, so an Inbox that empties itself is
accounted for; a file with the same bytes as one Downloads/ already holds (dropped twice) is removed and
logged; anything not recognised stays and is printed.

project.json names the manifest, the design ids to take, the design ids to drop (unbuilt schemes), and
single rows to exclude with a reason. A row is taken when count_as is drawing (downloadable, no
same_item_as) or document_pointer (downloadable), and its design_id shares an id with "designs" and
none with "drop_designs". Rows of dropped designs and excluded rows are listed in the index with the reason.

Every request goes through guard.py (via fetch_guarded.py): robots.txt read live (unreadable = do not fetch),
at least one second between requests per host, a 403/429/bot challenge refuses the host. Each distinct URL is fetched once into
Downloads/<host>/<name> with a sidecar <name>.json (every row it serves, source, holder, licence, sha256,
measured size). Rerunnable: a file whose sidecar sha256 matches is not fetched again. A file saved by
hand under the expected name (or found in --pickup) is adopted with fetched_by "hand". Downloads/index.csv
gets one line per manifest row of the project, excluded and skipped rows with their reason.
"""
import argparse
import csv
import datetime as dt
import hashlib
import json
import re
import shutil
import sys
from collections import OrderedDict
from pathlib import Path
from urllib.parse import unquote, urlparse



def download(url, net=None, **kw):
    """Replaced by tools/fetch_guarded.py (guard.Guard.fetch). The rekon downloader of the original is not part of
    this kit, so a direct run must not send requests."""
    raise SystemExit("run tools/fetch_guarded.py; fetch_project.py does not fetch on its own")


def net_for():
    raise SystemExit("run tools/fetch_guarded.py; fetch_project.py does not fetch on its own")

MAGIC = {"tif": (b"II*\x00", b"MM\x00*"), "pdf": (b"%PDF",), "jpg": (b"\xff\xd8",), "png": (b"\x89PNG",),
         "dwg": (b"AC10",)}
INDEX_FIELDS = ["row_id", "design_id", "kind", "local_path", "status", "http_status", "bytes", "sha256",
                "pixel_size", "pages", "fetched", "note"]


def ids(d):
    return [] if not d or "|" in d else d.split("+")


def ascii_name(s):
    return re.sub(r"[^A-Za-z0-9._+-]+", "_", s).strip("_")


def ext_of(url, row):
    base = unquote(Path(urlparse(url).path).name)
    if "." in base:
        return base.rsplit(".", 1)[1].lower()
    return (row.get("file_type") or "bin").lower()


def file_name(url, row):
    """The name a file gets in Downloads/<host>/: the URL's own name, made unambiguous where hosts reuse
    names (LOC HABS sheets, LOC pnp ids) or give none (NPGallery assets)."""
    u = urlparse(url)
    host, base = u.netloc.lower(), unquote(Path(u.path).name)
    if host == "tile.loc.gov" and "/habshaer/" in u.path:
        m = re.search(r"/habshaer/\w+/\w+/(\w+)/", u.path)
        name = "habs_%s_sheet_%s" % (m.group(1) if m else "x", base)
    elif host == "tile.loc.gov" and "/pnp/" in u.path:
        name = u.path.split("/pnp/")[1].split("/")[0] + "_" + base
    elif "." not in base:
        name = "%s.%s" % (row["row_id"], (row.get("file_type") or "bin").lower())
    else:
        name = base
    return host, ascii_name(name)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def measure(path, ext):
    out = {}
    try:
        if ext in ("tif", "tiff", "jpg", "jpeg", "png"):
            from PIL import Image
            Image.MAX_IMAGE_PIXELS = None
            with Image.open(path) as im:
                out["pixel_size_measured"] = "%dx%d" % im.size
                out["mode"] = im.mode
                if im.info.get("dpi"):
                    out["dpi"] = [round(float(x), 1) for x in im.info["dpi"]]
        elif ext == "pdf":
            import pymupdf
            with pymupdf.open(path) as doc:
                out["pdf_pages"] = doc.page_count
    except Exception as e:  # noqa: BLE001 - recorded, not fatal
        out["measure_error"] = "%s: %s" % (type(e).__name__, e)
    return out


def find_pdf(folder, rows):
    """A PDF in `folder` that is this document: same page count as the rows' "PDF page x of N" and every
    word of the title (the part before ", fig" or " (") in the text of its first three pages."""
    import pymupdf
    ofs = {int(m.group(1)) for r in rows for m in [re.search(r"\bof\s+(\d+)", str(r.get("pages") or ""))] if m}
    title = re.split(r",\s*fig|\s\(", rows[0].get("title") or "")[0]
    words = [w.lower() for w in re.findall(r"[A-Za-z]{4,}", title)]
    if not ofs or not words:
        return None
    for f in sorted(folder.glob("*.pdf"), key=lambda f: -f.stat().st_mtime):
        try:
            with pymupdf.open(f) as doc:
                if doc.page_count not in ofs:
                    continue
                text = " ".join(doc[i].get_text() for i in range(min(3, doc.page_count))).lower()
        except Exception:  # noqa: BLE001 - not a readable PDF
            continue
        if all(w in text for w in words):
            return f
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("config")
    ap.add_argument("--migrate-from", help="old root whose index.csv local_path entries are moved in")
    ap.add_argument("--pickup", help="folder to adopt hand-saved files from (matched by file name)")
    args = ap.parse_args()

    cfg_path = Path(args.config).resolve()
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    proj = cfg_path.parent
    rb = proj.parent.parent
    dl = proj / "Downloads"
    dl.mkdir(parents=True, exist_ok=True)
    index_path = dl / "index.csv"
    manifest = (proj / cfg["manifest"]).resolve()
    rows = [json.loads(line) for line in open(manifest, encoding="utf-8")]
    designs, drop = set(cfg["designs"]), set(cfg.get("drop_designs", []))
    exclude = cfg.get("exclude_rows", {})

    old = {}
    if args.migrate_from:
        root = Path(args.migrate_from)
        for line in csv.DictReader(open(root / "index.csv", encoding="utf-8-sig")):
            if line["local_path"]:
                old[line["row_id"]] = rb / line["local_path"]

    jobs, lines, now = OrderedDict(), [], dt.datetime.now().isoformat(timespec="seconds")
    for r in rows:
        d = set(ids(r["design_id"]))
        if not d & (designs | drop):
            continue
        reason = None
        if d & drop:
            reason = "excluded: " + cfg.get("drop_reason", "design dropped from this project")
        elif r["row_id"] in exclude:
            reason = "excluded: " + exclude[r["row_id"]]
        elif r["count_as"] == "drawing" and r["downloadable"] and not r["same_item_as"]:
            jobs.setdefault(r["download_url"], {"kind": "drawing", "rows": []})["rows"].append(r)
            continue
        elif r["count_as"] == "document_pointer" and r["downloadable"]:
            jobs.setdefault(r["download_url"], {"kind": "issue", "rows": []})["rows"].append(r)
            continue
        else:
            reason = ("same item as " + r["same_item_as"]) if r["same_item_as"] else \
                     "3d model, %s" % r["access"] if r["count_as"] == "3d_model" else \
                     "excluded in manifest" if r["count_as"] == "excluded" else \
                     "not downloadable: %s" % r["access"]
        lines.append({"row_id": r["row_id"], "design_id": r["design_id"], "kind": r["count_as"],
                      "status": "excluded" if reason.startswith("excluded") else "skipped",
                      "pages": r.get("pages") or "", "fetched": now, "note": reason})

    # files saved by hand: the project's Inbox/ always, plus --pickup
    inbox = proj / "Inbox"
    inbox.mkdir(exist_ok=True)
    pickups = [inbox] + ([Path(args.pickup)] if args.pickup else [])
    receipt = []

    net = net_for()
    total = len(jobs)
    for i, (url, job) in enumerate(jobs.items(), 1):
        first = job["rows"][0]
        host, name = file_name(url, first)
        dest = dl / host / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        side = dest.with_name(dest.name + ".json")
        ext = ext_of(url, first)
        magic = MAGIC.get({"tiff": "tif", "jpeg": "jpg"}.get(ext, ext))
        status, note, http, body, meta = "ok", "", 200, None, {}

        # an earlier layout: move file and sidecar in
        src = next((old[r["row_id"]] for r in job["rows"] if r["row_id"] in old and old[r["row_id"]].exists()), None)
        if src is not None and not dest.exists():
            shutil.move(str(src), str(dest))
            s_side = src.with_name(src.name + ".json")
            if s_side.exists():
                shutil.move(str(s_side), str(side))
        # a hand-saved copy waiting in the pickup folder: by its own name, or (a browser may rename it) a PDF
        # whose page count equals the manifest's "of N" and whose first pages carry the document title
        for folder in pickups:
            if dest.exists():
                break
            cand = folder / unquote(Path(urlparse(url).path).name)
            if not cand.is_file() and ext == "pdf":
                cand = find_pdf(folder, job["rows"])
            if cand is not None and cand.is_file():
                shutil.move(str(cand), str(dest))
                note = "picked up from %s/%s" % (folder.name, cand.name)
                receipt.append("%s  taken    %s -> %s (%s)" % (now, cand.name, dest.relative_to(proj).as_posix(),
                                                              re.split(r",\s*fig", first["title"])[0]))

        if dest.exists() and side.exists() and json.loads(side.read_text(encoding="utf-8")).get("sha256") == sha256(dest):
            status = "exists"
            meta = json.loads(side.read_text(encoding="utf-8"))
        elif dest.exists():
            with open(dest, "rb") as f:
                head = f.read(8)
            if magic and not head.startswith(magic):
                status, note, http = "bad_content", "hand-saved file starts %r" % head, ""
            else:
                status, note, http = "manual", "saved by hand in a browser; adopted", ""
        else:
            http, body, note = download(url, net=net)
            if http != 200 or not body:
                status = "refused" if http == -1 else "error"
            elif magic and not body.startswith(magic):
                status = "bad_content"
                note = (note + "; " if note else "") + "body starts %r" % body[:8]
        if status in ("ok", "manual"):
            if status == "ok":
                part = dest.with_name(dest.name + ".part")
                part.write_bytes(body)
                part.replace(dest)
            meta = {
                "row_ids": [r["row_id"] for r in job["rows"]],
                "design_ids": sorted({r["design_id"] for r in job["rows"]}),
                "titles": [r["title"] for r in job["rows"]],
                "pages_used": [r["pages"] for r in job["rows"]],
                "download_url": url, "page_url": first.get("page_url"),
                "author": first.get("author"), "holder": first.get("holder"), "date": first.get("date"),
                "license": first.get("license"), "license_status": "unconfirmed",
                "rights_note": "private research material for this project; not redistributed",
                "access": first.get("access"), "sha256": sha256(dest), "bytes": dest.stat().st_size,
                "fetched": dt.datetime.now().isoformat(timespec="seconds"), "http_status": http,
                "fetch_note": note or None,
            }
            if status == "manual":
                meta["fetched_by"] = "hand, in a browser (the host is closed to scripts)"
            meta.update(measure(dest, ext))
            side.write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
        elif status == "exists" and src is not None:
            status = "moved"
        rel = dest.relative_to(proj).as_posix() if status in ("ok", "exists", "manual", "moved") else ""
        if status == "refused":
            note = (note + "; " if note else "") + "save by hand as " + dest.relative_to(proj).as_posix()
        print("[%d/%d] %-8s %s -> %s %s" % (i, total, status, url[-60:], rel or "-", ("(%s)" % note) if note else ""), flush=True)
        for r in job["rows"]:
            lines.append({"row_id": r["row_id"], "design_id": r["design_id"], "kind": job["kind"],
                          "local_path": rel, "status": status, "http_status": http,
                          "bytes": meta.get("bytes", ""), "sha256": meta.get("sha256", ""),
                          "pixel_size": meta.get("pixel_size_measured", ""), "pages": r.get("pages") or "",
                          "fetched": meta.get("fetched", now), "note": note or ""})

    # what is left in the Inbox: a second copy of a file Downloads/ holds is removed, the rest stays
    held = {}
    for f in dl.rglob("*"):
        if f.is_file() and f.suffix not in (".json", ".csv", ".part"):
            held.setdefault(f.stat().st_size, []).append(f)
    for f in sorted(inbox.iterdir()):
        if not f.is_file() or f.name.startswith("_"):
            continue
        twin = next((h for h in held.get(f.stat().st_size, []) if sha256(h) == sha256(f)), None)
        if twin is not None:
            f.unlink()
            receipt.append("%s  removed  %s: same bytes as %s" % (now, f.name, twin.relative_to(proj).as_posix()))
        else:
            print("Inbox: %s not recognised; left there" % f.name)
    if receipt:
        with open(inbox / "_picked_up.txt", "a", encoding="utf-8") as fh:
            fh.write("\n".join(receipt) + "\n")
        print("\n".join(receipt))

    order = {r["row_id"]: k for k, r in enumerate(rows)}
    lines.sort(key=lambda x: order.get(x["row_id"], 1 << 30))
    tmp = index_path.with_suffix(".csv.part")
    with open(tmp, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=INDEX_FIELDS)
        w.writeheader()
        for line in lines:
            w.writerow({k: line.get(k, "") for k in INDEX_FIELDS})
    tmp.replace(index_path)
    counts = {}
    for line in lines:
        counts[line["status"]] = counts.get(line["status"], 0) + 1
    print("rows by status:", counts)
    print("requests:", net.counters)


if __name__ == "__main__":
    main()
