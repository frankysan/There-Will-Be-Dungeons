# Wastes Cleanup — Batch 83: legacy Arc Six paragraph-to-episode pilot at the approved Arc 10/11 boundary

**Date:** 2026-10-28 (Europe/Stockholm). **Status: READ-ONLY bounded paragraph/source-link pilot COMPLETE; NO narrative migration.** D-045 approves *arc boundaries*, not proposed chapter prose or destructive relocation. D-047 requires explicit approval for substantial new narration, scene relocation/deletion, or unsupported interpretations. D-048 demands reader-first writing while preserving traceability. Do not treat this report as approval to create or overwrite final Arc 10/11.

## Preflight and exact live baseline

- Rechecked access priority: local checkout absent under `/local`, `/mnt/data/There Will Be Dungeons Transcripts`, `/workspace/There Will Be Dungeons Transcripts`, `/workspaces/There Will Be Dungeons Transcripts`; Keycloak-authenticated repository MCP reachable. GitHub, Git patches and ZIP not required; restart priority on every file access batch and if MCP fails.
- Live repository `There Will Be Dungeons Transcripts`: branch **`main`**, HEAD **`02e35be895c72260d3c0ebc8ef402ef361d90206`**, **clean working tree (0 visible / 0 restricted)** at opening. Changed HEAD since Batch 82; do **not** assume previous 12 working changes are still uncommitted or recreate old patches. No stage/commit/push/reset here.
- Unmodified `narrative/ARC_SIX.md`: **813 numbered lines / 206,128 bytes**, independently reported SHA-256 **`44e8b30073d3d95a93b449783de11c7cafac1e74473c2ea082ce7e68b1ee541d`**. Source was read in ten ordered 90-line structural windows covering L1–813 (headings/length), and in gap-free numbered detail windows **L185–321** for this pilot. This is a source-line/paragraph inventory, **not a complete paragraph-level mapping of all 813 lines**.
- Approved arc crosswalk: [eleven-arc chapter map](../project/WASTES_NARRATIVE_CHAPTER_MAPS.md) (D-045) assigns **Arc 10** S2E01–S2E12 plus S3E01–S3E03, and **Arc 11** S3E04–S3E18. Chapters and chapter-beat outlines in that document remain **preliminary, not checked/source-complete**.
- Referenced played episode dossiers, all individually confirmed readable:
  - `episodes/S2E12.md` 16,590 bytes / SHA `9ef4ea50c1a76aaa49c434648f9d5c490d57ac6e81abb025dbffec66a402e86d`.
  - `episodes/S3E01.md` 16,758 bytes / SHA `a7e5adf192035ada7615369447dfa76d1481f00addb0eb0ebd9be4a85a0f54fd`.
  - `episodes/S3E02.md` 18,221 bytes / SHA `5a5669349cbbfc96553944a14fdb10a032b01ee287cb8281bb6a24aeb6eecf48`.
  - `episodes/S3E03.md` 14,896 bytes / SHA `8b483e33fa462c48878fd2d0dc3a08f434df94ffaf64c5c09bf7bec0463815b4`.
  - `episodes/S3E04.md` 14,974 bytes / SHA `13738e21dcd0dd0193c4d0e993825933819f1e3c6b272bd491dae0a2a162e0ae`.
  - `episodes/S3E05.md` 16,179 bytes / SHA `011c43db4d5e34cce5d5fdaf590d506ad5e47b33c8cc4a37a99a61b194671241`.
  These are episode **processed-ASR research dossiers**, not independent original audio listening. The season episode labeling on the *legacy source* predates D-045; preserve it as historical working context rather than assuming already migrated arcs.

## Complete contiguous boundary pilot: original source L185–321 (137/137)

This is an exact **line-level** inventory, using numbered Markdown source **line** IDs as provisional paragraph IDs; if content is edited later, add stable paragraph hashes to a separate preservation manifest first. Word counts count whitespace-separated tokens in the source Markdown, **including emphasis syntax**, and exclude headings and blank lines; they are **diagnostic approximations**, not rendered prose counts.

