"""Sort a multi-building project's downloaded drawings into Plans/<folder>/Vectorized and Plans/<folder>/Rasterized.

    python3 tools/sort_plans.py "Projects/Venice Biennale Pavilions" [--plans ../Plans] [--only german,russian]

Reads <project>/pavilions.json (route, slug, folder per building), <project>/manifest.jsonl (merged by
merge_routes.py) and <project>/Downloads/index.csv with the sidecars fetch_guarded.py wrote. For every downloaded
file of a building's design ids (<slug>, <slug>-alt, <slug>-reno, <slug>-unk) it decides, by opening the file:
  Vectorized   DWG, DXF, SVG, AI, EPS, IFC and other CAD formats; a PDF whose drawing pages are vector line work
  Rasterized   JPG, PNG, TIF, GIF, WEBP, BMP, JP2; a PDF whose drawing pages are scanned or embedded images
A PDF page counts as vector when it carries at least VEC_ITEMS path items (lines, curves, rectangles) and no image
covers more than RASTER_COVER of it; text glyphs are not paths, so a text page with a raster figure stays raster.
A PDF of more than LONG_DOC pages whose manifest rows list the drawing pages is not copied whole: the listed pages
are cut into one PDF per class (insert_pdf keeps the vector line work), "(p12-13)" in the name; the whole document
stays in Downloads/. Files of unbuilt schemes (-alt) carry "ALT unbuilt" in the name.

Each run rebuilds the Vectorized/ and Rasterized/ folders of the buildings it touches (files are hard links into
Downloads/ where the file system allows, else copies) and writes Plans/<folder>/index.csv (one line per file:
class, evidence, rows, titles, sheet types, source and page URLs, author, holder, licence as stated, sha256) and
Plans/index.csv over all folders. A building with no file yet keeps its two empty folders (.gitkeep).
"""
import argparse
import csv
import hashlib
import json
import os
import re
import shutil
from collections import OrderedDict
from pathlib import Path

import pymupdf

KIT = Path(__file__).resolve().parent.parent
VECTOR_EXT = {"dwg", "dxf", "svg", "svgz", "ai", "eps", "ps", "ifc", "dgn", "skp", "3dm", "rvt", "pln", "emf", "wmf"}
RASTER_EXT = {"jpg", "jpeg", "png", "tif", "tiff", "gif", "webp", "bmp", "jp2", "heic"}
VEC_ITEMS = 300
RASTER_COVER = 0.6
LONG_DOC = 10
MAX_SCAN = 80
CLASSES = ("Vectorized", "Rasterized")
FIELDS = ["folder", "class", "file", "evidence", "row_ids", "design_ids", "titles", "sheet_types", "pages",
          "download_url", "page_url", "author", "holder", "license", "date", "pixel_size", "bytes", "sha256",
          "source_file"]


def ids(d):
    return [] if not d or "|" in d else d.split("+")


def page_numbers(spec, n):
    """'PDF page 12 of 140', '12,13 of 140', '12-14' -> [12, 13, 14] (1-based, within 1..n)."""
    if not spec:
        return []
    s = re.sub(r"\bof\s+\d+.*$", "", str(spec))
    out = []
    for a, b in re.findall(r"(\d+)\s*(?:[-–]\s*(\d+))?", s):
        lo, hi = int(a), int(b or a)
        out += [p for p in range(lo, hi + 1) if 1 <= p <= n]
    return sorted(set(out))


def page_class(page):
    """('vector'|'raster'|'text', evidence) for one PDF page."""
    area = abs(page.rect) or 1.0
    try:
        items = sum(len(d.get("items", ())) for d in page.get_drawings())
    except Exception:  # noqa: BLE001 - a broken content stream counts as no paths
        items = 0
    cover = 0.0
    try:
        for info in page.get_image_info():
            r = pymupdf.Rect(info["bbox"]) & page.rect
            cover = max(cover, abs(r) / area)
    except Exception:  # noqa: BLE001
        pass
    if cover <= 0.05 and items >= VEC_ITEMS // 6:
        return "vector", "%d path items, no image" % items
    if items >= VEC_ITEMS and cover <= RASTER_COVER:
        return "vector", "%d path items, largest image %.0f%%" % (items, cover * 100)
    if cover > 0.05:
        return "raster", "%d path items, image covers %.0f%%" % (items, cover * 100)
    return "text", "%d path items, no image" % items


