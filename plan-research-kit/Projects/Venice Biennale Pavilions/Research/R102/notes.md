# R102 notes: gap route and completeness critic for R2 (Russian Pavilion, Giardini)

Route R102, slug `ru`, Plans folder `Plans/russian/`. Started 2026-10-10 13:50 UTC.
Read before acting: BRIEFING.md, R2 manifest/notes/leads/hand, R2 lines of requests.jsonl, refused_hosts.json,
plan-sources.md, Giudecca_critic.md, R2's saved page renderings under `_work/guard/pages/`.

## 1. Gaps in R2 (listed before acting)

State of refusals at 13:50: commons.wikimedia.org, en/it/de.wikipedia.org still hard-refused (429) in
refused_hosts.json. ru.wikipedia.org is open. Soft refusals of R2 older than 30 min (pavilionrus.com 13:09, muar.ru
13:00, goskatalog.ru 13:00, www.culture.ru 13:04, 2050.plus 13:13, www.mapstudio.eu 13:12, russianpavilion.org 13:15,
garagemca.org, www.kommersant.ru 13:25, www.sobaka.ru 13:25, www.mk.ru 13:24) have expired and may be re-tested once;
web.archive.org was soft-refused again by R3 at 13:46 (expires 14:16).

G1. Wikimedia Commons: the category of the pavilion exists under a name R2 never tried:
    `Category:Venice_Biennale_pavilions_(Russia)` (30 files), read off R1's saved page
    `_work/guard/pages/commons.wikimedia.org/b9520419_Category_Venice_Biennale_pavilions.html.txt`. R2 guessed three
    wrong names and drew the 429. Commons is still refused -> hand.md with the exact URL (unless the host is taken off
    the list during this run).
G2. ru.wikipedia: the article on the pavilion was never found (two title guesses 404). Not tried: the article
    "Венецианская биеннале" (lists national pavilions with links), other titles. Wikidata item of the pavilion
    (P373 Commons category, sitelinks) not read; SPARQL and /wiki/Special: are robots-disallowed.
G3. pavilionrus.com (current site): soft refusal expired; home page, year archives (2022-2026), architecture pages
    never read.
