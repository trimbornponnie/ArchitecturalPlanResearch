# Audit of the research run, 2026-10-03 (Giudecca Housing, Gino Valle)

Scope: routes R1-R9 (and the critic's transcript), checked against the BRIEFING.md "Rules" section. Sources: the ten
agent transcripts of workflow wf_7eb31692-c1e, `_work/guard/requests.jsonl` (1829 lines), `_work/guard/refused_hosts.json`
(58 hosts), `Research/critic.md` section 2, each route's `notes.md` "## Rule log", and the project `manifest.jsonl`
(195 rows). This audit sent no web request. Times are local (CEST); transcript times were converted from UTC.

Short result: two requests are missing from the guard log (R5, R8), and one borderline request reached the alias of a
refused host (R5). No request outside the guard and no unauthorised copy was found. Every WebFetch has its check and
its log line. The biggest problem nobody reported: R1 sent its Flickr WebFetches in parallel bursts of up to six.

## Breaches

A request that should not have been sent, an unlogged request, or an unauthorised copy.

| # | Route | Time | What happened | Evidence | Reported by |
|---|---|---|---|---|---|
| B1 | R5 | 18:29:19-21 | **Unlogged request.** `guard.py get` of `https://api.openalex.org/works?search=%22Gino%20Valle%22&filter=is_oa:true&per-page=100` sent the request and saved `_work/R5/openalex_839c11.json` (1,294,099 bytes, 18:29:21). Then it crashed in `out.relative_to()` before writing its log line. | Bash 18:29:19: `for u in ...; do PY _tools/guard.py ... -r R5 get "$u" --out "Projects/.../_work/R5/openalex_$(...).json" \|\| break; done`. The output is a Traceback. The log has the check at 18:29:14 (pid 88716) and no get line for this URL. | R5 slip 1; critic #6. Cause: a tool bug, since fixed (`out = Path(out).resolve()`). |
| B2 | R8 | 19:18:09 | **Request missing from the log under its own URL.** The WebFetch of `https://www.flickr.com/photos/unfoldingpavilion/archives/date-posted/2018/02/` followed a same-host 302 by itself to `https://www.flickr.com/signin/?acf=...`. That address then redirected off-host to `identity.flickr.com/login` (not followed). So one request reached the Flickr sign-in page. No credentials were sent and nothing was downloaded. | The WebFetch result says "REDIRECT DETECTED ... Original URL: https://www.flickr.com/signin/?acf=... Redirect URL: https://identity.flickr.com/login?redir=..." (the reported "original" is the sign-in address, so that hop was fetched). The log line (`webfetch`, 19:18:16) reads `302 redirect to www.flickr.com/signin (login required; not followed)`. Only the second, off-host hop went unfollowed. | Partly: R8 logged the 302 but described it as not followed. The critic ran before R8. The cause is WebFetch's built-in same-host redirect handling, which the agent cannot switch off. |
| B3 | R5 | 18:30:11 | **Borderline: a request to the alias of a refused host.** iris.polito.it was refused for every route at 18:17:11 (robots.txt 403, by R7). R5 knew that "PORTO@Iris" is PoliTo's repository (notes items 18 and 34). It still checked `http://porto.polito.it/2279799/1/Valle_AV82_PAC.pdf`, the retired predecessor host of the same repository. The guard fetched `http://porto.polito.it/robots.txt` (HTTP 301 to /old/index.html) and refused the URL. Nothing beyond robots.txt was fetched. | Log lines 934-935 (18:30:11, pid 95832). R5 notes item 37: "repository retired, now iris.polito.it which is refused". | Not reported as a slip by R5; not in critic.md. Judged a near-breach of "no mirror of the same host". |

Count of unlogged requests: **2**. B1 has no log line at all. B2 is logged only inside its WebFetch's result text. A
WebFetch that silently follows a same-host redirect and then succeeds leaves no trace in the transcript, so this
count can only be a lower bound (see Method).

Nothing else falls into this class:
- **Requests outside the guard:** none. No Bash or PowerShell command, written script or edited file in any route
  contains curl, wget, Invoke-WebRequest, Invoke-RestMethod, `urllib` (other than `urllib.parse`), `requests.`,
  http.client, httpx, aiohttp, Start-BitsTransfer, urlopen or a browser. No route used PowerShell. The scripts the
  routes ran (add_rows.py, tb.py, fix_evidence.py, r2_addrows.py, r5_add.py, r7_rows.py, make_pub_rows.py and others)
  are local. peek.py has no network code.
- **Requests to a host after it entered refused_hosts.json:** none. All 62 `refuse_host` events were replayed against
  every later get, robots and webfetch line. The only later requests are re-tests after the 30-minute soft expiry:
  miesarch.com and www.miesarch.com at 18:41:06/08 (R3), old.atervenezia.it at 18:51:37 (R4) and blogs.cornell.edu at
  18:55:07 (R6). No WebFetch went to a refused host.
- **Unauthorised copies:** none. No get or WebFetch fetched an Internet Archive upload, Scribd, Pinterest, Google
  Books, academia.edu, a file-sharing copy or a usmodernist PDF. Pinterest (R6 18:17:53), Google Drive (R2 18:20:16,
  the exhibition's own press kit), academia.edu (R7 18:31:56) and Dropbox (R5 18:39:34) got as far as robots.txt and
  were refused at check. R9 read only usmodernist's HTML pages (index-pa, home, library, terms, about). Its row r9-0004
  points to `PA-1988-02.pdf` with downloadable=false, and that PDF was neither checked nor fetched. No get reached a
  page behind a login or a paywall. R9's `researchprofiles.ku.dk` PDF answered 403, and the UPM files marked
  "administrator only" were not requested.

## Form issues

A rule's form was broken. No request was sent that should not have been, unless a row says otherwise.

| # | Route | Time | Issue | Reported by |
|---|---|---|---|---|
| F1 | R1 | 18:22:19 (x6), 18:37:07 (x2), 18:40:51 (x6), 18:41:15 (x5), 18:43:43 (x2), 18:45:46 (x5) | **Parallel WebFetch bursts to www.flickr.com.** 26 of R1's 36 WebFetches were issued as parallel tool calls in 6 assistant turns, up to 6 at once. Each burst followed one multi-URL `check --as claude-user` (commands 18:21:56, 18:36:43, 18:39:55 used for two bursts, 18:43:29, 18:45:16). The guard takes the host's turn only for 3 s per check, so this defeats the one-request-per-host spacing. **Rate effect:** concurrent requests to one host. Every request was allowed and logged. | **Not reported** by R1 or the critic (the log cannot show it). |
| F2 | R8 | 19:40:05 (x2) | The same problem once: two parallel WebFetches (photo pages 38528961280 and 39441049305) after one 22-URL check at 19:38:33. | R8 slip 1. |
| F3 | R1, R2, R8 | see note | WebFetch checks were batched: one `check --as claude-user` command per group of URLs instead of one before each WebFetch. R1 ran 6 commands for 29 URLs, R2 4 commands for 13 URLs, R8 1 command for 22 URLs. R2's Rule log says "each preceded by its own check --as claude-user command", which is inaccurate. | R8 slip 4. R1 and R2 did not report it. |
| F4 | all routes | many | A check shared its Bash command with local commands (a notes/leads append, a grep of refused_hosts.json, a local python). It never shared a command with a get. Counts: R1 5 (two of them chained after `webfetch-done ...;` at 18:47:43 and 18:48:22), R2 4, R3 9, R4 10, R5 14, R6 6, R7 4, R8 1, R9 8. | R5, R8 and R9 reported it. R1, R2, R3, R4, R6 and R7 did not. Critic #12 covered R5 only. |
| F5 | R3 | 18:17:38 | A get followed a `\|\| break` loop after `;` in the same command (7 Atlante images, then `.../en/wp-json/wp/v2/posts/1642`). That get drew **HTTP 401 at 18:17:49**, which closed atlantearchitetturacontemporanea.cultura.gov.it for every route. The URL had its own ALLOWED check (18:17:07), and all 7 loop gets returned 200, so the compliant form would have sent the same request. The form break itself had no request effect; the 401 is the cost of an unneeded API call. | R3 slips 1a and 3; critic #7 and #11. |
| F6 | R3 | 18:18:52 | Two get loops in one command (5 Censimento images, then /progetto and /metodologia). No effect: all returned 200. | R3 slip 1b; critic #8. |
| F7 | R1 | 18:24:23; 18:23:02-18:24:19 | A get was attempted without a matching check (the guard refused it and sent nothing). URLs read from a CRLF file left a trailing CR in 78 check and 49 get log entries. | R1 irregularity 1; critic #1 and #2. |
| F8 | R6, R3 | 18:17:29; 18:41:08 | A sibling hostname was tried inside the block of its twin, and no HTTP request reached a server. R6 tried www.zaquadrato.com 5 s after zaquadrato.com failed DNS. R3 checked miesarch.com 2 s after www.miesarch.com failed in the same re-test command (pid 48472); the connection was refused. | R6 slip 1 (critic #10). R3 listed both refusals but not the sibling point. |
| F9 | R3, R2 | 18:26:12; 18:20:16 | A second route was tried to a resource refused by robots.txt. R3 checked the api.europeana.eu search API (public demo key) after www.europeana.eu/it/search was disallowed; one robots.txt request reached api.europeana.eu (302) and the URL was refused. R2 checked Google Drive `/uc?export=download` after `/open` was disallowed; robots.txt was cached, so no request was sent. | R3 slip 2 (critic #9). R2 listed both refusals. |
| F10 | R3, R4, R5, R7 | e.g. R7 18:23:21-18:28:03, R4 18:18:32-18:53:19, R3 18:25:33-18:29:22, R5 18:25:36-18:40:36 | Catalogue and site searches were sent as GET query URLs (OPAC SBN, Polo SBN, Polimi OPAC; ATER wp-json and Golem `?q=`; catalogo.beniculturali.it, Censimento ricerca-opere; OpenAlex, Crossref, DOAJ, fupress, TU Delft, ETH). This is borderline under rule 3 ("never submit a form"). I judge it not a form submission: robots allowed, no POST, no credentials. | R7 and R4 reported it; R3 and R5 did not. Critic #13 covered R7 only. |
| F11 | R8 | 19:29:00, 19:30:25 | WebFetch was used to fetch two image files (`casabellaweb.eu/wp-content/uploads/2010/07/478-cp.jpg` and `528-cp.jpg`) instead of pages. The research UA is refused there through the ClaudeBot group, and Claude-User is allowed through `*`. The binaries remain in the session tool-results folder (`webfetch-1791048541085-d5z10h.jpg`, `webfetch-1791048626524-thchi2.jpg`), outside the project and in no row. These are the publisher's own cover images, so this is not an unauthorised copy. | R8 slip 5. |
| F12 | R1, R8 | R1 18:23-18:44; R8 19:22-19:37 | Flickr `_h` (1600 px) files were taken where the sizes pages offer this free account's photos for download only up to 1024 px. R1 took 70 files: 67 now moved into `Downloads/live.staticflickr.com/`, and 3 rowed files still in pages/. R8 took building and exhibition photos (no rows), several at `_h`. This is the briefing's size clause, a decision for the download step. The rights basis (archive drawings lent to the exhibition) is unaffected. | R1 irregularity 2; R8 slip 6; critic #5. |
| F13 | R7 | ~18:38 | 28 manifest rows were written in one batch (rule 6). | R7; critic #14. |
| F14 | R1, R2, R4, R5 | - | Rule-log gaps: R1's two unused claude-user checks and its parallel bursts (F1) are missing. R2's claim of one check per WebFetch is wrong (F3). R4 says "Slips: none known" despite F4. R5 omits B3. | - |

Observations, no rule broken:
- After R4 drew a bot challenge on www.comune.venezia.it (18:22:29), R4 and R7 used other Comune hosts:
  portale.comune.venezia.it (robots refused), consiglio2020.comune.venezia.it (PDF, 200), and live. and
  dime.comune.venezia.it, both of which then drew challenges (R7 18:31:06/12). These are separate services, not
  mirrors, but the same organisation's firewall was triggered three times.
- 20 URLs were fetched by two routes each (8 pairs R2/R5, 3 R3/R7, 9 other pairs). That wastes 20 requests; no rule
  is broken.
- The `setup` route (the orchestrator, not a research route) expired the www.miesarch.com refusal by hand after 95 s
  (18:10:23) and ran a guard self-test whose get was refused without a request (critic #15).
- guard.py was patched during the run (file time 19:47:01): `check` now strips the URL, and `get` resolves `--out`
  before the request. Log lines before the patch keep the trailing CR (F7).

## Critic items settled

- **Critic #3 (R1, www.flickr.com/photos/unfoldingpavilion/ and .../page9): no WebFetch was sent.**
  - The 18:36:43 command checked three URLs as claude-user: `39627198664/sizes/k/`, `/albums` and the photostream
    root (ALLOWED 18:36:48). Only the first two were WebFetched (18:37:07 and 18:37:08, `webfetch-done` for both at
    18:37:44).
  - The 18:47:43 command checked `/page8` and `/page9` (ALLOWED 18:47:44). Only `/page8` was WebFetched (18:47:58);
    the next WebFetch was `/page7` (18:48:32) after its own check.
  - None of R1's 36 WebFetch calls has the URL `.../unfoldingpavilion/` or `.../page9`.
- **Critic #4 (R2, unfoldingpavilion2018.tumblr.com/archive): no WebFetch was sent.** The 18:21:25 command checked
  /page/3, /page/4, /archive and /events (ALLOWED 18:21:30 for /archive). The following WebFetches were /page/3
  (18:21:41) and /page/4 (18:22:21). /archive appears in none of R2's 19 WebFetch calls. R2's earlier checks of
  /events and /page/2 (18:19:23, 18:19:27) went unused at the time; each was WebFetched later after a fresh check.
- **WebFetch pairing, extended to R8 (which ran after the critic):** every one of the 108 WebFetch calls (R1 36,
  R2 19, R6 1, R7 2, R8 50) has an earlier `check --as claude-user` of the exact URL by the same route that printed
  ALLOWED, and a later `webfetch-done` line for the same URL. Transcript and log counts match per route. R3, R4, R5
  and R9 sent no WebFetch, and their logs show none. R8's 50th result is the 302 of B2; the other 107 are `ok`, and
  no WebFetch showed an error that was logged as `ok`.
- **Critic #6** is confirmed from the transcript: Traceback at 18:29:19-21, and the file was saved (B1).
- **Critic #1, #2, #7, #8, #9, #10, #12** are confirmed command by command. #12 is broader than the critic found
  (F4), and #13 is broader too (F10).
- **Critic "Own checks"** is confirmed and extended to R8 and R9: all 508 gets that were sent had an earlier ALLOWED
  check of the exact URL by the same route, in another process, within 60 minutes. The one apparent exception (R7
  `architettivalle.net/contatti/`, get 18:22:11) had R7's own check at 18:22:06; R3 checked the same URL at
  18:22:09.
- **Critic "Community uploads"** is confirmed and extended to R8 and R9: none downloaded. R8 left the Flickr album's
  136 publication-page scans as leads.
- **Not seen by the critic:** B2, B3, F1 and the full F4/F10 scope.

## Unused fetched files

`_work/guard/pages/` holds 531 files. 174 are `.txt` renderings of fetched HTML pages, and 10 are files a manifest row
points to: they stayed in pages/ because the download step skipped those rows (same_item_as or `related`). The other
**347 files (342.9 MB, 85 hosts)** are pointed to by no `download_url` in `manifest.jsonl`. Every one has its guard
get line in requests.jsonl, and no file lacks one. Nothing was deleted. Files the download step adopted were moved to
`Downloads/` and are not counted here.

| Host | Files | MB | Route(s) | What they are (from the routes' notes) |
|---|---|---|---|---|
| 64.media.tumblr.com | 52 | 9.5 | R2 | Unfolding Pavilion 2018 tumblr images (640 px): installation views and participants' works (ENTER Studio room, Trabucco textile, ANALOGIQUE "M.I.Mo." diagrams, WAR, Bunker, Studiospazio, La Cameretta, THE MAIL), Little Italy post photos; artworks or exhibition photos, no rows |
| live.staticflickr.com | 31 | 8.1 | R8 | 24 "Gino Valle Archive" building photos (album 72157665838816838), 6 exhibition photos (albums 72157691864069790, 72157694683764912), 1 third-party building photo (acaland, 14438636474); fetched "to classify", no rows |
| docomomo.com | 6 | 185.5 | R5, R9 | proceedings page; PDFs of 16th IDC vol. 2, 17th IDC ebook, 12th IDC, 14th IDC, "Modern Futures" 2025 (108 MB); searched, no Giudecca drawings |
| opac.biblio.polimi.it | 4 | 39.7 | R7 | two OPAC search pages; two Casabella index PDFs 1982-1988 (authors/articles/projects; subjects/places/books) used to locate the 1982/1986 articles |
| ater-venezia.golemnet.it | 22 | 5.7 | R4 | ATER "Societa Trasparente" pages and search results; Patrimonio immobiliare .ods; Piano di vendita 2019 PDF; Programma triennale lavori PDFs 2022-24 and 2026-28 (later works) |
| repository.regione.veneto.it | 1 | 15.3 | R4 | PDF found by a search snippet that turned out to be another plan (Riese Pio X), a wasted request R4 reported |
| onlinepa.info | 4 | 12.7 | R4 | ATER transparency portal (to 2025), module pages |
| repozytorium.biblos.pk.edu.pl | 2 | 10.3 | R5 | two Polish papers on Venice and water; Giudecca mentioned only generally, no Valle |
| scindeks-clanci.ceon.rs | 1 | 8.9 | R5 | SAJ 15/3 (2023) Maranelli article PDF; text mentions Valle's complex, no drawings rowed |
| oa.upm.es | 2 | 7.9 | R9 | record 85313 and the open "Liminal spaces" excerpt of Housing Atlas Europe (TOC gives the Giudecca at pp. 323-327; no spread) |
| api.openalex.org | 7 | 4.7 | R5 | OpenAlex query results (JSON), discovery |
| www.wearch.eu | 8 | 3.3 | R2 | two articles; 6 images of the 2024 Udine exhibition (Talmone/Fantoni, "Courtesy Casa Cavazzini"), none with Giudecca material |
| polovea.sebina.it | 9 | 3.1 | R7 | Polo SBN Venezia catalogue search, record and library pages (holdings of Lotus and Casabella) |
| atlantearchitetturacontemporanea.cultura.gov.it | 10 | 2.4 | R3, setup | Atlante page (IT, EN), credits page, images E22-01..07 (building photos by Marco Introini), noted as a photo source |
| atervenezia.it | 13 | 1.8 | R4, R7 | ATER site pages, announcements 2024-26, wp-json search results, POR "17 alloggi" PDF; call-centre contact page (R7) |
| architecturetoday.co.uk | 1 | 1.6 | R9 | Housing Atlas review page |
| www.redalyc.org | 1 | 1.6 | R6 | journal article PDF checked for drawings |
| www.arc.usi.ch | 5 | 1.4 | R2, R3 | exhibition notices, Mendrisio Academy Press pages, book-presentation invitation PDF |
| censimentoarchitetturecontemporanee.cultura.gov.it | 11 | 1.3 | R3 | scheda 1404, search, progetto/metodologia/indice pages; images 8056, 8058, 8059, 8060 (photos scanned from publications; 8057 is rowed as r3-0001) |
| ocio-venezia.it | 5 | 1.3 | R4 | OCIO reports on ex Scalera/Trevisan, C.U.R.A. Giudecca dossier PDF 2019, two report images |
| www.ilpais.it | 14 | 1.2 | R2 | two articles; 12 exhibition photos by E. Foramiti (Udine 2024); the 13th is rowed as r2-0009 |
| bia.unibz.it | 5 | 1.2 | R5, R9 | Esploro chapter page (JavaScript shell), sitemap index and sitemap, two OAI records (dc:rights Restricted) |
| www.architettivalle.net | 9 | 1.1 | R2, R3, R4 | Valle Architetti Associati site pages, sitemaps, wp-json search, contacts |
| divisare.com | 10 | 1.1 | R2, R4, R6 | project and author pages (338437 ZA2, 386846, 388095, 390381, 390725, 391131); images on images.divisare.com refused |
| en.silvanaeditoriale.it | 7 | 0.9 | R2 (R5 fetched the same URLs) | catalogue page and 6 publisher preview images of "Gino Valle. La professione come sperimentazione continua" (2024) |
| www.archdaily.com | 1 | 0.8 | R2 | Unfolding Pavilion article (images on images.adsttc.com refused) |
| www.boanoprismontas.com | 1 | 0.8 | R2 | "165x165" project page |
| assets.archisearch.gr | 3 | 0.7 | R2 | Boano Prismontas "165x165" images (two Unfolding Pavilion views, Aerial View); the PLAN image is rowed as r2-0010 |
| opac.sbn.it | 3 | 0.6 | R7 | OPAC home, search and record pages (VEA0011220) |
| www.maxxi.art | 4 | 0.6 | R7 | MAXXI home, archive centre, architecture collections, exhibition page |
| www.conoscerevenezia.it | 2 | 0.5 | R4, R6 | entries ?p=42611 and ?p=4969 (addresses of the IACP housing) |
| ilgiornaledellarchitettura.com | 2 | 0.5 | R2, R3 | 2011 and 2024 reviews |
| insula.it, sezione-storica.insula.it | 2 + 4 | 0.3 | R4 | home, wp-json and site searches; "Calle dei Lavraneri" press release; "10 alloggi alla Giudecca" |
| farworkshop.wordpress.com | 2 | 0.3 | R5 | WAVE 2011 workshop page (Croset; another site) and a WAVE 2012 .doc analysis sheet |
| siusa-archivi.cultura.gov.it | 6 | 0.1 | R3, R7 | SIUSA producer (Valle Gino 52898; 52895), complex and holder pages |
| www.usmodernist.org | 5 | 0.3 | R9 | P/A index, home, library, terms, about pages (rights check; no PDF fetched) |
| www.messaggeroveneto.it | 1 | 0.3 | R2 (R3 fetched the same URL) | Pietro Valle interview on the 2023-24 exhibition |
| hiddenarchitecture.net | 3 | 0.2 | R6 | post /giudecca/, about page, wp-json media listing; the blog's images were not fetched |
| atervenezia.tuttogare.it | 2 | 0.1 | R4 | tender detail (gara 414, lift maintenance) and tender list |
| catalogo.beniculturali.it | 5 | 0.1 | R3 | catalogue search result pages |
| atlas.landscapefor.eu | 9 | 0.1 | R9 | landscape atlas POI pages, "Area ex Trevisan, nuove abitazioni popolari" |
| www.iuav.it | 4 | 0.3 | R3 | Archivio Progetti pages, Petit tour 22 (no Gino Valle fonds) |
| images.squarespace-cdn.com | 2 | 0.1 | R9 | 300 px renditions of E. Pigionatti's building photos |
| 41 further hosts, 1-3 files each | 46 | 4.9 | various | text pages read for facts or contacts: api.crossref.org, doaj.org, oajournals.fupress.net, repository.tudelft.nl (JS shell), disegnarecon.unibo.it, journals.openedition.org (CRAU 297 HTML, CRAUP 15594), www.engramma.it, www.acsa-arch.org (ACSA 1995 paper PDF, no Valle drawings), cataloghidedicati.iuav.it (incl. a 3.8 kB index PDF), iuav.unifind.cineca.it, collezionearchitettura.maxxi.art, www.csacparma.it, www.treccani.it, it.wikipedia.org, commons.wikimedia.org, fondoambiente.it, jemolo.com, naransa.it, www.laterizio.it, consiglio2020.comune.venezia.it (council question PDF), dati.venezia.it, idt2.regione.veneto.it (downloader page), www.anteferma.it, friulisera.it, ildiscorso.it, www.finestresullarte.info, urbancuratortat.org, qui.uniud.it, www.civicimuseiudine.it, www.baunetz.de, www.archisearch.gr, www.area-arch.it, www.atelierxyz.info (domain now unrelated), laurianghinitoiu.com, www.coam.org, www.lundhumphries.com, research.tudelft.nl, researchprofiles.ku.dk, search.usi.ch, www.osti.gov, www.emanuelepigionatti.com |

Two fetched files lie outside pages/ and in no row: `_work/R5/openalex_839c11.json` (the unlogged request, B1) and
the two Casabella cover JPEGs in the session tool-results folder (F11). The per-file list (host, route, time, type,
bytes, URL) is in the session scratchpad:
`C:/Users/trimb/AppData/Local/Temp/claude/c--Users-trimb-Desktop-Rekonstruktion/5f583334-15ae-480b-85c0-35b96a996eb7/scratchpad/audit/unused_list.txt`.

## Method

- **Transcripts.** Every `tool_use` and its `tool_result` in the ten `agent-*.jsonl` files (route from `.meta.json`)
  was extracted with a Python script run in the project venv. Timestamps were converted UTC to CEST, and parallel
  tool calls were identified by the shared assistant request id. No transcript was read whole.
- **Check 1.** Each WebFetch was paired with the latest earlier `check` log line (identity `claude-user`, same route,
  same URL) and the first later unused `webfetch` log line. Then the reverse: claude-user checks with no WebFetch,
  and webfetch lines with no WebFetch.
- **Check 2.** Bash, PowerShell, Write and Edit inputs were matched against a pattern for HTTP clients and browsers;
  every hit was read in context (all were `urllib.parse` or text). URLs in non-guard commands were listed and read.
- **Check 3.** Guard sub-commands were parsed per command. Loop spans were located from do/done pairs; the audit
  flagged get outside a loop after it, several loops, a missing `|| break`, a pipe masking the exit status, and check
  together with get. A second pass listed everything that shared a command with a check, counting only commands
  whose output shows a check result.
- **Check 4.** `refuse_host` and `expire_refusal` events were replayed in log order against every later
  get/robots/webfetch with a real request (`http` other than -1). Sibling and alias hosts (same registrable domain)
  after each refusal were listed and judged by hand.
- **Check 5.** All 508 sent gets were grouped by host and the rights-sensitive hosts reviewed (tumblr, Flickr,
  usmodernist, blogs, publishers, repositories). R8's Flickr downloads were matched to photo titles from
  `R8/album_photos_list.tsv` and R1's to `R1/album_list.tsv`. Manifest rows with `downloadable: true` were grouped
  by host.
- **Check 7.** File paths under pages/ were mapped to URLs through the log's `out` field and compared with the
  stripped `download_url` set of `manifest.jsonl`.
- **Limits.**
  - WebFetch reports only off-host redirects. A same-host redirect that ends in a successful fetch leaves no trace,
    so further unlogged hops (like B2) cannot be ruled out.
  - Requests made by the orchestrating session outside the routes (the `setup` and `fetch` log routes) were not
    audited beyond the log.
  - Rules 4-7 were not audited beyond the WebSearch budget (all routes within 15: R1 2, R2 11, R3 12, R4 15, R5 15,
    R6 15, R7 15, R8 0, R9 13) and a check that no Read opened a PNG.
