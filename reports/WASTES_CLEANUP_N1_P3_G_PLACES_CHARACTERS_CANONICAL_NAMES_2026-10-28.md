# The Wastes — N1-P3-G bounded places and characters name cleanup

**Date:** 2026-10-28 (Europe/Stockholm). **Authorization:** D-047 permits small nonsemantic spelling/display corrections without repeat owner approval, grounded in D-044 established spellings **The Principal**, **Khaervilon**, **T'ietkalla**. No D-045 arc migration, D-046 Races schema, disputed identity or other substantive material changes are authorized.

**Initial Git:** `There Will Be Dungeons Transcripts`, `main`, HEAD `7f331552a7c87172a18a9b165f258f4b1c036f38`; 228 visible working changes and 65 restricted entries omitted at initial inspection. Previous Wastes and concurrent Delvers work protected; no commit/push. The live repo is accessible via workspace MCP; direct local checkout not mounted.

## Fixed seven-article microbatch (full source read completed before edits)

All **200/200 numbered lines** read gaplessly; complete source bytes and original SHA-256 checked before defining precise line scope. Proposed corrections: **29 canonical-name updates on 22 original lines**, with **108 existing Markdown destination URLs** and zero footnote tokens to protect. Exactly one editorial dual-name label is expanded without deleting old aliases.

| Original article | Pre-edit SHA-256 | Lines / Markdown links | Exact line numbers | Display fixes | Format |
| --- | --- | --- | --- | ---: | --- |
| `world/places/razak-val.md` | `bb23b12796ce77e8a0b7a599b66f43d8f3263c6e3ceb79988f15bebc7c0c1071` | 58 / 30 | 7, 23, 33, 43 | 6 | LF |
| `world/places/the-harbor.md` | `146c5ec1f46cd903af9a2b604d2dae031f581b65ca07a30f56d3ba45ab9ead3f` | 39 / 17 | 3, 19, 21, 27, 33 | 5 | CRLF |
| `world/places/villa-ornath.md` | `231ac0654bfaf4763ef04d7bf64f0826979760c607aab25ee7cb880da1bbdb0e` | 35 / 16 | 29 | 1 | LF |
| `world/characters/emenil.md` | `234d8b5decae48b1a9104b0a66e68b55368789bef5bad3abafca06466e29c5f3` | 29 / 19 | 7, 13, 17, 19 | 5 | CRLF |
| `world/characters/buttons.md` | `cd39099634f2ac895ad1b725e7970bf158e26cf596f6ee675a299329ca1fca03` | 21 / 15 | 5, 19, 21 | 4 | CRLF |
| `world/characters/dick-pendleton.md` | `7db6728d6b2458b66e25902237b614fdb1e95ee642aef68fe6679499cedeb5a4` | 11 / 5 | 7, 11 | 4 | LF |
| `world/characters/kefeli.md` | `93516675b6bd8a2dd42a74619b943482b5ecd274d558eb496f1e64801fe21c68` | 7 / 6 | 3, 5, 7 | 4 | LF |
| **TOTAL** | | **200 / 108** | **22 lines** | **29** | |

**Referent and source boundaries:** In Razak Val, the live old dual variant `**Kervalon/Kaer Valon**` becomes `**Khaervilon (formerly Kervalon/Kaer Valon)**`: preserve both historical aliases while preferring map canonical spelling, plus normalize five reader-facing Tietkalla uses. In Emenil the description of a `Principal-backed` chancellor remains **Emenil's report**, not an established link. In Dick Pendleton the villain-parentage assertion remains **hostile testimony**, not proven lineage. Buttons' death/court account remains distinct; Kefeli's *own* orthography remains unresolved, only the written city name changes. Villa Or'Nath, the Harbor's founding and Razak Val's succession/travel do not get new interpretations. Old path slugs and all URLs, direct quotes, episode references, labels unrelated to these names and original ASR unchanged.

**Required execution:** First create this journal, then separately create seven byte-identical original archives in `research/legacy/`, verify every SHA-256/size before editing. Check current source hash again; perform guarded unique line replacements on only the listed lines, preserving aliases on Razak Val line 43. Re-read full edited and original bytes to assert exact line change sets, 200/200 source lines, 108/108 identical ordered Markdown destinations, footnote tokens and LF/CRLF formats. Record final hashes and checkpoint in manifest and progress once. No commits/pushes.

