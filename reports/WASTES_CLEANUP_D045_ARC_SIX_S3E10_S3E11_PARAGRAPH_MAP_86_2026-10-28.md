# Wastes Cleanup — Batch 86: Arc 11 chapter 4 source-to-paragraph audit (S3E10–S3E11)

**Date:** 2026-10-28 (Europe/Stockholm). **Disposition:** READ-ONLY bounded mapping COMPLETE. **No narrative migration, semantic edits, archiving or new canonical chapter filenames.** D-045 arc boundaries are approved; preliminary chapter labels/story beats are not blanket approval for rewriting, truncating scenes, relocating uncertain lore or breaking compatibility under D-047.

## Fresh live source and access preflight

- Re-evaluated priority chain at batch start: no mounted local checkout at `/local/There Will Be Dungeons Transcripts`, `/mnt/data/There Will Be Dungeons Transcripts`, `/workspace/There Will Be Dungeons Transcripts`, `/workspaces/There Will Be Dungeons Transcripts`; Keycloak OAuth workspace **MCP connected**. GitHub, Git-generated patches and ZIP fallbacks not needed. Re-evaluate the entire order at each new batch of file access and on any failure.
- Repository `There Will Be Dungeons Transcripts`, branch `main`, HEAD **`02e35be895c72260d3c0ebc8ef402ef361d90206`**. Opening Git status **5 visible pre-existing changes / 0 restricted entries** (three prior read-only reports and two tracked progress files). Preserved, no reset, staging, commit or push.
- Published source `narrative/ARC_SIX.md` **813 numbered lines / 206,128 bytes**, SHA-256 **`44e8b30073d3d95a93b449783de11c7cafac1e74473c2ea082ce7e68b1ee541d`**, **unchanged**. The source range L483–560 was read in contiguous numbered views; **78/78 lines available**, no gap. First inspected through L722 for subsequent headings but **detailed mapping here stops at S3E11**. S3E12 begins L561 and is deliberately not prematurely assigned to chapter 4.
- [Approved eleven-arc map](../project/WASTES_NARRATIVE_CHAPTER_MAPS.md) L157–166: **Arc 11 / proposed chapter 4 = S3E10–S3E11**; chapter 5 = S3E12–S3E13. Prior [Batch 85](WASTES_CLEANUP_D045_ARC_SIX_ARC11_OPENING_PARAGRAPH_MAP_85_2026-10-28.md) mapped S3E05–S3E09 L321–482, **72 paragraphs/~6,750 words**, and Batch 83 mapped S3E04 15 paragraphs/~1,410 words. **No final chapter filename scheme has been chosen.**

## Complete paragraph-to-episode allocation (source original line IDs)

**Method:** Each original numbered nonempty prose paragraph is counted once. The `###` heading and the separately attached final citation/provenance line are inventoried but **excluded from prose count**. Words are whitespace-separated Markdown source tokens, approximate—not edited or rendered word counts. Stable content hashes still needed before any source transformation.

| Approved destination | Legacy episode section and original heading | Exact original span | All prose paragraph starting line IDs | Paragraphs | Approx. words |
| --- | --- | --- | --- | ---: | ---: |
| **Arc 11 / proposed ch 4** | **S3E10 — Stomping Grounds**, `### Stomping grounds` L483 | **L483–524** | **485, 487, 489, 491, 493, 495, 497, 499, 501, 503, 505, 507, 509, 511, 513, 515, 517, 519, 521** | **19** | **1,665** |
| **Arc 11 / proposed ch 4** | **S3E11 — Two Wrongs**, `### Two wrongs` L525 | **L525–560** | **527, 529, 531, 533, 535, 537, 539, 541, 543, 545, 547, 549, 551, 553, 555, 557** | **16** | **1,503** |
| **TOTAL** | **2 played episodes, not a newly resolved war** | **78/78 consecutive source lines** | **35 unique original prose/status paragraph IDs** | **35** | **3,168** |

**Episode source-note retention:** L523 is `[Played S3E10 dossier](../episodes/S3E10.md) · [complete-export P/Q audit](../reports/WASTES_S3E10_ASR_COMPARISON_2026-10-27.md)` with ASR-only qualification. L559 is `[Played S3E11 dossier](../episodes/S3E11.md) · [exact P/Q text audit](../reports/WASTES_S3E11_ASR_COMPARISON_2026-10-27.md)`. **All four link destinations were independently opened by binary metadata reads; no missing target.** These source notes are not optional scene paragraphs and must remain with the corresponding episode records during a future migration. No new source/citation links were inserted in the legacy narrative.

## Primary evidence checked (processed ASR dossiers; original audio NOT listened to)

| Current linked file | Size (bytes) | SHA-256 |
| --- | ---: | --- |
| `episodes/S3E10.md` | 16,839 | `8853d9a2ac1d7c462c312377a8324669b614072b5789d456b0af43fca44e2867` |
| `episodes/S3E11.md` | 15,504 | `ded2d7d7418dff4e6e2f30e6d902269a2668b86f66ca30ddac217d0623432726` |
| `reports/WASTES_S3E10_ASR_COMPARISON_2026-10-27.md` | 9,655 | `bd101fcc87ec4bbac5a537f5df335bfdae3b22551df37ef5062b037619461aa3` |
| `reports/WASTES_S3E11_ASR_COMPARISON_2026-10-27.md` | 10,159 | `c3f20908a1e564a6f0a6de178ce892d4d8307ab34483ac014579d8a86a8a6ddd` |
| `episodes/S3E12.md` (next-boundary confirmation) | 17,646 | `3a67d8989bc8cf18ec785ed2b2c802d92f1f8b80fcb77902885eb1772d02b938` |

