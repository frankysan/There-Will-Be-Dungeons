# Backlog — next pilot milestones

This is a prioritized plan, not a list of completed actions.

**Implemented experiment (2026-10-21):** [multi-pass export comparison, review
ledger, targeted job generation and provisional reconciliation](../reports/MULTIPASS_PIPELINE.md).
The [E000/E001 export pilot](../reports/MULTIPASS_PILOT_2026-10-21.md) and the
[first real bounded third pass](../reports/TARGETED_VERIFICATION_2026-10-21.md)
are complete. Original E000/E001 audio hashes now match the manifest. The current
priority is the listening reference in item 2 and independent
deletion/insertion/substitution measures. Include
agreed passages as controls to detect omissions missed by all recognition runs.

Maintenance follow-up: existing `validate_pilot.py` / legacy rebuild helpers use
short `E000.*`/`E001.*` source filenames absent after the full-title filename
migration. Repair source resolution without changing retained transcript text.
The new comparison manifests already reference the current full filenames.

1. **GitHub canonical home established.** Repository `frankysan/There-Will-Be-Dungeons-Transcripts` is connected. Review [external reference and chronology policy](EXTERNAL_REFERENCES.md) and keep original MP3s outside Git by default. Decide how to manage provenance, licensing and spoiler-sensitive references before scaling.
2. **Listener-verified reference passages.** Create 20–30 minutes of manually checked transcription for E000/E001; include Q4/Q8 disagreements (00:23, 01:51, 02:13), proper nouns, overlaps and music boundaries.
3. **Select ASR recognition model.** Benchmark Parakeet TDT 1.1B, Qwen Q4 and Qwen Q8 against the *same* reference; track omissions separately from WER.
4. **Select aligner separately.** The Q4+Canary test fixed invalid SRT durations, but changed the word-level speaker labels. If Q8 wins, test Q8+Canary.
5. **Validate diarization.** Resolve speaker-ID disagreement regions against audio. Retain per-episode mapping `speaker 5 → Scott` for E001; do not generalize across episodes.
6. **Create reviewed E000/E001 reader editions.** Apply verified corrections only, with an auditable correction log; the existing drafts remain unchanged meanwhile.
7. **Expand world reference with verified spellings and citations.** Preserve conflicting names and speaker/character distinctions until checked.
8. **Build resumable bulk pipeline.** Process the 1,000+ hour archive only after the two-episode milestone meets review acceptance criteria.

9. **Source-supported name normalization.** Compare externally documented spellings (Dusthill, Oriphi Akmenos, Vorel Rasvim Kurik, Nash Maggard, Jimster, Shun'ti Stoutbarrel) with the pilot's audio and entity index. Keep ASR aliases and label wiki-only support separately from listener confirmation.
10. **Character sheet snapshots.** Record exact linked D&D Beyond URLs and observation dates; treat these as campaign-end states, with no reconstructed opening-level stats.

11. **Ground Parakeet segmentation choices in audio.** Use the [five-run E001 benchmark](../reports/PARAKEET_SEGMENTATION_2026-10-21.md) to verify the opening greeting, 01:23–01:42 banter, 02:17–03:08 interjections, 04:13–04:37 reactions and 04:45–08:45 Dusthill narration. Compare omissions, invented speech and timestamp stitching to a manually checked reference; turning LCS dedup off was a no-op on these outputs.

12. **Validate two-job CrispASR concurrency.** [Initial observation](../reports/ASR_CONCURRENCY_2026-10-21.md): two instances complete episodes in roughly 6–7 minutes each with very low disk traffic and GPU activity, despite near-max system RAM. Measure sequential versus concurrent total wall-clock throughput on the **same inputs**; collect available/committed RAM and hard page-read metrics before settling on a default queue concurrency. Later test a mixed Parakeet/Qwen pair separately.

## Documentation consolidation — Year One (2026-10-21)

**Phases A–B implemented as first editorial passes:** Four-layer [architecture](DOCUMENTATION_ARCHITECTURE.md), [Year One narrative](../narrative/YEAR_ONE.md), [short root README](../README.md), [world portal](../world/README.md) and [archived research indexes](../research/legacy/2026-10-21/README.md). **Character/place consolidation completed for first reference set:** [10 character profiles](../world/CHARACTERS.md), [5 principal location profiles](../world/PLACES.md) and [archived original compendia](../research/legacy/2026-10-21/README.md). **Next:** world-theme and unified chronology consolidation (Phase C), then active/resolved consistency-ledger cleanup (Phase D). Minor-character expansion and source listening remain open editorial work. Track concrete acceptance criteria in [CONSOLIDATION_CHECKLIST.md](CONSOLIDATION_CHECKLIST.md); **this does not imply an audio review**.
