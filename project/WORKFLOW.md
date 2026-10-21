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

## I. Experimental multi-pass comparison and targeted verification

Use [the implemented comparison workflow](../reports/MULTIPASS_PIPELINE.md) before
making reconciliation decisions. Run `python tools/pilot_asr.py --out
local/multipass-pilot` from the repository root (one command; new output directory).
It compares full E000/E001 raw Parakeet and Qwen Q8 exports and separately scopes
the five detailed E001 experiments to the opening ten minutes. SRT timing remains
cue-level; model metadata and unknown configuration fields remain explicit.

Inspect `comparison.md` alongside `comparison.json`. Review hypotheses include
possible omissions, conflicting wording, suspicious low-confidence unilateral
text, boundary anomalies and uncertain segmentation. No majority vote or lexical
cleanup changes speech. Candidate IDs link to primary/alternative wording and
the immutable source hashes. `jobs.json` adds context and consolidates nearby
regions, with a 120-second default maximum. Jobs require explicit selection for
execution; comparison does not run ASR.

Record accept/reject/defer decisions, reviewer, date, evidence and audio status in
the separate ledger. Recompare with `--decisions` into a fresh directory; stale
IDs fail visibly. `reconciliation.json` preserves primary text and all candidates;
it is not a publication format. Import targeted third-pass exports as additional
runs with explicit coverage and timestamp origin. Recognition, attribution,
alignment, punctuation and lore spelling remain separate evaluation concerns.

Before adopting this experiment for production, create a manually verified
reference with both flagged passages and agreed controls. Measure deletion,
insertion and substitution rates separately using `asr_reference_metrics.py`.
Capture source identity, configuration, runtime, differences and uncertainties
for every future experiment; see the [pilot evidence](../reports/MULTIPASS_PILOT_2026-10-21.md).

The first real job has now been executed and imported; see the
[29.640-second E001 execution record](../reports/TARGETED_VERIFICATION_2026-10-21.md).
To reproduce comparison of the retained third-pass evidence without ASR, run
`python tools/compare_asr.py experiments/multipass/E001-opening-with-third.json --out local/e001-third-recomparison`
into a fresh directory. The manifest retains the original primary and all six
historical runs. The new clip uses an explicit 74,760 ms timestamp offset;
its recognition output is still awaiting listening review.

## F. Written spelling evidence from Discord (2026-10-21)

For Wastes world dossiers and later name-edit candidates, consult [Discord cast and document spelling register](../reports/DISCORD_SPELLING_2026-10-21.md) and [the spelling ledger](../world/CONSISTENCY_LEDGER.md). Accept **Diontalus** as the archive-owner-approved, creator-authoritative spelling, **not** a verified utterance; maintain `Dion Talus` and other source strings as search aliases. Other direct cast forms are useful to prioritize listening, but do not override unresolved conflicts by frequency. In particular **Tietkalla** is cast-backed but historical `Tiat Cala` mentions require referent matching, and `Catoblepraithe/Catobelpraithe` remains unresolved.

Never apply cross-campaign names from the **Inverse GM outline** or **Delvers guild guide** to Wastes episodes. Distinguish `cast-written`, `creator-document`, `cast-posted handout`, `cast-shared recap`, `archived-link preview`, and `fan inventory` in review records. The report did **not** listen to audio; no rewrite of machine SRT or reader drafts is implied. As for other edits, preserve explicit per-turn provenance and tests for any future generated reader-edition change.

## J. From source dossiers to consolidated references and narrative

After new episode dossiers are indexed, use the [four-layer architecture](DOCUMENTATION_ARCHITECTURE.md). The **episode dossier** captures source timestamps, direct scenes, uncertainty and later corrections; the **world reference** has one current spoiler-scoped entry per entity; the **narrative** uses source-backed story arcs, not an appended list of research updates; and the **decisions/review queue** keeps accepted judgments separate from open listening tasks.

Do **not** keep expanding the root README with each batch; it is now a navigation page. Before a rewrite of `world/CHARACTERS.md`, `PLACES.md`, `WORLD.md`, `CHRONOLOGY.md` or `CONSISTENCY_LEDGER.md`, freeze the previous text into `research/legacy/`, preserve link targets, and follow the [consolidation checklist](CONSOLIDATION_CHECKLIST.md). Source SRTs and E### dossiers must not change merely because a story has been retold. Distinguish **episode-era knowledge**, **post-arc GM commentary**, **possible but unplayed routes**, and **later owner confirmation**.
