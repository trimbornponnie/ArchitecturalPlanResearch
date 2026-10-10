# Sighting schema for the image-sighter subagent

One JSON object per image, appended to `sighting-<batch>.jsonl`. The agent writes
`machine_sighted: true`; it never writes `sighted` (that word is reserved for a human who looked).

```json
{
  "file": "commons/xyz.jpg",
  "machine_sighted": true,
  "shows_building": true,
  "part": "south facade | roof | west tower | interior | detail:<what> | none",
  "zone_matches_order": true,
  "framing": "whole | facade | bay | detail",
  "obstruction": "none | trees | scaffolding | vehicles | crowd",
  "usable_for": ["material", "bay-rhythm", "opening-sizes", "roof", "none"],
  "note": "one line"
}
```

Batches of at most 12 images per agent (a batch of 24 ran into the turn limit; method review N1). The agent gets the order's target part and the building
name; it answers per image and writes the file as it goes (incident: multi-agent sighting runs
died at session limits; results kept only in memory were lost, Cologne 2026-09-21).

The reference image the agent compares with is a photograph of the confirmed building (a file
from its own Commons category, with licence in the sidecar), not a rectified street ortho:
method review N8 gave a north-front ortho as the reference, and the sighter named the
Wallarkaden in `Burohauser_..._Wallarkaden_Koln-1169.jpg` as its neighbour, while the
signed photo `...-7148.jpg` shows the same piers, pier stubs and plinth.

Per-batch summary the agent returns: counted `shows_building`, `zone_matches_order`, and the
names of files that are wrong-zone (incident: at 148 of 420 sighted, 71 sat in the wrong zone;
every per-zone count in the crawl plan was void until recounted).
