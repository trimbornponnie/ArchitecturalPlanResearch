# R90 leads: Wikimedia sweep not finished (Commons and upload.wikimedia.org refused with 429)

Status 2026-10-10 14:35: commons.wikimedia.org refused (HTTP 429 to R105 at 14:30:26) and upload.wikimedia.org
refused (HTTP 429 to R90 at 14:33:06). Both refusals are final for scripts until the user lifts them. Everything
below is for a later scripted run once the user lifts them (or for the user's browser, see hand.md). Category names
were taken from listings saved in the guard cache, never guessed.

## A. Candidate files already identified (from cached category listings; not opened, not downloaded)

| File page | Original (path from the thumbnail URL) | What is known | Design id if it is a drawing |
|---|---|---|---|
| https://commons.wikimedia.org/wiki/File:Map_of_Venice_Biennial.pdf | https://upload.wikimedia.org/wikipedia/commons/5/58/Map_of_Venice_Biennial.pdf (answered 429) | 1,752 x 1,239 px, 1.54 MB, in Category:Venice_Biennale. A WebSearch snippet calls it a self-made map of the 2005 *structure* of the Biennale, i.e. maybe an organisation chart, not a site map (unconfirmed). | `site` only if it shows the Giardini layout |
| https://commons.wikimedia.org/wiki/File:Venice._Sestiere_of_Castello._Public_GardenSt._Biennale_Pavilions_2007_-_Touring_Club_Italiano_GR_Venezia@0535.tif | https://upload.wikimedia.org/wikipedia/commons/f/fe/Venice._Sestiere_of_Castello._Public_GardenSt._Biennale_Pavilions_2007_-_Touring_Club_Italiano_GR_Venezia%400535.tif (not requested) | 956 x 1,110, 4.31 MB TIFF, in Category:Venice_Biennale_pavilions. Touring Club Italiano archive upload; map or photograph is open. R105 was opening it when Commons answered 429. | `site` if a map |
| https://commons.wikimedia.org/wiki/File:Caramel-architekten-biennale-venedig-3.gif | https://upload.wikimedia.org/wikipedia/commons/b/b8/Caramel-architekten-biennale-venedig-3.gif (not requested) | 1,000 x 666, 218 KB, in Category:Venice_Biennale; caramel architekten (Vienna). Which pavilion / drawing or photo: open. | probably `at-reno` (exhibition layout) if it is a drawing in the Austrian pavilion; confirm |
| https://commons.wikimedia.org/wiki/File:Scenografia_KinshasaVenezia.pdf | https://upload.wikimedia.org/wikipedia/commons/9/91/Scenografia_KinshasaVenezia.pdf (not requested) | 1,754 x 1,239, 593 KB, in Category:Venice_Biennale; a scenography sheet by its name; venue open. | `other` unless the venue is a Giardini pavilion |

## B. Commons categories not walked (exact URLs from the cached listing of Category:Venice_Biennale_pavilions)

In scope (Giardini pavilions), with the file counts shown in the parent listing:
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Australia) (2 F) -> `au`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Austria) (17 F) -> `at`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Belgium) (5 F) -> `be`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Brazil) (6 F) -> `br`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Canada) (14 F) -> `ca`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Czech_and_Slovak_countries) (6 F) -> `cz-sk`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Denmark) (11 F) -> `dk`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Egypt) (3 F) -> `eg`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Finland) (7 F) -> `fi`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Greece) (9 F) -> `gr`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Hungary) (30 F) -> `hu`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Israel) (12 F) -> `il`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Italy) (31 F) -> `it` (Central Pavilion) / `venezia`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Japan) (3 F) -> `jp`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Netherlands) (12 F) -> `nl`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Nordic_countries) (1 C, 22 F) -> `nordic` (its subcategory name is not known yet)
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Poland) (9 F) -> `pl`
- https://commons.wikimedia.org/wiki/Category:Romanian_pavilion_(Venice_Biennale) (3 F) -> `ro`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Serbia) (5 F) -> `rs`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(South_Korea) (11 F) -> `kr`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Sweden) (4 F) -> `nordic` (check: Nordic pavilion or a city venue)
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Uruguay) (2 F) -> `uy`
- https://commons.wikimedia.org/wiki/Category:Venice_Biennale_pavilions_(Venezuela) (3 F) -> `ve`

