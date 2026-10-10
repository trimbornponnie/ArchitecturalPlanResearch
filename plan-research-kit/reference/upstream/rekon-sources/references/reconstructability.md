# Reconstructability verdict

Decided 2026-09-17 for the predecessor project, binding here. The focus of every building
research is the ability to reconstruct the building from drawings, not its provenance chain.

A sheet set is judged on whether the publicly available (or supplied) sheets together give:

| No. | Sheet | Weight |
|---|---|---|
| 1 | Plan of every storey, dimensioned or gridded | necessary |
| 2 | Section in both directions | necessary |
| 3 | Elevation of every side | necessary |
| 4 | Framing / ceiling / roof structure per level, or the structure legible in sections and plans (a concrete frame of flat slabs and piers has no framing sheet and never will; Wallarkaden 1.6) | necessary |
| 5 | Eaves section for wall build-up and overhang | detail depth |
| 6 | Details of joints, windows, doors, hardware | detail depth |
| 7 | Dimension tables per piece with grid mark, type, section | component catalogue |

Deformation diagrams, damage maps, cost tables and schedules do not count and are listed apart.

Present is not measurable. Every sheet gets two numbers in the verdict, because text and
geometry scale differently:

- **px per sheet mm** decides the text. Lettering is about 2.5 mm on the sheet whatever the
  scale, so it needs about 3.2 px per sheet mm (8 px letters) to be read and 2 px per sheet mm
  (5 px) to be strained. A 1:100 A0 sheet at 4800 px gives 4.0 px per sheet mm. The number needs
  the sheet size; where that is `assumed` (no title block, no catalogue) the glyph probe measures
  the small-text height on the image instead.
- **px/m on the building** decides the geometry: bays and openings need about 10 px/m. The same
  4800 px A0 sheet gives 40 px/m at 1:100.

A 1:1 detail can show 877 px/m on the building and still not one legible word: Centre Pompidou
frp_24 is 763 px across an 870 mm sheet, 0.88 px per sheet mm (X2; the old single px/m number
called it "text readable"). The Centre Pompidou set had all four necessary types, its plans and
elevations at 2 to 17 px/m (the RSHP east elevation 17, the FRP sheets 2 to 13), and no sheet with
legible dimension text; the trustworthy geometry there was written text (the Arup module) and
the levels in the drawing numbers (dry run 1.6). A set that is present but not measurable is
`hybrid` at best.

Sheet count alone says nothing: twenty deformation graphs are insufficient, six sheets with a
plan, two sections, four elevations and a framing plan are modellable.

## Route decision

| Sheets 1-4 present | Route | What stage 3 does |
|---|---|---|
| all four, and the gap table's envelope, slab, core and stair classes `covered` (text legible or vector) | `plans` | reads sheets; facades only to confirm materials |
| some | `hybrid` | reads what exists; facades fill the rest, marked `derived` |
| none usable | `street` | massing from footprint and height; facades from panoramas; all `derived`/`assumed` |
| user-supplied | `manual` | as `plans` or `hybrid` depending on what was supplied; no web search |

Write the filled table (with a Measurable column), the route with one sentence of reasoning,
the part-class gap table with the request that would fill each gap, and a section "Other sources
checked, nothing usable" that separates "checked, empty" from "checked, not readable" (refused,
403, login) into `02-sources/plans/verdict.md`. `rekon verdict` pre-fills all three from the
sidecars, `requests.json` and `search-log.jsonl`. Vector before raster is a preference for
choosing between sources, not a gate for the route.

## Part classes: the stop rule

The seven sheet types say what kind of drawing exists; the fourteen part classes of `break.md`
say what the model must hold. `gaps.json` gives per class the candidate sheets (by sheet type and
by title words in English, German and French, or by a reader's `shows` list), the best reading
among them and its status: `covered` (legible text or vector), `weak` (candidates, none legible),
`unknown` (legibility not measurable), `gap` (no candidate). A class that is `weak` or `gap`
without a logged search or a drafted request is a finding at `done 1`; a class with candidates
beside plan basis `none` in `break.md` is a finding at `done 4` (warn-only for now). Incident:
the Wallarkaden verdict called the basements "not needed" beside the two sections that drew
them (2026-09-23).
