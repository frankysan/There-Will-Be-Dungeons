# Wastes Cleanup — Batch 93: D-045 eleven-arc filename/compatibility decision proposal and E101 migration pilot

**Date:** 2026-10-28. **Status:** DECISION-READY, READ-ONLY PLANNING. **Owner choice required before implementation.** The existing **D-045 owner approval applies to the eleven episode-based arc boundaries**, not new filenames, deletion/replacement of published documents, revised chapters or narrative rewriting. D-047 substantive-scene/uncertain-lore approval and original working-copy preservation rules remain in force. No canonical arc page, compatibility stub, episode, route, world page or decision log is changed by this batch.

## Fresh access / current repository

- Rechecked local mounts at `/local/There Will Be Dungeons Transcripts`, `/mnt/data/There Will Be Dungeons Transcripts`, `/workspace/There Will Be Dungeons Transcripts` and `/workspaces/There Will Be Dungeons Transcripts`: no directly mounted repository. The Keycloak-authenticated **MCP** was responsive. A transient `UNAVAILABLE` while reading `narrative/SEASON_THREE.md` was retried after connection ping and succeeded. GitHub/git-generated patches/ZIP fallbacks not needed for these bounded text reads. Reconsider the **whole priority chain at each file-access batch and on failures**, not only the current MCP status.
- Repository **main**, HEAD **`875625eba95369804be8f3ceba8d46daf4f8d998`**, opening worktree **six visible Wastes changes / zero restricted** (four prior reports Batches91–92, two trackers). The previous UI **"Error in input stream"** interrupted an earlier group of read requests but no Batch93 write existed: checked Git/status and report listing first before continuing. Existing six edits preserved, no reset/commit/push.
- `narrative/` currently has exactly **six published word-form arcs**, `README.md`, `SEASON_TWO.md` and `SEASON_THREE.md`. **No numeric new arc pages exist.** `project/WASTES_CAMPAIGN_CLEANUP_PLAN.md` L65 explicitly calls `ARC_01.md`–`ARC_11.md` an **option**, not an accepted naming decision. `project/DECISIONS.md` D-045 fixes the actual **eleven-arc episode boundaries only**.

## Approval requested — choose the new public filename + legacy path policy

**Recommendation (proposed new decision D-049; NOT yet accepted):**

1. Make **`narrative/ARC_01.md` through `narrative/ARC_11.md`** the eventual canonical eleven-arc filenames. Zero-padding makes natural lexical order unambiguous. In particular, **new `ARC_06.md` is E067–E081, and old `ARC_SIX.md` is S2E01–S3E18**; these are **not** interchangeable. Use D-044 canonical display spellings in new editorial prose without changing historical transcript quotations or stable legacy slugs.
2. **Preserve every existing `narrative/ARC_ONE.md`–`ARC_SIX.md` file as an accessible legacy edition**, retaining its content and original relative URLs, not automatically redirecting, deleting or overwriting it. This maintains known internal incoming links, citations, GitHub file references and long-lived external deep links. Old Arc Six spans **new Arcs 10 and 11** and therefore must **not** be redirected only to one. Keep those legacy files navigable under a clearly identified **"Earlier six-arc edition"** section when the new edition is ready.
3. Leave `narrative/README.md`, `wastes/README.md`, `world/` crosslinks and season stubs unchanged until **all eleven new files are authored, source-backed, validated and accepted**; perform the public reading-index change as one coordinated batch. Retain `narrative/SEASON_TWO.md` and `SEASON_THREE.md` filenames as seasonal navigation. After acceptance, Season Two leads to new **Arc 10**; Season Three leads to **Arc 10 (S3E01–03)** and **Arc 11 (S3E04–18)** while noting that **S3E019** is out-of-game cast commentary.
4. Keep the historical **D-042/D-043 six-arc decisions** intact as evidence. Once approved, add a **new explicit owner decision** to `project/DECISIONS.md` recording the numeric filename contract, immutable legacy files, compatibility behavior, accepted release gate and any eventual alias plan. Do not call this D-049 until the owner confirms and checks that the ID is unused; the identifier is a *candidate*.
5. **Do not interpret filename approval as blanket approval for a full rewrite.** Separate story/scene decisions are subject to D-047 and the paragraph-level preservation/coverage protocol, with ambiguity flagged `[[review-needed:reason]]`. Start by drafting one small and one dense arc in **unpublished files only after appropriate approval**, retaining originals and allowing scene/paragraph conservation testing.

| Current published arc file | Approved new destination arcs | Compatibility rule |
| --- | --- | --- |
| `ARC_ONE.md` | `ARC_01.md`, `ARC_02.md` | Old path remains readable, new arc index holds entry points |
| `ARC_TWO.md` | `ARC_03.md`, `ARC_04.md` | Same |
| `ARC_THREE.md` | `ARC_05.md`, `ARC_06.md` | Same |
| `ARC_FOUR.md` | `ARC_07.md` | Same; final chapter E101 through **completed portal departure** |
| `ARC_FIVE.md` | `ARC_08.md`, `ARC_09.md` | Same; **Arc 08 begins in remainder of E101**, not E102 |
| `ARC_SIX.md` | `ARC_10.md`, `ARC_11.md` | Same; **S2E12 is season end, S3E03 ends Arc10, S3E04 starts Arc11** |

