# Delvers S1E01 — automated audio-clock anchor pilot

**Date:** 2026-10-27. **Scope:** three local MP3 windows; machine-generated timing candidates only. No listening verification or story correction.

## Result

Selected unique phrase matches occur near the original SRT clock at opening, break and closing speech. They do **not support subtracting the approximately 19.94-second final-duration difference globally**. Model timing and cue intervals are estimates; the samples do not establish a full-recording mapping. DEL-PREP-002 remains open.

| Window / export | Matched phrase | Model-estimated original MP3 seconds | Archived SRT cue(s) / interval seconds |
| --- | --- | --- | --- |
| opening / P | listeners and viewers and welcome back to there | 9.680–11.520 | 1–2 / 9.120–13.896 |
| opening / Q | greetings listeners and viewers and welcome back to | 9.040–11.280 | 1–2 / 9.120–12.720 |
| break / P | take care of y'all good luck out there | 3535.440–3538.000 | 918–918 / 3535.461–3542.237 |
| break / Q | hands you your guide as soon as he | 3540.560–3542.000 | 1490–1491 / 3540.260–3542.180 |
| outro / P | you next time on there will be dungeons | 9005.200–9007.920 | 2332–2333 / 9003.621–9026.180 |
| outro / Q | you next time on there will be dungeons | 9005.200–9007.920 | 3920–3921 / 9005.270–9007.810 |

The [checkpoint](../project/DELVERS_S1E01_ANCHOR_PILOT_2026-10-27.json) retains all 24 candidate phrases, original cue IDs, model word offsets, coarse first-word offset intervals, exact input paths and raw-output hashes. Candidate uniqueness is checked only within the selected search windows.

## Tail boundary

The local MP3 ends at **9,011.291813 seconds**. Archived P cue 2333 spans **9,017.060–9,026.180**, and P cue 2334 ends at **9,031.230**. Q network-credit cues 3922–3925 occupy **9,023.970–9,030.930**. These network-credit cue intervals extend beyond the local audio duration. The fresh outro recognizer ends with the show sign-off and does not return the network credits. This suggests a copy/tail or cue-timing mismatch for targeted review; it does not prove that the original recognizers invented speech or that this MP3 is missing it. A new run from the same family is not listening evidence.

## Method and provenance

Used the existing `tools/run_asr_job.py` with local CrispASR 0.8.43 eb633d90 and the installed `parakeet-tdt-1.1b.gguf`. Explicit English and requested Vulkan; no explicit VAD, chunking, diarization or auxiliary alignment. Native word timing uses documented JSON `offsets.from/to` milliseconds; no `t0/t1` unit inference. Original MP3 hash is the [preparation packet](DELVERS_S1E01_LISTENING_PREPARATION_2026-10-27.md) identity. Clips cover original audio 0–70, 3,520–3,620 and 8,920–9,011.291 seconds. Raw JSON/SRT, logs, commands and receipts remain ignored/local.

Normalized lexical tokens with the existing evidence helper; used ordered exact matching blocks of at least six words between fresh recognition and each prepared SRT excerpt. Kept unique six-to-eight-word phrases from distributed positions, at most four per export/window. The archived SRT retains cue-level timing; fresh word offsets remain model estimates. First-word offset intervals are coarse candidate ranges, not a calibrated correction. No full-episode ASR disagreement, WER, accuracy score or recognizer ranking was computed.

The opening job completed recognition but its import failed because job audio metadata lacked `id`; its raw outputs and original receipt are preserved. Adding the metadata allowed validated import without rerunning recognition. Break/outro jobs completed normally. No software or model was installed.

## Next review and limits

Listen to candidate opening, break and closing anchors in the [local review page](../local/episode-analysis/delvers-S1E01-alignment-2026-10-27/review.html); record observed MP3 time, export/cue, wording, reviewer/date and confidence. Inspect the final local audio and the archived network-credit tail. Do not apply a global correction or mark date/name/negation questions resolved. If the client cannot expose audio to a reviewer, retain the candidates as unverified.

## Preservation and validation

[Exact pre-edit records](../research/legacy/2026-10-27/delvers-s1e01-anchor-pilot/README.md) preserve the queue, cleanup manifest and model-test log. Prior preparation/checkpoints, original audio/SRTs and narrative/world prose are not rewritten. Validation checks source states, raw outputs, candidate phrase provenance, archive/protected hashes, new links, targeted Markdownlint and scoped whitespace. No whole-repository audit is claimed.

The targeted four-file Markdownlint run retains 40 independently reproduced baseline violations in the shared model-test log, with zero new violations. The new report, queue and cleanup-manifest changes introduce none; archive README lint passes separately.