| Legacy source line span | Original heading / record | Proposed new home | Prose paragraph IDs | Approx. words | Source/evidence |
| --- | --- | --- | ---: | ---: | --- |
| **185–200** | `### Dust to Dust — the end of a season, not the quest` | **Arc 10, ch.6**, closing S2E12 | **7** (includes L199 season-cutoff statement) | **632** | [Played S2E12](../episodes/S2E12.md); **season only**, NOT arc ending |
| **201–204** | Season Three / editorial boundary pointer, L203 inline `[S3E01]` | **Compatibility/source notes**, not a new story scene | **0** | **0** | [Played S3E01](../episodes/S3E01.md) |
| **205–226** | `A ship caught between Hell and chrome` | **Arc 10, ch.7** | **10** | **779** | [S3E01](../episodes/S3E01.md): regeneration, Hell vessel and Principal arrival; battle unfinished |
| **227–238** | `The price of the Hand` | **Arc 10, ch.7** | **5** | **447** | [S3E02](../episodes/S3E02.md): stolen Hand, rescue and rift escape |
| **239–252** | `Sprout and the lives saved` | **Arc 10, ch.7** | **6** | **567** | [S3E02](../episodes/S3E02.md): aftermath, Union/Spider surgery, living Sprout, Mars choice |
| **253–264** | `An unwelcome feast of memories` | **Arc 10, ch.7** | **5** | **548** | [S3E03](../episodes/S3E03.md): parasite-induced shared dream; claims not independently true |
| **265–274** | `The hundred Nashes` | **Arc 10, ch.7** | **4** | **342** | [S3E03](../episodes/S3E03.md): arrival on Mars, 99 variants, family reunion |
| **275–284** | `Gifts before war` | **Arc 10, ch.7; last source section** | **4** | **334** | [S3E03](../episodes/S3E03.md): vulnerability, Hope receives *Diplomacy*, proposed augmentation (not performed yet) |
| **285–300** | `A final evening, and the work of being alive` | **Arc 11, ch.1; first source section** | **7** | **690** | [S3E04](../episodes/S3E04.md): actual augmentation, Vorel refuses, lizardfolk ritual, family/Monsoon farewells |
| **301–306** | `A feast for heroes` | **Arc 11, ch.1** | **2** | **152** | [S3E04](../episodes/S3E04.md): **actual** *Heroes' Feast* and one bowl consumed |
| **307–320** | `The second council` | **Arc 11, ch.1; source cutoff** | **6** | **568** | [S3E04](../episodes/S3E04.md): Ruby completed, briefly tested **on Mars**, war plan **approved but not executed** |
| **321** | `The assault begins` heading | **Arc 11, ch.2**; next episode boundary | heading only | **0** | [S3E05](../episodes/S3E05.md) actual attack begins |

**Totals:** S3E01–S3E03 target Arc 10/ch.7 = **34 narrative paragraphs / ~3,017 source words**; S3E04 target Arc 11/ch.1 = **15 paragraphs / ~1,410 source words**. Together **49 paragraphs / ~4,427 words**, excluding headings, transition note and S2E12 ending. S2E12 closing adds **7 source prose/status paragraphs / ~632 words** to Arc 10/ch.6. All **137 consecutive numbered lines L185–321 were available without gaps**. L203 contains **one existing episode link**; the L205–320 narrative paragraphs have **no inline Markdown links**, so future evidence citations must be attached based on dossiers rather than erroneously claiming per-paragraph existing citations. The original Arc Six source has concentrated global source/audit links around L805–813 that require a separate migration/compatibility inventory.

### Paragraph-level retention manifest for the approved S3E03→S3E04 split

These are **all source paragraph starting-line IDs**, not illustrative excerpts:

- **Arc 10/ch.7 — S3E01 (10):** L207, 209, 211, 213, 215, 217, 219, 221, 223, 225.
- **Arc 10/ch.7 — S3E02 (11):** L229, 231, 233, 235, 237; L241, 243, 245, 247, 249, 251.
- **Arc 10/ch.7 — S3E03 (13):** L255, 257, 259, 261, 263; L267, 269, 271, 273; L277, 279, 281, 283.
- **Arc 11/ch.1 — S3E04 (15):** L287, 289, 291, 293, 295, 297, 299; L303, 305; L309, 311, 313, 315, 317, 319.
- **Source boundary:** End of **S3E03** at paragraph **L283**. New **Arc 11 begins at heading L285**; first body paragraph **L287**. Source S3E05 starts heading **L321**. **Do not** relocate S3E03 `Gifts before war` (L275–283) merely because its name anticipates battle.

### Source-to-scene trace and safeguards (selected material details)

