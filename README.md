# There Will Be Dungeons — The Wastes archive

**A local-first transcription and campaign-reference project.** The long-term goal is an accurate, searchable, source-linked archive of *The Wastes*, beginning with the first campaign arc and its cast/GM discussions.

**Current research coverage:** corrected **E000–E054**, including the intentionally intermediate **E013.5**, a separate **E043 holiday one-shot**, and the **March 2019 Year One Q&A** bonus. These episode dossiers are **provisional notes from processed Parakeet SRTs, not finished or listener-proofread transcripts**. The ongoing E000/E001 speaker-labelled reader-edition pilot remains separate.

## Choose how to explore

| I want to… | Start here |
|---|---|
| **Read the story** | **[Year One — From Dusthill to the Crown](narrative/YEAR_ONE.md)** (full arc spoilers) |
| Understand the story's organization and spoiler limits | [Narrative guide](narrative/README.md) |
| Look up a character, place, event or contested fact | [World reference portal](world/README.md) |
| Inspect **episode-by-episode evidence** | [E000 dossier](episodes/E000.md), [E001 dossier](episodes/E001.md) and the numbered `episodes/E###.md` files |
| Read the first post-arc GM/cast retrospective | [March 2019 Year One Q&A](episodes/BONUS-2019-03.md) — **bonus, not E055** |
| Check actual versus original episode numbering | [Corrected crosswalk](project/EPISODE_NUMBERING.md) |
| Follow unresolved listening tasks | [Review queue](project/REVIEW_QUEUE.md) |
| Understand source confidence and editing conventions | [Editorial guide](project/EDITORIAL_GUIDE.md), [documentation architecture](project/DOCUMENTATION_ARCHITECTURE.md) |

The **Year One narrative** is for reading. The **episode dossiers and source SRTs** support the research; a story summary is not a replacement for original cues, transcripts, source handouts or audio verification.

## Transcriptions and source status

This repository distinguishes four kinds of text:

- **Original or processed ASR sources:** model/run-specific SRTs and experimental evidence in `sources/` and `reports/`. Retain these rather than silently replacing them when a new model disagrees.
- **Readable machine drafts:** [E000](transcripts/E000.readable-draft.md) and [E001](transcripts/E001.readable-draft.md), with approximate timestamps and diarization.
- **Reader-edited pilot drafts:** [E000](transcripts/E000.reader-draft.md) and [E001](transcripts/E001.reader-draft.md), accompanied by [E000](transcripts/E000.reader-edits.json) and [E001](transcripts/E001.reader-edits.json) change logs. Spelling edits and speaker normalization do **not** certify every word.
- **Source-linked reference dossiers and syntheses:** the current `episodes/`, `world/` and `narrative/` material. Later episodes and the Q&A may **resolve questions** without making the original episode's contemporaneous perspective wrong.

Examples of evidence that must stay separate: **Diontalus** and **Eye of Groxl** are owner-confirmed display spellings, not proof a given audio syllable was heard correctly; **Tietkalla** is cast-written but matched to the relevant ASR referent contextually. The E054 rescue establishes **Angelashi survived** a previously reported death. The Q&A reveals Beau's intended explanation for **Buttons' motives**, which the characters did not necessarily know while he was alive.

### Run the pilot tooling

The project uses Python scripts and tests. Refer to the full [workflow](project/WORKFLOW.md), [model experiments](project/MODEL_TESTS.md), [multi-pass method](reports/MULTIPASS_PIPELINE.md) and [source audit](reports/SRT_AUDIT.md) before reprocessing files.

```bash
python tools/build_transcripts.py
python tools/build_reader_editions.py
python -m unittest discover -s tests -p 'test_reader_editions.py'
python tools/audit_sources.py
```

These commands rebuild/check the **pilot**, not the entire long-form episode archive. Audio recordings are not bundled in the repository, and unchanged machine output must not be confused with an audio review. For material from the fan wiki or Discord see [external-source policy](project/EXTERNAL_REFERENCES.md), [asset provenance](project/IMAGE_ASSETS.md) and the [spelling report](reports/DISCORD_SPELLING_2026-10-21.md). Images do **not** inherit an automatic distribution license from wiki text.

## Documentation evolution

Previously this README accumulated **detailed appendices for every researched episode batch**, mixing workflow results, narrative and source review. That inventory has been preserved as a [historical 2026-10-21 snapshot](research/legacy/2026-10-21/ROOT_README.md), with its relative links adjusted. The corresponding old [world README](research/legacy/2026-10-21/WORLD_README.md) is also preserved.

The active organization is described in [documentation architecture](project/DOCUMENTATION_ARCHITECTURE.md). **Narrative Year One and the brief portals are complete first-pass consolidations; the large `world/` research compendia have *not* all been rewritten yet.** Their migration to subject-centered reference files follows in stages, keeping original detail available and correcting links before retiring duplicated prose.

The [project decisions](project/DECISIONS.md) track accepted choices; [project backlog](project/BACKLOG.md) records implementation work. Nothing in this rewrite overwrites the original SRTs or the seed [entities.json](world/entities.json).
