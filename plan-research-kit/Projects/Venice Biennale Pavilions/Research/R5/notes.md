# R5 notes: United States Pavilion (Padiglione degli Stati Uniti), slug `us`

Route R5, started 2026-10-10. Plans folder `Plans/american/`. Facts to confirm (leads): Giardini; 1930 by Delano &
Aldrich (William Adams Delano, Chester Holmes Aldrich); owned by the Solomon R. Guggenheim Foundation since 1986.
refused_hosts.json read at start (commons.wikimedia.org, en/de/it.wikipedia.org 429; www.europeana.eu 403;
web.archive.org network; images.adsttc.com 403; www.dezeen.com 403; world-architects.com 403; gallica 403 ...).

## Sources tried (in order)

### WebSearch 1 (it): "Padiglione degli Stati Uniti" Giardini Biennale Delano Aldrich pianta restauro
Hits: labiennale.org Giardini pages, austria-architects.com "6 National Pavilions in 3 Pairs" (2025; sister site of
world-architects.com, which is refused 403 -> treated as alias, hand.md), artribune (refused host). No plan.

### WebSearch 2 (en): US Pavilion Venice Giardini Delano Aldrich floor plan drawing
Hits: en.wikipedia American pavilion (host refused 429), Arch Record 2025 open call, designboom officeUS 2014,
guggenheim-venice.it US pavilion, architizer us-pavilion-14th, arch.uic.edu PressRelease_USPavilion.pdf (2021).

1. https://www.guggenheim-venice.it/en/art/us-pavilion/ (class 1, owner): ALLOWED, get OK. Text: Palladian-style,
   designed 1930 by W. A. Delano and C. H. Aldrich; bought 1986 by SRGF from MoMA (confirmed). Year pages 1986-2026.
   Year pages read (2025, 2023, 2022, 2021, 2019, 2018, 2016, 2012, 2010, 2008, before 1986): exhibition credits and one
   photo each, no drawings. They give the exhibition sites: porchusavenice2025.org, everlastingplastics.org,
   americanframing.org, dimensionsofcitizenship.org, thearchitecturalimagination.org (+ Google Arts & Culture 2016),
   spontaneousinterventions.org, simoneleighvenice2022.org, martinpuryearvenice2019.org, almaallenvenice2026.org.
   Found (leads only).
2. https://www.designboom.com/architecture/officeus-venice-architecture-biennale-06-09-2014/ (class 4): ALLOWED, get OK.
   Leong Leong "floor plan of the pavilion" = offceUS-pavilion.jpg (818x583, r5-0001) and model photo (r5-0002).
   No larger variant in srcset (WordPress originals without -WxH suffix were taken). Found.
3. https://www.architizer.com/projects/us-pavilion-14th-venice-biennale : REFUSED (robots.txt unreachable, redirect
   to http://architizer.com, DNS). hand.md.
4. https://www.architecturalrecord.com/articles/16751-... : REDIRECT to .../16751-open-call-issued-...; new URL
   checked ALLOWED, get -> HTTP 403 bot challenge: host closed for all routes. hand.md.

