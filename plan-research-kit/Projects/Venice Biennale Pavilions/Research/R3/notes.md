# R3 notes: French Pavilion (Padiglione della Francia), Giardini

Route R3, slug `fr`, Plans folder `Plans/french/`. Started 2026-10-10.
Facts to confirm (leads): Giardini; 1912 by Faust Finzi.
Watch: 2013 swap (Germany exhibited in the French building; France in the German building).

## Sources tried (in order)

### WebSearch 1 (it): "Padiglione della Francia Giardini Biennale Faust Finzi 1912 pianta progetto"
Hits: en.wikipedia.org/wiki/French_pavilion (host refused 429 for all routes, not opened); iris.unive.it Padiglione
centrale PDF (Central Pavilion, R30's building; noted only); italia.it Giardini page; labiennale.org/it/node/19 (host soft-
refused, network); italyworldsfairs.org / iwf3.ucsd.edu postcards "Padiglione della Francia" by Stefano Molli = the
French pavilion of the 1911 Turin International Exposition (NOT the Venice pavilion; trap, no row: postcards are photos
of a different building). Wikipedia snippet: built 1912, design Faust Finzi (chief engineer of the Comune di Venezia),
layout similar to the German pavilion (Donghi, Finzi's former superior) -> unconfirmed (snippet, page not read).

### WebSearch 2 (fr): "pavillon français Venise Biennale plans du pavillon DWG appel à candidatures Institut français dossier technique"
Hits: culture.gouv.fr press pages of the calls for the French pavilion (2018, 2020), png.archi press release PDF,
comitedesgaleriesdart.com IF presentation PDF.
### Class 1: commissioning body (Ministère de la Culture / MEAE / Institut français, operator of the pavilion)
- culture.gouv.fr 2020 call page (guard 200, text read): call run on IF PROG (http://ifprog.institutfrancais.com/fr/login,
  LOGIN: not used). Attachment = press release PDF only.
- culture.gouv.fr content/download/217136/2269541 (guard 200, 222 kB): 2-page press release 9 July 2019, no drawing.
  No row.
- culture.gouv.fr 2018 call page (guard 200): press release 20170404_MCC-CP-appel-a-projet-Biennale2018.pdf (256 kB,
  not fetched: same kind of press release) and link to institutfrancais.com actualité (followed below).
  -> the call dossiers with the pavilion's technical plans sit behind the IF PROG login (hand.md / leads.md).
- png.archi press release PDF (guard 200, 3 pp): 30 Oct 2015, selection of Obras/Frédéric Bonnet + Collectif AJAP14
  "Nouvelles du front, nouvelles richesses?" for 2016; no drawing. No row.
- www.institutfrancais.com: my check of an http:// URL failed DNS locally (no http_proxy in this container) and the
  guard soft-refused the HOST for 30 min (13:21:24) -> see Rule log. To retry with https after 13:51.

### Class 1: La Biennale / ASAC (inventories of the Fondo storico)
- Read locally the three inventories R2 fetched (Scatole nere padiglioni, Paesi, Lavori e gestione delle sedi) and
  fetched three more (guard 200): 04-Scatole_nere.pdf (66 pp, nothing for the French pavilion), 04-Architettura.pdf
  (228 pp), 04-Arti_Visive.pdf. Found (confirmed from inventory text): rows r3-0001..r3-0007 (archive-only pointers):
  1926-28 planimetrie (SN Padiglioni b. 5 fasc. 4); 1948 pianta (Paesi b. 12); 1958 works plans (Lavori b. 5);
  5 piante + nota sul padiglione 1951-55 (Lavori b. 7); 1975 ristrutturazione correspondence (Lavori b. 9 fasc. 12);
  Architettura agibilità files with plans 2000-2018; Arti visive 1972 (weak). Nothing for the 1912 construction in the
  inventories (the construction file may be at the Comune di Venezia, Finzi being the municipal chief engineer).
- www.labiennale.org: soft-refused (R2, network). Not tried by R3 yet.

### WebSearch 3 (fr): "pavillon français Giardini Venise restauration rénovation travaux architecte plans coupe"
Hits: mostly the Canada pavilion restoration (other building); myartguides France 2025; inexhibit 2025 French pavilion.
Fact (confirmed, myartguides + Inexhibit): the French pavilion was CLOSED FOR RENOVATION during the 2025 Architecture
Biennale; the French contribution "Vivre avec / Living with" (Jakob+MacFarlane with Martin Duplantier and Éric
Daniel-Lacombe; commissioners Ministère de la Culture, MEAE, Institut français, Arter) was an open-air structure between
the pavilion and the canal, wrapping the building site. Renovation architect: not found yet (open).
- myartguides.com france-2025 (guard 200): text, og:image = interior render of the installation (fetched, 840x469, no row).
- inexhibit.com ?p=82810 -> REDIRECT -> case-studies/... (checked, 200): images render-1 (axonometric with the existing
  pavilion, row r3-0008), render-2 (top-down render, row r3-0009), render-3 (installation interior, no row), sito (site
  photos, no row), progettisti (portrait, not fetched). All originals 870 px wide (no larger variant in the HTML).

### WebSearch 4 (fr): "\"Vivre avec\" pavillon français Biennale architecture 2025 dossier de presse pdf rénovation du pavillon"
Hits: culture.gouv.fr 2025 press release, chroniques-architecture.com, linfodurable, tess.fr, artnewspaper.fr, Frac Centre
"DP-Vivre-avec.pdf", architecturedecollection.fr, archdaily tag, arter.net.
- frac-centre.fr DP-Vivre-avec.pdf (guard 200, 22.7 MB, 28 pp): Frac Centre educational dossier (2026 exhibition);
  pp. 4, 5, 27 photos of the 2025 pavilion/installation; no drawing. Text: pavilion "inauguré en 1912" (confirmed
  1912 opening). No row.
- arter.net project page (guard 200): production company; photos only (SRB_*, LaForgia), no drawing.
- architecturedecollection.fr: REFUSED (robots.txt answered 403) -> host refused; hand.md.
- chroniques-architecture.com ?p=75861 -> REDIRECT -> article (checked, 200). Images 01, 01-bis, 02, 03, 04 originals
  fetched; 03 (1600x533, axonometric + aerial) = row r3-0010; others installation renders / portrait.
  Article links the Institut français press kit
  https://www.institutfrancais.com/sites/default/files/medias/documents/DP%20final%20-%20Biennale%20archi%202025.pdf
  (host soft-refused by my http slip; to retry after 13:51).
- culture.gouv.fr 2025 press release page (guard 200): FACT (confirmed): "fermeture du Pavillon français pour
  d'importants travaux de rénovation menés par l'Ambassade de France en Italie" (public reception and energy
  performance). The renovation client is the French Embassy in Italy -> look for its tender (Italian procurement).
  Attachment 240503_GOUV_CP_BIENNALE_D_ARCHITECTURE_2025.pdf (press release).

