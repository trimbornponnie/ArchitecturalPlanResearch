# Case Study House plan sources: download instructions

This file tells a later session how to fetch every drawing that the research of 2026-09-26 located for the Case Study House program (Arts & Architecture, 1945-1966). The research report is `reports/Case Study House plan sources.md`. The per-researcher notes and manifests in `research_notes/Case Study House plan sources/` are the evidence behind every row; do not edit them.

## Files

| File | What it holds |
|---|---|
| `plan_manifest.jsonl` | The merged manifest, one JSON object per line, 513 rows. This is the file to script against. |
| `plan_manifest.csv` | The same 513 rows and columns, UTF-8 with BOM, for a spreadsheet. List values are JSON-encoded. |
| `building_list.csv` | One row per design (41 designs), ranked, with counts, verdicts, best source and next step. |

Every original key of the 11 researcher manifests is kept unchanged. The merge added these columns:

| Column | Meaning |
|---|---|
| `row_id` | Stable id `<design_id>-NNNN`; a plus sign in a design id becomes `_`, a vertical bar becomes `_or_` (e.g. `csh08-0001`, `csh23a_csh23b_csh23c-0004`, `csh18w_or_csh18e-0001`). |
| `design_id` | Canonical design label (list below). `a+b` = the row covers both designs (shared). `a` vertical-bar `b` (e.g. `csh26t` or `csh26k`) = the source does not say which of the two designs it shows. `program` = covers the whole program. |
| `source_notes` | Notes file(s) the row came from. |
| `source_rows` | `manifest_<name>.jsonl:<line>` of the original row(s), 1-based. |
| `downloadable` | `true` when `download_url` is set, `access` is `open` and `url_status` is `checked_ok` or `redirect` (the definition given for this merge, applied literally). |
| `auto_fetch_ok` | `downloadable` and the host may be fetched by a script (robots.txt allows it, no login). `false` rows need a human in a browser. |
| `count_as` | `drawing` (a sheet, page, figure or file), `document_pointer` (a whole issue, book or thesis whose drawing pages are not itemised), `3d_model`, `related` (a different but related building), `excluded` (wrong file or not this design). |
| `same_item_as` | `row_id` of the preferred copy when this row is another copy of the same item (other host, other researcher, re-upload). Empty for the preferred copy. |
| `fetch_rule` | Host rule that makes `auto_fetch_ok` false. |
| `merge_note` | Why a row was merged, excluded or linked. |

## Canonical design ids

`csh01-1945`, `csh01`, `csh02`, `csh03`, `csh04`, `csh05`, `csh06`, `csh07-1945` (first scheme), `csh07`, `csh08-bridge` (1945 Bridge House), `csh08`, `csh09`, `csh10`, `csh11`, `csh12`, `csh13`, `csh15`, `csh16w` (Walker), `csh16e` (Ellwood, Salzman House, also called CSH 1953), `csh17w`, `csh17e`, `csh18w` (West House), `csh18e` (Fields House), `csh19`, `csh20n` (Neutra, Stuart Bailey House), `csh20b` (Bass House), `csh21n` (Neutra, Huggins House, unbuilt), `csh21k` (Koenig, Walter Bailey House), `csh22`, `csh23a`, `csh23b`, `csh23c`, `csh24`, `csh25`, `csh26t` (Thorne, Harrison House), `csh26k` (Killingsworth, Nugent Pavilion, unbuilt), `csh27`, `csh28`, `csh1950` (Soriano), `csa01`, `csa02`. There is no `csh14`: no source attests a design with that number.

## Which rows to fetch

1. Drawings a script may fetch now (235 rows, 249 distinct downloadable drawings in total):
   `downloadable == true and auto_fetch_ok == true and count_as == "drawing" and same_item_as is null`.
2. Drawings that are downloadable but need a person in a browser (14 rows): the same filter with `auto_fetch_ok == false`. They are the UCSB ADC Omeka images (robots.txt disallows `/files/`) and the Drawing Matter images.
3. Whole issues and books (`count_as == "document_pointer"`, 93 rows): fetch only when the design needs its other articles. Their `pages` field lists pages where archive.org full-text search found the architect's name; these include the contents page and advertisements, so a person or an image check must find the drawing pages.
4. 3D models (`count_as == "3d_model"`): none is openly downloadable. They need a free login (Sketchfab, 3D Warehouse, GrabCAD) or are view-only. Do not register accounts automatically.
5. Catalogue-only rows (`count_as == "drawing"` and `downloadable == false`): paper holdings, paid CAD files, login-only files and unverified URLs. They go into the reproduction requests below, not into a download script.

