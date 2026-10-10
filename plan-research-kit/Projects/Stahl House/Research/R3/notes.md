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