5. Exhibition sites from the Guggenheim year pages (class 0/4), one check command:
   - https://www.porchusavenice2025.org/ (2025 PORCH, Fay Jones School / Marlon Blackwell): ALLOWED, get OK; subpages
     design-team, exhibition-tour, press, introduction, exhibitors, press-release-july/-august/-finalists all get OK.
     exhibition-tour holds two drawings of the whole pavilion: floor-plan map Map_2.png 2000x1540 (r5-0003) and front
     elevation Map_.png 2000x700 (r5-0004), Squarespace originals. Other images: Tim Hursley photos up to 2500 px
     (photo source, no rows) and exhibitors' own buildings. Press images in a Dropbox folder
     https://www.dropbox.com/scl/fo/byjh2yzwexwmbl0ccvsl3/... : REFUSED (robots.txt Disallow /scl/) -> hand.md. Found.
   - https://www.everlastingplastics.org/ (2023): REFUSED (robots.txt unreachable, SSL EOF). Not readable -> hand.md.
   - http://www.americanframing.org/ (2021): REFUSED (DNS: domain gone). Not readable.
   - http://dimensionsofcitizenship.org/ (2018): REFUSED (DNS). Not readable.
   - http://www.spontaneousinterventions.org (2012): REFUSED (DNS). Not readable.
   - https://simoneleighvenice2022.org/ (2022 art): REFUSED (expired certificate). Not readable.
   - https://www.martinpuryearvenice2019.org/ (2019 art): get OK, parked page (4 kB). Empty.
   - https://www.almaallenvenice2026.org/ (2026 art): get OK; /pavilion, /exhibition, press release get OK, /explore 404.
     Only installation photos (Agostino Osio, up to 11648x8736: photo source, no rows); 360 tour on Google Maps. Empty.
   - https://www.thearchitecturalimagination.org/ (2016): get OK; /press, /the-sites get OK. Press release PDFs
     "Call for Proposals" (redirect to static1.squarespace.com, checked, get OK, 1 p.) and "Architects Announced"
     (redirect, checked, get OK, 2 pp.): text only, no plan. Press Dropbox https://www.dropbox.com/sh/lw8ik57xpftvxlu/...
     REFUSED (robots.txt Disallow /sh/) -> hand.md. Google Arts & Culture exhibit 2016 -> hand.md. Empty (drawings).
   - https://arch.uic.edu/sites/arch.uic.edu/files/pdfs/PressRelease_USPavilion.pdf (2021 American Framing announcement,
     2019-11-25): get OK, 2 pp., logos + text only. Empty.

6. Class 0, practices of later interveners (exhibition designers):
   - https://www.paulpreissner.com/ (American Framing 2021): get OK; splash page, amfram.jpg (1068x1600) = photo of the
     timber frame, no drawing (no row). Book "Kind of Recent Projects and Drawings" (Amazon link) = print lead.
   - https://indiearch.com/ (Paul Andersen, Independent Architecture): REFUSED (robots.txt unreachable, reset).
   - https://www.marlonblackwell.com/ : get OK (home lists "Porch: An Architecture of Generosity");
     /projects/porch-an-architecture-of-generosity checked ALLOWED, get -> network error (SSL EOF), host now on the
     refusal list. hand.md.
   - https://www.leong-leong.com/ -> REDIRECT https://leong-leong.com/ (checked, get OK). Project pages are lazy-loaded;
     WP REST queried (checked ALLOWED, get OK): wp-json/wp/v2/search?search=office (finds post 296 "U.S. Pavilion - 14th
     Venice Biennale") and wp-json/wp/v2/media?search=biennale (21 items with full sizes). Project page
     https://leong-leong.com/14th-venice-biennale-u-s-pavilion/ get OK. All 16 post-296 media fetched from
     leong-leong.com/wp-content/uploads/2016/09/ (each checked ALLOWED): three CAD line floor plans of the whole
     pavilion with walls and officeUS furniture (r5-0005..0007, ~800 px), rendered exploded plan 1200x900 (r5-0008,
     larger copy of r5-0001), model photo (r5-0009); the other 11 are installation photos (no rows). Home-page media
     LEONG-LEONG_BIENNALE_1/2/3 (3300-5616 px) are Canon 5D photos per WP metadata (no rows). The page also embeds
     160925_AXON-02 and 160925_CONCEPT-DIAGRAM-01 from s3.amazonaws.com/leongleong/...: check REFUSED (S3 robots.txt
     answered 403 -> s3.amazonaws.com now closed for every route). hand.md. Found.

### WebSearch 3 (en): Delano & Aldrich architectural drawings Avery Library "Venice" American pavilion 1930 Grand Central Art Galleries
Hits: en.wikipedia (refused host), Columbia finding aid cul-3460565 "Delano & Aldrich architectural records and papers,
1900-1949" (Avery; by appointment), Columbia "Jewels in her crown" exhibit, gildedage.omeka.net Grand Central Art
Galleries page, archrecord 3166 (refused host). Facts (from search snippets, unconfirmed until read): commissioned and
paid by the Grand Central Art Galleries (Walter Leighton Clark), opened 4 May 1930; architects donated the plans.

7. Class 1b: https://findingaids.library.columbia.edu/archives/cul-3460565 (Avery, Delano & Aldrich records and
   papers 1900-1949, 7,000 drawings): ALLOWED, get OK; EAD XML get OK: no container list, Venice not named; CLIO
   record REFUSED (robots.txt Disallow /). Archive-only lead (leads.md 2). Empty online.
   https://gildedage.omeka.net/exhibits/show/galleriesandclubs/galleries/grandcentral : get OK; text confirms the Grand
   Central Art Galleries were "responsible for the creation, design, and construction of the United States Pavilion at
   the Venice Biennale, 1930-1954"; images are gallery thumbnails, no pavilion drawing. Empty.
