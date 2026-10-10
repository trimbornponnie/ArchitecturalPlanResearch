# R103 notes: gap route and completeness critic for R3 (French Pavilion, Giardini)

Route R103, slug `fr`, Plans folder `Plans/french/`. Started 2026-10-10 14:35 UTC.
Read first: BRIEFING.md (complete), R3 manifest.jsonl (70 rows), notes.md, leads.md, hand.md, R3's 576 lines in
`_work/guard/requests.jsonl` (221 gets), `_work/guard/refused_hosts.json` (state at 14:35), plan-sources.md,
Giudecca_critic.md, `Plans/french/index.csv` (41 sorted files).

State of shared hosts at 14:35: commons.wikimedia.org (429, R105, 14:30) and upload.wikimedia.org (429, R90, 14:33) are
CLOSED again (hard refusals), so the "Wikimedia reopened" window is over; R3 had already read
Category:Venice_Biennale_pavilions_(France) (6 photographs, no drawing) and Category:Giardini_della_Biennale_(Venice).
Soft (network/5xx) refusals that R3 met expire 30 min after their timestamp: www.labiennale.org (14:16:53),
christophehutin.com (14:16:37), www.muoto.fr (14:18:13), jakobmacfarlane.com (14:18:40), web.archive.org (14:19:41),
www.obras-architectes.fr (14:11:47), www.exyzt.org (520, 14:11:58), larchitecturedaujourdhui.fr (13:39),
dspace.unive.it (14:14:54), iris.iuav.it (14:18:33), catalogo.beniculturali.it (14:09:29).

## 1. Gaps in R3 (listed before acting)

G1. ASAC record pages never opened: R3 read the search JSON only. Fascicolo foto 538478 "Padiglione Francia" (SEDI,
    PAD.STRANIERI.2.38-50, item nr. 50 "Pianta") and 489837 (1976 allestimento) have record pages
    (/collezioni/fototeca/fascicoli/<id>, the form R104 used) that may list digitised items (getimg.php).
G2. www.labiennale.org national-participation pages for France (2014-2025 architecture and art years): two gets
    answered connection reset at 14:16; never read. Soft refusal expires 14:47.
G3. Ministry press kits of other years on culture.gouv.fr (allowed host): only the 2018 DP was read. 2014 (Cohen),
    2016 (Obras/AJAP14), 2021 (Hutin), 2023 (Muoto), 2025 (240503_GOUV_CP... attachment named but not fetched) and the
    Art Biennale kits (2017, 2019, 2022, 2024, 2026) were never looked for. Press kits often carry a plan of the pavilion
    with the exhibition layout.
G4. Exhibition websites of past French contributions never looked for (only the practices' sites were tried):
    2014 "Modernity: Promise or Menace?", 2016 "Nouvelles du front", 2021 "Les communautés à l'œuvre", 2023 "Ball
    Theater", 2025 "Vivre avec", 2017 "Studio Venezia", 2019 Prouvost, 2022 Sedira, 2024 Creuzet, 2026 Barrada.
G5. Architecture press that publishes exhibition plans and was never searched: Metalocus, Archello, Baunetz,
    afasia, AMC / Le Moniteur, d'architectures, Archistorm, Domus article pages (only the search URL 404'd),
    e-flux announcement pages (search disallowed, announcements not tried), Arquitectura Viva.
G6. Frac Centre Bouchain notebooks: 209 of 220 spreads never fetched (R3 lead L9, rule 8). Navigart gives no caption
    per spread, so drawing spreads cannot be picked without looking.
