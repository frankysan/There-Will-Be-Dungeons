# Wastes cleanup — Batch 98: approved Chapter III chronology and data-core repair

**Date:** 2026-10-28 (Europe/Stockholm). **Execution checkpoint: approved bounded edit complete; static validation passed; draft remains unpublished and not independently audio-verified.**

## Authorization and exact scope

The owner explicitly approved: **“Proceed with Batch 98: correct the Arc 01 Chapter III chronology and restore the C4N-D13 data-core handoff. Preserve originals, Arc 07, and public navigation.”** This authorization permits one source-backed substantive rewrite confined to **`narrative/ARC_01.md`, Chapter III**. It does *not* permit changes to historic `ARC_ONE.md`–`ARC_SIX.md`, `narrative/ARC_07.md` or its partial draft, season stubs, public reading guides, world/episode/source records, or other story episodes. D-045/047/048/049 remain in effect.

**Repository preflight:** `There Will Be Dungeons Transcripts`, branch `main`, HEAD `571d1d372906a99d1cb79fe565007f929e025351`. Five inherited Batch97 working-tree changes (new report, two historical tracker backups, two modified trackers), zero restricted. Direct local repository mount probes failed; Keycloak workspace MCP connected. Re-evaluate full local → MCP → GitHub → patch → ZIP access order for each separate file access batch and after failures; never reset/replay inherited work.

**Precise target input:** `narrative/ARC_01.md` size 14,712 UTF-8 bytes, SHA-256 `3ed8463af7a316c461d556ff8c535a56d659ff2d50bb3e07e3a891ef38b465e5`, established by current MCP metadata and Batch96. Source evidence is `episodes/E005.md` and `episodes/E006.md` (processed ASR, no independent audio listening), and [Batch97 review](WASTES_CLEANUP_D045_DRAFT_FIDELITY_REVIEW_97_2026-10-28.md). Existing six chapters, seven footnote IDs, all links and old Arc01 17/17 paragraph provenance must be retained.

## Expected factual chronology and custody

E005: Peter's earlier claims, goblin raid, losses and Bruce Bane. E006 time-sliced played events:

1. **00:24–00:26:** Nash directly confirms flow by opening the Dusthill surface water valve, distinct from the E005 engine restart.
2. **00:32–00:45:** Vorel tracks goblins and captures a stray goblin who treats him as a lizard king; this is not consensual equal recruitment.
3. **00:45–01:06:** Stanley visits Jenjen, former guard Thomas's widow; Aaron and another ambush Stanley, who kills Aaron while fighting.
4. **01:08–01:18:** Vorel and Hope attend to the captured goblin at Jimster's garage; the goblin identifies himself as **Bok Bok**.
5. **01:19–01:52:** the *following morning's* public meeting, Shun'ti's interim-townmaster offer, defenses, trade and search, Wilma's accusation, a gunshot, and Nash's uncontrolled flames/visions; the accusations are not independently adjudicated.
6. **01:53–02:13:** private council, including Zorenthelas's beliefs about Elhandar and dragon engines — only his testimony.
7. **02:12–02:17:** Hope's unusual wrench speaks in Dwarven; Shun'ti interprets it as urging repair.
8. **02:15–02:30:** Hope presents Fate 4 and **Zorenthelas receives the C4N-D13 medical automaton's data core** with a request to bring it to **Elhandar**; the automaton's claimed significance for the data and future delivery are unverified.
9. **02:30–02:41:** the company departs in Fate 4 toward the goblin raiders.

**Operation intent:** Preserve Chapter III's first two paragraphs; replace only its two temporally compressed last paragraphs (currently original lines 29 and 31) with source-aligned, reader-first storytelling. Add the data-core handoff without asserting successful arrival or later custody. Preserve existing `[^arc01-4]` reference and the rest of the file byte-for-byte except this bounded replacement.

## Executed operations and independent checks

