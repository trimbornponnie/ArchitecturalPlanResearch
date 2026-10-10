# R2 notes: official and institutional records (Stahl House, CSH 22)

Started 2026-10-10. Sources tried in order.

## 1. California OHP draft NRHP nomination (parks.ca.gov)

- `https://demo2.parks.ca.gov/pages/1067/files/ca_los%20angeles%20county_case%20study%20house%2022_draft.pdf`
  guard check ALLOWED, get 200, 96,524 bytes, 9 pages, saved
  `_work/guard/pages/demo2.parks.ca.gov/264b230e_ca_los_angeles_county_case_study_house_22_draft.pdf`.
  NPS Form 10-900 draft, prepared by Amanda Seward, Los Angeles Conservancy Modern Committee, January 2009.
  Text only: 0 images on all 9 pages (pdf-text image counts). No drawings, no sketch map; the photo log lists
  six photos by Hans Andamson (sic), 2011-03-31, originals at LA Conservancy, not included in the PDF.
  Facts read (confirmed from the draft text, p.3): one storey, L-shaped, "2,300 square foot"; living-dining and
  kitchen in the short leg, bedrooms and carport in the other; dressing room, master bath and service area at the
  juncture; 20-ft modules / 20-ft grid of columns and beams, 20x20 ft bays; "12-inch I-beam and ... 40-inch
  H-column" (sic, probably 4-inch); overhangs 7-8 ft; steel decking wall to the street; concrete footbridge over
  the pool from carport to entrance; only the kitchen updated. Lat/long N 34.10047 W 118.37022.
  No manifest row (no drawing in the file).
- `https://ohp.parks.ca.gov/pages/1067/files/...draft.pdf` and `https://www.parks.ca.gov/pages/1067/files/...draft.pdf`:
  ALLOWED, get 200, 296,087 bytes each (identical): a 1-page "California State Parks Accessibility Archived
  Document ... only available by request" stub. Not the nomination. The request route
  (parks.ca.gov/DocumentRequest) is a form: not used (rule 3).

## 2. NPGallery final NRHP nomination (ref. 13000519)

- `https://npgallery.nps.gov/AssetDetail/NRIS/13000519` and `/NRHP/AssetDetail/NRIS/13000519`: ALLOWED, get 200
  (text). Two assets: `21b55ed9-5129-4f45-aef5-3067e3e9f11d` (pdf, 4,031,141 bytes) and
  `f7ce8ef5-5543-4b3d-b135-3a9669eda7be` (pdf, 22,151 bytes).
