# Initial model tests (supplied by archive owner)

## 2026-10-22: first Qwen Q8 + Canary CTC + Nemotron batch intake

[Reproducible intake report](../reports/QWEN_CANARY_INTAKE_2026-10-22.md) and
[complete candidate evidence](../reports/QWEN_CANARY_INTAKE_2026-10-22.json) compare
the March and April 2019 bonus exports plus the additional E039 export with their
existing processed Parakeet counterparts. All three Qwen SRTs parse and have
zero nonpositive cue durations; adjacent overlaps are 3 / 3 / 0 respectively.
Time-aware alignment produces 2,245 / 357 / 1,623 candidate groups without bounded
fallback. Counts describe disagreement, not audio-verified errors or omissions.

The owner identifies the new configuration as Qwen Q8 + Canary CTC + Nemotron;
exact builds, VAD/chunking, decoding, post-processing and runtime remain
unconfirmed. These recordings have no same-audio Q8-without-Canary control, so
this intake does not establish alignment-only text preservation. April's
different basenames were paired using the matching opening introduction; audio
hash identity has not been verified. Source hashes were unchanged after analysis.
No recognizer was executed, no listening was performed and no transcript wording
was accepted. The report supplies timed review examples in both directions.

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

## 2026-10-21: E001 Parakeet segmentation experiments

[Full five-run benchmark with transcript comparisons and audio-review targets](../reports/PARAKEET_SEGMENTATION_2026-10-21.md). CrispASR 0.8.43, Parakeet TDT 1.1B GGUF, English, Radeon RX 9070 via Vulkan, 600 seconds of the same E001 audio. The following are **machine-output comparisons, not audio-verified WER**.

| Run | Time / speed | Words | Finding |
|---|---:|---:|---|
| Full audio, no VAD | 15.75 s / 38.1× | 1,701 | Preserves the opening greeting; provisional baseline |
| Default Silero VAD | 13.33 s / 45.0× | 1,699 | Misses candidate `hello everybody`, captures other possible brief remarks |
| VAD with 700 ms padding | 12.96 s / 46.3× | 1,699 | Recovers greeting; nearly merges VAD regions; near-same-time duplicate `if` |
| 30 s chunks + 3 s overlap, LCS auto | 15.77 s / 38.0× | 1,692 | Some better phrases, but possible lost greetings around 01:40 |
| Same chunks, LCS off | 14.96 s / 40.1× | 1,692 | **JSON and SRT are byte-identical** to LCS auto |

Stop optimizing segmentation based solely on model-to-model agreement. Listen to the timestamped review samples before revising the model choice. No existing source SRTs or transcript drafts were changed in this test.

## 2026-10-21: reproducible multi-pass export comparison

[Implementation](../reports/MULTIPASS_PIPELINE.md) and
[measured pilot with machine-readable evidence](../reports/MULTIPASS_PILOT_2026-10-21.md).
The new standard-library tooling compares full E000/E001 Parakeet/Qwen Q8 SRTs
and the five 600-second Parakeet JSON runs against each other and the opening of
the full Qwen export. Explicit common coverage prevents the rest of a full
episode being labelled missing from a short run. Original wording, source hashes,
cue/word timing precision, probabilities and configuration uncertainty survive.

The local export pilot produces structured disagreement reports, padded job
proposals and provisional reconciliation with no automatic text changes. It
rediscovers the `hi`/`kyle` versus `i guess` discrepancy, the 03:08 near-same-time
`if if`, and timestamps beyond the requested 600 seconds. These are not new
listener-verified findings. C1/C2 remain byte-identical historical experiments.

The installed CrispASR help was inspected for the optional single-job adapter;
the adapter's bounded argument construction and hash rejection are tested.
E000/E001 original audio was not found in the expected local locations, so no new
recognizer run or listening verification was performed. No model/configuration
was promoted on the basis of these comparison counts.

## 2026-10-21: first real bounded third pass

After the original E000/E001 MP3s became available, both matched the existing
manifest hashes. [Real execution and import evidence](../reports/TARGETED_VERIFICATION_2026-10-21.md)
records one Parakeet TDT 1.1B run on E001 01:14.760–01:44.400: 29.640 s of
mono 16 kHz PCM, CrispASR 0.8.43 / eb633d90, Vulkan, English, no explicit
VAD/chunking. Extraction took 0.816 s; the ASR process including startup took
2.850 s. The 101-word result includes `hi kyle hi hi`, while the historical
chunked versions contain `i guess`. This remains an unreviewed alternative.

The clipped run is the same recognizer family with a different window, not a
new independent-model vote. Import retained all six historical runs, all fifteen
prior alignments and all 971 candidate IDs, adding 56 pairwise review records.
The portable export removes only an embedded private model path and preserves
the entire transcription array. No audio-based wording decision, WER claim or
canonical transcript update follows from this run alone.

## 2026-10-21: two-process CrispASR throughput observation

[Full observation, limitations and controlled follow-up](../reports/ASR_CONCURRENCY_2026-10-21.md). The owner ran **two CrispASR instances concurrently** and reported near-full 32 GB system RAM, ~8.5 GB/16 GB VRAM, GPU copy/compute peaks around 25%, virtually no drive activity, and approximately **6–7 minutes completion time per episode** without obvious slowdown. This is a provisional throughput observation; episode durations/settings and sequential control timings are not yet recorded. It does **not** measure ASR accuracy.
