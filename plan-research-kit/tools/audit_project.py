"""Completeness audit of one project against the manifest (the list).

    python3 "tools/audit_project.py" "Projects/<Project Name>/project.json"

A. Every manifest row of the project's designs (and dropped designs) must end in exactly one state: in the
   plan set, waiting for a hand download, excluded with a reason, a whole document kept as source, or
   skipped with a reason (archive only, 3D model, duplicate, excluded in the manifest).
B. Every file in Downloads/: sidecar present, sha256 equal, magic bytes fit the extension, measured pixel
   size equal to the manifest's pixel_size, PDF page count equal to the manifest's "of N".
C. Every register line of the plan set: file present, opens, one page for page cuts, hard link intact.
D. Counts against building_list.csv, if the project's designs are in it.
E. Report excerpts (if _work/excerpts/decisions.json exists): one PDF per report, cover + kept pages, each
   excerpt page carries the text of the source page it claims, and model pages.csv lists the same pages.
Writes _work/completeness.json and prints a summary. Exit code 1 when anything fails.
"""
import csv
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import pymupdf
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
MAGIC = {".tif": (b"II*\x00", b"MM\x00*"), ".pdf": (b"%PDF",), ".jpg": (b"\xff\xd8",), ".png": (b"\x89PNG",), ".dwg": (b"AC10",)}


