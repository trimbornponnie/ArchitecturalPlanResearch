"""Create a plan-research project folder with project.json and the research briefing.

    python3 tools/new_project.py "<Project Name>" --slug <slug> [--building "<one-line identity>"]
                                 [--rights all-reachable|owner-published] [--searches 15]

Writes, under Projects/<Project Name>/ (refuses if the folder exists):
  project.json            name, building, manifest, design ids, default_design, rights_mode, one catch-all group
  Research/BRIEFING.md    templates/BRIEFING.md with the name, slug, rights mode and search budget filled in
  Inbox/  Downloads/  _work/

The project name is the building's name in plain words ("Eames House"), the slug a short ASCII id ("eames").
Design ids: <slug> (as built), <slug>-alt (unbuilt schemes; dropped from the project, kept in research),
<slug>-reno (later works), <slug>-unk (state not stated; default for rows without a design id).
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("name")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--building", default="")
    ap.add_argument("--rights", choices=["all-reachable", "owner-published"], default="all-reachable")
    ap.add_argument("--searches", type=int, default=15, help="WebSearch budget per route")
    a = ap.parse_args()
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,30}", a.slug):
        sys.exit("slug: lower-case ASCII letters, digits and hyphens, at most 31 characters")
    if re.search(r'[<>:"/\\|?*]', a.name) or a.name.strip() != a.name or a.name.endswith("."):
        sys.exit("project name: no <>:\"/\\|?* characters, no leading/trailing space, no trailing dot")
    proj = ROOT / "Projects" / a.name
    if proj.exists():
        sys.exit("exists: %s" % proj)
    for sub in ("Research", "Inbox", "Downloads", "_work"):
        (proj / sub).mkdir(parents=True)
    s = a.slug
    cfg = {
        "name": a.name,
        "building": a.building,
        "manifest": "manifest.jsonl",
        "designs": [s, s + "-reno", s + "-unk"],
        "drop_designs": [s + "-alt"],
        "drop_reason": "a design scheme that differs from the building as built; research keeps it, the project does not",
        "default_design": s + "-unk",
        "rights_mode": a.rights,
        "exclude_rows": {},
        "groups": [{"folder": "01 Drawings"}],
        "title_strip": [],
    }
    (proj / "project.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    brief = (ROOT / "templates" / "BRIEFING.md").read_text(encoding="utf-8")
    for k, v in (("{NAME}", a.name), ("{SLUG}", s), ("{RIGHTS_MODE}", a.rights), ("{SEARCH_BUDGET}", str(a.searches))):
        brief = brief.replace(k, v)
    (proj / "Research" / "BRIEFING.md").write_text(brief, encoding="utf-8", newline="\n")
    for sub in ("Inbox", "Downloads", "_work"):
        (proj / sub / ".gitkeep").touch()
    print("created %s" % proj.relative_to(ROOT).as_posix())
    print("next: fill 'The building' and 'Routes' in Research/BRIEFING.md")


if __name__ == "__main__":
    main()
