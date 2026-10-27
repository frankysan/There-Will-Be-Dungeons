# Wastes cleanup — Phase 0 narrative structural census, batch 02

**Batch ID:** `20261027T171419+0100-phase0-narrative-02`. **Started:** 2026-10-27 17:14:19 +01:00 (Europe/Stockholm). **Completed structural reads:** 2026-10-27 17:17:03 +01:00. **Status:** both target files structurally inventoried; full source-to-scene/hash/links baseline remains pending.

## Identity, scope and approval

- **Workspace:** `There Will Be Dungeons Transcripts/` via local workspace MCP; direct local checkout was not mounted in the current tool container. `main` HEAD `5531bd660d0b465f2f658b961f17eccbc33fde56`; initial Git status **clean**.
- **Approved operation:** user invoked `$twbd-wastes-cleanup`; existing [progress pointer](../project/WASTES_CLEANUP_PROGRESS.md) names exactly this read-only Phase 0 census slice. D-045 already approves eleven future arc boundaries; no new boundary, content or canon decision is inferred.
- **Input files:** `narrative/ARC_THREE.md` and `narrative/ARC_FOUR.md` only, in that order. They must remain unmodified. Historical originals, raw SRTs, media, maps, other campaigns and prior reports are protected.
- **Control edits:** this journal, [progress](../project/WASTES_CLEANUP_PROGRESS.md) and [manifest](../project/WASTES_CLEANUP_MANIFEST.md) — tracking only. No rewrite of story, headings, footnotes, navigation or schema.
- **Preservation:** read-only census requires no rewrite archive. Actual working-copy SHA-256 and exact byte count **unavailable through the current MCP text reader**; no input hash is asserted. This prevents archival replacement until a byte-exact local source is available.

## Ordered operations and recovery

| Operation | Target | Prerequisite | State |
| --- | --- | --- | --- |
| CENSUS-03 | `narrative/ARC_THREE.md` | Read complete reported numbered line ranges | **Read complete, structurally inventoried** |
| CENSUS-04 | `narrative/ARC_FOUR.md` | Read complete reported numbered line ranges | **Complete (structural inventory)** |
| CHECK-02 | This journal, manifest and progress pointer | Record and synchronize the census | **Complete: journal, pointer and manifest read back** |

**Measurement scope:** Every numbered line of both files was returned without range gaps or omitted parsed lines (four MCP read chunks per file). Headings, body-section rough word counts, paragraph blocks, footnote definitions and missing footnote identifiers were checked. **Not** a claim-level audit, paragraph mapping, byte-level hash, Markdownlint, incoming-link or anchor validation.

**Current coverage:** earlier [batch 01](WASTES_CLEANUP_PHASE0_NARRATIVE_2026-10-27.md) inventoried `ARC_ONE.md` and `ARC_TWO.md`. This batch adds `ARC_THREE.md` and `ARC_FOUR.md`. **Four of nine narrative files structurally inventoried; five remain**: `ARC_FIVE.md`, `ARC_SIX.md`, `README.md`, `SEASON_TWO.md`, and `SEASON_THREE.md`.

## Results and validation

| Existing narrative file | Complete numbered ranges | Story sections (including prologue / epilogue) | Approx. body words* | Body paragraph blocks | Footnote definitions | Notes start | Broken footnote references |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `narrative/ARC_THREE.md` | **1–155 / 155** | 10 | **3,459** | 43 | **21** | line 111 | **0** |
| `narrative/ARC_FOUR.md` | **1–167 / 167** | 9 | **3,003** | 48 | **21** | line 119 | **0** |

\*Counts are approximate, based on stripping Markdown decorations and targets from body text, excluding `## Notes`, and splitting on Unicode word tokens. Paragraph blocks are nonempty blank-line-separated body text; footnote matches check that every `[^id]` used has a `[^id]:` definition. This is **not** a rendered-text measurement or validation of whether note claims are accurate.

### ARC_THREE.md — chapter/section baseline

