# Parakeet segmentation benchmark — E001 opening ten minutes (2026-10-21)

**Status:** ASR-output comparison, **not audio-verified accuracy**. This is an experiment log for *The Wastes S1E001 — The Campaign Begins!*, not a replacement for the existing E001 transcript or its listener-review decisions.

## Purpose and evidence

Test whether VAD, VAD padding, and shorter overlapping chunks improve speech coverage for fast multi-speaker conversation without hallucinating or duplicating words. All five trials ran on the **same opening 600 seconds** of the same MP3. Inputs for the analysis were the owner's CrispASR console logs and the full, word-timed JSON/SRT exports. The original audio was **not supplied for a new listening comparison** in this evaluation.

- Software: CrispASR **0.8.43** (git `eb633d90`), Parakeet **TDT 1.1B** GGUF, English; GPU backend `vulkan` on **AMD Radeon RX 9070 (16 GiB)**; Windows, four CPU threads. The logs confirm `Vulkan0` was initialized; the separate Silero VAD stage may run on CPU.
- Common recognition settings: `--backend parakeet -m ".\models\parakeet-tdt-1.1b.gguf" -l en --gpu-backend vulkan -d 600000 -ojf -osrt -v`. The exact input path is intentionally excluded from repository documentation. Output stems distinguish each run. The VAD experiments included the previously specified strict/require-VAD options; the chunking tests included `--strict-pipeline`.
- JSON contains per-word timestamps and per-token probabilities. **Confidence is not a calibrated accuracy score.** SRT cues are long processing segments, not publishable subtitle lines.
- Existing E001 audio-verified facts (Cohere's substantial omissions; the extra diarization cluster being Scott's character voice) are separate from the *unverified* differences discussed below. See [model tests](../project/MODEL_TESTS.md), [review queue](../project/REVIEW_QUEUE.md), and [external evidence policy](../project/EXTERNAL_REFERENCES.md).

## Configurations and measured output

| Run | Difference from common recognition settings | Time to process 600 s | Speed | Words | Output segments | Confidence tokens | Mean token probability | Tokens < 0.90 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| B0 full audio | No explicit VAD or chunking | 15.75 s | 38.1× | 1,701 | 7 | 2,828 | 0.9764 | 191 |
| V1 default VAD | `--vad`; default threshold/padding | 13.33 s | 45.0× | 1,699 | 16 | 2,828 | 0.9781 | 173 |
| V2 padded VAD | `--vad --vad-speech-pad-ms 700`; default threshold | 12.96 s | 46.3× | 1,699 | 7 | 2,815 | 0.9754 | 188 |
| C1 chunked + dedup | `--chunk-seconds 30 --chunk-overlap 3 --lcs-dedup auto`; no VAD | 15.77 s | 38.0× | 1,692 | 20 | 2,804 | 0.9769 | 192 |
| C2 chunked, dedup off | Same, except `--lcs-dedup off` | 14.96 s | 40.1× | 1,692 | 20 | 2,804 | 0.9769 | 192 |

These are **single runs** per condition, not replicated timing benchmarks. Do not rank quality by speed, confidence, or raw word count.

### VAD region coverage

- Default Silero VAD identified **145** speech regions covering about **510.42 s** of the ten-minute window, excluding approximately **89.58 s**. Its first region began near **00:12.29**.
- With **700 ms padding**, there were still **145** detected regions, but their expanded coverage reached about **588.31 s**, excluding only **11.69 s**. The first region began near **00:11.62**. Expanded regions practically merged into two spans, removing most of the original silence-skipping benefit.
- **B0** and **V2** recognized `hello everybody` at approximately **00:11.76–00:11.78**; **V1** started later with `and welcome`. Thus default VAD has a **plausible missed greeting**, but this remains a hypothesis until checked by listening.
- The baseline also emitted `no m h` between **00:00.32–00:01.00**, which may be non-speech/music hallucination. Do not delete solely on this inference.

### Output-text comparison (not WER)

Word-level comparisons below use ordered exact-word sequence alignment (longest matching subsequence); they do **not** use an audio ground truth. Word positions can differ even when the recognized phrase is equivalent.

| C1 compared with | Matching words in order | Words on other side unmatched | C1 words unmatched |
|---|---:|---:|---:|
| B0 | 1,649 | 52 | 43 |
| V1 | 1,639 | 60 | 53 |
| V2 | 1,641 | 58 | 51 |

**C1 and C2 are exactly identical** in their entire **JSON** and **SRT** outputs, including word timestamps and confidence probabilities. File byte equality was independently checked by SHA-256:

- C1/C2 JSON: `ac9dc3c9dc6d338bc7804cdba1a979da6b645a526c1159fdc097c9818a8187f6`
- C1/C2 SRT: `e9d7ed524e39f241f33588f5025b921a23b22adbdf8cdf7aa108f6dee84b2ddc`

This means **turning LCS deduplication off did not restore any missing words or change the exported result in this case**. Do not infer that the option never operates on other recordings, or that the cause of any missing phrase has been proven. The difference between 15.77 and 14.96 seconds is a single-run runtime variation, not an accuracy gain.

## Specific review candidates

