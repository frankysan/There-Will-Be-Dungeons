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
6. For Qwen, Q4 with Canary CTC preserved all words and improved E001 SRT structural validity, but altered speaker attribution on ~2.9% of words. Keep a text-level comparison and separate attribution review before adopting Canary.
7. Record the **actual aligner** in run metadata, not just a filename implying "raw" or "native". If Q8 is selected, run Q8+Canary as a distinct test.

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

## D2. Reader-edited spelling layer

Run `python tools/build_reader_editions.py` after `python tools/build_transcripts.py`. This writes `E000.reader-draft.md`/`E001.reader-draft.md` and `*.reader-edits.json`, leaving the source SRT and generated `*.readable-draft.md` unchanged. Only wiki-supported proper names and the written cast label Jon are normalized within timed speaker turns. Every substitution records source time, original/replacement text, rule and wiki citation.

**Not an audio review:** Retain dialogue containing explicit naming or pronunciation uncertainty (e.g. “Orifi or Orify?”) as originally recognized. Do not insert a later-disclosed surname into an early-episode spoken utterance. Treat character-sheet data as final-campaign snapshots, not early episode build statistics. See [external reference policy](EXTERNAL_REFERENCES.md).

Run `python -m unittest discover -s tests -p 'test_reader_editions.py'` after regenerating; keep both builds reproducible.

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

## H. Mandatory ASR experiment documentation

Record **every** ASR/model/precision/segmentation/VAD/diarization/alignment/postprocessing experiment in [model tests](MODEL_TESTS.md) and, for multi-run comparisons, in a dated `reports/` file. Capture the episode/audio identity, time window, model/build/hardware, exact relevant flags and processing stages, runtime, segment and word counts, token-confidence caveats, timestamp anomalies, representative passages, and source-output hashes where useful. Preserve original artifacts with run-specific names; don't overwrite another run or a reader edition.

**Separate evidence classes:** model disagreement, wiki-backed orthography, confidence heuristics and actual audio/listener verification are not interchangeable. Only an audio-grounded reference supports definitive omissions, hallucinations and WER rankings. Record decisions in [DECISIONS.md](DECISIONS.md), outstanding listening tasks in [REVIEW_QUEUE.md](REVIEW_QUEUE.md), and update the backlog. Avoid absolute local paths and private environment details in repository docs.

Example: [five-run Parakeet E001 segmentation evaluation](../reports/PARAKEET_SEGMENTATION_2026-10-21.md).
