# Briefing: drawings of the national pavilions of the Venice Biennale

Plan-research job for `Projects/Venice Biennale Pavilions/` (paths are relative to `plan-research-kit/`, the folder
that holds `tools/`; work from there). Every route agent reads this file first and follows it exactly. The rules come
from incidents in earlier runs (see `reference/upstream/research-building-plans/Giudecca_critic.md`,
`Giudecca_rule_audit.md` and `reference/upstream/rekon-sources/references/plan-sources.md`, which also gives the
order of source classes to search); a breach is reported in the route's rule log, never hidden.

## The buildings

The Giardini della Biennale (Castello, Venice) hold 29 national pavilions plus the Central Pavilion, the Venice
Pavilion and the Book Pavilion; Italy's pavilion is in the Arsenale (Tese delle Vergini). One route per pavilion; the
route table at the end gives each pavilion's slug, Plans folder and facts to confirm (leads, not readings).

- Names in use: search every pavilion in Italian ("Padiglione della Germania", "Padiglione Germania ai Giardini"),
  English, the country's own language(s) ("Deutscher Pavillon Venedig", "Павильон России"), and by architect.
- Do not confuse a pavilion with its neighbours in the Giardini, with the same country's exhibitions in other venues
  (palazzi in the city, Arsenale halls), with temporary installations of the same name, or with the 2013 swap of the
  German and French pavilions (Germany exhibited in the French building that year). Rows for those are `other` with
  `count_as: excluded` or `related` and the reason.
- Known shared sources (every route checks the ones that apply to its pavilion): La Biennale di Venezia and its
  historical archive ASAC (asac.labiennale.org); Marco Mulazzani, "I padiglioni della Biennale di Venezia" (Electa,
  1988, 2004, 2014 editions); Wikimedia Commons categories of the Giardini and of each pavilion; IUAV Archivio
  Progetti; Comune di Venezia / Ufficio tecnico; architects' archives and estates; each commissioning body (ministry,
  arts council, foundation) and its call-for-proposals or tender documents, which often carry survey plans of the
  pavilion as PDF or DWG annexes; exhibition sites of past national contributions (installation plans show the
  pavilion plan); ArchDaily, Divisare, Dezeen, Domus, Stylepark, e-flux press kits; university theses.
- Exhibition and installation plans drawn on the pavilion's plan count as drawings of the pavilion
  (`<slug>-reno`, shows_state "existing-survey" or "renovation", notes "exhibition layout <year>").

## Design ids

Per route, with the route's slug (`de` for the German pavilion):

| id | Meaning |
|---|---|
| `<slug>` | the pavilion as built (and its current state) |
| `<slug>-alt` | competition entries, unbuilt schemes, discarded alternatives (kept and downloaded; flagged in file names) |
| `<slug>-reno` | later works: renovation, extension, survey of the existing state, exhibition layouts drawn on the plan |
| `<slug>-unk` | the source does not say which state it shows |
| `other` | a different building (with `count_as: excluded` or `related`) |

## What to collect

Drawings of the pavilion: site plans, floor plans (every level), sections, elevations, details, framing / structure
plans, axonometrics, sketches and design-development drawings, measured survey drawings, exhibition layouts drawn on
the plan, photos of original drawings or of the model; CAD and vector files (DWG, DXF, SVG, vector PDF) wherever they
exist. Also whole documents (PDF articles, theses, reports, catalogues, tender documents) that contain such drawings,
with the page numbers. Building photographs are not the target: note good photo sources in your notes, do not make
manifest rows for them.

## Deliverable

After each batch the orchestrator merges the routes (`tools/merge_routes.py`), downloads every downloadable row
(`tools/fetch_guarded.py`) and sorts the files with `tools/sort_plans.py` into the repository's
`Plans/<folder>/Vectorized/` and `Plans/<folder>/Rasterized/` (the folder is the route's nationality, e.g.
`Plans/german/`). The sorter decides vector or raster by opening each file (a PDF page counts as vector when its
drawing is made of vector paths); your `format` field is a first guess. Make the guess honestly and say in `notes`
when a PDF holds both.

## Leads found while scoping (2026-10-10, WebSearch only; the container could not open them yet)