G7. Theses and repository APIs not queried: Crossref API, CORE, BASE, iris.unive.it / iris.iuav.it item pages (search
    pages closed by robots), DSpace unive (R3's http slip). No thesis on the pavilion found yet.
G8. 1912-1914 Biennale catalogues and guides (Giardini plan with the new French pavilion; 1912 photo plates):
    R3's archive.org title search returned only 1910; other title forms ("Catalogo illustrato", "Esposizione
    internazionale d'arte della città di Venezia", 1912/1914) not tried. The Ojetti 1912 PDF (photo of the pavilion)
    was not downloaded.
G9. Wikimedia Commons / upload.wikimedia.org: closed again (429 at 14:30/14:33, other routes) -> hand.md; R3 had read
    the France category (photos only). Deeper Commons categories (Claude Parent, Giardini maps) not reachable.
G10. 2025-26 renovation tender and project set: STBI (French Embassy) named, architect not; TED, BOAMP, PLACE
    (marches-publics.gouv.fr) and Italian press never searched. TED soft refusal (202, R101 14:11) has expired.
G11. Larger sizes not taken: designboom has "fullsize" variants for Ball Theater (fullsize-01/02 fetched); r3-0069
    (Ball-Theater-10, 818 px) has no fullsize checked. chroniques/inexhibit sizes were checked by R3 (originals).
    jeannouvel originals (about 2560 px) fine. Navigart max 1000 px confirmed in the API (max_width 1000): closed.
G12. Centre Pompidou collection (R3 lead L13) never queried; its online collection is also a Navigart instance
    (public API, like the Frac Centre's) -> check for Parent / Nouvel / Portzamparc / Architecture Principe items on the
    French pavilion.
G13. Practice sites refused by network errors only (Muoto, Jakob+MacFarlane, Obras, EXYZT, Hutin /projets,
    L'Architecture d'Aujourd'hui): each soft refusal expires; one re-test each after expiry.
G14. Sheet types / states with no sheet: original 1912 state (plan, elevations, section: none); 1922 rear-room
    addition (none); current state after the 2025-26 renovation (none); roof / skylight trusses (none); a modern
    measured plan of the whole pavilion (only Parent 1996 ink plan, 1000 px, and the 2018 cutaway axonometric 750 px).
    Exhibition plans 2006-2024 (Metavilla, Perrault, Lion, Cohen, Obras, Veilhan, Prouvost, Hutin, Sedira, Creuzet):
    none.
G15. Files on disk never sighted for drawing content: Frac Centre DP-Vivre-avec.pdf (28 pp), culture.gouv.fr 2018 DP
    (25 pp), tess.fr sheet (r3-0018, design_id `other` for the 2025 installation at the pavilion: to verify).

## 2. Following the gaps (in order)

### WebSearch 1 (fr): "pavillon français" Biennale Venise dossier de presse pdf plan du pavillon exposition 2021 OR 2022 OR 2024 OR 2026
Hits: jeannouvel (have it), culture.gouv.fr 2018 CP page, aphg.fr 2016 CP PDF, tess.fr (have it), culture.gouv.fr
switchToLanguage 266116 / 433850, 2019 Toulouse page. No press kit with a plan.
- culture.gouv.fr 2018 CP page (guard 200): attachment 20180222_CP-BiennaleArchitectureVenise.pdf (84 kB press release;
  the 25-page DP of the same day was read by R3) -> not fetched, no drawing expected.
- aphg.fr 2016 CP PDF (guard 200, 3 pp): "Nouvelles du front" press release, text only (page 3 one cover image). No row.
- culture.gouv.fr switchToLanguage/266116 -> REDIRECT (checked) 2019 Toulouse page (guard 200): Prouvost tour, photos
  only. switchToLanguage/433850 -> REDIRECT (checked) "Biennale de Venise : le Pavillon français entre en orbite"
  (5 May 2026, guard 200): FACT (confirmed): Barrada 2026 rooms named "Salle des plis", "Salle de travail", "Salle des
  Lumières"; images are artworks and portraits, no plan. No row.
### G1 ASAC record pages (closed)
- asac.labiennale.org/collezioni/fototeca/fascicoli/538478 (guard 200): "Padiglione Francia", SEDI, faldone 0002,
  PAD.STRANIERI.2.38-50, 1930-1996, 13 originals (10 photos, 3 slides): nr. 48 (1996 facade), nr. 49 (facade), nr. 50
  "s.d. - Pianta"; photographers Graziano Arici, Tomaso Filippi, Giacomelli; note "Costruito nel 1912, progetto di
  Umberto Bellotto". NO digitised image on the record page -> same item as r3-0070, no new row.
- fascicoli/489837 (guard 200): 1976 "L'ambiente - Francia" (A.V.118.1976.1-55), installation photos. No row.
### WebSearch 2 (it): "padiglione francese" OR "padiglione della Francia" Giardini Biennale restauro rinnovo 2025 lavori progetto architetto lucernari
Hits: labiennale ASAC "Biennale Works in Progress", Central Pavilion 2026 (R30), Canada 2018, Venezuela (R9). Nothing on
the French pavilion renovation: architect and tender still not traced (G10 open).
### WebSearch 3 (en): French pavilion plan section drawings on metalocus / afasia / baunetz / amc
Hits: jeannouvel, archdaily tag, italyworldsfairs Turin 1911 (trap, other building), myartguides 2015, e-flux
directory 52404, tess.fr. No press page with plans.
- Site searches: metalocus.es search REFUSED (robots Disallow /*?*keys); archello.com REFUSED (robots.txt 403 -> host
  refused for the project); baunetz.de /suche REFUSED (robots). -> hand.md H3.
- e-flux directory 52404 "French Pavilion at the Venice Biennale" (guard 200): 15 announcements listed (2008-2026):
  127812 Veilhan 2017, 245572 Prouvost 2019, 29682 Boursier-Mougenot 2015, 35615 (2011), 38076 Lévêque 2009, 39071 (2008
  architecture), 413849 Hutin 2021, 42066 Messager 2005, 438576 Sedira 2022, 514459 Ball Theater 2023, 52406 Veilhan,
  551067 Radio Utopia, 601579 Creuzet 2024, 646909 Vivre avec 2025, 6787311 Barrada 2026. Checked six (ALLOWED); the first
  get (413849) failed with an SSL EOF -> www.e-flux.com soft-refused (network) for 30 min from 14:46. Retry later.
### G11 sizes
- designboom Ball-Theater-10-.jpg is already the original (no -WxH suffix; srcset tops at 768 px); 818x447 stays.
- Navigart: API field max_width = 1000 for every media: 1000 px is the largest offered (closed).
### G2 www.labiennale.org (soft refusal expired 14:47)
- /en/architecture/2025/national-participations/france: HTTP 404 (R3's URL form is wrong); the right form is
  /en/<architecture|art>/<year>/france. Fetched (guard 200): architecture 2025, architecture 2023, art 2026, art 2024:
  text only (commissioner, curators, exhibitors list), no image, no plan. ASAC "Biennale Works in Progress"
  (REDIRECT checked, guard 200): 2010 exhibition of the Biennale's own buildings, nothing on the French pavilion.
### G6 Frac Centre: Bouchain "Les Métavilla, Venise" notebooks (Navigart)
- Notebook 016 090 001 (67 images 4M22386..4M22452; R3 had 4M22386, 22420, 22440): checked the 64 missing URLs
  (ALLOWED), fetched all (guard 200 each), viewed all on sheets R103_6..R103_11 (+ R103_12 at larger size). The notebook
  is Bouchain's design notebook for the 2006 French pavilion: 25 spreads draw the pavilion (plans with the inhabited
  rooms, coloured zoning plans, scaffold axonometrics, front elevations with the scaffold tower, a section collage, a
  site sketch) -> rows r103-0001..r103-0025 (fr-reno, exhibition layout 2006). The rest are notes, clippings, a budget
  sheet, press releases and photos of the pavilion (no rows).
- Notebooks 002-005 (145 images not yet fetched): checked ALLOWED, fetching (background) to sight them the same way.
### Sighting of R3's files (contact sheets R103_1..R103_5, tess PDF page R103_tess.jpg)
All 61 downloadable R3 files on disk were viewed and measured (peek info): every pixel size in R3's rows matches the file.
All show this pavilion or its own exhibitions/competitions (no neighbour, no other venue). Fixes in corrections.json:
r3-0014 = mirrored copy of r3-0013 (same_item_as); r3-0068 is a longitudinal section sketch of the whole pavilion with the
Metavilla scaffold (count_as drawing, shows_state renovation); r3-0063..0067 are photographs of notebook covers
(sheet_type other). r3-0018 (T/E/S/S sheet) shows only the 2025 temporary scaffold pavilion and its details, not the
French pavilion: design_id other / related stays. Frac Centre DP-Vivre-avec.pdf (28 pp) and the 2018 ministry DP
(25 pp): pdf-text grep confirms R3 (photos and text only, no drawing).

## Rule log

