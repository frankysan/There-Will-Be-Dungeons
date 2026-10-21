# Project charter

## Goal

Create **human-readable, accurate, searchable transcripts for every episode** of a primarily English podcast archive exceeding 1,000 hours. Preserve audio and timecode provenance. Build a parallel, sourced reference collection about the fictional world, people, places, organizations, artifacts, and events so that later transcripts and reference entries can be reconciled consistently.

## First milestone: E000 and E001

- Establish a deterministic procedure from selected SRT source to readable paragraphs and episode/time references.
- Preserve all provided recognition variants and original source MP3s outside the lightweight deliverable.
- Establish source-to-draft-to-reviewed lifecycle; identify known errors and open questions.
- Seed, rather than exhaustively finish, a **campaign/world reference** from the introductions and first actual-play episode.
- Verify by listening to targeted discrepancies before deciding whether Parakeet or Qwen is the final ASR engine.

## Success criteria

### Transcription

- Every recorded spoken passage is represented, including informal exchanges relevant to the episode.
- Speakers are represented by real people where identified; a participant using a character voice does not imply a new human participant.
- Names and terms are consistent with a sourced spelling registry.
- Paragraphs are readable, indexed by approximate timestamps, and easily matched to their original audio and SRT cue ranges.
- Uncertainty is explicitly documented; no fabricated missing dialogue or silent rewriting.

### Reference documentation

- Each claim cites the relevant episode and approximate time.
- Distinguish game-master exposition, character backstory/belief, in-session events, and assistant inference.
- Track uncertain spelling and apparent contradictions; do not silently resolve them.
- Separate out-of-world people/roles from in-world characters and their dramatic voices.

## Out of scope for this milestone

- Automatic proof of word-for-word correctness across the full 3-hour episode.
- A complete encyclopedia of the setting.
- Paid cloud transcription, indexing service, or custom user interface.
- Correcting retroactively based on future episodes without a source citation and change record.

## Scale strategy

Pilot on two episodes → assess accuracy and correction workload → refine formatting/validation → batch process remaining episodes → maintain living lore and spelling references. Any later automation should re-run without changing manually reviewed text unexpectedly.
