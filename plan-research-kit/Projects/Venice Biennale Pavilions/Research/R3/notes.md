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
