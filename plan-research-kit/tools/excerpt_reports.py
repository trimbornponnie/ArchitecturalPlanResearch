"""Cut long reports down to the pages a 3D model needs.

    python3 "tools/excerpt_reports.py" "Projects/<Project Name>/project.json"

Input: Projects/<name>/_work/excerpts/decisions.json, one entry per report:
    {"<key>": {"title", "short", "source" (path in the project), "pages": [{page, keep, category, also,
     building, facts, reason, disputed, judged, redundant_with}]}}
The decisions come from a page review (every page looked at, challenged both ways, disputes judged).

Output in Projects/<name>/Report excerpts/:
    <short> - model pages.pdf   a cover page, then the kept pages in their original order, copied with
                                insert_pdf (text and vector content stay), page labels = original page
                                numbers, one bookmark per page with its category and facts
    model pages.csv             one line per kept page: report, source page, category, facts, reason
and _work/excerpts/page_decisions.csv with every page of every report, kept or dropped, with the reason.
The full reports stay in Downloads/ as the checksummed source; nothing is taken from them but pages.
"""
import csv
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

import pymupdf

LABEL = {"drawing": "drawing", "dimensions": "dimensions", "materials_construction": "materials",
         "colour_finish": "colour", "site_topography": "site", "trees_landscape": "trees",
         "alterations_record": "alterations", "photo_fabric": "photo", "none": "-"}


def runs(pages):
    """Consecutive runs of page numbers: [(first, last), ...]."""
    out = []
    for p in pages:
        if out and p == out[-1][1] + 1:
            out[-1][1] = p
        else:
            out.append([p, p])
    return out


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    cfg_path = Path(sys.argv[1]).resolve()
    proj = cfg_path.parent
    dec = json.loads((proj / "_work" / "excerpts" / "decisions.json").read_text(encoding="utf-8"))
    out_dir = proj / "Report excerpts"
    out_dir.mkdir(exist_ok=True)
    kept_lines, all_lines, made = [], [], []
    for key, rep in dec.items():
        src_path = proj / rep["source"]
        src = pymupdf.open(src_path)
        pages = sorted(rep["pages"], key=lambda p: p["page"])
        if [p["page"] for p in pages] != list(range(1, src.page_count + 1)):
            sys.exit("%s: decisions cover %d of %d pages" % (key, len(pages), src.page_count))
        keep = [p for p in pages if p["keep"]]
        by_cat = {}
        for p in keep:
            by_cat[LABEL[p["category"]]] = by_cat.get(LABEL[p["category"]], 0) + 1

        doc = pymupdf.open()
        cover = doc.new_page(width=src[0].rect.width, height=src[0].rect.height)
        text = [
            rep["title"],
            "",
            "Model pages: %d of %d pages, kept because they hold drawings, dimensions, materials and" % (len(keep), src.page_count),
            "construction, colours and finishes, site and tree data, dated alterations, or photographs of",
            "the fabric of the house as built. Everything else (history, significance, policies, lab",
            "methods, monitoring, collections) is left out.",
            "",
            "Kept by category: " + ", ".join("%s %d" % kv for kv in sorted(by_cat.items(), key=lambda kv: -kv[1])),
            "",
            "Page labels and bookmarks give the page number of the full report.",
            "Why each page was kept: model pages.csv beside this file.",
            "Full report: %s" % rep["source"],
            "sha256 %s" % sha256(src_path),
            "Made %s from a page review (machine_sighted: agents looked, no person has)." % dt.date.today().isoformat(),
            "Private research material; the report's own copyright and terms apply.",
        ]
        box = cover.rect + (54, 60, -54, -60)
        head = pymupdf.Rect(box.x0, box.y0, box.x1, box.y0 + 60)
        cover.insert_textbox(head, text[0], fontsize=14, fontname="helv")
        body = " ".join(text[2:6]) + "\n\n" + text[7] + "\n\n" + "\n".join(text[9:])
        cover.insert_textbox(pymupdf.Rect(box.x0, head.y1 + 10, box.x1, box.y1), body, fontsize=9.5, fontname="helv")
        for a, b in runs([p["page"] for p in keep]):
            doc.insert_pdf(src, from_page=a - 1, to_page=b - 1)
        labels = [{"startpage": 0, "prefix": "cover", "style": ""}]
        at = 1
        for a, b in runs([p["page"] for p in keep]):
            labels.append({"startpage": at, "prefix": "", "style": "D", "firstpagenum": a})
            at += b - a + 1
        doc.set_page_labels(labels)
        toc = [[1, "Cover: what was kept and why", 1]]
        for i, p in enumerate(keep, 2):
            toc.append([1, "p. %d  %s  %s" % (p["page"], LABEL[p["category"]], p["facts"][:110]), i])
        doc.set_toc(toc)
        name = "%s - model pages.pdf" % rep["short"]
        tmp = out_dir / (name + ".part")
        doc.save(str(tmp), garbage=3, deflate=True)
        doc.close()
        tmp.replace(out_dir / name)
        made.append((name, len(keep), src.page_count))
        for p in pages:
            line = {"report": rep["short"], "source_page": p["page"], "kept": "yes" if p["keep"] else "no",
                    "category": LABEL[p["category"]], "also": " ".join(LABEL[c] for c in p.get("also") or []),
                    "building": p.get("building", ""), "facts": p.get("facts", ""), "reason": p.get("reason", ""),
                    "review": "judged after a dispute" if p.get("judged") else "disputed, first decision held" if p.get("disputed") else "",
                    "redundant_with": p.get("redundant_with", "")}
            all_lines.append(line)
            if p["keep"]:
                kept_lines.append({k: line[k] for k in ("report", "source_page", "category", "also", "facts", "reason")})
    with open(out_dir / "model pages.csv", "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["report", "source_page", "category", "also", "facts", "reason"])
        w.writeheader()
        w.writerows(kept_lines)
    with open(proj / "_work" / "excerpts" / "page_decisions.csv", "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(all_lines[0].keys()))
        w.writeheader()
        w.writerows(all_lines)
    for name, k, n in made:
        print("%-45s %3d of %3d pages" % (name, k, n))


if __name__ == "__main__":
    main()
