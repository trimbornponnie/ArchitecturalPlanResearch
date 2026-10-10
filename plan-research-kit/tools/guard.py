"""Guarded web access for plan-research projects. Every request an agent or a script sends for a
project goes through here, so robots.txt, the shared refusal list, the rate limit and the request log cannot
be skipped at one call site while honoured at another.

    PY=python3   (Windows: py -3; run from the repository root)
    $PY tools/guard.py -p "Projects/<Project>" -r <route> check <url> [<url> ...]   # its own command, first
    $PY tools/guard.py -p "Projects/<Project>" -r <route> get <url> [--out FILE] [--text]
    $PY tools/guard.py -p "Projects/<Project>" -r <route> check --as claude-user <url>   # before a WebFetch
    $PY tools/guard.py -p "Projects/<Project>" -r <route> webfetch-done <url> --result ok|403|...
    $PY tools/guard.py -p "Projects/<Project>" -r <route> refuse <host> --code 403 --reason "..."
    $PY tools/guard.py -p "Projects/<Project>" status

Rules (incidents: Japane101 research rounds 2026-10-01..03, memory research-agent-briefing):
- `check` prints "ALLOWED <url>" (exit 0) or "REFUSED <url>: <reason>" (exit 3) for each URL. `get` sends
  nothing unless an earlier `check` of the same URL, run as a separate command (another process), printed
  ALLOWED in the last 60 minutes; it then checks again in-process before the request.
- robots.txt is read the way Google reads it: blank lines ignored, groups with the same agent merged, * and $
  honoured, the longest matching rule wins, Allow wins a tie. A URL must pass the "*" group and every group
  that names an Anthropic agent (ClaudeBot, Claude-User, Claude-SearchBot, anthropic-ai, Claude-Web).
  404/410 means no rules. A robots.txt that answers 401/403/429, 5xx, a bot challenge or a network failure
  refuses the host for the project; one that redirects refuses the URL (use the URL on the target host).
- The largest Crawl-delay in robots.txt, at least 1 s, separates any two requests to one host, across
  processes (lock file per host); there are never two requests to one host at the same time.
- No redirect is followed: a 30x prints its Location and exits 5; check the new URL as a new URL.
- A 401, 403, 429 or a bot challenge refuses the host for the whole project (shared file, all routes see it).
  No retry, no second client, no browser User-Agent.
- A binary that WebFetch saved (an image on a host whose robots.txt admits Claude-User but not the research
  User-Agent) is taken over with `adopt-webfetch <url> --file <saved path>` after its `webfetch-done ... ok`.
- robots.txt per RFC 9309: up to five redirects are followed; a 4xx other than 401/403/429 means no rules.
  A 401 on a content URL fails that URL only; 403, 429 and bot challenges refuse the host.
- WebFetch sends as Claude-User. Before each WebFetch: `check --as claude-user <url>` as its own command
  (judged by the Claude-User group where robots.txt has one, else "*"; it also takes the host's turn), then
  the WebFetch, then `webfetch-done` with the result; a 401/403/429/challenge result refuses the host.
- A network failure, a 5xx or an unexpected 2xx (202 = throttling) refuses the host for 30 minutes for every route;
  the host's robots.txt is then read again.
- Every check, request and refusal is appended to <project>/_work/guard/requests.jsonl with its route.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

RB = Path(__file__).resolve().parent.parent
CONTACT = os.environ.get("PLAN_RESEARCH_CONTACT", "contact-not-set")
UA = "plan-research/0.3 (%s; private architectural research, 1 req/s) python-urllib/%d.%d" % \
     ((CONTACT,) + tuple(sys.version_info[:2]))
CLAUDE_AGENTS = ("claudebot", "claude-user", "claude-searchbot", "anthropic-ai", "claude-web")
CHECK_TTL = 3600
STALE_LOCK = 180
MIN_GAP = 1.0
# Hosts whose published rate limit is stricter than MIN_GAP (seconds between requests; robots.txt Crawl-delay still
# wins when larger). loc.gov JSON API 20 req/min with a 1 h block; LOC MARCXML SRU 30 req/min with a 72 h block
# (loc.gov/apis, read 2026-10-10).
HOST_MIN_GAP = {"www.loc.gov": 3.1, "loc.gov": 3.1, "lx2.loc.gov": 2.1}
MAX_BYTES = 600 * 1024 * 1024
SOFT = "network, 2xx other than 200, 5xx"   # refusals that expire (hard: 401, 403, 429, challenge)
SOFT_EXPIRY = 1800
CHALLENGE = re.compile(r"<title>\s*(just a moment|attention required|access denied|are you a robot|"
                       r"security check|captcha)|challenge-platform|cf-chl-|_incapsula_resource|px-captcha|"
                       r"geo\.captcha-delivery|datadome", re.I)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


OPENER = urllib.request.build_opener(NoRedirect)


def now():
    return dt.datetime.now().isoformat(timespec="seconds")


def safe(s, n=90):
    s = re.sub(r"[^A-Za-z0-9._-]+", "_", s).strip("_.")
    return s[:n] or "x"


class Guard:
    def __init__(self, project, route):
        p = Path(project)
        self.proj = p if p.is_absolute() else (RB / p)
        if not self.proj.is_dir():
            raise SystemExit("project folder not found: %s" % self.proj)
        self.dir = self.proj / "_work" / "guard"
        for sub in ("robots", "locks", "pages"):
            (self.dir / sub).mkdir(parents=True, exist_ok=True)
        self.route = route or "?"
        self.log_path = self.dir / "requests.jsonl"
        self.refused_path = self.dir / "refused_hosts.json"

    # ---- shared files ---------------------------------------------------------------------------------
    def _lock(self, name, stale=STALE_LOCK, wait=900):
        path = self.dir / "locks" / (name + ".lock")
        t0 = time.time()
        while True:
            try:
                fd = os.open(str(path), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(fd, str(os.getpid()).encode())
                os.close(fd)
                return path
            except FileExistsError:
                try:
                    if time.time() - path.stat().st_mtime > stale:
                        path.unlink()
                        continue
                except FileNotFoundError:
                    continue
                if time.time() - t0 > wait:
                    raise SystemExit("lock %s busy for %d s" % (name, wait))
                time.sleep(0.25)

    @staticmethod
    def _unlock(path):
        try:
            path.unlink()
        except FileNotFoundError:
            pass

    def log(self, **entry):
        entry = dict(ts=now(), route=self.route, pid=os.getpid(), **entry)
        lk = self._lock("_log", stale=30, wait=120)
        try:
            with open(self.log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        finally:
            self._unlock(lk)

    def entries(self):
        if not self.log_path.is_file():
            return []
        out = []
        for line in open(self.log_path, encoding="utf-8"):
            try:
                out.append(json.loads(line))
            except ValueError:
                pass
        return out

    def refused(self):
        if self.refused_path.is_file():
            try:
                return json.loads(self.refused_path.read_text(encoding="utf-8"))
            except ValueError:
                return {}
        return {}

    def refuse_host(self, host, code, reason, url=""):
        lk = self._lock("_refused", stale=30, wait=120)
        try:
            data = self.refused()
            if host not in data:
                data[host] = {"code": code, "reason": reason, "route": self.route, "ts": now(), "url": url}
                tmp = self.refused_path.with_suffix(".part")
                tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
                tmp.replace(self.refused_path)
        finally:
            self._unlock(lk)
        self.log(op="refuse_host", host=host, code=code, reason=reason, url=url)

    def forget_host(self, host):
        lk = self._lock("_refused", stale=30, wait=120)
        try:
            data = self.refused()
            old = data.pop(host, None)
            tmp = self.refused_path.with_suffix(".part")
            tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
            tmp.replace(self.refused_path)
        finally:
            self._unlock(lk)
        for f in (self.dir / "robots").glob("*_%s.json" % safe(host)):
            f.unlink()
        self.log(op="expire_refusal", host=host, old=old)

    # ---- host rate --------------------------------------------------------------------------------------
    def _wait_turn(self, host, gap):
        last = self.dir / "locks" / (safe(host) + ".last")
        try:
            t = float(last.read_text())
        except (OSError, ValueError):
            t = 0.0
        rest = t + gap - time.time()
        if rest > 0:
            time.sleep(rest)

    def _done_turn(self, host):
        (self.dir / "locks" / (safe(host) + ".last")).write_text("%.3f" % time.time())

    # ---- robots.txt -----------------------------------------------------------------------------------
    def robots(self, scheme, host):
        """(text or None, note). None with a note = unreadable (refuse)."""
        store = self.dir / "robots" / (safe(scheme + "_" + host) + ".txt")
        meta = store.with_suffix(".json")
        if meta.is_file():
            m = json.loads(meta.read_text(encoding="utf-8"))
            if m.get("text_ok"):
                return store.read_text(encoding="utf-8", errors="replace"), m.get("note", "")
            return None, m.get("note", "unreadable")
        url = "%s://%s/robots.txt" % (scheme, host)
        lk = self._lock(safe(host))
        code, text, note, refuse_code, hops = None, None, "", None, []
        try:
            target = url
            for hop in range(6):
                thost = urllib.parse.urlsplit(target).netloc.lower()
                if hop and thost != host and self.refused().get(thost):
                    note = "robots.txt redirects to %s, a host refused in this project" % thost
                    break
                self._wait_turn(thost, MIN_GAP)
                try:
                    with OPENER.open(urllib.request.Request(target, headers={"User-Agent": UA,
                                                                             "Accept-Encoding": "identity"}),
                                     timeout=30) as r:
                        code = r.status
                        body = r.read(2_000_000)
                        ctype = r.headers.get("Content-Type", "")
                    text = body.decode("utf-8", "replace")
                    if CHALLENGE.search(text[:20000]):
                        text, note, refuse_code = None, "robots.txt answered a bot challenge page", "challenge"
                    elif "html" in ctype.lower() and re.search(r"<html", text[:2000], re.I):
                        note = "robots.txt answered an HTML page (no rules parsed from it)"
                    break
                except urllib.error.HTTPError as e:
                    code = e.code
                    if 300 <= e.code < 400 and e.headers.get("Location") and hop < 5:
                        # RFC 9309 2.3.1.2: follow at least five consecutive redirects for robots.txt
                        target = urllib.parse.urljoin(target, e.headers.get("Location"))
                        hops.append("%d->%s" % (e.code, target))
                        self._done_turn(thost)
                        continue
                    if 300 <= e.code < 400:
                        note, refuse_code = "robots.txt redirects more than five times", "network"
                    elif e.code in (401, 403, 429):
                        note, refuse_code = "robots.txt answered HTTP %d" % e.code, e.code
                    elif 400 <= e.code < 500:
                        # RFC 9309 2.3.1.3: robots.txt "unavailable" (4xx): no rules apply
                        text, note = "", "no robots.txt (HTTP %d): no rules" % e.code
                    else:
                        note, refuse_code = "robots.txt answered HTTP %d (unreachable: assume disallow)" % e.code, e.code
                    break
                except Exception as e:  # noqa: BLE001 - recorded
                    note, refuse_code = "robots.txt unreachable: %s: %s" % (type(e).__name__, e), "network"
                    break
                finally:
                    self._done_turn(thost)
            if hops:
                note = ("redirects %s; " % ", ".join(hops)) + note
        finally:
            self._done_turn(host)
            self._unlock(lk)
        self.log(op="robots", url=url, http=code, note=note)
        if text is not None:
            store.write_text(text, encoding="utf-8")
        meta.write_text(json.dumps({"url": url, "http": code, "text_ok": text is not None, "note": note,
                                    "fetched": now()}, indent=1), encoding="utf-8")
        if refuse_code is not None:
            self.refuse_host(host, refuse_code, note, url)
        return text, note

    @staticmethod
    def groups(text):
        """[(agents, rules, delays)], consecutive user-agent lines opening a group (Google semantics)."""
        out, agents, rules, delays, in_rules = [], [], [], [], False
        for raw in text.splitlines():
            line = raw.split("#", 1)[0].strip()
            if ":" not in line:
                continue
            key, val = [s.strip() for s in line.split(":", 1)]
            key = key.lower()
            if key == "user-agent":
                if in_rules:
                    out.append((agents, rules, delays))
                    agents, rules, delays, in_rules = [], [], [], False
                agents.append(val.lower())
            elif key in ("allow", "disallow"):
                in_rules = True
                if val:
                    rules.append((key, val))
            elif key == "crawl-delay":
                in_rules = True
                try:
                    delays.append(float(val))
                except ValueError:
                    pass
        if agents:
            out.append((agents, rules, delays))
        return out

    @staticmethod
    def _pattern(path):
        rx = "".join(".*" if c == "*" else ("$" if c == "$" and i == len(path) - 1 else re.escape(c))
                     for i, c in enumerate(path))
        return re.compile(rx)

    def verdict(self, text, url, identity=None):
        """(blocking rule or None, crawl delay). identity None: the research User-Agent, which must pass the "*"
        group and every Anthropic-agent group. identity "claude-user": a WebFetch request, judged by the
        Claude-User group if robots.txt has one, else by "*"."""
        u = urllib.parse.urlsplit(url)
        target = (u.path or "/") + ("?" + u.query if u.query else "")
        groups = self.groups(text)
        if identity:
            identities = [[identity]] if any(identity in g[0] for g in groups) else [["*"]]
        else:
            identities = [["*"]] + [[a] for a in CLAUDE_AGENTS if any(a in g[0] for g in groups)]
        delay = max([d for g in groups for d in g[2]] or [0.0])
        for ident in identities:
            rules = [r for g in groups if any(a in g[0] for a in ident) for r in g[1]]
            best = None
            for kind, path in rules:
                if self._pattern(path).match(target):
                    if best is None or len(path) > len(best[1]) or (len(path) == len(best[1]) and kind == "allow"):
                        best = (kind, path)
            if best and best[0] == "disallow":
                return "%s (group %s)" % (best[1], ident[0]), delay
        return None, delay

    def judge(self, url, identity=None):
        """(allowed, reason, delay)."""
        u = urllib.parse.urlsplit(url)
        if u.scheme not in ("http", "https") or not u.netloc:
            return False, "not an http(s) URL", 0
        host = u.netloc.lower()
        ref = self.refused().get(host)
        if ref and (str(ref["code"]) == "network" or str(ref["code"])[:1] in ("2", "5")) and \
                time.time() - dt.datetime.fromisoformat(ref["ts"]).timestamp() > SOFT_EXPIRY:
            self.forget_host(host)          # a network failure or 5xx expires; robots.txt is read again
            ref = None
        if ref:
            return False, "host refused earlier in this project (%s, route %s: %s)" % (
                ref["code"], ref["route"], ref["reason"]), 0
        text, note = self.robots(u.scheme, host)
        if text is None:
            return False, note or "robots.txt unreadable", 0
        rule, delay = self.verdict(text, url, identity)
        delay = max(delay, HOST_MIN_GAP.get(host, 0.0))
        if rule:
            return False, "robots.txt Disallow: %s" % rule, delay
        return True, "robots.txt allows" + ("; crawl-delay %.0f s" % delay if delay else ""), delay

    # ---- commands ---------------------------------------------------------------------------------------
    def check(self, url, identity=None):
        url = url.strip()   # URLs read from a CRLF file kept a trailing CR (R1, 2026-10-03)
        ok, reason, delay = self.judge(url, identity)
        self.log(op="check", url=url, result="allowed" if ok else "refused", reason=reason,
                 identity=identity or "research-ua")
        if ok and identity:
            # WebFetch sends the request itself: take the host's turn now and keep it for 3 s
            host = urllib.parse.urlsplit(url).netloc.lower()
            lk = self._lock(safe(host))
            try:
                self._wait_turn(host, max(MIN_GAP, delay))
                (self.dir / "locks" / (safe(host) + ".last")).write_text("%.3f" % (time.time() + 3))
            finally:
                self._unlock(lk)
        print("%s %s%s%s" % ("ALLOWED" if ok else "REFUSED", url,
                             (" (as %s, for WebFetch)" % identity) if identity else "",
                             "" if ok else ": " + reason), flush=True)
        return ok

    def prior_check(self, url):
        limit = time.time() - CHECK_TTL
        for e in reversed(self.entries()):
            if e.get("op") == "check" and (e.get("url") or "").strip() == url and e.get("pid") != os.getpid() and \
                    e.get("identity", "research-ua") == "research-ua":
                try:
                    t = dt.datetime.fromisoformat(e["ts"]).timestamp()
                except (KeyError, ValueError):
                    continue
                if t < limit:
                    return False
                return e.get("result") == "allowed"
        return False

    def fetch(self, url, out=None, require_prior=True):
        """(status, path or None, note). status: 200, 3xx, 4xx/5xx, -1 refused by the guard, 0 network."""
        url = url.strip()
        if require_prior and not self.prior_check(url):
            self.log(op="get", url=url, http=-1, note="no prior ALLOWED check in a separate command")
            return -1, None, "no prior ALLOWED check of this exact URL in a separate command (run check first)"
        ok, reason, delay = self.judge(url)
        if not ok:
            self.log(op="get", url=url, http=-1, note=reason)
            return -1, None, reason
        u = urllib.parse.urlsplit(url)
        host = u.netloc.lower()
        if out is None:
            base = safe(urllib.parse.unquote(Path(u.path).name) or "index", 70)
            out = self.dir / "pages" / safe(host) / ("%s_%s" % (hashlib.sha1(url.encode()).hexdigest()[:8], base))
        out = Path(out).resolve()   # a relative --out crashed relative_to() after the request (R5, 2026-10-03)
        out.parent.mkdir(parents=True, exist_ok=True)
        lk = self._lock(safe(host))
        status, note, ctype, size, sha = 0, "", "", 0, ""
        try:
            self._wait_turn(host, max(MIN_GAP, delay))
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
                with OPENER.open(req, timeout=60) as r:
                    status = r.status
                    ctype = r.headers.get("Content-Type", "")
                    h = hashlib.sha256()
                    part = out.with_name(out.name + ".part")
                    last_touch = time.time()
                    with open(part, "wb") as f:
                        while True:
                            chunk = r.read(1 << 20)
                            if not chunk:
                                break
                            f.write(chunk)
                            h.update(chunk)
                            size += len(chunk)
                            if size > MAX_BYTES:
                                raise ValueError("body larger than %d bytes; stopped" % MAX_BYTES)
                            if time.time() - last_touch > 10:
                                os.utime(lk)
                                last_touch = time.time()
                    sha = h.hexdigest()
                if not out.suffix and "html" in ctype.lower():
                    out = out.with_name(out.name + ".html")
                part.replace(out)
                if "html" in ctype.lower() or size < 200_000:
                    head = out.read_bytes()[:200_000].decode("utf-8", "replace")
                    if CHALLENGE.search(head):
                        out.unlink()
                        status, note = 403, "200 with a bot-challenge page"
            except urllib.error.HTTPError as e:
                status = e.code
                if 300 <= e.code < 400:
                    note = "redirect to %s (not followed; check it as a new URL)" % e.headers.get("Location")
                elif e.code in (401, 403, 429):
                    note = "HTTP %d" % e.code
                elif e.code == 503 and (e.headers.get("cf-mitigated") or "cloudflare" in str(e.headers.get("Server", "")).lower()):
                    note = "HTTP 503 from a bot wall"
                    status = 403
            except Exception as e:  # noqa: BLE001 - recorded
                status, note = 0, "%s: %s" % (type(e).__name__, e)
                for p in (out.with_name(out.name + ".part"),):
                    if p.exists():
                        p.unlink()
        finally:
            self._done_turn(host)
            self._unlock(lk)
        if status != 200 and out.exists() and not (300 <= status < 400):
            out.unlink()
        if status in (403, 429):
            self.refuse_host(host, status, note or ("HTTP %d" % status), url)
        elif status == 0 or 500 <= status < 600 or 200 < status < 300:
            # a network failure, a 5xx, or an unexpected 2xx (Nabunken answered 202 when throttling,
            # 2026-10-02) stops every route on the host for SOFT_EXPIRY seconds
            note = note or ("HTTP %d" % status)
            self.refuse_host(host, "network" if status == 0 else str(status), note, url)
        self.log(op="get", url=url, http=status, bytes=size, sha256=sha, content_type=ctype,
                 out=(os.path.relpath(out, self.proj) if status == 200 else ""), note=note)
        return status, (out if status == 200 else None), note

    def get(self, url, out=None, text=False):
        status, path, note = self.fetch(url, out)
        if status != 200:
            label = "REFUSED" if status == -1 else "REDIRECT" if 300 <= status < 400 else "HTTP %d" % status
            print("%s %s%s" % (label, url, (": " + note) if note else ""), flush=True)
            return 3 if status == -1 else 5 if 300 <= status < 400 else 6 if status in (403, 429) else 7
        print("OK %s -> %s (%d bytes)" % (url, path, path.stat().st_size), flush=True)
        if text:
            raw = path.read_bytes()
            if raw[:4] == b"%PDF" or not re.search(rb"<(html|body|div|p)\b", raw[:50000], re.I):
                print("not HTML; no text rendering", flush=True)
            else:
                tpath = path.with_name(path.name + ".txt")
                tpath.write_text(render(raw, url), encoding="utf-8")
                print("TEXT %s" % tpath, flush=True)
        return 0


class Page(HTMLParser):
    BLOCK = {"p", "div", "br", "li", "tr", "section", "article", "header", "footer", "figure", "figcaption",
             "table", "ul", "ol", "dd", "dt", "h1", "h2", "h3", "h4", "h5", "h6"}

    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base, self.title, self.text, self.links, self.images, self.meta = base, "", [], [], [], []
        self._skip, self._in_title, self._a = 0, False, None

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag in ("script", "style", "noscript", "svg"):
            self._skip += 1
        if tag == "title":
            self._in_title = True
        if tag == "base" and a.get("href"):
            self.base = urllib.parse.urljoin(self.base, a["href"])
        if tag == "meta":
            k = (a.get("property") or a.get("name") or "").lower()
            if a.get("content") and (k.startswith(("og:", "twitter:", "citation_", "dc.", "dcterms.")) or
                                     k in ("description", "author", "keywords")):
                self.meta.append((k, a["content"]))
        if tag == "link" and a.get("href") and a.get("rel", "").lower() in ("alternate", "canonical", "license"):
            self.links.append((urllib.parse.urljoin(self.base, a["href"]), "[link rel=%s]" % a.get("rel")))
        if tag == "a" and a.get("href"):
            self._a = [urllib.parse.urljoin(self.base, a["href"]), []]
        if tag in ("img", "source"):
            for key in ("src", "data-src", "data-original", "data-lazy-src", "data-full", "data-large-file",
                        "data-orig-file", "data-zoom-image", "data-hi-res"):
                if a.get(key) and not a[key].startswith("data:"):
                    self.images.append((urllib.parse.urljoin(self.base, a[key]), a.get("alt", ""), key))
            for key in ("srcset", "data-srcset"):
                if a.get(key):
                    last = a[key].split(",")[-1].strip().split(" ")[0]
                    if last:
                        self.images.append((urllib.parse.urljoin(self.base, last), a.get("alt", ""), key))
        if tag in self.BLOCK:
            self.text.append("\n")
            if tag[0] == "h" and tag[1:].isdigit():
                self.text.append("#" * int(tag[1:]) + " ")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg") and self._skip:
            self._skip -= 1
        if tag == "title":
            self._in_title = False
        if tag == "a" and self._a:
            self.links.append((self._a[0], " ".join("".join(self._a[1]).split())[:120]))
            self._a = None
        if tag in self.BLOCK:
            self.text.append("\n")

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._skip:
            return
        self.text.append(data)
        if self._a:
            self._a[1].append(data)


def render(raw, url):
    m = re.search(rb'charset=["\']?([A-Za-z0-9_-]+)', raw[:4000])
    enc = m.group(1).decode() if m else "utf-8"
    try:
        doc = raw.decode(enc, "replace")
    except LookupError:
        doc = raw.decode("utf-8", "replace")
    p = Page(url)
    try:
        p.feed(doc)
    except Exception:  # noqa: BLE001 - malformed HTML; keep what was parsed
        pass
    body = re.sub(r"[ \t\r\f\v]+", " ", "".join(p.text))
    body = re.sub(r"\n\s*\n+", "\n\n", body).strip()
    seen, links, imgs = set(), [], []
    for u, t in p.links:
        if u not in seen:
            seen.add(u)
            links.append("%s | %s" % (u, t))
    for u, alt, key in p.images:
        if u not in seen:
            seen.add(u)
            imgs.append("%s | %s | %s" % (u, alt[:120], key))
    return "\n".join(["URL: " + url, "TITLE: " + " ".join(p.title.split())] +
                     ["META %s: %s" % kv for kv in p.meta] +
                     ["", "---- TEXT", body[:300000], "", "---- LINKS (%d)" % len(links)] + links +
                     ["", "---- IMAGES (%d)" % len(imgs)] + imgs) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("-p", "--project", required=True, help="project folder, relative to the repository root")
    ap.add_argument("-r", "--route", default="", help="route or agent name, written into the log")
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("urls", nargs="+")
    c.add_argument("--as", dest="identity", choices=["claude-user"],
                   help="judge for a WebFetch request (Claude-User group, else *)")
    ad = sub.add_parser("adopt-webfetch", help="copy a binary that WebFetch saved into _work/guard/pages and log it")
    ad.add_argument("url")
    ad.add_argument("--file", required=True, help="the path WebFetch reported for the saved binary")
    w = sub.add_parser("webfetch-done", help="log a WebFetch request after it returned")
    w.add_argument("url")
    w.add_argument("--result", required=True, help="ok, or the HTTP status / error the WebFetch reported")
    g = sub.add_parser("get")
    g.add_argument("url")
    g.add_argument("--out")
    g.add_argument("--text", action="store_true", help="also write a text rendering of an HTML page (.txt)")
    r = sub.add_parser("refuse")
    r.add_argument("host")
    r.add_argument("--code", required=True)
    r.add_argument("--reason", required=True)
    r.add_argument("--url", default="")
    sub.add_parser("status")
    args = ap.parse_args()
    gd = Guard(args.project, args.route)
    if args.cmd == "check":
        results = [gd.check(u, args.identity) for u in args.urls]
        sys.exit(0 if all(results) else 3)
    if args.cmd == "get":
        sys.exit(gd.get(args.url, args.out, args.text))
    if args.cmd == "adopt-webfetch":
        url = args.url.strip()
        ok = any(e.get("op") == "webfetch" and (e.get("url") or "").strip() == url and
                 str(e.get("result", "")).lower().startswith("ok") for e in gd.entries())
        if not ok:
            print("REFUSED: no webfetch-done ... --result ok logged for this URL; log the WebFetch first")
            sys.exit(3)
        src = Path(args.file)
        u = urllib.parse.urlsplit(url)
        base = safe(urllib.parse.unquote(Path(u.path).name) or "index", 70)
        out = gd.dir / "pages" / safe(u.netloc.lower()) / ("%s_%s" % (hashlib.sha1(url.encode()).hexdigest()[:8], base))
        out.parent.mkdir(parents=True, exist_ok=True)
        data = src.read_bytes()
        out.write_bytes(data)
        gd.log(op="get", url=url, http=200, bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
               content_type="", out=os.path.relpath(out, gd.proj), note="saved by WebFetch (Claude-User), adopted from %s" % src,
               via="webfetch")
        print("OK %s -> %s (%d bytes, via WebFetch)" % (url, out, len(data)))
        return
    if args.cmd == "webfetch-done":
        gd.log(op="webfetch", url=args.url, result=args.result)
        code = re.match(r"\s*(\d{3})", args.result)
        if (code and code.group(1) in ("403", "429")) or \
                re.search(r"challenge|captcha|cloudflare|forbidden|too many", args.result, re.I):
            gd.refuse_host(urllib.parse.urlsplit(args.url).netloc.lower(), code.group(1) if code else "challenge",
                           "WebFetch: " + args.result, args.url)
            print("host refused for the project")
        print("logged")
        return
    if args.cmd == "refuse":
        gd.refuse_host(args.host.lower(), args.code, args.reason, args.url)
        print("host %s refused for the project" % args.host)
        return
    if args.cmd == "status":
        es = gd.entries()
        by = {}
        for e in es:
            if e.get("op") in ("get", "robots", "webfetch"):
                key = (e.get("route"), urllib.parse.urlsplit(e.get("url", "")).netloc)
                by[key] = by.get(key, 0) + 1
        print("refused hosts:")
        for h, v in sorted(gd.refused().items()):
            print("  %-40s %s  %s  (route %s)" % (h, v["code"], v["reason"], v["route"]))
        print("requests by route and host:")
        for (rt, h), n in sorted(by.items()):
            print("  %-12s %-40s %d" % (rt, h, n))


if __name__ == "__main__":
    main()
