# Wastes S1E002 — Spiders: ASR comparison (2026-10-23)

**Played session; ASR-provisional.** This compares the complete existing exports,
including the final network credits. No new recognition, listening or transcript
correction occurred. [Episode dossier](../episodes/E002.md).

## Inputs and measurements

| Export | Pipeline label from filename | Cues | Normalized tokens | Last cue end |
| --- | --- | ---: | ---: | --- |
| [Parakeet](../sources/The%20Wastes%20S1E002.%20Spiders.parakeet.processed.srt) | Parakeet processed | 4,257 | 27,096 | 02:39:16 |
| [Qwen](../sources/The%20Wastes%20S1E002.%20Spiders.qwen-q8.canary-ctc.nemotron.srt) | Qwen Q8 / Canary CTC / Nemotron | 5,020 | 26,744 | 02:39:15 |

**Exact ordered word Levenshtein: 2,897 edits / 27,096 Parakeet tokens = 10.69%.**
The denominator and comparison direction are processed Parakeet to Qwen. This is
inter-ASR disagreement, not audio-grounded WER or an accuracy ranking.

All cue text is joined in chronological order after removing leading speaker
decorations, lowercased, stripped of straight/curly apostrophes, and split after
replacing non-Unicode-letter/digit characters with spaces. Repetitions remain.
The dependency-free exact bit-vector metric is checked against an independent
dynamic-programming implementation. A separate existing time-aware alignment
locates **2,244 candidate groups**, with **zero bounded fallback blocks**; those
groups do not measure edit distance. Both exports have zero nonpositive-duration
cues and one adjacent overlap pair each. Overlap is not itself a speech error.

## Selected parallel-text review

| Recording window | Observed export disagreement | Review action |
| --- | --- | --- |
| 00:56:30–00:57:10 | Qwen adds “Tell us how the pump works. You are not in a position to negotiate” between the Hillmaster's warning and “Fine”; Parakeet moves directly to “Here. Fine”. Candidate is at 00:56:52–00:56:57, Qwen cues 1836–1838. | Listen for a short interjection and its speaker. Do not automatically insert the Qwen wording or strengthen the Hillmaster's technical testimony. |
| 01:27:47 | Parakeet-only aligned text repeats `tuk` nine times. | Check whether this represents voiced sound effects, music, meaningful speech or an alignment difference. Preserve the source repetition pending listening. |
| 02:35:20–02:36:50 | Both descriptions identify the falling body's head as the Hillmaster's. Around 02:35:49–02:35:57 Parakeet's repeated `no` has no aligned Qwen words, although Qwen also has `No!` in the surrounding same-clock passage. | Verify shout timing and overlapping reactions; an empty aligned side does not establish absence from the export or recording. Keep the death scene distinct from E003's later recap. |

These are selected textual windows, not a manual review of every cue. Both full
exports were parsed for the global metric and candidate evidence; the existing
dossier remains provisional. No speaker number was mapped across runs.

## Reproduction and remaining evidence

Run `python experiments/asr_backfill_2026_10_23.py`. The
[machine-readable evidence](ASR_BACKFILL_2026-10-23.json) contains exact source
paths, SHA-256, millisecond endpoints, structural anomalies and every candidate
with both texts and cue IDs. Source hashes were unchanged after computation.
The alignment uses 2,000 ms drift, 192-token blocks and 30,000 ms fallback buckets;
its lexical normalization differs from the global metric and never assigns word
times within SRT cues.

Pairing rests on corrected filenames, title and corresponding opening content;
original audio identity and exact recording-clock equivalence remain unverified.
Builds, decoding/VAD settings, hardware, inference runtime and audio hashes were
not established. Listen to the selected windows, the opening/ending and agreed
controls before accepting wording. [Coverage and next work](ASR_COMPARISON_COVERAGE_2026-10-23.md)
· [Review queue](../project/REVIEW_QUEUE.md).
