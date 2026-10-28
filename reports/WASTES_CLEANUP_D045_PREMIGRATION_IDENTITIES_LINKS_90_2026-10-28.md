# Wastes Cleanup — Batch 90: D-045 Arc Six immutable identities and navigation-compatibility gate

**Date:** 2026-10-28. **Disposition:** **READ-ONLY MIGRATION-PREFLIGHT COMPLETE** — immutable paragraph ledger, exhaustive original outbound Markdown link and heading ledger, bounded file-target checks and scoped incoming/filename dependency review. **No changes to narrative, root/story indices, arc titles, chapters, redirects, canon or compatibility paths.** D-045 eleven-arc boundaries were approved; final target filenames, revised chapter authoring, lossless consolidation and public route switch were **not** approved under D-047.

## Re-evaluated access and live repository status

- The direct local checkout was **independently checked** under `/local/There Will Be Dungeons Transcripts`, `/mnt/data/There Will Be Dungeons Transcripts`, `/workspace/There Will Be Dungeons Transcripts` and `/workspaces/There Will Be Dungeons Transcripts`, and **none are mounted** in this container. Authenticated Keycloak workspace **MCP is reachable** and preferred; GitHub access, Git-generated patches and ZIP fallbacks were not needed. Re-evaluate the full priority from local access again at the start of **each** new file access batch and after failures.
- Live repository `There Will Be Dungeons Transcripts` on **main**, HEAD **`02e35be895c72260d3c0ebc8ef402ef361d90206`**, **nine prior uncommitted visible changes / zero restricted** at batch start (seven Batch83–89 reports and two cleanup checkpoints). They were preserved with no reset/stage/commit/push. This batch created two additional reports and updated the cleanup pointers only.
- Original `narrative/ARC_SIX.md`: **206,128 bytes / 813 CRLF-terminated lines**, SHA-256 **`44e8b30073d3d95a93b449783de11c7cafac1e74473c2ea082ce7e68b1ee541d`**. Four contiguous 64-KiB binary reads were reassembled exactly and their full-file digest **independently recomputed**, matching the server. The hashing implementation also passed the known SHA-256 test vector `abc`. No original source mutation or new legacy source archive was performed in this read-only batch.

## Deliverable 1 — all original narrative paragraph content identities

[Full stable byte identity register](WASTES_CLEANUP_D045_ARC_SIX_PARAGRAPH_SHA256_LEDGER_90_2026-10-28.md).

- Exactly **347** unique source narrative/status paragraphs: **116** in owner-approved **Arc 10** source range (S2E01–12 plus S3E01–03), **231** in **Arc 11** source range (S3E04–18). Episode/chapter groups agree with Batches 83–89 at **30 played episode groups**. **Zero duplicate SHA-256 paragraph contents**.
- One ledger row for each original one-line source paragraph: **original 1-based line number, episode, provisional chapter number, zero-based original byte offset and UTF-8 byte count, and SHA-256 of exactly that paragraph's raw UTF-8 bytes with the CRLF excluded**. This contract does **not** remove original punctuation, whitespace within the line, spelling or Markdown emphasis. The record is reproducible against this precise source hash.
- Crucial correction during read: the actual file uses **CRLF**, whereas several Wastes world/reference pages use LF. An initial naive line classification included CR-only blank rows as supposed prose, **was rejected before any ledger was written**, then corrected. The created ledger's **347** records and 813 original line terminators were independently checked against the full-file SHA and prior paragraph counts.
- **Stable content digest ≠ stable exact location.** Future destination mapping must carry original source SHA, episode + line number + raw byte span and target paragraph/scene disposition, because edited text changes digest and duplicated texts (if any appear later) can be ambiguous.
- Excluded from 347 story paragraph count: original headings, blanks, editorial intro L1–8, Season Three transition L201–204, standalone episode evidence-note lines, and the footer L807–813's **three nonstory audit paragraphs**. They must have separate retention paths and were enumerated in the link/heading ledger and prior Batch 89 report. No final reader chapter wording has been prepared or approved.

## Deliverable 2 — original Markdown link and section heading ledger

[All old link occurrences and headings with exact line IDs](WASTES_CLEANUP_D045_ARC_SIX_LINK_HEADING_LEDGER_90_2026-10-28.md).

