# Report and snapshot retention — consolidation proposal

**Prepared:** 2026-10-29 (Europe/Stockholm). **Status:** inventory and proposal only; **no files deleted, moved or replaced**. **Owner policy:** [D-052](DECISIONS.md) and [repository instructions](../AGENTS.md). **Worktree inspected:** `main`, HEAD `d2ab1273fa8e247f619c64b4ea8332b1f8b5c1e7`, with 29 pre-existing visible staged/modified paths when this inventory began. Preserve those concurrent changes. This is an administrative review, not permission to change story, canon, accepted editorial states or publication.

## 1. Inventory and evidence limits

| Location | Observed root entries | Evidence and limitation |
| --- | ---: | --- |
| `reports/` | 484 | Workspace directory count. The listing interface returns at most 200 entries; search can sample additional reports but not provide an exhaustive path/size/hash listing. **Do not describe all 484 as inspected or byte-classified.** |
| `research/legacy/` | 138 | Complete root listing: **131 files and 7 dated subdirectories**. Contents of dated subdirectories were not inventoried in this pass. |
| `research/legacy/WASTES_CLEANUP_MANIFEST_PRE_*.md` | 16 files | Consecutive, full-text administrative snapshots for batches 97 through 115 (some grouped). |
| `research/legacy/WASTES_CLEANUP_PROGRESS_PRE_*.md` | 16 files | Matching progress-tracker snapshots for the same batches. |
| `research/legacy/DECISIONS_PRE_*.md` | 3 files | Pre-D-049, pre-D-050 and pre-D-051 decisions-ledger snapshots. |
| `research/legacy/ARC_*.md` | 7 files | Historical narrative or before-correction copies; require **individual** source/acceptance classification. |
| Other files at `research/legacy/` root | 89 | Largely `PRE_*` subject/reference backups, plus other historical artifacts. These are **not** automatically redundant. |

The 16 recorded batch suffixes, present in **both** tracker families, are `97`, `98`, `99_100`, `101`, `102`, `103`, `104`, `105`, `106_107`, `108`, `109`, `110`, `111`, `112`, `113`, and `115` (followed by the corresponding date suffix). The three decision snapshots are `DECISIONS_PRE_D049_94_2026-10-28.md`, `DECISIONS_PRE_D050_102_2026-10-29.md` and `DECISIONS_PRE_D051_111_2026-10-29.md`.

The 32 Wastes tracker copies are **repeated versions of living administrative records**, not established byte-identical duplicates. The sampled `PROGRESS_PRE_110` and `PROGRESS_PRE_111` have different line counts (251 versus 253) and successive additions. They have historical information, but the meaningful changes can likely be carried in one concise chronological log. **No complete hash-equality, unique-claim, backlink or link-target census has yet been performed**, so no individual copy is cleared for deletion.

Examples of serial world-reference snapshots to evaluate later: `ANTAGONISTS_PRE_D048_51`–`56`, `CHARACTERS_PRE_D048_67`–`72`, `FACTIONS_AND_POWERS_PRE_D048_63`–`65`, and `WORLD_PRE_D048_58`–`61`. Unlike the tracker sequence, these are original article states across actual content edits; keep their protection until each source's first major-rewrite baseline and meaningful later rewrite boundary are identified.

## 2. Proposed dispositions

| Class | Proposed treatment | Gate before any deletion/move |
| --- | --- | --- |
| **Administrative `MANIFEST_PRE_*` / `PROGRESS_PRE_*` (32)** | First-priority **consolidation candidates**. Build a dated, concise change/decision/recovery ledger from their meaningful state transitions and existing reports. Preserve a true pre-major-restructure baseline if applicable, plus any snapshot carrying uniquely recoverable information. Stop creating new copies; future updates modify active controls in place. | Full content/hash comparison and proof that unique approved decisions, hashes, pending tasks and source pointers survive in canonical records; link/reference scan; explicit owner approval for deletions. |
| **`DECISIONS_PRE_*` (3)** | Second-priority candidates. The active `project/DECISIONS.md` is intended to remain append-only and records supersession. Assess whether each pre-decision copy adds evidence not in that ledger, Git history or approval reports. | Confirm decision IDs D-049–D-051 and their exact owner receipts remain traceable; review uncommitted provenance; obtain deletion approval. |
| **Legacy narrative and major pre-rewrite world-article copies** | **Retain** one exact verified baseline per major rewrite/restructure and retain historically designated first editions, accepted versions and source/scene evidence. A later independent large rewrite can warrant a second baseline. | Check original bytes, stage of rewrite, acceptance/status, source links and compatibility. **Never consolidate by simply keeping the newest file.** |
| **Routine batch execution journals in `reports/`** | Future work should use a **single continuing change/recovery log** with dated entries. Existing per-batch journals may be consolidated after extracting their actual approvals, source-to-scene decisions, checks and corrections. | Complete report path inventory; identify cited documents; preserve unique research/recovery evidence and exact proof of contested edits. |
| **Chapter-pair draft files in `reports/`** | Preserve until each arc's integrated `narrative/ARC_XX.md` has been reviewed against every originating draft, scene boundary, note definition and owner acceptance. Thereafter decide whether draft stages remain useful historical versions; **not currently approved for removal**. | Full textual/semantic comparison; draft provenance, footnotes, owner approval state, immutable accepted SHA pins and all links verified. |
| **ASR comparisons, source investigations, maps, discovery reports and specialist evidence** | **Retain by default** as independently useful research, not routine administrative clutter. Future similar research should be consolidated per investigation where practical. | Evidence-source and reproducibility review; no blanket pruning. |
| **Older dated `research/legacy/YYYY-MM-DD/` archives** | **Retain, out of scope** until individually inspected. | Separate archive inventory and owner-approved migration policy. |