### WebSearch 5 (it): "Ambasciata di Francia in Italia gara appalto lavori ristrutturazione Padiglione francese Giardini Biennale Venezia progetto"
Hits: artribune (Padiglione Italia 1988; 2023 'Ball Theater' French pavilion page; host refused 403 by R2), lapresse
(Central Pavilion 2026, R30), static.labiennale.org descrizione-appalto PDFs 2019/2020/2023 (Biennale exhibition fit-
out tenders for Arsenale / Central Pavilion, not the French pavilion; not fetched, noted for R30/R32), iris.unive.it
(Central Pavilion), labiennale.org Spain 2022. No tender of the French Embassy found by search.
### Class 1 (renovation client): French Embassy in Italy
- it.ambafrance.org -> REDIRECT it.diplomatie.gouv.fr -> REDIRECT /fr (each checked, 200; /it 200). Sitemap fetched:
  no Venice/pavilion page. Tender page https://it.diplomatie.gouv.fr/it/presence-francaise/offerte-di-lavoro-e-bandi-di-gara
  REFUSED (robots.txt Disallow */presence-francaise) -> hand.md H2.

### WebSearch 6 (en): "French Pavilion Venice Giardini floor plan section drawing exhibition Ball Theater OR \"Lieux infinis\" OR \"Studio Venezia\""
Hits: jeannouvel.com project (en/fr), italyworldsfairs.org Turin 1911 drawings (trap), culture.gouv.fr 2012 press
release "Inauguration of the French Pavilion" (guard 404), archdaily tag giardini, tess.fr printpdf/783, inexhibit.
### Class 0 / 1b: 1990 competition for a new French pavilion (curator Jean-Louis Froment)
- jeannouvel.com/en/projects/pavillon-francais-de-la-biennale -> REDIRECT (trailing slash; checked, 200). FACTS
  (confirmed, page): 1990, client Ministère des Affaires étrangères; at the 44th Biennale d'arte (27 May-30 Sep 1990)
  curator Jean-Louis Froment exhibited competition models by Jean Nouvel (winner), Christian de Portzamparc and Philippe
  Starck for replacing/reworking "the original model, dating from 1912"; not built; habitable area 400 m2 (pavilion).
  Text: GPR (Piano Regolatore) forbade changing surface or volume without exemption. Images: 5 originals (WordPress
  files without -WxH suffix, about 2560 px) + 1 screen capture -> rows r3-0011..r3-0016 (fr-alt; model photos; r3-0011
  shows the old pavilion's ring of rooms, r3-0012 the existing exedra front).
- Portzamparc: christiandeportzamparc.com -> REDIRECT 2portzamparc.com/fr -> REDIRECT / (checked, 200); projects page
  (lazy list, 32 items) and the full Yoast project-sitemap.xml (307 URLs) read: NO Venice/Biennale project. Closed.
- Starck: www.starck.com REFUSED (robots.txt 403) -> hand.md H4.
- italyworldsfairs.org "Plan of the main floor of the French Pavilion 1:100" (guard 200): Turin 1911 -> row r3-0017
  `other`/excluded (trap note).
- www.jakobmacfarlane.com: robots.txt unreachable (connection reset) -> soft refusal (network) -> hand.md H5.
- www.muoto.fr (2023 'Ball Theater'): robots.txt TLS error -> soft refusal -> hand.md H5.
- encoreheureux.org (2018 'Lieux infinis'): robots.txt connection reset -> soft refusal -> hand.md H5.
- www.duplantier.fr: guessed domain, parked (for sale page). Not Martin Duplantier's site. No row.
- fr.wikipedia.org/wiki/Pavillon_français_de_la_Biennale_de_Venise: guessed title, 404. query.wikidata.org/sparql:
  REFUSED (robots Disallow /sparql). Commons and en/it/de Wikipedia already refused (429) for the project.

### Class 4: Divisare
- divisare.com/search?q=french pavilion venice and ?q=padiglione francia (guard 200): one relevant hit, project 538106
  "jakob + macfarlane, Schnepp Renou ... French Pavilion Venice Biennale" (guard 200): "Photo essay by Schnepp Renou",
  22 images on images.divisare.com = photographs of the 2025 installation -> photo source, no rows, not downloaded.

### Class 5: Internet Archive
- archive.org advancedsearch ("french pavilion" AND venice/biennale, "padiglione francese", "padiglione della francia",
  "pavillon francais" AND venise, "Faust(o) Finzi"): 5 hits: 2 audio (Cressound 2023 = 2023 French pavilion sound
  pieces), 1 video (Christophe Hutin 2021 "Les communautés à l'œuvre", YouTube copy), 1 audio 1912 "Faust" (opera,
  homonym), 1 text "Take care of yourself" (Sophie Calle, Actes Sud 2007 = French pavilion 2007 catalogue): metadata
  read: inlibrary / access-restricted (lending) -> not downloaded (rule 2), leads.md L3.

### WebSearch 7 (it): "\"Faust Finzi\" OR \"Fausto Finzi\" ingegnere padiglione Francia Biennale Venezia 1912 progetto disegni"
Hits: en.wikipedia French pavilion (refused host), ateneoveneto.org Pajusco 2019 extract PDF, ASAC inventory (have it),
areq.net "Biennale de Venise" (fr text), cini.it press release (glass, other), iris.unive.it (Central Pavilion),
larchitecturedaujourdhui.fr 42806 (Xavier Veilhan 2017 "Studio Venezia" in the French pavilion), labiennale.org node/19,
finestresullarte (glass exhibition 1912-1930, other).
Snippet facts (unconfirmed, pages not read): "Le pavillon français, inauguré en 1912 avec une exposition Rodin, fut
dessiné par l'ingénieur Faust Finzi tandis que le décor fut confié à Umberto Bellotto" (areq.net); Pajusco (Ateneo
Veneto 2019) names engineers Faust Finzi and Nicolò Piamonte on a style commission (which pavilion: open).
- ateneoveneto.org PDF: REFUSED (robots.txt 403) -> hand.md H6.
- larchitecturedaujourdhui.fr: robots.txt TLS hostname mismatch -> soft refusal -> hand.md H6.
- areq.net (guard 200) but the body arrived compressed/undecoded (binary in the .txt): not readable. No retry.

