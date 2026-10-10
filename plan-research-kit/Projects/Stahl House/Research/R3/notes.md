# R3 notes: web publications, re-posts, models and CAD (Stahl House, CSH 22)

Started 2026-10-10. Sources in the order tried.

## 1. Wikimedia Commons
- `https://commons.wikimedia.org/wiki/Category:Stahl_House` ALLOWED, get 200. 58 files, no subcategories. Files: 13 crops
  "Julius Shulman - Case Study House 22, Arts & Architecture, June 1960 (page 14..21 crop)" (photos), Flickr photo
  uploads (Case_Study_House_22_(59019...), Stahl_House_(8658...)), Stahl_House_2/5/6/7, Breeze_Blocks: all photographs,
  no drawing file in the category. One PDF: `File:Arts_&_Architecture,_June_1960.pdf` (36 pages, 1635x2047, 80.18 MB,
  PD-US-not renewed; uploaded 2025-10-22 from artsandarchitecture.com/issues/pdf01/1960_06.pdf) -> r3-0001.
- Commons search (`/w/index.php?search=...`) REFUSED by robots (Disallow: /w/); Wikidata Special:Search REFUSED
  (Disallow: /wiki/Special:). So no intitle: search was possible through the guard.
- `upload.wikimedia.org/.../Arts_%26_Architecture%2C_June_1960.pdf` check ALLOWED, get **HTTP 429** -> host refused
  for the project (refused_hosts.json). Wikimedia's upload servers reject User-Agents without contact details; the
  guard UA carries "contact-not-set" on purpose. The PDF goes to hand.md. No other upload.wikimedia.org request made.
- Photo sources (not rows): the Shulman crops and the Flickr-derived photos in the category.

## 2. jimlochner.com PDF
- `https://jimlochner.com/s/Case-Study-House-No-22.pdf` ALLOWED, get -> REDIRECT to static1.squarespace.com
  `.../Case+Study+House+No.+22.pdf`; checked ALLOWED, get 200 (3,573,065 bytes) ->
  `_work/guard/pages/static1.squarespace.com/35ef2a23_Case_Study_House_No._22.pdf`.
- Content: one magazine page "Backstory / Case History" by Jim Lochner (page 80 of a magazine), text + 3 photos
  (two Shulman, one by Charlotte Wiederholt). **No drawing.** No manifest row. Text facts: L-shape with a single hallway,
  2,200 sq ft, 2 bed / 2 bath, cost $37,500, lot bought 1954 for $13,500, adopted into CSH program early 1959.

## 3. WikiArquitectura (es, en)
- es `/edificio/casa-stahl/` -> REDIRECT `/edificio/casa-stahl-case-study-house-no22/` checked ALLOWED, get 200.
  Section "Planos": 6 images, originals (no -WxH suffix) fetched, all 200: Planta_2 (472x445, A&A-style plan),
  Planta (675x791, sepia book plan, Spanish caption), Plano_2 (1998x723 ext. perspective), Plano_4 (1998x573 living
  room perspective), Plano_3 (630x494 kitchen perspective), Plano_5 (800x559 visitor sketchbook) -> r3-0002..0007.
  No licence or source statement on the page. 8 photos Casa_Stahl_1..11 (photos, not rows).
- en `/building/stahl-house/` -> REDIRECT `/building/stahl-house-case-study-house-no22/` ALLOWED, get 200: same six
  files under en.wikiarquitectura.com/wp-content/uploads/2017/01/ (same names); not fetched twice.

## 4. Web searches 1-2 (of 15)
- WS1 `"Stahl House" Koenig plan section drawings archdaily OR archeyes OR divisare OR metalocus` -> archeyes.com/?p=43209,
  newschoolarch.edu student PDF, pcad.lib.washington.edu/building/1837.
- WS2 `archdaily "AD Classics: Stahl House" Pierre Koenig` -> archdaily.com/83038/..., architecturelab.net, archjourney.org,
  architectuul.com, 5osa.com/8865.

## 5. ArchEyes, PCAD, architectuul
- archeyes.com: check REFUSED, robots.txt answered HTTP 403 -> host refused (hand.md).
- pcad.lib.washington.edu/building/1837/: REFUSED (robots Disallow: / for ClaudeBot). PCAD is a text database record
  (lot 86x150 ft per the search snippet); no WebFetch tried (no drawings expected). Lead only.
- architectuul.com/architecture/stahl-house: ALLOWED, get -> 200 with a bot-challenge page -> host refused (403).

