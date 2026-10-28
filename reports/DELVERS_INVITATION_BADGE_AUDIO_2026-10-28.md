# Delvers — invitation and badge local audio-review packets

**Date:** 2026-10-28. **Episodes:** S3E12 and S3E09. **Issues:** DEL-S3E12-006 and DEL-S3E10-002. **Outcome:** two prepared review packets and 16 machine-only timing candidates; no listening confirmation, fictional resolution or calibrated clock mapping.

## Prepared review

The [local review page](../local/episode-analysis/delvers-invitation-badge-audio-2026-10-28/review.html) contains two audio players, original-MP3 time instructions, collapsible paired SRT excerpts/candidate hints and listener-observation fields with JSON download. Notes are not saved automatically. Clips, raw recognizer outputs, receipts, commands and logs remain ignored/local. The page requires the local checkout; these audio assets are not published.

| Packet | Fingerprinted local audio duration | Selected original-MP3 window | Pending listening question |
| --- | --- | --- | --- |
| S3E12 invitation | 10,152.724813 s | 9,950–10,030 s (80 s) | What groom name and initials are audibly spoken? Does the passage explicitly identify the Traveler? Keep spoken form distinct from authoritative written spelling |
| S3E09 badge | 10,508.486438 s | 10,120–10,200 s (80 s) | What exactly is handed back, and to whom? Preserve an unspecified badge or recipient when the line does not establish one |

Durations and SHA-256 fingerprints identify these local copies, not the original files supplied to the historical recognizers. The archived SRT search ranges were used to choose bounded MP3 search clips; this does **not** presume those clocks are calibrated. Candidate matches occur inside both clips, but a listener must confirm audible correspondences before translating target seeks. Do not extend one local candidate or the premiere's offsets to an entire episode or another copy.

## Machine anchor candidates

Both bounded jobs completed using the installed CrispASR **0.8.43 eb633d90** and `parakeet-tdt-1.1b.gguf` through the existing `tools/run_asr_job.py`. Explicit English and Vulkan were requested; no explicit VAD, chunking, diarization or auxiliary alignment was applied. No software or model was installed. Native JSON `offsets.from/to` are word milliseconds relative to the extracted mono 16 kHz PCM clip, then translated by adding that clip's original-MP3 start. These remain model timing estimates; SRT cue intervals are not word timings.

Exact ordered six-to-eight-token matching blocks against each prepared export yield at most four distributed, unique-within-window phrases per export: **16 candidates total**. Target groom-name/initials and badge tokens were excluded from anchor selection, so disputed words do not serve as timing authority. The recognizer belongs to the existing Parakeet family and is not independent ground truth. No full-export disagreement, WER, accuracy or model ranking is calculated.

Examples below are normalized machine phrases, not listener-verified quotations. The [checkpoint](../project/DELVERS_INVITATION_BADGE_AUDIO_2026-10-28.json) records all candidates, word/token indices, raw-output hashes, source cue provenance, coarse first-word difference intervals and per-run settings/timing.

| Episode / export | Candidate phrase | Model-estimated original MP3 seconds | Archived cues / SRT seconds |
| --- | --- | --- | --- |
| S3E12 / P | many other monstrous and bizarre employees that have | 9956.240–9959.520 | 2333–2334 / 9954.709–9961.470 |
| S3E12 / Q | all working the farm well and many other | 9954.720–9956.880 | 3892–3893 / 9951.834–9958.040 |
| S3E09 / P | going you're going to get to the guild | 10127.760–10128.960 | 2576–2577 / 10126.201–10129.995 |
| S3E09 / Q | that's way in the open i got a | 10138.480–10140.960 | 4365–4366 / 10138.560–10141.280 |

## Required listening gate

Listen before expanding the ASR hints where possible. For matching anchors and target wording, record **reviewer/date, original MP3 time, export/cue, observed words, alternatives/interruptions, uncertainty and confidence**. Add the displayed clip start to the player's relative time. The downloadable notes explicitly remain unassessed until the reviewer documents confirmation. No observations have been entered by this preparation pass.

If the target is outside its clip or a matching phrase cannot be confirmed, record that outcome and expand only the affected local window. More recognizer agreement cannot substitute for listening or supply a missing identity, handoff, wedding or rescue roster. A written invitation or explicit creator statement would be a separate evidence source if actually located. **Both existing issue keys remain open.**

## Preservation and validation

[Exact pre-edit tracking records](../research/legacy/2026-10-28/delvers-invitation-badge-audio/README.md) preserve the queue, cleanup manifest and model-test log. World, narrative, episode dossiers, original MP3/SRT and prior research remain unchanged. Validation checks audio/SRT file states, raw run receipts, exact candidate provenance/uniqueness, local player assets, ignored output paths, protected hashes, guarded edits, links and scoped whitespace. Targeted Markdownlint and its baseline limitations are checkpointed after execution. No whole-repository audit is claimed.

The four-file targeted Markdownlint run reproduces 40 existing violations in the shared model-test log, independently matched to its archived original, with zero new violations. The report, queue and cleanup-manifest changes introduce none; the archive README passes separately.
