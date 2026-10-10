# Completeness critic: Giudecca housing (Gino Valle), routes R1-R7

Date 2026-10-03. Read: `Research/BRIEFING.md`; `manifest.jsonl`, `notes.md` and `leads.md` of R1-R7;
`_work/guard/requests.jsonl` (1,472 lines); `_work/guard/refused_hosts.json` (57 hosts); `_tools/guard.py`.
I also read local files the routes had already saved: OpenAlex JSON in `_work/R5` and `_work/guard/pages/api.openalex.org`,
the saved Docomomo proceedings page, and R1 `album_list.tsv`. This critic sent no web request and ran no search.

## Where the research stands

- 150 manifest rows, 101 of them downloadable. Every downloadable row's `download_url` answered HTTP 200 to a guard `get`.
  - R1 has 83 downloadable rows: 79 photos of original drawings on Flickr ("Gino Valle - Drawings"), mostly the 1984-85 "SE / GT 80" working set, plus 4 exhibition photos.
  - R2 has 11, R3 has 1 and R5 has 6. R4, R6 and R7 have none.
- The Flickr album is the core of the result. Everything else is either low resolution (Censimento plan 800 px; Docomomo "reduced" PDF, about 1000 px) or a pointer to print publications held by libraries.

## 1. What is missing

### Gaps found in the files

1. **A Flickr album of the same account was never opened.** The tumblr `/press` page links the set
   `https://flic.kr/s/aHskwnRLmo`, labelled "Giudecca Social Housing Building (1986)". Its base58 code decodes to album
   **72157665838816838**. That album is not one of the six R1 opened (…739764, …764912, …810832, …965864, …352280,
   …748845). R2 handed it to R1 in its leads; it appears nowhere in R1's files or the request log.
2. **The Flickr photostream was only sampled.** R1 read photostream pages 7-8, which render about 24 of 100 photos each.
   The drawings were uploaded on 17-18 Feb 2018. Sheets SE 1-7, 19, 52, 55, 57, 61, 62 and 67+ are missing from the
   album, so they may sit in the photostream outside any album. Flickr's date-posted archive pages were not tried.
3. **The Flickr album list is incomplete** because of lazy loading: the drawings album itself is not among the 24
   albums that rendered. The `/albums/with/<album id>` view, which renders the list around a given album, was not tried.
4. **Flickr poster photo 41336770664** was handed to R1 by R2 (row r2-0011) and never fetched. The tumblr names
   `c1.staticflickr.com/1/824/41336770664_df709c4261_b.jpg`. It would replace the 700 px copy in r2-0011.
5. **A third-party Flickr photo was never opened.** R7 saw `flickr.com/photos/90472413@N06/14438636474`, titled
   "Gino Valle - quartiere residenziale, ex Area Trevisan … 1980-86". The Pinterest pin R6 could not open has the same
   title, so this photo is probably the pin's source. Hidden Architecture re-posts Flickr ids close to it (14439743815).
6. **casabellaweb.eu issue pages were never read.** The page for no. 478
   (`https://casabellaweb.eu/the-magazine/yearannata-1982-xlvi/cb_cp-478/`, cited by it.wikipedia) would settle
   whether the cover is a Giudecca perspective (rows r5-0006 and r7-0001, both `gv-giudecca-unk`) and the article's end
   page. The guard UA is refused there, but R7 already used a Claude-User WebFetch on this host.
7. **Open copies listed in the saved OpenAlex JSON that no route requested:**
   - "Giudecca" (1996), University of Copenhagen: `https://curis.ku.dk/ws/files/173946681/RoerGiudecca1996.pdf`
     (OpenAlex W7135819657). Content unknown.
   - Teso et al. 2022, a second OSTI record: `https://www.osti.gov/biblio/1962151`. R5 tried only OSTI 1853955, which
     redirects to the 30-minute-blocked escholarship host.
   - The unibz chapter by Ferrando, Favargiotti and Munteanu (2022, CC BY), "Venezia: Complesso residenziale alla
     Giudecca: Unfolding Pavilion 2018". OpenAlex holds only the JavaScript landing page, and the book it belongs to was
     never identified. It is the curators' own text on the complex, so it is the most likely open source of archive
     drawings after Flickr.
8. **Licences not read:**
   - 73 R1 rows carry "All rights reserved (unconfirmed)"; only 19 of 94 photo pages were read.
   - For the CRAU article (r5-0005, r5-0006) R5 fetched only the PDF, not the HTML page
     `https://journals.openedition.org/crau/297` that states the licence.
