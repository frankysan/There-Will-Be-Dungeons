# Transcription workflow (v0 pilot)

## A. Ingest and preserve

1. Keep original MP3s intact; record path, duration, file size, SHA-256, title and episode ID.
2. Keep machine SRTs **by engine, model, precision, aligner, diarizer and post-processing status**, never under a generic `transcript.srt` overwrite target.
3. Work in a disposable processing directory; copy approved exports into the archive only after source identity is checked.

## B. Recognition and model choice

1. Use **Parakeet TDT 1.1B** as the provisional primary ASR candidate, with **Nemotron-3-Diarization**, because it is fast and has captured important dialogue.
2. Use **Qwen3-ASR 1.7B Q8** as a second opinion on selected difficult passages; it was reported to take roughly **2–3×** Parakeet/Cohere processing time. F16 reportedly took **7–8×** and has low priority until it shows measurable accuracy improvements.
3. Do **not** select Cohere for archival production without fixing its confirmed tendency to skip substantial speech. Retain it as historical test data.
4. Preserve both pre- and post-Subtitle Edit outputs when possible; the provided examples show text and cue changes between different runs.
5. Evaluate recognition, diarization, alignment, and punctuation/cleanup **independently**. Same diarizer across ASR engines is not independent evidence of correctness.

## C. Normalize speakers

1. Map numeric IDs by **episode**, never globally. See `tools/build_transcripts.py`.
2. Map Episode 1 speaker 5 to Scott (acting voice), based on listener confirmation. Do not erase the raw label from original sources.
3. Speaker = **performer/participant** in transcripts. World/reference entries may separately indicate the in-world character or narrator role.
4. Flag unconfirmed splits and overlap, rather than guessing the speaker.

## D. Render for reading

1. Input: selected processed SRT, currently Parakeet. Keep its words/punctuation unchanged.
2. Join subtitle lines, group contiguous cues from the same participant into a paragraph; prefer boundaries after sentence punctuation.
3. Prefix each paragraph with speaker and start time. Use ten-minute headings for navigation.
4. Keep an accompanying JSON file with cue start/end and cue IDs for automated verification and future correction tools.
5. Do not use a generic LLM to insert unverified dialogue, adjust history, or invent endings. Any separate editorial rewrite should be labelled and retain the machine draft.

## E. Quality control

### Automated checks

- Cue parsing, timestamps, nonpositive durations, overlaps, unknown speakers, word coverage, and source hashes.
- Speech-like regions not represented by text are *review candidates* (music/sound effects can cause false positives).
- Highlight model disagreements, highly repeated words, long gaps inside apparent conversation, text near music, and unusual proper nouns.

### Listening review

- Confirm episodes begin/end on speech boundaries.
- Sample at least several minutes from easy and difficult regions before scaling.
- Check all known missing-speech incidents (Episode 1 around 00:47 and 01:55), character voices, and ambiguous names.
- Use verified examples as regression tests for later engine/settings changes.

## F. Editorial review and publication

- Apply the [editorial guide](EDITORIAL_GUIDE.md).
- Record each meaningful correction in a review log: episode, time/cues, old/new form, evidence, reviewer, date.
- Write lore facts only after checking the matching passage; note whether a speaker is the DM, a character, or a player discussing rules.
- Expose status distinctly: `asr`, `readable-draft`, `review-in-progress`, `reviewed`, `published`.

## G. Later batch processing

- Add a checkpointed processing script and resumable per-episode manifest.
- Retry errors without overwriting good output; limit GPU concurrency based on measured throughput/VRAM.
- Run targeted second ASR only where human review or automated disagreement detection indicates value.
- Index reviewed text and lore in a search database after editorial conventions stabilize.
