# Where drawings come from

Ordered from most to least likely to yield vector or measured sheets. Each entry: what it holds,
how to query, what was learned. Status of each lesson: `confirmed` unless marked. The number of
each heading is the source class of the search log (`rekon search-log --class`); every class
searched is logged, empty or not, and the verdict lists them.

## 0. The architect's and the developer's project pages (buildings of the last thirty years)

For a recent building the first and richest source is the practice's own project page: the
Wallarkaden page on carusostjohn.com serves the nine sheets of the 2018 Leitdetailplanung (plans
and sections 1:100, elevations 1:50, dimension chains, NHN marks; csj_01 to csj_05 at 4800 px,
csj_06 to csj_09 at 4000 px, csj_08 and csj_09 on 1300 and 1600 mm wide sheets, not A0), and
nothing in the classes below points there (Wallarkaden 1.1). Query `<practice> <building>`
and `<building> site:<practice domain>`; developers' and contractors' pages come next. Read
the raw HTML, never the page summary: the sheets sit in `srcset` / `data-src` variants (232 px
in the page, 4800 px in the srcset, 1.4); `rekon harvest <slug> <url>` lists them largest
first. Index with `rekon sheet <slug> <url> --type ...`. The stage-0 leads give the first
queries: `rekon harvest <slug> --seeds`.

## 1. The building's own institution

Museums, foundations, cathedral works, universities. Search `<name> archive drawings digital
collection`, `<name> plans pdf site:<institution domain>`. Example: Centre Pompidou has a digital
architecture collection (1972-2011) on centrepompidou.fr; the 1971 competition originals were
rediscovered in 2024 and are being digitised (Domus, 2024-01-30). Cathedral archives are often
on-site only (Dombauarchiv Köln: ~20,000 plans, appointment only, no online catalogue; contact
archiv.dombauhuette@koelner-dom.de).

## 1b. The architects' foundations and estates (20th-century buildings)

Fondazione Renzo Piano, RSHP, Fondation Le Corbusier, Alvar Aalto Foundation, Frank Lloyd
Wright Foundation / Avery, Getty (Eames, Neutra, Lautner), Norman Foster Foundation, Vitra.
For a building of 1920-2000 look here BEFORE the building's own institution: the Fondazione
Renzo Piano page for the Centre Pompidou holds the whole construction-set catalogue (51
drawings with archive codes, dates, scales and drawing numbers) while centrepompidou.fr holds
sketches and models at thumbnail size (Centre Pompidou dry run 1.1, 2026-09-23). The catalogue
is the value even when the copies are small: it names the sheets a research request would ask
for (`rekon request <slug> draft --kind archive --sheets "<codes>"`). Harvest the page with
`rekon harvest`, which reads `data-src` / `srcset` / IIIF links from the raw HTML; the fetch
summariser reads prose and invented a URL pattern here (1.2). Measure what arrives: the uncached
"original" was 550 px on the short side, the "print" PDFs smaller still (1.3): 0.6 to 1.3 px per
sheet mm, so no dimension text is legible on any of the 51 (X2).

## 2. National heritage survey programmes (measured sheets)

- USA, HABS/HAER/HALS at the Library of Congress: measured drawings as 400 dpi TIFF, often 1-bit
  CAD prints. Catalogue pages block automated fetch, the file server does not:
  `https://tile.loc.gov/storage-services/master/pnp/habshaer/<st>/<st>NN00/<id>/sheet/0000Na.tif`
  (Eames House CA-2903, 13 sheets, downloaded 2026-09-18).
- Korea, Korea Heritage Service (국가유산청): full repair/survey reports as free PDFs; reports after
  ~2010 are true vector (Sungnyemun 2013: 102 vector pages). The one place where canon, vector and
  free access coincide.
- Japan: Nabunken repository (repair reports, e.g. 1956 Yakushi-ji east pagoda, ID 73686, 116 pp
  at 400 dpi); municipal boards of education publish born-digital repair reports (Sodegaura 2014:
  38 pure vector pages); Agency for Cultural Affairs tender documents can carry full component
  schedules. No DXF/DWG for any National Treasure was ever found.
- UK, The National Archives and Historic England; Germany, Landesdenkmalämter and state LoD2
  (massing only, roof heights untrustworthy).

## 3. Wikimedia Commons and Wikidata

`Category:<Building>` and its subcategories `Floor plans of ...`, `Architectural drawings of ...`,
`Sections of ...`. Query with `deepcategory:"<category>" filetype:drawing` and
`intitle:"<name>" plan`. Historic plates (19th-century Tafelwerke) often live here at high
resolution; for a building still under copyright (architect died after 1955) Commons holds
photographs only (Centre Pompidou: 13 subcategories, no drawings, 1.13). Wikidata P373 gives the category; P84 the architect (whose own archive may hold sheets).

## 4. Published raster plans (last resort for geometry, first for orientation)

ArchDaily, Dezeen, ArchEyes, archINFORM, Domus, El Croquis: small raster plans and sections,
usually unscaled. Good for storey count, bay rhythm, plan shape; not for measurement. Index them
as `raster, unscaled` and never calibrate a model on them alone.

## 5. Archives and libraries with scans

Europeana (`europeana.eu/api`), archive.org (`plan`, `elevation`, `section` with the architect's
name), Bibliothèque nationale (Gallica), Bayerische Staatsbibliothek (IIIF), university
repositories. Expect anisotropic scans (~1.5 %): calibrate on printed dimension chains, never on
the scale bar.

## 6. Permit and competition sets (real jobs)

