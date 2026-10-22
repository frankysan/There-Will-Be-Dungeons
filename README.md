# There Will Be Dungeons — campaign transcript and reference archive

**A local-first transcription and campaign-reference project.** The long-term goal is an accurate, searchable, source-linked archive of the show's campaigns. **The Wastes and Inverse are separate fictional realities**, with independent continuity, characters, cosmologies and research indexes. The Wastes remains the main researched corpus.

**Current *Wastes* research coverage:** corrected **E000–E081**, including **E013.5**, a separate **E043 holiday one-shot**, and **March, April, June, July, August, September, October and November-publication 2019 bonus discussions**. E055 begins after a **real three-month fictional jump** following E054. These episode dossiers are **provisional notes from processed Parakeet SRTs, not finished or listener-proofread transcripts**. The ongoing E000/E001 speaker-labelled reader-edition pilot remains separate. **Inverse research:** All **four episodes** now have provisional dossiers: [S1E01](inverse/episodes/S1E01.md), [S1E02](inverse/episodes/S1E02.md), [S1E03](inverse/episodes/S1E03.md) and [S1E04 — the recorded finale](inverse/episodes/S1E04.md). Two two-part adventures are indexed in a [strictly separate campaign reference](inverse/README.md). **The final episode delivers the cipher journal, but the Bound plot and companions' auction fate remain open**.

## Choose how to explore

| I want to… | Start here |
| --- | --- |
| **Explore *Inverse* (separate reality)** | [Complete four-episode index](inverse/README.md), [S1E01](inverse/episodes/S1E01.md), [S1E02](inverse/episodes/S1E02.md), [S1E03](inverse/episodes/S1E03.md) and [S1E04 finale](inverse/episodes/S1E04.md). **Not a Wastes timeline** |
| **Read the Wastes story** | [**Year One — From Dusthill to the Crown**](narrative/YEAR_ONE.md), then [**Year Two — Stones, Souls and the Great Fang**](narrative/YEAR_TWO.md) (E055–E081) |
| Understand the story's organization and spoiler limits | [Narrative guide](narrative/README.md) |
| Look up a character, place, event or contested fact | [World reference portal](world/README.md) |
| Inspect **episode-by-episode evidence** | [E000 dossier](episodes/E000.md), [E001 dossier](episodes/E001.md) and the numbered `episodes/E###.md` files |
| Read the latest researched episodes | [E078](episodes/E078.md), [E079](episodes/E079.md), [E080](episodes/E080.md), [E081](episodes/E081.md) |
| Read the cast/GM bonus discussions | [March 2019 Q&A](episodes/BONUS-2019-03.md), [April 2019 The First and Last](episodes/BONUS-2019-04.md), [June public-release Q&A](episodes/BONUS-2019-06.md) (called May's bonus when recorded), [July public-release Q&A](episodes/BONUS-2019-07.md) (called June's bonus; **June 29 recording-date claim** in ASR) and [August public-release Q&A](episodes/BONUS-2019-08.md) (**July 27 recording-date claim** in ASR), and [September public-release Q&A](episodes/BONUS-2019-09.md) (early member access; **exact recording date unverified**), plus [October public-release Q&A](episodes/BONUS-2019-10.md) (early member access; **exact recording date unverified**, separate *Inverse* discussion) and [November public-release Q&A](episodes/BONUS-2019-11.md) (host calls it an **October bonus**; actual recording/publication dates need verification). **For bonuses, filename months represent public publication, not recording or early-member availability**; **not numbered Wastes episodes** |
| Check actual versus original episode numbering | [Corrected crosswalk](project/EPISODE_NUMBERING.md) |
| Follow unresolved listening tasks | [Review queue](project/REVIEW_QUEUE.md) |
| Run Markdown structure and table checks | [Markdownlint setup and CI](project/MARKDOWN_LINTING.md) — `npm install`, then `npm run lint:markdown` |
| Understand source confidence and editing conventions | [Editorial guide](project/EDITORIAL_GUIDE.md), [documentation architecture](project/DOCUMENTATION_ARCHITECTURE.md) |

The **consolidated Year One and Year Two narratives** are for reading. **Year Two now covers the completed CHIDS/Traversal Drive confrontation through E081**, while the larger Principle/soul pact story is unresolved. The **episode dossiers and source SRTs** support the research; a story summary is not a replacement for original cues, transcripts, source handouts or audio verification.

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

The active organization and the [E055–E081 second-arc consolidation report](reports/SECOND_ARC_CONSOLIDATION_2026-10-22.md) are described in [documentation architecture](project/DOCUMENTATION_ARCHITECTURE.md). **Phases A–D are now structurally consolidated as first editorial passes:** the two arc narratives, navigational portals, [subject-based characters](world/CHARACTERS.md) and [places](world/PLACES.md), [thematic world guide](world/WORLD.md) and [unified chronology](world/CHRONOLOGY.md). Their older batch research is preserved in the [2026-10-21](research/legacy/2026-10-21/README.md) and [2026-10-22](research/legacy/2026-10-22/README.md) archives. The [active consistency ledger](world/CONSISTENCY_LEDGER.md) now separates **open issues** from **accepted spellings and source-cutoff resolutions**. The [review queue](project/REVIEW_QUEUE.md) prioritizes listening and handouts, preserving the old full registers in the [archive](research/legacy/2026-10-22/README.md). **This does not certify audio accuracy or a complete entity index.**

The [project decisions](project/DECISIONS.md) track accepted choices; [project backlog](project/BACKLOG.md) records implementation work. Nothing in this rewrite overwrites the original SRTs or the seed [entities.json](world/entities.json).