**No approval assumption:** the owner's earlier "Proceed" actions authorize this read-only audit, not automatically the new naming/compatibility contract or actual prose modification. Before implementation ask for explicit acceptance or a specific change.

## Proposed new reader navigation — exact draft shape, NOT written to public files

Once all eleven new arcs exist and pass checks, the guide can present:

```markdown
## The Wastes — Eleven-arc reading edition
[01 · Beginnings in Dusthill](ARC_01.md) · [02 · Chains and Bargains](ARC_02.md) · [03 · Road to a Lost Kingdom](ARC_03.md)
[04 · The Crown of T'ietkalla](ARC_04.md) · [05 · Kings and Consequences](ARC_05.md) · [06 · Beneath the World](ARC_06.md)
[07 · The City of Doors](ARC_07.md) · [08 · Separate Paths](ARC_08.md) · [09 · The Fall of Elhandar](ARC_09.md)
[10 · Across the Stars](ARC_10.md) · [11 · The Last War](ARC_11.md)

The original [six-arc reading edition](ARC_ONE.md) remains available for legacy references.
[Legacy Arc Two](ARC_TWO.md) · [Legacy Arc Three](ARC_THREE.md) · [Legacy Arc Four](ARC_FOUR.md) · [Legacy Arc Five](ARC_FIVE.md) · [Legacy Arc Six](ARC_SIX.md)
```

**Proposed adjacent-link contract:** `ARC_07.md` end can link `[Previous](ARC_06.md) · [Next](ARC_08.md)`; `ARC_08.md` begins with a short, **source-supported** line such as *"E101 continues after Hope's solo departure: the remaining companions regroup at White Tower while Hope follows the Voice toward Kaiser Casino."* New URLs are not inserted anywhere before pages exist.

## The critical E101 original-paragraph disposition pilot

The [exact five-arc SHA/byte-offset ledger](WASTES_CLEANUP_D045_SEASON_ONE_PARAGRAPH_SHA256_LEDGER_91_2026-10-28.md) establishes stable identity for original paragraphs; [Batch92](WASTES_CLEANUP_D045_E101_HANDOFF_AND_SEASON_ONE_LINK_TARGETS_92_2026-10-28.md) checks event timing, footnotes and later-episode dossiers. **Each original source paragraph below is a unique content identity**, and "split" means a **proposed** eventual scene/episode decomposition with source evidence, *not* permission to edit or claim facts outside the dossier.

| Original paragraph ID (file:line) | SHA-256 prefix (full in Batch91 ledger) | D-045 destination and treatment | Evidence / caution |
| --- | --- | --- | --- |
| `ARC_FOUR.md:101` | `f51fb00f2c81` | New Arc 07 ch7, **preceding E100**, not Arc 08 | Open chest, Fist and still-severed Hand; source `[^four-15]` |
| `ARC_FOUR.md:105` | `0532b69f942c` | New Arc 07 ch8, **E101** | Stanley revives; private Hope patron instruction; no settled chest lock |
| `ARC_FOUR.md:107` | `55a4714bb8f3` | New Arc 07 ch8, **E101** | Hope attaches Hand; Eye of Groxl restored; true patron identity unverified |
| `ARC_FOUR.md:109` | `386fbe7837a4` | New Arc 07 ch8, **E101** | Separate glove returned to **open** case; Finger of Death performed |
| `ARC_FOUR.md:111` | `26324605d29a` | New Arc 07 ch8, **E101** | Hope chooses solo departure; demons retreat, not end of Blood War |
| `ARC_FOUR.md:113` | `d66fb6064f9c` | New Arc 07 ch8, **E101** | Stone arch crossed by patron, Hope and Spatulo |
| `ARC_FOUR.md:115` | `6ca10a71da78` | New Arc 07 **final E101 paragraph** | Portal physically closes **~01:57–01:59**; party remains |
| `ARC_FIVE.md:7` | `e6c31a6bb497` | New Arc 08 ch1 **E101 remainder**, with a brief **boundary recap** of Hope's already completed departure rather than second departure | Preserve White Tower disagreement, Nash wounded by separation, Vorel hopeful; **Nash re-locks chest and gives medallion key to Stanley** (in E101 dossier but not fully stated in legacy synopsis) |
| `ARC_FIVE.md:9` | `f9431731035e` | **Split**: E101 mark removal + arrival at Kaiser Casino/host and refusal of binding pact → Arc 08 ch1 E101 tail; necklace + replacement travel ring → **E102 scene** in Arc 08 | Brett's identity/contract claims testimony, **no E101 performed pact** or future-kingdom visit |
| `ARC_FIVE.md:11` | `c2e6a1e46c` | **Split/keep chronological:** first tower emotional aftermath already E101, but Tungan saucer crash, Walnut rescue, Stanley's performed *Modify Memory* on Alentris and actual airship departure → **E102 scene** in Arc 08 | Do not duplicate E101's long rest or claim false recollection is objective history |
| `ARC_FIVE.md:13` | `681a7eabde31` | **Split:** E102 Brett's three helpers + actual portal to royal chambers; E103 Celibus killed and guards fought → separate Arc 08 scenes | Keep Stump's death a played event; don't backdate it to E101 |
| `ARC_FIVE.md:15` | `50a8eeb651f9` | **E103** T'ietkalla residents' reports, patron's demand, station fire, and moon/ship crisis elsewhere | Reports ≠ proven earlier rail attacks; the station is not burned in E101 |
| `ARC_FIVE.md:19–27` | source IDs in Batch91 ledger | Arc 08 **E104–06**, separate later scenes | E107–E109 **historical Dunebreaker** not a chronological gap to invent |