### Class 2: Italian heritage catalogue (MiC catalogo generale dei beni culturali)
- catalogo.beniculturali.it/search?query=padiglione francia biennale (guard 200; GET search, borderline form, see Rule
  log): 4 hits: two photographic records "Padiglione Francia <Biennale; Venezia>" by Roloff Beny (CRV-F_0004279 positive,
  CRV-F_0004295 negative, Regione Veneto photo archive) = photo source, no rows; 2 unrelated. No architectural record,
  no survey drawing.
- domusweb.it/it/ricerca.html?q=... : HTTP 404 (search URL guessed). Domus search not available to the script.

### WebSearch 8 (fr): "pavillon français Venise Giardini rénovation 2025 2026 architecte maîtrise d'œuvre Ambassade de France réouverture"
Hits: archdaily.com/1025568 (2025 French pavilion), culture.gouv.fr 2025 (have it), myartguides, inexhibit, Russian
pavilion pages (R2). The renovation architect (maîtrise d'œuvre) and a reopening date were NOT found (open).
- archdaily.com/1025568: checked ALLOWED; get running in background (crawl-delay 300 s).
- archdaily.com/1025568 (guard 200, 797 kB): gallery of 34 items, all linked as "-photo"; images on images.adsttc.com,
  which is refused for the project (robots 403, R2). Earliest three (Jan 2025, ids 6781/0885.., 6781/0886.., 6781/088f..)
  are probably the curators' renders (axonometric/aerial as r3-0008/0009); 31 from Mar/Aug 2025 are photos.
  -> hand.md H7. No rows (not downloadable by script; the renders already have rows from other hosts).

### Class 1: La Biennale di Venezia website
- www.labiennale.org/it/node/19 (soft refusal by R2 had expired; robots re-read, ALLOWED) -> REDIRECT
  /it/luoghi/giardini-della-biennale (checked, 200). FACT (confirmed, page): construction list "1912 Francia (Umberto
  Bellotto)". CONFLICT with the Wikipedia/areq attribution to engineer Faust Finzi (Bellotto = decoration according to
  areq snippet). Attribution: open (Finzi design, Bellotto decoration is the likelier reading; unconfirmed).
  Slide image pad-francia.jpg (static.labiennale.org, 1300x600 style) = photo, no row.

