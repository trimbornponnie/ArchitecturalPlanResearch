# Briefing: drawings of Stahl House

Plan-research job for `Projects/Stahl House/` (inside `plan-research-kit/`). Every route agent reads this file first
and follows it exactly. The rules come from incidents in earlier runs; host rules learned so far are in
`reference/upstream/research-building-plans/CaseStudyHouse_DOWNLOAD_README.md` (section "Host rules", read it before
your first request) and in the section "Host rules for this project" below. A breach is reported in the route's rule
log, never hidden.

## The building

- Identity: Pierre Koenig (1925-2004), Case Study House No. 22 for Arts & Architecture's Case Study House Program
  (editor John Entenza). Clients C. H. "Buck" and Carlotta Stahl (Buck Stahl's own model and curved early scheme came
  first). Site: 1635 Woods Drive, Hollywood Hills, Los Angeles CA 90069 (Docomomo US gives 1636 by mistake). Design
  1957-59, built 1959-60 (published as finished in A&A June 1960). Structural engineer to confirm (Koenig's houses of
  the time used engineer William Porush; `open`). Still owned by the Stahl family; tours via stahlhouse.com.
  Listings: Los Angeles Historic-Cultural Monument No. 670 (1999-11-09); National Register of Historic Places, ref.
  13000519, listed 2013-07-24 under the Case Study House Program 1945-1966 MPS.
- Names in use: "Stahl House", "Stahl Residence", "Case Study House No. 22", "Case Study House #22", "CSH 22",
  "CSH #22", "Case Study House 22", "Casa Stahl" (es/it/pt), "Haus Stahl" / "Stahl-Haus" (de), "Maison Stahl" (fr).
  Catalogue titles at the Getty: "Case Study House No. 22 (Stahl House)" in the Pierre Koenig papers 2006.M.30.
- Known facts to confirm, not to repeat blindly: one storey, L-shaped plan (living/dining/kitchen wing and bedroom
  wing joined by a hallway), around a swimming pool on a levelled pad; steel frame on a 20 ft module with steel
  I-beam columns and long-span steel roof deck; cantilevered living room over the hillside; about 2,200 sq ft;
  carport. Status `open` until a drawing shows it.
- Do not confuse it with: Case Study House No. 21 (Walter Bailey House, also Koenig, 9038 Wonderland Park Ave, 1958;
  the Getty CDWA example drawing is CSH 21), other Koenig houses (Koenig House No. 1 and No. 2, Seidel, Johnson,
  Beagles, Iwata, Gantert, Schwartz, Rollins, Oberman), other Case Study Houses, and other buildings named "Stahl".
  Rows for those are `other` + `excluded` (or `related`) with the reason.
- Later works: restoration and repairs of the house by the Stahl family (with Koenig before 2004?), and any later
  survey drawings: design id `csh22-reno`. Buck Stahl's own early (curved) scheme and Koenig's preliminary schemes
  that differ from the built house: `csh22-alt`.
- Known publications (catalogue entries only unless an open copy exists): Arts & Architecture, June 1960 ("Case Study
  House No. 22"; earlier design announcement in 1959 to be checked); Esther McCoy, Modern California Houses: Case
  Study Houses 1945-1962 (Reinhold 1962; the upstream research found an archive.org PDF of about 61 MB); Elizabeth
  A. T. Smith (ed.), Blueprints for Modern Living (MOCA 1989); James Steele & David Jenkins, Pierre Koenig (Phaidon
  1998); Neil Jackson, Pierre Koenig (Taschen 2007); Neil Jackson, Pierre Koenig: A View from the Archive (Getty
  Publications 2009, ISBN 9781606065778 - check whether the Getty Virtual Library offers a free PDF); Bruce Stahl and
  Shari Stahl Gronwald, The Stahl House: Case Study House #22 (Chronicle 2021, with blueprints and sketches);
  Ethel Buisson & Thomas Billard, The Presence of the Case Study Houses (2004); Taschen, Case Study Houses (Smith /
  Gössel).
- Leads found while scoping (2026-10-10, not yet checked with the guard):
  - Draft NRHP nomination: `https://demo2.parks.ca.gov/pages/1067/files/ca_los%20angeles%20county_case%20study%20house%2022_draft.pdf`
    (look for the www.parks.ca.gov / ohp.parks.ca.gov copy too; final nomination on NPGallery, ref. 13000519).
  - `https://jimlochner.com/s/Case-Study-House-No-22.pdf` (unknown content).
  - Getty finding aid: `https://oac.cdlib.org/findaid/ark:/13030/kt4h4nf4b3/entire_text/` (OAC sits behind a WAF;
    see host rules). CSH #22 holdings per upstream research: flatfiles 20, 21, 22, 22D; 22A-22C (4 exhibition
    originals); box 1A folders 1-4; box 61* folders 5-6; boxes 45-46 (engineering).
  - SAH Archipedia `https://sah-archipedia.org/node/49189`; Docomomo US `https://docomomo-us.org/register/case-study-house-no-22`;
    LACMA `https://collections.lacma.org/node/212176`; MFAH `https://emuseum.mfah.org/objects/101889/...` (Shulman
    photo); Moderna Museet `https://www.modernamuseet.se/stockholm/en/?p=47499`; Getty podcast pages.
  - artsandarchitecture.com `/houses/` page: the Stahl House row is labelled 27 there (labels are wrong in places;
    find the right per-house excerpt PDF by its content).

## Design ids

| id | Meaning |
|---|---|
| `csh22` | the building as built |
| `csh22-alt` | competition entries, unbuilt schemes, discarded alternatives (research keeps them; the project drops them) |
| `csh22-reno` | later works: renovation, extension, survey of the existing state made for later works |
| `csh22-unk` | the source does not say which state it shows |
| `other` | a different building (with `count_as: excluded` or `related`) |

