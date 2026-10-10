# Briefing: drawings of {NAME}

Plan-research job for `Projects/{NAME}/`. Every route agent reads this file first and follows it exactly. The rules
come from incidents in earlier runs (see `.claude/skills/plan-research/references/incidents.md`); host rules
learned so far are in `.claude/skills/plan-research/references/host-rules.md`; a breach is reported in the route's rule log,
never hidden.

## The building

<!-- The orchestrator fills this section during scoping (step 1 of /plan-research). Keep it factual: -->
- Identity: architect(s), client, address / site, design years, construction years, later works.
- Names in use, in every relevant language (local name, English, transliterations, former names, catalogue titles).
- Known facts to confirm, not to repeat blindly (grid, storeys, structure, plan type).
- Do not confuse it with: neighbours on the same square or street, buildings of the same name, other works of the
  same architect with similar titles. Rows for those are `excluded` with the reason.
- Known publications (catalogue entries only unless an authorised open copy exists).
- Leads found while scoping, with URLs.

## Design ids

| id | Meaning |
|---|---|
| `{SLUG}` | the building as built |
| `{SLUG}-alt` | competition entries, unbuilt schemes, discarded alternatives (research keeps them; the project drops them) |
| `{SLUG}-reno` | later works: renovation, extension, survey of the existing state made for later works |
| `{SLUG}-unk` | the source does not say which state it shows |
| `other` | a different building (with `count_as: excluded` or `related`) |

## What to collect

Drawings of the building: site plans, floor plans (every level), sections, elevations, details, framing / structure
plans, axonometrics, sketches and design-development drawings, measured survey drawings, photos of original drawings
or of the model. Also whole documents (PDF articles, theses, reports, books openly published by their rights holder)
that contain such drawings, with the page numbers. Building photographs are not the target: note good photo sources
in your notes, do not make manifest rows for them.

## Rules (each comes from an incident)

1. **Every request to a web host goes through the guard.** Work from the repository root. Python is `python3`
   (Windows: `py -3`). The project argument is `-p "Projects/{NAME}"`, the route argument `-r <your route id>`.
   - `python3 tools/guard.py -p "Projects/{NAME}" -r R1 check <url> [<url> ...]` as its own Bash command. It prints
     ALLOWED or REFUSED per URL. Then, in a later, separate Bash command:
     `python3 tools/guard.py -p "Projects/{NAME}" -r R1 get <url> --text` (HTML: the `.txt` rendering lists text,
     links and image URLs including srcset/data-src; read that file) or `get <url>` (a file; it lands in
     `_work/guard/pages/<host>/`).
   - Never chain check and get with `&&`, `;` or a loop in one command. Check each exact URL, not one URL per path
     family. After a check command has finished, several `get`s may run in one later command only as a loop that
     stops at the first non-zero exit: `for u in ...; do python3 tools/guard.py ... get "$u" || break; done`.
   - **WebFetch counts as a request.** Use it only when a page needs it (the guard's User-Agent is refused but
     robots.txt lets Claude-User in, or the page is rendered by JavaScript). Before each WebFetch:
     `python3 tools/guard.py -p ... -r R1 check --as claude-user <url>` as its own command; WebFetch only after
     ALLOWED; afterwards `python3 tools/guard.py -p ... -r R1 webfetch-done <url> --result ok` (or the status / error
     shown). Every WebFetch is logged this way, without exception. One WebFetch at a time, never parallel bursts.
   - Never take URLs or image sizes from a WebFetch summary: it reports the displayed thumbnail and has invented URL
     patterns. Read the raw HTML through `guard.py get --text`.
   - **No other HTTP client:** no curl, wget, Python urllib/requests/httpx, no robots helper of your own, no browser
     automation.
   - **A REFUSED is final** for that URL. A 401, 403, 429 or a bot challenge ends the attempt on that host for every
     route (`_work/guard/refused_hosts.json`). No retry, no second client, no other User-Agent, no mirror or alias of
     the same host. Read `_work/guard/refused_hosts.json` before you start on a host.
   - **No redirect is followed automatically.** A REDIRECT line prints the new address; check it as a new URL and get
     it in a later command.