### Class 5: theses and French journal repositories
- dumas.ccsd.cnrs.fr/search and theses.hal.science/search: REFUSED (robots Disallow /search/) -> hand.md H8.
- www.persee.fr/search: REFUSED (robots Disallow /) -> hand.md H8.
- search.openedition.org/results -> REDIRECT to an http:// address; checked the https form instead (ALLOWED, 200): 973-byte
  JavaScript shell, no results in HTML. Not readable.
- api.archives-ouvertes.fr /search/ disallowed (robots, cached); zenodo /api disallowed (R1); api.openalex.org refused
  (429, R2). Not tried.
- gallica.bnf.fr SRU (1911-1913 press on the French pavilion in Venice): robots.txt answered HTTP 403 -> host refused for
  the project -> hand.md H9.
- web.archive.org CDX (to list archived Institut français press-kit PDFs): robots.txt unreachable (connection reset) ->
  soft refusal again (network). Not readable.

## Resumed run (2026-10-10, from 13:50)

The first run stopped at about 13:47 after the web.archive.org CDX refusal. All 8 WebSearches of the route budget were
used by the first run (WebSearch 1-8 above), so the resumed run sends NO WebSearch: it works from known hosts, site
sitemaps, WordPress/MediaWiki APIs and URLs read from pages. Rows r3-0001..r3-0017 kept; new rows from r3-0018.
Since 13:50 the guard sends a contact in its User-Agent and the refusals of commons.wikimedia.org and
de/it/en.wikipedia.org were lifted (briefing "Wikimedia reopened"): class 3 is open again.
Open items from the first run: tess.fr printpdf/783 (checked ALLOWED 13:32, never fetched); www.institutfrancais.com
(soft refusal of 13:21 expires 13:51; https only); Commons/Wikipedia; exhibition sites of past contributions; IUAV,
theses, Cité de l'architecture.

