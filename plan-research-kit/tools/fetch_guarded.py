"""Run fetch_project.py for a plan-research project with every request going through guard.py.

    PY=python3   (Windows: py -3; run from the repository root)
    $PY tools/fetch_guarded.py "Projects/<Project>/project.json" --check    # first command: robots check of every URL
    $PY tools/fetch_guarded.py "Projects/<Project>/project.json" [--pickup <folder>]   # second command: downloads

fetch_project.py itself is unchanged; the patches are local to this wrapper:
1. download() is guard.Guard.fetch(require_prior=True): no request without an ALLOWED check of the exact URL
   from an earlier command (the --check run), the project's shared refused-hosts list, a per-host lock with the
   largest Crawl-delay (at least 1 s), no redirect followed, and a 401/403/429/bot challenge refuses the host
   with no retry and no browser User-Agent (no hotlink retry).
2. A file that a research route already fetched through guard.py (same URL, HTTP 200, sha256 in the request
   log, the file still in _work/guard/pages) is adopted instead of being requested a second time; the
   sidecar's fetch_note names the route and the time. The candidate copy is removed afterwards.
3. file_name(): a URL name that is all non-ASCII, or whose stem ends in a dot, becomes <row_id>.<ext>
   (Japane101 incidents 2026-09-30 and 2026-10-01: two rows shared one file ".jpg").
"""
import hashlib
import json
import sys
import types
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))

import fetch_project  # noqa: E402
import guard  # noqa: E402

GUARD = None
ADOPTED = []


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def job_urls(cfg_path):
    """The distinct download URLs fetch_project.main() will request, in its order."""
    cfg = json.loads(Path(cfg_path).read_text(encoding="utf-8"))
    proj = Path(cfg_path).resolve().parent
    rows = [json.loads(line) for line in open((proj / cfg["manifest"]).resolve(), encoding="utf-8") if line.strip()]
    designs, drop = set(cfg["designs"]), set(cfg.get("drop_designs", []))
    exclude = cfg.get("exclude_rows", {})
    urls = []
    for r in rows:
        d = set(fetch_project.ids(r["design_id"]))
        if not d & designs or d & drop or r["row_id"] in exclude:
            continue
        take = (r["count_as"] == "drawing" and r["downloadable"] and not r["same_item_as"]) or \
               (r["count_as"] == "document_pointer" and r["downloadable"])
        if take and r["download_url"] not in urls:
            urls.append(r["download_url"])
    return urls


def adoptable(url):
    for e in reversed(GUARD.entries()):
        if e.get("op") == "get" and (e.get("url") or "").strip() == url and e.get("http") == 200 and e.get("out") and e.get("sha256"):
            path = GUARD.proj / e["out"]
            if path.is_file() and sha256(path) == e["sha256"]:
                return path, e
    return None, None


def download(url, net=None, **kw):
    path, e = adoptable(url)
    if path is not None:
        ADOPTED.append(path)
        return 200, path.read_bytes(), "fetched by route %s through guard.py at %s; adopted, not requested again" % (
            e.get("route"), e.get("ts"))
    status, path, note = GUARD.fetch(url, require_prior=True)
    if status == 200:
        body = path.read_bytes()
        path.unlink()
        return 200, body, note
    return status, None, note or ("HTTP %d" % status)


_file_name = fetch_project.file_name


def file_name(url, row):
    host, name = _file_name(url, row)
    stem, dot, ext = name.rpartition(".")
    if dot and (not stem.strip("_") or stem.endswith(".")):
        name = "%s.%s" % (row["row_id"], ext)
    return host, name


def main():
    global GUARD
    argv = [a for a in sys.argv[1:] if a != "--check"]
    cfg = Path(argv[0])
    GUARD = guard.Guard(str(cfg.resolve().parent), "fetch")
    if "--check" in sys.argv:
        urls = job_urls(cfg)
        ok = sum(GUARD.check(u) for u in urls)
        print("%d of %d URLs allowed; run again without --check to download" % (ok, len(urls)))
        return
    fetch_project.download = download
    fetch_project.net_for = lambda: types.SimpleNamespace(counters={"see": "_work/guard/requests.jsonl"})
    fetch_project.file_name = file_name
    sys.argv = [sys.argv[0]] + argv
    fetch_project.main()
    held = {sha256(f) for f in (GUARD.proj / "Downloads").rglob("*")
            if f.is_file() and f.suffix not in (".json", ".csv", ".part")}
    for p in ADOPTED:
        if p.is_file() and sha256(p) in held:
            p.unlink()
            for side in (p.with_name(p.name + ".txt"),):
                if side.exists():
                    side.unlink()


if __name__ == "__main__":
    main()