8. Class 1, ASAC: inventories of the Fondo storico read locally (fetched by R2, no new request): plan files for the US
   pavilion 1929-31 (construction), 1933-34, 1938, 1940-57 works, 1958 plans, 5 piante in the Padiglione Venezia
   series. Archive-only (leads.md 1). Found (archive-only).
9. Class 1, La Biennale: https://www.labiennale.org/it/luoghi/giardini-della-biennale and
   https://www.labiennale.org/en/architecture/2025/united-states-america : ALLOWED, get OK. Text confirms "1930 Stati
   Uniti d'America (Chester Holmes Aldrich e William Adams Delano)"; no map file, no drawings. Empty.

### WebSearch 4 (en): State Department ECA "U.S. Pavilion" Venice Biennale open call application "floor plan" pavilion pdf
Hits: archrecord 16751/17242 (refused host), UIC press release (done), e-flux 452597, bustler.net 10206, crystalbridges.
10. Class 1, commissioning body (US Department of State, ECA): no ECA page in the hits.
   - https://www.e-flux.com/announcements/452597/open-call-for-applications/ -> REDIRECT to the same path without the
     trailing slash (checked, get OK): 2022 call for the 2023 US Pavilion; "full funding opportunity and application
     materials are available at grants.gov", opportunity SFOP0008572; no plan on the page. Lead: the NOFO packages
     (SFOP0008572 for 2023 and the 2025 call) may carry a pavilion floor plan as attachment -> hand.md (grants.gov is
     JavaScript; https://simpler.grants.gov/search?query=venice%20biennale checked ALLOWED, get OK but results are
     rendered client-side: nothing readable).
   - https://bustler.net/news/10206/... : ALLOWED, get -> HTTP 403 bot challenge; host closed. hand.md.
11. Class 2, MiC catalogo generale: https://catalogo.beniculturali.it/search?query=padiglione%20stati%20uniti%20biennale
   ALLOWED, get -> network error (SSL EOF); host now on the refusal list, second query not sent. Not readable
   (other routes found only photo records there for their pavilions). hand.md. Vincoli in Rete / Comune / Soprintendenza:
   no online plan service known (leads.md).
12. Class 3, Wikimedia: commons.wikimedia.org closed (429, R2) before this route started; Wikidata API
   https://www.wikidata.org/w/api.php?action=wbsearchentities... REFUSED (robots.txt Disallow /w/). Not readable.
   hand.md.

### WebSearch 5 (en): "American Framing" US Pavilion Venice 2021 Andersen Preissner drawings plan section axonometric
Hits: Arch Record digital editions (digital.bnpmedia.com, July and May 2021), myartguides, whitewall, archiweb.cz,
iwfatlanta, nelma.org, avontuura.com, theedgesingapore.
13. Class 4/9 for 2021 American Framing:
   - https://www.archiweb.cz/en/b/americke-ramovani-pavilon-usa-na-17-bienale-v-benatkach : REFUSED (robots.txt
     Disallow / for claudebot). hand.md (archiweb usually publishes plans/sections).
   - https://digital.bnpmedia.com/article/AMERICAN+FRAMING/4060676/712463/article.html -> REDIRECT
     /publication/?i=712463&article_id=4060676&view=articleBrowser (checked ALLOWED), get -> HTTP 202 (interstitial);
     host closed. hand.md (Arch Record July 2021 article, May 2021 preview 4004900/704318).
   - https://www.avontuura.com/?p=26432 -> REDIRECT https://avontuura.com/?p=26432 (checked, get OK): now a shop home
     page, the old post is gone. Empty.
   - https://www.nelma.org/the-art-of-american-timber-framing-is-on-display-at-the-venice-biennale/ : ALLOWED, get ->
     HTTP 403 bot challenge; host closed. hand.md.

