# Briefing: drawings of Gino Valle's IACP housing on the Giudecca

This is a plan-research job in `C:\Users\trimb\Desktop\Research_Building Plans`, not a Rekonstruktion stage. No
rekon command is run and nothing under `Desktop\Rekonstruktion` or `Desktop\Japane101` is written.

## The building

- Gino Valle (1923-2003), public housing for IACP Venezia (Istituto Autonomo Case Popolari; today ATER Venezia) on
  the Giudecca, Venice, on the site of the former Trevisan cement works ("area ex Trevisan"). 94 dwellings.
  Design 1980-84, built 1984-86. Shortlisted for the 1988 Mies van der Rohe Award.
- Names in use: "Case IACP alla Giudecca", "Complesso residenziale IACP alla Giudecca", "Quartiere residenziale alla
  Giudecca", "Nuove abitazioni popolari alla Giudecca", "Edilizia residenziale pubblica alla Giudecca", "94 case di
  Gino Valle alla Giudecca", "Giudecca Social Housing", "Housing on Giudecca", "Wohnanlage auf der Giudecca",
  "Viviendas en la Giudecca".
- Known facts to confirm, not to repeat blindly: C-shaped dwelling plan on a 1.65 x 1.65 m grid, simplex/duplex/triplex
  types, heights stepping from 4 storeys (north) to 2 (south), lanes, portico, campiello and campazzo.
- Do not confuse it with other housing on the Giudecca: Campo di Marte (Siza and others, competition
  1985), the Junghans area (from the late 1990s), Sacca Fisola, the Hotel Giudecca, Molino Stucky. Rows for
  those are `excluded` with the reason.
- Known publications (catalogue entries only unless an authorised open copy exists): P.-A. Croset, "94 case di Gino
  Valle alla Giudecca. Un immenso appartamento collettivo", Casabella 528 (Oct 1986); P.-A. Croset, Lotus
  International 51 (1986) pp. 108-128; E. Ranzani, "Quartiere residenziale alla Giudecca", Domus 678 (Dec 1986)
  pp. 38-53; P.-A. Croset, Gino Valle. Progetti e architetture (Electa 1989).