## 6. ArchDaily "AD Classics: Stahl House / Pierre Koenig" (Andrew Kroll, 2010-10-22)
- `https://www.archdaily.com/83038/ad-classics-stahl-house-pierre-koenig` ALLOWED (robots crawl-delay 300 s), get 200.
  Gallery page `.../5037e56228ba0d599b000300-...-image` ALLOWED, get 200: the gallery JSON lists 14 images with
  slideshow sizes and captions. Drawings: image 14 (0302, plan 472x445), image 5 (0303, ext. perspective 1582x572),
  image 13 (0304, kitchen perspective 630x494), all '© wikiarquitectura.com'. The other 11 are photos (800x535,
  1024x768 etc.). -> rows r3-0021..0023 (same_item_as WikiArquitectura copies).
- images.adsttc.com: check REFUSED, robots.txt answered HTTP 403 -> host refused. The images are browser-only and
  not needed (copies at equal or larger size are downloaded).
- Plataforma Arquitectura uses the same images.adsttc.com CDN: not tried (host refused).

## 7. Architecture Lab (architecturelab.net) "Stahl House / Pierre Koenig | Classics on Architecture Lab"
- `https://www.architecturelab.net/stahl-house-pierre-koenig/` ALLOWED, get 200. 57 images with figcaptions/credits.
  19 candidates by credit (Pierre Koenig, WikiArquitectura, Adam Caruso Chair ETH Zurich) checked ALLOWED and fetched
  as originals (no -WxH suffix, present in srcset), all 200. 9 are drawings -> r3-0012..0020:
  plan 944x890 (=WA Planta_2 x2), plan 850x850 with scale symbol, ext. perspective 2000x979 (B/W), living-room
  perspective 1740x1066, ext. perspective 1582x572 (=ArchDaily), kitchen perspective 1260x988 (=WA Plano_3 x2),
  ETH Caruso chair site plan 850x850 and two sections 849x623.
  The 10 others credited "Pierre Koenig" (2,3,5-11,14) are photographs (credit is wrong); kept in pages/ but no rows.
- Photo credits on that page: Julius Shulman / Getty Research Institute, Brontis5, Cameron Carothers, cityNnature,
  Chris Schroeer-Heiermann, mbtrama (Commons), Design within Reach.

## 8. archjourney.org, 5osa.com
- archjourney.org/projects/stahl-house-case-study-house-22/ ALLOWED, get 200: 5 photos (495x400 thumbs), no drawings.
- 5osa.com/8865 (Korean Tistory blog, crawl-delay 20 s) ALLOWED, get 200: ~24 images on signed blog.kakaocdn.net URLs,
  text names no plan/drawing (no 도면/평면/단면); images not fetched (likely photos). Unchecked.

## 9. NewSchool of Architecture & Design student PDF
- `https://newschoolarch.edu/wp-content/uploads/2021/05/MARUCUT-S-ID-201-Final-Project.pdf` ALLOWED, get 200
  (6.2 MB, 44 slides). Analysis slides with redrawn site plan (p7/p19, 1777x1805 embedded), floor plan base
  'KOENIG CASE STUDY #22 MAIN FLOOR PLAN' with zone overlays (pp8-11, 1004x974), axonometric (p12, 1142x807);
  rest is the student's own guest-house proposal. -> r3-0008..0011. Slide 2 credits: William Porush engineer,
  Robert Brady contractor, Van Keppel-Green interiors, Catalina Pool Company.

## 10. Web searches 3-12 (12 of 15 used so far)
- WS3 hiddenarchitecture/atlas of places/archinform/socks-studio: nothing specific (rblind.com post, book listings).
- WS4 Adam Caruso ETH + Stahl House: nothing ties the ETH chair to CSH 22 drawings online -> lead.
- WS5 dwg/dxf/cad: archinform 9340, lacasadelaarquitectura.es, LEGO Ideas; no CAD file.
- WS6 3D models: cgarchitect.com (fan render), Evolve Lab forum (3D Warehouse model), Lumion recreation (Carlos
  Rodriguez), LEGO Ideas project. No Sketchfab hit in the search -> used Sketchfab API through the guard.
- WS7 es "Casa Stahl" planta seccion tesis: urbipedia.org/hoja/Casa_Stahl, designscad.com/?p=234238, acento.com.do.
- WS8 it pianta sezione: MEF University library record (student model of CSH 22, Berra Nur Bay, 2017, catalogue only),
  PCAD publication 3972 (Taschen Case Study Houses, Smith 2002, pp. 300-319 "plans, drawings"), Taschen Koenig.
- WS9 ja 平面図 断面図: metalocus author page, Getty Iris post ?p=53931, laconservancy pages, uncrate.
- WS10 floor plan blog/tumblr/flickr: rostarchitects.com article (plan + perspective).
- WS11 theses repositories: revistas.usach.cl Arteoficio article (Pablo Altikes, 2006; part of a Seville PhD thesis).
- WS12 es dwg bibliocad: nothing.

