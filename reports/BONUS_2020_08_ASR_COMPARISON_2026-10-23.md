# BONUS-2020-08 — full-export ASR comparison (2026-10-23)

[August 2020 bonus dossier](../episodes/BONUS-2020-08.md). **Out-of-game cast Q&A**, discussing Wastes material through E113 and the earlier Dunebreaker prequel; no new played events. Both complete exports were read through the farewell. **467 exact ordered normalized word edits / 5,621 primary Parakeet words = 8.31% text disagreement**. Qwen has **126 more words**, not a measured omission count or accuracy advantage. **No audio listening, ASR rerun or source edit.**

## Revision and input inventory

Initial **local `main` was clean at `f401cd889ca56f7156dc2c35b229d70b24f276a0`**. Direct filesystem access supplied both SRTs, ignored local audio, historical provenance manifest and documentation edits. The **workspace MCP Git status** independently matched repository, branch, HEAD and zero visible changes. Connected GitHub read capability was available, but no remote content was needed to replace or supplement these complete current local inputs; no revisions were silently mixed. The current remote branch tip was not independently refreshed.

| Filename / inferred pipeline | Cues | First start | Last end | Normalized tokens | Raw bytes |
| --- | ---: | --- | --- | ---: | ---: |
| [Bonus 2020-08 - August 2020.parakeet.processed.srt][p] — processed Parakeet primary | 594 | 00:00:05.360 | 00:29:36.060 | 5,621 | 58,977 |
| [Bonus 2020-08 - August 2020.qwen-q8.canary-ctc.nemotron.srt][q] — Qwen Q8 / Canary CTC / Nemotron | 902 | 00:00:05.440 | 00:29:35.800 | 5,747 | 75,537 |

Labels come from filenames; actual model builds, hardware, recognition settings, runtime and diarizer configuration are not verified. No additional current same-basename raw/alternate export was located beside these two sources.

| Input | SHA-256 of original local bytes |
| --- | --- |
| Parakeet SRT | `a3c44a0510d58c045c213bc6ea620746cf8e445795122a0900fe43db49bbbbee` |
| Qwen SRT | `2e7c86872ec0e9b6d9cb3fbd62711785987f4ea075ea464864cdf36a91ee788b` |
| Local MP3 | `a4b7a21207b358736da1e6ff8d6e831d4e95ab608f1a60c6ffd2eb9cca1fbaf8` |

