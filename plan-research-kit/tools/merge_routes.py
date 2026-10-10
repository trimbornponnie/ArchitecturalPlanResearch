"""Merge the route manifests of a project's web research into one project manifest.

    python3 tools/merge_routes.py "Projects/<Project>" [--corrections <json>]

Reads Projects/<Project>/Research/R*/manifest.jsonl (one row per line, schema in Research/BRIEFING.md) and writes
Projects/<Project>/manifest.jsonl and manifest.csv, the files project.json names for fetch_guarded.py,
assemble_project.py and audit_project.py.

- Every field fetch_project.py and assemble_project.py read is present (missing ones become null or false).
- downloadable is recomputed: download_url set, access open, url_status checked_ok or redirect, and the route's own
  downloadable flag. auto_fetch_ok stays what the route found with guard.py check.
- Copies of one item get same_item_as = the row kept: the same download_url; the same Flickr photo id (the
  largest size kept); the same file name on the same host with a WordPress "-WxH" size suffix (the unsuffixed or
  larger one kept).
- --corrections: a JSON object {row_id: {field: value, ...}} applied last (gap rounds, sighting), each change
  written into merge_note.
Prints counts by route, design_id and count_as.
"""
import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

RB = Path(__file__).resolve().parent.parent
FIELDS = ["row_id", "route", "design_id", "title", "sheet_type", "contents", "format", "file_type", "download_url",
          "page_url", "pages", "pixel_size", "scale", "date", "author", "holder", "license", "access", "url_status",
          "shows_state", "origin", "downloadable", "auto_fetch_ok", "count_as", "same_item_as", "fetch_rule",
          "evidence", "notes", "merge_note"]


def px(r):
    m = re.match(r"\s*(\d+)\s*[x×]\s*(\d+)", str(r.get("pixel_size") or ""))
    return int(m.group(1)) * int(m.group(2)) if m else 0


def item_key(url):
    if not url:
        return None
    u = urlparse(url)
    host, name = u.netloc.lower(), Path(u.path).name
    m = re.match(r"(\d+)_[0-9a-f]+(?:_[a-z0-9]+)?\.\w+$", name)
    if host.endswith("staticflickr.com") and m:
        return "flickr:" + m.group(1)
    m = re.match(r"(.+?)-\d+x\d+(\.\w+)$", name)
    if m:
        return "%s:%s" % (host, (Path(u.path).parent / (m.group(1) + m.group(2))).as_posix())
    return "%s:%s" % (host, u.path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--corrections")
    a = ap.parse_args()
    proj = Path(a.project) if Path(a.project).is_absolute() else RB / a.project
    cfg_path = proj / "project.json"
    cfg = json.loads(cfg_path.read_text(encoding="utf-8")) if cfg_path.is_file() else {}
    default_design = cfg.get("default_design", "unknown")   # rows without a design_id
    rows, seen_ids = [], set()
    for f in sorted((proj / "Research").glob("R*/manifest.jsonl"), key=lambda p: int(re.sub(r"\D", "", p.parent.name) or 0)):
        for n, line in enumerate(open(f, encoding="utf-8"), 1):
            if not line.strip():
                continue
            try:
                r = json.loads(line)
            except ValueError as e:
                print("unreadable line %s:%d (%s)" % (f.relative_to(proj), n, e))
                continue
            r.setdefault("route", f.parent.name)
            if not r.get("row_id") or r["row_id"] in seen_ids:
                r["row_id"] = "%s-%04d" % (f.parent.name.lower(), n + 9000)
            seen_ids.add(r["row_id"])
            row = {k: r.get(k) for k in FIELDS}
            row["source_rows"] = "%s:%d" % (f.relative_to(proj).as_posix(), n)
            row["downloadable"] = bool(r.get("downloadable")) and bool(r.get("download_url")) and \
                r.get("access") == "open" and r.get("url_status") in ("checked_ok", "redirect")
            row["auto_fetch_ok"] = bool(r.get("auto_fetch_ok")) and row["downloadable"]
            row["count_as"] = r.get("count_as") or "drawing"
            row["design_id"] = r.get("design_id") or default_design
            row["same_item_as"] = r.get("same_item_as") or None
            row["merge_note"] = r.get("merge_note") or ""
            rows.append(row)

    if a.corrections:
        fixes = json.loads(Path(a.corrections).read_text(encoding="utf-8"))
        by_id = {r["row_id"]: r for r in rows}
        for rid, change in fixes.items():
            if rid not in by_id:
                print("correction for unknown row %s" % rid)
                continue
            for k, v in change.items():
                by_id[rid]["merge_note"] = (by_id[rid]["merge_note"] + "; " if by_id[rid]["merge_note"] else "") + \
                    "%s: %r -> %r" % (k, by_id[rid].get(k), v)
                by_id[rid][k] = v

    # copies of one item: keep the largest, downloadable first
    groups = {}
    for r in rows:
        if r["count_as"] in ("drawing", "document_pointer") and r["download_url"] and not r["same_item_as"]:
            key = (item_key(r["download_url"]), r["count_as"], r.get("pages") if r["count_as"] == "drawing" else None)
            groups.setdefault(key, []).append(r)
    for key, members in groups.items():
        if len(members) < 2:
            continue
        members.sort(key=lambda r: (not r["downloadable"], not r["auto_fetch_ok"], -px(r),
                                    bool(re.search(r"-\d+x\d+\.\w+$", r["download_url"])), r["row_id"]))
        keep = members[0]
        for r in members[1:]:
            r["same_item_as"] = keep["row_id"]
            r["merge_note"] = (r["merge_note"] + "; " if r["merge_note"] else "") + "copy of %s (%s)" % (keep["row_id"], key[0])

    out = proj / "manifest.jsonl"
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(proj / "manifest.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS + ["source_rows"])
        w.writeheader()
        for r in rows:
            w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k, v in r.items()})
    print("%d rows -> %s" % (len(rows), out))
    for label, key in (("route", "route"), ("design_id", "design_id"), ("count_as", "count_as")):
        print(label, dict(Counter(r[key] for r in rows)))
    take = [r for r in rows if r["count_as"] in ("drawing", "document_pointer") and r["downloadable"] and not r["same_item_as"]]
    print("to fetch: %d rows, %d distinct URLs, auto_fetch_ok %d" % (
        len(take), len({r["download_url"] for r in take}), sum(r["auto_fetch_ok"] for r in take)))


if __name__ == "__main__":
    main()
