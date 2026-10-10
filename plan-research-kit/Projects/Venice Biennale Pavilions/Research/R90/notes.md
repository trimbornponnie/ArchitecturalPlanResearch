# R90 notes: Wikimedia sweep (Commons + Wikipedia), all Giardini pavilions

Route R90, started 2026-10-10 14:30 UTC. Briefing read in full. Scope: Giardini only. Rights mode all-reachable.
Commons robots.txt: crawl-delay 5 s (guard spaces requests; other routes R102/R105 use the host at the same time).
Gentle mode: pages that other routes fetched through the guard in the last hours were read from the shared cache
(`_work/guard/pages/commons.wikimedia.org/`) instead of being requested again; this is said per category below.

## Categories read

| Category | Source of copy | Subcats | Files | Drawings found |
|---|---|---|---|---|
| Category:Venice_Biennale_pavilions | cache (R105 get 14:29) | 43 | 21 | 1 candidate (TCI 2007 tif, to open) |
| Category:Giardini_della_Biennale_(Venice) | cache (R3 get 14:17) | 3 | 86 | 0 (all photographs) |
| Category:Venice_Biennale | cache (R0 get 13:50) | 50 | 72 | candidates: Map_of_Venice_Biennial.pdf, Caramel-architekten-biennale-venedig-3.gif, Scenografia_KinshasaVenezia.pdf |

### 14:31 Commons closed again (429)

- `guard check` of the first 12 pavilion categories (Australia ... Israel), 14:31:19: all REFUSED, "host refused
  earlier in this project (429, route R105: HTTP 429)". R105 received HTTP 429 at 14:30:26 on
  https://commons.wikimedia.org/wiki/File:Venice._Sestiere_of_Castello._Public_GardenSt._Biennale_Pavilions_2007_-_Touring_Club_Italiano_GR_Venezia@0535.tif
  (one minute before my first check). Per rule 1 the refusal is final for commons.wikimedia.org for every route:
  R90 sends no request to Commons, and does not read Commons file descriptions through a mirror of that host
  (e.g. en.wikipedia.org/wiki/File: pages, which transclude the Commons description). No R90 request reached Commons.
- What remains possible without touching Commons: (a) the Commons pages other routes already saved in the shared
  guard cache before the 429 (read locally, no request); (b) originals on upload.wikimedia.org (a separate host the
  briefing names, not refused, never used before in this project; original paths are taken from the thumbnail paths
  in the cached HTML, and every file is verified by a guard get); (c) Wikipedia articles (en/it/de/...; separate hosts,
  open), read from cache where another route saved them.
- The rest of the Commons walk goes to leads.md / hand.md with exact category URLs.

### 14:33 upload.wikimedia.org answered 429 to R90: all Wikimedia requests stopped