Many rows share one `download_url` (pages of the same PDF). Download each distinct URL once, then cut pages per row using `pages`. There are 253 distinct URLs across all downloadable rows (including issue pointers).

## Folder layout

Every download belongs to a project, one folder per building, under `Projects/`. Nothing is downloaded into a shared `downloads/` folder (user, 2026-09-26).

```
Research_Building Plans/Projects/<Project Name>/      e.g. Projects/Eames House/
  project.json                        which designs, which rows are excluded and why, sheet groups
  README.md                           what is where, what is missing, rights
  Downloads/<host>/<file>             the files as fetched, e.g. Downloads/tile.loc.gov/habs_ca4169_sheet_00003a.tif
  Downloads/<host>/<file>.json        sidecar: row_ids, download_url, page_url, license, author, holder, date, sha256, bytes, measured size
  Downloads/index.csv                 one line per manifest row of the project: local path, status (ok / exists / manual / refused / excluded / skipped), reason
  Plan set/<NN group>/<seq> <type> - <title> [<source id>].<ext>   hard links into Downloads/, plus single pages cut from PDFs
  Plan set/<Project> plan set.csv     the register, one line per sheet, with the sighting columns
  Plan set/<Project> contact sheet.pdf
  Inbox/                              drop files a person downloaded by hand here; the next fetch run moves them into Downloads/
  _work/                              previews, sighting results, register.json (working files)
```

The project name is the building's name in plain words, not the design id. Keep the original file name where the URL has one. HABS sheets become `habs_<survey>_sheet_<file>`, LOC P&P masters `<collection>_<file>` (e.g. `ppmsca_33529u.tif`), and URLs without a file name `<row_id>.<ext>`. Every file gets a sidecar with licence, author and source URL, as the Rekonstruktion rights rule requires. A project holds only the building as built. Rows of unbuilt schemes go into `drop_designs` or `exclude_rows` of `project.json` with their reason, and stay in the manifest.

The scripts are in `_tools/`. Run them with the Rekonstruktion venv:

```
C:/Users/trimb/Desktop/Rekonstruktion/tools/.venv/Scripts/python.exe _tools/fetch_project.py "Projects/<Project Name>/project.json" [--pickup "%USERPROFILE%/Downloads"]
C:/Users/trimb/Desktop/Rekonstruktion/tools/.venv/Scripts/python.exe _tools/assemble_project.py "Projects/<Project Name>/project.json"
```

`fetch_project.py` is rerunnable. It skips files whose sidecar sha256 matches. It adopts a file that a person saved by hand into the project's `Inbox/` (or into a `--pickup` folder) as `manual`, and it recognises the file by name, or for a PDF by page count and title. `_tools/audit_project.py` checks a project against the manifest: every row accounted for, every file matching its sidecar, the plan set intact.

## Host rules

