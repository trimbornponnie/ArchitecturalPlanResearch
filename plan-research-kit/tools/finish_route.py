"""Download and sort one building's drawings as soon as its research route (or gap route) is done.

    python3 tools/finish_route.py "Projects/Venice Biennale Pavilions" --folder german

One run at a time per project (a lock file in _work/; a second run waits), because merge_routes.py, fetch_guarded.py
and Downloads/index.csv are project-wide:
1. every Research/R*/corrections.json is combined into _work/corrections.json (a later route wins on a field);
2. tools/merge_routes.py merges all routes with those corrections into manifest.jsonl;
3. tools/fetch_guarded.py --check (its own process), then tools/fetch_guarded.py (a second process) downloads every
   downloadable row of the project that is not yet in Downloads/ (files a route already fetched are adopted);
4. tools/sort_plans.py --only <folder> rebuilds Plans/<folder>/Vectorized and Rasterized.
Prints the tail of each step and a summary of the folder. Exit code 0 unless a step crashed.
"""
import argparse
import csv
import fcntl
import json
import subprocess
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent


def run(args, tail=25):
    p = subprocess.run([sys.executable] + args, cwd=KIT, capture_output=True, text=True)
    out = (p.stdout + ("\n" + p.stderr if p.stderr.strip() else "")).strip().splitlines()
    print("$ %s  (exit %d)" % (" ".join(args[:3]), p.returncode))
    for line in out[-tail:]:
        print("  " + line)
    return p.returncode


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("project")
    ap.add_argument("--folder", required=True)
    a = ap.parse_args()
    proj = Path(a.project) if Path(a.project).is_absolute() else KIT / a.project
    rel = proj.relative_to(KIT).as_posix()
    (proj / "_work").mkdir(exist_ok=True)
    with open(proj / "_work" / "finish.lock", "w") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        fixes = {}
        for f in sorted((proj / "Research").glob("R*/corrections.json"), key=lambda p: int("".join(c for c in p.parent.name if c.isdigit()) or 0)):
            try:
                for rid, change in json.loads(f.read_text(encoding="utf-8")).items():
                    if isinstance(change, dict):
                        fixes.setdefault(rid, {}).update(change)
            except ValueError as e:
                print("unreadable %s: %s" % (f.relative_to(proj), e))
        cpath = proj / "_work" / "corrections.json"
        cpath.write_text(json.dumps(fixes, ensure_ascii=False, indent=1), encoding="utf-8")
        print("corrections: %d rows" % len(fixes))
        bad = 0
        bad |= run(["tools/merge_routes.py", rel, "--corrections", str(cpath)], tail=8) != 0
        bad |= run(["tools/fetch_guarded.py", rel + "/project.json", "--check"], tail=6) != 0
        bad |= run(["tools/fetch_guarded.py", rel + "/project.json"], tail=40) != 0
        bad |= run(["tools/sort_plans.py", rel, "--only", a.folder], tail=6) != 0
    idx = KIT.parent / "Plans" / a.folder / "index.csv"
    if idx.exists():
        lines = list(csv.DictReader(open(idx, encoding="utf-8-sig")))
        print("Plans/%s: %d files (%d vectorized, %d rasterized)" % (
            a.folder, len(lines), sum(x["class"] == "Vectorized" for x in lines), sum(x["class"] == "Rasterized" for x in lines)))
        for x in lines:
            print("  %s  %s" % (x["file"], x["pixel_size"] or ""))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
