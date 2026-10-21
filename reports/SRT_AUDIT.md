# SRT source audit

**Scope:** Structural properties of the supplied SRT files. This is **not** a word-accuracy or speaker-correctness measurement. Overlaps may legitimately result from simultaneous speakers; invalid durations should be reviewed. The original MP3 files are excluded from the ZIP but are hashed in `source_manifest.json`.

| Source SRT | Cues | Words | Invalid (end ≤ start) | Overlap pairs | First cue | Last cue end |
|---|---:|---:|---:|---:|---|---|
| E000.cohere.processed.srt | 187 | 1,616 | 1 | 0 | 00:00:00 | 00:13:11 |
| E000.parakeet.processed.srt | 193 | 1,625 | 0 | 0 | 00:00:00 | 00:13:28 |
| E000.parakeet.raw.srt | 184 | 1,606 | 0 | 1 | 00:00:00 | 00:13:11 |
| E000.qwen-f16.processed.srt | 189 | 1,614 | 0 | 0 | 00:00:00 | 00:13:10 |
| E000.qwen-q8.processed.srt | 189 | 1,616 | 0 | 0 | 00:00:00 | 00:13:10 |
| E001.cohere.processed.srt | 4,918 | 30,522 | 35 | 42 | 00:00:12 | 03:03:33 |
| E001.parakeet.processed.srt | 4,819 | 32,721 | 0 | 1 | 00:00:11 | 03:03:33 |
| E001.parakeet.raw.srt | 3,911 | 31,205 | 0 | 16 | 00:00:05 | 03:03:33 |
| E001.qwen-q8.processed.srt | 5,040 | 32,167 | 2 | 19 | 00:00:11 | 03:03:33 |

## Known interpretation

- All `.processed.srt` sources were provided after Subtitle Edit post-processing and automatic speaker name find/replace in some files; they are **not raw recognition outputs**.
- Parakeet `.raw.srt` sources were supplied from a later run with post-processing disabled. Therefore differences between raw and processed files may include inference/run differences.
- Valid subtitle timing does **not** imply words are aligned correctly: the E000 processed final word is visibly placed much later than in the raw file.
- An ASR engine that skips speech may have perfectly valid cue structure. Cohere's verified E001 omissions are a **coverage** issue, not merely an SRT structural error.

## Next testing milestone

Verify against audio a hand-transcribed 20–30-minute sample that includes proper nouns, rapid dialogue, quieter speech and the two known Cohere omissions. Measure WER, omissions and speaker attribution separately for Parakeet and Qwen Q8.
