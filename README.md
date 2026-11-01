# There Will Be Dungeons — campaign transcript and reference archive

Explore the stories, people and worlds of *There Will Be Dungeons*. Choose a campaign for its narrative and setting, or browse the standalone adventures and cast conversations. Each campaign keeps its own continuity.

## Choose how to explore

### Campaigns

| Campaign | Story and setting | Start reading |
| --- | --- | --- |
| **The Wastes** | Nash, Hope, Stanley and Vorel journey from Dusthill through lost civilizations, other planes and distant worlds | [Campaign overview](wastes/README.md) · [Story guide](narrative/README.md) · [World and history](world/README.md) |
| **Delvers** | Three guild adventurers follow small commissions into Atomer's secrets and the danger beneath the city | [Campaign overview](delvers/README.md) · [Three-arc story](delvers/narrative/README.md) · [World and lore](delvers/world/README.md) |
| **Inverse** | A failing waystation draws travelers into a refuge's divisions, a shipwreck and a struggle over its protective barrier | [Campaign overview, adventures and lore](inverse/README.md) |

The Wastes, Delvers and Inverse are separate fictional realities. Similar names, performers or creatures do not establish a shared world. The campaign portals describe each story's recorded ending and unresolved threads.

### One-shots and short adventures

[Browse the one-shot index](oneshots/README.md) for **Merry Chromeness!**, **Spider Claws** and **Send In The Spores**. Their original dossier paths remain available; each entry explains its relationship to the main campaigns. A standalone adventure can use a campaign setting without continuing its main-party story.

The **Dunebreaker** three-part story belongs to the Wastes' earlier history. Follow it from the [Wastes history route](wastes/README.md#earlier-history-and-related-adventures).

### Cast conversations and bonus material

[Browse bonus discussions and retrospectives](bonuses/README.md) for questions about the characters, setting design, abandoned possibilities and the making of the show. These conversations provide context; they do not add performed scenes to the campaigns.

## Sources and project notes

This archive contains source-linked narrative syntheses, world references, episode dossiers and machine transcripts. Story and reference pages can contain spoilers. Source availability, editorial cleanup and transcript agreement are separate from actual listening verification.

### Transcriptions and source status

This repository distinguishes four kinds of text:

- **Original or processed ASR sources:** model/run-specific SRTs and experimental evidence in `sources/` and `reports/`. Retain these rather than silently replacing them when a new model disagrees.
- **Readable machine drafts:** [E000](transcripts/E000.readable-draft.md) and [E001](transcripts/E001.readable-draft.md), with approximate timestamps and diarization.
- **Reader-edited pilot drafts:** [E000](transcripts/E000.reader-draft.md) and [E001](transcripts/E001.reader-draft.md), accompanied by [E000](transcripts/E000.reader-edits.json) and [E001](transcripts/E001.reader-edits.json) change logs. Spelling edits and speaker normalization do **not** certify every word.
- **Source-linked reference dossiers and syntheses:** the current `episodes/`, `world/` and `narrative/` material. Later episodes and the Q&A may **resolve questions** without making the original episode's contemporaneous perspective wrong.

### Run the pilot tooling

The project uses Python scripts and tests. Refer to the full [workflow](project/WORKFLOW.md), [model experiments](project/MODEL_TESTS.md), [multi-pass method](reports/MULTIPASS_PIPELINE.md) and [source audit](reports/SRT_AUDIT.md) before reprocessing files.

```bash
python tools/build_transcripts.py
python tools/build_reader_editions.py
python -m unittest discover -s tests -p 'test_reader_editions.py'
python tools/audit_sources.py
```

These commands rebuild/check the **pilot**, not the entire long-form episode archive. Audio recordings are not bundled in the repository, and unchanged machine output must not be confused with an audio review. For material from the fan wiki or Discord see [external-source policy](project/EXTERNAL_REFERENCES.md), [asset provenance](project/IMAGE_ASSETS.md) and the [spelling report](reports/DISCORD_SPELLING_2026-10-21.md). Images do **not** inherit an automatic distribution license from wiki text.

### Documentation evolution

The [documentation architecture](project/DOCUMENTATION_ARCHITECTURE.md) describes the story, world-reference, evidence and project layers. The [reader-first presentation standard](project/READER_FIRST_PRESENTATION.md) keeps story, world, lore and history ahead of project maintenance across every campaign. Consult the [editorial guide](project/EDITORIAL_GUIDE.md), [world style](project/WORLD_NARRATIVE_STYLE.md), [decisions](project/DECISIONS.md) and [backlog](project/BACKLOG.md) for maintenance. Each campaign portal links its own evidence and progress records.

The root's former campaign-specific research updates and old onward pointers are preserved in the [pre-reorganization reading copy](research/legacy/2026-10-28/reader-index-reorganization/reading/README.md). Earlier versions remain in the [2026-10-21 root snapshot](research/legacy/2026-10-21/ROOT_README.md). These are historical records, not current reading instructions. [Index reorganization checkpoint](project/READER_INDEX_REORGANIZATION_2026-10-28.json).