- GetAsset 21b55ed9: ALLOWED, GET 200, 4,031,141 bytes, 28 pages. Saved
  `_work/guard/pages/npgallery.nps.gov/856f9afe_21b55ed9-5129-4f45-aef5-3067e3e9f11d` (no extension; PDF 1.6).
  Contents (contact sheet viewed): form pp.1-10 (prepared by Amanda Seward, LA Conservancy Modern Committee,
  Jan 2009, rev. March 2013); p.8 Google location map; p.11 LA County assessor's map APN 5556-031-003 at 1"=100';
  pp.12-17 six colour photos; pp.18-28 correspondence (NPS evaluation sheet, SHPO letter of 2013-05-29, OHP staff
  report on the MPS, LA Cultural Heritage Commission resolution). No plan/section/elevation of the house.
  Rows r2-0001 (document_pointer) and r2-0002 (assessor's map, site, lot lines only).
- GetAsset f7ce8ef5: ALLOWED, GET 200, 22,151 bytes: 1-page "The PDF file for this National Register record has
  not yet been digitized." placeholder. No row.

## 3. Case Study House Program MPS cover document (NRIS 64501186)

- WebSearch 1: `"Case Study House Program" 1945-1966 Multiple Property Documentation Form npgallery pdf`.
- `https://demo2.parks.ca.gov/pages/1067/files/ca_multiple%20counties_case%20study%20house%20program_mpdf.pdf`:
  ALLOWED, get 200, 541,250 bytes, 40 pages (Word export "NR form for inhouse use", 2013-03-18). Text only (the
  "237 images" per page are shared form resources, no figures). CSH 22 paragraph p.22; list p.36. No drawings.
  No manifest row. Prepared by Peter Moruzzi for the LA Conservancy Modern Committee (Dec 2012, rev. Mar 2013).
- `https://npgallery.nps.gov/AssetDetail/54215cf5-9b1b-45af-875d-d8b965494d0d`: ALLOWED, get 200; MPS 64501186,
  metadata "File Size 22151" (stale).
- `https://npgallery.nps.gov/GetAsset/54215cf5-9b1b-45af-875d-d8b965494d0d`: ALLOWED, guard get logged HTTP 200,
  76,377,088 bytes, application/pdf, saved `_work/guard/pages/npgallery.nps.gov/c9c1b133_54215cf5-...` - but the
  file is TRUNCATED (no xref/trailer/%%EOF; pymupdf repair finds 0 pages). The transfer was cut off. Not re-fetched:
  the 40-page draft shows the cover document has no figures, so drawings of CSH 22 are not expected in it. The
  truncated file should not be adopted. No manifest row.

## 4. LA Historic-Cultural Monument No. 670, Docomomo US, SAH Archipedia, LA Conservancy, HistoricPlacesLA

- WebSearch 2: `"Historic-Cultural Monument" 670 "Case Study House" 22 Stahl Woods Drive planning.lacity` - no
  planning.lacity.gov file; Wikipedia/Docomomo give HCM 670, designated 1999-11-09; Mills Act contract mentioned.
- WebSearch 3: `"1635 Woods Drive" Cultural Heritage Commission OR "council file" OR "Mills Act" lacity pdf` - only
  generic CHC/Mills Act documents on planning.lacity.gov (dcpapi2/meetings/document/...), none for this address.
  The 1999 HCM application/CHC report is not online as far as found: lead (leads.md).
- `https://docomomo-us.org/register/case-study-house-no-22`: check ALLOWED; get answered HTTP 202 (guard: soft
  refusal of docomomo-us.org for 30 min, all routes). Not retried.
- `https://sah-archipedia.org/node/49189`: REFUSED (robots.txt answered HTTP 403): host closed for the project.
  hand.md.
- `https://historicplacesla.org/` and `https://www.historicplacesla.org/`: REFUSED (robots.txt unreachable, TLS
  hostname mismatch on both names). HistoricPlacesLA is a JS app anyway; lead/hand.
- `https://www.laconservancy.org/learn/historic-places/stahl-house-case-study-house-22/`: ALLOWED, get 200
  (text). Photos only (og:image Stahl_TimStreet-Porter.jpg; StahlHouseCanvaEdit.png; Adrian Scott Fine 2017),
  link to the NPS weekly-list copy of the nomination. No drawings.
- `https://www.nps.gov/history/nr/feature/places/pdfs/13000519.pdf`: ALLOWED, REDIRECT to
  `https://www.nps.gov/nr/feature/places/pdfs/13000519.pdf`: ALLOWED, get HTTP 404. (Use NPGallery copy r2-0001.)

## 5. Getty (podcast, CDWA, Getty Publications)

- WebSearch 4: `getty.edu research collections "Case Study House No. 22" Koenig drawing` - no digitised CSH 22
  drawing record; Getty images of CSH 22 are Shulman photos (2004.R.10).
- `https://www.getty.edu/podcasts/art-and-ideas/inside-la-most-iconic-modernist-home-case-study-house-22/`:
  ALLOWED, get 200 (text). Images: four Shulman/colour photos at media.getty.edu IIIF (photo sources, not drawings):
  e6f70357-... (full/5629,), c351b39d-... (book cover), 519b070b-... (full/5393,). Transcript PDF
  `https://media.getty.edu/Text/bd65e014-2f6d-51c7-91b7-379a9b2cc0cc.pdf` (not fetched; text). Content: Buck Stahl
  made a model of the lot from crushed cans and clay with an L-shaped plan, a butterfly roof and a curved wall
  following the road (csh22-alt, original model not located); terrazzo floors not laid for lack of money.
- WebSearch 5: `"Pierre Koenig" "A View from the Archive" Getty Publications virtual library free pdf` - no free copy.
- `https://shop.getty.edu/products/pierre-koenig-a-view-from-the-archive-978-1606065778`: ALLOWED, get 200: book is
  2019 (not 2009), 304 pp., 53 colour and 200 b/w ills, ISBN 978-1-60606-577-8, on sale: not in the Getty Virtual
  Library (that library holds out-of-print titles). Lead.
- `https://www.getty.edu/publications/virtuallibrary/`: ALLOWED, REDIRECT to http://www.getty.edu/publications-reports
  (not followed; not needed after the shop page).
- WebSearch 6: `"2006.M.30" Koenig "Case Study House" 22 drawing Getty Research Institute image` - only the CSH 21
  CDWA example (other building) and the finding aid.
- `https://www.getty.edu/research/publications/electronic_publications/cdwa/examples/127_building_house.html`:
  ALLOWED, REDIRECT to the generic CDWA page (example withdrawn). Not followed.
- `https://web.archive.org/web/2024id_/https://oac.cdlib.org/findaid/ark:/13030/kt4h4nf4b3/entire_text/`: REFUSED
  (robots.txt unreachable: connection reset; soft refusal 30 min).

## 6. LACMA, Moderna Museet

- `https://collections.lacma.org/node/212176` -> REDIRECT `https://lacma.org/art/collections/node/212176` ->
  REDIRECT `https://www.lacma.org/art/collections/node/212176` -> REDIRECT `https://collections.lacma.org/object/133059`
  (each checked ALLOWED before its get): get 200. Julius Shulman, Case Study House #22, 1960 printed later, gelatin
  silver print, gift of the artist and Craig Krull Gallery. Photo, no row.
- `https://www.modernamuseet.se/stockholm/en/?p=47499`: ALLOWED, REDIRECT to `/en/stockholm/?p=47499` (relative).
  Not followed: Koenig biography page of "Time & Place: Los Angeles 1957-1968"; photo/biography only per search
  snippet.

## 7. MoMA, SFMOMA, Art Institute of Chicago

- WebSearch 7: `Pierre Koenig "Case Study House" 22 drawing museum collection SFMOMA OR MoMA OR "Art Institute of
  Chicago" OR "Canadian Centre for Architecture"` - only Shulman photographs: LACMA, MFAH (emuseum.mfah.org objects
  101889, chromogenic print "Case Study House #22 (Playboy)"), NGV Melbourne (work 159841, "Two Girls", gelatin
  silver), Getty 2004.R.10. Photo sources, no rows.
- `https://api.artic.edu/api/v1/artworks/search?q=Pierre%20Koenig&...`: ALLOWED, get 200 (JSON). Top 30 of a fuzzy
  match are all other "Pierre" artists: AIC holds no Koenig work.
- `https://www.sfmoma.org/artist/Pierre_Koenig/`: ALLOWED, get HTTP 404 (no artist page at that slug).
- `https://www.moma.org/collection/?q=Pierre%20Koenig`: ALLOWED, get HTTP 403: moma.org refused for the project
  (all routes). hand.md.

## 8. Getty Research Institute holdings (search), Smithsonian AAA, UCSB ADC

- WebSearch 8: `getty.edu/research/collections "Pierre Koenig papers and drawings" Stahl` - no getty.edu research
  collections page with digitised CSH 22 components; only the OAC finding aid (2006.M.30, 239.6 linear ft, Ann
  Harrison 2010). oac.cdlib.org not requested (upstream: AWS WAF challenge); containers kept as leads.
- WebSearch 9: `"Esther McCoy papers" "Case Study House" 22 Koenig box folder Archives of American Art` - AAA folder
  records for CSH #16 (ref475) and #8/#9 (ref476) only; no CSH 22 folder seen. Also found: UCSB ADC "Esther McCoy
  research papers" (0000103), OAC ark:/13030/c8d21wm4, with reprographic copies of Case Study Houses 1-26 and 1950
  (whether #22 is among them not visible): lead.
- `https://sirismm.si.edu/EADpdfs/AAA.mccoesth.pdf` (AAA EAD PDF of the McCoy papers): ALLOWED, get HTTP 526
  (Cloudflare origin error; soft refusal 30 min). Not retried. si.edu/aaa.si.edu pages not requested (upstream:
  Cloudflare 403, human only).
- `https://www.adc-exhibits.museum.ucsb.edu/api/items?search=Koenig` / `...search=Stahl`: REFUSED (robots.txt
  unreachable: connection reset; soft refusal 30 min). Not retried.

## NOTE for the orchestrator: foreign rows in this manifest

- `r2-0003` and `r2-0004` (A&A June 1960, USModernist AA-1960-06.pdf, document_pointer + p.17 plan) were NOT written by
  R2. They appeared in this file between 15:06 and 15:15 and duplicate R1's own rows `r1-0003` and `r1-0004` (the R1
  agent seems to have appended them to the wrong manifest). Left untouched; treat them as same_item_as r1-0003 /
  r1-0004 (or drop them) at merge. R2's own rows are r2-0001, r2-0002, r2-0005 onward.

## 9. Getty exhibition "Overdrive: L.A. Constructs the Future, 1940-1990" (2013), CCA, Cooper Hewitt

- WebSearch 10: `Getty Iris blog Pierre Koenig archive Stahl House drawing sketch Case Study House #22` - pointed to
  the Neil Jackson podcast page and Iris posts.
- `https://blogs.getty.edu/iris/?p=45390`: REFUSED (robots.txt Disallow: / for *). Not requested.
- `https://www.getty.edu/podcasts/art-and-ideas/pierre-koenig-modernist-la-homes` -> REDIRECT to the same path with
  trailing slash: checked ALLOWED, get 200 (text). Only the book-cover image (IIIF 6ecb3db7-..., full/3000,) and a
  transcript PDF. No drawing.
- `https://www.getty.edu/art/exhibitions/overdrive/`: ALLOWED, get 200 (text). Links to section pages.
- `https://www.getty.edu/art/exhibitions/overdrive/residential_fabric.html`: ALLOWED, get 200 (text). Shows
  "Case Study House 22 (Stahl House) by Pierre F. Koenig, West Hollywood, construction completed 1960. Drawing, 1960.
  The Getty Research Institute" = `images/r31089_2006_m_30_ff22c_001.jpg` (displayed 720x388).
- `https://www.getty.edu/art/exhibitions/overdrive/images/r31089_2006_m_30_ff22c_001.jpg`: ALLOWED, get 200,
  173,191 bytes, JPEG 720x388. Viewed: Koenig's ink perspective of the cantilevered living-room end, signed. Row
  r2-0005. File name = GRI image r31089 of 2006.M.30 flatfile 22C item 001 (one of the exhibition originals).
- `https://collection.cooperhewitt.org/search/collection/?query=Pierre%20Koenig`: REFUSED (redirects to si.edu;
  robots 403). Not requested.
- `https://www.cca.qc.ca/en/search?query=Pierre%20Koenig`: ALLOWED, get 200 (text). 24 results, all library records
  (Jackson 2019; Steele/Jenkins 1998; Koenig vertical file; "The Steel frame in the architecture of Pierre Koenig: a
  selected bibliography"; Bradbury, The iconic house; Pardey 20/20). No CCA archival drawings of CSH 22.

- `http://news.getty.edu/press_materials.cfm` (Overdrive press kit): ALLOWED, REDIRECT to
  `https://news.getty.edu:443/press_materials.cfm`: ALLOWED, REDIRECT to `https://www.getty.edu/404.html` (dead).

## 10. Calisphere / USC / LOC search; Getty research collections data service

- WebSearch 11: `"Case Study House" 22 OR "Stahl House" Koenig drawing OR plan site:calisphere.org OR
  site:digitallibrary.usc.edu OR site:loc.gov` - one hit: Calisphere item
  `https://calisphere.org/item/3a87c1e938853b3cf07b1d5293574171` (USC Architectural Teaching Slide Collection,
  "Stahl residence", 1635 Woods Drive, CSH #22, 1960, source credited to Pierre Koenig; thumbnail on the USC digital
  library). Whether the slide shows a drawing or a photo is not known. Calisphere item pages are behind an AWS WAF
  (upstream rule) - not requested; Wayback copy to try. No LOC hit; the NRHP form lists no HABS/HAER/HALS number.
- `https://www.getty.edu/research/collections/search?q=Case%20Study%20House%2022%20Koenig`: ALLOWED, get 200, but a
  JS shell with no results in the HTML.
- `https://data.getty.edu/research/collections/` -> REDIRECT `/research/collections/dashboard`: ALLOWED, get 200
  (Getty Research Collections LOD Gateway: 878K records, SPARQL API `https://data.getty.edu/research/collections/sparql`).
- SPARQL GET (labels containing "Case Study House No. 22" or "Stahl House", LIMIT 200): ALLOWED, get timed out
  (HTTP 0, read timeout; the full-text FILTER is too heavy). Guard: soft refusal of data.getty.edu for 30 min. Not
  retried.

## 11. Moderna Museet (Time & Place: Los Angeles 1957-1968, 2008)

- `https://www.modernamuseet.se/en/stockholm/?p=47499` (redirect target of the `?p=47499` search URL): ALLOWED, get
  200 - generic museum home page, not the entry.
- `https://www.modernamuseet.se/en/stockholm/exhibitions/time-place-los-angeles-1957-1968/biographies/pierre-koenig/`:
  ALLOWED, get 200 (text). Koenig biography; one image, Shulman's photo of CSH #22 (credit (c) J. Paul Getty Trust,
  Julius Shulman Photography Archive). No drawing.

## 12. Overdrive section pages, one more Getty search

- WebSearch 12: `"getty.edu/research/collections/component" Koenig "Case Study House No. 22"` - no component page.
- `https://www.getty.edu/art/exhibitions/overdrive/engines_of_innovation.html`: ALLOWED, get 200 - no Koenig image.
- `https://www.getty.edu/art/exhibitions/overdrive/video_gallery.html`: ALLOWED, get 200 - videos "The Case Study
  House Program: Realized Designs" Parts I-II on YouTube (playlist PLdcw4RhcVX8vScPcfT0_ZXj9DvwHtNY65); may show
  drawings/animations of CSH 22. Video, not a drawing file: lead only (YouTube not requested).

- Final nomination text (r2-0001) re-read for open facts: no engineer or contractor named; structure "12-inch
  I-beam and ... 40-inch H-column" (sic) on a 20-ft grid; 2,300 sq ft. Repositories of additional data (p.7): GRI
  Library (Julius Shulman photos), LA Central Library, LA Conservancy library, UCLA Library, USC Helen Topping
  Architecture & Fine Arts Library. No HABS/HAER/HALS number.

## 13. SFMOMA search, Getty special collections highlights, Cal Poly Pomona pointer

- WebSearch 13: `sfmoma.org artwork Pierre Koenig architecture drawing collection` - no SFMOMA hit. New pointers:
  Calisphere `https://calisphere.org/item/ark:/13030/c8xd13ck` (per snippet: Cal Poly Pomona ENV Archives-Special
  Collections, 1958 presentation floor plan by Koenig; which house is not stated - could be CSH 21 or CSH 22) and
  `https://calisphere.org/item/1d3a61d53540309f96f8c4668940a7e8` (USC slide collection, photo of Koenig). Calisphere
  item pages: WAF, not requested; Wayback to try.
- `https://www.getty.edu/research/special_collections/highlights/architecture_design/index.html`: ALLOWED, get 200 -
  text names the Koenig archive among highlights; no Koenig image.

## Status at 15:23 (resumable)

- Done: parks.ca.gov draft, NPGallery final nomination + MPS, LA Conservancy, Getty podcast/Overdrive/shop/CDWA/CCA,
  LACMA, Moderna Museet, AIC, SFMOMA slug. Manifest R2 rows r2-0001, r2-0002, r2-0005 (r2-0003/0004 foreign).
- Pending (waiting for soft refusals to expire): web.archive.org `id_` copies of the OAC Koenig finding aid
  (kt4h4nf4b3) and of Calisphere items 3a87c1e9... (USC slide "Stahl residence") and ark:/13030/c8xd13ck (Cal Poly
  Pomona 1958 Koenig presentation floor plan); a lighter SPARQL query on data.getty.edu (identifier "2006.M.30").

## 14. Wayback copies (second attempt, 15:40)

- `https://web.archive.org/web/2024id_/https://oac.cdlib.org/findaid/ark:/13030/kt4h4nf4b3/entire_text/`: REFUSED
  again (robots.txt unreachable: connection reset; agent proxy reported "ws_closed_mid_exchange" for
  web.archive.org:443 both times, 15:10 and 15:40). The Calisphere item copies
  (`.../2024id_/https://calisphere.org/item/ark:/13030/c8xd13ck/`, `.../item/3a87c1e938853b3cf07b1d5293574171/`) were
  refused with it. web.archive.org is not reachable from this session; not retried again. hand.md.