## What to collect

Drawings of the building: site plans, floor plans (every level), sections, elevations, details, framing / structure
plans, axonometrics, sketches and design-development drawings, measured survey drawings, photos of original drawings
or of the model. Also whole documents (PDF articles, theses, reports, books openly published by their rights holder)
that contain such drawings, with the page numbers. Building photographs are not the target: note good photo sources
in your notes, do not make manifest rows for them.

## Rules (each comes from an incident)

1. **Every request to a web host goes through the guard.** Work from the repository root. Python is `python3`
   (Windows: `py -3`). The project argument is `-p "Projects/Stahl House"`, the route argument `-r <your route id>`.
   - `python3 tools/guard.py -p "Projects/Stahl House" -r R1 check <url> [<url> ...]` as its own Bash command. It prints
     ALLOWED or REFUSED per URL. Then, in a later, separate Bash command:
     `python3 tools/guard.py -p "Projects/Stahl House" -r R1 get <url> --text` (HTML: the `.txt` rendering lists text,
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
   `all-reachable`.
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
4. **WebSearch budget:** at most 15 searches per route (a session has about 200 in total; one route
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

`Projects/Stahl House/Research/<route>/`:
- `manifest.jsonl`: one JSON object per line, schema below.
- `notes.md`: sources tried in order (URL, guard result, what was there), findings, and a final section
  `## Rule log` listing every refusal, every WebFetch (URL and result) and any slip of the rules above.
- `leads.md`: what could not be downloaded and where it is (archive, publication and pages, contact route).
- `hand.md`: anything closed to scripts (robots.txt, 403, bot wall, login): the exact URL, what to save and the file
  name to give it, for the user to open in a browser and drop into `Projects/Stahl House/Inbox/`.

## Manifest row schema

```
{"row_id": "r1-0001", "route": "R1",
 "design_id": "csh22" | "csh22-alt" | "csh22-reno" | "csh22-unk" | "other",
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

## Host rules for this project

On top of the upstream host rules (CaseStudyHouse_DOWNLOAD_README.md, "Host rules"):
- stahlhouse.com: robots.txt `Disallow: /`. Never script it; a page worth saving goes into `hand.md`.
- `PLAN_RESEARCH_CONTACT` is not set on purpose: do not put any e-mail address into a User-Agent or a request.
- Whole A&A or magazine issues are `document_pointer` rows (with the drawing pages in `pages`) plus one `drawing` row
  per drawing page of CSH 22. A whole issue may be fetched with `guard.py get` (the guard stops at 600 MB).
- A file over about 150 MB: make the row, but do not fetch it; note its size in the row.

## Routes

WebSearch budget: 15 per route. Every route writes only into `Projects/Stahl House/Research/<route>/` and reads the
shared guard files. Row ids: `r1-0001`, `r2-0001`, `r3-0001`.

| Route | Source classes | Start points |
|---|---|---|
| R1 | Magazines and books: Arts & Architecture (CSH 22 design announcement 1959 and finished house June 1960, any later A&A mention), other period magazines (House & Home, Architectural Forum, Progressive Architecture, Architectural Record, L'Architecture d'Aujourd'hui, Domus, Bauen + Wohnen, Japanese magazines) on USModernist and archive.org, Esther McCoy's 1962 book and other open books on archive.org (downloadable files only, no borrow items). | artsandarchitecture.com `/houses/` and its per-house excerpt PDFs; `https://www.usmodernist.org/AA/AA-1960-06.pdf` and the 1959 issues; archive.org `sim_arts-architecture_1960-06*`, `usmodernist-AA-1960-06`; archive.org search for McCoy "Modern California Houses". |
| R2 | Official and institutional records: NRHP nomination (NPGallery, NPS, California OHP / parks.ca.gov), LA Historic-Cultural Monument No. 670 file (LA City Planning, HistoricPlacesLA, SurveyLA), LA Conservancy, Docomomo US, SAH Archipedia; museum and archive collections: Getty Research Institute (Pierre Koenig papers 2006.M.30, digitised items, Getty Open Content, Getty Virtual Library free books incl. "Pierre Koenig: A View from the Archive"), LACMA, MoMA, SFMOMA, MOCA, Moderna Museet, Art Institute of Chicago, Canadian Centre for Architecture, Calisphere / UC libraries, LOC (HABS/HALS if any), USC Digital Library; LADBS building records (lead only). | The parks.ca.gov draft nomination; NPGallery search for ref. 13000519 and the CSH MPS 64501100-ish; planning.lacity.gov HCM files; getty.edu research collections search; the Getty finding aid via web.archive.org copies. |
| R3 | Web publications, re-posts, models and CAD: Wikimedia Commons and Wikidata; Wikiarquitectura (es/en), ArchDaily (incl. "AD Classics"), ArchEyes, archINFORM, Arquitectura Viva, Metalocus, Divisare, Plataforma Arquitectura, Afasia, blogs and Tumblr/Flickr re-posts of plans; student and scholarly analyses (theses, papers, open repositories, issuu, Scribd previews are leads only); `jimlochner.com` PDF; free DWG/DXF/PDF plan files; 3D models (Sketchfab, 3D Warehouse, GrabCAD: leads unless openly downloadable without login). | `https://commons.wikimedia.org/wiki/Category:Stahl_House`; `https://es.wikiarquitectura.com/edificio/casa-stahl/`; ArchDaily "AD Classics: Stahl House"; archeyes.com; jimlochner.com PDF; searches in English, Spanish, Italian, German, French. |
