# E115 — full-export ASR comparison (2026-10-23)

[E115 dossier](../episodes/E115.md). **The Wastes S1E115 — The Forest for The Trees**, played Arc Five session. Both complete exports were read through the final network outro. **1,848 exact ordered normalized word edits / 24,120 primary Parakeet tokens = 7.66% inter-model text disagreement**. Qwen has **308 more tokens**; neither figure measures omissions, WER or audio accuracy. **No listening, ASR rerun or original-source editing.**

## Access, revision and source inventory

Research began with **clean local `main`, HEAD `9de6cdd2d687ea5a1db481a746843ba0dfeea2a7`**. Direct filesystem access supplied the complete SRTs, ignored MP3, Git checks and documentation edits. **Workspace MCP Git status** independently reported the same repository, branch, HEAD and zero visible changes. Connected GitHub read capability was available but no remote replacement was needed for complete local evidence. No remote tip synchronization is claimed and no source revisions were silently combined.

| Exact filename / pipeline label | Cues | First start | Last end | Normalized tokens | Bytes |
| --- | ---: | --- | --- | ---: | ---: |
| [The Wastes S1E115. The Forest for The Trees.parakeet.processed.srt][p] — primary processed Parakeet | 2,691 | 00:00:03.920 | 03:04:21.680 | 24,120 | 264,128 |
| [The Wastes S1E115. The Forest for The Trees.qwen-q8.canary-ctc.nemotron.srt][q] — Qwen Q8 / Canary CTC / Nemotron | 4,386 | 00:00:09.600 | 03:04:20.660 | 24,428 | 355,516 |

Labels are **filename-derived**, not verified model builds, aligner settings, hardware, runtime or run configuration. No other same-basename raw/alternate export was located beside these sources. The original publisher episode number/title and publication date were not independently resolved; archive identity is exact and no number is extrapolated.

| Input | SHA-256 of local file bytes |
| --- | --- |
| Parakeet SRT | `f5980bda07a39a368c13b2ec1c92fed45910829af29d6fd1595e3b27e7a4939c` |
| Qwen SRT | `c67ae857aa85aa4a4d69a53a8de5237a710896052eb9a751d7be25d546f561a4` |
| Same-basename local MP3 | `2692ddad057ec7d846cd70235195509948ad5ab7411a406fcec3a56e846448fd` |

Audio copy: **`local/The Wastes S1E115. The Forest for The Trees.mp3`**, **177,542,473 bytes**, **11,068.056 seconds (03:04:28.056)** by ffprobe. This is a filename association and current fingerprint, not proof those exact MP3 bytes were the historical ASR input. The short audio tail after the final text cue was not listened to. [Machine-readable measurements](E115_ASR_COMPARISON_2026-10-23.json).

## Exact method and reading coverage

Extract all chronological cue text, excluding SRT indices/timestamps and optional `(speaker N)` tags; join. Lowercase; remove straight/curly apostrophes; replace all characters other than Unicode letters and digits with whitespace; split. Compute **unrestricted ordered unit-cost word Levenshtein**, **Parakeet → Qwen**, dividing by **24,120 Parakeet tokens**. An arbitrary-precision Myers bit-vector implementation was checked against scalar dynamic programming on **1,000 deterministic random pairs**, in both directions, including empty sequences. The full reversed-input calculation also returns **1,848**. Precise ratio **7.6616915423%**, rounded **7.66%**.

Full reading used recording-clock **ten-minute chunks from 00:00 to 03:00, then 03:00–03:05**, with common lexical text shown once and explicit P/Q alternatives. Case/punctuation folding applied only to that display; no source was rewritten. Selected passages were reread with original cue IDs and speaker decorations. The **~01:37–01:40 stream repair** is retained as out-of-game recording content, not invented story time. Both exports reach the final outro; an early extra cue or later final timestamp is not evidence of more correct speech.

## High-risk wording and continuity checks