## 11. archINFORM, Urbipedia, lacasadelaarquitectura.es, Metalocus
- www.archinform.net/projekte/9340.htm REFUSED (robots Disallow: / for ClaudeBot). Lead only (archINFORM normally has
  literature lists, sometimes plan thumbnails).
- www.urbipedia.org/hoja/Casa_Stahl REFUSED (robots.txt answered 403) -> host refused. Its text is a copy of
  WikiArquitectura's; images probably the same files.
- lacasadelaarquitectura.es resource page ALLOWED, get 200: Wikipedia text only, no images of the house.
- metalocus.es/en/author/koenig ALLOWED, get 200: only two CSH 21 (Bailey House) sale articles; nothing on CSH 22.

## 12. 3D models
- api.sketchfab.com/v3/search?type=models&q=stahl%20house ALLOWED, get 200 (JSON): 3 relevant models -> r3-0024..0026
  (one CC BY and downloadable after login; two view-only). Not fetched (login).
- 3dwarehouse.sketchup.com/search/?q=stahl%20house ALLOWED, get 200 but JavaScript-only page (no results in HTML).
  forum.evolvelab.io post (get 200) says the 3D Warehouse has a Stahl House model -> r3-0027 (lead).
- grabcad.com REFUSED (robots.txt answered 403) -> host refused.
- Renders (not rows): cgarchitect.com/projects/a5996e9c-stahl-house-case-study-house-22 (3ds Max/Corona),
  lumion.com/made-with-lumion/stahl-house-recreation, ideas.lego.com project e1c89800-... (841-piece set renders).

## 13. ROST Architects article "Nine Things You Should Know About The Stahl House" (2020-10-06)
- rostarchitects.com URL -> REDIRECT to www.rostarchitects.com; checked ALLOWED, get 200. Two drawings on Squarespace
  CDN; originals (URL without ?format) checked ALLOWED, get 200:
  `Stahl+House+Plan.JPG` 1254x1238 (whole plan sheet with border, north arrow and graphic scale) -> r3-0028;
  `Stahl+House.jpg` 1582x572 (the sepia exterior perspective again) -> r3-0029.
  Other images: Shulman photos (GRI 2004.R.10 file names, 'Inside Utopia' pages), own photos.

## 14. Arteoficio No. 5 (USACH, 2006): Pablo Altikes, "La habitabilidad de la caja. Casa Carlota Stahl"
- revistas.usach.cl/ojs/.../download/854/26005618/26017952 ALLOWED, get 200 (3-page PDF, 969 kB): visit account
  with 5 small photos (max 453x290). **No drawing.** No row. File saved without extension:
  `_work/guard/pages/revistas.usach.cl/6303ab41_26017952`.

## 15. CAD hosts
- bibliocad.com `/en/search/?q=stahl+house` ALLOWED, get 404 (search URL shape wrong). archweb.com
  `/en/search/?q=stahl` ALLOWED, get 404. designscad.com `/?s=` REFUSED by robots; its `/?p=234238` (search hit) is
  a REDIRECT to an Adolf Loos Steiner House DWG (not this building; not followed). cadbull.com REFUSED (robots 403).
  No free DWG/DXF of CSH 22 found.

## 16. Wikidata Q2328939
- Special:EntityData/Q2328939.json ALLOWED, get 200: P18 = 'Case Study House No. 22.JPG' (photo); no P3311 plan image;
  NRHP 13000519; address 1635 Woods Dr; archINFORM id present (P5383). No drawing.

## 17. Publisher previews: Taschen and Chronicle Books
- taschen.com/en/books/architecture-design/49298/koenig/ ALLOWED, get 200: 6 preview spreads of Neil Jackson,
  *Koenig* (2007) on taschen.makaira.media (f_webp,w_1200; checked ALLOWED, get 200, WebP 1200x765/768). Spreads
  dd992d85 (CSH 22 photo + sepia perspective), 35f3b6bb (CSH 22 kitchen + sepia kitchen perspective), e80ff505
  ("1960 Stahl House" opening + small plan) -> r3-0030..0033. Spreads 983c0d0e, c022f0ff, 4457ca01 show the Bailey
  House (CSH 21: green perspective sketches, photos): no rows (other building).
- chroniclebooks.com/products/the-stahl-house -> 404 (guessed URL). WS13 gave the real URL
  `/collections/art-design/products/case-study-house-22` (ALLOWED, get 200): only the cover image; text confirms
  "blueprints, floor plans, and sketches by Pierre Koenig" and Buck Stahl's DIY schematic model; 208 pp.

## 18. Web searches 13-14 and midcenturyhome.com
- WS13 de Grundriss Schnitt: Chronicle product URL, stagprovisions, architectuul, docomomo-us. WS14 fr plan coupe:
  midcenturyhome.com, lamag.com "A shot in the dark" (photo story), MEF library record.
