# Wastes Batch 66 — Factions and powers D-048 static page acceptance

**Date:** 2026-10-28 (Europe/Stockholm). **Authority:** D-048 reader-first standard, D-047 minor-editorial permission, D-045 eleven-arc crosswalk (not yet implemented). **Type:** read-only source/content audit, no canon or page edit approved/required by this batch.

## Fresh baseline and scope
- Access hierarchy checked from local filesystem → repository MCP → GitHub → Git patches → ZIP. Local checkout is not mounted here; Keycloak-authenticated workspace MCP is reachable, revision-correct and capable. No need to fall back to the lower-priority routes.
- Repository `There Will Be Dungeons Transcripts`, `main` HEAD `59e327f283b0f1357e7eab733dab99323e9aff4e`.
- Git baseline: **ten pre-existing visible working-tree changes**, including the Batch 62–65 journals, archives, faction page, manifest and progress; zero restricted entries. All protected. No commit/push.
- Audit target `world/FACTIONS_AND_POWERS.md`: **40 LF-ended lines, 10,955 bytes, SHA-256 `9e8ec68b5c67e398bdb08303d584829f8dee533560f3948124c2a2fce2836a4a`** (live read). No new archive necessary because no source mutation is planned.
- Source horizon remains **ASR-provisional, researched through S3E15**; neither S3E18 played finale nor S3E19 Q&A is backfilled. Preserve original source links, index aliases, existing notes and Groxl/giant/Eye uncertainty.

## Ordered audit plan
1. Re-read complete exact current page and verify reader-first heading, introductory sentence, three-column source index, distinct entries, reader navigation and final `Sources and project notes` section.
2. Verify table row shape and content boundaries, including Groxl identity tension, S3E05–09 chronology and no invented resolution.
3. Enumerate every inline Markdown link in the complete page, resolve relative paths from `world/` and independently check each **distinct target file** is readable. Separate file existence from anchor validity and external link checks.
4. Enumerate every Markdown footnote use and definition, verify one-to-one pairs, unique IDs, nonempty definitions and preservation of the seven earlier notes plus two new evidence notes.
5. Record observed page SHA/length and checks, exceptions and unrun limitations, then append one manifest and one progress-pointer checkpoint. Re-read all checkpoint writes and Git status. Never claim full canon/audio, rendering, Markdownlint or Git whitespace acceptance without actually running the check.

## Audit results and dispositions

**Source persistence:** The live source remained **40 lines / 10955 bytes**, SHA-256 `9e8ec68b5c67e398bdb08303d584829f8dee533560f3948124c2a2fce2836a4a`, matching the exact post-Batch-65 checkpoint `9e8ec68b5c67e398bdb08303d584829f8dee533560f3948124c2a2fce2836a4a`. **No changes to `world/FACTIONS_AND_POWERS.md` in Batch 66**, so no new source-original archive is needed. Original LF-only formatting, no image embeds, and researched S3E15/ASR-provisional boundary preserved.

**D-048 reader-first structure PASS:** One page H1 (`Factions, institutions and supernatural powers`) is followed immediately by an in-world introduction. A three-column faction/source index occupies original lines 5–21. Source/production metadata and navigation to campaign/portal appear in the **final** H2 `Sources and project notes` (line 25). No production-status banner precedes the story. This is an overview/index, so the final sources section is appropriate.

**Full table PASS:** 17 table lines comprise **one header, one three-column alignment/separator and 15 data rows** (lines 7–21), each containing exactly **three nonempty cells**, with **15 distinct subject labels**, no unexpected pipes/columns, and no inferred new final-state or Groxl identity. The newer S3E07/S3E08 rows and earlier S3E05/S3E06/S3E09 rows retain their chronology and witness qualifiers; the S3E07 GM Eye-recognition vs S3E08 `not Grojil`/abomination contradiction remains a documented open issue. S3E09 self-described Eye origin remains testimony rather than a new fact.

**Complete inline-link static verification PASS:** **46 Markdown link occurrences, 40 distinct relative URL file targets**; each path resolved relative to `world/` and **all 40/40 independently confirmed readable** using the authenticated repository workspace. Two transient access restrictions were resolved without source edits: `world/places/slavetown.md` failed a text read safety check but succeeded via bounded binary read and SHA/size; `episodes/S3E13.md` failed a binary access safety check but succeeded with a one-line numbered text read. All other 38 distinct targets succeeded in first bounded access. **No external URLs, fragment anchors or image embeds** occur in the page; this checks the **target files**, not backlinks, Markdown rendering or semantic accuracy.

**Footnotes PASS:** **9 unique inline use IDs and 9 unique, nonempty definitions**, with exact one-to-one matches, no orphan/duplicate IDs. Seven prior notes and two Batch-65 note IDs (`factions-solar-e07` and `factions-solar-e08`) remain present. Their original evidence descriptions were previously verified verbatim against the byte-exact pre-Batch-65 archive; this batch did not change them.

**Acceptance decision:** `world/FACTIONS_AND_POWERS.md` is **D-048 static reader-first layout, Markdown table-shape, paired footnote, and relative link target-file readability ACCEPTED** at the above exact source hash. This is NOT full rendering acceptance, audio/canon source adjudication, or overall Wastes campaign cleanup completion. Pending elsewhere: GFM rendering and clickable footnotes, Markdownlint, `git diff --check`, incoming backlinks, independent source audio, and broad tests. No commit/push.

**Next Batch 67:** Bounded reader-first inventory and, where permitted, presentation migration of the high-priority `world/CHARACTERS.md` index (including performer column, finale mechanics and canonical display names). Re-evaluate access from local first, inspect live HEAD and working tree, preserve any original before source edits, and do not resolve contested identity or genealogy without owner approval.