- Leads found while scoping (2026-10-03): Flickr album "Gino Valle - Drawings" of the Unfolding Pavilion 2018
  (https://www.flickr.com/photos/unfoldingpavilion/albums/72157692795739764; drawings lent by the Gino Valle archive);
  MiC Atlante (images E22-01..07 at /wp-content/uploads/E22-0N_Valle_Giudecca.jpg); MiC Censimento scheda-opera
  id=1404; IUAV Archivio Progetti "petit tour" 22; divisare 338437 (Valle Architetti Associati with Lorenzo and
  Emiliano Zandri / ZA2, "Edilizia residenziale a Giudecca (IACP)", a later intervention); miesarch.com/work/1509;
  Dezeen 2018-06-22; jemolo.com (photos); conoscerevenezia.it; SIUSA producer 52898 (Valle Gino).

## What to collect

Drawings of the building: site plans, floor plans (every level), sections, elevations, details, axonometrics,
dwelling-type plans, sketches and design-development drawings, survey drawings of the existing state made for later
works, and photos of original drawings or of the model. Also whole documents (PDF articles, theses, books openly
published by their rights holder) that contain such drawings, with the page numbers. Building photographs are not
the target: note good photo sources in your notes, do not make manifest rows for them.

Tag every row with the scheme it shows. Research lists every scheme; the project later keeps only the building as
built. Competition entries and discarded alternatives are tagged `gv-giudecca-alt`, not dropped from the research.

## Rules (each comes from an incident; a breach is reported, never hidden)

1. Every request to a web host goes through the guard. Python is always
   `C:/Users/trimb/Desktop/Rekonstruktion/tools/.venv/Scripts/python.exe` (call it PY); work from
   `C:/Users/trimb/Desktop/Research_Building Plans`; the project argument is
   `-p "Projects/Giudecca Housing (Gino Valle)"` and the route argument `-r <your route id>`.
   - `PY _tools/guard.py -p ... -r R1 check <url> [<url> ...]` as its own Bash command. It prints ALLOWED or REFUSED per
     URL. Then, in a later, separate Bash command: `PY _tools/guard.py -p ... -r R1 get <url> --text` (HTML pages:
     the .txt rendering lists text, links and image URLs; read that file, or grep the saved .html) or
     `get <url>` (a file; it lands in `_work/guard/pages/<host>/`). Never chain check and get with `&&`, `;` or a
     loop in one command. Check each exact URL, not one URL per path family. `check` takes many URLs in one
     command (each is judged and logged on its own). After that check command has finished, several `get`
     commands may run in one later command only as a loop that stops at the first non-zero exit
     (`for u in ...; do PY _tools/guard.py ... get "$u" || break; done`); the guard refuses the host for every
     route after a 401/403/429/challenge, and for 30 minutes after a 5xx, a network failure or an unexpected 2xx.
   - WebFetch counts as a request. Use it only when a page needs it (the guard's own UA is refused but the site's
     robots.txt lets Claude-User in, as on www.flickr.com, or the page is rendered by JavaScript). Before each
     WebFetch: `PY _tools/guard.py -p ... -r R1 check --as claude-user <url>` as its own command; WebFetch only after
     it printed ALLOWED; afterwards `PY _tools/guard.py -p ... -r R1 webfetch-done <url> --result ok` (or the status /
     error the WebFetch showed). Every WebFetch call is logged this way, without exception.
   - No other HTTP client: no curl, wget, PowerShell Invoke-WebRequest, Python urllib/requests, no robots helper of
     your own, no browser automation.
   - A REFUSED is final for that URL. A 401, 403, 429 or a bot challenge ends the attempt on that host for every
     route (the guard records it in `_work/guard/refused_hosts.json`; a WebFetch that shows one is recorded by
     `webfetch-done`). No retry, no second client, no other User-Agent, no mirror of the same host. Read
     `_work/guard/refused_hosts.json` before you start on a host.
   - No redirect is followed automatically. A REDIRECT line prints the new address; you may check it as a new URL and
     get it in a later command.
2. Rights. Record licence, author, holder and source page for every row. Never download, and never make a
   `downloadable` row for: community uploads of in-copyright books or magazines (Internet Archive user uploads,
   Scribd, Pinterest pins, blog re-posts of magazine scans, file-sharing sites), Google Books, items behind a login,
   a paywall or "borrow". Those are leads: cite the original publication and page instead. Material published by its
   rights holder or with permission (an archive, a ministry, the architect's successor studio, an exhibition that
   borrowed from the Gino Valle archive, an open-access journal or repository) may be downloaded for private
   research. Nothing is redistributed.
3. Never register, log in, pay, submit a form, or write to anyone. Do not draft letters or e-mails; a contact is a
   lead (institution, route with URL, what could be asked).
4. WebSearch budget: at most 15 searches per route. Search in Italian, English, and where useful German and Spanish.
5. Viewing files: render with `PY _tools/peek.py` (pdf-text with --grep to find drawing pages, pdf-pages and sheet for
   JPEG previews of at most ~300 kB). Never Read a PNG or a full-size image of more than 1 MB; make a sheet first.
6. Write to disk as you go: append each row to your manifest the moment you have it, and update your notes after each
   source. A run that stops must be resumable from your files.
7. Status words: a fact read off a page is `confirmed`; one you infer is `unconfirmed`; one you could not settle is
   `open`. Do not call a guess a reading.

## Your files

`Projects/Giudecca Housing (Gino Valle)/Research/<route>/`:
- `manifest.jsonl`: one JSON object per line, schema below.
- `notes.md`: sources tried in order (URL, guard result, what was there), findings, and a final section
  `## Rule log` listing every refusal, every WebFetch (URL and result) and any slip of the rules above.
- `leads.md`: what could not be downloaded and where it is (archive, publication and pages, contact route).

## Manifest row schema

```
{"row_id": "r1-0001", "route": "R1",
 "design_id": "gv-giudecca" | "gv-giudecca-alt" | "gv-giudecca-reno" | "gv-giudecca-unk" | "other",
 "title": "as captioned or catalogued", "sheet_type": "site|plan|section|elevation|detail|axonometric|perspective|sketch|model|other",
 "contents": "what it shows: which block or dwelling type, which level, scale bar or dimensions visible",
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
- Prefer the largest size the owner exposes (Flickr: the largest size listed on the photo's sizes page, if the
  owner allows it; WordPress: the original file without the -WxH suffix, if it answers).
- A file you already fetched with `guard.py get` will be adopted by the download step; it is not fetched twice.

## Round 2 (user instruction, 2026-10-03 evening): use every available source, skip none

The user said: "use all available sources, never skip any, go back through all the other leads that you skipped".
For round 2 (routes R10 and later) this replaces rule 2 above:

- Download every copy of a drawing, a publication page or a model photo that a script may reach: uncredited blog
  re-posts (Hidden Architecture, Naransa, AtlasFor), Pinterest images, publication-page scans on Flickr or elsewhere,
  Internet Archive uploads whose files can be downloaded (not "borrow" or lending-only items), whole magazine issues on
  USModernist, images on divisare, tumblr, archisearch and similar. Building photos are taken when they sit in a
  source set you are fetching anyway (a Flickr album, a blog post); do not hunt for building photos separately.
- Record rights honestly in each row: `license` as stated, or "not stated"; `origin` "publication" (a page scan),
  "redraw", "photo-of-drawing" or "original"; `notes` says "re-post, original source not traced" or "community upload"
  where that is so. Nothing is redistributed.
- Still never: shadow libraries and piracy sites (Library Genesis, Z-Library, Anna's Archive, Sci-Hub and the like),
  logins, registrations, payments, CAPTCHAs, forms, lending/borrow items.
- Unchanged: every request through the guard; robots.txt decides (the guard now reads it per RFC 9309: up to five
  redirects followed, a 4xx other than 401/403/429 means no rules); a 403, 429 or bot challenge ends the attempt on
  that host with no second client and no other User-Agent; no redirect followed without a new check.
- A host whose robots.txt admits Claude-User but not the research User-Agent: read pages with WebFetch (check --as
  claude-user first, webfetch-done after). An image there may be fetched with WebFetch too; WebFetch saves the binary
  and reports its path; then run `PY _tools/guard.py -p ... -r <route> adopt-webfetch <image url> --file "<saved path>"`
  so the download step can take it over.
- Anything closed to scripts (robots.txt, 403, bot wall, login) goes into `Research/<route>/hand.md`: the exact URL,
  what to save, and the file name to give it, for the user to open in a browser and drop into the project's Inbox/.
- WebSearch budget for round 2: at most 12 searches per route.
