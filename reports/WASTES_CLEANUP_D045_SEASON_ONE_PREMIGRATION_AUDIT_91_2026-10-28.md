# Wastes Cleanup — Batch 91: Season One five-arc preservation and E101 navigation audit

**Date:** 2026-10-28. **Disposition: READ-ONLY PRE-MIGRATION AUDIT COMPLETE.** D-045 accepts eleven arc **boundaries**, not a selected new filename convention, final chapter prose, or destructive renaming. D-047 prohibits unapproved chronology, scene, identity, source, custody, meaning and compatibility changes. **No narrative/episode/world/compatibility source edits, source archives, staging, commits or pushes performed in this batch.**

## File access, Git and original-source integrity

At batch start re-evaluated the full access priority: direct local repository checkout not mounted at `/local/There Will Be Dungeons Transcripts`, `/mnt/data/There Will Be Dungeons Transcripts`, `/workspace/There Will Be Dungeons Transcripts`, `/workspaces/There Will Be Dungeons Transcripts`; authenticated **workspace MCP reachable**, GitHub available as the next fallback, Git-generated patches and ZIP not required. Re-evaluate from the beginning for each future access batch or after a failure.

Live `There Will Be Dungeons Transcripts` `main` HEAD **`875625eba95369804be8f3ceba8d46daf4f8d998`**, **clean worktree (0 visible changes / 0 restricted)** at opening. This **differs from Batch 90's HEAD**, and the previously generated Batch83–90 artifacts are now present in the repository baseline; do not recreate presumed pending changes. After the read-only report writes, pre-existing narrative bytes were not modified.

**[Five-arc per-paragraph immutable SHA-256 ledger](WASTES_CLEANUP_D045_SEASON_ONE_PARAGRAPH_SHA256_LEDGER_91_2026-10-28.md):**

| Legacy published arc | Exact bytes | CRLF lines | Original narrative body paragraphs | Inline Markdown link occurrences | Footnote definitions | Full-file SHA-256 |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `ARC_ONE.md` | **24,216** | **145** | **42** | 47 | 15 | `956c0a4a6314fc09aee7f985bd7c95a6c9c6274ee958cfb0eaec557e11b39e7a` |
| `ARC_TWO.md` | **25,058** | **152** | **39** | 49 | 18 | `7893a77a9f77ab94bd79e316abeb8d2c32f5c489f3ab8c7f8acb5318687c5f38` |
| `ARC_THREE.md` | **28,792** | **155** | **42** | 29 | 21 | `730c17ee5ed78d8aca1c0f716bc8bb766b39289a6fbe97aeaf447877ad7cbca7` |
| `ARC_FOUR.md` | **24,569** | **167** | **47** | 46 | 21 | `428f5e930d4d2e55de3f77f98d0809e9e6db6f3e526d75a4672c9b82be095a39` |
| `ARC_FIVE.md` | **28,734** | **177** | **47** | 43 | 29 | `a2dfb834af74f8ad73c95332156ee19419614c30df2d305d53482734f26c8284` |
| **Total** | **131,369** | **796** | **217** | **214** | **104** | — |

**The complete SHA-256 algorithm passed the standard `abc` test vector.** Four files were directly read as complete original MCP binary and independently compared against their MCP-advertised SHA and previously recorded SHA/size. `ARC_ONE.md` is an **access fallback case**, not silently skipped: direct MCP full binary and broad first-line reads were safety-blocked, smaller MCP windows worked; GitHub default supplied **LF-normalized** text, which was restored to original CRLF and independently yielded the **exact previously documented original 24,216 bytes and full SHA**. This is a cryptographically matched substitute, **not** a claim of complete direct MCP download. Maintain original line endings/UTF-8 bytes on any future backup.

The SHA ledger records every original body paragraph's file, one-based line, zero-based byte offset, exact UTF-8 byte count and **SHA-256 of line content excluding CRLF**. Five files use one-line prose paragraphs separated by blank lines. There are **217** such original body paragraphs. These are immutable source **identities**, **not** final scene-to-chapter destinations or permission to drop other content.

## Link, heading and footnote retention

**[Exhaustive five-file original links/heading/footnote-ID ledger](WASTES_CLEANUP_D045_SEASON_ONE_LINK_HEADING_LEDGER_91_2026-10-28.md):**

- **214** original ordinary inline Markdown link occurrences, **148 distinct URL destination strings**, **55 original ATX headings** and **104 footnote definitions**. All **104 original footnote reference IDs are paired** to definitions within their respective files; zero missing/unused definitions in the parsed source. **0** outbound URL fragments and **0** external link schemes were found by the static parser.
- Original link label, exact destination, file and line are all recorded; original heading text/line and original footnote ID/line are listed. Footnote **bodies** remain in original source and must be preserved by archive/explicit mapping before any migration; a definition ID does **not** substitute for its source and interpretive content.
- The static parser counted 148 destination strings but the attempted **bulk file-target validation exceeded the tool-call limit**. A follow-up directory-list approach was also safety-blocked. **Do not claim 148/148 target files have been independently opened.** Important exact paths were separately rechecked with bounded file reads: `episodes/E101.md`, `reports/E101_ASR_COMPARISON_2026-10-23.md`, `episodes/E000.md`, `episodes/E128.md`, `narrative/ARC_FOUR.md`, `narrative/ARC_FIVE.md`, `world/HISTORICAL_EVENTS.md`, `world/CONSISTENCY_LEDGER.md`; all **eight** can be read, with two initial narrow-binary safety blocks resolved by two-to-five-line MCP text reads.
- Original prose and notes are based on processed ASR, **not independent audio listening**. No GFM rendering, Markdownlint, full target/anchor/inbound-link tests or test suite performed.

