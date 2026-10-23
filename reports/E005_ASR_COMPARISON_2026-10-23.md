# Wastes S1E005 — Goblincide: ASR comparison (2026-10-23)

**Played session; ASR-provisional.** Both full exports were computed through the
final “Oops” after the network credits. No new ASR execution, listening or source
correction occurred. [Episode dossier](../episodes/E005.md).

## Inputs and measurements

| Export | Pipeline label from filename | Cues | Normalized tokens | Last cue end |
| --- | --- | ---: | ---: | --- |
| [Parakeet](../sources/The%20Wastes%20S1E005.%20Goblincide.parakeet.processed.srt) | Parakeet processed | 4,191 | 27,354 | 02:47:31 |
| [Qwen](../sources/The%20Wastes%20S1E005.%20Goblincide.qwen-q8.canary-ctc.nemotron.srt) | Qwen Q8 / Canary CTC / Nemotron | 4,976 | 27,130 | 02:47:31 |

**Exact ordered word Levenshtein: 2,855 edits / 27,354 Parakeet tokens = 10.44%.**
Direction and denominator are processed Parakeet to Qwen. This is inter-ASR
disagreement, not WER against verified audio or a quality ranking.

Normalize by joining chronological cue text without speaker decorations,
lowercasing, deleting straight/curly apostrophes, replacing characters other than
Unicode letters/digits with spaces and splitting. Repeated words remain. The
exact bit-vector metric is independently checked against dynamic programming.
Separate time-aware alignment produces **2,119 candidate groups**, with **zero
fallback blocks**. Both inputs have zero nonpositive-duration cues; adjacent
overlap pairs are zero for Parakeet and one for Qwen. These are structural facts.

## Selected parallel-text review

| Recording window | Observed export disagreement | Review action |
| --- | --- | --- |
| 00:23:15–00:23:45 | Qwen adds “We should have died in there. Yet we didn't. We persevered. Why can't we now?” after the recollection of Quizquaz's prediction. Parakeet moves directly to the water-supply objection. | Listen for interruptions and attribution. The extra argument does not establish another death, resurrection or successful removal of the engine. |
| 00:52:10 | Parakeet-only aligned text contains fifteen `dunk/dum/dung` tokens. | Check music, vocal effects and overlap before treating the sequence as speech to retain or remove. |
| 02:29:00–02:29:50 | The trader appears as `Boxtow` in Parakeet and `Boksto` in Qwen. Both introduce his offer in the same scene. | Keep competing name forms searchable; no canonical orthography follows from two phonetic readings. The map labels in the dossier still need source-map/audio review. |
| 02:47:00–02:47:31 | Both contain the session-six sign-off. Qwen locates it around 02:47:02; Parakeet has it around 02:47:10–02:47:19. Time-aware alignment therefore labels text unilateral on both sides. | This is an observed export timing difference, not evidence either export lacks the sign-off. Check its true audio position and repeated network announcement separately. |

Contextual manual text inspection is limited to the selected windows; all cues
feed the global metric and candidate extraction. No speaker-number equivalence
across exports was assumed. Preserve the dossier's E005/E006 cutoff: successful
surface-water testing is not established by this comparison.

## Reproduction and remaining evidence

Run `python experiments/asr_backfill_2026_10_23.py`. The
[complete JSON evidence](ASR_BACKFILL_2026-10-23.json) retains source paths,
SHA-256, millisecond endpoints, structural anomalies and every candidate's text
and cue IDs. Input hashes remained unchanged. Candidate alignment uses 2,000 ms
drift, 192-token blocks and 30,000 ms fallback buckets; its lexical normalization
is separate from the global metric. SRT timings remain cue-level.

Filename/title and introductory content support pairing; original audio hashes,
precise clock equivalence, builds, settings, runtime and hardware remain unknown.
Listen to the windows, opening/ending and agreed controls before accepting text.
[Coverage and next work](ASR_COMPARISON_COVERAGE_2026-10-23.md) ·
[Review queue](../project/REVIEW_QUEUE.md).