| Recording clock | Text disagreement / interpretive risk | Evidence treatment |
| --- | --- | --- |
| ~00:00:03–00:00:10 | P begins with a separate `no` before greeting; Q first cue begins later | Opening speech boundary requires audio; not a verified omitted word |
| ~00:08–00:12 | Toesalt/Solania spellings; P `can't tell you the trajectory`, Q `can tell you` (~09:35); crew deaths and station shot | Pirate origin partly crew inference; observed ship destruction distinct from permanent captain death |
| ~00:15–00:24 | Recap calls Nash a changeling; resumed dialogue says partly shifter/human; P `plant`, Q `plan` in intimate recollection | Preserve attributed explanation and failed frog attempt; no new shapeshifting power established |
| ~00:20:24–00:20:28 | P `i must be done on`, Q `I must become a frog` (P 311; Q 484–485), labelled **speaker 3** | Another participant's paraphrase/joke, not Scott/Nash casting an incantation; he explicitly says he has no spell |
| ~00:43–00:44 | Admiral first addresses Nash/Stanley but later P/Q say history with Nash/**Vorel**, apparently conflicting with context | Keep the welcoming scene and naming slip visible; don't invent a particular prior Vorel relationship |
| ~00:47–00:49; 01:19–01:22 | Failed save/trance begins, then Stanley objects and High Elf stops; therapy assignment required but attendance voluntary | No completed memory download or compulsory attended session; no literal father/king inference |
| ~00:51–01:04 | Principle appears, claims blast and demigodhood; private “old friend” warning; **Vladimir** named in elven response | Growth, telekinesis and portal observed; ascension/blast responsibility/friend survival remain attributed claims |
| ~01:20:56–01:23:16 | P `vale or / nath`, `valeer valere ornoth`; Q `Valier Ornath`, then `Valier or Nath`; surname pun heavily garbled (P 1196–1232; Q 1863–1929) | Birth-name identity acknowledged by Stanley; **spelling remains provisional**, preferred name Stanley retained; don't certify the pun or Nash's joke alias |
| ~01:26–01:30 | **Daliot / Dalit**, father's death, corrupted-soil explanation and proposed search | Admiral's historical/cosmological testimony; no father recovered or body identified |
| ~01:34:35–01:35:30 | Both preserve ashes now missing (P 1374–1388; Q 2149–2172), contrary to earlier vial custody | Report Vorel's confession and unresolved loss mechanism; space/fire alternatives are not observed facts |
| ~01:43–01:45 | P `bachbock dad chunks`, Q `Bock Bock, dead chunks`, then explicit **father / take care of Chunks** in both | Chunks alive; caretaker role supported by subsequent behavior; no death or biological paternity inferred from garble |
| ~01:51–01:55 | Baby names first proposed as nicknames, later explicitly accepted after natural twenty / total 28 | **Fork, Boot, Pipe, Nash Junior Maggard** are agreed names at cutoff; other three sex/form assignments unknown |
| ~02:00–02:05 | P fragments `i am close oh course i am dying`; Q separates close/dying/find-me phrases; waking voice continues | Telepathic experience private to Nash; source identity unknown, no completed search |
| ~02:10–02:18 | Four-day rest agreed; fifth-day breakfast; hand loss recollection disputed and GM says **two hands** (P 1987–2006; Q 3204–3243) | Exhaustion clears; explicit continuity correction, no witnessed regrowth procedure or exact medical mechanics |
| ~02:22:50–02:23:05 | Both **no longer Fang / Fang of nothing** (P 2118–2121; Q 3435–3440) | Vorel's self-description after loss, not a new title conferred by elves or proof all subjects are dead |
| ~02:34–02:42 | Initial “about a day” estimate corrected to **a year of daily casting** for a new permanent circle; existing station circle then confirmed | No new circle built, sigils learned or teleport trip performed; extended-stay proposals aren't elapsed time |
| ~02:51–03:02 | **Nobieri/Nobiary**, **Omnom/Omnun**, **Emenil/Emanil/Emmanuelle**; book/Hand understanding incomplete | Nobieri actually visits, others' presence is his report; no confirmation Hope ordered invasion |
| ~03:02–03:04 | Level **13 → 12** correction; coming bonus **January → September** correction | Record corrected level and stated off-air timing; no literal story-year or recording-date conclusion |

Speaker IDs are local to this export/recording; contextual attribution and direct addresses take precedence over importing a previous episode's map. The new phrase/title entries retain competing recognition and performer distinctions. No majority vote resolves speech.

## Follow-through and next source

The [dossier](../episodes/E115.md), [ledger](../world/CONSISTENCY_LEDGER.md), [chronology](../world/CHRONOLOGY.md), [Arc Five](../narrative/ARC_FIVE.md), affected profiles and review queue distinguish observed events, admitted names, NPC testimony, GM continuity corrections and unperformed plans. The earlier ash-vial and missing-hand cutoffs remain historically indexed. Four days of recovery do not close the user-defined arc or establish a months/year jump.

**Next:** The Wastes **S1E116 — Large Spectral Pile Of Babies**, exact [Parakeet](../sources/The%20Wastes%20S1E116.%20Large%20Spectral%20Pile%20Of%20Babies.parakeet.processed.srt) and [Qwen](../sources/The%20Wastes%20S1E116.%20Large%20Spectral%20Pile%20Of%20Babies.qwen-q8.canary-ctc.nemotron.srt) files verified nonempty, not analyzed here. Bonus research remains separately at **BONUS-2020-09**.

## Documentation validation

**24 changed/new Markdown files pass Markdownlint with the repository configuration; 66 new/changed local link targets and anchors resolve.** Measurement JSON parses and agrees with the source counts. `git diff --check` passes. Both original SRT hashes and the matching MP3 hash remain unchanged; no original-source path appears in Git changes. New chronology/coverage rows are contiguous with E114 and retain the correct table columns. The new Elhandar profile, names, cutoff and register changes were read back.

The full **`npm run lint:markdown`** run checks **261 maintained files**, reporting **two pre-existing MD012 blank-line violations in the untouched E113 comparison report at lines 34–35**. Those same violations reproduce from initial HEAD contents; all changed directories are covered by the runner. Work is **local and uncommitted**. These checks are not audio verification; publisher numbering/date, spoken spellings, private-contact identity and custody discrepancies remain bounded review tasks.

[p]: ../sources/The%20Wastes%20S1E115.%20The%20Forest%20for%20The%20Trees.parakeet.processed.srt
[q]: ../sources/The%20Wastes%20S1E115.%20The%20Forest%20for%20The%20Trees.qwen-q8.canary-ctc.nemotron.srt
