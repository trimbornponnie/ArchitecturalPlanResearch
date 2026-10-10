"""Assemble a project's downloaded drawings into Projects/<Project Name>/Plan set/.

    python3 "tools/assemble_project.py" "Projects/Eames House/project.json" [--no-previews]

Reads the manifest named in project.json and Downloads/index.csv, and rebuilds Plan set/ from scratch:
  <group folder>/<seq> <type> - <short title> [<source id>].<ext>   hard links into Downloads/ (no second copy)
  <group folder>/<seq> <type> - <short title> (p<N>).pdf           one page cut from a multi-page PDF
                                                                    (pymupdf insert_pdf keeps vector line work)
  <Project> plan set.csv          the register, one line per sheet
  <Project> contact sheet.pdf     thumbnails with captions, 12 per page
Previews (JPEG, long side 1600 px) go to _work/previews/ for sighting.

project.json keys used here: name, manifest, designs, drop_designs, exclude_rows, groups (list of
{"folder", "match": {"url": [...], "design": [...], "rows": [...]}}, first match wins, a group without
match takes the rest; "priority" raises a group in matching), title_strip (regexes, or [regex, replacement]
pairs, applied to catalogue titles for file names), extra_pages
(optional JSON list of pages found in whole documents: {"source": <path in Downloads>, "page", "row_id",
"design_id", "sheet_type", "title", "contents", "date", "author", "holder", "license", "url"}), extra_group.
"""
import argparse
import csv
import json
import os
import re
import shutil
from pathlib import Path

import pymupdf
from PIL import Image, ImageDraw, ImageFont