9. **Publications not checked for an online copy:**
   - Progressive Architecture 2/1988 pp. 32-33 (Smetana, row r7-0014). The US Modernist Library hosts P/A issues; no
     route looked, and its rights statement decides whether a copy may be downloaded.
   - Spanish, Catalan and French open journal archives were never searched: COAM "Arquitectura" on coam.org,
     Quaderns on raco.cat, and Persée / OpenEdition in French.
10. **Search angles no route tried:**
    - student redrawings at the Mendrisio Academy (Atelier Graf), searched directly rather than via exhibition press;
    - the "mat-building / low-rise high-density" literature that redraws the plan;
    - the synonyms "ex cementificio Trevisan" and "Area Trevisan" with "Valle";
    - Japanese;
    - the HAL and Zenodo APIs;
    - D.T. Ferrando's own blog beyond one post.
11. **Bibliography leads found by R3 and R5 but missing from R7's rows:**
    - E. Barbiani (ed.), *Edilizia popolare a Venezia*, Electa 1983. This is IACP's own book, published while the design
      was under way.
    - T. Campostrini (ed.), *Costruire a Venezia*, il Cardo 1993.
    - *Anfione e Zeto* 6-7 (1990-91), a monographic issue on Valle.
12. **Scheme tags that are guesses or that conflict across routes** (fixable locally; see "Manifest fixes").

### Bundle 1: Flickr completion and settling the cheap leads (most valuable)

Flickr pages are fetched only by WebFetch after `check --as claude-user`, and image files by guard check, then get.

1. **Unopened album.** WebFetch `https://www.flickr.com/photos/unfoldingpavilion/albums/72157665838816838`, then the
   `/albums/72157665838816838/with/<first photo id>/` view. Record the title, item count and each item's title and
   image URL. Mark which items are drawings, model photos or building photos. Add a row for every drawing and model
   photo, fetch the files through the guard, and set `same_item_as` against R1's 90 items.
2. **Photostream by upload date.** WebFetch `https://www.flickr.com/photos/unfoldingpavilion/archives/date-posted/2018/02/`,
   then the day pages `.../2018/02/17/` and `.../2018/02/18/`. List every photo id and title. Compare with
   `R1/album_list.tsv` and record anything not in the album, especially SE 1-7, 19, 52, 55, 57, 61, 62, 67+ and further
   "AG" sheets.
3. **Hidden albums.** WebFetch `https://www.flickr.com/photos/unfoldingpavilion/albums/with/72157692795739764`. Record
   every album title not among the 24 already listed in R1 notes item 10, and open any whose title names Valle,
   Giudecca, drawings or the model.
4. **Poster.** WebFetch `https://www.flickr.com/photos/unfoldingpavilion/41336770664/` and record the credit and licence.
   Then check and get `https://live.staticflickr.com/824/41336770664_df709c4261_b.jpg`. Record the pixel size and
   set `same_item_as` = r2-0011.
5. **Third-party photo / Pinterest origin.** WebFetch `https://www.flickr.com/photos/90472413@N06/14438636474/`. Record
   what it shows (building photo, own drawing or scan of a publication), the author and the licence, and whether it is
   the source of Pinterest pin 511510470159568432. Make a row only if it shows a drawing or model and its licence permits
   it. A scan of a magazine page is a lead that cites the magazine.
6. **Casabella 478 and 528.** WebFetch `https://casabellaweb.eu/the-magazine/yearannata-1982-xlvi/cb_cp-478/`. Record
   the cover subject (Valle Giudecca or Siza Malagueira), the table of contents and the Valle article's page range. Then
   re-tag r5-0006 and r7-0001. From the 1986 year page linked at `https://casabellaweb.eu/the-magazine/`, do the same for
   no. 528 (confirm pp. 34-35).
7. **R1 licences.** WebFetch the in-album photo page of each of the 73 drawing items whose licence is unconfirmed
   (URLs in R1 `page_url`). Record the licence line, the description and the upload date in each row. This is the
   lowest-value task in the bundle; do it only if budget remains.

### Bundle 2: open documents nobody opened, and untried search angles

1. **unibz chapter (Ferrando, Favargiotti, Munteanu 2022).** WebSearch
   `"Complesso residenziale alla Giudecca" "Unfolding Pavilion 2018"` together with the authors' names. Record the book
   title, publisher, DOI, licence and any direct file URL (e.g. a `bia.unibz.it/view/delivery/39UBZ_INST/...` address).
   If a direct file URL appears, check and get it, and record the drawing pages with their captions and credits.