The user's own PDFs (permit sets at 1:100, competition sheets at 1:200): true vector, colour-
coded (black existing, red new, yellow demolition). Everything is line segments; there are no
rectangles to find. Snap to the drawing raster (2.5 cm at 1:200) or 1 mm slivers appear.
Supplied files enter with `rekon import`, which reads the printed scale and the page size of a
vector PDF (Gartenhaus: five sheets, 1:100, A3). A permit file that is not public is asked for
with `rekon request <slug> draft --kind permit-file`: in Germany the Bauakte is open to the
owner or to someone holding the owner's written authorisation; the letter is drafted, never
sent by rekon.

UK planning portals (Idox Public Access and its kin) disallow robots in their robots.txt; `rekon
sheet` refuses them, and a human downloads the sheets and imports them (`rekon import`). No
scraper for them is written (method review, "do not do").

## 7. Survey data as substitute for drawings

Airborne LiDAR (heights, roof planes), state photogrammetry meshes (SLPK/I3S; partial extraction
with HTTP range requests works), LoD2 CityGML. Heights from the cloud, vertical alignment from
the mesh; LoD2 roof heights untrustworthy (Cologne: +6.6 m on a turret, -1.9 m on the towers).
In NRW the witness (`rekon.geo.witness`, DGM1/DOM1/TrueDOP, dl-de/zero) and the roof plan from
the true ortho (`rekon.geo.roofplan`) are stage-3 and stage-4 tools; here they are logged as
class 7 only when they stand in for a missing sheet.

## 8. Registers

Where a building's drawings sit in a register, the register is searched by address or parcel
and logged as class 8, whether or not it answers. Status of every line: `unconfirmed`, not yet
used on a dry run.

| Jurisdiction | Register | What it gives | Access |
|---|---|---|---|
| Germany | Bauaufsichtsamt of the town (Bauakte) | the permit set, often with statics | owner or authorised person, on request |
| Germany | Denkmalliste / Landesdenkmalamt | listing text, sometimes a measured survey | public text; surveys on request |
| UK | local planning authority (Idox Public Access and kin) | applications since about 2000, PDFs | public; robots.txt disallows, a human downloads |
| USA, New York | Department of Buildings (BIS / DOB NOW) | scanned plans for many filings | public records |
| Netherlands, Amsterdam | Stadsarchief bouwtekeningen | permit drawings | public records, some on request |
| France | Archives municipales / départementales (permis de construire) | permit files | reading room |

## 9. Trade press and participants

Structural engineers, facade consultants, suppliers and contractors publish reference pages and
articles with sections and details that the architect's page leaves out. Search the building
with the trades: `<building> Tragwerksplanung`, `<building> structural engineer`, `<building>
Fassade <supplier>`, the construction years in the trade journals (1.9). Examples, `unconfirmed`
until a dry run uses one: the Wallarkaden structural engineer's reference page (kevee.com / IDK
Kleinjohann, Tragwerksplanung) and the brick supplier's page (backstein-kontor). On a shared
square the supplier's page shows its own building's facade only if its caption names the
address; the shared-square rule of the traps below holds here too.

## What to record per sheet

file, sha256, provenance URL, licence and its status, author or institution, sheet type,
vector/raster, scale as printed, MEASURED pixel size, sheet size with status and source, state
(year the drawing shows), status `unread`. `rekon.plans.fetch.add_sheet` writes all of it, for
downloads (`rekon sheet`) and for supplied files (`rekon import`) alike; known URLs go into a
per-building `02-sources/plans/fetch_sheets.py` (template: buildings/centre-pompidou), not to an
agent. A sheet whose provenance is unknown is indexed and marked unusable. A licence is
`confirmed` only with the name of the human who confirmed it.

## Traps

- The original may itself be the thumbnail: measure the file, never trust the page (Wallarkaden
  1.4 went one way, Centre Pompidou 1.3 the other).
- srcset: a fetch summary reports the image the page shows (232 x 116 px); the 1200 / 2400 /
  3600 / 4800 variants live only in the `srcset` and `data-src` attributes of the raw HTML.
  Before indexing any image found on a page read the HTML for larger variants, record the
  pixel size in the sidecar, refuse anything under about 2000 px as a sheet (Wallarkaden 1.4).
- Shared square: on a corner or a square two buildings share the street address. Both
  competition hits for the Wallarkaden were the neighbour (Haus am Rudolfplatz) filed under
  the same street; the title block's site line decides, not the portal's address field
  (Wallarkaden 1.2).
- A title-only hit on a collection site ("Plan", "Élévation" by the architect) can belong to
  another building: check the ensemble / series field first (1.5: Lloyd's drawings under a
  Beaubourg search).
- Engineering journals covered the DESIGN years: the Arup Beaubourg issue is June 1973, four
  years before the opening (1.9). Search the construction dates, not the completion date.
- A page that serves a 52-byte body to a research User-Agent has a hotlink guard: `rekon sheet`
  retries once with a browser User-Agent and `Referer`, only where robots.txt allows the path,
  and says so in the sidecar (1.7).
- Sources that cannot be read (connection refused, 403, login) are listed in the verdict as
  "checked, not readable", neither absent nor checked (1.8).

- "Vector and canon diverge" really means "vector and public access diverge" (confirmed twice).
- Historic sheets show ideal completions or superseded states (Boisserée 1821; 1860 zinc roof
  replaced 1961-73): record the state shown.
- Feet: Roman, Paris and Rhineland feet stand side by side on 19th-century sheets and no sheet
  says how many metres a foot is. Record the unit as `open` until a chain proves it.
- pdftotext silently drops en- and em-dashes: read dimension ranges with pymupdf and gap widths.