FONTS = ("C:/Windows/Fonts/arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "DejaVuSans.ttf")


def load_font(size):
    for path in FONTS:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            pass
    return ImageFont.load_default()

Image.MAX_IMAGE_PIXELS = None
TYPE_ORDER = {t: i for i, t in enumerate(
    ["site", "plan", "section", "elevation", "framing", "detail", "axonometric", "perspective", "schedule", "other"])}


def ids(d):
    return [] if not d or "|" in d else d.split("+")


def pages_of(pages):
    """'PDF page 11 of 208' -> ([11], 208); '3' -> ([3], None); '33,34' -> ([33, 34], None)."""
    if pages in (None, ""):
        return [], None
    s = str(pages)
    m = re.search(r"\bof\s+(\d+)", s)
    total = int(m.group(1)) if m else None
    s = re.sub(r"\bof\s+\d+", "", s)
    return [int(x) for x in re.findall(r"\d+", s)], total


def clean(s, n=70):
    s = re.sub(r"[\\/:*?\"<>|\r\n\t]+", " ", s or "")
    s = re.sub(r"\s+", " ", s).strip(" .")
    return s if len(s) <= n else s[:n].rstrip(" .,;-") + "~"


def short_title(r, strips):
    t = (r.get("title") or "").lstrip("[")
    for pat in strips:
        pat, repl = (pat, "") if isinstance(pat, str) else pat
        t = re.sub(pat, repl, t, flags=re.I)
    t = re.sub(r"\]?\s+/\s.*$", "", t)
    t = t.strip(" .[]")
    if t.endswith(")") and t.count(")") > t.count("("):
        t = t[:-1].rstrip(" .")
    return t or re.split(r"[.;]", r.get("contents") or r.get("title") or "")[0]


def src_id(src):
    m = re.match(r"habs_\w+?_sheet_0*(\d+)a$", src.stem)
    if m:
        return "HABS sheet %s" % m.group(1)
    m = re.match(r"(ppmsca|ppmsc|cph|ds|ppss|ppmsca)_(\w+?)u?$", src.stem)
    if m:
        return "LOC %s %s" % m.groups()
    return ""


def group_of(r, groups):
    """First matching group; groups with a higher "priority" are tried first (a shared site plan on
    tile.loc.gov belongs with the shared sheets, not with the working drawings)."""
    url, d = r.get("download_url") or "", set(ids(r["design_id"]))
    for g in sorted(groups, key=lambda g: (-g.get("priority", 0), 0 if g.get("match") else 1)):
        m = g.get("match")
        if not m:
            return g["folder"]
        if any(u in url for u in m.get("url", [])) or d & set(m.get("design", [])) or r["row_id"] in m.get("rows", []):
            return g["folder"]
    return groups[-1]["folder"]


def link_or_copy(src, dst):
    try:
        os.link(src, dst)
        return "hardlink"
    except OSError:
        shutil.copy2(src, dst)
        return "copy"


def preview_image(path):
    ext = path.suffix.lower()
    if ext == ".pdf":
        with pymupdf.open(path) as doc:
            page = doc[0]
            zoom = 1600 / max(page.rect.width, page.rect.height)
            pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), alpha=False)
            return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    if ext in (".tif", ".tiff", ".jpg", ".jpeg", ".png"):
        with Image.open(path) as im:
            im.load()
            if im.mode in ("1", "P", "I;16", "I", "F"):
                im = im.convert("L")
            elif im.mode not in ("L", "RGB"):
                im = im.convert("RGB")
            im.thumbnail((1600, 1600), Image.LANCZOS, reducing_gap=3.0)
            return im.copy()
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("config")
    ap.add_argument("--no-previews", action="store_true")
    args = ap.parse_args()
    cfg_path = Path(args.config).resolve()
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    proj = cfg_path.parent
    name = cfg["name"]
    SET = proj / "Plan set"
    work = proj / "_work"
    prev = work / "previews"
    rows = [json.loads(line) for line in open((proj / cfg["manifest"]).resolve(), encoding="utf-8")]
    index = {line["row_id"]: line for line in csv.DictReader(open(proj / "Downloads" / "index.csv", encoding="utf-8-sig"))}
    designs, drop, exclude = set(cfg["designs"]), set(cfg.get("drop_designs", [])), cfg.get("exclude_rows", {})
    sel = [r for r in rows if set(ids(r["design_id"])) & designs and not set(ids(r["design_id"])) & drop
           and r["row_id"] not in exclude and r["count_as"] == "drawing" and r["downloadable"] and not r["same_item_as"]]
    groups = cfg["groups"]
    gorder = {g["folder"]: k for k, g in enumerate(groups)}
    strips = cfg.get("title_strip", [])

    if SET.exists():
        shutil.rmtree(SET)
    SET.mkdir(parents=True)
    prev.mkdir(parents=True, exist_ok=True)
    for f in prev.glob("*.jpg"):
        f.unlink()

    items, missing = [], []
    for r in sel:
        line = index.get(r["row_id"])
        if not line or line["status"] not in ("ok", "exists", "manual", "moved") or not line["local_path"]:
            missing.append((r["row_id"], line["status"] if line else "not in index", line["note"] if line else ""))
            continue
        pg, tot = pages_of(r["pages"])
        items.append({"row": r, "src": proj / line["local_path"], "group": group_of(r, groups), "pages": pg, "of": tot})
    xp = cfg.get("extra_pages")
    if xp and (proj / xp).exists():
        for e in json.loads((proj / xp).read_text(encoding="utf-8")):
            items.append({"row": {"row_id": e["row_id"], "design_id": e["design_id"], "title": e["title"],
                                  "sheet_type": e["sheet_type"], "contents": e.get("contents", ""), "format": "raster",
                                  "file_type": "pdf", "download_url": e.get("url"), "page_url": e.get("url"),
                                  "scale": None, "date": e.get("date"), "author": e.get("author"),
                                  "holder": e.get("holder"), "license": e.get("license"), "pixel_size": None},
                          "src": proj / e["source"], "group": cfg["extra_group"], "pages": [int(e["page"])], "of": None})

    items.sort(key=lambda it: (gorder[it["group"]], it["row"].get("download_url") or "", it["pages"][:1] or [0],
                               TYPE_ORDER.get(it["row"]["sheet_type"], 9), it["row"]["row_id"]))
    register, seq = [], 0
    for it in items:
        r, src = it["row"], it["src"]
        folder = SET / it["group"]
        folder.mkdir(exist_ok=True)
        stype = r["sheet_type"] or "other"
        short, sid = short_title(r, strips), src_id(src)
        rec = {"seq": seq + 1, "group": it["group"], "design_id": r["design_id"], "row_id": r["row_id"],
               "title": r["title"], "short_title": short, "source_id": sid, "sheet_type": stype,
               "contents": r.get("contents") or "", "format_manifest": r.get("format"), "file_type": "",
               "pixel_size": "", "pdf_page": "", "vector_paths": "", "images_on_page": "",
               "scale": r.get("scale") or "", "date": r.get("date") or "", "author": r.get("author") or "",
               "holder": r.get("holder") or "", "license": r.get("license") or "",
               "download_url": r.get("download_url") or "", "page_url": r.get("page_url") or "",
               "source_file": src.relative_to(proj).as_posix(), "file": "", "how": ""}
        if src.suffix.lower() == ".pdf" and it["pages"]:
            p = it["pages"][0]
            with pymupdf.open(src) as doc:
                if p < 1 or p > doc.page_count:
                    missing.append((r["row_id"], "page %d outside %d pages" % (p, doc.page_count), ""))
                    continue
                seq += 1
                rec["seq"] = seq
                dst = folder / ("%03d %s - %s (p%d).pdf" % (seq, stype, clean(short), p))
                out = pymupdf.open()
                out.insert_pdf(doc, from_page=p - 1, to_page=p - 1)
                rec["vector_paths"] = len(out[0].get_drawings())
                rec["images_on_page"] = len(out[0].get_images())
                out.save(dst, garbage=3, deflate=True)
                out.close()
                rec["how"] = "page cut from source PDF"
                if it["of"] and it["of"] != doc.page_count:
                    rec["how"] += "; WARNING source has %d pages, manifest says %d" % (doc.page_count, it["of"])
                if len(it["pages"]) > 1:
                    rec["how"] += "; row lists pages %s, first taken" % it["pages"]
            rec.update(file_type="pdf", pdf_page=p)
        else:
            seq += 1
            rec["seq"] = seq
            ext = src.suffix.lower()
            dst = folder / ("%03d %s - %s%s%s" % (seq, stype, clean(short), (" [%s]" % sid) if sid else "", ext))
            rec["how"] = link_or_copy(src, dst)
            rec["file_type"] = ext.lstrip(".")
            if ext in (".tif", ".tiff", ".jpg", ".jpeg", ".png"):
                with Image.open(src) as im:
                    rec["pixel_size"] = "%dx%d" % im.size
        rec["file"] = dst.relative_to(SET).as_posix()
        register.append(rec)
        if not args.no_previews and dst.suffix.lower() != ".dwg":
            try:
                im = preview_image(dst)
                if im is not None:
                    im.convert("RGB").save(prev / ("%03d.jpg" % seq), quality=85)
            except Exception as e:  # noqa: BLE001
                missing.append((r["row_id"], "preview failed: %s" % e, ""))
        print("%03d %-34s %s" % (seq, it["group"][:34], rec["file"][-80:]), flush=True)

    fields = list(register[0].keys())
    with open(SET / ("%s plan set.csv" % name), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(register)
    (work / "register.json").write_text(json.dumps(register, ensure_ascii=False, indent=1), encoding="utf-8")
    (work / "assemble_missing.json").write_text(json.dumps(missing, ensure_ascii=False, indent=1), encoding="utf-8")

    if not args.no_previews:
        font, small = load_font(16), load_font(13)
        W, H, cols, rws = 1754, 1240, 4, 3
        cw, ch = (W - 60) // cols, (H - 90) // rws
        pages, page, k = [], None, 0
        for rec in register:
            pv = prev / ("%03d.jpg" % rec["seq"])
            if k % (cols * rws) == 0:
                page = Image.new("RGB", (W, H), "white")
                ImageDraw.Draw(page).text((30, 20), "%s plan set - contact sheet %d" % (name, len(pages) + 1), fill="black", font=font)
                pages.append(page)
            d = ImageDraw.Draw(page)
            cx, cy = 30 + (k % cols) * cw, 60 + ((k // cols) % rws) * ch
            if pv.exists():
                with Image.open(pv) as im:
                    im = im.convert("RGB")
                    im.thumbnail((cw - 16, ch - 58))
                    page.paste(im, (cx + (cw - im.width) // 2, cy))
                    d.rectangle([cx + (cw - im.width) // 2 - 1, cy - 1, cx + (cw + im.width) // 2, cy + im.height], outline=(180, 180, 190))
            else:
                d.rectangle([cx + 8, cy, cx + cw - 8, cy + ch - 60], outline=(180, 180, 190))
                d.text((cx + 20, cy + 20), "%s (no preview)" % rec["file_type"].upper(), fill=(90, 90, 90), font=small)
            d.text((cx + 8, cy + ch - 54), "%03d  %s" % (rec["seq"], rec["sheet_type"]), fill="black", font=small)
            d.text((cx + 8, cy + ch - 36), clean(rec["short_title"], 42), fill=(70, 70, 80), font=small)
            k += 1
        if pages:
            pages[0].save(SET / ("%s contact sheet.pdf" % name), save_all=True, append_images=pages[1:], resolution=150)
    print("sheets:", len(register), "| missing or skipped:", len(missing))
    for m in missing:
        print("  ", m[0], m[1], m[2][:120])


if __name__ == "__main__":
    main()