**E101 footer provenance/footnotes:** preserve `ARC_FOUR.md` `[^four-15]` through `[^four-18]`, especially boundary note `[^four-16]` and [E101 dossier](../episodes/E101.md)/[two-ASR audit](E101_ASR_COMPARISON_2026-10-23.md) in `[^four-17]`; preserve `ARC_FIVE.md` `[^five-1]` original scope and `[^five-2]` E101–E103 composite evidence and redistribute note *references* according to performed scenes. Keep `[^five-3]` tied to E104–06 and prequel status. **No footnote IDs or bodies changed here**.

**Source truth and custody:** Hand of Voice actually attached to Hope, **Fist** separate in chest, **key with Stanley at end of E101**, Eye of Groxl in Vorel. The hooded Voice's claims and Asmodeus/Brett's offered alliance are not proven cosmology. Other PCs cannot know Hope's private words until they learn them in play. No reunion or binding Brett pact in E101. Treat E101 as **one counted source dossier** contributing two narrative arcs, without a second episode ID.

## Migration acceptance checks — not yet run

1. **Resolve explicit owner choice** for exact filename pattern, retaining old six files, seasonal stubs and any desired permanent redirects/aliases. Record as a new decision **only after approval**.
2. For every source edit, re-evaluate access priority, check current Git and **archive the exact then-current working-copy source bytes under a new unique `research/legacy/` path before mutation**; separately confirm backup matches original size and SHA-256. Existing committed originals are not a substitute for preserving newer uncommitted working bytes.
3. Produce a complete source → new-scene → new-chapter disposition ledger for **564 unique narrative paragraphs** (217 across old Arcs One–Five plus 347 in old Arc Six) and separately preserve **104 Season One footnote definitions**, original source-note/commentary blocks and original **281 ordinary Markdown link occurrences** (214 Season One + 67 Arc Six). Content can be responsibly summarized when **approved** but every unique event, character choice, provenance and unresolved claim must have an explicit disposition.
4. Maintain accepted D-045 boundaries, including the **E101 split**, **E013.5** supplemental at correct fictional time, one-offs E043/E127, historical E107–09 prequel, **S2E12 season end rather than arc end**, **S3E03→S3E04** transition, S3E18 as final played session, S3E019 as out-of-game commentary.
5. Before reader-index switch, require **all 11 new destination files** exist, Markdown target/anchor/footnote checks pass, source evidence links resolve, old six paths and both season-stub paths still work, and all guide/world navigation updates agree. Audit live URLs, backward source links and older edition discoverability. Run small targeted validation; full tests to owner/CI.
6. Chapter word-count **350–450** is a diagnostic, **not a delete-to-fit command**. D-047 authorial changes and meaning/chronology uncertainty require owner approval or `[[review-needed:reason]]`, not silent confidence. Preserve D-044 spellings in *new* prose and old source text exactly where historical quotes/aliases require it.

## Explicit unresolved approval (no publication in this batch)

> **Do you approve `narrative/ARC_01.md`–`ARC_11.md` as the canonical new filenames, while keeping all six old word-form arc files (and two season stubs) permanently readable for compatibility, with the public guide switched only after all eleven source-backed new arcs are validated?**

Approval of this infrastructure/presentation contract would authorize recording the naming policy, **not** unreviewed narrative rewriting. If the owner prefers a different compatibility approach (e.g. old paths become index pages after archiving exact originals, or a different filename scheme), revise this proposal before writing new arc files.

**Next Batch 94 if approved:** record explicit owner decision in `project/DECISIONS.md` and cleanup plan, then prepare a narrow source-backed draft/retention plan (owner-gated for substantive prose). **If not yet approved**, a read-only chapter-scene coverage/uncertainty matrix for short Arc01 and dense Arc07/Arc10 may continue, but **do not create the public eleven arc pages**.

**No narrative source edit, new public arc, redirect, commit or push in Batch 93.** Full tests, independent audio and rendered GFM/link/backlink validation not claimed.