### Class 3 (resumed): Wikimedia Commons, Wikidata, Wikipedia
- commons Category:Venice_Biennale_pavilions (guard 200) -> Category:Venice_Biennale_pavilions_(France) (guard 200):
  6 files, all photographs (Giardini_pavilion_France_biennale_art_2009.jpg; French_pavilion,_Venice_(542017454/
  542017614/542125653).jpg; Le_pavillon_de_la_France_(Biennale_d'architecture,_Venise)_(15258288019/15258459978/
  8089514104).jpg). No subcategory, no drawing -> photo source only, no rows. Parent categories include
  "Claude Parent" and "Built in 1912".
- Wikidata Q63502874 (EntityData JSON, guard 200): P84 architect = Q2977923 Claude Parent (French architect 1923-2016;
  Wikidata's architect claim, probably from Parent's 1970 work on the pavilion; NOT the 1912 designer) ; P5383
  archINFORM project 4523; P373 Commons category above. www.archinform.net REFUSED (robots Disallow / for claudebot);
  ita.archinform.net (cited by it.wikipedia) is an alias of the same site -> not tried (no mirror).
- en.wikipedia French_pavilion (guard 200): "built in 1912 and designed by architect Faust Finzi, chief engineer for the
  Venice municipality. Its layout and details are similar to that of the German pavilion, whose architect was Finzi's
  former boss" (cites Volpi 2013 in Re Rebaudengo, Pavilions and Garden of Venice Biennale, Contrasto, p. 169) ->
  Finzi CONFIRMED as stated by Wikipedia (secondary). 2026: Yto Barrada (curator Myriam Ben Salah).
- it.wikipedia Padiglione_Francia (guard 200): Finzi design, decoration attributed to Umberto Bellotto; 1990 Nouvel/
  Portzamparc/Starck proposals not built; "rimasto sostanzialmente invariato fino agli interventi di rinnovamento
  funzionale ed energetico eseguiti durante il 2025. È stato riaperto in occasione della Biennale Arte 2026" (cites
  institutfrancais.com/fr/pavillon-francais-biennale-venise). Bibliography lead: Didier Schulmann (ed.), "La France à
  Venise: le pavillon français de 1948 à 1988", AFAA / Carte Segrete 1990 (leads.md L8). Reference to the culture.gouv.fr
  2018 press kit 20180222_DP-BiennaleArchitectureVenise.pdf (followed below).
- es.wikipedia (guard 200): stub, nothing new.
- tess.fr printpdf/783 (guard 200, 1-page PDF, 201 kB): TESS (structural engineers, class 9) reference sheet for the 2025
  French pavilion installation (structure and tensioned canopies; architects Jakob+MacFarlane, EDL architectes, Martin
  Duplantier; client Institut français; "the French Pavilion ... is currently undergoing restoration until 2026").