R1, German pavilion:
- History pages of the pavilion site: https://2013.deutscher-pavillon.org/en/info/geschichte/ and
  https://archiv.deutscher-pavillon.org/2007/english/geschichte.htm (the archive site may list every year's
  contribution; each year's site may carry plans).
- 2014 BBSR call for the general commissioner, possibly with pavilion plans as annex:
  https://baunetz.de/dl/1523705/Bekanntmachungs-_und_Informationsunterlage.pdf
- 2014 Deutscher Werkbund Berlin and Architekturmuseum TU Berlin, 22 architecture offices' proposals for the
  "dilapidated" pavilion (exhibition "This is Modern", Venice 2014; `de-alt` unless a sheet is a survey of the
  existing building): schneider+schumacher https://www.schneider-schumacher.de/wp-content/uploads/pdf/deutscher-pavillon.pdf ;
  https://ingenhovenarchitects.com/news-de-de/news-archiv-de-de/exhibition-this-is-modern-at-architekturmuseum-tu-berlin-de-de/pdf ;
  look for the other 21 and the Architekturmuseum TU Berlin online collection.
- Exhibitions on the plan: 2014 Bungalow Germania https://www.bungalowgermania.de/en/exhibition ; 2016 Making Heimat
  (DAM, makingheimat.de); 2018 Unbuilding Walls (GRAFT); 2022 Maria Eichhorn (excavated the 1909 Donghi pavilion's
  traces inside Haiger's 1938 building: survey drawings likely); 2023 Open for Maintenance (ARCH+, SUMMACUMFEMMER,
  Büro Juliane Greb) https://archplus.net/de/archiv/english-publication/Open-for-Maintenance/ ; 1993 Hans Haacke
  "Germania". Press: https://www.stylepark.com/en/news/germania-in-venezia , deutschland.de, domusweb 2018-02-13,
  e-flux 535809, archdaily 788636.
- Wikipedia "German pavilion" (en/de/it) for references; Ernst Haiger (1938) and Daniele Donghi (1909) as architects.

## Rules (each comes from an incident)

