---
name: rekon-sources
description: Stages 1 and 2 of the reconstruction pipeline. Stage 1 finds, downloads and indexes drawings (or indexes user-supplied sheets on the manual route), gives the reconstructability verdict and fixes the route. Stage 2 acquires images from open repositories and street panoramas with a bearing filter and a sample sighting. Argument is the building slug; the stage comes from state.json.
disable-model-invocation: true
argument-hint: <slug>
allowed-tools: Bash(tools/rekon.sh *) Bash(tools/rekon.cmd *) Bash(tools/.venv/Scripts/python.exe *) Read Write Edit Glob Grep WebSearch WebFetch Agent
---

# Stages 1 and 2 · sources

First visible line: `Loaded skill rekon-sources (stage <1|2>). Governing rules: plansatz habit, part classes as the stop rule, vector before raster, expectation per order, bearing filter, sample before harvest, rights in every sidecar.`

Slug: `$ARGUMENTS`. Read `state.json`; `stage` says whether this is 1 or 2. Run only that one.

---

## Stage 1 · plans

Output: `02-sources/plans/` with `index.csv` (columns: file, sha256, provenance, type, note,
added, status), a sidecar per sheet, `search-log.jsonl`, `gaps.json`, `requests.json` when a
request was drafted, and `verdict.md`.

The stop rule is the gap table, not the sheet types: the search ends when every one of the
fourteen part classes of `break.md` is `covered`, or its gap carries a logged search or a drafted
request (method review X2; incident: the Wallarkaden verdict called the two basements "not
needed" while csj_05 and csj_06 drew them, 2026-09-23).

1. `tools/rekon.sh start <slug> 1`
2. **Manual route** (`route: manual`): `tools/rekon.sh import <slug> <files>` for everything in
   `02-sources/plans/inbox/`. Import goes through `add_sheet`: sidecar, sha256, pixel size,
   vector flag, the scale printed in a vector PDF, and the page size of a vector PDF as a
   measured sheet size. Give `--type` when the file name does not say it, and `--sheet-size` with
   `--sheet-size-source` when a title block states it. A sheet indexed without a sidecar (before
   X2) gets one on re-import ("sidecar added"). No web search. Go to step 5.
3. **Web route**: search in the order of `references/plan-sources.md` and log every source,
   empty or not: `tools/rekon.sh search-log <slug> --class <0..9> --query "..." --outcome
   found|empty|"not readable"|skipped [--sheets n] [--note]`. The first queries come from the
   stage-0 leads: `tools/rekon.sh harvest <slug> --seeds`.
   - For a building of the last thirty years the first source is the architect's and the
     developer's own project page (Wallarkaden 1.1: nine sheets, csj_01 to csj_05 at 4800 px and
     csj_06 to csj_09 at 4000 px, on carusostjohn.com). For a 20th-century building the
     architects' foundation or estate comes before the building's own institution (Centre
     Pompidou 1.1).
   - Read a page with `tools/rekon.sh harvest <slug> <url> --class <c>`: it lists `srcset`,
     `data-src`, `og:image`, PDF / TIFF / CAD links and IIIF manifests from the raw HTML, largest
     first, and logs the search. Never read a page through the fetch summariser (1.2: it reported
     "no image URLs" and invented a pattern; 1.4: it reported the 232 px thumbnails).
   - Index a sheet with `tools/rekon.sh sheet <slug> <url> --type T --provenance "..."`. It asks
     robots.txt first, waits between requests, backs off on 429, retries a hotlink guard once
     with a browser User-Agent only where robots.txt allows it (1.7), writes to a temporary name,
     refuses a second file under a taken name ("collision"), and refuses sheets under
     `--min-px 2000` (1.4). The licence stays `unconfirmed` until a human is named with
     `--license-confirmed-by`. Known URLs in bulk: `02-sources/plans/fetch_sheets.py` (copy the one
     in buildings/centre-pompidou) with `rekon.plans.fetch.fetch_list`, same checks.
   - A `fetcher` subagent (haiku) is for pages that still need reading to find the URLs; give it
     a step budget and the `rekon sheet` line.
   - On a shared square or corner the title block's site line decides which building a sheet
     shows, not the portal's address field (1.2: both competition hits were the neighbour).
     Design sheets of a built building (revision indices, "Tektur") make the route `hybrid`,
     never `plans`: the panoramas verify the built state (1.7). A title-only hit on a collection
     site is checked on its ensemble field (1.5). Engineering journals are searched on the
     design years (1.9). Sources that refuse (connection, 403, login) are logged as "not
     readable" (1.8).
   - Sheets found are downloaded and indexed at once (plansatz habit); whole archives are never
     bulk-scraped (incident: 1,862 Himeji sheets started downloading before the user stopped it,
     2026-09-17). A IIIF manifest gives whole images (`full/max`), never tiles.
