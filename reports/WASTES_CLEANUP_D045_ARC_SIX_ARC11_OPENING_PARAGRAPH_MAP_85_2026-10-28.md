# Wastes Cleanup — Batch 85: Arc 11 S3E05–S3E09 source-paragraph and provenance map

**Date:** 2026-10-28 (Europe/Stockholm). **Disposition:** READ-ONLY BOUNDED MAPPING COMPLETE. This is a candidate source-to-chapter crosswalk under **D-045**, not rewritten narrative, approved chapter prose, a claim of original-audio verification, or permission to delete old arcs. **D-047 substantive story edits require explicit owner approval**; D-048 requires source retention.

## Current repository, access and protected original

- Checked file-access hierarchy from the start: no directly mounted local checkout at `/local`, `/mnt/data/There Will Be Dungeons Transcripts`, `/workspace/There Will Be Dungeons Transcripts`, or `/workspaces/There Will Be Dungeons Transcripts`. Keycloak-authenticated workspace **MCP connected**; GitHub, Git-generated patches and ZIP fallback unneeded. Re-evaluate the chain on every subsequent access batch and on tool failure.
- Live repository `There Will Be Dungeons Transcripts`, branch **main**, HEAD **`02e35be895c72260d3c0ebc8ef402ef361d90206`**. **Four pre-existing visible changes, zero restricted**, only Batches 83–84 report/tracker work; preserved. No Git stage, reset, commit or push.
- Original `narrative/ARC_SIX.md` remains **813 numbered lines / 206,128 bytes**, SHA-256 **`44e8b30073d3d95a93b449783de11c7cafac1e74473c2ea082ce7e68b1ee541d`**. This unchanged source was **read in four consecutive source ranges L321–362, L363–402, L403–442 and L443–482: 162/162 lines, zero gaps**. The extra read through L482 completes S3E09 rather than cutting mid-episode at the initially projected ~L450. Next episode S3E10 starts at `### Stomping grounds` L483, separately previewed, not included in the counting below.
- D-045 approved Arc 11 spans played **S3E04–S3E18**, not S3E019 cast Q&A. [Approved chapter proposal](../project/WASTES_NARRATIVE_CHAPTER_MAPS.md): **ch 1 S3E04**, **ch 2 S3E05–S3E06**, **ch 3 S3E07–S3E09**, **ch 4 S3E10–S3E11**, then later scenes. [Batch 83](WASTES_CLEANUP_D045_ARC_SIX_PARAGRAPH_PILOT_83_2026-10-28.md) already mapped Arc 11/ch 1 (S3E04, L285–320, 15 paragraphs/~1,410 words). Chapter titles and exact word budgets remain **preliminary**.

## Exact episode-section and source paragraph ledger

The source has **six scene headings for five episodes**: `### The assault begins` and `### Fire at the northern gate` are **both S3E05**, whereas `### Bring in the ape` starts S3E06. One heading = one played episode is **not** a valid general rule.

**Counting method:** line IDs below are starting lines of nonempty narrative prose/status paragraphs, excluding `###` headings, blank rows and the three **standalone citation/provenance lines L405, L441, L481**. Words count source Markdown whitespace-separated tokens and are approximate diagnostics, not rendered-reader text. Stable paragraph content hashes need to be established separately before any future edit; source-line IDs change after edits.

| Arc 11 destination | Played episode, original scene heading(s) | Exact legacy source interval | Narrative paragraph starts | Paras | Approx words |
| --- | --- | --- | --- | ---: | ---: |
| **Ch 2** | **S3E05 — The Attack**; `The assault begins` L321; `Fire at the northern gate` L339 | **L321–354** | **323,325,327,329,331,333,335,337,341,343,345,347,349,351,353** | **15** | **1,621** |
| **Ch 2** | **S3E06 — Bring In The Ape**; `Bring in the ape` L355 | **L355–378** | **357,359,361,363,365,367,369,371,373,375,377** | **11** | **1,090** |
| **Ch 3** | **S3E07 — Dragon on Dragon Action**; `Dragon on dragon action` L379 | **L379–406** | **381,383,385,387,389,391,393,395,397,399,401,403** | **12** | **1,191** |
| **Ch 3** | **S3E08 — Electric Lizard**; `Electric lizard` L407 | **L407–442** | **409,411,413,415,417,419,421,423,425,427,429,431,433,435,437,439** | **16** | **1,402** |
| **Ch 3** | **S3E09 — Tank Boy**; `Tank boy` L443 | **L443–482** | **445,447,449,451,453,455,457,459,461,463,465,467,469,471,473,475,477,479** | **18** | **1,446** |

