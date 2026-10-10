export const meta = {
  name: 'biennale-pavilion-plans',
  description: 'Research, download and sort the architectural plans of one Venice Biennale pavilion (research, download, gap-fill and sighting, download)',
  whenToUse: 'One pavilion from Projects/Venice Biennale Pavilions/pavilions.json; args = {pavilion, research?}. Run five of these at once for a batch.',
  phases: [
    { title: 'Research', detail: 'research route, every request through tools/guard.py' },
    { title: 'Download', detail: 'tools/finish_route.py: merge, fetch, sort into Plans/<folder>/Vectorized|Rasterized' },
    { title: 'Gap and sighting', detail: 'completeness critic follows every missed lead, checks each file shows the pavilion' },
  ],
}

const KIT = '/home/user/ArchitecturalPlanResearch/plan-research-kit'
const PROJ = 'Projects/Venice Biennale Pavilions'

const RESEARCH_SCHEMA = {
  type: 'object',
  properties: {
    route: { type: 'string' },
    rows_total: { type: 'integer' },
    files_downloaded: { type: 'integer', description: 'files fetched with guard.py get that are drawings or documents with drawings' },
    vector_candidates: { type: 'integer', description: 'rows that are DWG/DXF/SVG or PDFs that look vector' },
    sources_tried: { type: 'integer' },
    hosts_refused: { type: 'array', items: { type: 'string' } },
    leads_open: { type: 'integer', description: 'entries in leads.md not downloaded' },
    hand_items: { type: 'integer', description: 'entries in hand.md for the user browser' },
    searches_used: { type: 'integer' },
    rule_slips: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string', description: 'five lines at most: what was found, the best sheets, what is still missing' },
  },
  required: ['route', 'rows_total', 'files_downloaded', 'hosts_refused', 'leads_open', 'hand_items', 'searches_used', 'rule_slips', 'summary'],
}

