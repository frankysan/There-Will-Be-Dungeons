# Wastes S1E004 — The Oil Demon: ASR comparison (2026-10-23)

**Played session; ASR-provisional.** Whole-export computation includes credits
and the final “Not again” line. No new model execution, listening or transcript
correction occurred. [Episode dossier](../episodes/E004.md).

## Inputs and measurements

| Export | Pipeline label from filename | Cues | Normalized tokens | Last cue end |
| --- | --- | ---: | ---: | --- |
| [Parakeet](../sources/The%20Wastes%20S1E004.%20The%20Oil%20Demon.parakeet.processed.srt) | Parakeet processed | 4,180 | 26,934 | 02:54:08 |
| [Qwen](../sources/The%20Wastes%20S1E004.%20The%20Oil%20Demon.qwen-q8.canary-ctc.nemotron.srt) | Qwen Q8 / Canary CTC / Nemotron | 4,951 | 26,686 | 02:54:08 |

**Exact ordered word Levenshtein: 2,604 edits / 26,934 Parakeet tokens = 9.67%.**
Direction and denominator are processed Parakeet to Qwen. This measures export
disagreement, not audio-grounded WER, omissions or model accuracy.

Normalization joins chronological cue content without speaker decorations,
lowercases, removes straight/curly apostrophes, replaces non-Unicode-letter/digit
characters with spaces, then splits. Repetitions remain. The exact bit-vector
metric is independently checked against dynamic programming. Separate time-aware
alignment yields **2,063 candidate groups**, with **zero fallback blocks**.
Both inputs have zero nonpositive cue durations; Parakeet has zero adjacent
overlap pairs and Qwen has one. Neither structure nor cue count proves coverage.

## Selected parallel-text review

| Recording window | Observed export disagreement | Review action |
| --- | --- | --- |
| 00:44:15–00:45:50 | Qwen has extra fragments around the question about the well; at the end of the window the ruin is `Moegfarain` versus Parakeet `Mog Forain`. Both attribute the Peter/well account to the entity. | Check interjections and the place name against audio/written evidence. Do not make the entity's historical claim an independently verified fact. |
| 01:51:45–01:52:30 | Qwen adds “It might be better to have more hit points than less” at 01:52:14–01:52:16 (cues 3176–3177); Parakeet goes from the player's deliberation to standing and casting Cure Wounds. | Listen for overlapping table advice and its speaker. Both contain the stand/cast declaration; this does not establish additional healing or a different mechanical outcome. |
| 02:53:20–02:54:08 | Both retain the network credits and “Not again! I don't want to hurt anyone.” | Check the ending against audio before classifying trailing text as a stinger, unrelated background speech or hallucination. Agreement alone does not decide. |

These are selected contextual text checks. Complete-export metric coverage is
not a claim of manual reading or listening to every cue. Speaker IDs remain local
to each recognizer's export.

## Reproduction and remaining evidence

Run `python experiments/asr_backfill_2026_10_23.py`. The
[JSON evidence](ASR_BACKFILL_2026-10-23.json) retains source paths, SHA-256,
millisecond endpoints, anomaly cue IDs and all candidate wording/cue references.
All source hashes were unchanged after computation. Candidate alignment uses
2,000 ms drift, 192-token blocks and 30,000 ms fallback buckets; its normalization
is distinct from the global metric. SRT intervals are not word timings.

Pairing relies on corrected filenames and matching introductory content; original
audio hashes and precise recording-clock equivalence remain unverified. Model
builds, inference settings, hardware and runtime are unknown. Listen to selected
windows and agreed controls before accepting text. [Coverage](ASR_COMPARISON_COVERAGE_2026-10-23.md)
· [Review queue](../project/REVIEW_QUEUE.md).