**Matching audio:** `local/Bonus 2020-08 - August 2020.mp3`, **29,013,577 bytes**, **1,785.000 seconds (29:45)** by ffprobe. Its size and SHA-256 match the retained **`local/bonus-identification-2026-10-22/rename-manifest.json`** entry: original basename `011.bonus_twbd_august.mp3`, owner-sheet row **138**, feed title **`TWBD Bonus 8-11-2020`**, [archived publisher source](https://shows.acast.com/there-will-be-dungeons/episodes/6501086309d52c00124340eb). The manifest records prior correlation results **0.9689 / 0.98987**; those historical measurements were **not rerun** and are not a new listening verdict. No linked recording was downloaded again. Actual historical ASR-run input bytes remain unverified. The approximately nine-second audio tail after the final text cue was not listened to.

The **August archive label is public-publication month**. The recording itself supplies no explicit date; Scott's “today” mine-cart/Styx discussion associates it with E113's subject matter but does not prove a day. Do not parse the publisher title as a certified recording date or rename this file to a presumed earlier month. [Machine-readable measurements](BONUS_2020_08_ASR_COMPARISON_2026-10-23.json).

## Exact metric and complete reading

Extract chronological SRT cue content, removing cue numbers, timing rows and optional `(speaker N)` decorations; join text. Lowercase, delete straight/curly apostrophes, replace other non-Unicode-letter/non-digit characters with spaces, and split. Compute **unrestricted ordered word-level unit-cost Levenshtein distance** over the complete sequences. Comparison direction is **Parakeet → Qwen**, denominator **5,621**, not the Qwen count or their average.

An arbitrary-precision **Myers bit-vector recurrence** was checked against scalar dynamic programming on **1,000 deterministic random pairs**, both directions, including empty sequences. The complete reversed-direction calculation independently returns **467**. The precise ratio is **8.3081302259%**, rounded to **8.31%**. This is distinct from time-anchored alignment-candidate counts and does not establish which recognizer is correct.

The full texts were read in **00:00–00:10, 00:10–00:20 and 00:20–00:30 recording-clock chunks**, displaying shared lexical content once and explicit P/Q alternatives for differences. Case/punctuation differences were folded only in that reading display. Selected high-risk passages were also reread with original cue IDs and speaker decorations. All lexical material through the final farewell was included; no canonical reconciliation was applied.

## Concrete text differences and audio priorities

| Recording clock | Evidence / discrepancy | Documentary treatment |
| --- | --- | --- |
| ~00:00:56–00:01:03 | P `flaw just in space` / `pento vice`; Q `flagestian space` / `Pentel Vice` (P 20–21; Q 31–32) | Related to E113's phlogiston/prison lead; exact geography/name still unverified, no prison arrival |
| ~00:05:45–00:07:20 | Shared live-effects account; broken P `meet they` versus Q `immediately` in Styx recollection | Live production and “today” mine-cart reference, not proof of scripted scenes or exact recording day |
| ~00:08:45–00:09:30 | Garbled Tedna/Roger recollection, alongside explicit alternate-Pod/Tedna context | Do not convert counterpart discussion into original-character resurrection or certify Roger spelling |
| ~00:09:44–00:10:20 | Both preserve Kyle's earlier king/goblin aspiration; P `storyverrell` versus Q `story arcs? Well, Varel` at question transition | Retrospective goal, not a newly granted title or formed army |
| ~00:11:14–00:11:16 | P **`there has been a lot of that lately`**, Q **`there hasn't been a lot of that lately`** about combat (P 237–238; Q 344–345) | Meaningful polarity disagreement; retain both, do not editorially certify a combat-frequency claim |
| ~00:11:34–00:12:24 | P `carabel / on`, `quizquas`; Q `Carabalan`, `Quizquaz`; shared four-person sacrifice and unchosen beam route (P 244–260; Q 355–377) | Beau's retrospective preparation account; alternatives were not played E081 actions |
| ~00:12:30–00:13:35 | P `i have a absolutely know`, Q `I haven't absolutely know` amid Scott's hypothetical ending | The surrounding repeated **if he survives** condition is clear; ending undisclosed and not guaranteed |
| ~00:13:35–00:14:15 | P `squid`, Q `Squirt` in death-beam question | Context identifies E111 Squirts; no changed survival result or exact balancing data |
| ~00:17:53–00:19:58 | P `and we need` / Q `Stanley needs` at therapy transition; shared true-name/family recollection | Jon's backstory statement and Beau's conditional hint; no actual therapy, name reveal or recovered artifact |
| ~00:22:40–00:23:05; 26:18–27:05 | Cant words and obscure airship-etymology term diverge; linked glossary not reproduced in SRT | Quote as uncertain cast reading, not verified Planescape dictionary or Wastes location |
| ~00:24:29–00:26:18 | P `favorite terrain` / Q `favored terrain`; P `wings tied` / Q `wings tight` | Scott has no developed Underdark travel history for Hack; eagle tattoo is creator-described, not observed by PCs |
| ~00:28:50–00:29:05 | P `makes us their way items`; Q `makes us throw away items` in Baldur's Gate proposal | A joke about a possible game, not a played item disposal or scheduled stream |
| ~00:29:20–00:29:36 | Both reach next-regular-show farewell, with small cue-boundary differences | No separate late topic identified in either export; audio tail remains unchecked |

Speaker labels are **local to this recording**. Context supports Scott's hosting/Hack answers, Kristen's questions, Beau's GM answers, Jon's Stanley answers and Kyle's Vorel recollection; diarizer numbers alone do not verify identity. In these passages **Beau is labelled 2 and Jon 3**, unlike a mapping one might import from another episode. Exact split boundaries remain open to listening.

## Follow-through

The [dossier](../episodes/BONUS-2020-08.md), [review queue](../project/REVIEW_QUEUE.md), affected character/place references and thematic world/consistency notes distinguish **creator statements, unchosen routes, production practice and future possibilities**. **No Wastes event chronology or narrative chapter is advanced**. The Nash phrase register receives no invented spell; Vorel's retrospective wording is indexed without backdating a title.

Next exact bonus pair: **BONUS-2020-09 — September 2020**, [Parakeet](../sources/Bonus%202020-09%20-%20September%202020.parakeet.processed.srt) / [Qwen](../sources/Bonus%202020-09%20-%20September%202020.qwen-q8.canary-ctc.nemotron.srt), both present and nonempty, not researched here. The main-story pointer stays **Wastes S1E115**.

## Documentation validation

**11 changed/new Markdown files pass Markdownlint with the repository configuration; 35 new/changed local link targets and anchors resolve.** The comparison JSON parses and agrees with the source counts. `git diff --check` passes; original SRT/MP3 fingerprints remain unchanged. No played chronology or narrative file is modified.

The full **`npm run lint:markdown`** run checks **258 maintained files** and reports **two pre-existing MD012 blank-line violations in the untouched E113 comparison report, lines 34–35**. The same violations are reproduced from its initial HEAD contents. All directories changed here are included by that runner. Work is **local and uncommitted**; these checks do not verify audio wording or recording dates.

[p]: ../sources/Bonus%202020-08%20-%20August%202020.parakeet.processed.srt
[q]: ../sources/Bonus%202020-08%20-%20August%202020.qwen-q8.canary-ctc.nemotron.srt