All rows below describe *differences between ASR runs* unless a separate evidence class is explicitly stated. A smooth transcript is not automatically a faithful transcript; preserve real interjections, interruptions and false starts.

| Approximate episode time | Observation | What listening must determine |
|---|---|---|
| 00:00–00:12 | B0/C1/C2 output `no m h` before the greeting; V1 omits the greeting, V2 recovers it | Is the initial text speech or music/noise? Is `hello everybody` clearly audible? |
| 01:23–01:28 | V1 includes `you also shouldn't show our…`, whereas B0/V2/C1/C2 begin closer to `or…` | Whether a participant says those extra words and whether recognition is garbled |
| 01:40–01:42 | B0/V1/V2 recognize multiple `hi` / `kyle` responses; C1/C2 instead output `i guess` | Check greeting sequence, turn-taking and any omitted short response |
| 02:17–02:21 | V1 includes brief `yeah` interjections missing in some other trials | Which voices/interjections were actually audible? |
| 02:32 | V2 recognizes `you're sweating`; C1/C2 do not | Is it spoken and overlapped by someone else? |
| 02:40 | C1/C2 produce `armpit` rather than `armit` / `arpit` | Verify exact phrasing |
| 02:54–02:55 | V1 recognizes `finality` and others omit it | Is the word actually spoken? |
| 03:08 | V2 produces `if if` with near-identical timestamps (**03:08.510–03:08.750** and **03:08.520–03:08.760**); C1/C2 contain one `if` | Very likely boundary/stitching duplicate; confirm before final correction |
| 04:13 | Chunked versions include `no i can go`; other settings differ | Check for recovered side remark |
| 04:37 | Some settings capture a `whoa` reaction while others omit it | Is the reaction audible? |
| 05:16–05:18 / 06:32 / 07:14 | Recognition differs around Dusthill description, false starts such as `is by is populated`, and `finally` before the garage | Compare to the original narration **audio**; a fan-wiki exposition passage may help with spelling but is not a verbatim reference |

Other machine-output issues: `Dusthill` becomes `dust hill`, `dus hill` or `dusill`; `Beau Schwartz` becomes `bo` or `both`; and concatenations such as `toestablish`, `foundedessentially`, `thoroughvetting` occur. Consult the [wiki-backed spelling registry](../project/EXTERNAL_REFERENCES.md), but do **not** overwrite raw ASR outputs, infer spoken dialogue from wiki prose, or import end-of-campaign sheet information into E001.

### Timing and stitching cautions

- B0 has **0** word-level backwards overlaps, V1 **1**, V2 **1**, C1/C2 **0** (defined as a word beginning before the previous word's end). V2's duplicate `if` is a genuine timestamp anomaly; one V1 overlap involves adjacent `the`/`yeah` and may be legitimate simultaneous speech.
- The **C1/C2 final word ends at 00:10:00.800**, although the requested audio window is `[0, 600.00 s)`; treat this as an output timestamp-boundary anomaly rather than proof extra audio was read.
- All five runs provide per-word timestamps. None of these ASR-only results has speaker diarization or restored punctuation, and none of the raw SRTs is ready to publish.
- CrispASR's own gap-fill messages report 6 recovered words in B0, 1 in V1, 0 reported in V2, and 5 in each of C1/C2. A gap-fill count is **not** an independent measure of total omitted words.

## Provisional decision

**Retain B0 (full-audio Parakeet, no explicit VAD/chunking) as the primary comparison baseline.** Keep V1 as a *secondary disagreement detector*, not a source of automatic inserts; V2's near-total audio coverage plus boundary duplication makes it a poor production default. C1/C2 do not establish better completeness; importantly, switching LCS deduplication did not change the output. No config has established lower audio-grounded WER/deletion rate yet.

**Stop tuning segmentation blindly.** Next: listen to a timestamped, manually verified E001 reference sample emphasizing overlapping banter and short greetings (**00:11, 01:23–01:42, 02:17–03:08, 04:13–04:37**), plus a narrative sample containing **Dusthill** (about **04:45–08:45**). Use that reference to evaluate omissions, insertions, substitutions and timing (separately from spelling and diarization), then decide whether selective retranscription or a distinct model/aligner is warranted.

## Preservation / reproducibility

The owner-provided five sets of logs, JSON, and SRT were evaluated within the conversation; these fresh **benchmark outputs were not added to the repository**. Preserve originals under run-specific names in the private experiment archive if future byte-reproducibility is desired, and record audio-file identity/hash when exporting into the project's source manifest. Avoid copying the owner's local computer paths or runtime environment into public documentation.

This report is an analysis of **machine outputs**. The project already has distinct **listener-verified** E001 findings; do not downgrade or contradict those when using this report.

## Later repository inventory — 2026-10-21

The five `experiments/episode01-*.json` / `.srt` pairs are now present in the
repository. The earlier preservation note above records the state at preparation
time; it is retained as history. The [multi-pass export pilot](MULTIPASS_PILOT_2026-10-21.md)
reuses these exact artifacts, records their hashes, and confirms the two chunked
pairs remain byte-identical. The unrelated `experiments/baseline.*` pair is not
assigned an episode or time window without additional identity evidence.
