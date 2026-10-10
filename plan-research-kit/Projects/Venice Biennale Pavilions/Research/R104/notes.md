# R104 notes: gap route and completeness critic for R4 (British Pavilion, slug `gb`)

Route R104, started 2026-10-10 14:27 UTC. Plans folder `Plans/british/`. Design ids gb, gb-alt, gb-reno, gb-unk.
Read before start: BRIEFING.md (incl. "Wikimedia reopened"), refused_hosts.json (96 hosts), plan-sources.md,
Giudecca_critic.md, R4 manifest.jsonl (13 rows), notes.md, leads.md (L1-L11), hand.md (H1-H7), R4's 322 lines in
requests.jsonl, ../Plans/british/index.csv (6 files sorted: r4-0001..0005, r4-0008).
WebSearch budget: 4.

Guard note read in tools/guard.py: soft refusals (network, 5xx, unexpected 2xx) expire after 30 min (SOFT_EXPIRY 1800 s)
and the guard then re-reads robots.txt; hard refusals (401/403/429/challenge) stay. The Giudecca critic records
re-tests after the 30-minute soft expiry as permitted by the rules. R4's British Council timeouts (13:39:44 and
13:45:32) and visualarts' 503 (13:55:37) are past that expiry; archive.org (14:00:26) expires 14:30, www.labiennale.org
(R3, 14:16:53) 14:47. R104 re-tests these hosts once with new URLs (never the exact URL that was refused) and stops at
the first new refusal. Hard refusals stay closed: www.britishcouncil.org, www.britishcouncil.it, old.designcurial.com,
www.e-architect.com, www.tandfonline.com, images.adsttc.com, www.dezeen.com.

## 1. Gaps in R4 (listed before acting)

G1. British Council hosts, soft refusals now expired: venicebiennale.britishcouncil.org (open-call PDFs 2020 and 2027,
    the "British Pavilion User Guide" appendix with drawings PDF, elevations PDF, floor loading PDF and VECTOR ZIP;
    press pages; timeline pages; exhibition guides), design.britishcouncil.org (open-call blog posts 2010-2018 with
    attachments), visualarts.britishcouncil.org (exhibition pages, history of the pavilion). R4 never reached any.
G2. archive.org (soft, expires 14:30): item britainatveniceb0000unse never inspected (lending or open); the 26 other
    hits of R4's advancedsearch never listed in notes; no search for Rickards' own monograph "The art of E. A. Rickards"
    (1920, public domain, drawings by Rickards) nor for 1909-1914 Biennale catalogues / periodicals (The Builder, The
    Studio, Architectural Review 1909) that may print the converted pavilion.
G3. www.labiennale.org (soft, expires 14:47): bandi-e-gare (tenders with planimetria of the Giardini), the national
    participations pages of past years, Giardini map PDFs. R4 never reached them (refused by R3's reset).
G4. ASACdati online catalogue (asac.labiennale.org/risultati?termine=...): R4 used only the PDF inventories; R3 found
    that the Fototeca has a "Padiglione <country>" SEDI / PAD.STRANIERI photo dossier with plan items ("Pianta") and some
    digitised images (getimg.php). Not queried for Gran Bretagna / Inghilterra.
G5. ASAC inventory PDFs already on disk (04-Architettura, 04-Arti_Visive, 04-Scatole_nere, fetched by R3) were not read
    for British units: grep (local) shows planimetrie / piante / agibilità files for Gran Bretagna in Architettura 2000
    (b. 291/3), 2002 (b. 335, b. 375), 2006 agibilità (b. 423/17), 2010 agibilità (b. 457), 2018 (p. 217). Archive-only.
G6. Wikimedia Commons: R4 opened only the UK pavilion category and the Giardini category. Not opened: Commons
    categories of Edwin Alfred Rickards / Lanchester & Rickards (drawings), maps of the Giardini / of the Biennale
    (SVG maps would show the pavilion footprint, vector), historic photo categories (1909-1930s Biennale) that might
    hold photos of drawings; Wikipedia articles of Rickards (works list, references) and de/fr Wikipedia pavilion pages.
G7. Other routes' files that show the British Pavilion and were not taken by R4: r101-0009 (kleihues+kleihues 2014
    site plan with the neighbouring pavilions drawn in plan, "Great Britain"), the other R101 "this is modern" 2014
    sheets (site plans of the German pavilion's surroundings), R3 drawings of the French pavilion (immediate
    neighbour; site sheets may draw the British pavilion in full), r3-0009 (2025 aerial render, partial).