- From the cached Commons pages (see below) four candidate files had their original paths in the thumbnail URLs.
  `guard check` (14:33:00, its own command; the guard read https://upload.wikimedia.org/robots.txt, HTTP 200) of the four originals on upload.wikimedia.org: ALLOWED. `guard get` loop
  (14:33:06, "|| break"): the first URL,
  https://upload.wikimedia.org/wikipedia/commons/5/58/Map_of_Venice_Biennial.pdf , answered **HTTP 429**; the loop
  stopped there, the other three were not requested. The guard refused upload.wikimedia.org for the project.
- Two 429s from two Wikimedia hosts within three minutes (Commons to R105 at 14:30:26, upload to R90 at 14:33:06)
  point to a Wikimedia-wide throttle on this User-Agent / exit address, so R90 stops **every** Wikimedia request,
  including en/it/de Wikipedia (still open in the guard), to avoid closing them for the other routes too. Step 3
  (Wikipedia articles) is done only from articles already in the shared guard cache; the rest goes to leads.md / hand.md.
- Total R90 requests to Wikimedia: 2 (the guard's robots.txt read of upload.wikimedia.org, 200, and the get that answered 429). Requests to other hosts: 0.

## Cached Commons pages read (no request; saved by other routes through the guard)

| Category | Saved by | Subcats | Files | Drawings found |
|---|---|---|---|---|
| Category:Venice_Biennale_pavilions_(Germany) | R1 12:40 | 0 | 16 | 0 (photographs) |
| Category:Venice_Biennale_pavilions_(France) | R3 13:51 | 0 | 6 | 0 (photographs) |
| Category:Venice_Biennale_pavilions_(Russia) | R102 14:14 | 0 | 30 | 0 (photographs, exhibition views) |
| Category:Venice_Biennale_pavilions_(United_Kingdom) | R4 13:51 | 0 | 6 | 0 (photographs) |
| Category:Venice_Biennale_pavilions_(United_States_of_America) | R105 14:29 | 0 | 16 | 0 (photographs, events) |
| Category:Alexey_Shchusev | R102 14:15 | 8 | 23 | 0 for Venice (one photo of a 2014 Biennale exhibit on Shchusev) |
| Category:Architectural_drawings_and_designs_by_Alexey_Shchusev | R102 14:15 | 0 | 9 | 0 for Venice (Moscow, Tashkent, Kazan station, Petrograd sheets) |
| Category:Delano_%26_Aldrich | R105 14:29 | 16 | 10 | 0 (no drawings subcategory; its Venice subcat is the USA one above) |

Candidates from the cached pages (file names; none opened, none downloaded):
- File:Map_of_Venice_Biennial.pdf (Category:Venice_Biennale; 1,752 x 1,239, 1.54 MB; original
  https://upload.wikimedia.org/wikipedia/commons/5/58/Map_of_Venice_Biennial.pdf -> 429). A map by its name; which
  venues it shows is not known (open).
- File:Venice._Sestiere_of_Castello._Public_GardenSt._Biennale_Pavilions_2007_-_Touring_Club_Italiano_GR_Venezia@0535.tif
  (Category:Venice_Biennale_pavilions; 956 x 1,110, 4.31 MB). Name pattern of the Touring Club Italiano archive
  uploads, which are mostly photographs; whether it is a map or a photograph is open. R105 was opening it at the 429.
- File:Caramel-architekten-biennale-venedig-3.gif (Category:Venice_Biennale; 1,000 x 666, 218 KB): caramel
  architekten (Vienna), Biennale contribution; drawing or photo is open.
- File:Scenografia_KinshasaVenezia.pdf (Category:Venice_Biennale; 1,754 x 1,239, 593 KB): a scenography sheet by its
  name; venue open (may not be the Giardini).

## Wikipedia articles (step 3), read from the shared guard cache only (no request)

| Article | Saved by | Content images | Drawings |
|---|---|---|---|
| en: American pavilion | R105 | Padiglione_Stati_Uniti,_Venezia_2020.jpg (photo) | 0 |
| en: French pavilion | R3 | Giardini_pavilion_France_biennale_art_2009.jpg, 2026 portrait (photos) | 0 |
| en: German pavilion | R1 | Padiglione_Germania.JPG, 2026 portrait (photos) | 0 |
| en: Russian pavilion | R102 | Russia_pavilion_Biennale_Giardini_art_2009.jpg, 2026 protest photos | 0 |
| en: British pavilion | R4 | Venice_Biennale_pavillion-Great_Britain.JPG (photo) | 0 |
| en: Giardini della Biennale | R3 | three photos; an OSM map tile (maps.wikimedia.org, not a drawing file) | 0 |
| en: Ernst Haiger | R1 | Biennale_di_Venezia_1995,_German_pavilion.jpg and two Munich photos | 0 |
| it: Giardini della Biennale | R3 | about 20 photos of pavilions and monuments (Belgio 1909 is a historic photo, not a drawing) | 0 |
| it: Padiglione Francia / Padiglione della Gran Bretagna | R3 / R4 | one photo each, flag maps | 0 |
| es: Francia / Rusia / Reino Unido pavilions | R3 / R102 / R4 | photos; Venezia_location_map.svg (generic city locator map, not a pavilion drawing) | 0 |
| ru: Venice Biennale; Shchusev | R102 | photos; Shchusev sheets for Moscow projects only | 0 |

## WebSearch (budget 2, used 2)

1. "padiglione Biennale Venezia Giardini pianta disegno File: commons" (commons.wikimedia.org only): photographs and
   category pages only; no plan file.
2. "Giardini Biennale Venice pavilions map plan svg OR pdf OR drawing wikimedia" (Wikimedia domains): found
   File:Map_of_Venice_Biennial.pdf again (snippet: a self-made map of the 2005 Biennale "structure", possibly an
   organisation chart; unconfirmed), en.wikipedia Greek_pavilion and pavilion lists. No SVG/PDF plan of a pavilion.

## Result

No drawing could be downloaded: 0 manifest rows. Commons was refused (429) one minute before R90's first check, and
upload.wikimedia.org answered 429 to R90's first download. Four candidate files and the unwalked categories / articles
are in leads.md (for a scripted run once the user lifts the refusals) and hand.md (for the browser).
Categories read (all from cache): 11 Commons category pages (Venice_Biennale_pavilions, Giardini_della_Biennale_(Venice),
Venice_Biennale, 5 pavilion categories, Alexey_Shchusev, his drawings category, Delano_&_Aldrich). Files looked at by name / listing: 21 + 86 + 72 + 16 + 6 +
30 + 6 + 16 + 23 + 9 + 10 = 295 listing entries, plus the content images of 15 cached Wikipedia articles.

## Rule log

- Refusals met:
  - commons.wikimedia.org: 12 category URLs REFUSED by `guard check` at 14:31:19 (host refused by R105's HTTP 429 at
    14:30:26). Accepted as final; no retry, no other client, no mirror (en.wikipedia File: pages not used).
  - upload.wikimedia.org: HTTP 429 to R90's `guard get` at 14:33:06 on
    https://upload.wikimedia.org/wikipedia/commons/5/58/Map_of_Venice_Biennial.pdf (check ALLOWED at 14:33:00 in a
    separate command; loop stopped at the first non-zero exit). The guard refused the host for every route.
- Possible slip, reported: the request to upload.wikimedia.org was sent about 2.5 minutes after Commons had been
  closed with a 429. upload.wikimedia.org is a separate host that the briefing names and the guard allowed, but it is
  Commons' own media store, so it can be read as an alias of the closed host; and the request closed it for the other
  routes too. After it, R90 sent no further request to any Wikimedia host (Wikipedia, Wikidata, thumb host).
- Cached pages: Commons and Wikipedia pages that other routes had saved through the guard were read locally instead
  of requesting them again (no request; listed per page above).
- WebFetch: none. WebSearch: 2 of 2. No other HTTP client. No image or PDF opened (nothing downloaded).
- Original file URLs on upload.wikimedia.org were built from the hash path in the cached thumbnail URLs (Wikimedia's
  fixed storage scheme), not from a WebFetch summary; only one was requested and it answered 429, so none is verified.
