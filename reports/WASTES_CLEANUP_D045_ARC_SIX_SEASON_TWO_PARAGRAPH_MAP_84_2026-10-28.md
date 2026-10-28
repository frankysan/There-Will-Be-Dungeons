# Wastes Cleanup — Batch 84: legacy Arc Six Season Two paragraph map into approved Arc 10 chapters 1–6

**Date:** 2026-10-28 (Europe/Stockholm). **Status:** READ-ONLY pilot of complete source L1–200, no source mutations, no arc migration or invented headings. Owner-approved **D-045** concerns the eleven **arc episode boundaries**, not automatically approved chapter names, arbitrary compression, old-path removal, or source-free recasting. **D-047** stops unapproved meaning-changing scene/identity edits.

## Access, live source and scope

- Re-evaluated file-access chain: local checkout absent at `/local/There Will Be Dungeons Transcripts`, `/mnt/data/There Will Be Dungeons Transcripts`, `/workspace/There Will Be Dungeons Transcripts`, `/workspaces/There Will Be Dungeons Transcripts`; Keycloak-authenticated **workspace MCP connected**; GitHub, Git-generated patches and ZIP not needed. One overbroad S2E11 dossier read was safety-rejected; a **narrow, numbered L1–3** read and independent binary metadata read succeeded, demonstrating safe bounded fallback. Reevaluate hierarchy again at each new access batch and after failures.
- Live repository `There Will Be Dungeons Transcripts`, branch **`main`**, HEAD **`02e35be895c72260d3c0ebc8ef402ef361d90206`**, **three pre-existing Wastes Batch 83 worktree changes**, zero restricted. No reset, stage, commit or push.
- Exact **unmodified** `narrative/ARC_SIX.md`: **813 numbered lines / 206,128 bytes**, SHA-256 **`44e8b30073d3d95a93b449783de11c7cafac1e74473c2ea082ce7e68b1ee541d`**. Source L1–200 fully retrieved in **three contiguous independent line windows L1–80, L81–160, L161–200**: **200/200 lines, no gaps**. Page contains **14 Season Two scene headings** covering **12 played episodes**, plus one H1 and a season heading. Current narrative file is published legacy Arc Six; it is not yet split.
- **D-045 approved Arc 10** episode scope: S2E01–S2E12 plus S3E01–S3E03; **D-045 approved Arc 11** begins S3E04. The approved chapter map proposes Arc 10 chapters 1–6 corresponding to paired Season Two episodes and chapter 7 for first three S3 episodes, but **chapter beat summaries themselves remain preliminary**. [Batch 83 boundary inventory](WASTES_CLEANUP_D045_ARC_SIX_PARAGRAPH_PILOT_83_2026-10-28.md) already maps L185–321.

## Crucial correction: scene headings are NOT one episode apiece

There are **14** scene-level `###` headings for **12** actual played episodes. In particular, S2E01's Villa/Fate Six transformation occupies **L9–16** and S2E02's ghost crew, first flight, Mars arrival and family/council approach span **three section headings at L17, L23 and L31**; the title **“Enemy Mine” at L43** begins S2E03, while **“Captain Confusion” at L59** starts S2E04. An automated heading-count = episode-count approach would wrongly misplace everything after L17. Source dossier titles and S2E02-to-S2E03 continuity resolved the mapping; the completed chronological episode sequence after L43 is one heading per played episode through `Dust to Dust` S2E12 L185. No season or new-arc break occurs after S2E12.

## Complete source-paragraph allocation — provisional chapter destinations, not rewritten prose

Original **numbered Markdown source line IDs** serve as provisional paragraph identities; stable content hashes must be made before any future rewrite. Word counts are whitespace-separated source tokens, **including Markdown emphasis syntax**, excluding headings/blank lines and the L3/L5 editorial introduction. All source-line IDs below are preserved rather than invented future IDs.

