# The Wastes — artifact disposition manifest

**Purpose:** Record which maintained artifacts exist, which paths must remain compatible, and where exact preservation originals live. **Do not record task completion here.** The single canonical checkbox/task tracker is [Wastes cleanup tasks](WASTES_CLEANUP_TASKS.md). This is a **live disposition overview**, not an exhaustive verified per-file inventory; the remaining inventory work is [WCL-013](WASTES_CLEANUP_TASKS.md#wcl-013).

The former 858,462-byte cumulative batch/inventory research record was preserved **unaltered** before this structural consolidation: [historical manifest, 2026-10-31](../research/legacy/WASTES_CLEANUP_MANIFEST_PRE_TASK_REGISTER_2026-10-31.md). Earlier dated reports and evidence references retain their provenance. See [historical changelog](../research/legacy/WASTES_CLEANUP_CHANGELOG_PRE_TASK_REGISTER_2026-10-31.md) for batch-level context. The repository is **private**; private reading access is not an external/public website release.

## Maintained artifact dispositions

| Artifact or path set | Disposition / compatibility contract | Task reference |
| --- | --- | --- |
| `narrative/ARC_01.md`–`ARC_11.md` | Current eleven-arc private reader edition; retain accepted episode boundaries and editorial source links | [WCL-002](WASTES_CLEANUP_TASKS.md#wcl-002) |
| Six original word-form `narrative/ARC_*.md` files | Byte-preserved historic edition, readable at unchanged paths; not to be overwritten by current numbered arcs | [WCL-003](WASTES_CLEANUP_TASKS.md#wcl-003) |
| `narrative/SEASON_TWO.md`, `narrative/SEASON_THREE.md` | Compatibility entry points, not additional arcs or independently verified recordings | [WCL-003](WASTES_CLEANUP_TASKS.md#wcl-003) |
| Root / Wastes / narrative reading entry points | Active private-edition navigation; external site deployment not claimed | [WCL-004](WASTES_CLEANUP_TASKS.md#wcl-004) |
| `world/RACES.md`, initial `world/races/` pages | Pilot people/culture domain; remaining peoples and completeness not presumed | [WCL-009](WASTES_CLEANUP_TASKS.md#wcl-009), [WCL-012](WASTES_CLEANUP_TASKS.md#wcl-012) |
| `world/ENTITY_SCHEMA.md`, `world/entities.json` | Race/culture v2 pilot with compatibility; not an all-campaign complete knowledge graph | [WCL-010](WASTES_CLEANUP_TASKS.md#wcl-010), [WCL-035](WASTES_CLEANUP_TASKS.md#wcl-035) |
| Selected rewritten world places, technology and biographies | Maintained subject pages at their original stable paths; preserve original chapter/heading/slug links and source-bearing footnotes | [WCL-014](WASTES_CLEANUP_TASKS.md#wcl-014)–[WCL-030](WASTES_CLEANUP_TASKS.md#wcl-030) |
| `world/characters/vorel.md` and [pre-WCL118 original](../research/legacy/VOREL_PRE_WCL118_2026-10-31.md) | Current reader-first biography at its stable path; all original research-body bytes, 44 heading texts and 205 link occurrences retained in the historical appendix. One exact pre-rewrite baseline preserved separately; native/browser heading behavior remains untested | [WCL-118](WASTES_CLEANUP_TASKS.md#wcl-118) |
| `world/characters/stanley-billings.md` and [pre-WCL119 original](../research/legacy/STANLEY_BILLINGS_PRE_WCL119_2026-10-31.md) | Current eleven-arc biography at its stable path; original body retained in historical appendix with only two introduction/development heading labels distinguished. Original fragment names retained on corresponding new main headings; all 155 original links and nine source notes retained. One exact pre-rewrite baseline preserved; native/browser compatibility remains untested | [WCL-119](WASTES_CLEANUP_TASKS.md#wcl-119) |
| [Badass T](../world/characters/badass-t.md), [Tedna](../world/characters/tedna.md), character index | New dedicated alternate-counterpart reader profile: first encountered E106, last directly depicted S2E09; later mentions are not appearances. Original Tedna page/heading routes remain byte-preserved. Separate index rows retain the old E110 combined-row footnote ID and source destination; no route move or entity-pilot change | [WCL-120](WASTES_CLEANUP_TASKS.md#wcl-120) |
| `world/CHRONOLOGY.md` and technical ledgers | Intentional source-keyed technical exceptions to ordinary story-first biographies; historical episode cutoffs retain their dates | [WCL-028](WASTES_CLEANUP_TASKS.md#wcl-028), [WCL-040](WASTES_CLEANUP_TASKS.md#wcl-040) |
| [Nash E112-E128 phrase-discovery inventory](../reports/NASH_PHRASE_BACKFILL_E112_E128_2026-10-31.json) | One research evidence artifact: exact local export metadata/hashes, candidate and read-window cues, dispositions and limits. Supplements the preserved E000-E111 discovery inventory; neither original sources nor a full-episode/audio verification substitute | [WCL-051](WASTES_CLEANUP_TASKS.md#wcl-051) |
| `world/CONSISTENCY_LEDGER.md`, `project/REVIEW_QUEUE.md` | Source/issue tracking remains distinct from cleanup tasks; unresolved issue IDs must not be silently discarded | [WCL-036](WASTES_CLEANUP_TASKS.md#wcl-036) |
| `sources/`, historic reports, accepted originals and private assets | Preserve original evidence and authorization boundaries; original recordings/ASR are not rewritten by cleanup | [D-052](DECISIONS.md) |
| `research/legacy/` one-time major-rewrite originals | Evidence archives are not worklists. Retain SHA-verified before-state snapshots and their stable source paths | [D-052](DECISIONS.md), [WCL-042](WASTES_CLEANUP_TASKS.md#wcl-042) |

## Lifecycle and source of truth

An individual file can be **not inventoried**, **inventoried**, **retained as a technical exception**, **edited**, **structurally validated**, **fact reviewed** or **accepted**. These are different evidence gates; a Markdownlint pass is not audio or factual approval. Add **per-file dispositions only when the inventory is actually examined**, and point their active work to one `WCL-###` task. Keep links/aliases and content migration evidence in the original article, original archive or an independently useful report—not copied into three task summaries.

- **Work status and next step:** [WASTES_CLEANUP_TASKS.md](WASTES_CLEANUP_TASKS.md).
- **Owner approvals and policy:** [DECISIONS.md](DECISIONS.md).
- **Meaningful dated milestones only:** [WASTES_CLEANUP_CHANGELOG.md](WASTES_CLEANUP_CHANGELOG.md).
- **Old detailed execution history:** [preserved manifest](../research/legacy/WASTES_CLEANUP_MANIFEST_PRE_TASK_REGISTER_2026-10-31.md), [preserved progress](../research/legacy/WASTES_CLEANUP_PROGRESS_PRE_TASK_REGISTER_2026-10-31.md) and [preserved changelog](../research/legacy/WASTES_CLEANUP_CHANGELOG_PRE_TASK_REGISTER_2026-10-31.md).

**Editing rule:** Do not append a new batch narrative or repeated validation receipt to this document. Update it only for an actual file creation, preservation/disposition or compatibility change. Historical chapter crosswalk and retention indexes remain at their dedicated paths.