- **98.1 Complete:** Git/access/approval/source evidence and exact two-paragraph edit scope were checked at opening; this journal was persisted before target edit.
- **98.2 Complete:** Archived the *then-current exact working copy* to `research/legacy/ARC_01_PRE_CHAPTER_III_REPAIR_98_2026-10-28.md` **before editing**. The original and newly written archive each measured **14,712 bytes** and SHA-256 `3ed8463af7a316c461d556ff8c535a56d659ff2d50bb3e07e3a891ef38b465e5`, verified by separate MCP binary reads.
- **98.3 Complete:** Immediately before editing, the live draft hash and size still matched preflight. One **unique guarded replacement** changed only the original two final paragraphs of Ch III (old 1,092 text characters replaced by 2,255), preserving all prefix and suffix bytes/text. New `narrative/ARC_01.md` is **15,875 UTF-8 bytes**, SHA-256 `ca7e951972048351cb4a8b7482bbc1c32aff19243a87d9a704f887b31bbc0548`.
- **98.4 Complete — static/dossier validation:** Direct source-after read and independent full-document comparison found **4,726 identical prefix characters** and **8,846 identical suffix characters**. Exactly the intended bounded Ch III segment changed. Six numbered chapters still exist. Exactly **7 footnote uses / 7 definitions, zero dangling references**. **All 19 Markdown links are byte-identical to their pre-edit occurrence list**; link destinations therefore remain those checked in Batch96 (not freshly rendered in this batch). Corrected Ch III approximates **477 whitespace-like words**; the 350–450 guideline is diagnostic, not a deletion quota.
- **Chronology check:** E006's surface-water test → Vorel's goblin capture → Aaron ambush → Bok Bok self-identification → **next morning** Shun'ti/Wilma meeting → private council → speaking wrench → Fate4 unveiling / **C4N-D13 core delivered to Zorenthelas with Elhandar request** → departure were all found in the corrected chapter in that strict order. Source is [E006 dossier](../episodes/E006.md), L13–23, which itself draws from processed, unverified ASR. E005 waterworks restart is still distinct from E006 surface proof; the Aaron/Wilma dispute remains unresolved. The core's future arrival and the automaton's interpretations remain *unverified claims*, not performed outcomes.
- **Protected-source verification:** MCP binary metadata after the edit confirms unchanged `narrative/ARC_ONE.md` 24,216 bytes/SHA `956c0a4a6314fc09aee7f985bd7c95a6c9c6274ee958cfb0eaec557e11b39e7a`, `narrative/ARC_FOUR.md` 24,569 bytes/SHA `428f5e930d4d2e55de3f77f98d0809e9e6db6f3e526d75a4672c9b82be095a39`, Arc07 ending pilot 8,902 bytes/SHA `33d13f2750cf38b8b00bc3b7a1a693bb76c7fb142e1f46d612a4c2480cf1443f`, public `narrative/README.md` 14,825 bytes/SHA `5178cb9246e9d93f289d8b8219a828d4238de96c1b50d41112625f042f5165a3`, and `wastes/README.md` 4,048 bytes/SHA `fd90039aef48455fb9695bd1cd034823e7bdf2370566eec9b9321f6b2fee6349`. No changes to four other word-form arcs or season stubs in Git diff.
- **98.5 Tracker prewrite retention complete:** Before synchronizing, archived exact live modified tracker bytes: `research/legacy/WASTES_CLEANUP_PROGRESS_PRE_98_2026-10-28.md` **180,321 bytes/SHA `c405bb4f3f1faa85b84a413f7767a8bf3495f0e9276d291cf373e450c49f7a5d`**, and `research/legacy/WASTES_CLEANUP_MANIFEST_PRE_98_2026-10-28.md` **224,065 bytes/SHA `d7c194949c3b770a4ae80e5a55f488fbb4efe5604dee9ca4e4b2220f8f6a9792`**. Each archive exactly matched its current source SHA and byte size after creation. Manifest/progress checkpoint **complete**: both updated trackers' appended Batch98 records were read back and contained the expected report reference and new Arc01 SHA; final Git scope inspection found **10 visible changes, zero restricted**, including **5 inherited Batch97 changes**, new Batch98 report, current Arc01 edit, one new pre-edit narrative archive, and two pre-tracker archive files. No other narrative or public navigation paths changed.

**Lifecycle:** Revised Arc01 = *edited / structurally validated / reviewed against bounded episode dossier*, not independently audio-confirmed or finally owner-accepted. The dense Arc07 ending pilot remains untouched. **No publication/index switch, extra scene writing, further arc files, independent audio, GFM renderer, Markdownlint, `git diff --check`, stage, commit or push** is claimed.

## Next bounded action

**Batch98 complete.** Both trackers are synchronized and source-scope readback verified. The next batch should re-review the corrected Ch III within Arc01's six-chapter story for reader flow and remaining evidence concerns, distinguishing a **working drafted/structurally validated page** from finally accepted narrative. Do not extrapolate permission to rewrite other arcs, change public routes, or publish the eleven-arc edition.
