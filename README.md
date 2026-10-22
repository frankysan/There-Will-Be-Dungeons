# There Will Be Dungeons — The Wastes archive

**A local-first transcription and campaign-reference project.** The long-term goal is an accurate, searchable, source-linked archive of *The Wastes*, beginning with the first campaign arc and its cast/GM discussions.

**Current research coverage:** corrected **E000–E065**, including **E013.5**, a separate **E043 holiday one-shot**, and **March, April, June and July-archived 2019 bonus discussions**. E055 begins after a **real three-month fictional jump** following E054. These episode dossiers are **provisional notes from processed Parakeet SRTs, not finished or listener-proofread transcripts**. The ongoing E000/E001 speaker-labelled reader-edition pilot remains separate.

## Choose how to explore

| I want to… | Start here |
|---|---|
| **Read the story** | [**Year One — From Dusthill to the Crown**](narrative/YEAR_ONE.md), then [**Year Two — Stones, Souls and the Great Fang**](narrative/YEAR_TWO.md) (E055–E065) |
| Understand the story's organization and spoiler limits | [Narrative guide](narrative/README.md) |
| Look up a character, place, event or contested fact | [World reference portal](world/README.md) |
| Inspect **episode-by-episode evidence** | [E000 dossier](episodes/E000.md), [E001 dossier](episodes/E001.md) and the numbered `episodes/E###.md` files |
| Read the latest researched episodes | [E062](episodes/E062.md), [E063](episodes/E063.md), [E064](episodes/E064.md), [E065](episodes/E065.md) |
| Read the cast/GM bonus discussions | [March 2019 Q&A](episodes/BONUS-2019-03.md), [April 2019 The First and Last](episodes/BONUS-2019-04.md), [June-archived Q&A](episodes/BONUS-2019-06.md) (spoken as May's show) and [July-archived Q&A](episodes/BONUS-2019-07.md) (**spoken as June's show, recorded June 29, per introduction**); **not numbered Wastes episodes** |
| Check actual versus original episode numbering | [Corrected crosswalk](project/EPISODE_NUMBERING.md) |
| Follow unresolved listening tasks | [Review queue](project/REVIEW_QUEUE.md) |
| Understand source confidence and editing conventions | [Editorial guide](project/EDITORIAL_GUIDE.md), [documentation architecture](project/DOCUMENTATION_ARCHITECTURE.md) |

The **Year One narrative** and **opening Year Two chapters** are for reading. The **episode dossiers and source SRTs** support the research; a story summary is not a replacement for original cues, transcripts, source handouts or audio verification.

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

The active organization is described in [documentation architecture](project/DOCUMENTATION_ARCHITECTURE.md). **Phases A–D are now structurally consolidated as first editorial passes:** the Year One narrative, navigational portals, [subject-based characters](world/CHARACTERS.md) and [places](world/PLACES.md), [thematic world guide](world/WORLD.md) and [unified chronology](world/CHRONOLOGY.md). Their older batch research is preserved in the [2026-10-21](research/legacy/2026-10-21/README.md) and [2026-10-22](research/legacy/2026-10-22/README.md) archives. The [active consistency ledger](world/CONSISTENCY_LEDGER.md) now separates **open issues** from **accepted spellings and source-cutoff resolutions**. The [review queue](project/REVIEW_QUEUE.md) prioritizes listening and handouts, preserving the old full registers in the [archive](research/legacy/2026-10-22/README.md). **This does not certify audio accuracy or a complete entity index.**

The [project decisions](project/DECISIONS.md) track accepted choices; [project backlog](project/BACKLOG.md) records implementation work. Nothing in this rewrite overwrites the original SRTs or the seed [entities.json](world/entities.json).
