# Wastes S1E103 — Granite pipeline evaluation (2026-10-23)

**Recommendation: do not generate Granite transcripts for every remaining episode yet.** The supplied **Granite Plus Q4 / Canary CTC / Nemotron** export is a more promising candidate than the [ARK export](E103_ARK_EVALUATION_2026-10-23.md): it retains the previously flagged story/mechanical passages, differentiates speakers, and has substantially closer sampled timing. However, it contains malformed annotation text, two zero-duration cues, a long repetitive-output failure, and multi-sentence gaps relative to both existing transcripts. Selected inspection did not establish an audio-verified benefit beyond Parakeet plus Qwen. Retain it as experimental evidence; a repaired, bounded audio-reviewed pilot is justified before considering routine third-pass generation.

Scope is **The Wastes, season 1, corrected E103, “When in doubt, burn it”**, a played campaign episode whose introduction states May 10, 2020. Original publisher numbering was not independently checked. This is a pipeline evaluation, separate from the [E103 story dossier](../episodes/E103.md) and [Parakeet/Qwen story comparison](E103_ASR_COMPARISON_2026-10-23.md). **All three exports were measured through their final cues; qualitative review used selected parallel passages through the outro, not a complete manual episode reading. No audio listening or ASR execution was performed.**

## Inputs and provenance

Direct local checkout on `main`, initial HEAD `8563bdc46fc9cfabf5c1c12f59276e87d8b24f42` (`granite pilot`). Existing uncommitted E103 story/reference edits were preserved. Filename components provide pipeline labels, not verified model versions or execution settings.

| Export | Exact source | Cues | Normalized words | First start | Last end | Speaker-label inventory |
| --- | --- | ---: | ---: | --- | --- | --- |
| Parakeet processed | [SRT](../sources/The%20Wastes%20S1E103.%20When%20in%20doubt%2C%20burn%20it.parakeet.processed.srt) | 2,639 | 23,243 | 00:00:04.560 | 02:44:12.950 | 8 numeric labels |
| Qwen Q8 / Canary CTC / Nemotron | [SRT](../sources/The%20Wastes%20S1E103.%20When%20in%20doubt%2C%20burn%20it.qwen-q8.canary-ctc.nemotron.srt) | 4,551 | 23,672 | 00:00:03.360 | 02:44:12.760 | 8 numeric labels |
| Granite Plus Q4 / Canary CTC / Nemotron | [SRT](../sources/The%20Wastes%20S1E103.%20When%20in%20doubt%2C%20burn%20it.granite-plus-q4.canary-ctc.nemotron.srt) | 3,621 | 22,408 | 00:00:02.400 | 02:43:57.800 | 8 numeric labels plus 73 cues unparsed as speakers |

Granite's SHA-256 is `8d20a9609977674063c1aeb555144ce23613379f46711aa3bfc7fe912d639ee1` (297,105 bytes). The [JSON evidence](GRANITE_E103_METRICS_2026-10-23.json) records all three source hashes, structure counts, ten-minute inventories, selected original cue text/IDs/times and comparison diagnostics. Run `python experiments/granite_e103_2026_10_23.py` using the [reproduction script](../experiments/granite_e103_2026_10_23.py). Hashes are checked again after measurement; no source is rewritten.

The matching local MP3 is `local/The Wastes S1E103. When in doubt, burn it.mp3`, 158,129,353 bytes, SHA-256 `2ed3f72afcf6e3df3e3e850d8a97dd6706a6db49928488941f4b1022aefe4b0d`. It was hashed, not listened to. Matching ID/title and corresponding introductory text support the association; the input-audio hash of each ASR run is unavailable. Exact Granite build/model identity beyond the filename, decoding/chunking flags, postprocessing, hardware, runtime, quantization effects and intermediate outputs are unknown. No VAD component is named in Granite's filename, which does not establish whether VAD was used. The Parakeet export is explicitly processed. Findings apply to this delivered pipeline output; the responsible stage is not established.

## Complete-export measurements

Use the same established report normalization as the ARK evaluation: parse every cue chronologically, strip leading parenthesized speaker decoration, join text, lowercase, delete straight/curly apostrophes, replace non-Unicode-letter/digit characters with spaces and split into tokens. Compute exact ordered unit-cost word Levenshtein distance. The bit-vector implementation is independently checked against scalar dynamic programming on 200 seeded short sequence pairs by this script.