The dossiers were read in bounded numbered windows to compare chronology, custody/identity claims and actual played events. Agreement between multiple processed transcripts is **not independent original-audio verification**.

## Scene-level retention and uncertainty safeguards

**S3E10 — descent, childhood trauma, the living door (L483–524):**
- **L485–495:** Actual freight-elevator descent from Walmart, scouting with `Message`, two mine-cart tracks, Hope operating the spare cart and the short rest. The GM **explicitly confirms Ruby is now with the descending party**; earlier S3E09 last-visible Ruby with surface allies is a time-limited record, not a reason to invent an on-screen pickup or specific permanent custodian. Device is **not installed/activated**; GM describes what it *will* do if inserted at hottest point.
- **L497–507:** Six worker-cage chambers contain many slaughtered people, but perpetrator/precise time and exact total remain uncertain. Nash revisits the site of actual childhood abuse. His former masked teacher **is physically killed by Stanley**; Nash takes the **Fury Road VHS cassette**, not VCR; childhood torture and the cell's relics are direct witnessed acts and memories, not newly discovered reliable written laboratory records.
- **L509–521:** Three Kuromokishi guards accept Nash's **fake Principal voice** before Vorel/Stanley initiate combat; avoid attributing the deception to the real Principal. Heat conduit, living embedded heads and encounter with **Hope's father** culminate at the **Empty Chamber door**. Hope ends her father's animated suffering, but do not imply permanent recovery, an identified soul destination or resolution of all victims' fates. The Principal **has not yet been physically met** by the S3E10 cutoff; the Ruby remains unplaced.
- The source uses legacy spelling `Principle` in older prose. **D-044 canonical display is “The Principal”**, but these historical original paragraphs are unedited in this read-only batch. Do not rename compatibility slugs or silently revise source quotations.

**S3E11 — chamber, conditional truce, Château Weir (L525–560):**
- **L527–533:** Living Door Authority door **actually opens** after reporting fines paid; rumored Dorothy debt/romance and who paid are door testimony, not independently verified history. Main Nash and party cross the lava bridge and encounter the **Principal and four chanting Dragonsons** in the subterranean chamber. His assertions about engineering Nash, fatherhood, repeated realities and origin of Weir/Worldbreaker are **self-interested NPC testimony**, not objective exposition. The **fully built Ruby is present with the party in the chamber but not inserted**.
- **L535–541:** Hope proposes a **strict temporary cessation of fighting** to face the Soulbroker first, not surrender or permanent alliance. Terms include no contact with surface allies before the meeting and allow conflict to resume after. Vorel remains morally opposed, and Stanley explicitly wrestles with apparent betrayal of fallen allies. An actual eight-hour long rest is taken; **no rejuvenation syringe used**.
- **L543–547:** Nana Truffled arrives, supplies food and comforting memory; her claimed parental/teacher history is NPC testimony. Stanley **casts a new *Heroes' Feast*** using the **second and last** costly bowl; don't imply old feast remained active forever. Principal gives Hope a charged modified **Gate ring**, and Hope **actually opens passage to Château Weir's courtyard**; all four heroes and the Principal cross. This ring must not be confused with the Mask of Eltanfawr, ordinary teleport rings or the stolen Hand itself.
- **L549–557:** In Château Weir, Quizquaz returns **without demonstrated resurrection** and confronts **three** old pact signers; **Vorel did not sign**. Stanley sits on the throne as an affront, **not coronation**. Soulbroker appears and disputes Principal, claims he **could** remove Worldbreaker but **does not do so**. Both villains' theories of Weir history and early humans are attributed, not accepted as fact. Vorel calls himself Contractless/Defender of Earth. **S3E11 closes with Soulbroker transforming and the château collapsing into a cyclone**, *not* an already adjudicated victory or portal escape.
- **S3E12 source boundary:** `### Too many of them` starts **L561**; [played S3E12](../episodes/S3E12.md) first carries the real cyclone battle and Soulbroker's physical defeat. **No S3E12 paragraphs are placed in chapter 4.**

## Density, total coverage and remaining work

This prospective single Chapter 4 has **35 paragraphs / ~3,168 source words**, well beyond the historic ~350–450-word *diagnostic*; do **not** automatically delete emotional beats, Hope's father, Nash's childhood scenes, the party's ethical dilemma or the two separate antagonists to meet a cap. D-045 approves arc episode ranges, not compulsory one-episode/one-heading structure or a seven-paragraph rewrite.

Measured Arc 11 paragraph mapping through S3E11 now includes **S3E04** 15/~1,410 (Batch83), **S3E05–09** 72/~6,750 (Batch85), **S3E10–11** **35/~3,168** (this batch), **total 122 source prose/status paragraphs / ~11,328 words**. The rest of published Arc Six **L561–805 (S3E12–S3E18)** and global source footnotes/audit near **L807–813** still require paragraph and semantic mapping. All source files remain published unchanged.

**Next Batch 87:** Re-evaluate full access priority and Git. Read a bounded, complete-episode source range starting **L561** for **S3E12–S3E13** (approved Arc 11 candidate chapter 5) with complete paragraph ID ledger, note/link destinations, meaningful scene/custody and uncertainty checks; don't stop in the middle of an episode. Later map S3E14–18 and source footers. Before any actual source mutation require a fresh byte-exact archived working original, SHA verification, target naming/compatibility design and approvals where substantive narration changes. No stage/commit/push or full suite; GFM rendering, Markdownlint, `git diff --check`, all backlinks and independent original audio remain outstanding.

**This Batch 86 changes only its new report and the two tracker checkpoints. No narrative/episode/places/wiki/character source files edited.**