def classify_pdf(path, pages):
    """(per-page {page: (cls, ev)}, overall class, evidence). pages: 1-based drawing pages, or [] for all."""
    with pymupdf.open(path) as doc:
        todo = pages or list(range(1, min(doc.page_count, MAX_SCAN) + 1))
        res = OrderedDict((p, page_class(doc[p - 1])) for p in todo if p <= doc.page_count)
    kinds = [c for c, _ in res.values()]
    if "vector" in kinds:
        cls = "Vectorized"
    else:
        cls = "Rasterized"
    ev = "PDF, %d page(s) looked at: %d vector, %d raster, %d text" % (
        len(kinds), kinds.count("vector"), kinds.count("raster"), kinds.count("text"))
    return res, cls, ev


def safe_name(s, n=110):
    s = re.sub(r'[<>:"/\\|?*\x00-\x1f]+', " ", s or "")
    s = re.sub(r"\s+", " ", s).strip(" .")
    return s[:n].rstrip(" .") or "untitled"


def link_or_copy(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        dst.unlink()
    try:
        os.link(src, dst)
    except OSError:
        shutil.copy2(src, dst)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("project", help="project folder, relative to plan-research-kit/ or absolute")
    ap.add_argument("--plans", default=str(KIT.parent / "Plans"), help="Plans root (default: <repo>/Plans)")
    ap.add_argument("--only", default="", help="comma-separated Plans folders to rebuild (default: all)")
    a = ap.parse_args()

    proj = Path(a.project)
    proj = proj if proj.is_absolute() else KIT / proj
    plans = Path(a.plans).resolve()
    pav = json.loads((proj / "pavilions.json").read_text(encoding="utf-8"))["pavilions"]
    only = {x.strip() for x in a.only.split(",") if x.strip()}
    folder_of = {}
    for p in pav:
        for d in (p["slug"], p["slug"] + "-alt", p["slug"] + "-reno", p["slug"] + "-unk"):
            folder_of[d] = p["folder"]

    rows = {}
    mpath = proj / "manifest.jsonl"
    if mpath.exists():
        for line in open(mpath, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                rows[r["row_id"]] = r
    files = OrderedDict()   # local_path -> [row ids]
    ipath = proj / "Downloads" / "index.csv"
    if ipath.exists():
        for line in csv.DictReader(open(ipath, encoding="utf-8-sig")):
            if line["local_path"] and line["status"] in ("ok", "exists", "manual", "moved"):
                files.setdefault(line["local_path"], []).append(line["row_id"])

    plan = {}   # folder -> list of (src, rows)
    for lp, rids in files.items():
        rs = [rows[r] for r in rids if r in rows]
        folders = {folder_of[d] for r in rs for d in ids(r["design_id"]) if d in folder_of}
        for f in folders:
            plan.setdefault(f, []).append((proj / lp, [r for r in rs if any(folder_of.get(d) == f for d in ids(r["design_id"]))]))

    targets = [p["folder"] for p in pav if not only or p["folder"] in only]
    all_lines = []
    for folder in targets:
        base = plans / folder
        for c in CLASSES:
            d = base / c
            if d.exists():
                for f in d.iterdir():
                    if f.is_file() and f.name != ".gitkeep":
                        f.unlink()
            d.mkdir(parents=True, exist_ok=True)
        lines, used = [], set()
        for src, rs in plan.get(folder, []):
            if not src.is_file():
                print("missing %s" % src)
                continue
            first = rs[0]
            ext = src.suffix.lower().lstrip(".")
            alt = any(d.endswith("-alt") for r in rs for d in ids(r["design_id"]))
            stype = first.get("sheet_type") or "other"
            title = safe_name(first.get("title") or src.stem, 80)
            tag = "[%s]" % first["row_id"]
            stem = "%s - %s%s" % (stype, "ALT unbuilt - " if alt else "", title)
            side = src.with_name(src.name + ".json")
            meta = json.loads(side.read_text(encoding="utf-8")) if side.exists() else {}
            common = {
                "folder": folder, "row_ids": " ".join(r["row_id"] for r in rs),
                "design_ids": " ".join(sorted({r["design_id"] for r in rs})),
                "titles": " | ".join(OrderedDict.fromkeys(r.get("title") or "" for r in rs)),
                "sheet_types": " ".join(OrderedDict.fromkeys(r.get("sheet_type") or "" for r in rs)),
                "download_url": first.get("download_url"), "page_url": first.get("page_url"),
                "author": first.get("author"), "holder": first.get("holder"), "license": first.get("license"),
                "date": first.get("date"), "source_file": src.relative_to(proj).as_posix(),
            }
            outs = []   # (class, dst, evidence, pages, writer)
            if ext in VECTOR_EXT:
                outs.append(("Vectorized", None, "file type .%s" % ext, "", None))
            elif ext in RASTER_EXT:
                outs.append(("Rasterized", None, "file type .%s" % ext, "", None))
            elif ext == "pdf":
                try:
                    with pymupdf.open(src) as doc:
                        n = doc.page_count
                except Exception as e:  # noqa: BLE001
                    print("unreadable PDF %s: %s" % (src, e))
                    outs.append(("Rasterized", None, "PDF not readable (%s); placed as raster for a look by hand" % type(e).__name__, "", None))
                    n = 0
                if n:
                    listed = sorted({p for r in rs for p in page_numbers(r.get("pages"), n)})
                    per, cls, ev = classify_pdf(src, listed)
                    if n > LONG_DOC and listed:
                        blank = [p for p, (k, _) in per.items() if k == "text"]
                        if blank:
                            print("%s: listed page(s) %s hold neither paths nor images; not cut" % (src.name, blank))
                        for c in CLASSES:
                            want = "vector" if c == "Vectorized" else "raster"
                            pg = [p for p, (k, _) in per.items() if k == want]
                            if pg:
                                outs.append((c, None, "%s; pages %s cut from a %d-page document" % (ev, ",".join(map(str, pg)), n), pg, "cut"))
                    else:
                        outs.append((cls, None, ev, "", None))
            else:
                outs.append(("Rasterized" if ext in ("html", "htm") else "Vectorized", None, "unknown type .%s, check by hand" % ext, "", None))

            for cls, _, ev, pg, how in outs:
                if how == "cut":
                    span = "p%s" % (",".join(map(str, pg)) if len(pg) < 6 else "%d-%d" % (pg[0], pg[-1]))
                    name = "%s (%s) %s.pdf" % (stem, span, tag)
                else:
                    name = "%s %s.%s" % (stem, tag, ext)
                name = safe_name(name, 150)
                while name.lower() in used:
                    name = name.replace(tag, tag + "+")
                used.add(name.lower())
                dst = base / cls / name
                if how == "cut":
                    with pymupdf.open(src) as doc, pymupdf.open() as out:
                        for p in pg:
                            out.insert_pdf(doc, from_page=p - 1, to_page=p - 1)
                        out.save(dst, garbage=3, deflate=True)
                else:
                    link_or_copy(src, dst)
                line = dict(common)
                line.update({"class": cls, "file": "%s/%s" % (cls, name), "evidence": ev,
                             "pages": ",".join(map(str, pg)) if pg else (first.get("pages") or ""),
                             "pixel_size": meta.get("pixel_size_measured", ""), "bytes": dst.stat().st_size,
                             "sha256": sha256(dst)})
                lines.append(line)
        with open(base / "index.csv", "w", encoding="utf-8-sig", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=FIELDS)
            w.writeheader()
            for line in lines:
                w.writerow({k: line.get(k, "") for k in FIELDS})
        for c in CLASSES:
            keep = base / c / ".gitkeep"
            if not any(f.name != ".gitkeep" for f in (base / c).iterdir()):
                keep.touch()
            elif keep.exists():
                keep.unlink()
        v = sum(1 for x in lines if x["class"] == "Vectorized")
        print("%-18s %3d vectorized, %3d rasterized" % (folder, v, len(lines) - v))
        all_lines += lines

    # the overall index covers every folder's index.csv, not only the ones rebuilt now
    total = []
    for p in pav:
        f = plans / p["folder"] / "index.csv"
        if f.exists():
            total += list(csv.DictReader(open(f, encoding="utf-8-sig")))
    plans.mkdir(parents=True, exist_ok=True)
    with open(plans / "index.csv", "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        for line in total:
            w.writerow({k: line.get(k, "") for k in FIELDS})
    print("Plans/index.csv: %d files in %d folders" % (len(total), len({x["folder"] for x in total})))


if __name__ == "__main__":
    main()