### Class 1 (resumed): Institut français (operator of the pavilion) and the ministry's press kits
- www.institutfrancais.com/fr/pavillon-francais-biennale-venise (soft refusal expired; https check ALLOWED; guard 200):
  FACT (confirmed): "Dessiné par l'ingénieur Faust Finzi, le Pavillon français est inauguré en 1912 avec une exposition
  d'Auguste Rodin." Pavilion closed one year for renovation, reopened for the Biennale Arte 2026 (Yto Barrada, "Comme
  Saturne"). 2027 Architecture: agence Particules ("res publica: what is this space between you and me ?").
  www.institutfrancais.com robots: Disallow /*.pdf$ -> the old press-kit URL .../medias/documents/DP final - Biennale
  archi 2025.pdf REFUSED (robots).
- IF magazine 29 Apr 2026 "À la Biennale de Venise, un Pavillon français plus éco-responsable" (guard 200): FACTS
  (confirmed): renovation client = STBI (Service des travaux et bâtiments français en Italie), head Matthieu Bourez;
  works: timber roof trusses carrying the skylights reinforced, skylights replaced by motorised double glazing, interior
  blinds, new HVAC, full facade restoration, new access ramp for reduced mobility; energy label F -> A3. Renovation
  architect NOT named. Images = construction photos (Façade principale pendant, Verrière centrale pendant), no drawing.
- IF 2025 "Vivre avec" article (guard 200): links the press kit on site.cdn.institutfrancais.com/files/imported/DP final -
  Biennale archi 2025.pdf; IF 2026 Barrada article (guard 200) links the 2026 press kit on site.cdn...; both REFUSED:
  site.cdn.institutfrancais.com robots.txt answered HTTP 403 -> host refused -> hand.md H10. Images on the pages:
  2025 renders (Perspective extérieure / intérieure, card size only; original on the refused CDN), photos.
- IF 2023 programme page (guard 200): 'Ball Theater' card image only ("DT Ball Theater - Le projet", CDN refused).
- culture.gouv.fr 2018 press kit 20180222_DP-BiennaleArchitectureVenise.pdf (guard 200, 5.47 MB, 25 pp; cited by
  it.wikipedia): "Lieux infinis" (Encore Heureux, scenography with Collectif Etc reusing Veilhan's 2017 Studio Venezia
  timber). No drawing of the pavilion (pp. 16-19 photos and Jochen Gerner pictograms). p. 21 (PDF p. 21) history,
  quoting "La France à Venise" (AFAA/Carte Segrete 1990): FACTS (confirmed as printed): 1912 pavilion "due à
  l'ingénieur vénitien Faust Finzi", facing the German pavilion; "En 1922, une salle postérieure est ajoutée dans le
  prolongement du salon central, faisant passer la superficie totale de 340 m² à 420 m²"; pavilion otherwise unchanged;
  1990 reconstruction question after a lease renewal. pp. 21-22: list of French architecture exhibitions 1990-2016
  (1996 Migayrou "Le Monolithe fracturé" around André Bloc and Claude Parent; 2000 vaporetto by Matthieu Poitevin;
  2004 Jourda; 2006 Bouchain/EXYZT "Metavilla" (pavilion inhabited); 2008 Rambert; 2010 Perrault "Metropolis?";
  2012 Yves Lion; 2014 J.-L. Cohen; 2016 Obras/AJAP14). No row (no drawing).

### Class 4/9 (resumed): chroniques-architecture.com (WordPress REST search API) and other years' contributions
- wp-json/wp/v2/search?search=pavillon français venise (guard 200, JSON): 41 hits; opened the French-pavilion ones (each
  guard 200): "Quand Venise bat pavillon français" (2018/05, photos of Lieux infinis by Sophie Scher + Alexa Brunet
  photos of the ten places: no drawing); "Ball Theater ... par Muoto" (2023/05: renders only); "un pavillon sonore
  imaginé par Studio Muoto" (2023/01): model photos 03 and 04 -> rows r3-0021, r3-0020; renders 01 (and 02 of the
  2023/05 article) show only the mirror-ball object, no row; "Les communautés à l'œuvre, par Christophe Hutin" (2021:
  poster only); "A Venise, Encore Heureux, Etc." (2018/02): image 02 = cutaway axonometric of the whole pavilion with
  the four exhibition spaces -> row r3-0019 (best plan-like drawing so far; 750 px original per srcset); image 01 =
  photo; "Biennale d'art 2017 ... Veilhan" (2017/03): image 02 sketch -> row r3-0022 (related); 01/05 renders/model of
  the installation, no rows; "Des Zadistes à Venise" (2018/05): photos only.
- inexhibit.com wp-json search "french pavilion": empty result ([]).
- designboom wp-json search -> REDIRECT to an http:// address (not followed; https form to check separately).

### Class 1b (resumed): FRAC Centre-Val de Loire collection (Orléans; Navigart) - the main find of the route
- Wikidata's architect claim (Claude Parent) led here. collections.frac-centre.fr -> REDIRECT collection.frac-centre.fr
  (checked, 200): a JavaScript Navigart app; its bundle (guard 200) names the public API https://api.navigart.fr/503.
  Queries (each checked ALLOWED, guard 200, JSON): artworks?q=venise&size=60 / size=100 (90 hits), q=pavillon français
  (83), q=biennale venise (83). Records read: title, author, date, technique, size, inventory, medias (max 1000 px,
  url_template https://images.navigart.fr/{size}/{file_name}). Images fetched at /1000/ (the largest offered).
- Claude PARENT, "Le Monolithe fracturé, Pavillon français de la Biennale de Venise", 1996 (ensemble inv. 997 87 / 997 01
  248, 35 elements; curator Frédéric Migayrou, 5th Architecture Biennale): 29 images downloaded -> rows r3-0023..r3-0051:
  best sheets: r3-0023 ink FLOOR PLAN of the existing pavilion (4M08710); r3-0025 'Exécution : coupe' LONGITUDINAL
  SECTION through the whole pavilion (4M08722); r3-0024 'Plan / Coupe / Rampe'; r3-0026 'Exécution : plan et façade';
  r3-0027 'Elévation éch. 1:100' (front elevation of the pavilion); propositions I-III (front elevations), sketches,
  cardboard model (4M04584). Photo of the realised monolith (5H04084, A-997 87 32) downloaded but no row (photograph).
  Without images (archive-only, leads.md L10): photocopy lots A-997 87 28..31, 'Biennale de Venise, 1970' (A-009 134
  012, 3 photocopies of drawings + 1 photo by G. Ehrmann), 'Stark - Le Monolithe fracturé' (A-997 01 303).
- Philippe STARCK, "Pavillon français, Biennale de Venise" (1990 competition) model, inv. 998 01 33: 6 views -> rows
  r3-0052..0057 (fr-alt). Starck collage 90 x 123 cm (998 01 31) and Jean NOUVEL's 1990 model (998 01 34): no image
  (leads.md L10).
- ODBC "Monolithe fracturé, Biennale de Venise" collages (A-997 87 33), 4 images -> rows r3-0058..0061 (related).
- ARCHITECTURE PRINCIPE (Parent/Virilio) "Un parcours oblique continue sensibilité par les artistes", Venise 1970,
  photo print of a sketch -> row r3-0062 (related; 1970 French pavilion concept). Gilles EHRMANN "La ligne de la plus
  grande pente, Projet pour le Pavillon français de la Biennale de Venise", 1970, slide show of 285 ektachromes (11 on
  Navigart, 4M18654..4M18664): title card and one slide checked (photos of people), no rows; photo source.
- Patrick BOUCHAIN "Les Métavilla, Venise" 2003-2006, five notebooks (016 090 001..005), 220 photographed spreads:
  covers + 6 sample spreads fetched; mostly handwritten notes; rows r3-0063..0067 (document pointers, covers) and
  r3-0068 (spread with section sketch, related). Remaining spreads not bulk-fetched (rule 8) -> leads.md L9.
- Other hits not for this pavilion (no rows): New-Territories Acqua Alta (IUAV competition), Avignon-Clouet models
  (2002 contribution's own projects), Sottsass, Superstudio, Selmani, Aldo Rossi Teatro del Mondo, Smith-Miller &
  Hawkinson panels 1996 (no image).
- archiwebture.citedelarchitecture.fr (Cité de l'architecture, fonds Parent/Nouvel/Bouchain): REFUSED (robots.txt 403)
  -> hand.md H11.

### Class 4 (resumed): designboom (WordPress REST search, https form of the redirect target)
- wp-json/wp/v2/search -> REDIRECT to http://...search/? ; checked and fetched the https form
  https://www.designboom.com/wp-json/wp/v2/search/?search=french pavilion venice (guard 200, 50 hits).
- Opened (guard 200): Ball Theater 2023 (12 images fetched from static.designboom.com: only Ball-Theater-10 shows the
  pavilion (model of the exedra entrance) -> row r3-0069; the rest installation objects, mood board); Jakob+MacFarlane
  "Living with" re-staged at Frac Centre Orléans 2026 (two 1800 px photos fetched: exhibition photos, no rows);
  Veilhan 2017 (designboom01-05 + 1800: exhibition photos by caption, not fetched); 2014 J.-L. Cohen "Modernity:
  Promise or Menace?" (designboom-04..13, -2-02..07: exhibition photos by caption, not fetched); 2008 article (no
  French-pavilion images in the HTML). Photo sources only. Not opened (art exhibitions, photos): Prouvost 2019,
  Creuzet 2024, Boursier-Mougenot 2015, Lévêque 2009, Boltanski 2011, Anri Sala 2013 (German pavilion, swap year).

### Class 1 (resumed): ASACdati (asac.labiennale.org) search
- Home (guard 200) is Next.js; its search page chunk (guard 200) pushes to /risultati?termine=<text>, which is
  server-rendered with the Elasticsearch result in __NEXT_DATA__ (R2 thought the search was client-side only). GET
  query (borderline form, Rule log): /risultati?termine=padiglione francia (guard 200): Fototeca 24033, Fascicoli 528,
  Architettura 133 hits (fuzzy); first page: fascicolifoto 538478 "Padiglione Francia", SEDI, 1930-1996, PAD.STRANIERI.
  2.38-50, 10 photos + 3 slides incl. "nr. 50 s.d. - Pianta"; note "Costruito nel 1912, progetto di Umberto Bellotto";
  no digitised image -> row r3-0070 (archive-only). fascicolifoto 489837 (1976 allestimento, 2 digitised photos on
  asacdati.labiennale.org/it/fondi/fototeca/getimg.php?c=170553 / 170873: installation photos, not fetched). Queries
  "pianta padiglione francia" and "progetto padiglione francia" (guard 200): first pages only persons (fuzzy). Deeper
  paging / collection filters not attempted (form-driven).
  Attribution: ASAC and labiennale.org name Umberto Bellotto; Institut français, the 2018 ministry press kit (quoting
  AFAA 1990) and en/it Wikipedia name engineer Faust Finzi (it.wikipedia: decoration by Bellotto). Open; the likelier
  reading is Finzi design, Bellotto decoration (unconfirmed).

### Practice sites of later interveners (class 0, resumed)
- www.perraultarchitecture.com (2010 "Metropolis?"): REFUSED (robots.txt 403) -> hand.md H12.
- www.obras-architectes.fr (2016): robots.txt unreachable (proxy 502) -> soft refusal -> hand.md H12.
- www.veilhan.com (2017): guard 200 but an Angular shell (no content in HTML) -> not readable -> hand.md H12.
- www.exyzt.org (2006 Metavilla): HTTP 520 (origin error) -> not readable -> hand.md H12.
- www.christophehutin.com -> REDIRECT christophehutin.com (checked, 200): home with a video and /projets link only
  (2021 "Les communautés à l'œuvre" not on the home page); /projets not opened -> leads.md L11.

### Class 5 (resumed): theses and university repositories
- iris.unive.it /simple-search, www.politesi.polimi.it /discover, thesis.unipd.it /discover, cataloghidedicati.iuav.it
  /it/ricerca/: all REFUSED by robots.txt -> hand.md H13. dspace.unive.it: checked an http:// URL by mistake (DNS
  failure; host soft-refused 30 min) and the https form was then refused by the host block (Rule log).

### Class 4 (resumed): other press searches
- www.e-flux.com/search: REFUSED (robots Disallow /search). www.floornature.com: REFUSED (robots.txt 403).
  www.stylepark.com/en/search (guard 200): JavaScript results, nothing in HTML. www.domusweb.it/en/search.html: 404.
  www.archiportale.com/search -> REDIRECT to archiproducts.com (not followed).

### More checks (resumed run, 14:00-14:20)
- christophehutin.com/projets: checked ALLOWED, get -> connection reset (host soft-refused, network) -> leads L11 stays.
- www.labiennale.org/en/architecture/2023|2018/national-participations/france: checked ALLOWED, get -> connection reset
  (www.labiennale.org soft-refused again, network) -> not readable this run.
- www.inexhibit.com wp-json posts?search=french pavilion: [] again (search disabled or no match).
- commons.wikimedia.org/w/api.php search: REFUSED (robots Disallow /w/). Category:Giardini_della_Biennale_(Venice)
  (guard 200): photographs, one statues subcategory, no map or site plan (site plans are R32's).
- www.culture.gouv.fr/recherche?SearchText=... (guard 200): results rendered by JavaScript, nothing in HTML.
- Soft refusals re-tested after 30 min: encoreheureux.org now REFUSED by robots (Disallow / for claudebot);
  www.jakobmacfarlane.com ALLOWED -> REDIRECT jakobmacfarlane.com -> robots unreachable (connection reset, soft refusal);
  www.muoto.fr still TLS error. All stay in hand.md H5.
- catalog.hathitrust.org / babel.hathitrust.org: refused for the project (403, R5). www.internetculturale.it search:
  REFUSED (robots). archive.org: soft-refused by R4 at 14:00 (network) -> retry after 14:30 for the 1909-1930 Biennale
  catalogues (site plans of the Giardini with the French pavilion).
- Navigart further queries (guard 200): q=jakob macfarlane (7 works, none Venice), encore heureux (Bouchain Haie Vive,
  Bony Mosconi: none Venice), exyzt (the five Metavilla notebooks again), muoto (0), perrault metropolis (0).
- it/en Wikipedia "Giardini della Biennale" (guard 200): photos only, no site map; it.wikipedia caption "Padiglione
  Francia, di Umberto Bellotto, 1912".
- www.inexhibit.com sitemap_index.xml and case-studies-sitemap1..4.xml (guard 200): French-pavilion articles 2014,
  2016, 2018, 2025 (+ Italian versions). Opened 2014 (no French-pavilion images left in the HTML), 2016 (photos
  01/03/04 and exhibited projects, 870 px), 2018 "Infinite places" (Encore-Heureux 1-9 and the ten places: photos,
  largest 870w in srcset). Photo sources only; no drawings; not downloaded.
