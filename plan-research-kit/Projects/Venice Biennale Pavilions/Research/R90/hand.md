# R90 hand list (closed to scripts; for the user's browser)

commons.wikimedia.org and upload.wikimedia.org answered HTTP 429 to the project's scripts on 2026-10-10 (14:30 and
14:33). In a browser they work normally. Save files into `Projects/Venice Biennale Pavilions/Inbox/`.

1. Open these four file pages; if one is a drawing (map, plan, section, elevation, layout) of the Giardini or a
   Giardini pavilion, use "Original file" and save it under the name given; otherwise nothing to save.
   - https://commons.wikimedia.org/wiki/File:Map_of_Venice_Biennial.pdf -> `site_commons_Map_of_Venice_Biennial.pdf`
     (may be an organisation chart of the 2005 Biennale rather than a map).
   - https://commons.wikimedia.org/wiki/File:Venice._Sestiere_of_Castello._Public_GardenSt._Biennale_Pavilions_2007_-_Touring_Club_Italiano_GR_Venezia@0535.tif
     -> `site_commons_TCI_GR_Venezia_0535.tif`
   - https://commons.wikimedia.org/wiki/File:Caramel-architekten-biennale-venedig-3.gif -> `<slug>-reno_commons_caramel-architekten-3.gif`
     (slug of the pavilion it shows; the Austrian pavilion is likely, check the description)
   - https://commons.wikimedia.org/wiki/File:Scenografia_KinshasaVenezia.pdf -> `<slug>-reno_commons_Scenografia_KinshasaVenezia.pdf`
     only if the description places it in a Giardini pavilion.
   For each saved file, note author and licence from the file page in a line of `Inbox/R90_inbox_notes.txt`.
2. Look through the 23 pavilion categories listed in `Research/R90/leads.md` section B (one page each, 2 to 31
   files) and save any drawing, photo of a drawing or photo of a model as `<slug>_commons_<original file name>`
   (design id per `pavilions.json`; `site_` for maps of several pavilions). SVG/PDF/DjVu/TIFF files first.