**Unrun unless separately available:** Markdownlint, `git diff --check`, actual Markdown target/fragment/backlink checks, original audio/source listening.

## Completed N1-P3-G change ledger

**Checkpoint 0 — PASS:** D-047 scope recorded before any source mutation; all seven live files SHA-256 matched their reported baselines, and **all seven original working copies** were created and independently verified byte-for-byte under `research/legacy/{RAZAK_VAL,THE_HARBOR,VILLA_ORNATH,EMENIL,BUTTONS,DICK_PENDLETON,KEFELI}_PRE_N1_P3_G_2026-10-28.md`. Matching SHA-256 and byte sizes include original CRLF/LF formats; no edit occurred before archival verification.

| Original file | Exact modified original lines | Verified spelling corrections | Post-edit SHA-256 |
| --- | --- | ---: | --- |
| `world/places/razak-val.md` | 7, 23, 33, 43 | 6 | `6d16a5b8c182ca41c26d3e0a63430d563e45fc61fb2e838a615e8d6b9ddbdc2c` |
| `world/places/the-harbor.md` | 3, 19, 21, 27, 33 | 5 | `a4ae4c0f44555cc434e5f95a154f2c03f6bfb40b7d0284083a625b2c34366824` |
| `world/places/villa-ornath.md` | 29 | 1 | `2b10231bff00ee3b1af8be47d993587e66f3b9077a45fbd8607538ec3f473007` |
| `world/characters/emenil.md` | 7, 13, 17, 19 | 5 | `139251bbb0eb7d7deeb89c959d2e3a5ed7d00ac2c50973d8eb93614f7ba042b4` |
| `world/characters/buttons.md` | 5, 19, 21 | 4 | `5bf5a7d04af0107b595b6b17af2e36d7f5abe3f89ff08744939dc30a1f0ae846` |
| `world/characters/dick-pendleton.md` | 7, 11 | 4 | `9dccbf820cd2eb9b0dee3cd0d8d018d7698e13875148b9b2931676bef87dc8dc` |
| `world/characters/kefeli.md` | 3, 5, 7 | 4 | `95ea9329bbe3122488c494e41be0fb27d624f1145bc15dc36cef448121778e39` |

**Checkpoint 1 — PASS:** 22 guarded unique-context source line replacements applied; exactly 29 written proper-name improvements. In Razak Val line 43 only, the historical double spelling was normalized to `**Khaervilon (formerly Kervalon/Kaer Valon)**`, without erasing historical forms; all other edited lines are literal `Principle`→`Principal`, `PRINCIPLE`→`PRINCIPAL`, `Tietkalla`→`T'ietkalla` substitutions. All provenance, playable event facts, quotations, epistemic qualifiers, location IDs, file slugs and original Markdown targets left unchanged.

**Checkpoint 2 — PASS:** Independent all-seven complete source-vs-archive binary comparison verified **200/200 original numbered source lines**, exactly **22/22 specified changed original lines**, exactly **29/29 canonical-name updates**, **108/108 identical ordered Markdown link destinations**, all original footnote tokens (zero), and unchanged original LF/CRLF counts for each file. No other source lines differ. Observed changes in place labels and historical-name introduction do not change the cited story outcomes.

**Checkpoint 3 — CLOSED:** Exactly one N1-P3-G completion checkpoint appended to `project/WASTES_CLEANUP_MANIFEST.md` (line 203) and one to `project/WASTES_CLEANUP_PROGRESS.md` (line 129); both reread and confirmed. Final workspace Git status checked: `main`, unchanged HEAD `7f331552a7c87172a18a9b165f258f4b1c036f38`, **243 visible changes and 65 restricted entries omitted**, including independent concurrent project work. This N1-P3-G pass touched only the seven listed source articles, their seven byte-identical pre-edit archives, this execution journal and two Wastes progress records. No commit/push. **Next:** N1-P3-H referent-aware character articles beginning Nash Maggard and Vorel titles, with bounded D-047 edits; do not conflate identity claims or interpret old quoted source variants as errors. **Unrun:** full `git diff --check`, Markdownlint, true Markdown target/fragment/backlink checks and audio listening. C1, D-045 A1 and D-046 R1 remain substantive owner decision gates.