2. **Teso et al. 2022, second OSTI copy.** Check, then get, `https://www.osti.gov/biblio/1962151` and
   `https://www.osti.gov/servlets/purl/1962151`. Record whether the Valle complex is one of the ATER case buildings and,
   if so, the pages that carry plans or sections and the licence.
3. **Copenhagen 1996 "Giudecca".** Check, then get, `https://curis.ku.dk/ws/files/173946681/RoerGiudecca1996.pdf`
   (landing page `https://researchprofiles.ku.dk/da/publications/362f1e9b-e298-4e88-a3b6-456d02a51347`). Record the
   author, the kind of document, whether it shows the Valle complex, its drawing pages and the licence.
4. **CRAU licence.** Check, then get, `https://journals.openedition.org/crau/297`. Record the licence line in r5-0005
   and r5-0006.
5. **Progressive Architecture 2/1988.** WebSearch `usmodernist Progressive Architecture 1988`. Read the library's own
   rights statement (about / FAQ page) and find the February 1988 PDF address. Record the address and pp. 32-33
   (Smetana) as a row. The row is `downloadable` only if the site states the rights holder's permission; otherwise it
   is a document pointer.
6. **WebSearch angles, recording each hit with page URL, rights and whether drawings are shown:**
   - (a) `"Franz Graf" OR "Atelier Graf" Mendrisio "Gino Valle" Giudecca ridisegno OR modello`
   - (b) `"Gino Valle" Giudecca logements sociaux plan coupe`
   - (c) `"Gino Valle" Giudecca site:coam.org` and `Giudecca Valle site:raco.cat`
   - (d) `"Gino Valle" Giudecca "mat building" OR "low-rise high-density" plan`
   - (e) `"area ex Trevisan" OR "ex cementificio Trevisan" Valle pianta`
   - (f) `site:dtferrando.eu Giudecca Valle`
   - (g) Japanese: `ジーノ・ヴァッレ ジュデッカ 集合住宅`
7. **Repository APIs not used.** Check, then get,
   `https://api.archives-ouvertes.fr/search/?q=Giudecca%20Valle&fl=title_s,uri_s,fileMain_s&rows=50` and
   `https://zenodo.org/api/records?q=Giudecca%20Valle&size=50`. Record any hit that shows the complex, with its file URL
   and licence.
8. **Older Docomomo proceedings (low priority).** Get
   `https://docomomo.com/wp-content/uploads/2025/09/14-IDC-Proceedings_complete.pdf` and
   `https://docomomo.com/wp-content/uploads/2025/10/Docomomo_proceedings_12th_taitto_s470_comp.pdf`, then run
   `peek.py pdf-text --grep "Giudecca|Gino Valle"`. These volumes are published by the rights holder; record any pages
   that match.

### Not put in the bundles (refused host, login, payment or letter), for the record

- **Hosts that robots.txt closes, or that are refused for good.** Only a person with a browser can open these.
  - e-periodica WBW 74/1987 Heft 3, pp. 56-64 (r6-0008 / r7-0008). This is the best open copy of a 1987 article
    with drawings.
  - archINFORM, Arquitectura Viva, ArchiDiAP, divisare images, ArchDaily images, Google Drive press kit,
    unfoldingpavilion.com, miesbcn.com.
- **Soft refusals.** `escholarship.org` (202), `journal.urbanform.org` and `blogs.cornell.edu` (network), and
  `miesarch.com` (network) are still listed in `refused_hosts.json`. The guard would re-test them after 30 minutes, but
  under this task's instructions they are left out.
- **Library and archive leads** need a visit or a letter: Casabella 478/528, Lotus 51, Domus 678, L'Industria delle
  Costruzioni 186, Edilizia Popolare 168, Graf/Albani 2024, Archivio Studio Valle, ATER and the Comune di Venezia.

### Manifest fixes that need no request

- **R2 model photos at a lower resolution than R1's.** r2-0001..0004 (tumblr `tumblr_pa4awnldjp1xrfamjo1..4`, 640 px,
  "(c) atelier XYZ") are very probably the same four frames as r1-0091..0094 (Flickr album 72157694683764912, photos
  "14".."17", 1600 px). Compare them visually, link `same_item_as`, and keep the 1600 px files.