## Exact E101 shared-episode boundary (new Arc 07/08)

This is a **verified owner-confirmed narrative boundary**, **not** a proposed season break or a new twelfth arc.

- `narrative/ARC_FOUR.md` **L103–115** (chapter VIII): Hope actually attaches the **Hand of the Voice** to her own severed right arm, distinct from the Fist gauntlet that remains with the others. The Voice offers a solo choice; **Hope physically leaves White Tower through the stone arch/infernal portal with Spatulo**. By **L115** Nash, Stanley and Vorel remain at the White Tower and the portal has closed. The recorded four-arc story stops here.
- `narrative/ARC_FOUR.md` **footnote L153** documents the **end around 01:57–01:59 in E101** and explicitly assigns the subsequent same-recording Kaiser Casino sequence to Arc Five. `narrative/README.md` L46 describes the earlier choice around **01:44**, physical closed portal around **01:58**, and two continuing POV threads. This is supported by [E101 dossier](../episodes/E101.md), [two-ASR comparison](E101_ASR_COMPARISON_2026-10-23.md), and `world/CONSISTENCY_LEDGER.md` L608; the recorded timing is approximate processed-source timing, not independently listened.
- `narrative/ARC_FIVE.md` **L5–15** immediately opens **after** Hope has departed, following her Kaiser Casino encounter with the Asmodeus-claiming host Brett and Nash, Stanley, Vorel's ongoing White Tower business in parallel. These are **separate experienced viewpoints**, not identical events or fresh independent recording numbers.
- Approved D-045 **Arc 07** = legacy `ARC_FOUR.md` E082–E101 **through departure**; approved **Arc 08** = legacy `ARC_FIVE.md` **remainder of E101**, E102–E106 and E110–E114. **E101 is one unique dossier**, referenced in two story arcs; never duplicate source-count, infer all companions know Hope's private patron instructions, or relocate the postdeparture casino dialogue before the portal choice.
- Explicit unchanged world-history incoming links: `world/HISTORICAL_EVENTS.md` L24 to both Arc Four and Five; `world/CONSISTENCY_LEDGER.md` L608; `world/places/white-tower.md` to Arc Four; the reader `narrative/README.md` L46 and L65–66 record the transitional split. They require coordinated compatibility protection, not piecemeal edits.
- Separate record exceptions remain binding: **E013.5** supplemental scene placement in fictional time; **E043** and **E127** standalone one-offs; **E107–E109** historical Dunebreaker prequel, not the main sequence or an extra journey before E110; E128 is the actual Season One finale. D-045's approved arc mapping for old arcs: One→01/02, Two→03/04, Three→05/06, Four→07, Five→08/09.

## Scoped incoming source dependencies

Literal `ARC_ONE.md`…`ARC_FIVE.md` searches were executed within the **narrative, wastes and world** directories, with exact reader/crosslink matches checked against source. The following are the main actionable sources:

- `narrative/README.md` links every old word-form arc as a reader entry and again in its table and source notes; older arcs additionally contain **previous/next arc navigation** and scholarly citation links between them.
- `wastes/README.md` contains all five direct story route links (two broad searches were safety-blocked, but the entry paths are already confirmed in the directly read 40-line overview).
- `world/CHRONOLOGY.md` mentions old Arc One/Two/Three labels, with `world/characters/nash-maggard.md` and `world/places/dusthill.md` linking Arc One. `world/HISTORICAL_EVENTS.md`, `world/CONSISTENCY_LEDGER.md` and `world/places/white-tower.md` reference the Arc Four/Five and E101 transition.
- `project/DECISIONS.md`, approved eleven-arc crosswalk and historical cleanup reports contain **historical references**. Do not rewrite those as though the old structure was never published; add migration decisions/compatibility as new records.
- These are **scoped discovery and verified key examples**, **not a full count of every inbound hyperlink** in reports, project notes, archived `local/` sources or external HTTP bookmarks. The bulk `local/` and broad root census are not certified. Keep all six historical arc paths working while eleven-arc navigation is being prepared.

## Decision gate / next bounded work

**Existing published `narrative/` still contains only six word-form Arc One–Six files, the guide and two season compatibility stubs**. The previously recommended numeric `ARC_01.md`–`ARC_11.md` is an **option, not an approved filename policy**; no new arc files, redirects, route replacements or scene rewrites were created by Batch91.

**Recommended next Batch92:** Finish the **148 distinct original Season One URL destinations** with directory-index or appropriately throttled file existence checks, verify source footnote body/mapping and explicit inbound links, then prepare a **short high-impact scene/paragraph pilot** around legacy Arc Four L103–115 and legacy Arc Five L5–27 for target Arcs 07/08. That pilot can add original episode source provenance, but must not invent authoring decisions. Before actual migration resolve filenames/compatibility with the owner, independently archive exact **then-current source working bytes** for each edited arc, verify SHA/size, map paragraph identities/notes to retained/summarized/new chapters and revalidate existing incoming links. No unapproved story-time or identity edits.

**Batch 91 files added:** this report and the two source ledgers, plus manifest/progress checkpoint changes. **No source edits or commit/push.**