1. **Every request to a web host goes through the guard.** Work from the repository root. Python is `python3`
   (Windows: `py -3`). The project argument is `-p "Projects/Venice Biennale Pavilions"`, the route argument `-r <your route id>`.
   - `python3 tools/guard.py -p "Projects/Venice Biennale Pavilions" -r R1 check <url> [<url> ...]` as its own Bash command. It prints
     ALLOWED or REFUSED per URL. Then, in a later, separate Bash command:
     `python3 tools/guard.py -p "Projects/Venice Biennale Pavilions" -r R1 get <url> --text` (HTML: the `.txt` rendering lists text,
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
2. **Rights: user instruction 2026-10-10, "download ANY accessible files without taking into account the image
   license, since it's a personal project, and don't skip any leads".** Rights mode `all-reachable`, widest form.
   - Download every copy a script may reach: archive and institution files, open-access papers and theses, publication-
     page scans, blog re-posts, Pinterest/tumblr/Flickr images, Internet Archive uploads with downloadable files,
     competition and tender documents, exhibition press kits, the largest displayed image size. The licence is never a
     reason to skip a file. Still record licence (as stated, or "not stated"), author, holder and source page honestly
     ("re-post, original source not traced", "community upload").
   - Never skip a lead: every lead you see is either followed to its end (downloaded, or settled as closed with the
     reason) or written to `leads.md` / `hand.md` with the exact URL. "Probably nothing there" is not a reason.
   - Still never: shadow libraries and piracy sites (Library Genesis, Z-Library, Anna's Archive, Sci-Hub and the like),
     logins, registrations, payments, CAPTCHAs, forms, lending/borrow items, Google Books page images. A host closed
     to scripts (robots.txt, 401/403/429, bot wall) is not forced: it goes to `hand.md` for the user's browser.
   - Nothing is redistributed. Downloads are private research material.
3. **Never register, log in, pay, submit a form, or write to anyone.** Do not draft letters or e-mails here; a contact
   is a lead (institution, route with URL, what could be asked).
4. **WebSearch budget:** at most 8 searches per research route and 4 per gap route (a session has about 200 in total; one route
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

`Projects/Venice Biennale Pavilions/Research/<route>/`:
- `manifest.jsonl`: one JSON object per line, schema below.
- `notes.md`: sources tried in order (URL, guard result, what was there), findings, and a final section
  `## Rule log` listing every refusal, every WebFetch (URL and result) and any slip of the rules above.
- `leads.md`: what could not be downloaded and where it is (archive, publication and pages, contact route).
- `hand.md`: anything closed to scripts (robots.txt, 403, bot wall, login): the exact URL, what to save and the file
  name to give it, for the user to open in a browser and drop into `Projects/Venice Biennale Pavilions/Inbox/`.


## Manifest row schema

```
{"row_id": "r1-0001", "route": "R1",
 "design_id": "<slug>" | "<slug>-alt" | "<slug>-reno" | "<slug>-unk" | "other"  (slug: your route's, see Routes),
 "title": "as captioned or catalogued", "sheet_type": "site|plan|section|elevation|detail|framing|axonometric|perspective|sketch|model|other",
 "contents": "what it shows: which block or wing, which level, scale bar or dimensions visible",
 "format": "raster|vector|pdf"  (vector: DWG/DXF/SVG/AI/EPS or a PDF whose line work is vector paths; raster: JPG/PNG/TIF/GIF/WEBP or a PDF that only holds scanned images; pdf: not yet looked at), "file_type": "jpg|png|pdf|tif|dwg",
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

One research route per pavilion; its gap route is R1xx (R101 for R1, R102 for R2, ...), same slug, same folder.
Research runs five routes at a time in the batch order. The user asked to start with the German pavilion.

| Route | Batch | Slug | Plans folder | Pavilion | Facts to confirm |
|---|---|---|---|---|---|
| R1 | 1 | `de` | `Plans/german/` | German Pavilion (Padiglione della Germania) | Giardini. Built 1909 as Padiglione Bavarese by Daniele Donghi; German from 1912; remodelled 1938 by Ernst Haiger. Many exhibition-era alterations and survey drawings (1993 Haacke, 2014 Bungalow Germania, 2016 Making Heimat, 2018 Unbuilding Walls, 2023 Open for Maintenance). |
| R2 | 1 | `ru` | `Plans/russian/` | Russian Pavilion | Giardini. 1914 by Alexey Shchusev; later renovations. |
| R3 | 1 | `fr` | `Plans/french/` | French Pavilion | Giardini. 1912 by Faust Finzi. |
| R4 | 1 | `gb` | `Plans/british/` | British Pavilion | Giardini. 1887 cafe/tea pavilion (Enrico Trevisanato), converted 1909 by Edwin Alfred Rickards; 2018 'Island' by Caruso St John with Marcus Taylor. |
| R5 | 1 | `us` | `Plans/american/` | United States Pavilion | Giardini. 1930 by Delano & Aldrich; owned by the Solomon R. Guggenheim Foundation since 1986. |
| R6 | 2 | `nl` | `Plans/dutch/` | Dutch Pavilion (Rietveld Pavilion) | Giardini. 1912 pavilion by Gustaf Ferdinand Boberg replaced 1953-54 by Gerrit Rietveld. |
| R7 | 2 | `nordic` | `Plans/nordic/` | Nordic Pavilion (Norway, Sweden, Finland) | Giardini. 1958-62 by Sverre Fehn. |
| R8 | 2 | `fi` | `Plans/finnish/` | Finnish Pavilion (Alvar Aalto Pavilion) | Giardini. 1956 by Alvar Aalto (prefabricated timber); restorations incl. 1976, 1982, 2011. |
| R9 | 2 | `ve` | `Plans/venezuelan/` | Venezuelan Pavilion | Giardini. 1954-56 by Carlo Scarpa. |
| R10 | 2 | `at` | `Plans/austrian/` | Austrian Pavilion | Giardini. 1934 by Josef Hoffmann with Robert Kramreiter; later extension by Hoffmann. |
| R11 | 3 | `jp` | `Plans/japanese/` | Japan Pavilion | Giardini. 1956 by Takamasa Yoshizaka; later renovation works. |
| R12 | 3 | `ch` | `Plans/swiss/` | Swiss Pavilion | Giardini. 1951-52 by Bruno Giacometti. |
| R13 | 3 | `ca` | `Plans/canadian/` | Canada Pavilion | Giardini. 1958 by BBPR; restoration completed 2018. |
| R14 | 3 | `au` | `Plans/australian/` | Australian Pavilion | Giardini. 1988 temporary pavilion by Philip Cox (demolished 2014); 2015 pavilion by Denton Corker Marshall. |
| R15 | 3 | `kr` | `Plans/korean/` | Korean Pavilion | Giardini. 1995 by Seok Chul Kim and Franco Mancuso. |
| R16 | 4 | `be` | `Plans/belgian/` | Belgian Pavilion | Giardini. 1907 by Leon Sneyers (first foreign pavilion); later alterations (Virgilio Vallot). |
| R17 | 4 | `hu` | `Plans/hungarian/` | Hungarian Pavilion | Giardini. 1909 by Geza Rintel Maroti; rebuilt 1958 by Agost Benkhard; later restoration. |
| R18 | 4 | `es` | `Plans/spanish/` | Spanish Pavilion | Giardini. 1922 by Javier de Luque; facade 1952 by Joaquin Vaquero Palacios. |
| R19 | 4 | `cz-sk` | `Plans/czech-and-slovak/` | Czech and Slovak Pavilion | Giardini. 1926 by Otakar Novotny; later alterations. |
| R20 | 4 | `dk` | `Plans/danish/` | Danish Pavilion | Giardini. 1932 by Carl Brummer; extension 1958-60 by Peter Koch. |
| R21 | 5 | `il` | `Plans/israeli/` | Israeli Pavilion | Giardini. 1952 by Zeev Rechter; 1966 alteration by Fritz Janeba; later renovation. |
| R22 | 5 | `gr` | `Plans/greek/` | Greek Pavilion | Giardini. 1934 by M. Papandreou and B. Papadimitriou. |
| R23 | 5 | `uy` | `Plans/uruguayan/` | Uruguayan Pavilion | Giardini. Former storage building, assigned to Uruguay about 1960. |
| R24 | 5 | `br` | `Plans/brazilian/` | Brazilian Pavilion | Giardini. 1964 by Amerigo Marchesin. |
| R25 | 5 | `eg` | `Plans/egyptian/` | Egyptian Pavilion | Giardini (Sant'Elena side). 1932 by Brenno Del Giudice, part of the Padiglione Venezia complex; Egypt from 1952. |
| R26 | 6 | `rs` | `Plans/serbian/` | Serbian Pavilion (former Yugoslav Pavilion) | Giardini. 1930s by Brenno Del Giudice (Yugoslavia). |
| R27 | 6 | `pl` | `Plans/polish/` | Polish Pavilion | Giardini. 1932 by Brenno Del Giudice. |
| R28 | 6 | `ro` | `Plans/romanian/` | Romanian Pavilion | Giardini. 1938 by Brenno Del Giudice. |
| R29 | 6 | `venezia` | `Plans/venetian/` | Venice Pavilion (Padiglione Venezia) | Giardini (Sant'Elena side). 1932 by Brenno Del Giudice; later renovation. |
| R30 | 6 | `it` | `Plans/italian/` | Central Pavilion (former Padiglione Italia) and Padiglione Italia at the Arsenale (Tese delle Vergini) | Giardini Central Pavilion: 1894 Palazzo dell'Esposizione (Enrico Trevisanato), facades 1895/1914/1932, Carlo Scarpa interventions (1948-1968), renovation 2009. Arsenale: Padiglione Italia in the Tese delle Vergini since about 2009-2011. |
| R31 | 7 | `qa` | `Plans/qatari/` | Qatar Pavilion (new permanent pavilion) | Giardini. Lina Ghotmeh selected 2025; state of design or construction to confirm. |
| R32 | 7 | `site` | `Plans/_site/` | Giardini and Arsenale site plans, Book Pavilion (James Stirling, 1991) and other non-national structures | Site plans of the Giardini and the Arsenale; Stirling and Wilford Book Pavilion (Electa bookshop) 1991; Carlo Scarpa ticket booth 1952. |
