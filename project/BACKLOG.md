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

## Illustration style and continuity (2026-10-25)

**Written foundation established:** [working style guide](ILLUSTRATION_GUIDE.md),
[subject template](ILLUSTRATION_SUBJECT_TEMPLATE.md) and a bounded
[Fate 4 introduction-state pilot](ILLUSTRATION_REFERENCES.md#wastes-fate-4).
The owner's comic-book / graphic-novel direction is recorded. A first
[two-pass vehicle trial](../reports/ILLUSTRATION_STYLE_STUDY_2026-10-25.md)
has been generated and visually reviewed by the assistant; its simplified
second pass is the closer candidate. No owner approval, selected production
reference or complete subject-appearance audit is implied.

- [ ] Inspect the two Fate 4 design images directly, extract drawable
  features, and compare the separate floorplan without merging unresolved
  layouts or assuming all sheets depict the introduction-era vehicle.
- [x] Produce and visually review a small style study; record line/shadow
  treatment, palette, accent use, exact prompts and provisional choices.
  Two previews completed, with assistant review in the linked report.
  This tests rendering only; owner style feedback and source-image review
  remain outstanding for those *vehicle studies*. Owner has since confirmed
  the [general adult-animation-inspired graphic direction](ILLUSTRATION_GUIDE.md)
  from [Nash's face explorations](../reports/ILLUSTRATION_NASH_FACE_DIRECTION_2026-10-25.md);
  **style v2** is now the common prompt lock, not approval of any individual
  picture or model sheet.
- [ ] Refine the rendering from feedback, then test a sourced character
  appearance for expression, proportion and consistency. A vehicle study
  alone does not validate those parts of the style.
- [x] Establish a first recurring subject record: the
  [Fate 4 reference](ILLUSTRATION_FATE4_REFERENCE.md) now integrates the
  [source audit](../reports/FATE_4_TRANSCRIPT_AUDIT_2026-10-25.md),
  preserving its [original pilot](ILLUSTRATION_FATE4_PILOT_0_2.md),
  introduction state A01, later changes, and provisional artistic choices.
  This is **not** audio-verified or a completed full-history reference.
- [ ] Complete Fate 4 source-image/era verification; triage remaining
  later-season candidates, then revise the exterior/interior study with
  the dragon-skull front, solar roof, purposeful combat handholds and
  time-accurate roof patch. Obtain explicit selection feedback.
- [ ] Apply the same entity-first method to a recurring character, with
  provenance, time-specific features and anatomy/expression style tests.
- [ ] Implement the [progressive recurring-character sheet skill plan](ILLUSTRATION_PROGRESSIVE_CHARACTER_SHEET_PLAN.md):
  source brief → face → front → side → back → final layout, with per-anchor
  acceptance, saved prompts/reference images, 1024-square sRGB PNG checks,
  and explicit owner approval before reusing a complete model sheet. Pilot
  on Nash E000; two earlier full-sheet render attempts were rejected.
  Four subsequent [Nash face studies](../reports/ILLUSTRATION_NASH_FACE_DIRECTION_2026-10-25.md)
  yielded an owner-preferred style. **Assets now present:**
  [front v1](../illustrations/references/Nash_Maggard_Front_v1.png) is
  **FRONT_APPROVED** for E000/A01 (owner-accepted, 1024-square and sRGB-tagged,
  repository SHA-256 verified); [face study v1](../illustrations/references/Nash_Maggard_Face_v1.png)
  is **not FACE_APPROVED** (1254-square, untagged). A separate
  **1024-square sRGB-tagged face export is now prepared and visually checked**
  ([normalization record](../reports/ILLUSTRATION_NASH_FACE_DIRECTION_2026-10-25.md#normalized-candidate-prepared--2026-10-25)), but must still be
  added to the repository and explicitly approved before side/back views. No complete model sheet yet.

## Documentation consolidation — Arcs One–Two (2026-10-21)

**Phases A–D implemented as structural first editorial passes:** Four-layer [architecture](DOCUMENTATION_ARCHITECTURE.md), [Arc One](../narrative/ARC_ONE.md) and [Arc Two](../narrative/ARC_TWO.md) narratives, [short root README](../README.md), [world portal](../world/README.md) and [archived research indexes](../research/legacy/2026-10-21/README.md). **Character/place consolidation completed for first reference set:** [10 character profiles](../world/CHARACTERS.md), [5 principal location profiles](../world/PLACES.md) and [archived original compendia](../research/legacy/2026-10-21/README.md). **Phase C now implemented:** [Thematic world history](../world/WORLD.md), [unified chronology](../world/CHRONOLOGY.md), and [frozen source research](../research/legacy/2026-10-22/README.md). **Phase D now implemented:** [active open/resolved ledger](../world/CONSISTENCY_LEDGER.md) and [prioritized review queue](REVIEW_QUEUE.md); complete original records preserved in [dated archive](../research/legacy/2026-10-22/README.md). **Next:** actual audio/handout review, expansion of secondary entities and continuing later episodes. Minor-character expansion and source listening remain open editorial work. Track concrete acceptance criteria in [CONSOLIDATION_CHECKLIST.md](CONSOLIDATION_CHECKLIST.md); **this does not imply an audio review**.

## Opening Arc Three coverage — E055–E056 and April 2019 bonus (2026-10-22)

Created provisional [E055](../episodes/E055.md), [E056](../episodes/E056.md), and [April roundtable](../episodes/BONUS-2019-04.md) dossiers, alongside opening [Arc Three narrative](../narrative/ARC_THREE.md) and reference updates. **New in played story:** three months elapsed, government reforms underway, Nash/Angelashi pregnancy, Softhead envoy and mutilation, lethal stone storm, spirit apparitions, Vorel restored from ghost-aging, Emenil attacked at E056 cutoff. **Unresolved:** actual captives released, storm/dragon cause, Emenil's final fate, undead Carnage identity, exact contractor and new place names. Next regular episode is corrected **E057**. All research is **processed-SRT-only pending audio**.

## E057–E060 continuation (2026-10-22)

**Source-first dossiers completed provisionally:** [E057](../episodes/E057.md), [E058](../episodes/E058.md), [E059](../episodes/E059.md), [E060](../episodes/E060.md). [Arc Three narrative](../narrative/ARC_THREE.md), [chronology](../world/CHRONOLOGY.md), [world](../world/WORLD.md), [Razak Val](../world/places/razak-val.md) and new [Diptak](../world/characters/diptak.md), [Orp](../world/characters/orp.md) and [Emenil](../world/characters/emenil.md) profiles updated.

**Current cutoffs:** **Emenil survives E057**; **Nash returns alive E058**; **Diontalus is extracted into Principle's crystal E059 but not proved destroyed**; **named Dusthill captives actually return E059**; **Orp kills Diptak E060 and accepts Vorel's *future* duel**; **private scarless Nash lookalike's “future” claim not authenticated**. **Next:** corrected E061 and targeted listening/handout verification per [review queue](REVIEW_QUEUE.md). Raw processed SRTs and entity seed are not part of this editorial pass.
