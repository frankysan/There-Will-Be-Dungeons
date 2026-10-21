# Roadmap and open work

## Milestone 1 — two-episode pilot

- [x] Preserve all supplied SRT variants under unambiguous names.
- [x] Produce E000/E001 speaker-labelled, human-readable **drafts** with timestamps.
- [x] Apply listener-confirmed `speaker 5` → Scott mapping **only in E001's presentation layer**.
- [x] Create project decisions, workflow, editorial policy, review queue, initial world dossiers and source manifests.
- [x] Add reproducible renderer and mechanical regression checks for completeness and links.
- [ ] Listen and correct both drafts to achieve **reviewed** status (not yet done).
- [ ] Resolve important name spellings and spoken-word timing at the E000 end.
- [ ] Measure real transcription accuracy (WER and coverage) on verified samples from these two recordings.

## Milestone 2 — quality and maintainability

- [ ] Define a sampled reference set of 20–30 minutes, across both episodes and including known failures.
- [ ] Compare Parakeet versus Qwen Q8 against manually checked audio; measure WER, omissions and diarization mistakes separately.
- [ ] Build a correction overlay that is **not overwritten** by automatic transcript regeneration.
- [ ] Add episode-specific pronunciation/name lexicon; note confirmed spellings and aliases.
- [ ] Add selective second-pass transcription for suspected dropped speech.
- [ ] Develop validators for speech/music boundaries, repetition artifacts and overlap.

## Milestone 3 — whole archive

- [ ] Inventorize episodes, durations, audio properties and source provenance.
- [ ] Build resumable batch processing with per-episode manifest/state and GPU resource limits.
- [ ] Process all episodes to `readable-draft`; independently track editorial `reviewed` status.
- [ ] Link transcripts to world-reference entries, including character aliases and evolving plot facts.
- [ ] Add full-text search for transcripts and lore (SQLite FTS5 is a potential fit).
- [ ] Establish source and output backup/restore checks.

## Milestone 4 — ongoing consistency

- [ ] Establish 'first mention' and 'latest clarification' for each named entity across episodes.
- [ ] Annotate retcons, mistaken in-world claims and contradictory scenes rather than silently replacing the historical record.
- [ ] Maintain episode summaries, plot threads, entities, relationships and timeline, with provenance for each claim.
- [ ] Add focused editorial search prompts to find inconsistent spellings and suspect character attribution across the archive.

These phases are **plans**, not commitments that accuracy work or the full archive have already been completed.