**Counts verified independently:** **Arc 11/ch 2 = 26 paragraphs / ~2,711 words**; **Arc 11/ch 3 = 46 paragraphs / ~4,039 words**; **total 72 paragraphs / ~6,750 words** across 162 consecutive lines and five played episodes. Adding previous S3E04 Arc 11/ch 1 gives **87 mapped Arc 11 original prose/status paragraphs / ~8,160 whitespace words from S3E04–S3E09**. This is source material volume, **not** acceptable compression targets or finished replacement chapter lengths.

## Provenance/readability checkpoint

Played dossier files were opened in bounded numbered reads and their exact current binary metadata independently fetched. No original audio was listened to.

| Dossier | Readable file bytes | SHA-256 |
| --- | ---: | --- |
| `episodes/S3E05.md` | 16,179 | `011c43db4d5e34cce5d5fdaf590d506ad5e47b33c8cc4a37a99a61b194671241` |
| `episodes/S3E06.md` | 14,857 | `07326d2c3f12e2a5f2a7287a67cc243d68c09cfd79831adb533deeb17d9f8f3c` |
| `episodes/S3E07.md` | 16,002 | `1cb2bde6ca651474e1b171009b8cd17f53824f8f1b5fa3ff4ec9c8b5e751236c` |
| `episodes/S3E08.md` | 15,464 | `849ff919390e62ac07282db19f31197946284d91858c72ccb7bfaef7f9b5a718` |
| `episodes/S3E09.md` | 19,498 | `d910b2e8a320e911755444692d1fba6fa440f2af4a24531e1d493a92f2da95a5` |

The **three original narrative source/provenance link paragraphs must follow their episode sections**, not be lost as unassigned "extra narrative":
- L405: `[Source-first S3E07 dossier](../episodes/S3E07.md)` and `[Two-ASR comparison](../reports/WASTES_S3E07_ASR_COMPARISON_2026-10-26.md)`;
- L441: `[Played S3E08 dossier](../episodes/S3E08.md)` and `[two-ASR comparison and audio questions](../reports/WASTES_S3E08_ASR_COMPARISON_2026-10-26.md)`;
- L481: `[Played S3E09 dossier](../episodes/S3E09.md)` and `[independent ASR comparison](../reports/WASTES_S3E09_ASR_COMPARISON_2026-10-27.md)`.

All **six Markdown link destinations** in those three lines were independently read and exist, including all three comparison reports. S3E05/S3E06 source intervals have **zero inline narrative links**; new source notes in any rewritten reader-first chapter must derive from actual dossiers, not fictitious old per-paragraph citations. Global research/source audit links near L807–813 remain to be inventoried in a later batch.

## Source-to-scene continuity and meaning protections

**Chapter 2 — S3E05–S3E06 (L321–378):**
- **L323–337:** War council decisions turn into actual embarkation and attack **only during S3E05**. Keep Stanley/Union's private loyalty conversation, Vorel rallying ~75 lizardfolk, Nash's farewell to Angelashi and four children, the alternate Nashes' uneven discipline and Stanley's real confrontation with Delit Or'Nath's enchanted face. Ruby is **fully constructed but not Earth-deployed**. Attack at the north gate begins, Hope drives the improvised vehicle, first gate Slow Peters fall.
- **L339–353:** *Mask of Eltanfawr / Peer into Plurality* foresight is activated, Stanley temporarily blinded; allies take losses. Gate and air-defense state **not settled at S3E05 cutoff**, even though two sentry Slow Peters were destroyed. Respect episode-cutoff distinction between intentions, radio reports and actual cannon destruction.
- **L355–377:** S3E06 is new battle continuing the still-closed north gate. Stanley **actually transforms into a giant ape**, combats the Paladin and eight Kuromokishi; Vorel redirects fire and remains a front-line combatant. The northern encounter is won by cutoff, **but gate not visibly opened, other AA targets unconfirmed in that episode**, and Ruby still undelivered. Do not attribute S3E07's later all-four-AA confirmation to S3E06.