### WebSearch 6 (en): "United States Pavilion" Venice Biennale history 1930 Delano Aldrich "Grand Central Art Galleries" article OR thesis pdf plan
Hits: en.wikipedia x4 (refused), archrecord 3166 (refused), modernism.ro, guggenheim (done), Google Arts asset,
spectator.com, liquisearch (Wikipedia copy). Snippet lead: en.wikipedia "17th Venice Biennale" cites a 1930 issue of
"The Architect" (New York) on the pavilion (period publication; leads.md).
14. https://www.modernism.ro/?p=46093 -> REDIRECT .../2011/07/19/gloria-allora-calzadilla-us-pavilion-... (checked, get
   OK): 2011 photos only. Empty. https://spectator.com/article/message-behind-us-pavilion-venice-biennale/ : get OK,
   text only ("Delano and Aldrich donated their services"). Empty.
15. HathiTrust full-text and catalogue search (for 1930 journals, now US public domain):
   https://babel.hathitrust.org/cgi/ls?... and https://catalog.hathitrust.org/Search/Home?... : REFUSED (robots.txt
   answered 403 -> both hosts closed for every route). Not readable. hand.md.

### WebSearch 7 (en): "American pavilion" Venice 1930 Delano Aldrich "Architecture" OR "Pencil Points" OR "American Architect" OR "Architectural Forum" usmodernist
Hits: only Wikipedia, guggenheim, archrecord, frieze 2013 review, artforum. No period article found. Empty.
16. Further exhibition designers / sites (class 0/4):
   - http://www.officeus.org/ (2014): REFUSED (DNS). https://storefrontnews.org/programming/officeus/ : REFUSED (proxy
     502 / connect_rejected). Not readable.
   - https://futurefirm.co/ (Ann Lui, co-curator 2018 Dimensions of Citizenship): get OK; no Venice project listed. Empty.
   - https://artsandculture.google.com/exhibit/biennale-architettura-2016-... -> REDIRECT /story/QgXxo7NkA2TwJg (checked,
     get OK): 2016 story; text names Monica Ponce de Leon's courtyard installation (13 star-fluted columns); drawings
     shown are the Detroit projects (not the pavilion); images load client-side. Lead for MPdL.
   - https://www.mpdlstudio.com/ -> REDIRECT https://mpdlstudio.com/ (checked, get OK); WP REST search?search=venice and
     media?search=venice / ?parent=349 / ?parent=1241 (checked, get OK); project pages "Courtyard of the US Pavilion,
     Venice" and "The Architectural Imagination, Venice Biennale" get OK. One drawing: 160108_StarColumns original
     3400x2200 (r5-0010, installation columns only, related); the rest are photos (Flickr-sourced 1600-2048 px, exterior
     photos 2560 px: photo source, no rows). Found.
   - https://usmodernist.org/ -> REDIRECT https://www.usmodernist.org/ (checked ALLOWED; not fetched yet).

17. Class 5 (archives, libraries, repositories, theses): Internet Archive (archive.org, web.archive.org) and Europeana
   closed before this route started; HathiTrust closed by this route (robots 403); Zenodo API REFUSED (robots Disallow
   /api); IUAV IRIS https://iris.iuav.it/simple-search?... REFUSED (proxy 502); OpenAlex closed (429, R2). No thesis
   found in WebSearch 6 and 8. Not readable / empty.
   https://search.architecturalperiodicals.com/architects.php (USModernist periodicals index, checked, get OK): Delano &
   Aldrich not in the architects index. Empty.

### WebSearch 8 (it): "padiglione USA" OR "padiglione americano" Giardini Biennale Delano Aldrich 1930 progetto disegni tesi OR rilievo OR restauro
Hits: Wikipedia (refused), artribune (refused), archrecord (refused), labiennale (done), inexhibit.com Giardini page.
18. https://inexhibit.com/mymuseum/giardini-della-biennale-venice/ -> REDIRECT www.inexhibit.com (checked, get OK):
   Giardini site map over aerial photo with pavilion footprints, original 1024x1220 (r5-0011, site, related; all
   pavilions named). Found (orientation only).
19. Press-site searches (GET, borderline form, see Rule log): designboom ?s= -> REDIRECT /search-result/?q= (checked,
   get OK) and https://www.archdaily.com/search/all?q=... (get OK): both render results client-side, nothing readable.
   e-flux announcements search: REDIRECT not followed. Instead the related links on the e-flux 452597 page were read:
   e-flux 591904 (2025), 533715 (Everlasting Plastics 2023), 408633 (American Framing 2021), 252746 / 231177 / 201483
   (Dimensions of Citizenship 2018): all checked, get OK; captions name photos only; the image CDN
   images-eflux.b-cdn.net REFUSED (connection reset) -> hand.md. Empty (readable part).
