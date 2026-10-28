# The Wastes — N1-P3-C T'ietkalla creature articles: D-047 editorial-minor execution

**Date:** 2026-10-28 (Europe/Stockholm). **Authority:** D-047, explicitly owner-confirmed permission for bounded, unambiguous minor spelling/display-name corrections without per-file approval. D-044 independently fixes the canonical written **T'ietkalla**. No new lore, source claims or entity identity rulings are in scope.

**Repository at start:** `There Will Be Dungeons Transcripts`, `main`, HEAD `7f331552a7c87172a18a9b165f258f4b1c036f38`; **117 visible working changes, 49 restricted entries omitted**. Prior Wastes and unrelated concurrent Delvers work protected; no commit/push. Direct local repo not accessible in this session; connected workspace MCP used according to repository priority.

## Ordered scope, pre-edit input and recovery checkpoints

Six related creature pages, **126/126 gapless numbered lines fully read** before mutation, all references assessed. Only seven source lines and seven occurrences of `Tietkalla` in maintained, reader-facing narrative and display-link labels are in scope. The historical `../places/tietkalla.md` URL is a stable old slug and **must not be changed**.

| ID | Source path | Lines | Pre-edit SHA-256 | Exact line(s) | Substitutions | Links | Footnote uses / defs | Status |
| --- | --- | ---: | --- | --- | ---: | ---: | --- | --- |
| C01 | `world/creatures/basilisk-of-the-under-pit-caves.md` | 20 | `1d0a9e578e7946aa16c51bcf335500fd465e32fdc2aac89a5d5450dc9f9324eb` | 5 | 1 | 7 | 4 / 4 | queued |
| C02 | `world/creatures/black-puddings.md` | 20 | `c7500f8393b82a279aeb1f53f3e5cce54b76068e5e8979a70d8f1dafe2a74826` | 5, 15 | 2 | 6 | 4 / 4 | queued |
| C03 | `world/creatures/bloodsucking-desert-swarm.md` | 20 | `c51b90fb1b4aa396f72c563adb2f7df8964a70d357afecb0324a97f649e1272b` | 5 | 1 | 6 | 4 / 4 | queued |
| C04 | `world/creatures/mushroom-pit-spider.md` | 20 | `ea92c601b4a6873884033de1786bdaaff96a551520dcd29a250b1496d6f1a889` | 5 | 1 | 7 | 4 / 4 | queued |
| C05 | `world/creatures/pale-tentacled-burrower.md` | 23 | `ebf1aac10c0dc8d2cfd116a60a5ad5aa29b29c40820fd69a8db81fb347bfb0a7` | 5 | 1 | 7 | 5 / 5 | queued |
| C06 | `world/creatures/river-undead.md` | 23 | `5c11f9129254e301d1002f56ca25841ecd11eb56354920398a5328bcafa35d35` | 5 | 1 | 9 | 5 / 5 | queued |
| **Total** | **Six original files** | **126** | | **7 lines** | **7** | **42** | **26 / 26** | **pending** |

**Change contract:** Render `Tietkalla` as `T'ietkalla` (including `[Tietkalla's]` → `[T'ietkalla's]`), but retain every Markdown link destination, parent/child heading, footnote ID, original quoted words, established timeline, observed kill/escape outcome, uncertainties, and other creature identities. No scope expansion from search results. Four technical steps: (0) create and validate byte-identical original working copies under `research/legacy/` before editing; (1) guarded exact-text replacements on specified lines only; (2) re-read originals and edited source for exact changes and line endings, links and footnotes; (3) journal + one manifest and one progress checkpoint + final Git status.

**Source-horizon context:** Basilisk, black puddings, mushroom pit spider, pale tentacled burrower and river undead are T'ietkalla Pit/underground encounters; bloodsucking desert swarm is on the road between T'ietkalla and Razak Val. Each keeps its independently sourced event cutoff and uncertainty.

**Validation limits:** Link *destinations* and footnote tokens can be compared locally through MCP bytes; actual target/fragment/backlink resolution, Markdownlint, `git diff --check`, and original audio/ASR verification remain **unrun** unless made available. No commit/push.

**Checkpoint 0 — PASSED:** Intent recorded before edits. Each of six live originals rechecked against its table SHA-256, then preserved byte-identically as `research/legacy/{BASILISK_UNDER_PIT,BLACK_PUDDINGS,BLOODSUCKING_SWARM,MUSHROOM_PIT_SPIDER,PALE_TENTACLED_BURROWER,RIVER_UNDEAD}_PRE_N1_P3_C_2026-10-28.md`; each archived file reread, size and SHA-256 identical to original. All originals LF; no file was edited before archival check.

## Actual per-file results — D-047 minor-editorial

| ID | Source changed original line(s) | Exact old→new spelling occurrences | Post-edit SHA-256 | Verified |
| --- | --- | ---: | --- | --- |
| C01 | 5 | 1 | `b2eb69eb0ea62b4072cdbf07aef63c0131700e497cd04387e6ef12053331cf75` | Passed |
| C02 | 5, 15 | 2 | `6d385c1427cbdeeb8272bbc905ebb03cb31c04c78fc7a5212f7156dc436b4aca` | Passed |
| C03 | 5 | 1 | `9253bd9bfb75dd907e276e95ec869513a42491dea155544e6c055e65097c990a` | Passed |
| C04 | 5 | 1 | `3fe4919a4cd2fd6bfa3cbd68a418e058f623085f9dd55f2b00773b12ac87980b` | Passed |
| C05 | 5 | 1 | `b8606b11a431b944756692aca9aaeb801b7f394b5f67681856455c0237a376c7` | Passed |
| C06 | 5 | 1 | `f82f3a6246e62c3b7a83cb39046f1ce5cc126a336182a4e38a861d84565500a4` | Passed |

**Checkpoint 1 — PASSED:** Seven unique guarded replacements succeeded, exclusively `Tietkalla`→`T'ietkalla` in editorial narrative or displayed link labels. Existing `../places/tietkalla.md` URLs retained. No other referents or lore changed.

**Checkpoint 2 — PASSED:** All six edited sources reread in full and compared against their archived originals. **126/126 original source lines**, exactly **7/7 intended changed line numbers** and **7/7 name substitutions**, **42/42 identical ordered Markdown destination URLs**, **26/26 footnote uses and 26/26 unchanged footnote definitions**; original LF endings unchanged. Each changed line matched the expected literal name substitution byte-for-byte; no remaining standalone legacy `Tietkalla` spelling found in these six articles. No audio/source claim verification was performed.

**Checkpoint 3 — CLOSED:** Exactly one completion entry added to `project/WASTES_CLEANUP_MANIFEST.md` (line 195) and one to `project/WASTES_CLEANUP_PROGRESS.md` (line 121); both read back. Final Git status confirmed `main`, HEAD `7f331552a7c87172a18a9b165f258f4b1c036f38` unchanged, 139 visible working changes and 59 restricted entries omitted. Unrelated Delvers and style-guide work progressed concurrently, not touched by this cleanup batch. Six creature files, their six original archives, this execution report and the two Wastes checkpoint files are the only intended N1-P3-C changed paths. No commit/push. **Next N1-P3-D:** inspect remaining T'ietkalla creature/technology files (`pixie-hulks.md`, `sand-squid.md`, `eye-of-groxl.md`, `gem-of-tides.md`) and apply only unambiguous small edits under D-047, with full byte/archive/line/link/footnote checks; stop for any substantive ambiguity. C1, D-045 A1, D-046 R1 still separately gated.