| Source inventory | Exact count | Interpretation |
| --- | ---: | --- |
| Ordinary inline Markdown link occurrences | **67** | Preserve each original occurrence's provenance/context until approved deduplication |
| Distinct destination strings | **54** | **54/54** current target files independently opened/read by authenticated MCP metadata |
| Links in intro/narrative/episode note lines L1–806 | **34** | Includes **26 occurrences** on mapped original S3 episode evidence-note lines |
| Links in research/footer L807–813 | **33** | Season Two and Three audit/closure register; not Arc 11 scene prose |
| ATX headings | **42** | All original heading text and line IDs recorded; includes 30 played episode scene groups, seasonal headings and research footer |
| Original footnote definitions | **0** | The source uses inline narrative citations; other files may have different structure |
| Original link URLs containing fragments | **0** | This is an **outbound** property, not a claim about incoming anchors |
| Original link URL schemes/absolute paths | **0** | All links relative to current `narrative/` |
| Percent-encoded source URLs | **2 occurrences** | S3E019 roundtable SRT referenced in S3E18 note and footer; actual file with spaces independently read |

**All 54/54** distinct original link destinations were checked by individually opening their actual normalized repository paths in seven bounded batches (8+8+8+8+8+8+6); zero missing/unreadable files. The S3E019 Markdown path needs percent-decoding into its **literal-spaced filename** for MCP file access. This is **file-target readability only**, not hyperlink rendering, Markdownlint, link anchors, source audio or full incoming-backlink validation. Link-count statistics include duplicated URLs in different source contexts and are **not** a unique citation count.

## Scoped incoming ARC_SIX.md/backlink inventory

Targeted `search_workspace` with literal `ARC_SIX.md` across **narrative, wastes, world, project, reports, episodes** and other top-level areas; main directories were searched separately to avoid root search truncation. Important **maintained reader-facing incoming sources**:

| Existing file | Observed link(s) / role | Migration requirement |
| --- | --- | --- |
| `narrative/README.md` L19 and L27 | **2 direct Arc Six links**, six-current-arc story guide | On acceptance, present eleven new readable arcs, keep older reading access |
| `narrative/SEASON_TWO.md` L3 | Season Two compatibility stub **1 direct Arc Six link** | Keep path working; newly guide Arc 10's S2E01–12 and S3E01–03 without mislabeling season ending |
| `narrative/SEASON_THREE.md` L3 | Season Three stub **1 direct Arc Six link** | Keep path working; newly guide Arc 10's S3E01–03 and Arc 11's S3E04–18 |
| `wastes/README.md` L16 | Campaign overview **1 direct Arc Six route link** | Change only when all approved routes exist; link coordinated with narrative README |
| `world/FACTIONS_AND_POWERS.md` L15 | Solar Mines coalition status **1 direct Arc Six link** | Repoint to the appropriate verified new arc/episode, or preserve functioning old link |
| `project/DECISIONS.md` D-043 and other planning rows | Historical implementation contract and relative path | Preserve **historical decision record**; add supersession/implementation note, don't rewrite earlier owner decision |
| `reports/PRINCIPAL_RELATED_NAMES_AUDIT_2026-10-27.md` L30 | Historical evidence link to exact old Arc Six | Preserve historic reference as evidence to original baseline |
| `.agents/skills/twbd-episode-analysis/SKILL.md` L91 | Workflow instruction refers to `ARC_ONE`–`ARC_SIX` as the current maintained narrative and says Arc Six is **“STILL-OPEN”** | Existing wording now **factually stale** since S3E18; update deliberately as part of workflow migration, retaining completed-story distinction |
| `project/DOCUMENTATION_ARCHITECTURE.md` L60–61 | Declares Arc Six **ongoing and reviewed only through S3E01**; season stubs | Also stale current status; migrate architecture documentation as a coordinated change |
| `README.md` L11 | Root campaign hub links **indirectly** to `wastes/README.md` and `narrative/README.md` | Preserve hub route; no direct ARC_SIX link found in inspected root entry |