## 3. Specific Wastes narrative safeguards

- Preserve all six original `narrative/ARC_ONE.md`–`ARC_SIX.md` historical first-edition pages and both season compatibility stubs under [D-049](DECISIONS.md); the public navigation switch remains deferred.
- Preserve hash-pinned **provisional unpublished** `ARC_01.md` under D-050 (`a6455256ed1f557669dfcd646a025da29ee62e148f3d27cd664ee2c2508a2a43`) and `ARC_02.md` under D-051 (`01097538b32a6330286014c07952d57292dcb6cde6e6ce5fdc3a66b267ca1ee7`).
- **Arc 03** is staged/in-progress and **not provisionally accepted**. In particular, the staged `reports/WASTES_CLEANUP_D045_ARC03_CHAPTERS_I_II_DRAFT_112_2026-10-29.md`, `reports/WASTES_CLEANUP_D045_ARC03_CHAPTERS_III_IV_DRAFT_113_2026-10-29.md`, `reports/WASTES_CLEANUP_D045_ARC03_CHAPTERS_V_VII_DRAFT_114_2026-10-29.md` and `reports/WASTES_CLEANUP_D045_ARC03_INTEGRATION_115_2026-10-29.md` are dependency evidence for the staged `narrative/ARC_03.md`. The three execution journals for Batches 112, 113 and 114 hold distinct mapping/approval/validation material. **Do not remove or recombine them as part of this proposal.**
- The `research/legacy/ARC_TWO_PRE_ARC03_DRAFT_112_2026-10-29.md` is a documented byte-preserved original for the Arc03/Arc04 split; retain.
- Reports recording D-050/D-051 owner acceptance, source-fidelity repairs (especially Arc02 batch 109), and high-risk chronology/knowledge corrections are **protected evidence**, even if their administrative status can later be summarized more concisely.

## 4. Suggested execution sequence (requires separate owner authorization before removal)

1. **Finish exact inventory using a capable local listing/hashing runner**: enumerate all `reports/` paths and dated legacy folders, file sizes, SHA-256, tracked/untracked status and reference counts. The currently available workspace listing is capped at 200 entries per directory; do not infer the omitted names. Capture inventory in a compact machine-readable manifest **outside `reports/`**, updated in place. Do not package raw source/audio or private data.
2. **Establish an administrative retention set**: compare each of the 16 manifest and 16 progress snapshots against preceding/succeeding versions and the current controls. Identify their distinct state transitions and any uniquely retained owner decisions or blockers. Preserve major pre-rewrite baselines and archival pointers.
3. **Build one concise Wastes change history** (dated event / affected paths / owner decision / rationale / source link / outcome / significant validation / unresolved item), using existing `project/DECISIONS.md`, `WASTES_CLEANUP_MANIFEST.md` and reports as authorities. Do not repeat full tracker contents or whole chapter prose.
4. **Prepare an exact reviewable removal manifest**, identifying each file, SHA-256, replacement evidence location, inbound references and a reason; group by low-risk administrative copies first. Mark every uncertain item `retain`, not `remove`.
5. **Seek explicit owner approval of that file-level removal list.** Only afterward perform bounded deletions/moves, update links, run targeted Markdown/link tests, and verify clean preservation of accepted narrative versions and uncommitted work. No commits, publication or story changes are implied.

## 5. Continuing policy

From D-052 onward, a **new report is not the default deliverable of a task** and a new `PRE_*` copy of the manifest/progress/decision ledger is not the default preservation mechanism. Create a single exact pre-transformation snapshot **when a major rewrite actually starts**, reuse it within the effort, and keep a human-readable change/decision log. Recovery of routine edits should rely on Git diffs/guarded readbacks and in-place checkpoints. Historical reports cannot be removed merely because this policy is now in effect.