20. https://www.guggenheim-venice.it/en/press/ and /en/art/library-archive-photography/ : get OK; press room lists PGC
   exhibitions only; the PGC library/archive offers remote services by e-mail (lead, leads.md 6).

## Source classes (verdict)

| Class | Verdict | Notes |
|---|---|---|
| 0 architects / later interveners | found | Leong Leong officeUS 2014: three CAD floor plans of the whole pavilion + rendered plan + model (r5-0005..0009); PORCH 2025 site: floor plan 2000x1540 and front elevation 2000x700 (r5-0003/0004); MPdL 2016 column drawing (r5-0010, related); Preissner splash page (photo); indiearch, marlonblackwell project page, americanframing.org, officeus.org, storefrontnews not readable (hand.md); Delano & Aldrich firm long gone (see 1b) |
| 1 La Biennale / ASAC / owner / commissioning body | found (archive-only) + empty online | ASAC inventories list 1929-31 construction plans and later plan files (leads.md 1); labiennale.org: text only; Guggenheim (owner since 1986): year pages, exhibition links, no drawings; State Dept/ECA NOFO packages on grants.gov not readable (hand.md) |
| 1b architects' archives / national museum | archive-only | Avery Drawings & Archives, Delano & Aldrich records 1900-1949 (7,000 drawings; no item list; Venice not named) (leads.md 2); MoMA Archives, AAA Grand Central Art Galleries records not searched (leads.md 7) |
| 2 heritage records | not readable | catalogo.beniculturali.it network error; no Soprintendenza / Comune plan service online |
| 3 Wikimedia Commons / Wikidata | not readable | Commons 429 (closed by R2), Wikidata /w/ robots-disallowed, Wikipedia 429 |
| 4 published plans / exhibition sites | found | designboom 2014 (r5-0001/0002); PORCH site (r5-0003/0004); Inexhibit site map (r5-0011); 2016/2026 sites, Google Arts 2016, e-flux, avontuura, modernism.ro: no pavilion drawings; ArchDaily images, archiweb, Arch Record, bustler, nelma, everlastingplastics.org, simoneleighvenice2022.org, Dropbox press kits closed (hand.md) |
| 5 archives / libraries / theses | not readable / empty | archive.org, Europeana, HathiTrust, Zenodo, IUAV IRIS, OpenAlex closed; no thesis found |
| 9 trade press / engineers / contractors | empty / leads | no renovation architect or contractor of the pavilion found online; American Framing timber trade articles (nelma.org) closed; print catalogues (leads.md 5) |

## Findings

- Best sheets: PORCH 2025 exhibition map, floor plan of the whole pavilion 2000x1540 PNG (r5-0003) and front elevation
  2000x700 (r5-0004); Leong Leong 2014 CAD line floor plans with walls, niches, doors, WC (r5-0005, r5-0006, r5-0007,
  about 800 px). All are exhibition-era drawings (us-reno) but show the 1930 building shell; none is scaled or
  dimensioned and none is vector. No original 1930 Delano & Aldrich drawing is online; originals are expected at ASAC
  (b. 15 fasc. 9 "Padiglione americano 1928: planimetrie" 1929-31; 5 piante in Lavori b. 7) and possibly at Avery.
- Facts read (confirmed): Palladian-style pavilion designed 1930 by W. A. Delano and C. H. Aldrich (guggenheim-venice.it,
  labiennale.org, inexhibit); built for the Grand Central Art Galleries of New York (construction acts dated August 1929
  in ASAC; gildedage.omeka.net: GCAG responsible for "creation, design, and construction ... 1930-1954"); sold to
  MoMA (ASAC files 1951-1955 on the sale to MoMA), bought by the Solomon R. Guggenheim Foundation from MoMA in 1986
  (guggenheim-venice.it). Opening 4 May 1930 and "architects donated the plans" are from search snippets of Wikipedia
  (unconfirmed). Plan read from r5-0003/r5-0005: central domed rotunda with four niches, four corner galleries with
  chamfered corners, service rooms behind the rotunda, U-shaped forecourt with a four-column portico.
