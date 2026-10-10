export const meta = {
  name: 'biennale-pavilion-plans-batch',
  description: 'Research and download the architectural plans of five Venice Biennale pavilions (research route, then gap-fill and sighting route per pavilion)',
  whenToUse: 'One batch of pavilions from Projects/Venice Biennale Pavilions/pavilions.json; args = {batch, pavilions: [entries]}',
  phases: [
    { title: 'Research', detail: 'one research route per pavilion, every request through tools/guard.py' },
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

const COMMON = (p) => `
You work in ${KIT} (cd there first in every Bash command, or use absolute paths). Python is python3.
The project is "${PROJ}". Read "${PROJ}/Research/BRIEFING.md" completely before anything else and follow it exactly:
every web request through tools/guard.py (check as its own command, get in a later command), no curl/wget/urllib/
requests, WebFetch only after "check --as claude-user" and followed by "webfetch-done", a REFUSED or 401/403/429 is
final for that host, no redirect followed without a new check, never Read an image over 1 MB (use tools/peek.py sheet
or pdf-pages first). Read "${PROJ}/_work/guard/refused_hosts.json" (if it exists) before you start on a host.
Also read reference/upstream/rekon-sources/references/plan-sources.md (source classes 0-9 and traps) and skim
reference/upstream/research-building-plans/Giudecca_critic.md (what earlier routes missed: unopened albums, lazy-
loaded lists, srcset variants, licence pages, theses and repository APIs nobody queried).

User instructions that override any narrower habit: download ANY accessible file of these drawings regardless of
its licence (personal project) and skip no lead: every lead is followed to its end or written to leads.md/hand.md
with the exact URL and why it stopped. Prefer vector files (DWG, DXF, SVG, vector PDF) and the largest raster size.

Pavilion: ${p.name}. Slug "${p.slug}" (design ids ${p.slug}, ${p.slug}-alt, ${p.slug}-reno, ${p.slug}-unk). Plans
folder Plans/${p.folder}/. Facts to confirm (leads, not readings): ${p.facts}
Other routes research other pavilions at the same time; stay on this pavilion. A drawing that shows several pavilions
(a Giardini site plan, a pavilion pair) gets a row with design_id "${p.slug}" when this pavilion is drawn in full,
and its notes name the other pavilions.`

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
"${PROJ}/_work/guard/requests.jsonl". Your files: "${PROJ}/Research/${gapRoute}/" (manifest.jsonl, notes.md,
leads.md, hand.md, corrections.json; create the folder). Row ids "${gapRoute.toLowerCase()}-0001", ...
WebSearch budget: 4 searches.

1. Gaps. List in notes.md, before acting, what ${p.route} missed: leads it saw but did not open (links in its saved
   .txt renderings, albums, "more" pages, lazy-loaded lists, other years' exhibition sites, tender documents, theses,
   catalogue entries), larger sizes not taken, source classes not searched, languages not searched, sheet types or
   states with no sheet (each level's plan, sections, elevations, the original state and every later state). Then
   follow each gap yourself to its end: download what is reachable through the guard and add rows; write what is
   closed to scripts into hand.md with the exact URL and file name; write the rest into leads.md with why it stopped.
   Never duplicate a row ${p.route} already has (same download_url): set same_item_as in corrections instead.
2. Sighting. For every downloadable row of ${p.route} and of your own route whose file is on disk (paths in
   "evidence", files under "${PROJ}/_work/guard/pages/"), make contact sheets with
   "python3 tools/peek.py sheet <files...> --out ${PROJ}/_work/sighting/${gapRoute}_<n>.jpg" (at most 12 per sheet)
   and look at them; for PDFs use "peek.py pdf-text --grep" and "pdf-pages" on the listed pages. Check that each file
   shows this pavilion (not a neighbour, not the same country's show in another venue, not a building photo), that
   sheet_type, design_id, pages and format are right, and measure pixel sizes ("peek.py info").
   Write every fix into "${PROJ}/Research/${gapRoute}/corrections.json" as {"<row_id>": {"<field>": <value>, ...}}:
   wrong building -> {"design_id": "other", "count_as": "excluded", "notes": "..."}; a building photo -> count_as
   "related"; a wrong page list, sheet type, format or pixel size -> the right value. Status words per the briefing.

Finish with notes.md's "## Rule log" complete, then return the structured summary.`

const batch = args && args.pavilions ? args.pavilions : []
if (!batch.length) throw new Error('args.pavilions is empty')
log(`Batch ${args.batch}: ${batch.map(p => p.folder).join(', ')}`)

const results = await pipeline(
  batch,
  (p) => agent(researchPrompt(p), { label: `research:${p.folder}`, phase: 'Research', schema: RESEARCH_SCHEMA }),
  (r, p) => {
    const gapRoute = 'R' + (100 + parseInt(p.route.slice(1), 10))
    return agent(gapPrompt(p, gapRoute, r), { label: `gap:${p.folder}`, phase: 'Gap and sighting', schema: GAP_SCHEMA })
      .then(g => ({ pavilion: p.folder, route: p.route, gapRoute, research: r, gap: g }))
  },
)
return results.map((x, i) => x || { pavilion: batch[i].folder, route: batch[i].route, failed: true })
