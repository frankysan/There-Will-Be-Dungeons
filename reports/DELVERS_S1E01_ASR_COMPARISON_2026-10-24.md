# Delvers S1E01 — complete-export ASR comparison, 2026-10-24

**Source-identity follow-up, 2026-10-27:** The [S1E02–S1E01 batch check](DELVERS_S1E02_S1E01_SOURCE_IDENTITY_2026-10-27.md#s1e01) verifies both complete local exports against their historical Git blobs after CRLF-to-LF conversion only, and verifies both source paths in the recorded source commit. Raw bytes differ in line endings. The original local-input raw SHA-256 records also match exactly; the Git blob IDs in this follow-up come from the recorded local commit tree, not a remote source fetch. Earlier provenance statements remain dated history. Prior interpretive coverage, inter-ASR measurements, played cutoff and audio status are unchanged.

**Episode:** Delvers season 1, corrected archive **S1E01 — How Much Is Potato**; publisher **TWBD Delvers S1E1: How Much Is Potato**. Played premiere with production/rules/outro sections. **Text-only research, ASR-provisional; no audio listened to and no new ASR run.** [Dossier](../delvers/episodes/S1E01.md) · [Review queue](../delvers/REVIEW_QUEUE.md).

## Inputs and access identity

Direct filesystem supplied both full SRTs and the matching local MP3. Local Git and workspace MCP independently reported clean `main`, HEAD **`9c74201783dbc53f21f724fcd3ef2ced8de144ba`**, before edits. The GitHub connector supplied `delvers/README.md` at that explicit commit; remote reads were used to check revision access, not as substitutes for ignored audio. No identical source bytes were unnecessarily refetched through other routes.

| Export | Exact source path | Cues | First start | Last end | Normalized tokens |
| --- | --- | --- | --- | --- | --- |
| Primary P | [Delvers S1E01. How Much Is Potato.parakeet.processed.srt](../sources/Delvers%20S1E01.%20How%20Much%20Is%20Potato.parakeet.processed.srt) | 2,334 | 00:00:09.120 | 02:30:31.230 | 21,024 |
| Independent Q | [Delvers S1E01. How Much Is Potato.qwen-q8.canary-ctc.nemotron.srt](../sources/Delvers%20S1E01.%20How%20Much%20Is%20Potato.qwen-q8.canary-ctc.nemotron.srt) | 3,925 | 00:00:09.120 | 02:30:30.930 | 21,066 |

Labels P/Q reflect **filenames**, not independently verified model builds, precision, aligner/diarizer runs, VAD, decoding settings or hardware. These are independent model-labelled exports; common diarizer labels are not independent speaker verification. No additional raw/other-model S1E01 export was located in `sources/`.

| Artifact | SHA-256 |
| --- | --- |
| P | `5a1257ebcc8d96f7a6ceeef1eb699c0c59945fa06696273c75ddecdfd9f3509f` |
| Q | `52f941abf06a20aebf8081b0a79cac8612545587dafa66ea4a36ab2bf008d59c` |
| `local/Delvers S1E01. How Much Is Potato.mp3` | `ea32c8bc9db10c34e4e181b35105e0afec7a0be2493ed7830750ed3d8dbf1492` |

The MP3 is **144,634,246 bytes**, ffprobe duration **9,011.291813 seconds (02:30:11.292)**, with no title/date tags returned by the requested probe. It is **19.938 seconds shorter than P's final cue**, and **19.638 seconds shorter than Q's**. Matching basenames, common opening and matching narrative progression support association but do not establish identical ASR-input audio or a constant seek offset. Possible copy/edit/timing differences remain open. No claim that the SRT overruns prove omitted audio, and no cues were truncated to fit this copy.

## Method and numerical result

Both exports were read in contiguous recording-clock windows from the first cue through the final speech/network outro, ending at approximately **02:30:31**. Nothing was cut from the metric: production introduction, edited break transition, rules talk and closing credits are included.

1. Parse SRT cue content in chronological order, excluding indices and timing lines; both files' start times were checked as nondecreasing.
2. Remove optional `(speaker N)` decorations and join cue text. The existing `build_transcripts.parse_srt` parser independently reproduced the counts below without those decorations.
3. Lowercase; remove straight and curly apostrophes to join contractions; replace characters other than Unicode letters/digits with whitespace; split into word tokens.
4. Compute exact **unit-cost ordered word Levenshtein distance**, using `tokens` and `distance` from [the existing reproducible comparison implementation](../experiments/asr_backfill_2026_10_23.py). Its arbitrary-width bit-vector method has no time buckets, anchors, band limits or approximate cutoffs. The existing three-test `test_asr_backfill.py` suite passed in this pass, including comparison against a dynamic-programming oracle.

**P-reference comparison, Q relative to P:** **1,692 edits / 21,024 P tokens = 8.0479452055%, rounded 8.05% inter-ASR disagreement**. Q has **42 more tokens**. The distance is symmetric; the percentage denominator is explicitly P. No edit-type decomposition or word-timing precision is claimed.

**This is not WER, audio accuracy, confirmed omissions, hallucinations or a model ranking.** Neither token-count advantage nor agreement establishes correct speech. SRT intervals are cue timings, not word timings. Original media and SRT bytes are preserved.

## High-risk differences and shared ambiguities

Times below use **SRT clocks**, pending audio-copy alignment. P/Q cue IDs are export-local. Representative variants are retained rather than silently corrected.

| Window / locator | Text evidence | Research consequence / listening question |
| --- | --- | --- |
| 00:00:14–00:00:19, P 3–4 / Q 4–6 | Both render Sunday January tenth and **2020**; [publisher page](https://shows.acast.com/there-will-be-dungeons/episodes/6501086309d52c00124340d9) gives **January 11, 2021** publication | Shared ASR reading may still be wrong, or a spoken slip. Listen; leave recording date unverified |
| 00:02:50–00:03:00; 01:01:53–01:02:38 | P `a Tom or` / `atmur`; Q `Atamer` / `Atmer` | Preserve city spelling alternatives; no unsupported canonical geography |
| 00:03:46–00:06:05; 00:14:38–00:15:20; 00:25:12 | P/Q vary `Crandall/Splendorbelt/Splunderbelt`, `Evelyn Greenkeeper/Grinkeeper`, `co spiros/co-spyros` | Written preview/cast leads support working **Krandal Splenderbelt, Evelyn Grinkeeper, Koh Spiros**, separately from listening and historical sheet state |
| 00:29:23–00:30:26; 00:38:50–00:40:52 | `Helenar/Helenor/Eleanor/Helena Clearstone`; `mickles/Mikkels/Mickle's` | Supplier and farmer spellings unresolved; do not create several NPCs from variants |
| 00:30:15–00:30:26, P 481–485 / Q 725–734 | P `i'm retrenished` and unclear bread reply; Q `I'm Reverend Travis` then `He recommended this bread` | Context includes bread in the mouth. Neither supports adding a new identity/title **Reverend Travis** |
| 00:32:16–00:33:48 | P `thunderius storm`; Q `Pandaria Storm`, later `thunderous storms` | Guild foreword attribution, not an appearance; written handout **Thun’Darious Storm** is separate evidence |
| 00:41:35–00:42:07 | P `eye of grumps`; Q `Eye of Grumsh` | Covered guild trophy associated with an orc cult; no identification with Wastes's Eye of Groxl |
| 00:52:54–00:56:46 | P `bell soonish`, Q `bellsonish`; `Riley Man Cave`; `Solburn/soul burn` | Guild patrons' spellings and advice need checking. Edgar's reported loss is not observed death or the recovered dragonborn's identity |
| 01:05:14–01:05:17, P 1030 / Q 1663–1664 | P `my anything`; Q **Watch my flank. I'll kill them if they do anything** | Q carries a longer apparent threat/banter turn. Preserve as a candidate, not a confirmed P omission |
| 01:22:48–01:23:38; 01:35:47–01:37:04 | Q `twenty-eight plus two` in Cure Wounds talk; both later correct the modifier to spell level + two | Do not report 28 healing or retain the initial six as final; Evelyn gains one retroactive HP, Krandal caps at ten |
| 01:46:09–01:46:48, P 1631–1642 / Q 2685–2711 | P **I would be able to see this obviously**; Q **I wouldn't be able to see this obviously** | A consequential negation: narration already establishes blindness. Do not assert he actually sees the radiance while engulfed |
| 02:12:38–02:12:41, P 2041 / Q 3438 | P `he doesn't have to climb down`; Q `you guys have to climb down` | Subsequent action clearly includes Koh's rope descent and Guidance. Preserve local wording disagreement without erasing the performed descent |
| 02:03:28–02:05:06; 02:22:31–02:23:05 | Both mention an octopus eye, then piercer eye and darkmantle tentacle; later submitted parts are proboscis/tentacle/eyeball | Exact extra-eye collection unclear. Do not double count an unsupported retained trophy |
| 02:23:44–02:26:26 | P `Bran Broscale`, Q `Bran Brosgail`; later `ram's/Rams` and `rosescale/rose scales` drift globe | Badge **542** belongs to the missing delver per Cassius, not the orb. Keep owner name unresolved; different prior mission, not automatically Edgar |
| 02:27:58–02:28:05 | Q groups `Very good` with speaker 2 before Koh's homeward reply; P assigns the acknowledgment to GM label 1 | Boundary/speaker alignment can leak adjacent words; map roles from context, not label alone |
| 02:29:36–02:30:31 | P `boving to you`; Q describes waving, plus slightly different ending segmentation | Do not infer Beau's physical return to the table from stray outro recognition. Both contain network credits, but local MP3 timing must be reconciled |

## Research decisions and next check

The shared played sequence supports a completed farm sealing job, paid reward, recovered badge returned, and drift globe retained by Koh. The grick is seen by Koh, identified later by Cassius and left alive below the sealed route. The crypt is tomorrow's assignment, not a played outcome. No later Delvers sources or Wastes lore were used to fill gaps.

Use **DEL-PREP-002** to establish MP3/SRT alignment before translating any listening windows. Then prioritize name/date windows, the Sacred Flame negation and healing/custody wording under the [Delvers queue](../delvers/REVIEW_QUEUE.md). No listening resolution is recorded here. **Next verified source pair: Delvers S1E02 — Agreeable Meatball.**

## Documentation validation

All **24** Markdown files in this change, including the new Delvers namespace, pass the installed Markdownlint library with the repository configuration. The standard `npm run lint:markdown` runner includes Delvers and reports **eight MD012 blank-line violations** in unrelated files. Running the same configured lint against the starting commit's 315 maintained Markdown files reproduced all eight, so they are baseline findings. Relative paths/anchors and source SHA-256 checks were also performed; both SRTs and the MP3 retain their input hashes. Git whitespace checks passed.

Unrelated Wastes/October-bonus working-tree edits appeared after the initial clean check, including a separate entry in the shared model log. Those edits were preserved and are outside this Delvers change. No commit, staging, push or source transcript/media edit was performed for this pass.