def ids(d):
    return [] if not d or "|" in d else d.split("+")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    cfg_path = Path(sys.argv[1]).resolve()
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    proj = cfg_path.parent
    rows = [json.loads(l) for l in open((proj / cfg["manifest"]).resolve(), encoding="utf-8")]
    designs, drop = set(cfg["designs"]), set(cfg.get("drop_designs", []))
    mine = [r for r in rows if set(ids(r["design_id"])) & (designs | drop)]
    index = {l["row_id"]: l for l in csv.DictReader(open(proj / "Downloads" / "index.csv", encoding="utf-8-sig"))}
    reg = json.loads((proj / "_work" / "register.json").read_text(encoding="utf-8"))
    in_set = {r["row_id"] for r in reg}
    fails = []

    # ---- A. every row accounted for
    state = {}
    for r in mine:
        rid, line = r["row_id"], index.get(r["row_id"])
        if rid in in_set:
            state[rid] = "in plan set"
        elif not line:
            state[rid] = "UNACCOUNTED: not in Downloads/index.csv"
        elif line["status"] == "refused":
            state[rid] = "waiting for a hand download"
        elif line["status"] == "excluded":
            state[rid] = "excluded: " + line["note"].replace("excluded: ", "")
        elif line["kind"] == "issue" and line["status"] in ("ok", "exists", "manual", "moved"):
            state[rid] = "whole document kept as source"
        elif line["status"] == "skipped":
            state[rid] = "skipped: " + line["note"]
        else:
            state[rid] = "UNACCOUNTED: status %s" % line["status"]
    unacc = [(k, v) for k, v in state.items() if v.startswith("UNACCOUNTED")]
    fails += ["row %s %s" % kv for kv in unacc]
    by_state = Counter(re.sub(r":.*", "", v) for v in state.values())

    # ---- B. files
    files = []
    man_by_url = defaultdict(list)
    for r in mine:
        if r.get("download_url"):
            man_by_url[r["download_url"]].append(r)
    for f in sorted((proj / "Downloads").rglob("*")):
        if not f.is_file() or f.suffix in (".json", ".csv", ".part"):
            continue
        rec = {"file": f.relative_to(proj).as_posix(), "problems": []}
        side = f.with_name(f.name + ".json")
        if not side.exists():
            rec["problems"].append("no sidecar")
        else:
            meta = json.loads(side.read_text(encoding="utf-8"))
            if meta.get("sha256") != sha256(f):
                rec["problems"].append("sha256 differs from sidecar")
            for k in ("download_url", "license", "holder"):
                if not meta.get(k):
                    rec["problems"].append("sidecar lacks " + k)
            mrows = man_by_url.get(meta.get("download_url"), [])
            with open(f, "rb") as fh:
                head = fh.read(8)
            magic = MAGIC.get(f.suffix.lower())
            if magic and not head.startswith(magic):
                rec["problems"].append("magic bytes %r do not fit %s" % (head, f.suffix))
            if f.suffix.lower() in (".tif", ".jpg", ".png"):
                with Image.open(f) as im:
                    rec["pixel_size"] = "%dx%d" % im.size
                want = {r.get("pixel_size") for r in mrows if r.get("pixel_size")}
                if want and rec["pixel_size"] not in want:
                    rec["problems"].append("pixel size %s, manifest says %s" % (rec["pixel_size"], "/".join(sorted(want))))
            if f.suffix.lower() == ".pdf":
                with pymupdf.open(f) as doc:
                    rec["pdf_pages"] = doc.page_count
                ofs = {int(m.group(1)) for r in mrows for m in [re.search(r"\bof\s+(\d+)", str(r.get("pages") or ""))] if m}
                if ofs and rec["pdf_pages"] not in ofs:
                    rec["problems"].append("PDF has %d pages, manifest says %s" % (rec["pdf_pages"], ofs))
        rec["bytes"] = f.stat().st_size
        files.append(rec)
        fails += ["%s: %s" % (rec["file"], p) for p in rec["problems"]]

    # ---- C. plan set
    set_dir = proj / "Plan set"
    on_disk = {p.relative_to(set_dir).as_posix() for p in set_dir.rglob("*") if p.is_file() and p.parent != set_dir}
    listed = {r["file"] for r in reg}
    for r in reg:
        p = set_dir / r["file"]
        if not p.exists():
            fails.append("plan set: missing %s" % r["file"])
            continue
        if r["how"] == "hardlink" and os.stat(p).st_nlink < 2:
            fails.append("plan set: hard link broken for %s" % r["file"])
        if p.suffix.lower() == ".pdf":
            with pymupdf.open(p) as doc:
                if doc.page_count != 1:
                    fails.append("plan set: %s has %d pages" % (r["file"], doc.page_count))
        if "WARNING" in r.get("how", ""):
            fails.append("plan set: %s %s" % (r["file"], r["how"]))
    fails += ["plan set: file not in register %s" % x for x in sorted(on_disk - listed)]

    # ---- D. counts against building_list.csv
    counts = {}
    bl = proj.parent.parent / "building_list.csv"
    if bl.exists():
        for d in csv.DictReader(open(bl, encoding="utf-8-sig")):
            if d["design_id"] in designs | drop:
                dl = [r for r in rows if d["design_id"] in ids(r["design_id"]) and r["count_as"] == "drawing"
                      and r["downloadable"] and not r["same_item_as"]]
                c = Counter(state.get(r["row_id"], "?").split(":")[0] for r in dl)
                counts[d["design_id"]] = {"building_list_downloadable": int(d["drawings_downloadable_now"]),
                                          "manifest_downloadable": len(dl), "by_state": dict(c)}
                if int(d["drawings_downloadable_now"]) != len(dl):
                    fails.append("count: %s building_list says %s, manifest gives %d" % (d["design_id"], d["drawings_downloadable_now"], len(dl)))

    # ---- E. report excerpts
    excerpts = {}
    dec_path = proj / "_work" / "excerpts" / "decisions.json"
    if dec_path.exists():
        dec = json.loads(dec_path.read_text(encoding="utf-8"))
        listed = Counter()
        mp = proj / "Report excerpts" / "model pages.csv"
        if mp.exists():
            listed = Counter(l["report"] for l in csv.DictReader(open(mp, encoding="utf-8-sig")))
        for key, rep in dec.items():
            keep = sorted(p["page"] for p in rep["pages"] if p["keep"])
            f = proj / "Report excerpts" / ("%s - model pages.pdf" % rep["short"])
            if not f.exists():
                fails.append("excerpt missing: %s" % f.name)
                continue
            with pymupdf.open(f) as ex, pymupdf.open(proj / rep["source"]) as src:
                if ex.page_count != len(keep) + 1:
                    fails.append("excerpt %s: %d pages, %d kept + cover" % (f.name, ex.page_count, len(keep)))
                else:
                    bad = [pg for i, pg in enumerate(keep, 1)
                           if ex[i].get_text().strip() != src[pg - 1].get_text().strip()]
                    fails += ["excerpt %s: page for source p%d differs from the source" % (f.name, pg) for pg in bad]
                if listed.get(rep["short"], 0) != len(keep):
                    fails.append("excerpt %s: model pages.csv lists %d, decisions keep %d" % (f.name, listed.get(rep["short"], 0), len(keep)))
                excerpts[rep["short"]] = {"kept": len(keep), "of": src.page_count}

    out = {"rows": len(mine), "by_state": dict(by_state), "states": state, "files": files,
           "plan_set_sheets": len(reg), "plan_set_from_manifest": len([r for r in reg if r["row_id"] in state]),
           "plan_set_found_in_review": len([r for r in reg if r["row_id"] not in state]),
           "counts": counts, "excerpts": excerpts, "fails": fails}
    (proj / "_work" / "completeness.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("manifest rows of the project:", len(mine))
    for k, v in sorted(by_state.items(), key=lambda kv: -kv[1]):
        print("  %-32s %d" % (k, v))
    print("files in Downloads:", len(files), "| %.2f GB" % (sum(f["bytes"] for f in files) / 1e9))
    print("plan set sheets:", len(reg), "=", out["plan_set_from_manifest"], "from the manifest +", out["plan_set_found_in_review"], "found in the review")
    for d, c in counts.items():
        print("  %s: building_list %d, manifest %d, %s" % (d, c["building_list_downloadable"], c["manifest_downloadable"], c["by_state"]))
    for k, v in excerpts.items():
        print("  excerpt %s: %d of %d pages" % (k, v["kept"], v["of"]))
    print("FAILS:" if fails else "no fails", len(fails))
    for f in fails:
        print("  ", f)
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
