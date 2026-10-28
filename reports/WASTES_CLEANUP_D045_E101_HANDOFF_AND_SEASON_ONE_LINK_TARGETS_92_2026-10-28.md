# Wastes Cleanup — Batch 92: Season One target existence and E101 source-to-scene handoff

**Date:** 2026-10-28. **Status:** READ-ONLY AUDIT COMPLETE. D-045 owner-approved arc boundaries are not chapter prose, filenames, route edits or approvals to collapse disputed lore (D-047). **No narrative, episode, world, route, decisions or compatibility source edited.** Source is processed-ASR research, **not independently listened original audio**. Retain exact historical references and D-048 reader-first/source-provenance distinction.

## Live source/access preflight

- Re-evaluated access chain from scratch at batch start: no direct checkout mounted under `/local/There Will Be Dungeons Transcripts`, `/mnt/data/There Will Be Dungeons Transcripts`, `/workspace/There Will Be Dungeons Transcripts` or `/workspaces/There Will Be Dungeons Transcripts`. Authenticated Keycloak **MCP works**; GitHub, generated git patches and ZIP backup not needed for this batch. Re-evaluate at every fresh file-access batch and after failure.
- Branch `main`, HEAD **`875625eba95369804be8f3ceba8d46daf4f8d998`**; starting worktree retained **five existing Batch 91 changes (three reports/two trackers), zero restricted**. Preserve all; no Git stage/commit/push/reset.
- Published `narrative/ARC_FOUR.md` baseline **24,569 bytes, 167 CRLF lines, SHA `428f5e930d4d2e55de3f77f98d0809e9e6db6f3e526d75a4672c9b82be095a39`** and `narrative/ARC_FIVE.md` **28,734 bytes, 177 CRLF lines, SHA `a2dfb834af74f8ad73c95332156ee19419614c30df2d305d53482734f26c8284`**; these exact original source baselines were established and independently hashed in [Batch 91's paragraph ledger](WASTES_CLEANUP_D045_SEASON_ONE_PARAGRAPH_SHA256_LEDGER_91_2026-10-28.md). The current Git status shows **no source edits**.
- Source ledger: [all original Season One link labels and URLs](WASTES_CLEANUP_D045_SEASON_ONE_LINK_HEADING_LEDGER_91_2026-10-28.md); [Batch 91 five-source audit](WASTES_CLEANUP_D045_SEASON_ONE_PREMIGRATION_AUDIT_91_2026-10-28.md).

## Exact link-target existence resolution — the remaining Batch 91 gate is now closed

The five legacy Season One arcs have **214 original ordinary Markdown link occurrences** resolving to **148 unique normalized repository paths**. No outbound URI scheme or anchor fragments were recorded in the original ledgers.

- Read **all 214** occurrence rows L71–284 of the original link ledger in six bounded 40-line windows, verified **148** exact distinct URL strings, normalized each from the old `narrative/` directory and percent-decoded URL path components.
- Enumerated existing repository directory entries using MCP `list_workspace`: `episodes` 199/199 file entries, `narrative` 9/9, `research/legacy/2026-10-23` 5/5, `research/legacy/2026-10-22` 19/19, and partial-but-relevant listings of `world`, `project`, `research/legacy/2026-10-24` and `reports` (maximum per-list limit 200, not full collection). **144 distinct linked file destinations** exactly matched these returned listings.
- **Three remaining linked file paths** were not shown due to truncated directory lists and were verified with independent 1–2-line MCP reads: `project/REVIEW_QUEUE.md`, `reports/E101_ASR_COMPARISON_2026-10-23.md` and `reports/E128_ASR_COMPARISON_2026-10-24.md`. These **three exist and are readable**.
- The last unique link target is **`../episodes/`**, a **directory**, not a Markdown file. Its source occurrences are legacy `ARC_ONE.md` **L137** ("E000–E026 episode dossiers") and `ARC_TWO.md` **L141** ("E027–E054 episode dossiers"). The `episodes/` directory was positively listed with **199 file entries** and therefore exists as a valid repository directory destination, although directory landing rendering/navigation is platform-specific.

**Result: 147/147 original linked file paths exist (144 listed + 3 individually opened), plus 1/1 linked directory exists — all 148/148 unique targets resolved at repository-path level; zero missing.** This is **path existence**, not 147 independent content reads, not rendered GFM/click handling, not semantic link-anchor verification, not external HTTP-bookmark preservation and not all possible incoming backlinks. Original `214` links include **two directory-link occurrences**, so 212 link occurrences refer to files.

Initial attempts at an oversized directory listing (limit 500) were rejected as invalid, and one bulk listing/read operation was safety-blocked; returned to documented per-directory limit **200** plus narrow existing-file reads. **No failures were silently classified as passes.**

## Scene-level preservation map: one E101 recording, two approved arcs

[Played E101 source-first dossier](../episodes/E101.md), [dual-export ASR comparison](E101_ASR_COMPARISON_2026-10-23.md), `narrative/README.md` L46 and `world/CONSISTENCY_LEDGER.md` L608–611 agree that E101 spans *both* the end of legacy Arc Four and the opening of legacy Arc Five. The **owner-approved D-045 split** is enacted **when Hope completes the solo portal departure**, not at E101/E102, the Fist attachment alone, or the season change.

| Original evidence and source paragraph(s) | Recorded event/cutoff | Proposed D-045 destination; preservation obligation |
| --- | --- | --- |
| **`ARC_FOUR.md` L101** | E100 cliffhanger: Vorel exposes Fist + its enclosed severed Hand; does **not** equip gauntlet | **Arc 07 previous chapter/scene**, not E101 relocation. Footnote **[^four-15]** links E097–100 and must stay with its cliffhanger |
| **`ARC_FOUR.md` L105** / E101 dossier L11–12 | Stanley survives natural-20 death save and revives/heals Alentris, Fist/Hand custody contested, only Hope hears instruction | **Arc 07 provisional ch8**, prevent treating unconscious E100 status as death at E101 cutoff or sharing Hope's private patron message with other PCs |
| **`ARC_FOUR.md` L107** / E101 dossier L13–14 | Hope *actually severs her own right hand* and fuses **Hand of the Voice**; patron actually restores **Eye of Groxl** in Vorel | **Arc 07 ch8**, witnessed action versus uncertain patron identity/lore, distinct Hand and separate gauntlet |
| **`ARC_FOUR.md` L109** / E101 dossier L15–16 | Hand powers and Hope's cast **Finger of Death** with undead flier; detached Fist gauntlet goes back to still-open case | **Arc 07 ch8**. Vorel cannot have already locked the chest; chest/key custody changes **later in E101 after departure** |
| **`ARC_FOUR.md` L111** / E101 dossier L17–18 | Hope chooses **to go alone**, sends Vorel back; Orcus-ordered demon retreat/temporary end to coalition, while Blood War continues | **Arc 07 ch8**. Hope's stated desire for godhood is **not achievement**; a general's account of motive remains reported |
| **`ARC_FOUR.md` L113–115** / E101 dossier L19 | Ulvert invitation, Spatulo follows; patron → Hope → Spatulo physically pass through infernal stone gate; **portal actually closes ~01:57–01:59** | **Arc 07 final scene/source boundary**. Nash, Stanley and Vorel remain at White Tower. **One E101 recording**, not duplicated episode count or a fabricated E102 gap |
| **`ARC_FIVE.md` L7** / E101 dossier L23–24 | Postdeparture White Tower companions have different emotions; gauntlet remains separate and **Nash successfully re-locks it in chest**, returns removed medallion **key to Stanley** | **Arc 08 proposed ch1**. L7 prose is a condensed recap; future version must retain these played custody updates and distinguish earlier E100 key-in-lock from final E101 key-with-Stanley |
| **`ARC_FIVE.md` L9, E101 portion only** / E101 dossier L25–27 | The Voice removes visible Prith-linked **mark**; Hope reaches casino and **meets Brett/Asmodeus-claiming host**, **refuses binding pact**; accepts drinking/social evening | **Arc 08 proposed ch1, E101 tail**. NPC claim of cosmic identity/contract freedom not objective proof. **The disguise necklace and replacement Gate ring in the same legacy paragraph occur in E102, not E101**—split source paragraph before target scene allocation |
| **`ARC_FIVE.md` L11** / E102 dossier L7–17 | First White Tower regrouping/locked gauntlet corresponds to **late E101**, but the **Tungan saucer crash, Stanley's performed Modify Memory on Alentris and the escape/airship takeoff occur in E102** | **Arc 08 ch1 may keep both played-episode scenes**, but **do not reassign all of legacy L11 to E101** or duplicate rest as an extra day. Future source-paragraph disposition should be **split by source episode** |
| **`ARC_FIVE.md` L13–15** / E102–103 dossiers | E102 Brett's real henchmen and gate to royal chambers; **E103** Hope actually kills Celibus Stump and later participates in station burning. Other party's Tungan airship confrontation also **E103** | **Arc 08 ch1 and subsequent beats**; **none** is performed during E101 and no E101 source cutoff may include it |
| **`ARC_FIVE.md` L19–27** | E104–106 later tracks: T'ietkalla crisis, Sigil/Tobacho, alternate Nash lead | Arc 08 later proposed chapters; **not part of one-recording E101 handoff**. Existing footnote **[^five-3]** correctly groups E104–106 |

**Important distinction:** the first five Arc Five body paragraphs **combine several played episodes**; the *arc* split is approved but **paragraph-level scene redistribution is still a future editorial decision**. Do not mechanically copy all of L7–15 into an "E101 chapter" or delete story detail to meet the 350–450-word diagnostic.

## Exact transition footnote bodies and source identities

| Footnote identity | Legacy location | Role and mandatory disposition |
| --- | --- | --- |
| `[^four-15]` | `ARC_FOUR.md` L151 | E097–E100 **preceding** evidence; not a played E101 source |
| `[^four-16]` | `ARC_FOUR.md` L153 | Explicit **E101 last-arc scene cutoff ~01:57–01:59** and Arc Five postportal continuation; retain as boundary provenance |
| `[^four-17]` | `ARC_FOUR.md` L155 | Direct E101 dossier and paired ASR report links; retain both |
| `[^four-18]` | `ARC_FOUR.md` L157–161 | Historical pre-consolidation source, out-of-game bonus commentary and unresolved sources; **don't promote bonus material to played scenes** |
| `[^five-1]` | `ARC_FIVE.md` L119–121 | First-scene E101 timestamp, single episode represented twice, separate E107–109 prequel and E128 close; retain scope metadata |
| `[^five-2]` | `ARC_FIVE.md` L123 | **Composite E101 + E102 + E103** original grouped citations; retain all and disaggregate with proper target scenes as needed |
| `[^five-3]` | `ARC_FIVE.md` L125 | E104–106 and E107–109 historical-prequel qualification; **not** source for E101's casino sequence |

Other source linkage: `narrative/README.md` L46 and L65–66, `world/HISTORICAL_EVENTS.md` L24, `world/CONSISTENCY_LEDGER.md` L608–611 and `world/places/white-tower.md` must remain navigable. `E101.md` L3 and L9–27 are the **time-window and semantic primary dossier**; `E102.md` and `E103.md` distinguish the later actions. Do not double-count E101 in the 154 distinct played/intro episode IDs of the accepted crosswalk.

## Fidelity and owner decision gates

- Keep **Hand of the Voice vs Zorander's Fist gauntlet vs floating chest vs medallion key** separate, with performed custody updates; the Hand stays with Hope, gauntlet closed in chest and key with Stanley at the *end* of E101. Eye of Groxl physically restored in Vorel.
- Keep **who hears what**: patron speaks privately to Hope, Vorel sees the Eye restoration, other PCs not privy to unseen instructions. **Asmodeus/Brett**, the Voice patron, old-soul claim and divine goals are source/character claims, not globally verified cosmology.
- Keep **the retreat actually performed** vs only a **one-day armistice**, and ongoing larger Blood War; White Tower not Earth. Keep the separately experienced original party and Spatulo with Hope.
- Do not retroactively move E102's gifts, saucer crash, ship takeoff or Stanley's memory alteration, or E103's T'ietkalla political violence, into E101. Don't count an additional independent long rest just because E102 briefly revisits E101's cutoff.
- D-045 approved new Arc **07 ends** after portal and Arc **08 begins** with the rest of E101. New numeric naming `ARC_01.md`–`ARC_11.md` remains **proposal only**. Old word-form arc files, navigation and source notes stay published and unmodified until filename/compatibility policy and future target chapters are explicitly approved.
- **Before any future actual source mutation**, repeat local→MCP→GitHub→Git-generated patch→ZIP hierarchy, check fresh Git HEAD/worktree, archive exact *then-current working* source file bytes **before edits**, independently verify backup SHA/size, map each source paragraph by content SHA and line to preserved/summarized target scene, handle citations/footnotes and run targeted link checks.
- **Unrun:** audio listening, rendered Markdown/footnote behavior, Markdownlint, `git diff --check`, exhaustive incoming backlinks and external browser bookmark verification, final reader-approved rewritten chapters, full test suite. **No commit/push.**

**Next Batch 93 (suggested):** prepare an explicit eleven-arc filename/legacy compatibility owner decision with a short sample of proposed Arc07→08 reader navigation, plus original-paragraph retention ledger for the E101 composite paragraphs L7–15 and proposed tests. **Stop before creating/rewriting public arc files until owner approval.** This batch made only this research report and cleanup manifest/progress checkpoint updates.