| Approved Arc 10 chapter proposal | Played episode and old heading(s), lines | Original paragraph line IDs | Paragraphs | Approx. source words |
| --- | --- | --- | ---: | ---: |
| **Ch 1 — Wreckage and ship** | **S2E01** `Four days in the wreckage` **L9–16** | **11, 13, 15** | 3 | 231 |
| **Ch 1 — Wreckage and ship** | **S2E02** `The ship that remembers` L17–22, `Earth beneath the sails` L23–30, `A home on Mars` L31–42 | **19, 21, 25, 27, 29, 33, 35, 37, 39, 41** | 10 | 687 |
| **Ch 2 — Council and new routes** | **S2E03** `Enemy Mine` L43–58 | **45, 47, 49, 51, 53, 55, 57** | 7 | 591 |
| **Ch 2 — Council and new routes** | **S2E04** `Captain Confusion` L59–72 | **61, 63, 65, 67, 69, 71** | 6 | 575 |
| **Ch 3 — Tower Nash and Burp** | **S2E05** `That's What The Blob Said` L73–90 | **75, 77, 79, 81, 83, 85, 87, 89** | 8 | 775 |
| **Ch 3 — Tower Nash and Burp** | **S2E06** `Schrödinger's Nash` L91–106 | **93, 95, 97, 99, 101, 103, 105** | 7 | 537 |
| **Ch 4 — Journey to Pentel Weiss** | **S2E07** `Brace for Impact` L107–126 | **109, 111, 113, 115, 117, 119, 121, 123, 125** | 9 | 730 |
| **Ch 4 — Journey to Pentel Weiss** | **S2E08** `No Magic Allowed` L127–142 | **129, 131, 133, 135, 137, 139, 141** | 7 | 701 |
| **Ch 5 — The prison rescue** | **S2E09** `The Call of Meats is Strong` L143–154 | **145, 147, 149, 151, 153** | 5 | 613 |
| **Ch 5 — The prison rescue** | **S2E10** `Big Mouthful of Carpet` L155–166 | **157, 159, 161, 163, 165** | 5 | 574 |
| **Ch 6 — Crypt and escape** | **S2E11** `Flesh Sauce` L167–184 | **169, 171, 173, 175, 177, 179, 181, 183** | 8 | 790 |
| **Ch 6 — Crypt and escape** | **S2E12** `Dust to Dust` L185–200 | **187, 189, 191, 193, 195, 197, 199** | 7 | 632 |

**Measured cumulative target chapters:**

| Arc 10 proposed chapter | Existing legacy source lines | Source paragraphs | Source words |
| --- | --- | ---: | ---: |
| **1** | **L9–42** | **13** | **918** |
| **2** | **L43–72** | **13** | **1,166** |
| **3** | **L73–106** | **15** | **1,312** |
| **4** | **L107–142** | **16** | **1,431** |
| **5** | **L143–166** | **10** | **1,187** |
| **6** | **L167–200** | **15** | **1,422** |
| **TOTAL** | **L9–200, 192 numbered lines** | **82 original paragraphs** | **7,436** |

**Introductory/editorial L1–8 is not a played scene**: H1 L1, current status/source/campaign endpoint L3 and ASR caveat L5, Season Two heading L7. Preserve those links, notes and date-specific scope as source/compatibility metadata, not as new Arc 10/ch1 narrative. There are **8 Markdown link occurrences in original L1–200**, but **zero inline Markdown link occurrences in the 82 mapped played-scene paragraphs**; links are in the intro or season-final status/editorial material. Citation destinations must be explicitly verified/migrated later; do **not** claim each original paragraph already carries its own evidence link. L199 states the **Season Two ending only**, not the story/arc ending; any future rewritten notes should preserve that qualification. Prior Batch83's L185–200 inventory overlaps intentionally and gives identical **7 paragraphs/~632 words** for S2E12.

## Checked played-dossier roster / provenance

Each corresponding **`episodes/S2E01.md` through `episodes/S2E12.md`** was independently opened or inspected by bounded reads; binary file existence, size and SHA were checked **12/12**. Sources are **processed-ASR episode dossiers, not independent listening to audio**:

| Episode | Current bytes | SHA-256 |
| --- | ---: | --- |
| S2E01 | 14,323 | `dd13e97b23b4aa11cf8cbfab4d095b3775a55313aae6198bb09442ebc85f9578` |
| S2E02 | 18,464 | `679041de5b6abcc2867b8fa90f793ebb3cafb128293fbb8f96b9ad298295181b` |
| S2E03 | 9,528 | `3c444d3a53b1f112a853ea1f98975dbf1fa09d99e2681872020ade817eaf9c37` |
| S2E04 | 12,613 | `820c6e54526ba8577ce9cd7f4bda6cf72156dfad44eb4c8fcde4ecdfcd373547` |
| S2E05 | 11,772 | `6d719d73df27eea6bc0c02ccd84f1d8778297750751d48b58d21469720a4f2a5` |
| S2E06 | 8,637 | `842976b618cc47129a450f16cb630fbb7e0d57ebb55f0f010d20a7edf2527329` |
| S2E07 | 11,316 | `c61144795a20c9d9e603b013e13e611368d0fc4cd0db214420212f354a921157` |
| S2E08 | 12,661 | `8d7cdfbbafb2292678bf2823d2e66572654dea401652858654f6df9336b2d4f8` |
| S2E09 | 13,863 | `635b833d6eba7cb0bbaec410ec04715c08c87b7d8d7498ab148a69c4bfbf8232` |
| S2E10 | 13,196 | `55fc5982c80abd8abfe09799af37a6cb9836aad060439698f9e985eb7d92562b` |
| S2E11 | 16,391 | `358a9bb08a3993993a0b658e5c13d4733af23f98e2f8362e8d319fcf86e7a293` |
| S2E12 | 16,590 | `9ef4ea50c1a76aaa49c434648f9d5c490d57ac6e81abb025dbffec66a402e86d` |