- Photo sources (no rows): PORCH site (Tim Hursley, up to 2500 px), Alma Allen 2026 site (Agostino Osio, up to 11648 px),
  Leong Leong (Naho Kubota photos up to 5616 px via WP media), MPdL (2016 courtyard photos 2560 px), Guggenheim year
  pages, modernism.ro 2011.

## Rule log

WebSearch: 8 of 8 used (it, en, en, en, en, en, en, it).
WebFetch: none (no check --as claude-user, no webfetch-done).

Refusals and closures caused by R5 (from requests.jsonl / refused_hosts.json):
- 403 / bot challenge (final, all routes): www.architecturalrecord.com (13:50:39), bustler.net (14:08:20),
  www.nelma.org (14:11:04); robots.txt answered 403: s3.amazonaws.com (14:00:57, Leong Leong axon images),
  babel.hathitrust.org and catalog.hathitrust.org (14:13:17); HTTP 202 interstitial: digital.bnpmedia.com (14:10:38).
- Network / DNS / TLS (soft): www.architizer.com, www.everlastingplastics.org, www.americanframing.org,
  dimensionsofcitizenship.org, www.spontaneousinterventions.org, simoneleighvenice2022.org, indiearch.com,
  www.marlonblackwell.com (get after ALLOWED check failed with SSL EOF), catalogo.beniculturali.it (same),
  www.officeus.org, storefrontnews.org, iris.iuav.it, images-eflux.b-cdn.net.
- robots.txt Disallow (URL refused, host not closed): Dropbox /scl/ and /sh/, leongleong.wpenginepowered.com /,
  clio.columbia.edu /, www.wikidata.org /w/, www.archiweb.cz / (claudebot), zenodo.org /api.
- Redirects: every REDIRECT was checked as a new URL in a separate command before its get (architecturalrecord,
  thearchitecturalimagination PDFs x2, leong-leong.com, e-flux 452597, digital.bnpmedia, avontuura, modernism.ro,
  Google Arts, mpdlstudio, usmodernist, inexhibit, designboom search). The e-flux search redirect was not followed.

Slips and borderline points (self-reported):
1. Form ("check as its own command"): five check commands shared one Bash command with local work placed before the
   check (notes/hand appends or a grep): PORCH rows + Dropbox check; practice sites check (paulpreissner, indiearch,
   leong-leong, marlonblackwell); Columbia/gildedage check; labiennale check; refused_hosts grep + Zenodo/IRIS check.
   No get was ever chained to a check.
2. Form: a few single gets were followed in the same command by local reads (`; ls`, `; grep` of the saved file):
   usmodernist home, architects.php, e-flux search (redirect only), refused_hosts grep before a get loop. No further
   request was chained; all multi-get commands used the `|| break` loop form.
3. Borderline "submit a form": GET searches on catalogo.beniculturali.it (failed, network), simpler.grants.gov,
   designboom, archdaily, e-flux (redirect not followed); documented WordPress REST API searches on leong-leong.com and
   mpdlstudio.com (search, media?search=, media?parent=).
4. Borderline "mirror/alias": the Leong Leong files were fetched from leong-leong.com/wp-content/uploads/2016/09/ (the
   source_url the site's own WP API gives; robots.txt of leong-leong.com allows it). The page itself embeds the same
   files from the CDN leongleong.wpenginepowered.com, whose robots.txt disallows all; I learned that only after the
   downloads (the CDN was never requested beyond its robots.txt).
5. A check was run once on a guessed grants.gov detail URL (https://www.grants.gov/search-results-detail/337979); only
   robots.txt was requested, the URL was never fetched.
6. Impact (no breach): R5's checks closed s3.amazonaws.com and both HathiTrust hosts for every route (robots.txt 403).
7. Tool/process issue (no breach): the shared scratchpad file scratchpad/addrow.py written by R5 was overwritten by
   route R102 at 14:00 (same session scratchpad). R5 rows r5-0001..0004 had been written before; R5 then moved its
   helper to scratchpad/r5/r5_addrow.py. Manifest checked: ids continuous r5-0001..r5-0011.
8. Image reads: only files under 1 MB or peek sheets were opened with Read (largest 919 kB JPEG via sheet; PNG plans
   51-264 kB read directly).