| Comparison | Exact edit distance | Reference denominator | Text disagreement |
| --- | ---: | ---: | ---: |
| Parakeet → Qwen | 2,198 | 23,243 Parakeet words | 9.46% |
| Parakeet → Granite | 4,747 | 23,243 Parakeet words | 20.42% |
| Qwen → Granite | 4,385 | 23,672 Qwen words | 18.52% |

**These are inter-export text differences, not audio WER, accuracy, verified omissions/hallucinations, or a model ranking.** More disagreement can provide useful alternatives or more review noise; it cannot distinguish those outcomes without an audio reference. The standard normalization leaves malformed inline annotations in Granite's text, so the next section also measures their influence.

Granite has **835 fewer normalized words than Parakeet (3.59%)**, and **1,264 fewer than Qwen (5.34%)**, compared with ARK's approximately 37% shortfall. Those totals include annotation contamination and repetitive output. Numeric formatting also differs: Granite uses forms such as `20` and `2020` where another export spells out words, and URLs/compounds split differently. Word-count differences must not be presented as omitted-speech totals. The ten-minute inventories show text throughout the episode; the selected gaps below remain material despite similar total length.

The separate existing time-aware alignment yields 1,805 Parakeet/Qwen candidate groups, 2,535 Parakeet/Granite groups and 2,271 Qwen/Granite groups, with **zero fallback blocks for all three pairs**. This supports more tractable comparison than the ARK output, but is not evidence of accurate speech or correct speaker attribution. No synthetic word timings or cross-model numeric speaker equivalences were used.

## Annotation and structural problems

Granite has **15 adjacent cue overlaps**, compared with zero in both baselines. Overlaps are a structural observation, not automatically an error or evidence of simultaneous speech. More directly actionable problems are:

- **73 inline `Speaker N` markers**, often glued to dialogue, such as `Speaker 1Hello`. These correspond to 73 cues the existing parser labels `Unknown`; eight normally formatted numeric speaker labels are also present. The markers may originate from recognition or a later stage; run metadata is needed to determine that. Having eight labels does not verify their identities or boundaries.
- **58 `T:` marker occurrences across 29 cues**, including `[T: 627]`, unbracketed forms and an incomplete `[T:` fragment. They appear prominently around 00:29:53–00:30:03, 01:14:17–01:14:41 and 01:39:04–01:39:14. The raw source and all IDs remain available.
- **Two zero-duration cues:** 580 at **00:30:01.380** (`T:798] T:798]`) and 2172 at **01:39:14.490** (`T:999] T:999]`). Parakeet and Qwen have zero nonpositive durations.
- **84 successive single-`I` cues** at **02:23:10.500–02:23:39.140**, Granite3175–3258, some with inline speaker markers. At the corresponding point Parakeet and Qwen contain a conversation about three shapes running to the playground and describing their silhouettes. This is an observable repetitive-output failure relative to the parallel text, not an audio-verified hallucination count.

For an **analysis-only sensitivity check**, strip case-sensitive inline `Speaker N` and optional-bracket `T:` markers, including incomplete fragments. Keep all repetitions, lexical variants, numbers and the original files unchanged. The resulting Granite sequence has **22,183 normalized words**:

| Annotation-stripped comparison | Edits | Reference denominator | Text disagreement |
| --- | ---: | ---: | ---: |
| Parakeet → Granite | 4,589 | 23,243 | 19.74% |
| Qwen → Granite | 4,230 | 23,672 | 17.87% |

Removing visible annotation syntax changes the result only modestly. It does not recover missing dialogue, resolve the 84-token repetition, or make the export production-ready. This cleaned sequence is a disclosed analytical variant, not a corrected transcript or a new accuracy measurement.

## Selected consequential passages

Times below are the approximate Parakeet/Qwen recording clocks. Original cue intervals, not word timestamps, are retained in the JSON.