4. For every sheet the sidecar `<file>.json` is the record, the index a list (1.5): provenance
   URL, licence and its status, author/institution, sheet type (plan / section / elevation /
   framing / detail / table / other), vector or raster, scale if printed, pixel size, sheet size
   with its status and source, sheet number, title, date and revision, `status: unread`. A sheet
   size read off the title block or an archive catalogue is `measured` with
   `sheet_size_source`; a size without a source is `assumed`, and the verdict says so (the
   Wallarkaden "A0" was an assumption: csj_08 and csj_09 are 1300 and 1600 mm wide). Unknown
   provenance = unusable, keep the row and say so (incident: three genuine official sheets with
   no recorded origin had to be flagged unusable, Yakushi-ji 2026-09-18).
5. **Gaps and verdict**: `tools/rekon.sh verdict <slug>` writes
   `02-sources/plans/verdict-skeleton.md` and `gaps.json`. Per sheet: px per sheet mm (text:
   2.5 mm lettering needs about 8 px, `READ_PX`), px/m on the building (geometry: bays need
   about 10 px/m), and the glyph probe's small-text height where the sheet size is unknown
   (P 1.6: present is not measurable). Per part class: its candidate sheets and whether the best
   of them is legible (`covered / weak / unknown / gap`). Fill `references/reconstructability.md`'s
   judgement into `02-sources/plans/verdict.md` from it.
6. **Requests for what is missing**: for every `weak` or `gap` class the web cannot fill, draft
   a request: `tools/rekon.sh request <slug> draft --to "<office or archive>" --kind
   permit-file|public-records|archive|owner --classes basement,roof-build-up [--sheets "<names
   or archive codes>"] [--address "..."] [--language de|en]`. It writes the letter under
   `02-sources/plans/requests/`, a row in `requests.json` and an open question. rekon never sends
   it; the user does, and moves it on with `tools/rekon.sh request <slug> set <id>
   sent|answered|refused|withdrawn --human "<name>"`. A German building authority's file
   (Bauakte) is not public: the owner asks, or someone holding the owner's written authorisation
   (Vollmacht); the letter names who may ask, and the user checks the office's own rules.
7. Route: `plans` (the envelope, slab, core and stair classes `covered`, the rest covered or
   requested), `hybrid` (some), `street` (none usable), `manual` (user-supplied). Vector before
   raster is a preference, not a gate.
8. Journal entry; then `tools/rekon.sh done <slug> 1 --route <plans|hybrid|street|manual> --count sheets=<n> --count vector=<n> --model <m> --effort <e> --turns <n>`
   (cost capture, P 1.12: the model and turns the session shows). `done` prints the gap finding
   and the sheets whose size has no source (warn-only). Print the checkpoint verbatim. Stop.

---

## Stage 2 · images

Output: `02-sources/images/` with per-source folders, a sidecar JSON per image, `index.jsonl`,
`orders.json`, `yield.json`, and `sighting-sample.md`.