| Host | Rule |
|---|---|
| tile.loc.gov | HABS CA-2903 masters: `https://tile.loc.gov/storage-services/master/pnp/habshaer/ca/ca4100/ca4169/sheet/000NNa.tif`, NN = 01..13 (00014a returns 404). Sheets 5-8 are 8-bit uncompressed, 138,240,696 bytes each; the others are 1-bit G4, 0.24-0.72 MB. The set is about 560 MB. P&P masters (`.../master/pnp/ppmsc|ppmsca|cph|ds/...u.tif`) were not sized; colour masters of about 11000x6300 px can reach ~200 MB. The server answers ranged GETs (HTTP 206): use them to resume. The `v.jpg` (1024 px) and `r.jpg` (640 px) derivatives are useless for measurement. |
| www.loc.gov | Item, resource and search pages (and `?fo=json`) return a Cloudflare challenge to scripts. Read them in a browser. Catalogue records can be read from the LC SRU server `http://lx2.loc.gov:210/lcdb` (MARCXML). |
| artsandarchitecture.com | Per-house excerpt PDFs `https://artsandarchitecture.com/wp-content/uploads/2026/04/<NN>.pdf` (34 used here, 0.5-44.6 MB). The `/houses/` labels are wrong in places: No. 5 is Whitney R. Smith, not Neutra; "18 Fields House" links `19.pdf` (Knorr); "21 Neutra" links `20-1.pdf` (Neutra No. 20, Dec 1948); the Stahl House row is numbered 27; `25.pdf` is Oct 1962, not Dec; `28.pdf` is Sep 1966, not Sep 1965; `26.pdf` and `26-2.pdf` are swapped. `18-2.pdf` returns 404; `18-1.pdf` (Walker No. 18) exists but is not linked. Whole issues: 119 issues are linked twice, and the `2026/04/` copy is then a 4-page stub (cover, contents, first article); take the `2026/05/` or `2026/09/` copy (full issue, 4-182 MB). robots.txt allows everything except `/wp-content/uploads/wpforms/`. |
| www.usmodernist.org | Whole A&A issues `https://www.usmodernist.org/AA/AA-YYYY-MM.pdf`, 30-45 MB, 3490x4372 px pages with OCR, PDF page = printed page. robots.txt explicitly allows ClaudeBot. Prefer these over the magazine's own issue files. House & Home issues (`/HH/`) are 46-197 MB. |
| archive.org | Mirror `usmodernist-AA-YYYY-MM`; independent microfilm series `sim_arts-architecture_YYYY-MM_*` to 1961-12 at 400 ppi; single leaves at `https://archive.org/download/<id>/<id>_jp2.zip/<id>_jp2%2F<id>_NNNN.jp2`. McCoy 1962 book PDF is about 61 MB. |
| npgallery.nps.gov | `GetAsset/<GUID>` answers HEAD with 404 but GET with 200 (application/pdf). Use GET, never decide on HEAD. The NRHP "site" rows are assessor parcel maps (~7 px/m): they carry no building geometry. |
| media.getty.edu | Three GCI PDFs: 39,207,931 / 37,979,087 / 22,252,350 bytes. Rows point to PDF pages; the vector figures can be extracted with pymupdf. On 2026-09-26 its robots.txt answered HTTP 503 (a Getty 'Service Unavailable' page) on every try, so scripts may not fetch (RFC 9309: an unreachable robots.txt means assume disallow). The old `www.getty.edu/conservation/publications_resources/pdf_publications/pdf/...` copies return 404. Save the three PDFs by hand from the report pages `getty.edu/publications-reports/item/2K7M17`, `2K7M1A` and `2K7M19`. |
| calisphere.org | Use the image URLs `https://calisphere.org/clip/1500x1500/27317/<hash>`; the image server answers scripts. Item pages and all oac.cdlib.org pages sit behind an AWS WAF challenge: read them in a browser, via headless Chrome, or from Wayback copies. |
| www.adc-exhibits.museum.ucsb.edu | robots.txt disallows `/files/`: do not script the image files (the early-program researcher fetched ten of them; the Killingsworth researcher declined; the robots rule wins). The JSON API (`/api/items`, `/api/files?item=N`) is allowed for metadata. Fetch by hand or order scans from ADC. |
| drawingmatter.org / drawingmattercollections.com | The four DMC 2771 images on drawingmatter.org are marked human-only here. The album (107 images) is on drawingmattercollections.com behind Cloudflare, and its robots.txt disallows ClaudeBot: a person must page through it. |
| cdm16296.contentdm.oclc.org | Cranbrook IIIF images `.../full/full/0/default.jpg`, open. |
| aaa.si.edu, www.si.edu, sova.si.edu | Cloudflare 403 to scripts: human browser only. ids.si.edu and edan.si.edu: robots.txt `Disallow: /` for all agents. The robots-clean route to live AAA records is `https://api.si.edu/openaccess/api/v1.0/content/ead_component:sova-aaa-mccoesth-ref422?api_key=<key>` with a free api.data.gov key (also ref423, ref475, ref476). |
| stahlhouse.com | robots.txt `Disallow: /`: never script. |
| 3dwarehouse.sketchup.com, sketchfab.com, grabcad.com, documentos.arq.com.mx | Login-only downloads; 3D Warehouse `/warehouse/download` and arq.com.mx `page.cgi` are disallowed in robots.txt. Never register or log in automatically. |
| archweb.com, bibliocad.com, designscad.com | Paid. Never buy automatically. designscad.com robots.txt sets Crawl-delay 10. |
| www.drawycad.com | The Eames House link serves `BTvillette.dwg` (Parc de la Villette). Row excluded; use the dwgLAB file. |
| web.archive.org | `id_` captures return the raw file (used for the CSH #3 OAC sheet). |
| UCLA Digital Library, HathiTrust | robots.txt disallows ClaudeBot (UCLA) or Cloudflare (HathiTrust); not used. |

## Rate limits

Read robots.txt of every host before the first request. Keep at least 1 s between requests to one host and never run two requests to one host at the same time; honour any stricter crawl-delay (sova.si.edu 1 s, designscad.com 10 s, USC Digital Library 30 s). Send a User-Agent that names the project. Resume large files with ranged GETs instead of restarting. Record the HTTP status of every attempt in the project's `Downloads/index.csv`.

## Rights

| Source | Terms as recorded |
|---|---|
| artsandarchitecture.com | (c) The Travers Family Trusts d.b.a. Arts & Architecture; "private, personal, noncommercial use by individual visitors" only; no redistribution without written permission. |
| USModernist | "Any unauthorized reproduction, publication, further distribution or public exhibition ... is strictly prohibited"; free to read and download. |
| LOC P&P, Work of Charles and Ray Eames | "Publication may be restricted" (Eames Office copyright). |
| LOC HABS CA-2903 | "No known restrictions on publication" (US Government work), not re-read on the blocked item page. |
| NPGallery NRHP/NHL PDFs | US federal records, no licence statement. |
| Getty (GCI PDFs) | (c) J. Paul Getty Trust, free PDF; some figures (c) Eames Office per caption. |
| UCSB ADC, Calisphere | Reproduction beyond fair use requires written permission of the copyright owners / UC Regents. |
| Cranbrook | (c) Cranbrook Educational Community; high-resolution copies via archives@cranbrook.edu. |
| Wikimedia Commons | CC BY-SA 3.0. |
| RiuNet theses | One CC BY-NC-ND, one all rights reserved. |

All of it is private research material for this project. Nothing is redistributed.

## Expected volume

Scripted drawings only (filter 1): about 1.5-3 GB, dominated by tile.loc.gov (HABS ~560 MB plus about 61 unsized P&P TIFFs) and the 34 A&A excerpt PDFs (up to ~0.5 GB). The Getty PDFs add ~100 MB, the McCoy book ~61 MB, NPGallery and LA City PDFs ~0.1 GB, images from CONTENTdm, neutra.org and Calisphere ~0.2 GB. Whole issues (filter 3) add about 75 USModernist A&A issues at 30-45 MB (~2.6 GB) and three House & Home issues (~340 MB). Plan for 5-7 GB if everything is fetched.

## Reproduction requests (not downloadable)

| Archive and contact | Containers | Designs |
|---|---|---|
| UCSB Art, Design & Architecture Museum, Architecture and Design Collection (ADC), adc@museum.ucsb.edu | J. R. Davidson papers (0000127): Drawer 113 FlatFile 7 (45 drawings, 1945 scheme); FlatFile 65, probably Drawer 111 (Mac Fadden house, 9 drawings: plans, sections, elevations, details, 1948); Drawer 113 FlatFile 8 (20 drawings) and Drawer 109 FlatFile 113 (board); Drawer 113 FlatFile 10 (2 drawings); FlatFile 27 and Drawer 109 FlatFile 124 (548 S Barrington, 19 drawings, relation to #11 to be checked) | csh01-1945, csh01, csh11, csh15 |
| UCSB ADC (as above) | Smith and Williams records (0000175): Drawer 100 FlatFile 168 (15 drawings), FlatFile 169 (21 drawings) | csh05, csh12 |
| UCSB ADC (as above) | Thornton M. Abell papers (0000102): Drawer 436 FlatFile 314 and 316 (built house); Drawer 451 FlatFile 29 (first scheme) | csh07, csh07-1945 |
| UCSB ADC (as above) | Edward A. Killingsworth papers (0000148): Drawer 664 FlatFile 855 (39 drawings) and 821 (29), FlatFile 856 (boards); FlatFiles 857-858 (45 sheets), Oversize Roll (Mosher), FlatFile 858b (board), Box 34 Folders 77-78 (specifications); FlatFile 248-248a (36 + 3 sheets); Nugent Pavilion entry to be looked up | csh23a, csh23b, csh23c, csh25, csa02, csh26k |
| UCSB ADC (as above) | John Elgin Woolf papers (0000197): 9554 Hidden Valley Rd alteration drawings (later state); Esther McCoy research papers, archival object 4117 (CSH #2, 1945) | csh17e, csh02 |
| UCLA Library Special Collections, Richard and Dion Neutra Papers (Collection 1179) | Subseries 4.2 folders 1020 (Omega, 2-173), 1019 (Alpha, 2-172), 1047 (Bailey, 2-219), 1046 (Huggins, 2-218), 1079 (Wilkins, related); Subseries 4.1 box 22 folder 4, box 35 folders 1, 3, 6-7, box 2000 folders 9-10 | csh06, csh13, csh20n, csh21n |
| UCLA Library Special Collections, A. Quincy Jones papers (Collection 1692) | Job 5076 612: prelim sketches, floor plans, sections, perspectives, original drawings, job file | csh24 |
| Getty Research Institute, Pierre Koenig papers 2006.M.30, via http://hdl.handle.net/10020/askref | CSH #21: flatfiles 17, 18, 19; box 1 folders 12-14A; box 61* folders 3-4; flatfile 189 and box 16 (1998 restoration). CSH #22: flatfiles 20, 21, 22, 22D; 22A-22C (4 exhibition originals); box 1A folders 1-4; box 61* folders 5-6; boxes 45-46 (engineering) | csh21k, csh22 |
| Cal Poly Pomona, ENV Archives-Special Collections, envspeccoll@cpp.edu (Robert Alexander, ralexander@cpp.edu, 909-979-5596) | Raphael S. Soriano Collection (cpp.ENVarchives.2): flat file FF15 folders 2A-2C and vertical file D26-V79A-F23&24; Craig Ellwood Collection (unitemised) | csh1950, csh16e, csh17e, csh18e |
| Archives of American Art, Esther McCoy papers, reference services (check first in a browser whether the folders are now digitised) | Series 4.1 Box 15 Folder 26 + Roll 49 (CSH #16 blueprints, 1952); Box 15 Folder 27 + Roll 50 (CSH #8 and #9 blueprints, c. 1949); Series 9.3 Box 37 Folder 9 (CSH #19, photographs) | csh16e, csh08, csh09, csh19 |
| UC Berkeley Environmental Design Archives, designarchives@berkeley.edu | Wurster / Wurster, Bernardi & Emmons Collection (1976-2): CSH #3 La Canada entry and 'Orinda 1947' entry | csh03 |
| Arizona State University Library, Design and the Arts Special Collections | Alfred Newman Beadle Collection MS MSS 30, Drawings Folder 10, Map Case RR1 D2 (12 drawings, 1964); Calvin Straub Collection MS MSS 14 Series 2 Items 50-53 (photo panels) | csa01, csh20b |
| The Huntington Library | Buff, Smith & Hensman business and design records (gift of Dennis G. and Lynne L. Smith); ask whether the Bass House and CSH #28 jobs are in it | csh20b, csh28 |
| Cranbrook Archives, archives@cranbrook.edu | Ralph Rapson Papers (2012-01) Folder 52; high-resolution copies of AD.26.33.01-.10 | csh04 |
| Library of Congress, Prints & Photographs Division (Ask a Librarian) | New 400 ppi scans of the CSH #9 originals (now only copy-negative scans); unprocessed lot 2010650189 (8 Saarinen drawings, CSH #9); framing sheets of the Bridge House | csh09, csh08-bridge |
| Eames Foundation (Charles and Ray Eames House Preservation Foundation) / Eames Office | Original sets listed in HABS data p.29: 9 sheets of 1948-10-14 (incl. foundation and framing plans), 5 steel shop sheets, 14 sheets of Jan-Mar 1949, 2 stair sheets; EGA measured drawings | csh08 |
| Drawing Matter (Somerset, UK) | DMC 2771, high-resolution scans of the bound set | csh21n |
| CSH #26 owners, hello@casestudyhouse.com (state the research use; students use a school address) | "1962 CSH26 Drawings"; Thorne's addition plans; Thorne family archive via Docomomo US/Northern California | csh26t |
| Walker family (via architectureforsale.com) | Private set of Walker's CSH #16 plans | csh16w |
| Owner of CSH #21 / Corsini Stark Architects | 2023 structural retrofit construction set | csh21k |