| Section start | Section | Approx. words | Blocks |
| ---: | --- | ---: | ---: |
| 5 | Prologue — A crown does not make the world safe | 144 | 2 |
| 11 | I. Stonefall and the metallic visitor | 356 | 5 |
| 23 | II. The Great Fang's ruined coronation | 366 | 4 |
| 33 | III. The family who never reaches sanctuary | 360 | 4 |
| 43 | IV. Beneath Kervalon, behind the doors | 447 | 5 |
| 55 | V. Cerinthala and the living underworld | 363 | 4 |
| 65 | VI. The Eye, the hive, and an impossible future | 407 | 5 |
| 77 | VII. The machine beneath the world | 432 | 5 |
| 89 | VIII. The last chance in space | 411 | 6 |
| 103 | Epilogue — What remains when the light goes out | 173 | 3 |

**Eleven-arc disposition lead, not confirmed paragraph mapping:** Existing Arc Three is the E055–E081 arc; approved **new Arc 05** is E055–E066 and **new Arc 06** is E067–E081. The current title for Chapter IV uses **Kervalon**, whereas owner-approved written canon is **Khaervilon** (D-044). **Flag the title for a later evidence-preserving edit**, not a bulk replacement or a claim that the historical author/source originally wrote it differently. The exact paragraph cut between Chapters III/IV, E066/E067 and supplemental material still requires source links to be traced.

### ARC_FOUR.md — chapter/section baseline

| Section start | Section | Approx. words | Blocks |
| ---: | --- | ---: | ---: |
| 5 | Prologue — After the light | 99 | 2 |
| 11 | I. Strangers in the City of Doors | 355 | 5 |
| 23 | II. A champion made by tricks | 359 | 6 |
| 37 | III. The friends who come back | 356 | 5 |
| 49 | IV. The dragon's price | 355 | 6 |
| 63 | V. Four leap, three arrive | 355 | 6 |
| 77 | VI. A different bargain in White Tower | 409 | 6 |
| 91 | VII. The rescue that becomes a battle | 357 | 5 |
| 103 | VIII. The hand and the road apart | 358 | 7 |

**Eleven-arc disposition lead:** Existing Arc Four covers E082–the E101 White Tower separation, **the same major source range accepted for new Arc 07**. It therefore appears more directly reusable than old Arc Three, but new numbering, heading, balance and compatibility must still pass source-to-scene and inbound-link review. **E101 is one recording shared with future Arc 08**; do not duplicate its scene or infer that all its notes belong only to Arc 07.

### Validation limits and recovery

- **Verified:** numbered-range completeness for both files (4 chunks each), original headings/section starts, body structural metrics, all encountered footnote reference IDs defined, no source edits.
- **Not verified:** working-copy SHA-256; byte sizes, exact paragraph content fingerprints, individual note targets/backlinks, incoming heading anchors, full episode-cue linkage, statement accuracy, scene chronology or acoustic verification. No suitable local command runner was available in this context. Do **not** mark structural metrics as fact-reviewed or approved prose.
- **Failure/recovery:** An interim checkpoint update attempted to replace a `CENSUS-03` row already completed in a preceding call and was rejected by the guarded unique-text editor. The live journal was read again; no story source was modified, and this update resumes only the missing bookkeeping. Do not retry stale replacements blindly.

**Exact next action:** Start read-only Phase 0 census **`narrative/ARC_FIVE.md`**, then `narrative/ARC_SIX.md` in appropriately bounded chunks (its length is much greater). Recheck Git HEAD/status and preserve concurrent changes. Complete other narrative navigation/compatibility pages next; afterward add actual byte hashes, inbound anchor links, source-to-scene trace and full world inventory before any narrative rewrite. The approved eleven boundaries in D-045 are not reopened without owner approval.

**Final checkpoint / concurrency:** Confirmed via local workspace MCP that HEAD remains `5531bd660d0b465f2f658b961f17eccbc33fde56`. The Wastes changes visible in status are the **new report** and the two control updates (`project/WASTES_CLEANUP_MANIFEST.md`, `project/WASTES_CLEANUP_PROGRESS.md`); the two inventoried narratives were not modified. An unrelated Delvers operation concurrently created/modified twelve other visible files; **these were left untouched**. No commit, push, full lint or audio check performed. Readbacks of all three Wastes tracking documents were successful. Historical batch 01 remains unchanged.