- No exact `ARC_SIX.md#...` references surfaced in separate scans of **narrative, wastes, world, project, reports, episodes, scripts and transcripts** (0 matches in these scopes). This is **not** a guarantee for uncatalogued source archives or direct HTTP bookmarks, and the root search reports truncation on very large collections. Preserve old headings/old file for compatibility until proved safe.
- `reports/` and `project/` contain many **historical mention strings** rather than actionable reader navigation. Maintain evidence/legal provenance as distinct from public reading route swaps. The scoped search found **42 report files** mentioning `ARC_SIX.md` at the time of scan (not a count of actual Markdown hyperlinks or unique source occurrences). `local/` bulk search was truncated and therefore is **not** certified as a full incoming-link audit; source archives should remain untouched.
- No direct `ARC_SIX.md` file links were found by scoped searches of **delvers, inverse, bonuses, oneshots, tools or tests**. `.agents` has a workflow reference. Original `ARC_SIX.md` includes no outbound fragment links; all **42 heading strings and original byte content** are protected in ledgers.

## Filename and compatibility decision — proposal only, owner gate OPEN

**Current published `narrative/` inventory contains exactly nine files:** `ARC_ONE.md`, `ARC_TWO.md`, `ARC_THREE.md`, `ARC_FOUR.md`, `ARC_FIVE.md`, `ARC_SIX.md`, `README.md`, `SEASON_TWO.md`, `SEASON_THREE.md`. Proposed **`ARC_01.md`–`ARC_11.md`** is named as an **option** in `project/WASTES_CAMPAIGN_CLEANUP_PLAN.md` L65; it is **not an enacted or owner-approved filename contract**. There is **no** `ARC_SEVEN.md`–`ARC_ELEVEN.md` published. No new arc is created here.

**Recommended future contract for explicit owner decision:**
1. Use **numeric zero-padded `narrative/ARC_01.md` through `ARC_11.md`** for the eventual 11-arc sequence. The reason is stable machine/lexical sorting and no confusion between numeric new Arc 06 (E067–E081) and legacy `ARC_SIX.md` (S2–S3), which have **different story meanings**. Do not silently rename the old words to new numbers.
2. **Keep all six old word-form `ARC_ONE.md`–`ARC_SIX.md` readable and byte-preserved during the new publication phase**, with exact originals archived under `research/legacy/` only **before** any authorized modifications. Do not redirect legacy `ARC_SIX.md` to **just** Arc 10 or Arc 11: it spans **both**; a later approved compatibility landing may link to both, but the original long synthesis should remain discoverable from archive and evidence links.
3. The two `SEASON_TWO.md`/`SEASON_THREE.md` compatibility stubs remain active. After replacement acceptance they should point readers to the appropriate **multiple new arcs**, while preserving seasonal meaning and S3E019 Q&A boundaries; they should **not** become another set of duplicate narrative drafts.
4. Update `narrative/README.md`, `wastes/README.md`, world index and subpages, chronology, relevant workflow skills and architecture docs **together at release readiness**, not piecemeal to nonexistent targets. Use transition references to maintain historic D-043 vs forward-looking D-045 distinctions. The original source paragraph, 67 outbound link occurrences and global research footer retain traceability.
5. Before any source edit, recheck Git status and full access hierarchy, **archive exact then-current working bytes** and independently verify SHA/size; build and verify target paragraph-disposition ledger (original SHA + byte span → new chapter + retained/summarized/archived + source evidence), then validate source-note links, incoming links, chapter headings, broken references and GFM. Scene compression/rewriting and unresolved lore require **D-047 owner approval**, not automatic machine restructuring.

**Proposed next Batch 91 (read-only):** Audit the **five legacy Season One narrative files** in similarly bounded format for original hashes, source paragraphs, inbound crossreferences and **E101 shared recording**. The approved eleven-arc boundary crosswalk also spans these files, and final migration/public route replacement remains blocked until exact filename/compatibility choices are owner-approved. This can proceed as a preservation audit without writing new arcs. If the owner first approves the numeric naming/compatibility contract, record that decision before implementation.

**Open/unrun:** comprehensive `local/` inbound census, original audio, rendered GFM/Markdownlint/`git diff --check`, full baseline incoming links including outside HTTP bookmarks, final chapter semantic coverage, editor-approved 11-arc prose, and broad tests. **Batch 90 edits reporting/trackers only; no commit/push.**
