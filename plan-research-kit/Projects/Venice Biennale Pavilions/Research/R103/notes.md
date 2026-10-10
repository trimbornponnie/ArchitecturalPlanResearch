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

## Rule log