2. **Rights.** Record licence, author, holder and source page for every row. Rights mode for this project:
   `{RIGHTS_MODE}`.
   - `all-reachable` (default for plan research, user decision 2026-10-03): download every copy a script may reach:
     archive and institution files, open-access papers and theses, publication-page scans, blog re-posts, Internet
     Archive uploads with downloadable files, the largest displayed image size. Record provenance honestly
     ("re-post, original source not traced", "community upload").
   - `owner-published`: only material published by its rights holder or with permission (archive, ministry,
     architect's office or estate, exhibition lending from the archive, open-access journal or repository).
     Community uploads of in-copyright books or magazines are leads, not downloads.
   - In both modes, never: shadow libraries and piracy sites (Library Genesis, Z-Library, Anna's Archive, Sci-Hub and
     the like), logins, registrations, payments, CAPTCHAs, forms, lending/borrow items, Google Books page images.
   - Nothing is redistributed. Downloads are private research material.
3. **Never register, log in, pay, submit a form, or write to anyone.** Do not draft letters or e-mails here; a contact
   is a lead (institution, route with URL, what could be asked).
4. **WebSearch budget:** at most {SEARCH_BUDGET} searches per route (a session has about 200 in total; one route
   once used them all up). Search in the local language(s) first, then English.
5. **Viewing files:** render with `python3 tools/peek.py` (`pdf-text --grep` to find drawing pages; `pdf-pages` and
   `sheet` for JPEG previews of at most ~300 kB). Never Read a PNG or a full-size image of more than 1 MB; make a
   sheet first (agents stalled after ~33 large image reads).
6. **Write to disk as you go:** append each row to your manifest the moment you have it and update your notes after
   each source. A run that stops must be resumable from your files.
7. **Status words:** a fact read off a page is `confirmed`; one you infer is `unconfirmed`; one you could not settle
   is `open`. Do not call a guess a reading.
8. **Whole archives are never bulk-scraped.** Take the sheets of this building; a IIIF manifest gives whole images
   (`full/max` or `full/full`), never tiles.

## Your files

`Projects/{NAME}/Research/<route>/`:
- `manifest.jsonl`: one JSON object per line, schema below.
- `notes.md`: sources tried in order (URL, guard result, what was there), findings, and a final section
  `## Rule log` listing every refusal, every WebFetch (URL and result) and any slip of the rules above.
- `leads.md`: what could not be downloaded and where it is (archive, publication and pages, contact route).
- `hand.md`: anything closed to scripts (robots.txt, 403, bot wall, login): the exact URL, what to save and the file
  name to give it, for the user to open in a browser and drop into `Projects/{NAME}/Inbox/`.

## Manifest row schema

```
{"row_id": "r1-0001", "route": "R1",
 "design_id": "{SLUG}" | "{SLUG}-alt" | "{SLUG}-reno" | "{SLUG}-unk" | "other",
 "title": "as captioned or catalogued", "sheet_type": "site|plan|section|elevation|detail|framing|axonometric|perspective|sketch|model|other",
 "contents": "what it shows: which block or wing, which level, scale bar or dimensions visible",
 "format": "raster|vector|pdf", "file_type": "jpg|png|pdf|tif|dwg",
 "download_url": "direct file URL or null", "page_url": "page that shows or links it",
 "pages": null or "PDF page 12 of 140" or "12,13 of 140",
 "pixel_size": "WxH" or null, "scale": "1:200" or null,
 "date": "drawing date or publication date", "author": "...", "holder": "...", "license": "as stated on the page",
 "access": "open|login|paid|archive-only|browser-only",
 "url_status": "checked_ok|redirect|unchecked|404",
 "shows_state": "built|design|competition|renovation|existing-survey|unknown",
 "origin": "original|publication|redraw|photo-of-drawing",
 "downloadable": true|false, "auto_fetch_ok": true|false,
 "count_as": "drawing|document_pointer|3d_model|related|excluded",
 "same_item_as": null, "fetch_rule": "why auto_fetch_ok is false, if it is",
 "evidence": "how you know: guard get result, what you saw in the preview",
 "notes": "..."}
```

- `downloadable` is true only when `download_url` is set, access is `open`, and you have seen the URL answer (a guard
  `get` of that URL, or a WebFetch of a page that embeds it at that exact address).
- `auto_fetch_ok` is true only when `download_url` passed `guard.py check` (the research User-Agent) with ALLOWED.
- One row per image file. For a multi-page PDF that holds drawings, make one `document_pointer` row for the file
  (`pages` lists the drawing pages) and optionally one `drawing` row per drawing page with the same download_url.
- Prefer the largest size the owner exposes (Flickr: the largest size on the photo's sizes page; WordPress: the
  original file without the `-WxH` suffix; srcset: the last, largest variant). Measure the file: the "original"
  may itself be a thumbnail. Under about 2000 px on the long side a sheet is orientation only, not measurement.
- A file you already fetched with `guard.py get` is adopted by the download step; it is not fetched twice.

## Routes

<!-- The orchestrator writes one line per route: id, source classes, start points, search budget. -->
| Route | Source classes | Start points |
|---|---|---|
| R1 | | |