| Legacy paragraph IDs | Scene/referent | Required disposition and doubt |
| --- | --- | --- |
| **L207–225** | Nash's regenerated heart/body, Tungsten's claimed retained rare material, Hell vessel attack and Principal confrontation | Retain performed *Regenerate*, partial regrowth and unfinished attack. Tungsten's hidden-reagent location remains **his claim**, not a verified retrieval. Principal's statements about Nash/identity remain unproven testimony |
| **L229–237** | Hope loses supernatural Hand; escaping the Princip(al)'s attack | Preserve actual severing and biological hand's return, independent of speculative past-life claims. Don't mark Principal dead in S3E02 |
| **L241–251** | Captives in brig, Sprout, Union's surgery, survivors, decision for Mars | Retain distinct living and deceased characters and Spider's performed surgery; do not invent additional rematerializations |
| **L255–263** | Hallucinatory Hillmaster and Principal "origin" narrative | Waking-world parasitic mind-fluff is witnessed; past-life and family claims presented in common dream are **NOT independently verified memories** |
| **L267–273** | Martian arrival, Tungsten and Dunglestar reunion, alternates, Nash family | Preserve **99** other Nashes (100 including original), provisional Holy Nash leadership, Nash Jr hammer trick and Sprout's existence; no completed war mobilization |
| **L277–283** | Vorel/Union relationship, gift of Diplomacy, Elhandari enhancement offer | Stanley actually **gives *Diplomacy* to Hope**. Four syringes allocated in S3E03; no one injected then. Augmentation **offered, not undertaken** by S3E03 ending |
| **L287–299** | Augmentation, lizardfolk courtship, Stanley/Hope evening, Nash family, Monsoon/Union | Nash, Hope and Stanley actually undergo surgery; Vorel refuses. Preserve no proven family relocation, later Monsoon plans as plans, and Union's reaction without invented permanent breakup |
| **L303–305** | *Heroes' Feast* | Spell **cast**, bowl consumed, protective effects real, but Sprout/body modifications **not cured** |
| **L309–319** | Earthly Defenders war council, Gluptwarp/Ruby, mission map | Ruby **built and briefly demonstrated on Mars**, not Earth-deployed; scout's claims distinguish reported from witnessed; AA strikes/assault **planned but not performed before S3E05** |

### Chapter density / no-compression gate

The preliminary chapter map suggests only **one Arc 10 chapter** for S3E01–03, but its legacy source contains **34 paragraphs and ~3,017 words**. The Arc 11 first chapter similarly contains **15 paragraphs and ~1,410 words**. Relative to the existing ~350–450-word chapter **diagnostic**, this requires purposeful scene grouping and selective non-lossy compression, **not a mechanical paragraph deletion or forcing every paragraph into a 400-word cap**. Preserve character/emotional consequences, knowledge boundaries, sources and causal transitions. The owner-approved **arc boundaries are unchanged**, but **chapter counts, scene selections and new prose need their own source/coverage review before writing**.

## Unfinished work, compatibility and next action

- **Legacy S2 section L1–184** (proposed Arc 10/ch.1–6) has only had full ordered **structural heading census**, not paragraph-to-scene/source coverage. **Arc 11 L321–805** likewise structurally inventoried but **not** paragraph mapped. Global source/audit notes L805–813, individual header anchors, current inbound arc links and precise source hashes for each future rewritten paragraph still need mapping.
- Existing `narrative/ARC_SIX.md`, `narrative/README.md`, `wastes/README.md` and `SEASON_TWO.md`/`SEASON_THREE.md` compatibility links remain live. Current arc file name is **legacy**; approved target filename convention `ARC_01.md`–`ARC_11.md` remains **unselected**, and `ARC_SEVEN.md`–`ARC_ELEVEN.md` were absent at Batch 82 audit. **Do not publish links or overwrite legacy routes on a filename guess.**
- **Next Batch 84:** a similarly bounded **read-only L1–200 paragraph mapping** into proposed Arc 10 chapters 1–6, with source-dossier pointers and a preservation ledger, complementing the already measured L185–321 transition. Then work across Arc 11 S3E05–S3E18 in bounded scene groups, before any narrative rewrite. Do not expand D-045 without approval if verified source scenes reveal a genuine boundary conflict.
- For eventual authorized edits: recheck local→MCP→GitHub→Git patch→ZIP at batch start, reread current working hashes/Git status, **archive exact full original narrative first and independently compare bytes**, agree canonical filenames/compatibility, use source-line/hash-to-target mapping and test footnotes/inbound links before modifying any published narrative. Small targeted checks only; full suite by owner/CI.
- **No narrative, places, episode dossier, decisions, source transcript or compatibility files edited in Batch 83.** This is a read-only report and two tracking checkpoints only. GFM/Markdownlint, `git diff --check`, comprehensive incoming-backlink/anchor audit, direct audio verification and complete scene migration **NOT performed**.
