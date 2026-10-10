# R4 notes (orchestrator gap fixes)

1. Taschen preview spreads (R3 rows r3-0031..0033). R3's URLs carry the Cloudinary transform `f_webp,w_1200`
   and deliver WebP files at 1200 px under `.jpg` names, which the fetch step's magic check rejects. The same
   images with `f_jpg` and no width: guard check ALLOWED (3 URLs, one command), then guard get HTTP 200 each,
   JPEG 2500x1593 px. Rows r4-0001..0003; R3's rows become copies of them (merge corrections).

## Rule log

- 1 check command (3 URLs), 1 get loop (3 gets, all 200). No WebFetch, no WebSearch, no refusal.
