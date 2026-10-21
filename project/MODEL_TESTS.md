# Initial model tests (supplied by archive owner)

These results describe **the user's actual local Subtitle Edit tests**, not generic benchmark claims. The real-time factors were approximate relative comparisons rather than standardized throughput measurements.

| Engine | Configuration as reported | Observations |
|---|---|---|
| Cohere Transcribe | `cohere-transcribe` + `Nemotron-3-Diarization.q8_0` + built-in aligner | Substantial speech omissions, **listener-confirmed** |
| Parakeet TDT 1.1B | `parakeet-tdt-1.1b` + `Nemotron-3-Diarization.q8_0` + built-in aligner | Strong current coverage/speed candidate; raw no-postprocessing SRTs additionally provided |
| Qwen3-ASR 1.7B F16 | `qwen3-asr-1.7b-f16` + `Nemotron-3-Diarization.q8_0` + `qwen3-forced-aligner-0.6b-q8_0` | Reported 7–8× slower than the fast alternatives; tested on E000 |
| Qwen3-ASR 1.7B Q8 | `qwen3-asr-1.7b-q8_0` + `Nemotron-3-Diarization.q8_0` + `qwen3-forced-aligner-0.6b-q8_0` | Reported 2–3× slower; valuable independent comparison |
| ARK | Configuration not recorded | Speaker identification failed; this does not, on its own, establish recognition accuracy |

## Comparison limitations

The Cohere and Qwen files supplied for this pilot are post-processed. Some speaker names were replaced globally by find-and-replace, preserving each engine's assignments but changing their labels. The additional Parakeet no-postprocessing files came from a **new run**, so differences cannot be ascribed exclusively to the post-processing module.

The originals are retained in `sources/`; **do not rank word accuracy solely by similarity to another model**. Only a verified reference or actual listening can establish correctness.

## 2026-10-21: additional Qwen raw-output variants

Six Qwen SRTs (Q4, Q4 + Canary CTC, and Q8, for E000 and E001) were added unmodified to `sources/`. [Detailed comparison](../reports/QWEN_VARIANTS_2026-10-21.md) and [machine-readable metrics](../reports/QWEN_VARIANTS.json) record the results. The `q4.raw.srt` filename does **not** prove no aligner was used; it only distinguishes the no-Canary export from the Canary variant.

**Findings:** Q4 + Canary preserves all Q4 text exactly while eliminating all E001 nonpositive cue durations (56 → 0). It also changes E001 speaker attribution for 924/32,007 tokens because cue boundaries and labels change. Q4 and Q8 recognition differ by 1,070 word edits in E001 and 17 in E000. These are disagreements, not an accuracy ranking.

Next experimental priority: audio-verified Q4/Q8/Parakeet discrepancies, plus a Q8 + Canary alignment run if Q8 is favored.