**Chapter 3 — S3E07–S3E09 (L379–482):**
- **L381–403 / S3E07:** Southwest operation results in radio-reported deaths of **97 of 99 alternate Nashes**, with **White Nash and Unfortunate Nash** surviving in reported status, not 97 witnessed individual deaths. All four AA objectives are **now reported successful**, Bokbok launched over north wall, heroes get back on Fate Six. Separate original Nash, both survivors, and later alternate identity claims. A chrome dragon is defeated in played combat; **Fate Six physically crushed by giant's hand** later and ghost crew dissipates, but their permanent metaphysical death **not shown**. **Dragon Nash rescues completed Ruby**, which is not activated in Earth's core. The giant is revealed as Groxl in table evidence, separate from dead chrome dragon. Preserve exact uncertainty of giant's origin and old titles.
- **L405:** Original S3E07 source/audit links and machine-transcript caution are part of the episode record.
- **L409–439 / S3E08:** Groxl giant combat, Eye of Groxl's response and Vorel entering the giant's body; **Hope/Nash extract and drop the giant's machinery generator into lava**. Do **NOT** misidentify this **generator** as Ruby or claim Ruby was permanently activated here. Diontalus's visible spectral form disintegrates; permanence of metaphysical death is uncertain. **Union and Emenil are actually crushed**, not merely missing. Vorel attacks Groxl from the inside; Groxl is killed; **not evidence that all his ancient self-told history is true**.
- **L441:** Original S3E08 playable dossier/comparison links and unresolved audio/identity notes retained.
- **L445–479 / S3E09:** Vorel experiences the Endless Dunes and a Groxl account; **his reported origin/god-killer claims are testimony**, not authenticated lore or proof of Vorel's biological lineage. Vorel returns to battle, mourns Union, receives an empathy grenade from Chrysorius. The party infiltrates an apparently ordinary suburban dome; Dick Pendleton/General Motors and Toyota Host confront them at Walmart. Unfortunate Nash **actually casts Meteor Swarm**, with collateral losses including Bertrand. Party finds freight elevator; **Ruby remains at allied surface defense at the last S3E09 confirmed cutoff**, not yet inserted or activated.
- **L481 and next dossier:** Preserve S3E09 original source/audit links. At **S3E10's played opening**, the GM/table expressly establish Ruby **with the descending group**, **without depicting its exact intervening retrieval/transfer**. This is a temporal evidence update, not a contradiction to "last visible at the S3E09 cutoff"; do not invent a carrying/handoff scene in either chapter. S3E10 source begins **L483** in original and is **reserved for next batch**.

**Character continuity and reader-first narrative value:** Stanley's conflict with his father's remaining voice; Nash's family farewell; Vorel/Union emotional and eventual loss; Hope's risks and tactical choices; and the scale of allied goblin/lizardfolk/alternate sacrifices must survive any shorter replacement prose. Don't flatten all these into a battle synopsis, equate NPC assertions with GM-confirmed history, or backdate losses/resurrection.

## Density, completeness and next batch

The existing ~350–450-word/chapter measure is **a diagnostic**, not an authorization to delete scenes. Ch 2 source **2,711 words**, ch 3 **4,039 words**: both demand scene/section grouping, potentially longer chapters or newly owner-approved subchapter treatment. The D-045 arc bounds are binding; intra-arc authoring choices are not settled.

This batch fully covers and preserves **source L321–482** at line/episode-granularity, with each of the 72 prose paragraph start IDs above and all three standalone provenance lines. Together with Batch 83, Arc 11 S3E04–S3E09 is now **87 mapped prose paragraphs / ~8,160 words**. **Source L483–805 S3E10–S3E18 and global source footnotes/audits L807–813 have not yet been paragraph-mapped**, though structurally inventoried. No paragraph content SHA mapping, full outbound/inbound URL census, rendered Markdown, source audio or complete migration acceptance.

**Next Batch 86:** Re-evaluate access/Git, then read source `ARC_SIX.md` L483–~630 (complete episodes rather than arbitrary line cutoff) for S3E10–S3E11, the descent and Soulbroker/Weir transition. Identify exact paragraph starts, headings, embedded source notes and verified episode dossier evidence. Advance only to clear episode boundaries, no narrative edits. For eventual edits: archive exact then-current full original, independently verify original bytes/SHA, resolve proposed filename and chapter scheme with owner, preserve paragraph/scene inventories and citations, and stop for any unapproved substantive change. No stage, commit or push.

**No source, episode, location, note, illustration or narrative file was edited in this read-only Batch 85.** Only the new report and cleanup tracking pointers are changed. Rendered GFM, Markdownlint, `git diff --check`, all backlinks, original audio and full tests remain unrun.
