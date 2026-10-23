# Wastes S1E003 — Soft Head Returns: ASR comparison (2026-10-23)

**Played session; ASR-provisional.** Both existing exports were parsed through
the network credits and post-credit music comment. No new ASR, listening or
source correction occurred. [Episode dossier](../episodes/E003.md).

## Inputs and measurements

| Export | Pipeline label from filename | Cues | Normalized tokens | Last cue end |
| --- | --- | ---: | ---: | --- |
| [Parakeet](../sources/The%20Wastes%20S1E003.%20Soft%20Head%20Returns.parakeet.processed.srt) | Parakeet processed | 4,808 | 32,144 | 03:10:52 |
| [Qwen](../sources/The%20Wastes%20S1E003.%20Soft%20Head%20Returns.qwen-q8.canary-ctc.nemotron.srt) | Qwen Q8 / Canary CTC / Nemotron | 5,635 | 31,397 | 03:10:52 |

**Exact ordered word Levenshtein: 3,266 edits / 32,144 Parakeet tokens = 10.16%.**
Direction and denominator are processed Parakeet to Qwen. This is inter-model
disagreement, not WER against an audio reference or a recognizer ranking.

Method: join chronological cue text without leading speaker decorations,
lowercase, remove straight/curly apostrophes, replace characters other than
Unicode letters/digits with spaces, and split. Retain repetitions. The exact
bit-vector implementation is independently checked against dynamic programming.
The separate time-aware alignment produces **2,627 candidate groups**, with
**zero fallback blocks**. Neither export has nonpositive cue durations or adjacent
overlap pairs. Candidate counts and subtitle counts do not measure correctness.

## Selected parallel-text review

| Recording window | Observed export disagreement | Review action |
| --- | --- | --- |
| 01:18:20–01:18:27 | Parakeet has fifteen `dunk/dum/dun` tokens with no aligned Qwen wording. | Check sound effects/music and interruptions; do not silently delete Parakeet text or treat token-count advantage as speech coverage. |
| 02:24:05–02:25:00 | Qwen includes a GM-style handoff sentence beginning “Vorel and Stanley, this this giant rocket pack…” at 02:24:25. Parakeet has the preceding plan to drop it off and then “What's this?” without that sentence. | Listen for the handoff, overlapping speech and the speaker boundary. Both exports already mention a rocket pack; do not turn an extra sentence into a new item or a proven omission. |
| 02:44:15–02:45:40 | Parakeet writes `C4N C4N-D13`; Qwen spells the sounds as `C C four N C four N dash D thirteen`. The candidate spans Parakeet cue 4208 and Qwen cue 4951. | Separate alphanumeric formatting from recognition. This contributes to token edits without establishing a different robot identity. Keep designation spelling provisional. |
| 03:06:35–03:07:25 | Both describe a frail living dwarf and a helmet/tube connection to an oil-like figure. Qwen repeats “A tube leading out of it” near 03:07:06; Parakeet has a single tube description. | Verify whether this is a repeated phrase or model variation. Preserve the living-versus-skeleton distinction and do not infer a second tube from token disagreement. |

Only these parallel windows received contextual textual inspection in this pass;
the metric and candidate extraction consume every cue. No cross-run speaker
mapping or audio-verified conclusion follows from agreement.

## Reproduction and remaining evidence

Run `python experiments/asr_backfill_2026_10_23.py`. The
[complete JSON evidence](ASR_BACKFILL_2026-10-23.json) preserves source paths,
SHA-256, exact cue endpoints and all timed candidate texts/cue IDs. All input
hashes remained unchanged. Candidate alignment uses 2,000 ms drift, 192-token
blocks and 30,000 ms fallback buckets; its lexical normalization is separate from
the global metric. SRT timing remains cue-level.

Pairing uses matching corrected ID, title and introductory content; original audio
identity and offsets remain unverified. Exact model builds, settings, hardware,
runtime and audio hashes are unknown. Listen to the windows, opening/ending and
agreed controls before accepting wording. [Coverage](ASR_COMPARISON_COVERAGE_2026-10-23.md)
· [Review queue](../project/REVIEW_QUEUE.md).
