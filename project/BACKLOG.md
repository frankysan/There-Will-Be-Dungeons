# Backlog — next pilot milestones

This is a prioritized plan, not a list of completed actions.

1. **Identify/connect GitHub project or repository.** Verify permissions and decide where to store source SRTs, human-readable drafts, review decisions and world records. Do not commit the original MP3s to Git by default.
2. **Listener-verified reference passages.** Create 20–30 minutes of manually checked transcription for E000/E001; include Q4/Q8 disagreements (00:23, 01:51, 02:13), proper nouns, overlaps and music boundaries.
3. **Select ASR recognition model.** Benchmark Parakeet TDT 1.1B, Qwen Q4 and Qwen Q8 against the *same* reference; track omissions separately from WER.
4. **Select aligner separately.** The Q4+Canary test fixed invalid SRT durations, but changed the word-level speaker labels. If Q8 wins, test Q8+Canary.
5. **Validate diarization.** Resolve speaker-ID disagreement regions against audio. Retain per-episode mapping `speaker 5 → Scott` for E001; do not generalize across episodes.
6. **Create reviewed E000/E001 reader editions.** Apply verified corrections only, with an auditable correction log; the existing drafts remain unchanged meanwhile.
7. **Expand world reference with verified spellings and citations.** Preserve conflicting names and speaker/character distinctions until checked.
8. **Build resumable bulk pipeline.** Process the 1,000+ hour archive only after the two-episode milestone meets review acceptance criteria.
