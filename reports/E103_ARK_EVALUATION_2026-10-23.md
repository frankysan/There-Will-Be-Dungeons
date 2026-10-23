# Wastes S1E103 — ARK pipeline evaluation (2026-10-23)

**Recommendation: do not generate ARK transcripts for all remaining episodes with this configuration.** The supplied ARK export is substantially shorter than both existing exports, loses consequential passages in the parallel text, assigns every cue to one speaker, and places matching dialogue minutes away from its location in the other two exports. Keep it as experimental evidence. A corrected short pilot would be worthwhile only if diagnosing this pipeline is a priority; this result does not justify archive-wide generation or replacing either existing transcript.

This is a model/pipeline evaluation of **The Wastes, season 1, corrected E103, “When in doubt, burn it”**, a played campaign episode. The introduction says May 10, 2020. Original publisher numbering was not independently checked. This pass does not create an E103 story dossier, advance the story-research queue, or establish canonical dialogue. **Full-export automated measurements and selected parallel-text inspection through the outro were performed; no full-episode manual reading or audio listening was performed.**

## Inputs and reproducibility

Direct local checkout, branch `main`, initial HEAD `df4d2aa221cef55bb3706215d23320d7617a5c62`, with existing uncommitted E102/bonus/reference edits preserved. During evaluation, HEAD advanced independently to `4ba7b92` (`E102`); the three E103 source hashes remained unchanged. Labels below are inferred from filenames, not verified run metadata.

| Export | Exact source | Cues | Normalized words | First start | Last end | Speaker labels | Adjacent overlaps |
| --- | --- | ---: | ---: | --- | --- | ---: | ---: |
| Parakeet processed | [SRT](../sources/The%20Wastes%20S1E103.%20When%20in%20doubt%2C%20burn%20it.parakeet.processed.srt) | 2,639 | 23,243 | 00:00:04.560 | 02:44:12.950 | 8 | 0 |
| Qwen Q8 / Canary CTC / Nemotron | [SRT](../sources/The%20Wastes%20S1E103.%20When%20in%20doubt%2C%20burn%20it.qwen-q8.canary-ctc.nemotron.srt) | 4,551 | 23,672 | 00:00:03.360 | 02:44:12.760 | 8 | 0 |
| ARK Q8 / Canary CTC / Nemotron / FireRed VAD | [SRT](../sources/The%20Wastes%20S1E103.%20When%20in%20doubt%2C%20burn%20it.ark-q8.canary-ctc.nemotron.vad-firered.srt) | 1,526 | 14,738 | 00:00:00.750 | 02:44:14.730 | 1 | 11 |

All three have zero nonpositive cue durations. ARK's only label is **`speaker 2`**, despite the Nemotron filename component. This demonstrates absent speaker differentiation in the delivered export, not a measured diarization error rate. Its overlap pairs involve second cues 12, 15, 187, 189, 190, 221, 232, 256, 259, 284 and 1401; overlapping intervals alone do not prove faulty recognition.

The matching local audio is `local/The Wastes S1E103. When in doubt, burn it.mp3` (158,129,353 bytes; SHA-256 `2ed3f72afcf6e3df3e3e850d8a97dd6706a6db49928488941f4b1022aefe4b0d`). It was hashed, not listened to. Filename/title and corresponding text support the association; the actual input-audio hash for each ASR run is unavailable. Builds, exact model identities beyond the supplied labels, decoding/chunking settings, VAD settings, processing logs, hardware and runtime are unknown. There was no ASR execution in this evaluation.

The ARK export changes both recognition label and VAD label relative to Qwen, while Parakeet is explicitly postprocessed. **The findings apply to this delivered pipeline output; they cannot isolate ARK recognition, FireRed VAD, alignment, diarization, export or postprocessing as the cause.**

Reproduce with `python experiments/ark_e103_2026_10_23.py`. The [script](../experiments/ark_e103_2026_10_23.py) reuses existing parsing, auditing and distance functions. [Machine-readable evidence](ARK_E103_METRICS_2026-10-23.json) retains source hashes, counts, ten-minute token inventories, alignment diagnostics, and selected passages with original cue IDs/times. Original sources are never rewritten. Each source hash is rechecked after measurement.

## Whole-export text comparison

Extract every cue in chronological order through the final cue; strip speaker decoration, join text, lowercase, remove straight/curly apostrophes, replace other non-Unicode-letter/digit characters with spaces, and split into tokens. Compute exact ordered unit-cost word Levenshtein distance. The existing arbitrary-width bit-vector implementation was cross-checked against scalar dynamic programming on 200 seeded short sequence pairs. This measurement has no time buckets or alignment cutoffs.

| Compared exports | Edit distance | Reference denominator | Inter-export disagreement |
| --- | ---: | ---: | ---: |
| Parakeet → Qwen | 2,198 | 23,243 Parakeet words | 9.46% |
| Parakeet → ARK | 10,279 | 23,243 Parakeet words | 44.22% |
| Qwen → ARK | 10,253 | 23,672 Qwen words | 43.31% |

These are **text disagreement rates, not WER, accuracy, verified omission/hallucination counts, or a ranking against spoken ground truth**. The first two rows share a denominator; the last uses Qwen. Word-count differences do not equal deleted-word counts.

