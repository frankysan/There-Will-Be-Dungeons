# The Wastes — N1-P3-F: CHIDS, Sigil and Solar Mines name display corrections

**Date:** 2026-10-28 (Europe/Stockholm). **Owner authorization:** D-047 standing permission for unambiguous minor editorial corrections; D-044 written canonical name forms **The Principal**, **Principal City**, **Khaervilon**, and **T'ietkalla**. This permission does not cover storyline rewrites, changed certainty of NPC recollections, removal of historical aliases, direct quotes or media/ASR source changes.

**Git baseline:** `There Will Be Dungeons Transcripts`, branch `main`, HEAD `7f331552a7c87172a18a9b165f258f4b1c036f38`, 161 visible changes and 65 restricted omitted. Direct local checkout not available; live workspace MCP edits. Concurrent Delvers and earlier Wastes edits protected; no commit/push.

## Ordered thematic batch — all original lines read

Exactly **371/371 gapless numbered lines** read in three place articles, and each source input SHA-256 verified. Reader-facing old spellings account for **39 occurrences across 23 distinct source lines**. No unrelated correction is included.

| ID | File / size | SHA-256 baseline | Lines targeted (correction counts) | Total line count | Markdown links | Footnote uses / defs |
| --- | --- | --- | --- | ---: | ---: | --- |
| F01 | `world/places/chids.md` / 25424 bytes | `7b1bb1dcd52915c0c58a2081186b866c2cb81035021ea5e8c626789d2891acb6` | 7, 31, 35, 65, 77, 93 (6 corrections) | 93 | 34 | 0 / 0 |
| F02 | `world/places/sigil.md` / 55325 bytes | `bc8c26ed9d89535faa9fd5a7e86765c369b749328108a528049f708ec907dd65` | 5, 7, 13, 27, 189, 201 (9 corrections) | 201 | 71 | 0 / 0 |
| F03 | `world/places/solar-mines.md` / 24510 bytes | `e6570e8c3fa76f855cf7df9e282b7c2f22384a950634af4601787320185cf2e3` | 9, 15, 19, 23, 27, 31, 35, 39, 43, 51, 75 (24 corrections) | 77 | 41 | 0 / 0 |
| **TOTAL** | **three existing place articles** | | **23 distinct lines, 39 old names** | **371** | **146** | **0 / 0** |

**Referent classification / limits:** In CHIDS, retain the quoted **“Principal Dombrovski”** as a separate named historical official, and retain uncertainty about whether this is today's **Principal**; only editorial `today's Principle` is misspelled. CHIDS's recorded access sequence, machine and prisoners remain unchanged. In Sigil, spell the intended location **Khaervilon**, preserving original **`/Caravalon (?)`** as an ASR uncertainty and the fact that Hope did not cross the Gate. The E106 refugees are still *absent* from the Sigil arrival, and the GM's E116 Gate test was unsuccessful; creator lore stays expressly conjectural. In Solar Mines, the father/N4SH theories remain unverified, Nash's original childhood abuse remains partially reconstructed memory, the Principal City and other place concepts remain distinct, and no mining, Ruby or Worldbreaker event is reinterpreted.

**Exact permitted edits:** Only canonical names in these specified already-read narrative/headings/link-label portions: `PRINCIPLE`→`PRINCIPAL`, `Principle`→`Principal`, `Kervalon`→`Khaervilon` and `Tietkalla`→`T'ietkalla`. Preserve all original URL paths (`kervalon.md`), quote text, source/episode IDs, other aliases, footnote identifiers, line formats, source claims and certainty. No blind repository-wide replacement.

**Procedure:** Create this journal before source mutations; archive actual live working originals with matching byte size / SHA-256 before edits, recheck input SHA before unique guarded per-line replacements, reread and compare exact changed lines, all 371 original numbered lines and 146 Markdown link destinations, footnotes and CRLF. Then record actual final hashes, one new manifest checkpoint and one progress checkpoint, verify final Git state. Stop for a substantive unapproved meaning change or intervening source drift.

**Checks unavailable/unrun:** Markdownlint, `git diff --check`, full destination/fragment/backlink resolution and original audio listening. Do not claim these passed.

## Applied changes and validation ledger

**Checkpoint 0 — PASS:** The scope journal was created before any source mutation. All three original source files matched the above SHA-256 baselines. Exact byte-identical copies were created and independently re-read with matching byte lengths/hashes at `research/legacy/{CHIDS,SIGIL,SOLAR_MINES}_PRE_N1_P3_F_2026-10-28.md` before the first source edit. Original files were CRLF and this format was retained.

| ID | Exact original source lines changed | Name corrections | SHA-256 after edits |
| --- | --- | ---: | --- |
| F01 | 7, 31, 35, 65, 77, 93 | 6 | `24c8a9826a1d287fdca030ea5902ad231757a794f857dbf9b333e6b5164a4dd9` |
| F02 | 5, 7, 13, 27, 189, 201 | 9 | `53934e82f61ed02f7ef42927fceadf8304821e04455a8a1ffbedc32438205472` |
| F03 | 9, 15, 19, 23, 27, 31, 35, 39, 43, 51, 75 | 24 | `d276efe6953831fb0cd819a656c456b7464376c9c321697bf49283244ca27b69` |

**Checkpoint 1 — PASS:** 23 guarded line replacements applied only in the named three source files, correcting 39 proper-name occurrences (`PRINCIPLE`→`PRINCIPAL`, `Principle`→`Principal`, `Kervalon`→`Khaervilon`, `Tietkalla`→`T'ietkalla`). No original URLs, media transcripts or campaign structure changed. In CHIDS, historical **“Principal Dombrovski”** remains distinct; uncertainty about whether he was the antagonist remains. Sigil's canonical written **`Khaervilon/Caravalon (?)`** retains the uncertain ASR variant and the unsuccessful Gate result. Solar Mines hypotheses about future experiments and the unlabeled past are still explicitly speculative.

**Checkpoint 2 — PASS:** All three complete original and edited source byte streams reread and compared against archives. Verified **371/371 original numbered lines, 23/23 specified changed line numbers, 39/39 exact canonical-name corrections, 146/146 identical ordered Markdown link destinations, zero original footnote identifiers altered and preserved per-file CRLF counts**. Each changed original line matches the precise expected proper-name-only substitution; no other lines differ. Source/post SHA-256 values recorded above and in the three live files. No independent source/audio fact-checking asserted.

**Checkpoint 3 — CLOSED:** One guarded completion checkpoint added to `project/WASTES_CLEANUP_MANIFEST.md` at line 201 and one to `project/WASTES_CLEANUP_PROGRESS.md` at line 127; both read back. Final `git_status` confirmed `main`, unchanged HEAD `7f331552a7c87172a18a9b165f258f4b1c036f38` and **168 visible changes**, including the exact three modified place articles, their three pre-edit research archives, this journal, and Wastes manifest/progress. Other concurrently changing Delvers and unrelated files not touched by this batch. No commit/push. Markdownlint, `git diff --check`, true link-target/anchor/backlink resolution and source listening **unrun**. **Next:** N1-P3-G bounded referent-aware remaining world places/characters canonical display inventory; autonomously apply only small unambiguous D-047 edits. Substantive C1, D-045 A1 and D-046 R1 still approval-gated.
