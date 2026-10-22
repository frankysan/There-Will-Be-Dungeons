# Qwen Q8 + Canary CTC + Nemotron: first intake — 2026-10-22

**Status:** Export structure and model disagreement only; no listening, audio-grounded accuracy measurement, new ASR execution, or canonical transcript edits.

Owner reports Qwen Q8 + Canary CTC + Nemotron; filenames agree. Model/build versions, VAD, chunking, decoding, post-processing and runtime unconfirmed.

Unicode lexical tokens excluding leading speaker labels; existing time-aware alignment with 2000 ms drift, 192-token cap, 30000 ms fallback buckets. Cue intervals are not word timestamps. Parakeet sources are processed, so differences can include recognition and processing. No same-episode Q8 without Canary is available for these pairs; aligner text preservation cannot be isolated.

The two alphabetical bonus exports and the additional E039 export were present at intake. April has different source basenames; its opening introduction corresponds in both exports. Pairing is provisional from filenames/content, not verified audio identity.

| Recording | Source | Cues | Normalized words | Nonpositive durations | Adjacent overlaps | Last cue end |
|---|---|---:|---:|---:|---:|---|
| BONUS-2019-03 | Parakeet processed | 3,572 | 32,625 | 0 | 0 | 03:01:13 |
| BONUS-2019-03 | Qwen Q8 + Canary + Nemotron | 5,564 | 33,646 | 0 | 3 | 03:01:13 |
| BONUS-2019-04 | Parakeet processed | 610 | 5,607 | 0 | 0 | 00:31:04 |
| BONUS-2019-04 | Qwen Q8 + Canary + Nemotron | 934 | 5,769 | 0 | 3 | 00:31:03 |
| E039 | Parakeet processed | 3,186 | 28,281 | 0 | 0 | 03:34:07 |
| E039 | Qwen Q8 + Canary + Nemotron | 5,087 | 28,438 | 0 | 0 | 03:34:07 |

## BONUS-2019-03

2,245 candidate groups; 0 bounded fallback blocks. These are review hypotheses.

- **00:40:29–00:40:33**: Parakeet: `(no aligned words)`; Qwen: `tile set I made a note I made a mental`.

- **02:09:59–02:10:03**: Parakeet: `(no aligned words)`; Qwen: `ah she can never do this You're like`.

- **00:07:34–00:07:38**: Parakeet: `but data but that but`; Qwen: `(no aligned words)`.

- **00:25:47–00:25:51**: Parakeet: `shep fifty one fifty`; Qwen: `(no aligned words)`.

## BONUS-2019-04

357 candidate groups; 0 bounded fallback blocks. These are review hypotheses.

- **00:19:06–00:19:07**: Parakeet: `(no aligned words)`; Qwen: `I think the role play`.

- **00:27:31–00:27:34**: Parakeet: `(no aligned words)`; Qwen: `Well they had that whole`.

- **00:03:41–00:03:41**: Parakeet: `like the fate for`; Qwen: `(no aligned words)`.

- **00:18:18–00:18:19**: Parakeet: `i said`; Qwen: `(no aligned words)`.

## E039

1,623 candidate groups; 0 bounded fallback blocks. These are review hypotheses.

- **02:39:17–02:39:21**: Parakeet: `(no aligned words)`; Qwen: `immortal myself I do not fear this man`.

- **03:31:02–03:31:06**: Parakeet: `(no aligned words)`; Qwen: `László I'll wave at László See you`.

- **00:07:11–00:07:12**: Parakeet: `four but it's not very tall he`; Qwen: `(no aligned words)`.

- **02:32:55–02:32:56**: Parakeet: `traversed these passages below the keep m`; Qwen: `(no aligned words)`.

## Reproduction and interpretation

`python experiments/qwen_canary_intake_2026_10_22.py` regenerates this report and the [JSON](QWEN_CANARY_INTAKE_2026-10-22.json), including every candidate, cue references and source SHA-256. Both sides retain every lexical token through alignment; all six source hashes were unchanged after analysis. Neither word counts nor candidate counts measure accuracy. Speaker IDs are local to each run. Overlaps can be simultaneous speech; valid cues do not establish accurate alignment.

Listen to the examples above, plus randomly selected agreed passages, before accepting wording. Check introductions and endings against audio for dropped speech or music hallucinations. Obtain exact settings/runtime before treating these as a reproducible production configuration. A same-audio Q8 export without Canary is still needed to isolate alignment effects.