| Passage | Granite observation | Evaluation |
| --- | --- | --- |
| 00:03:43–00:05:02, bedroom arrival | Granite75–95 retains furnishings, Spatulo entering through the smoke, silence, Hope's reaction and the warning; no ARK-like duplicated room-entry sentence in this selected passage. | Preserves context ARK lost; names/wording remain provisional, including `vagrant` for the bedroom reaction. |
| 00:50:59–00:51:15, guardian expiry | Granite978–982 retains three charges/kills, dissipation and the babies ascending away. | Preserves the mechanical transition ARK skipped, already present in both baselines. |
| 00:55:40–00:56:00, two weapons | Granite1113–1115 jumps from the reason for dual wielding to fixing something next week. Parakeet893–899 and Qwen1514–1524 retain the appearance joke, main-hand limitation and observation that no spells were selected. | Loses meaningful table/rules context, beyond punctuation or number formatting. |
| 01:14:17–01:14:43, Sacred Flame | Granite mixes the spell discussion with repeated `[T: 627]` markers. Both baselines retain ordinary dialogue, including the saving-throw outcome. | Useful dialogue is damaged by annotation contamination and absent wording; stripping tags alone does not reconstruct it. |
| 01:24:04–01:24:17, grapple outcome | Granite1828–1829 moves from running in directly to confirming one attack. Parakeet1405–1408 and Qwen2445–2450 describe grappling the orc from behind and forcing him face-down. | Loses the narrated physical outcome while surrounding mechanics survive. |
| 01:36:31–01:37:11, nonlethal intent | Granite2113–2123 retains the approach, leg stabbing and explicit nonlethal qualification. It then jumps to the missed attack, without the first attack-total wording retained by the baselines. | Much more complete than ARK on the key intention; still not verbatim coverage. |
| 01:40:34, distinctive timing anchor | The last-living-enemy instruction appears at **01:40:34** in Granite2193, as in Parakeet1690 and Qwen2987. | No multi-minute ARK-like displacement in this sample. This does not validate every cue. |
| 01:51:56–01:52:34, weather | Granite2418–2427 retains the unusual approaching storm-cloud description. | Preserves environmental context ARK skipped; no unique recovery beyond the pair. |
| 02:23:10–02:23:39, witness exchange | Granite3175–3258 emits the 84 single-`I` cues instead of the coherent witness exchange present in Parakeet2308–2314 / Qwen4017–4030. | Strong reason to inspect the run/intermediate output and include this window in a listening pilot. |
| 02:41:29–02:42:08, cliffhanger | Granite3576–3587 retains the large spaceship, attached saucers/two guns, emergence from cloak and attack, followed by the cliffhanger. Some attack-description wording differs or is absent. | Retains the specific reveal ARK lost. Later closing conversation/promotional wording is less complete than the baselines. |

Granite's outro includes the network credit and final-show remark, but its last end is **15.15 seconds earlier than Parakeet's** and ends with `Speaker 1this`. Since credit text survives, the earlier clock alone does not prove an audio-copy truncation; check final cue placement and run coverage rather than inferring missing audio.

## Complementary value and scale decision

Granite offers genuine alternative hypotheses in the sense of different machine output. Around **01:39:48**, for example, it includes **“it's a freaking hit”** within the excited reaction, while Parakeet and Qwen render shorter/different reactions. That could help a listener recover a brief utterance, or it could be erroneous extra wording. It is **not a demonstrated recovery**. Proper-name variants such as **steirius / mysterious business** do not improve upon the existing owner-confirmed written **Steerious Business** decision, and all three retain the suspect **Toyota host** rendering. Agreement is not a spelling authority.

The positive result is that Granite is substantially less destructive than the supplied ARK output on the checked passages. The missing evidence is whether Granite **correctly resolves mistakes shared by Parakeet and Qwen often enough to pay for generation and review**. This selected text comparison establishes no audio-verified example of that incremental benefit. Runtime is unknown, so compute cost and throughput cannot be assessed. Neither its larger disagreement rate nor its similar word total supplies the missing accuracy evidence.

**Keep Parakeet as the readable base and Qwen as the routine comparison. Do not launch an archive-wide Granite Q4 run on this evidence.** Granite merits a short controlled follow-up more than the current ARK pipeline, but first diagnose the annotation/repetition failures and obtain a small manually verified reference. Any conclusion here is about this Q4-labelled export, not all Granite configurations or precisions.

A bounded pilot should cover **00:55:30–00:56:20**, **01:14:10–01:14:55**, **01:23:50–01:24:50**, **01:39:40–01:40:20** and **02:23:00–02:24:00**, plus easy agreed controls. Check the clocks against original audio. Inspect retained recognition/intermediate outputs to locate whether the tags, repetitive sequence and missing passages originated during generation or later processing. Hand-transcribe the windows, separately measure substitutions/insertions/deletions, count audio-confirmed Granite-only improvements against the existing pair, inspect speaker/timing correctness and record runtime/settings. Verify a second episode before scaling. No rerun or audio review was executed here.

The evaluation adds this report, reproducible script/JSON, a model-log entry and a listening-queue entry. It does not edit source media/SRTs, reader editions or canonical story text, or close existing E103 listening questions.
