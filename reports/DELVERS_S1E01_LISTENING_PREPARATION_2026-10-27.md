# Delvers S1E01 — listening and clock-alignment preparation

**Date:** 2026-10-27. **Issue:** DEL-PREP-002. **Status:** preparation complete; listening and alignment unverified.

The local premiere MP3 matches the raw SHA-256 recorded in the [original comparison](DELVERS_S1E01_ASR_COMPARISON_2026-10-24.md): `ea32c8bc9db10c34e4e181b35105e0afec7a0be2493ed7830750ed3d8dbf1492`. Its size remains 144,634,246 bytes and ffprobe duration is 9,011.291813 seconds. Audio is MP3, stereo, 44.1 kHz; embedded artwork is excluded from clip extraction.

## Prepared search windows

| Clip | Original MP3 search seconds | P/Q SRT excerpt seconds | Purpose |
| --- | --- | --- | --- |
| Opening | 0–70 | 0–70 | Locate shared opening speech before the date question |
| Break | 3,520–3,620 | 3,540–3,600 | Locate the transition around SRT 00:59:25–00:59:42 |
| Outro | 8,920–9,011.291813 | 8,940–9,032 | Compare closing speech/network outro and the end-duration mismatch |

These are independent search windows, not paired timestamps or guaranteed drift bounds. No constant subtraction is inferred from the approximately 19.94-second difference between audio duration and the primary final cue. Expand a search window only if a matching anchor is absent. Cue intervals are not word timings.

The [local review page](../local/episode-analysis/delvers-S1E01-alignment-2026-10-27/review.html) provides three audio players and expandable P/Q cue tables. The page, mono 16 kHz PCM WAV clips and cue JSON stay under ignored `local/`; they are available in this checkout and are not published artifacts. Clip time plus its documented source start gives the original MP3 seek time, not the SRT time. The [checkpoint](../project/DELVERS_S1E01_LISTENING_PREPARATION_2026-10-27.json) retains exact extraction commands, media hashes, actual clip durations and source states.

## Listening completion rule

Listen to and identify matching speech at the opening, break and outro. For each anchor record original MP3 time, export/cue ID and SRT interval, exact observed wording, reviewer/date and uncertainty. Record changing offsets or discontinuities rather than forcing a constant mapping. Multiple independent anchors are needed before translating other issue windows.

DEL-PREP-002 remains open. DEL-PREP-001 (spoken year), DEL-PREP-003 (names) and DEL-S1E01-001 (healing/negation) are queued after suitable clock mapping; none is resolved by this preparation. The original MP3 duration mismatch remains an observation, not proof of missing speech. No ASR run, full-record audio review, speaker verification or canonical transcript edit occurred.

## Preservation and validation

[Exact pre-edit records](../research/legacy/2026-10-27/delvers-s1e01-listening-preparation/README.md) preserve the shared queue and cleanup manifest. Narratives, world pages, original SRTs/audio and earlier fingerprint results remain unchanged. Validation checks clip format/duration/hashes, cue provenance, local links, protected bytes, targeted Markdownlint and whitespace; results are persisted in the checkpoint. No whole-repository audit is claimed.