G4. previous.pavilionrus.com: 9 press pages linked from /en/about/press never opened (press releases 2019-2020,
    "Open", "Moving online", Domus 2020 interview, Monopol); /en/people, /en/projects/video-overview,
    /en/the-gamer/* not opened (low value, credits/games).
G5. Shchusev originals: muar.ru, goskatalog.ru, www.culture.ru (article "Итальянские проекты Алексея Щусева",
    2017 MUAR exhibition, very likely shows the Venice drawings) were network failures only (connection reset):
    soft, expired -> re-test once each.
G6. Garage Museum: the 2014 exhibition page was guessed (500); the real exhibition URL never found; the 2014 book
    (Evstratova/Koluzakov) may have a publication page with preview images.
G7. ArchDaily project page "Renovation of Russian Federation Pavilion at Venice Biennale / KASA" (2021-08-17): URL
    never found (www.archdaily.com itself is open; only images.adsttc.com is refused). Its image list (KASA drawings
    with captions) belongs in hand.md with exact URLs.
G8. KASA office website never found (Kovaleva and Sato Architects); 2050.plus and www.mapstudio.eu were network
    failures (soft, expired) -> re-test once.
G9. Exhibition layouts on the pavilion plan 2010-2019 (and 2011-2017 art shows) never searched: SPEECH/Tchoban
    (speech.su) for 2010 "Factory Russia" and 2012 "i-city"; Strelka 2014 "Fair Enough"; 2013 Zakharov "Danaë"
    (opening in the floor between the levels), 2016 "V.D.N.H." (spiral stair), 2017 "Theatrum Orbis", 2018 "Station
    Russia", 2019 Hermitage. La Biennale year pages for Russia never read (labiennale.org soft refusal over).
G10. Catalogue entries: ASAC inventory PDFs already saved in `_work/guard/pages/asac.labiennale.org/` by other routes
    (04-Architettura.pdf, 04-Arti_Visive.pdf, 04-Scatole_nere.pdf) were never grepped for URSS/Russia. ASACdati search
    is client-side: its JSON API (Next.js) was never looked for.
G11. Historic catalogues: the 1914 XI Esposizione catalogue and later Biennale catalogues (public domain, possibly on
    archive.org with a Giardini plan or a plan of the Russian pavilion) never searched; Internet Archive was searched
    only for "shchusev OR russian pavilion" in English.
G12. Theses and articles: no Russian academic article on the pavilion's history found (cyberleninka search
    disallowed; article pages allowed); no Italian thesis (IUAV/Politecnico) on the Giardini pavilions; AMIT
    (marhi.ru) and other open Russian journals never searched; HAL API not queried.
G13. Sheet types and states with no sheet: the 1914 original state has no plan and no section (only an elevation and a
    porch sketch, r2-0051/52, under 1300 px); Soviet-era states (1950s-60s floor raising, 1960s doors) have no
    drawing except KASA's Modification Logfile (r2-0034); exhibition-era states 2010-2019 none; no elevation drawing
    of the current state except the KASA watercolour (r2-0039/0055); no vector file.
G14. Larger sizes: Metalocus originals (2048 px) are the largest seen; WA copies 1200 px; KASA Traces pages 1500 px;
    jidipi (upload.jidipi.com refused) might hold larger copies -> hand only. Metalocus 23 and 24 (conceptual diagrams,
    "no row" in R2) and the photos 01-14/28-55 were judged without rows: check 23/24 on the sheets.
G15. Fetch step: r2-0028 (`story-3_kasa_400.gif`) answered 404 to the download step at 13:48:40; check whether R2's own
    copy exists on disk.

## 2. Sources tried (in order)

### G3 pavilionrus.com (current site; soft refusal of 13:09 expired)
- `https://pavilionrus.com/en`: ALLOWED, 200. The site now carries only the 2026 exhibition "The tree is rooted in the
  sky" (pages Participants, Roots, Press Release, Contacts, link "Previous Project" -> previous.pavilionrus.com).
  `/en/roots`, `/en/artists` fetched (artist portraits only); `/docs/eng_PRESS_RELEASE.pdf` fetched (4 pp, text only, no
  image). No architecture page any more (R2's `/en/architecture/project` 500 = removed route). Closed: no drawings.

### G4 previous.pavilionrus.com press subpages
- 8 of the 9 press subpages linked from `/en/about/press` fetched: all HTTP 404 (03-press-release, open, moving-online,
  open-call, press-release, press-release-moscow-6-december-2019, ippolito-pestellini-...-domus-july-august-2020,
  russian-pavilion-in-monopol). The ninth (newsletter) is a form. Closed: removed from the site.

### G5 Shchusev originals, re-test after soft expiry
- `https://www.culture.ru/materials/222308/italyanskie-proekty-alekseya-shuseva`: check REFUSED again (robots.txt
  unreachable, connection reset) -> soft refusal renewed; stays hand.md (H6 of R2, repeated in R102 hand.md).
- `https://muar.ru/`: ALLOWED, get -> connection reset (network) -> soft refusal renewed. Hand.md.

### G2 ru.wikipedia
- `Венецианская_биеннале` (percent-encoded): 200. No link to an article on the Russian pavilion; one photo
  (`Russia_pavilion_Biennale_Giardini_art_2009.jpg`, photo, no row) and an archived link to the 2009 pavilion site
  `https://web.archive.org/web/20130621090826/http://russian-pavilion.info/` (web.archive.org soft-refused until 14:16).

### G6 Garage Museum and RAAN (Russian Art Archive Network, Garage's online archive catalogue) - new source class 1b/5
- garagemca.org `/en/exhibitions` (JS list, no Venice hit), `/en/programs/publishing` (no hit),
  `/en/programs/archive-collection-and-raan` (links the online catalogue https://russianartarchive.net/en): all 200.
- RAAN search (server-rendered, robots allows): "Щусев" 387 results (Shchusev's archive at Garage, mostly 1923
  All-Russian Exhibition documents, e.g. D12289 sketch of the "Ukraine" pavilion); "Щусев Венеция" 3 results;
  "Венеции павильон" 28 results; "Venice pavilion Shchusev" 1; "план павильона Венеция" and
  "план экспозиции Венецианская биеннале" 0.
- Found (confirmed from the record pages):
  - D21933 "План Русского павильона в Венеции", 1996, three A4 sheets, Olga Tobreluts and Andrei Khaas Archive
    (Garage Archive Collection, St. Petersburg, TX-I.3.B-D21933): 3 images (800/1200 px, TIFF behind an expired signed
    link) -> rows r102-0001..0003 (browser-only).
  - D21935 "Экспозиция проекта «Новый Русский Классицизм» для Венецианской биеннале", 1998, 7 sheets; verso of the last
    sheet carries a hand-drawn plan -> row r102-0004 (document pointer, building unconfirmed). Related D21931 (14
    images) and D21943 (5 images): exhibition project texts for 1999, no plan named.
  - L33305: the Garage 2014 book (R2 lead L4) -> row r102-0005 (document pointer, archive-only).
  - EXRT (2014 Garage exhibition, curators Kalgaev/McGetrick/Paramonova; Strelka, MARCH), E3606 and E24185 booklets
    (2 and 3 images), E7933 press release (7 images): content of the images unknown -> hand.md.
  - L1927 "Русские художники на Венецианской биеннале, 1895-2013" (Stella Art Foundation 2013): history of the
    pavilion, archive documents and ASAC photos; no drawings named -> leads.md.
  - L65665 Kommersant 2003 "Русский павильон в Венеции не останется без крыши" (roof repairs 2003; a state with no
    drawing) -> leads.md.
- Images: all on hb.bizmrg.com, whose robots.txt disallows / for every agent (guard REFUSED, also `--as claude-user`).
  Nothing downloaded -> hand.md H1.
- 14:07 RAAN keyword query `search?keywords=<Venice Biennale>&keywords=<Architecture>` answered HTTP 500 -> soft
  refusal of russianartarchive.net (30 min; my slip: a double keyword parameter the site does not handle; see Rule log).

### G10 ASAC inventories already on disk (no web request)
- Grepped `04-Architettura.pdf` (228 pp), `04-Arti_Visive.pdf` (479 pp), `04-Scatole_nere.pdf` (66 pp), fetched by R3,
  for Russia/URSS units that name plans: Architettura 2000-2012 agibilità and participation files with plans of the
  Russian pavilion (b. 291/5, 305, 342, 416/4, 423/18, 437, 458, 468, 470) and Arti Visive 2001/2003/2013 files with
  plans of the exhibition spaces (b. 748, 790, 973) -> rows r102-0006, r102-0007 (archive-only pointers). Scatole nere:
  1930s catalogue-proof units only, no plan of the pavilion.

### WebSearch 1 (en): "\"Renovation of Russian Federation Pavilion\" KASA Kovaleva Sato archdaily drawings"
No ArchDaily project page, no KASA office site. One new host: archivibe.com/?p=18562 -> REDIRECT to www.archivibe.com
(checked) -> 404; www.archivibe.com/?s=russian+pavilion -> 404. Closed (site gone).

### WebSearch 2 (ru): Щусев "павильон" Венеции 1913 1914 Джардини статья pdf (cyberleninka OR elibrary OR marhi.ru)
Only news hits already seen by R2 (kommersant, rambler, sobaka, theblueprint, mk.ru). No academic article. Closed.

### G9 Exhibition layouts: SPEECH (speech.su), class 0 for 2010 and 2012
- speech.su/en/ -> REDIRECT /en -> REDIRECT /ru/en; speech.su/ -> REDIRECT /ru (each checked as new URL); /ru fetched.
  Project filter logic read in /system/js/custom.js (filter URL /ru/projects/exhibitions?page=N).
- /ru/projects/exhibitions pages 1-3: found "Экспозиция «i-citi/i-land» Российского павильона на XIII Архитектурной
  Биеннале" (2012) and "Проект «Фабрика Россия»" (2010).
- 2012 page: 23 lightbox images (`/images/project/large/<hash>.jpg`, 1200 px; the plain /images/project/ path is a
  670 px thumbnail, tested on the 3 drawings). All fetched and viewed (sheets R102_1, R102_2): 20 renderings/photos and
  3 CAD drawings with dimensions: First floor plan, Second floor plan, Section 1-1 -> rows r102-0008..0010.
- 2010 page: 8 images (1750 px), all fetched and viewed (sheet R102_3): installation photos only (diorama, exposed brick
  hall, panels) -> no rows (photos of the 2010 state; note for photo sources).
- www.tchoban-foundation.de: robots.txt unreachable (connection reset) -> soft refusal; not needed further.

### WebSearch 3 (ru): exhibition architects of the Russian pavilion 2016 «В.Д.Н.Х.» / 2018 «Станция Россия»
Hits: iz.ru 2018, projectbaikal.com article 1270 (news), style.rbc.ru, gazeta.ru 2014/2012, bfm.ru, realty.rbc.ru,
sobaka.ru. No exhibition architect named, no plan. projectbaikal.com: article page REDIRECT -> /pb/ru/... (checked,
fetched), PDF REDIRECT -> /pb/ru/article/download/1270/1260/1549 (checked, fetched): 1-page news item on the 2018
Biennale, no drawing. Closed.

### G1/G2 Wikimedia (hosts taken off refused_hosts.json during this run, re-read at 14:14)
- `https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Russia)` (name from R1's saved parent
  category): 200. 30 files, all photographs (2009 art, 2010/2012/2014 architecture shows via Flickr uploads, 2013
  Zakharov "Danaë", 2026 protests, "Born house venezia.jpg"); no subcategory, no drawing -> no rows. Wikidata item
  Q63769653 (from the category's authority box).
- `https://www.wikidata.org/wiki/Q63769653`: 200; sitelinks en ("Russian_pavilion") and es only: there is no
  ru.wikipedia or it.wikipedia article (settles R2's 404 title guesses).
- `https://en.wikipedia.org/wiki/Russian_pavilion`: 200; text only (built 1913-14 by Shchusev; closed 1922, 1938-54,
  1978-80; list of shows). No drawing, no new reference with drawings.
- `https://commons.wikimedia.org/wiki/Category:Alexey_Shchusev` and subcategory `Architectural_drawings_and_designs_by_Alexey_Shchusev`
  (9 files: Kazan station 1912, Trinity cathedral Petrograd, New Moscow 1923, 1934 projects): no Venice drawing.
  File page `L'architecte_Alekey_Shchusev_(Biennale_d'architecture_2014,_Venise)_(15572630398).jpg` = photo of a
  Shchusev portrait shown in the pavilion in 2014 (photo, no row). Closed.

### WebSearch 4 (it): "padiglione russo" OR "padiglione della Russia" Giardini ... pianta rilievo tesi pdf
Hits: ecoseven, artribune (refused host), domusweb 2021 gallery (R2: photos), finestresullarte x2, ilpost,
internazionale.it x2 (2026 news). No thesis, no survey. Budget used up (4 of 4).

### Re-tests after soft expiry (14:19-14:22)
- web.archive.org: check REFUSED again (robots.txt unreachable, connection reset) -> stays hand (R2 H8).
- 2050.plus: home fetched (Vue shell, no content, robots crawl-delay 60 s); `/sitemap_index.xml` -> connection reset ->
  soft refusal renewed -> hand.md H2.
- www.mapstudio.eu (proxy 502) and goskatalog.ru (connection reset): REFUSED again at check. Not readable from here.
- www.labiennale.org/en/architecture/2021/russia: REFUSED at check (host soft-refused by R3 shortly before) -> hand H3.

### 2. Sighting of R2's files (local, no requests)
- Files located through index.csv `source_file` and the guard log `out` (49 image files + the PGUPS PDF); r2-0028's
  file found under its real URL (`story-3@kasa_400.gif`).
- Contact sheets: R102_4 (r2-0001..0012), R102_5 (r2-0013..0024), R102_6 (r2-0025..0036), R102_7 (r2-0037..0054),
  R102_8 (comparisons: Traces 45 vs Metalocus 22, Metalocus 23/24/54, Meduza windows, p07 vs story_1 GIF), crop R102_c4
  (Traces p. 24 collage) and pdf-pages R102_9.jpg/shusev_p007.jpg (PGUPS p. 7, embedded images 1268x717 and 800x536
  confirmed with pymupdf).
- Pixel sizes measured with PIL for every file: all match R2's manifest.
- Every file shows the Russian pavilion except r2-0053 (Bari church, already `other`/excluded by R2). No building
  photo is counted as a drawing. Sheet types checked: correct as given (r2-0012/0013 are sections with interior
  elevation, r2-0038 a diagrammatic site section, r2-0040 an exploded axonometric).
- Fixes -> corrections.json: r2-0028 download_url ('@' not '_': the cause of the three 404s in the download step);
  r2-0029 same_item_as r2-0022 (same perspective, GIF 478 px); r2-0017 same_item_as r2-0037 (same watercolour long
  section, Metalocus 2048 px larger); r2-0002/r2-0035 and r2-0003/r2-0036 links reversed so the 2048 px Metalocus copies
  are primary; r2-0009 re-tagged `ru` (its collage carries thumbnails of Shchusev's ORIGINAL GF and 1F plans and his
  1913 perspective, about 130 px each).
- Metalocus 23 and 24 (on disk, no R2 row): watercolour garden views (roof corner only; trees) -> no row, R2 right.
- R102's own downloads: SPEECH 2012 and 2010 sets sighted on R102_1..3 and crops R102_c1..c3 (see G9 above).

### Further leads followed (14:23-14:27)
- en.wikipedia "Russian pavilion" references: one new host, `https://www.ruspavilion.com/` ("Official website", older
  site): robots.txt answered HTTP 522 (Cloudflare origin down) -> REFUSED (assume disallow). Dezeen 2014 Strelka
  article (www.dezeen.com refused for the project) -> photos expected; artsy/artnews/guardian: news. Closed / leads.
- es.wikipedia "Pabellón de Rusia en la Bienal de Venecia": 200, no references, no drawing. Closed.
- Commons `File:Born_house_venezia.jpg` (in the pavilion category): description "Павильон экспозиции Born House на
  Венецианской биеннале, в соавторстве с Юрием Аввакумовым" (an installation, 600 px): not a drawing of the pavilion,
  no row.
- domusweb.it search `/en/search.html?q=...`: 404 (search path unknown); the Domus 2020 interview stays in leads.md L4.
- worldarchitecture.org saved page re-checked: 24 Cappelletti photos + the 6 KASA drawings R2 took; nothing missed.