- www.midcenturyhome.com/case-study-houses-pierre-koenig-stahl-house -> REDIRECT to the same URL with a slash;
  checked ALLOWED, get 200: photos only (Shulman, Flickr james vaughan, a render), no drawing. No row.
- 14 of 15 WebSearches used.

## Summary of R3 findings
- 33 rows: 23 downloadable drawing rows (all fetched; none exceeds 2000 px on the long side, the largest is
  r3-0014 at 2000x979; everything is orientation only), 1 downloadable document pointer (student PDF),
  2 pointers not downloadable (Commons A&A PDF blocked by 429; Taschen book), 3 ArchDaily duplicates (images host
  refused), 4 3D-model leads.
- Distinct drawings found on the open web: (1) floor plan (A&A / Koenig presentation plan) in four reproductions,
  best r3-0028 (1254x1238, whole sheet with north arrow and graphic scale); (2) sepia/BW exterior perspective,
  best r3-0014 (2000x979); (3) living-room perspective, r3-0015 (1740x1066) / r3-0005 (1998x573 crop); (4) kitchen
  perspective, r3-0017 (1260x988); (5) ETH Caruso chair redraws: site plan r3-0018, two sections r3-0019/0020
  (850 px); (6) student redraws (site plan 1777x1805, floor plan 1004x974, axonometric) in r3-0008..0011;
  (7) a visitor's sketchbook spread r3-0007. No elevation, framing plan or detail of CSH 22 surfaced on the open web;
  no free CAD file; 3D models only behind logins.
- Facts read: credits slide (student PDF p2): engineer William Porush, contractor Robert Brady (secondary source,
  `unconfirmed` for the briefing's open engineer item). Floor area given as 2,200 sq ft (Chronicle, Lochner) and
  2,300 sq ft (Rost, others): `open`.

## Rule log
- Refusals and host closures caused on this route (all recorded by the guard in refused_hosts.json):
  - upload.wikimedia.org: guard get of the A&A June 1960 PDF answered **HTTP 429** (15:07:41) -> host refused for the
    project. Cause: Wikimedia rejects User-Agents without contact details; the guard UA says "contact-not-set" on
    purpose. No retry; the file is in hand.md. Other routes cannot fetch upload.wikimedia.org originals now.
  - archeyes.com (robots.txt 403), images.adsttc.com (robots.txt 403), grabcad.com (robots.txt 403),
    www.urbipedia.org (robots.txt 403), www.cadbull.com (robots.txt redirect to cadbull.com answering 403):
    refused at check, no content request sent.
  - architectuul.com: content get returned 200 with a bot-challenge page -> host refused (403). No retry.
- Robots refusals (URL only): commons.wikimedia.org /w/index.php search (Disallow: /w/); www.wikidata.org
  Special:Search (Disallow: /wiki/Special:); pcad.lib.washington.edu and www.archinform.net (Disallow: / for
  ClaudeBot); designscad.com /?s= (Disallow: /*?s=). None was attempted another way.
- Guard observation (not a slip, for the orchestrator): api.sketchfab.com/robots.txt answered **HTTP 202 with an
  empty body** (15:21:50); the guard treated it as a readable robots.txt with no rules and the check ALLOWED; the
  following get of the search API returned 200 JSON. The guard docstring treats an unexpected 202 on content as
  throttling; for robots.txt it did not. Flagged in case the rule should apply to robots.txt too.
- Redirects: each REDIRECT was checked as a new URL in a separate command before its get (jimlochner -> squarespace,
  WikiArquitectura es/en, rostarchitects -> www, midcenturyhome slash). designscad /?p=234238 redirect not followed
  (other building).
- WebFetch: none used.
- WebSearch: 14 of 15.
- Check/get separation: every get ran in a later command than its check. Multi-get commands were for-loops with
  `|| break`. One loop used a `case` inside the loop body to choose `--text` per URL (still one guard get per
  iteration, stopping at the first non-zero exit); the loop broke at the first REDIRECT as intended, and the
  remaining URLs were fetched in later commands within the 60-minute check window.
- One get command (ArchDaily gallery page + 5osa page) ran past the 120 s Bash timeout and was moved to the background
  by the harness because archdaily.com's crawl-delay is 300 s; it completed normally (both 200). No parallel request
  to the same host was sent while it ran (I worked on local files and other hosts).
- No image > 1 MB and no PNG was Read; contact sheets via peek.py. Two Read calls of small JPEGs directly
  (WikiArquitectura Plano_5, 49 kB; ROST plan, 109 kB), both under 1 MB.
- No login, registration, form, payment or CAPTCHA. No shadow library. No other HTTP client.