## Retention and uncertainty safeguards for later scene migration

**Ch 1 / S2E01–02:** Preserve Elhandar wreckage, four-day delay at the villa and ship transformation, the ghost crew and uncle Sever, Delit Or'Nath's reported essence, maiden voyage and reunion with family on Mars. **Do not** apply later Fate Six destruction/reconstitution or fully finished Ruby backward to these episodes; treat vessel history as episode-scoped.

**Ch 2 / S2E03–04:** Preserve Mars council's attribution of ancient dangers as testimony rather than authenticated prehistory, Solar Mines/Nash's guarded early memories, coalition choices and Stanley's actual Selle Prime election/transformation. Keep original/Nash alternate selves and alternate Tedna distinct; the group may consult Tower Nash, but alternate people are not replacement original party members.

**Ch 3 / S2E05–06:** Preserve herald's **claims** about Chronos/time separately from confirmed presence, the sandburger interlude, Blast Belly Rock/Burp bank robbery/investigation, stat-damaging blobs, coordinates/Tungsten clue and actual freeing of captives/orc surrender. Do not infer exact final bank contract meaning or backdate eventual Tungsten rescue to S2E06.

**Ch 4 / S2E07–08:** Preserve actual journey across charged nebula and entrance to Pentel Weiss, prohibition of magic in intake, separate fate of Badass T after shaft jump and later recovery. Keep warden-as-Eye and other supernatural attributions **uncertain**, distinguish a planned prison rescue from one already played, and do not conflate S2E08 into S2E09.

**Ch 5 / S2E09–10:** Preserve the actual werefolk confrontation, distinct rescued/still captive characters, finding Tungsten Wheel and Union and navigating threatening corridors. Preserve the crypt entrance as a later step; don't borrow S2E12 escape or future inventor work.

**Ch 6 / S2E11–12:** Preserve deceptive psychic/idealized visions versus waking-world perception, Stanley's performed song, ring and lich confrontation, Nash's disintegration/dragon-metal survival, return to Fate Six with Tungsten rescued, and S2E12 as **season finale only**. S3E01 `Regenerate` is a later act; **not** part of these scenes. The next scene in the *same approved Arc 10* begins at legacy L205.

**Density / approval gate:** All six candidate chapter allocations exceed the existing ~350–450-word diagnostic (**918, 1,166, 1,312, 1,431, 1,187, 1,422** words). These are **source-prose volumes**, not requirements to delete 60–75% of remembered events; future chapters may need more scenes, exceptional length or owner-approved microchapter design. D-045's **arc boundaries are fixed**, but the preliminary seven chapter grouping inside Arc 10 is **not final authoring approval**. No 'automatic 400-word compression' or manuscript rewrite.

## Completeness, open constraints and next task

- Batch83's **Arc 10/ch7** mapping (S3E01–03, old L205–283, 34 paragraphs/~3,017 words) and **Arc 11/ch1** mapping (S3E04 L285–319, 15 paragraphs/~1,410 words) combine with this batch to provide the **entire proposed Arc 10** at **116 legacy source paragraphs / ~10,453 source words** **excluding L1–8 intro, L201–204 season boundary metadata, blank/headings and source footer L807–813**. The numeric totals use Batch83's same whitespace-token convention but still need verified global unique paragraph hashes and source footer migration.
- **Arc 11 from S3E05** begins at legacy heading **L321**. Its S3E05–S3E18 scene paragraphs through L805 remain **structurally inventoried by headings only**, not fully mapped to unique target chapters or sources; source footer/citations **L805–813**, inbound narrative links and legacy compatibility stubs need subsequent checks.
- **Next Batch85:** Read-only first bounded chunk of **Arc 11 S3E05–S3E18** (recommend legacy `ARC_SIX.md` L321–~450) to inventory paragraphs and scene/episode boundaries and compare played dossiers, keeping S3E18 distinct from nonplayed S3E019. Do not publish new arc files, invent chapter titles, rename paths, or rewrite scenes without preservation and owner approval.
- **No source edits or source archiving** in this read-only batch: new journal and one manifest/progress pointer each only. No commit, push, stage or reset. Rendered GFM, Markdownlint, `git diff --check`, complete incoming links, audio and broad test suite **unrun**.