1. `tools/rekon.sh start <slug> 2`
2. Write `orders.json` (schema: `tools/rekon/images/ORDERS.md`). Order sources, tightest first:
   - Commons: the Wikidata Commons category and its subcategories by name (`deepcategory:`),
     plus `intitle:` searches with the building's names in the local languages. Never a bare
     term (incident: a bare term matched every Cologne photo with a Slavic caption).
   - Flickr with licence filter, only with a tight title/tag query.
   - Mapillary and Panoramax around the footprint with the bearing filter ON.
   - Street panoramas: Look Around and Street View at the computed viewpoints
     (`rekon.images.viewpoints`, then `rekon.images.sources.lookaround` / `streetview`).
   Each order carries `expectation` (confirmed / thin / empty) and the two-floor megapixel rule
   (a low floor for tight orders; incident: a 20 MPix floor dropped a whole roof tour at 18 MPix).
   Flickr needs `FLICKR_KEY`, Mapillary `MAPILLARY_TOKEN`; without them the order is skipped,
   so do not write it (2.2). On a building finished recently, street-photo sources return the
   construction site (2.6): the runner's `--min-date auto` (default) takes the END of the
   completion period (a year-only "2022" is a floor at 2022-12-31: a frame inside the year
   cannot be shown to postdate the completion, 3.9) and drops older Mapillary / Panoramax hits
   as `too_old`. The completion comes from the record in `state.json` first, then from
   `01-identify`. When neither exists the run says so: find the date (architect page, press,
   permit) and set it with `tools/rekon.sh completion <slug> <YYYY[-MM]> --status measured
   --source "<where it was read>"` before the harvest; failing that, the sample sighting must
   ask "finished building or site?" and the order is dropped on "site". `--max-date auto` reads
   the `valid_until` record (`rekon completion <slug> <date> --until ...`) and drops later
   frames as `too_new` (Centre Pompidou, closed for renovation until 2030). Repository orders
   get either bound only when you write one (old plates are the point of an archive order).
3. Dry run first: `tools/.venv/Scripts/python.exe -m rekon.images run orders.json --out ... --contact office@ponnie.net --dry-run`.
   Read the counts and the date-floor line. An order expected `empty` that returns nothing is a finding, not an error.
4. **Sample before harvest**: `run ... --sample 5` (no second order file; `max_items` counts
   across runs, so the harvest continues from the sample, 2.8), spawn one `image-sighter` subagent
   (sonnet, low) on the sample with the schema in `references/sighting.md`. If fewer than half of
   a source's sample show the building, drop (`--drop <id>`) or narrow that order before harvesting.
5. Harvest with the tuned orders (`--only` / `--drop` by id). Then `tools/.venv/Scripts/python.exe -m rekon.images yield <dir>` and write `yield.json`.
6. Street panoramas: run viewpoints, then `rekon.images.viewpoints.mark_party_walls` with the
   neighbour rings from `01-identify/neighbours.json` (a facade whose outward side lies inside
   another building is no facade and gets no panorama, 3.6), then lookaround and streetview with
   `--max-per-facade 3`. Street View takes the newest historical panorama inside the date
   window by itself (`--min-date auto`, `--max-date auto`, 3.9) and prints the date per
   panorama; Look Around drops captures outside the window before scoring and lists them in
   `panoramas_refused_by_date`. Write the dates into the count line. One tile failure is retried once (2.3).
   Sidecars carry `license_status: provider-terms, private research only, do not redistribute`.
7. `sighting-sample.md`: per order hits / accepted / on-target from the sample; `machine_sighted`
   only. `sighted` is set by a human, never here.
7b. **Evidence table per front** (method review X7): `tools/.venv/Scripts/python.exe -m
   rekon.images.evidence buildings/<slug> --out buildings/<slug>/02-sources/images/evidence.json`.
   Per front and aspect (openings, detail, crown, massing step) the best source with its date,
   native px/m on the wall, licence class and the share of the front the aerial clip leaves
   clear. It reads `01-identify/witness/` when `rekon.geo.witness` has run (NRW: run it here, it
   needs only the outline); without it, occlusion is unjudged and says so. A source dated before
   the completion record is listed, never best. A camera standing under a tree crown is not
   counted as blind by the crown above it. Its findings print at `done 2` (warn-only): a street
   front without a usable source for openings, and a party wall with panoramas assigned. On the
   Wallarkaden: F01-F04 with three panoramas each (3.6), and F08 without a source (the plane
   tree). Write each finding into the journal with what stage 3 does about it.
8. Journal entry; `tools/rekon.sh done <slug> 2 --count images=<n> --count panoramas=<n> --count on_target_sample=<n>`.
   Print the checkpoint verbatim. Stop.

## Rules for both stages

- Rights are recorded, not investigated: no licence enquiry before knowing a set shows anything.
- `kind: new` buildings never reach stage 2 unless the user reopened it with renderings or site photos.
- Subagents get a step budget in their prompt and write to disk as they go.
