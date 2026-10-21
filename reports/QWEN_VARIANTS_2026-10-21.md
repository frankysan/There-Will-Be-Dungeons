# Qwen ASR quantization and alignment pilot — 2026-10-21

**Input:** Six new *unprocessed* Subtitle Edit SRT exports for E000 and E001, supplied after the first pilot. The files are preserved byte-for-byte under `sources/`. The exact run configurations beyond filenames have **not** been independently confirmed; in particular, a filename without `canary-ctc` must **not** be interpreted as proof that native/no alignment was used.

**Critical distinction:** Counts here measure tokenized transcribed words, not verified speech accuracy. Word-level Levenshtein distance measures disagreement, **not WER**. Subtitle boundary problems do not automatically reflect ASR recognition quality.

## Results

| Episode / output | Subtitle cues | Normalized words | Nonpositive durations | Adjacent overlaps |
|---|---:|---:|---:|---:|
| E000 Q4 (without Canary) | 239 | 1,623 | 0 | 0 |
| E000 Q4 + Canary CTC | 239 | 1,623 | 0 | 0 |
| E000 Q8 (raw) | 244 | 1,623 | 0 | 1 |
| E001 Q4 (without Canary) | 5,497 | 32,007 | 56 | 19 |
| E001 Q4 + Canary CTC | 5,472 | 32,007 | 0 | 1 |
| E001 Q8 (raw) | 5,851 | 32,244 | 64 | 16 |

Tokenization: lowercase ASCII letters/digits with apostrophes inside words, excluding `(speaker N)` labels. `tools/evaluate_qwen_variants.py` reproduces counts and token edit distances (requires `rapidfuzz`). The existing `tools/audit_sources.py` uses whitespace word counts, which may differ slightly; label the method when comparing reports.

### Q4 versus Q4 + Canary CTC

- **Exactly identical concatenated text** for both E000 and E001, including punctuation, after joining cue texts with spaces. This is stronger than matching normalized word counts.
- E000 contains exactly the same 239 subtitle texts and numeric speaker assignments, cue by cue. Its timing changes modestly: median absolute boundary shift approximately 80 ms for starts and ends; at least one end boundary shifts by 2 seconds.
- E001's cue count changes from 5,497 to 5,472 while preserving full concatenated text. The 56 nonpositive durations disappear, and adjacent cue overlaps drop from 19 to 1.
- **However, 924/32,007 individual E001 word positions (2.89%) receive a different speaker ID** after the resegmentation. This is speaker-attribution *disagreement*, not a verified diarization error rate. Some assignments to or from speaker 5 also change. E000's word-level speaker sequence remains unchanged.
- These results favor testing Canary CTC for Qwen timestamp structure, but they do **not** establish its timing accuracy against audio or its superiority for speaker labeling. Retain separate ASR, alignment and diarization assessments.

### Q4 versus Q8 recognition

| Episode | Levenshtein token edits | Normalized by longer sequence | Breakdown |
|---|---:|---:|---|
| E000 | 17 | 1.05% | 11 replacements; 3 insertions; 3 deletions |
| E001 | 1,070 | 3.32% | 383 replacements; 462 insertions; 225 deletions |

- E000 includes different proper-noun spellings, such as `Nash Magard` (Q4) versus `Nash Maggard` (Q8); independently verify the intended spelling before changing the character reference. Other fantasy location/name spellings differ too.
- E001 includes longer divergences, sometimes involving speech present in Q8 but not Q4 (or vice versa). Examples to review against audio:
  - **E001 00:23:21:** Q8 includes additional interjections (`I think so`, `is there music in the background`) absent in Q4.
  - **E001 01:51:13:** Q8 includes a brief Scottish-accent discussion absent in Q4; it also differs on `the water's broken` versus Q4's `the ... is broken`.
  - **E001 02:13:40:** Q8 includes extra words (`voodoo and the steeple and the antenna`) before a sentence both models share. These extra words **must not be presumed correct** without listening.
  - **E001 01:15:17:** Q8 retains substantially more repeated conversational words than Q4. Those repetitions could be faithful disfluencies or recognition artifacts.
- Q8 supplies **237 more normalized tokens** than Q4 for E001; higher word count is not inherently greater accuracy or completeness.

## Recommendation and controls

1. **Retain Parakeet TDT 1.1B as the provisional primary** until an audio-verified Qwen/Parakeet comparison shows a clear benefit to changing it.
2. **Use Qwen Q8 as the initial accuracy challenger**, with Q4 now a serious efficiency candidate. A quality-focused comparison should test Q4 and Q8 on a listener-verified excerpt before ruling either out.
3. **Favor Q4 + Canary for an alignment pilot** because of dramatically cleaner structural timestamps. Do not infer that it improves speaker identification. If Q8 wins recognition tests, test **Q8 + Canary** explicitly before adopting a final pairing; that variant is not part of these six files.
4. Save unprocessed exports plus exact engine versions, quantization, aligner, diarizer, language, VAD, post-processing switches and wall-clock times. The filenames alone do not capture full configurations.
5. Do not update canonical character/place spelling from ASR agreement alone. Enter disputed names in `world/CONSISTENCY_LEDGER.md` and verify against audio or independent campaign materials.

## GitHub integration status

The archive owner reports creating a GitHub project. The connected GitHub repository search did **not** expose a repository matching `The Wastes`, `Dungeons` or `transcription` when this report was prepared. **No files were pushed to GitHub.** This report and the six new raw SRTs are bundled locally and ready to import; connect or identify the repository/Project before synchronizing.