G8. Larger sizes / unfetched items: 3GATTI render img_2 on designboom (seen, not fetched); 3GATTI optimole CDN variants;
    whether designboom serves larger originals of img_3/img_4 (818x1142); Metalocus Island set is the 2048 px original
    (no larger); CSJ files at the 4800 px maximum (done).
G9. Exhibition layouts drawn on the pavilion plan, years not covered: 2008 Home/Away, 2010 Villa Frankenstein (muf),
    2012 Venice Takeaway, 2014 A Clockwork Jerusalem (FAT + Crimson: crimsonweb.org project page not tried), 2016 Home
    Economics (curators' site not tried), 2021 The Garden of Privatised Delights (Unscene Architecture), 2023 Dancing
    Before the Moon (Jayden Ali / JA Projects and co-curators), 2025 GBR - Geology of Britannic Repair (Cave_bureau,
    Owen Hopkins, Kabage Karanja, Stella Mutegi). Art Biennale exhibition guides (room plans) never looked for.
G10. Class 4 hosts not tried for "Island" and other years: Archello (architects' own drawing uploads), Domus
    (domusweb.it), Architecture Today, RIBA Journal article pages (R4 only tried RIBAJ search), The Plan,
    Building Design, Icon, Wallpaper, Abitare, Stylepark / e-flux article pages (R4 only reached search pages).
G11. Repositories not queried: Zenodo API (R4 believed it refused; it is not in refused_hosts.json), CORE API, DOAJ,
    IUAV IRIS (soft refusal by R5 expires 14:48), theses on the pavilion (Italian and English). OpenAlex (429) and HAL
    search (robots) stay closed.
G12. RIBA collections: RIBApix search closed by robots.txt (/search?); item pages and the architecture.com image library
    may be open; never tried. RIBA catalogue entries for Lanchester & Rickards drawings of Venice not identified.
G13. Languages not searched: German, Spanish, French (only one Italian and four English searches in R4). Search terms
    not tried: "padiglione inglese" Giardini 1909, "caffè ristorante" Giardini 1887 Trevisanato, "Britischer Pavillon".
G14. Sheet types / states with no sheet: basement plan, sections, roof plan, upper (attic) level; original 1887
    cafe-restaurant (Trevisanato) and 1909 conversion (Rickards) drawings; 1993-95 Brooks Murray refurbishment;
    exhibition layouts 2008-2016 and 2021-2025; the vector set of the British Council user guide.
G15. Hosts refused for R4 that may be open again: as G1-G3; muf.co.uk and www.villafrankenstein.com were DNS failures
    (domain gone; soft expiry passed, but a DNS failure is not worth a re-test without a new address).

## 2. Work log (in order)

### G1 British Council hosts (re-test after the soft expiry)
1. https://venicebiennale.britishcouncil.org/sites/default/files/2025_12_15_v2_updated_british_council_venice_architecture_open_call.pdf
   and /open-call: check 14:31 -> robots.txt now answers HTTP 403 -> HARD refusal of the host for the project. The
   2027 open call and its "British Pavilion User Guide" (drawings PDF, elevations PDF, floor loading, vector ZIP) stay
   in R4 hand.md H1 (browser only). Closed.
2. https://design.britishcouncil.org/blog/2018/dec/19/FAQ-venice-architecture-biennale-2020/ : check -> robots.txt
   HTTP 503 (soft refusal again, 30 min). Not retried. R4 hand.md H2 stays.
3. https://visualarts.britishcouncil.org/exhibitions/venice-biennale : check ALLOWED (robots.txt read), get -> HTTP 503
   (soft refusal again). Not retried. R4 hand.md H5.3 stays.
### G4 ASACdati catalogue (asac.labiennale.org/risultati, server-rendered __NEXT_DATA__)
4. ?termine=padiglione%20gran%20bretagna (check ALLOWED, get 200): fascicolifoto 538597 "Padiglione Gran Bretagna"
   (SEDI, PAD.STRANIERI.2.111-131, 1909-1996, 18 photos + 3 slides, nr. 130 and 131 "s.d. - Pianta"). Record page
   /collezioni/fototeca/fascicoli/538597 (get 200): no digitised image. -> row r104-0001 (archive-only pointer).
   ?termine=padiglione%20inghilterra, ?termine=padiglione%20britannico, ?termine=Rickards (get 200): fuzzy person hits,
   a 1995 poster (Leon Kossoff, "Padiglione Britannico", manifesti 216445, poster not a drawing), 1914 paintings
   titled "Inghilterra". Nothing else. GET search URL = borderline form use (same as R3; Rule log).
### G5 ASAC inventory PDFs on disk (local, no request)
5. 04-Architettura.pdf (R3's file): units with planimetrie / piante / agibilita for Gran Bretagna 2000-2018 ->
   row r104-0002 (archive-only pointer). 04-Arti_Visive.pdf and 04-Scatole_nere.pdf: no British unit naming plans.
### G2 archive.org (soft refusal expired 14:30; re-tested with new URLs)
6. advancedsearch (identifier:britainatveniceb0000unse OR title:Rickards OR creator:Rickards, Edwin): get 200, 133 hits.
   britainatveniceb0000unse: access-restricted-item true, collections inlibrary / printdisabled (controlled lending,
   170 images) -> may not be borrowed (rule 2); stays a library lead (R4 L6 / H6 updated in leads.md).
   artearickards "The art of E. A. Rickards" (1920, Cardiff University Special Collections, CC BY-SA 4.0): metadata get
   200; AEAR_djvu.txt (REDIRECT archive.org/download -> dn760103.eu.archive.org, checked anew, get 200): list of
   illustrations and full text read: no Venice pavilion (only "Fountains, Venice", a watercolour). Closed, EMPTY.
### G6 Wikimedia (closed again)
7. commons.wikimedia.org: refused HTTP 429 by R105 at 14:30:26 and upload.wikimedia.org 429 by R90 at 14:33:06 (hard,
   project-wide) before R104 reached them; R104's check of File:Map_of_Venice_Biennial.pdf, the BnF "Recueil. Biennale
   de Venise 1938" category, Category:11th_Venice_Biennale and Category:Edwin_Alfred_Rickards was REFUSED by the guard
   (nothing sent). Leads seen in the saved Category:Venice_Biennale page -> hand.md H-R1.
### WebSearch 1 (en): "British Pavilion" Venice Caruso St John "Island" plan section drawings archello OR divisare OR domusweb OR architecturetoday
   New hosts: architecturetoday.co.uk/island (gallery), worldarchitecture.org (credits "Island Architectural Drawings
   (c) Caruso St John"), somethingcurated.com 2018 interview, cca.qc.ca library record of the catalogue "Island" (2018,
   235 pp.). Dezeen (refused host). No Archello/Divisare/Domus hit.
8. https://architecturetoday.co.uk/island -> REDIRECT /island/ (checked anew), get 200: 3 Cultureshock Media + 11 Helene
   Binet photos on atlive-wp.s3.eu-west-2.amazonaws.com; no drawing in the .txt or the raw HTML. Photo source. EMPTY.
9. https://worldarchitecture.org/architecture-news/ehffm/island-named-special-mention-...html : get 200. FOUND copies of
   the four CSJ drawings (data-src cdnimgfiles/extuploadc/cstj_britishpavilion_island_groundfl / deckplan / eastelev /
   northele-1-.jpg), fetched (get 200): each 1190x841 (72 dpi), smaller than Metalocus (2048) and CSJ (4800) ->
   rows r104-0003..0006 with same_item_as. Other images: press photos (British Council) and drone photos. 
10. somethingcurated.com interview (REDIRECT to trailing-slash URL, checked anew, get 200): images are the press set
   (Holy Rosary Church, Raft of the Medusa plan (Correard, not the pavilion), Tempest, curators, John Riddy photo of
   the pavilion). EMPTY for drawings.
### Sighting of WA copies and of other routes' files (local)
11. The WA groundfl / eastelev / northele files are NOT the same renderings as the CSJ / Metalocus files: groundfl is a
   wider version of the 'Ground floor plan 1:200' (hill contours, French and German pavilion fronts and Canada
   partly drawn); the two elevations tone the existing pavilion facades (brick hatching, pediment, windows) and draw the
   scaffold light (sheet R104_3: CSJ north vs WA north). Rows r104-0003, 0005, 0006 kept as own rows (variants);
   deckplan is the same drawing as r4-0001 -> r104-0004 same_item_as r4-0001.
12. r101-0009 (kleihues+kleihues 2014 site plan, R101's file on disk): the British pavilion is drawn in plan in full
   (walls, front stair, rear loggia) -> row r104-0007 (gb, same_item_as r101-0009). The other kleihues sheets
   (ansicht 1-4, schnitt 1-5, Detailbilder 00/14/15; sheet R104_4) show only the German proposal: no British pavilion.
### WebSearch 2 (en): "British Pavilion" Venice Biennale exhibition plan drawing "Garden of Privatised Delights" OR ... axonometric
   Hits: visualarts.britishcouncil.org/programmes/exhibition/the-british-pavilion-at-the-venice-biennale-2009 (snippet:
   "Reg Butler's drawn plan" for the 1954 exhibition: British Council Collection), design.britishcouncil.org 2017 call
   (host closed), worldarchitecture.org 2016 call, BC 2020 open call PDF (host closed), e-architect 2012/2023 (refused;
   mail.e-architect.com is an alias of the refused host: not used), objectif (done).
13. https://worldarchitecture.org/architecture-news/ccffc/call-for-participation-venice-architecture-biennale-2016.html :
   get 200: one photo of the pavilion, link to the design.britishcouncil.org call (closed). No attachment. EMPTY.
14. Repository APIs: zenodo.org/api REFUSED by robots.txt (Disallow /api); api.core.ac.uk/v3/search/works: check ALLOWED,
   get -> HTTP 429 (CORE refused for the project; the v3 API wants a key). Closed.
15. 3GATTI on designboom (R4's saved raw HTML): img_2 render (seen by R4, not fetched) and the header
   fullscreen_1552384075_ef78da07...jpg (1800x650, composite of img_1 + img_2): check ALLOWED, get 200 both; viewed
   (sheet R104_5): renders of the inflated installation -> row r104-0008 (related); the composite gets no row.
### WebSearch 3 (it): Trevisanato 1887 caffè ristorante Giardini Venezia "padiglione" Gran Bretagna Rickards 1909 pianta OR rilievo OR tesi
   Hits: iris.unive.it bitstream "Padiglione centrale.pdf", exhibitions.univie.ac.at (DoME exhibition database, no
   drawings), labiennale.org/en/node/19, illy / Giardini Reali cafe (another building, Lorenzo Santi 1816-17). Nothing
   on the 1887 cafe-restaurant drawings.
16. https://iris.unive.it/bitstream/10278/3734099/1/Padiglione%20centrale.pdf (get 200, 1 page, 2 book pages 392-393)
   and the handle page (get 200): V. Pajusco, "Padiglione Centrale", in "Le muse inquiete. La Biennale di Venezia di
   fronte alla storia" (La Biennale, 2020), section "I Padiglioni dei Giardini"; photos of the Central Pavilion only.
   Not this pavilion. The same section may hold a British pavilion entry with ASAC photos / plans -> leads.md (library).
17. Slip: https://www.labiennale.org/it/bandi-e-gare/archivio was checked at 14:45, one minute before the soft refusal of
   www.labiennale.org (R3, 14:16:53) expired -> REFUSED by the guard (nothing sent). Under "a REFUSED is final for that
   URL" this URL and R4's refused /it/bandi-e-gare are not checked again.
### G3 www.labiennale.org (soft refusal expired)
18. https://www.labiennale.org/it/trasparenza (check ALLOWED after the expiry, get 200): "Bandi di gara e contratti" links
   only to /it/bandi-e-gare (refused URL for R4, not re-checked); "Opere pubbliche: non si applica". The national
   participation pages carry one thumbnail photo (R5's US page). No plan source. Closed; tenders -> leads.md N8.
### G9 exhibition curators' sites
19. https://www.crimsonweb.org/ (get 200), WP search API ?search=clockwork / ?search=british%20pavilion (get 200), media
   API parent=1502 and 1600, page /a-clockwork-jerusalem/ (get 200): two small photos (500x302, 292x389). No plan. EMPTY.
   https://real-foundation.org/ (Home Economics 2016, Jack Self): REFUSED, robots.txt unreachable (proxy 502, soft).
### WebSearch 4 (es/de/fr): "pabellón británico" OR "pabellón de Gran Bretaña" Bienal Venecia planta OR "Britischer Pavillon" Venedig Grundriss OR "pavillon britannique" Venise plan
   Hits: Metalocus (es) Island 2018 (done by R4 in en), Metalocus (es) 2021 "El jardín de las delicias privatizadas",
   ArchDaily (es) tag pages of the 2023 curators (Joseph Henry, Jayden Ali, Sumitra Upham, Meneesha Kellay), Arquitectura
   Viva tag "venecia" (refused host per earlier routes), others irrelevant. No German or French hit.
20. Metalocus 2021 article (get 200): 41 images; captions read: 01-38 photos, 39 title graphic, 40 collage triptych,
   41 exhibition room map (Kellenberger-White). 39-41 fetched (get 200, 2048 px) -> row r104-0009 (related, diagram).
   Metalocus 2025 selection article "22 participaciones" (get 200): no British pavilion entry. Closed.