Read from cache, no drawings: Germany, France, Russia, United Kingdom, United States of America (see notes.md).

No subcategory in the listing for Spain (`es`), Switzerland (`ch`), Qatar (`qa`), the Venice Pavilion (`venezia`) or the
Book Pavilion (`site`): their Commons categories, if any, must be taken from the Wikipedia articles' Commons links or
Wikidata (P373) when Wikimedia is open again (it.wikipedia has https://it.wikipedia.org/wiki/Padiglione_Svizzera).

Out of scope (not Giardini; listed for completeness, not to be walked for this project): Argentina (1 C), Bangladesh,
Chile, China, Cuba, Estonia, Hong Kong, Iran, Iraq, Ireland, Luxembourg, Peru, Portugal, Thailand, United Arab Emirates.

Other Commons categories worth a look (exact URLs from the cached Category:Venice_Biennale listing):
- https://commons.wikimedia.org/wiki/Category:Mostra_Internazionale_di_Architettura_(Venice) (8 C, 1 P, 79 F): exhibition
  material of the architecture biennales; may hold layouts drawn on pavilion plans.
- BnF "Recueil" scans (Gallica press-cutting / document compilations, may contain catalogue plans of the French pavilion
  or the exhibition grounds): https://commons.wikimedia.org/wiki/Category:Recueil._Biennale_de_Venise.1938_-_btv1b10507589p (32 F),
  https://commons.wikimedia.org/wiki/Category:Recueil._Biennale_de_Venise.1947_-_btv1b10525497r (74 F),
  https://commons.wikimedia.org/wiki/Category:Recueil._Biennale_de_Venise.1948_-_btv1b10527256k (97 F),
  https://commons.wikimedia.org/wiki/Category:Recueil._Biennale_de_Venise.1948_-_btv1b105272571 (100 F).
- Numbered biennale categories with subcategories (e.g. 52nd-61st Venice Biennale, 1st Venice Biennale (1 C, 13 F)):
  URLs of the form shown in the cached listing, e.g. https://commons.wikimedia.org/wiki/Category:1st_Venice_Biennale .
- Architect categories (names not yet known, take them from each architect's Commons/Wikidata link): Carlo Scarpa,
  Alvar Aalto, Sverre Fehn, Gerrit Rietveld, Josef Hoffmann, BBPR, Bruno Giacometti, Takamasa Yoshizaka, James Stirling,
  Brenno Del Giudice, Denton Corker Marshall; look for "drawings" / "plans" subcategories with Giardini sheets.
  Read already: Alexey Shchusev and its drawings subcategory, Delano & Aldrich (no Venice drawings).

## C. Wikipedia articles not read (R90 stopped all Wikimedia requests after the second 429)

Known article URLs (from links in cached articles): https://it.wikipedia.org/wiki/Padiglione_Austria ,
https://it.wikipedia.org/wiki/Padiglione_Belgio , https://it.wikipedia.org/wiki/Padiglione_Germania ,
https://it.wikipedia.org/wiki/Padiglione_Romania , https://it.wikipedia.org/wiki/Padiglione_Svizzera ,
https://it.wikipedia.org/wiki/Padiglione_del_Brasile_(Biennale_di_Venezia) , https://it.wikipedia.org/wiki/Padiglione_della_Danimarca ,
https://it.wikipedia.org/wiki/Padiglione_della_Grecia , https://it.wikipedia.org/wiki/Padiglioni_Nazionali_(Biennale_di_Venezia) ,
https://en.wikipedia.org/wiki/National_pavilions , https://en.wikipedia.org/wiki/Greek_pavilion (WebSearch hit).
All other pavilions: en/it/de and national-language articles, titles to be taken from the pavilions' Wikidata items.
Read from cache (no drawings embedded; photographs only): en German, French, Russian, British, American pavilion,
Giardini della Biennale, Ernst Haiger; it Giardini della Biennale, Padiglione Francia, Padiglione della Gran Bretagna;
es Francia, Rusia, Reino Unido; ru Venice Biennale and Shchusev articles.
