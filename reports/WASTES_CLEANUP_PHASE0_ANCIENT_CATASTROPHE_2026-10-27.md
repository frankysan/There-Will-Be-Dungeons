# Wastes cleanup — Phase 0 ancient-catastrophe article, batch 12

**Date:** 2026-10-27 (Europe/Stockholm). **State:** ANCIENT-12-01/02/03 completed and verified. **Repository:** `There Will Be Dungeons Transcripts`, branch `main`, initial HEAD `ad80d071af89a968a25d186415b94cdb1a1b2df4`. Initial Git status: seven visible Wastes metadata changes from batches 07–11 (five added reports, modified manifest and progress), zero restricted entries reported.

## Authority and scope

User requested continuation of `$twbd-wastes-cleanup` from the current repository state. The exact next bounded slice recorded by [progress](../project/WASTES_CLEANUP_PROGRESS.md) is a **read-only first-pass structural census of `world/HISTORY_ANCIENT_CATASTROPHE.md`**. Only the audit report and Wastes manifest/progress metadata may be updated this batch. Original world, source, episode, narrative, archival and other-campaign files must not change; preserve all existing Git modifications. Do not commit or push. Owner-approved **D-044** spelling (The Principal, Principal City, Khaervilon, T'ietkalla and related map/family names) and **D-045** eleven-arc boundaries remain in force; no blind source rewrites or path renumbering. **Stop before any proposed new/undecided lore, genealogy, taxonomy, content revision or rename** and request explicit approval.

## Ordered bounded steps

| ID | Operation | State |
| --- | --- | --- |
| ANCIENT-12-01 | Read 17/17 numbered lines; classify headings, article horizon, GM prologue versus in-world testimony versus direct observations, and canonical name leads | **Complete: 17/17 lines, no gaps** |
| ANCIENT-12-02 | Count lexical Markdown links and check in-world targets against the unchanged 134-file world worklist; explicitly label other targets not verified | **Complete: eight in-world targets listed, nine episode links unchecked** |
| ANCIENT-12-03 | Record verified facts/limitations here, update Wastes cleanup manifest/progress via guarded writes, read back all records and recheck Git HEAD/status | **Complete: records read back and Git scope confirmed** |

## Findings and validation

### ANCIENT-12-01 — full structural read and evidence class

The exact current `world/HISTORY_ANCIENT_CATASTROPHE.md` is **17/17 consecutively numbered lines with no gaps**, **three Markdown headings** (one H1, two H2), **zero table lines**, no footnote reference/definition syntax and no `[[review-needed:...]]` markers. The in-world period is explicitly *long before the principal campaign*, with **no verified precise ancient calendar**. The article identifies its research as **processed-ASR-provisional**, not original-audio verified.

The `E000` GM prologue (line 9) anchors the **broad setting frame**: dragons arriving through gates, humans using sophisticated machines and pacts, catastrophic war and later scavenging. It does **not** prove gate builders, exact dates, duration, named participants or all details of later claims. Later **physical evidence** (line 13) includes old facilities/engineering at Dusthill, Leopold's laboratory, T'ietkalla and CHIDS—especially observed CHIDS bodies, conditioning controls and large Drive apparatus. These encounters demonstrate *local objects and acts*, **not** origins of every dragon, lizardfolk or entity. The distinct **speaker-attributed, contested accounts** (line 15) include a spectral dragon's planet-moving theory, hive council testimony of preserved minds and experiments, Quizquaz's Void mechanism, and the father-of-Stanley journal's possible Weir-related time adjacency. The final line explicitly retains all such mechanism and chronology questions **open**.

**Names and migration, not edited:** one displayed editorial `Tietkalla` (line 13) and one `Principle` (line 13) occur; D-044 confirms **T'ietkalla** and **The Principal** respectively for unambiguous editorial referents. The path `places/tietkalla.md` remains a stable legacy identifier; never replace slug links blindly or alter raw dialogue. The text has no legacy Arc Six narrative links. D-045's 11-arc reorganization does not require an invented ancient-calendar or story-world arc boundary in this article. Correct spelling is an owner-approved editorial policy but its application is **deferred** to referent-checked revision; no textual correction was performed in this read-only batch.

### ANCIENT-12-02 — scoped link membership

Found **17 ordinary Markdown link occurrences** (17 distinct targets): **eight within `world/`**, all eight matching paths in the **unchanged 134-file sorted, unique `project/WASTES_CLEANUP_WORLD_WORKLIST_2026-10-27.json`**; **zero missing among the checked world-file destinations**. These internal links are Historical Events, README, World, Dusthill, legacy Tietkalla, CHIDS, Chronology and Consistency Ledger. The other **nine links** reference distinct episode dossiers `E000`, `E008`, `E073`, `E077`, `E079`, `E067`, `E078`, `E081`, `E118`; **those targets, anchors, claims and source contents were not verified**. None of this article's ordinary links uses a `#fragment`. Lexical Markdown scanning is not full rendered-link validation or a repository-wide incoming-link test.

### Preservation and validation

No `world/`, `episodes/`, `sources/`, `narrative/`, `research/legacy/` or other-campaign content changed, no canonical identity/speculative testimony promoted to fact, and no source/link/path/slug rewrite occurred. **Unperformed:** working-copy SHA-256, full claim provenance and cross-episode cue resolution, original-audio listening, full Markdown AST/anchors/backlinks, verification of nine outside-world targets, Markdownlint and `git diff --check`. This file is a **first-pass structure review only**. World files fully structurally read to date: **12/134**, **122 still unread**.

## Recovery pointer

**ANCIENT-12-03 verified:** the new batch-12 journal (37 lines at readback), Wastes cleanup manifest (115 lines) and progress pointer (41 lines) were all read back with consistent evidence and next action. Final observed Git status: `main` HEAD `ad80d071af89a968a25d186415b94cdb1a1b2df4`; **eight visible Wastes-only metadata changes** (six added audit journals from batches 07–12 plus two modified Wastes cleanup controls), zero restricted entries reported. No world, episode, source, narrative, legacy or other-campaign content changed; no commit or push. **Next separate read-only slice:** `world/HISTORY_CHIDS_DRIVE.md`, after confirming live controls; do not conflate planet/Drive in-world claims with verified history. Unapproved substantive edits must stop for owner direction.