ARK has **8,505 fewer normalized words than Parakeet (36.59%)**, and **8,934 fewer than Qwen (37.74%)**. Spelled-out URLs/numbers and compounds affect these counts; they do not explain the missing multi-sentence passages below. The shortfall is distributed: ARK has fewer words in **every one of the 17 recording-clock bins**, including the last partial bin. For example, 00:10–00:20 contains 895 ARK words versus 1,473/1,498, and 01:10–01:20 contains 906 versus 1,606/1,646. Because clocks drift between exports, bins describe output distribution rather than identical speech samples. Reaching the outro does not demonstrate complete speech coverage.

The separate existing time-aware aligner produced 1,805 candidate groups for Parakeet/Qwen, 4,831 for Parakeet/ARK and 4,888 for Qwen/ARK. It required 0, 18 and 21 fallback blocks respectively. **These are review-workload diagnostics, not extra recovered content or quality scores.** ARK's timing drift also undermines same-clock candidate matching; the global distances above do not depend on that matching.

## Consequential text differences

Clocks in the first column belong to Parakeet/Qwen. The ARK column identifies the corresponding text at its own clock rather than assuming synchronization. All observations remain text-only. Source cue IDs and surrounding wording are in the JSON evidence.

| Existing-export clock / cues | Parakeet and Qwen text | Corresponding ARK text | Practical consequence |
| --- | --- | --- | --- |
| 00:03:43–00:05:02; P69 onward / Q98 onward | Bedroom arrival, furnishings, Spatullo/Spatulow entering through smoke, silence and Hope's reaction, then his warning. | Around 00:04:49–00:05:40, repeats the bedroom-arrival wording and jumps to the warning. | Loses scene context and adds repeated text relative to the other exports. Do not treat the repetition as verified spoken repetition. |
| 00:50:59–00:51:15; P814–821 / Q1372–1386 | After the magical babies kill guards, dialogue states that the charges/kills are used up, the baby dissipates, and the babies ascend away. | Around 00:50:59–00:51:06, moves from the attack description directly to more enemies arriving. | Loses a mechanical/state transition, beyond incidental filler. |
| 01:36:31–01:37:11; P1622–1633 / Q2859–2880 | Hope approaches a prone orc, stabs his legs, and explicitly asks for nonlethal attacks. | Around 01:40:33–01:40:46; ARK934–936, jumps from the preceding character's bonus-action discussion directly to attack results. | Loses the actor/target transition and the stated nonlethal intention. |
| 01:40:34; P1690 / Q2987–2988 | Instruction to describe killing the last living enemy in the room. | Same distinctive instruction at **01:44:17**, ARK969–970. | Approximately **3 minutes 43 seconds** of clock discrepancy for identifiable matching text; ARK cues cannot be used as trustworthy listening locators without checking audio. |
| 01:51:56–01:52:34; P1846–1855 / Q3257–3268 | After the blue/white sky crack, a substantial description of unfamiliar storm clouds approaching from the west. | Around 01:54:27–01:54:40; ARK1064–1066, jumps from stepping outside to Jimster's response. | Loses environmental information; this is not explained by a different spelling of a place name. |
| 02:41:29–02:43:01; P2594 onward / Q4472 onward | Large spaceship with attached saucers/two guns emerges from cloak and attacks; reaction and cliffhanger discussion follow. | Around 02:42:31–02:42:43; ARK1511–1513, repeats running to the back of the ship, then goes to the host's next-week promotion. | Retains the earlier saucer warning but loses the specific large-ship reveal, attack and substantial closing conversation. |

## Does ARK add useful independent evidence?

There are alternative readings, but the inspected examples do not establish enough benefit to offset these losses. At the character introduction ARK has **“sterious business”**, Qwen **“mysterious business”**, and Parakeet **“steerious business”**. The existing E102 report records the owner's canonical spelling **Steerious Business**; that written decision does not verify the E103 utterance. ARK provides another hypothesis, while Parakeet already preserves the useful steer reading. ARK's spellings of Tietkalla and other names also vary. Minor differences such as **“You can however hear voices”** versus the clipped Parakeet wording remain possible review clues, not demonstrated recoveries.

The opening date agrees across exports. All three also have the same suspect **Toyota host** rendering, so ARK does not resolve that recognition question. Readable surviving stretches and an ending timestamp close to the other exports do not restore the missing dialogue or speaker differentiation. No audio-verified ARK-only recovery was established; this was selected inspection, not an exhaustive inventory of every possible improvement.

For this archive, retaining interruptions, short replies, rules qualifications and scene transitions matters. This export adds a large amount of conflicting/poorly located text for review while losing information already available in both other outputs. **Keep Parakeet as the readable base and Qwen as the existing independent comparison; retain ARK without promoting it to a routine third pass.** Unknown runtime also prevents a defensible compute-cost/benefit estimate.

## Bounded follow-up if the pipeline is investigated

First inspect the existing ARK run log and intermediate recognition text, VAD regions, alignment and diarization outputs. Determine whether words/speakers were lost before recognition, during generation, or during alignment/export. Compare the same short audio with VAD disabled and enabled, preserving all other settings where supported. Do not infer the cause from the filename or this single output.

A useful repeat pilot would include 00:03:30–00:05:30, 00:50:30–00:51:20, 01:36:20–01:37:20 and 02:41:10–02:42:15 **on a checked original-audio clock**, plus easy agreed controls. Hand-check those audio samples, including overlapping speech and brief replies; measure substitutions, insertions and deletions separately, verify speaker differentiation/timing, and record runtime/settings. Then test another episode before considering broader generation. This is a proposed diagnostic pilot, not an executed job or a requirement to process the remaining archive.

The evaluation changes only its report, reproducible evidence/script, model-test log and a bounded listening-queue entry. Original SRT/MP3 files, reader editions, canonical text and story/reference coverage remain unchanged.