- **One 1988 model, three tag sets.** It is tagged `gv-giudecca` in R2 (count_as drawing/related), `gv-giudecca-unk`
  in R6 (r6-0003/0004, count_as drawing), and R1 counts its model photos as `related`. It was built in 1988 for the
  Mies award of the completed building, so use `gv-giudecca` and one `count_as` (`related`) throughout.
- **Misused renovation tag.** r6-0006/0007 (Studiospazio "Giudecca Windowsill", installation artworks) are tagged
  `gv-giudecca-reno`, a tag meant for renovation schemes. Tag them like R2's artworks (r2-0006..0008: `gv-giudecca`,
  `related`) or as `other`.
- **1980 design drawings tagged two ways.** r5-0002..0004 (Albani 2021, "Gino Valle Archive 1980") are `gv-giudecca`,
  while r1-0076 ("95 AG", July 1980) is `gv-giudecca-unk`. Compare the 1980 tower plans (r5-0004) with the 1984-85 tower
  sheets SE 36-43 (r1-0048..0054). Then tag both 1980 sources the same way: `gv-giudecca`, or `gv-giudecca-alt` if they
  differ from the built scheme.
- **Unlinked duplicates across routes:**
  - Werk, Bauen + Wohnen: r1-0083 with r6-0008 and r7-0008
  - Domus 678: r1-0080, 0084, 0086, 0089 with r7-0005
  - Lotus 51: r1-0081, 0085 with r7-0003 and r7-0004
  - Modulo 138: r1-0082 with r7-0012
  - L'Architecture d'Aujourd'hui 248: r1-0087, 0090 with r7-0007
  - Electa 2010: r1-0088 with r7-0018
  - Casabella 478 cover: r5-0005, 0006 with r7-0001
  - Censimento plan: r3-0001 probably shows the same drawing as r1-0010 ("0 Plan"); compare them.
- **Add to R7 as document pointers:** Barbiani (ed.) 1983, Campostrini (ed.) 1993, *Anfione e Zeto* 6-7 (1990-91).
- **Lotus 51 page range.** This is not a conflict. Flickr's "pp. 79-128" covers both articles: De Michelis pp. 78/79-94
  and Croset pp. 108/109-128.
- **r4-0001** (PEI 619.0, "Sant'Eufemia 89 alloggi"): R4's own address check points to Le Casette. Keep it as
  `gv-giudecca-unk` with that note, or move it to `other`.

## 2. Rule issues

Each issue below is checked against `requests.jsonl`. "Self-reported" means the route's own Rule log already names it.