const GAP_SCHEMA = {
  type: 'object',
  properties: {
    route: { type: 'string' },
    gaps_found: { type: 'integer' },
    gaps_closed: { type: 'integer', description: 'gaps followed to the end (downloaded or settled as closed with a reason)' },
    rows_added: { type: 'integer' },
    files_downloaded: { type: 'integer' },
    files_sighted: { type: 'integer' },
    corrections: { type: 'integer', description: 'entries written to corrections.json' },
    wrong_building: { type: 'array', items: { type: 'string' }, description: 'row ids whose file does not show this pavilion' },
    still_missing: { type: 'array', items: { type: 'string' }, description: 'sheet types / states / sources nobody could reach, with the reason' },
    searches_used: { type: 'integer' },
    rule_slips: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
  required: ['route', 'gaps_found', 'gaps_closed', 'rows_added', 'files_downloaded', 'files_sighted', 'corrections', 'wrong_building', 'still_missing', 'searches_used', 'rule_slips', 'summary'],
}

const FINISH_SCHEMA = {
  type: 'object',
  properties: {
    exit_code: { type: 'integer' },
    files_total: { type: 'integer' },
    vectorized: { type: 'integer' },
    rasterized: { type: 'integer' },
    errors: { type: 'array', items: { type: 'string' }, description: 'error / refused / bad_content lines of this pavilion, and any crash' },
  },
  required: ['exit_code', 'files_total', 'vectorized', 'rasterized', 'errors'],
}

const COMMON = (p) => `
You work in ${KIT} (cd there first in every Bash command, or use absolute paths). Python is python3.
The project is "${PROJ}". Read "${PROJ}/Research/BRIEFING.md" completely before anything else and follow it exactly:
every web request through tools/guard.py (check as its own command, get in a later command), no curl/wget/urllib/
requests, WebFetch only after "check --as claude-user" and followed by "webfetch-done", a REFUSED or 401/403/429 is
final for that host, no redirect followed without a new check, never Read an image over 1 MB (use tools/peek.py sheet
or pdf-pages first). Read "${PROJ}/_work/guard/refused_hosts.json" (if it exists) before you start on a host; it is
re-read on every guard call, so a host taken off the list (after a User-Agent fix) may be used again.
Several gets in one Bash command only as "for u in ...; do python3 tools/guard.py ... get \\"$u\\" || break; done",
nothing piped after the get, nothing chained after the loop (earlier routes slipped here).
Also read reference/upstream/rekon-sources/references/plan-sources.md (source classes 0-9 and traps) and skim
reference/upstream/research-building-plans/Giudecca_critic.md (what earlier routes missed: unopened albums, lazy-
loaded lists, srcset variants, licence pages, theses and repository APIs nobody queried).

User instructions that override any narrower habit: download ANY accessible file of these drawings regardless of
its licence (personal project) and skip no lead: every lead is followed to its end or written to leads.md/hand.md
with the exact URL and why it stopped. Prefer vector files (DWG, DXF, SVG, vector PDF) and the largest raster size.
Scope: the Giardini only.

Pavilion: ${p.name}. Slug "${p.slug}" (design ids ${p.slug}, ${p.slug}-alt, ${p.slug}-reno, ${p.slug}-unk). Plans
folder Plans/${p.folder}/. Facts to confirm (leads, not readings): ${p.facts}
Design id reminder: "-alt" is only for schemes that were never built (competition entries, unbuilt proposals);
an exhibition, installation, survey or catalogue that documents the real pavilion is "${p.slug}-reno" (or
"${p.slug}" for the original state), never "-alt".
Other routes research other pavilions at the same time; stay on this pavilion. A drawing that shows several pavilions
(a Giardini site plan, a pavilion pair) gets a row with design_id "${p.slug}" when this pavilion is drawn in full,
and its notes name the other pavilions.
If your route folder already holds files from an interrupted run of the same route, read them first and continue
from where it stopped: keep its rows (append new ones with the next row numbers), do not repeat sources notes.md
records as done.`

const researchPrompt = (p) => `${COMMON(p)}

You are research route ${p.route}. Your files: "${PROJ}/Research/${p.route}/" (manifest.jsonl, notes.md, leads.md,
hand.md; create the folder). Row ids "${p.route.toLowerCase()}-0001", "${p.route.toLowerCase()}-0002", ...
WebSearch budget: 8 searches. Write each row the moment you have it and update notes.md after each source, so a stop
leaves resumable files.

Search every source class of plan-sources.md that can apply, in order, and log each in notes.md (found / empty /
not readable): 0 architects' and later interveners' project pages (renovations, exhibition designers who surveyed the
pavilion); 1 La Biennale and ASAC, the commissioning body's pages and its calls for proposals / tender documents
(they often carry survey plans as PDF or DWG annexes), the pavilion's own website and its year archives; 1b architects'
archives, estates and the national architecture museum / archive of the country (online collection search); 2 heritage
survey records (Italian MiC catalogues, Comune di Venezia, Soprintendenza); 3 Wikimedia Commons and Wikidata (category
of the pavilion and its subcategories, file search for plan/pianta/Grundriss/section); 4 published plans (ArchDaily,
Divisare, Dezeen, Domus, Stylepark, archINFORM, e-flux press kits, exhibition sites of every year's national
contribution); 5 archives and libraries with scans (Europeana, Internet Archive downloadable files, university
repositories, theses, IUAV); 9 trade press, engineers, contractors. For each page read the raw HTML through
"guard.py get --text" and take the largest variant (srcset, data-src, original file without -WxH suffix, Flickr
largest size, IIIF full/max). Download every drawing file and every PDF that holds drawings with "guard.py get <url>"
(after its check) and record its path from the OK line in "evidence". Look at what arrived (peek.py info / sheet)
and record the measured pixel size or page count and the pages that hold drawings.

Finish with notes.md's "## Rule log" complete, then return the structured summary.`

const gapPrompt = (p, gapRoute, r) => `${COMMON(p)}

You are gap route ${gapRoute}: the completeness critic and second pass for research route ${p.route}, which just
finished. Its own summary: ${r ? JSON.stringify(r) : '(the research agent returned nothing; read its files)'}
Read "${PROJ}/Research/${p.route}/" (manifest.jsonl, notes.md, leads.md, hand.md) and the route's lines in
"${PROJ}/_work/guard/requests.jsonl". Its downloads are already sorted into "../Plans/${p.folder}/" (index.csv lists
each file). Your files: "${PROJ}/Research/${gapRoute}/" (manifest.jsonl, notes.md, leads.md, hand.md,
corrections.json; create the folder). Row ids "${gapRoute.toLowerCase()}-0001", ... WebSearch budget: 4 searches.

1. Gaps. List in notes.md, before acting, what ${p.route} missed: leads it saw but did not open (links in its saved
   .txt renderings, albums, "more" pages, lazy-loaded lists, other years' exhibition sites, tender documents, theses,
   catalogue entries), larger sizes not taken, source classes not searched, languages not searched, hosts that were
   refused for ${p.route} but are no longer in refused_hosts.json (Wikimedia Commons and Wikipedia were closed by a
   User-Agent problem early on: if they are open now, search them in full), sheet types or states with no sheet
   (each level's plan, sections, elevations, the original state and every later state). Then follow each gap
   yourself to its end: download what is reachable through the guard and add rows; write what is closed to scripts
   into hand.md with the exact URL and file name; write the rest into leads.md with why it stopped.
   Never duplicate a row ${p.route} already has (same download_url): set same_item_as in corrections instead.
2. Sighting. For every downloadable row of ${p.route} and of your own route whose file is on disk (paths in
   "evidence", files under "${PROJ}/_work/guard/pages/" or "${PROJ}/Downloads/"), make contact sheets with
   "python3 tools/peek.py sheet <files...> --out ${PROJ}/_work/sighting/${gapRoute}_<n>.jpg" (at most 12 per sheet)
   and look at them; for PDFs use "peek.py pdf-text --grep" and "pdf-pages" on the listed pages. Check that each file
   shows this pavilion (not a neighbour, not the same country's show in another venue, not a building photo), that
   sheet_type, design_id, pages and format are right, and measure pixel sizes ("peek.py info").
   Write every fix into "${PROJ}/Research/${gapRoute}/corrections.json" as {"<row_id>": {"<field>": <value>, ...}}:
   wrong building -> {"design_id": "other", "count_as": "excluded", "notes": "..."}; a building photo -> count_as
   "related"; a wrong page list, sheet type, design id, format or pixel size -> the right value. Status words per
   the briefing.

Finish with notes.md's "## Rule log" complete, then return the structured summary.`

const finishPrompt = (p, after) => `Run exactly this one Bash command (it can take up to 30 minutes; use a 1800000 ms
timeout) and report its result. Do nothing else: no other command, no file edits, no web requests.

cd ${KIT} && python3 tools/finish_route.py "${PROJ}" --folder ${p.folder}

It merges all research routes, downloads every downloadable row through the guard and sorts Plans/${p.folder}/.
This run follows the ${after} of route ${p.route}. Return the exit code, the counts from the final
"Plans/${p.folder}: N files (V vectorized, R rasterized)" line, and every line of the output that reports an error,
a refusal, bad_content or a crash.`

const p = args && args.pavilion
if (!p) throw new Error('args.pavilion is missing')
const gapRoute = 'R' + (100 + parseInt(p.route.slice(1), 10))
log(`${p.folder}: ${p.name} (route ${p.route}, gap route ${gapRoute})`)

let research = args.research || null
if (!research) {
  research = await agent(researchPrompt(p), { label: `research:${p.folder}`, phase: 'Research', schema: RESEARCH_SCHEMA })
} else {
  log(`${p.folder}: research route already finished; starting at the download`)
}
const dl1 = await agent(finishPrompt(p, 'research pass'), { label: `download:${p.folder}`, phase: 'Download', schema: FINISH_SCHEMA, effort: 'low' })
const gap = await agent(gapPrompt(p, gapRoute, research), { label: `gap:${p.folder}`, phase: 'Gap and sighting', schema: GAP_SCHEMA })
const dl2 = await agent(finishPrompt(p, 'gap and sighting pass'), { label: `download2:${p.folder}`, phase: 'Download', schema: FINISH_SCHEMA, effort: 'low' })
return { pavilion: p.folder, route: p.route, gapRoute, research, download_after_research: dl1, gap, download_final: dl2 }