| # | Route | URL | Log timestamp(s) | Issue | Status |
|---|---|---|---|---|---|
| 1 | R1 | https://live.staticflickr.com/4670/39440703755_5fdc82ecf3_h.jpg | get http -1 at 18:24:29; re-check 18:25:15; get 200 at 18:25:21 | `get` attempted without a matching check; the guard refused it and sent nothing | self-reported |
| 2 | R1 | 78 check and 49 get entries for live.staticflickr.com | 18:23:02 - 18:24:19 | URLs logged with a trailing CR (read from a CRLF file). The requests reached the right addresses, but log lines do not match the manifest URLs exactly. R1 notes say 79 checks; the log has 78 | self-reported (count differs) |
| 3 | R1 | https://www.flickr.com/photos/unfoldingpavilion/ and https://www.flickr.com/photos/unfoldingpavilion/page9 | check --as claude-user ALLOWED at 18:36:48 and 18:47:44 | No `webfetch-done` follows either check. R1 notes list 36 WebFetches and the log has 36, so most likely no WebFetch was sent; only the agent transcript can confirm | found in log, not in notes |
| 4 | R2 | https://unfoldingpavilion2018.tumblr.com/archive | check --as claude-user ALLOWED at 18:21:30 | No `webfetch-done` follows. Notes list 19 WebFetches and the log has 19, so it is probably unused; the transcript can confirm | found in log, not in notes |
| 5 | R1 | 70 live.staticflickr.com `_h` (1600 px) files | gets 18:23:08 - 18:44 | The sizes pages offer this free account's photos for download only up to 1024 px. The briefing's Flickr clause ("largest size listed on the photo's sizes page, if the owner allows it") points to the `_b` files. Not a guard breach; a decision for the download step | self-reported |
| 6 | R5 | https://api.openalex.org/works?search=%22Gino%20Valle%22&filter=is_oa:true&per-page=100 | check at 18:29:14 (pid 88716); no get line before 18:29:45 | A request was sent with no log line: `guard.py get --out <relative path>` crashed in `out.relative_to()` after fetching. Tool bug; guard.py should resolve `--out` before the request, or log before computing the relative path | self-reported |
| 7 | R3 | MiC Atlante images E22-01..07, then https://atlantearchitetturacontemporanea.cultura.gov.it/en/wp-json/wp/v2/posts/1642 | loop 18:17:39 - 18:17:48, then get at 18:17:49 (HTTP 401) | A further `get` ran after `;` behind a `|| break` loop. That get drew the 401 that closed the host for all routes | self-reported |
| 8 | R3 | Censimento images 8057..8060, then /progetto and /metodologia | loop 18:18:53 - 18:18:58, then gets at 18:18:59 and 18:19:00 | Same form as #7; no effect (all 200) | self-reported |
| 9 | R3 | https://api.europeana.eu/record/v2/search.json?wskey=api2demo&... | www.europeana.eu search refused 18:25:25; api.europeana.eu robots.txt fetched (302) and check refused at 18:26:12 | A second route to a search the site's robots.txt closes. One request (robots.txt) went to the sibling host; borderline under "no mirror" | self-reported |
| 10 | R6 | https://www.zaquadrato.com/robots.txt | zaquadrato.com refused (DNS) at 18:17:24; www. variant checked at 18:17:29 | Sibling hostname tried inside the 30-minute block. Both failed DNS, so nothing reached a server | self-reported |
| 11 | R3 | https://atlantearchitetturacontemporanea.cultura.gov.it/en/wp-json/wp/v2/posts/1642 | 18:17:49 | An unneeded API call drew a 401 and closed a ministry host for every route | self-reported |
| 12 | R5 | several `check` commands | e.g. 18:25:27 - 18:25:30 | Checks shared a Bash command with local greps or appends, never with a get. A form issue against "check as its own command" | self-reported |
| 13 | R7 | https://polovea.sebina.it/SebinaOpac/query/... ; https://opac.biblio.polimi.it/SebinaOpac/query/... ; https://opac.sbn.it/risultati-ricerca-avanzata?monocampo=... | 18:23:21, 18:25:19, 18:26:47, 18:28:02 and later | Catalogue searches sent as GET URLs. Borderline under "never submit a form" | self-reported |
| 14 | R7 | (manifest) | R7 manifest.jsonl written about 18:38 | 28 rows written in one batch instead of as found (rule 6) | self-reported |
| 15 | setup | https://www.dezeen.com/nocheck/ ; www.miesarch.com | get -1 at 18:11:16; `expire_refusal` of www.miesarch.com at 18:10:23, 95 s after its refusal at 18:08:48 | The guard self-test sent nothing. The expiry was manual, not the 30-minute rule. Not a route's act; noted for the guard's audit trail | found in log |

Checked and clean:

- **WebFetch pairing.** All 58 WebFetch entries (R1 36, R2 19, R6 1, R7 2) have an earlier `check --as claude-user`
  ALLOWED for the exact URL and route. R3, R4 and R5 used none, and their notes agree.
- **http -1 gets.** Only #1 above and the setup test.
- **Requests after a refusal.** No get, robots.txt fetch or WebFetch reached a host after its refusal, except the
  re-tests after the 30-minute soft expiry: miesarch.com and www.miesarch.com at 18:41:06/08 (R3), old.atervenezia.it
  at 18:51:37 (R4) and blogs.cornell.edu at 18:55:08 (R6). The rules permit these.
- **Own checks.** Every get had an ALLOWED check of the exact URL by the same route, in an earlier process. Check-to-get
  gaps are 4 s or more; one 2 s gap (R7 architettivalle.net/contatti/, 18:22:11) traced back to R7's own check at
  18:22:06.
- **Community uploads.** No downloadable row is a community upload. Pinterest (R6, 18:17:53), Google Drive (R2,
  18:20:16) and academia.edu (R7, 18:31:56) were only refused at check, after a robots.txt read; nothing was downloaded
  from Pinterest, Scribd, the Internet Archive or Google Books.
- **WebSearch budgets.** Every route stayed within 15: R1 2, R2 11, R3 12, R4 15, R5 15, R6 15, R7 15.

Guard design note, no incident yet (conjecture): `prior_check()` accepts a check from any route. In this run every get
had its own route's check, but the guard does not enforce that.
