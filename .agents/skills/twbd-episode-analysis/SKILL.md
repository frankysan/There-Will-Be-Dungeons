---
name: twbd-episode-analysis
description: Analyze and document There Will Be Dungeons episodes from available recordings and transcripts, including The Wastes, Inverse, Delvers, standalone one-shots, and out-of-game bonuses. Use for next-episode research, episode dossiers, ASR comparisons, continuity updates, and listening-review queues. Do not use for unrelated podcast questions or generic D&D research.
---

# TWBD episode analysis — source-first research across campaigns

## Trigger and scope

When asked to "proceed", "continue", or analyze a named episode, **complete one bounded source episode or bonus per pass** unless the user explicitly requests a different batch. Treat an explicitly supplied corrected episode ID or bonus label as authoritative. Resolve vague "next" against the requested campaign's **next bounded research** pointer and actual sources, rather than automatically advancing The Wastes. If several campaign queues are equally plausible, ask which while inspecting available inventories. Never manufacture filenames or extrapolate publisher episode numbers.

This skill follows the repository's existing policies. Consult only the applicable parts of:
- [Transcription workflow](../../../project/WORKFLOW.md)
- [Editorial/canon guide](../../../project/EDITORIAL_GUIDE.md)
- [Documentation architecture](../../../project/DOCUMENTATION_ARCHITECTURE.md)
- [Corrected numbering](../../../project/EPISODE_NUMBERING.md)
- [Open research queue](../../../project/REVIEW_QUEUE.md)
- [ASR experiment log](../../../project/MODEL_TESTS.md)
- The selected campaign's index, dossiers and consistency ledger; [the Wastes ledger](../../../world/CONSISTENCY_LEDGER.md) applies to Wastes research.

**Important:** Those relative links are from this SKILL.md inside .agents/skills/twbd-episode-analysis; the project documents themselves use repository-relative links appropriate to their own directory.

## 1. Establish the state before reading sources

1. Read Git status/branch/HEAD where available; preserve unrelated edits and never assume the checkout is clean. Identify the selected campaign's coverage, last dossier, next unresolved ID and relevant profiles. If an access method cannot expose working-tree state, state that limitation rather than claiming a clean checkout.
2. Establish **campaign, season, corrected archive ID, original publisher ID/title, and episode type** separately. Types include played campaign session, standalone/holiday one-shot, retrospective/roundup, Q&A, and other out-of-game discussion. A Wastes-prefixed filename can still be a one-shot or roundup. A bonus can discuss several campaigns. Classify from metadata and content, not filename alone.
3. Find the **exact** source filenames. Main Wastes files resemble `sources/The Wastes S1E###. Title.parakeet.processed.srt`; other exports may contain `qwen-q8.canary-ctc.nemotron`. Bonus files use public-publication-month labels but **not necessarily recording dates**. Consult the numbering crosswalk and owner-normalized inventory for other seasons, Delvers and one-shots; never assign them Wastes S1 `E###` IDs.
4. Locate all available exports and their matching audio/copy, including raw/processed variants and additional ASR models. Record unavailable or partial sources. One export supports provisional research; do not require two or claim an independent comparison from duplicate/derived copies. Do not silently substitute a different episode, year, season or campaign.

### Choose access by capability and source freshness

Use **all viable file-access methods available in the session**, including direct filesystem access, GitHub and MCP. Assess their capabilities and use them wherever they supply needed evidence or editing support; do not restrict the workflow to one provider or fetch identical bytes through every route just to exercise it. Prefer an available service connector for service operations; direct filesystem tools are appropriate for the shared checkout.

| Access route | Useful capabilities | Limits and revision checks |
|---|---|---|
| **Direct filesystem / shell** | Discover with `rg --files`, narrow text searches, bounded UTF-8 reads, local Git state/diffs, ignored/local-only sources, scripts, safe patches and parent-directory creation | Read workspace instructions first (including the RTK shell convention where applicable). Preserve unrelated changes and original media/ASR. Local files can differ from GitHub or an MCP workspace |
| **Connected GitHub tools** | Discover repository files, read tracked sources/docs at an explicit ref, inspect remote history and revisions | Discover actual tool schemas; `fetch_file` is an available example, not a guaranteed universal API. Pin a branch/commit and record it. Default-branch content does not prove local synchronization; GitHub cannot supply ignored or uncommitted files |
| **Workspace MCP** | Discover/search/read current workspace material, including permitted local files; use supported text/binary/PDF/archive readers and guarded edits | Discover current tool capabilities and workspace root. The **InfinityDB OAuth Probe** can expose this repository despite its name; paths can require `There Will Be Dungeons Transcripts/...`. Its workspace may differ from the direct checkout; verify identity/revision before combining them |

For that MCP, useful tools include `git_status`, `list_workspace`, `search_workspace`, `read_workspace_file`, `read_workspace_binary`, `read_workspace_pdf_pages`, `list_workspace_zip_members`, `read_workspace_zip_member`, `replace_workspace_text` and `create_workspace_file`, when exposed. Use narrow searches and bounded reads; do not scan the entire `local/` audio collection unnecessarily. Reading binary data does not mean listening.

Keep an input inventory with access route, exact path, repository/ref or workspace identity, model label, audio-copy association and any unresolved version differences. Compare commits or file hashes when necessary to establish equivalence. Limit retries after failures and switch to another viable route; an unavailable connector is not a blocker when direct files or a suitable pinned remote version suffice. Never silently mix revisions. If only remote evidence is available, report its revision and the unverified local state. Reuse permitted local provenance manifests before refetching linked materials; private archives remain local and unchanged, with no raw private messages uploaded or added to Git.

## 2. Research the entire recording within one source episode

Read the primary transcript and each independent export used for full-episode claims **through the final speech/outro**, not just opening excerpts. Chunk by **recording clock** (e.g., 5–12 minutes per excerpt) to avoid truncation. Identify missing/truncated portions and distinguish complete-episode coverage from a selected-window comparison. For played material, collect who acts, scene transitions, GM declarations, party separation and what remains true **at the episode cutoff**. For out-of-game material, map topics, questions, attributed answers, production discussion and teasers instead of imposing a scene/quest structure. Split mixed recordings into typed, timestamped sections.

Maintain a working evidence map with approximate timestamp, speaker/role if supportable, claim/action, confidence and cross-source conflicts. Keep separate:
- **Observed/GM-adjudicated played actions and outcomes**.
- **NPC testimony and character beliefs**, including lies or errors.
- **Player speculation, jokes, unused branches and game-rule discussion**.
- **Retrospective GM/cast statements**, which may illuminate past events but aren't additional played scenes.
- **Unresolved ASR wording/proper-name alternatives**, pending listening.

Do not fill unexplained gaps with presumed offscreen actions. Distinguish **intended**, **attempted**, **scheduled/promised**, **performed**, **observed** and **completed**. Explicitly track item custody, spell-scroll usage, deaths and resurrection, physical locations, private versus shared knowledge, rituals, contracts, and changes to an earlier cliffhanger. Do not use future bonus-episode spoilers to assert outcomes in earlier main-story episodes.

Keep **The Wastes**, **Inverse**, **Delvers**, each standalone adventure and the **out-of-game publication timeline** separate. Shared cast, similar names, rules or a common recording do not establish shared continuity. Supporting Inverse planning documents and Delvers guild material apply only within their documented scope; plans and upcoming-campaign teasers are not played events. Bonus publication labels do **not** prove recording dates. Keep recording-clock offsets distinct from story time and publication order, especially across copies with different advertising.

## 3. Independently compare ASR exports

For each input, record the exact filename, cue count, last end timestamp, normalized token count, and model/pipeline label **as inferred from the filename**, distinguishing those labels from verified run metadata. Compute measurements where tools permit; otherwise mark them unavailable. Do not invent build flags, model versions, GPUs, performance, hashes or audio provenance. If only one independent export exists, document single-source limitations and targeted listening questions instead of producing a comparison figure.

For the project's established reproducible full-episode comparison:
1. Extract SRT cue content in chronological order, discarding cue indices and timing lines.
2. Remove optional `(speaker N)` decorations; join cue text.
3. Lowercase; remove straight/curly apostrophes (join contractions); replace characters other than Unicode letters and digits with whitespace; split into word tokens.
4. Compute **unit-cost ordered word-level Levenshtein distance** between complete token sequences, using a reliable exact implementation or a rigorously validated bounded optimization; report edits / **primary Parakeet token count** and percentage when Parakeet is primary. Otherwise name the chosen reference export and denominator explicitly, including comparison direction. With more than two exports, label each measured pair; do not treat a model majority as truth. Use existing comparison tooling only after verifying its metric and normalization match the report; alignment/candidate counts are not automatically this distance.
5. Describe **specific high-risk disagreements with recording timestamps**: divergent names, apparent deletions, stage/cure mechanics, speaker mapping, scene boundaries, contradictory dialogue and stray ending cues. Keep findings **text-only** until audio is checked.

**Never call inter-model disagreement WER, accuracy, confirmed omissions or hallucinations.** Neither agreement nor token-count advantage proves correctness. If computational tools or a complete source are unavailable, **say comparison not computed** instead of fabricating a figure. If manually listening, identify exactly which windows and evidence were checked and distinguish them from untouched windows.

### Reusable episode preparation (when local Python execution is available)

Use `tools/prepare_episode.py` to parse complete SRTs and prepare small, timestamped windows **before remote/manual editorial reading**. It reuses `build_transcripts.parse_srt`, the exact shared `asr_metrics` normalization/distance (also used by the older ASR backfill), and the established separate time-aware alignment. Example for a verified matching pair:

`python tools/prepare_episode.py --id E121 --primary "sources/<verified-primary-name>.srt" --secondary "sources/<verified-secondary-name>.srt" --out local/episode-analysis/E121`

Replace placeholders with **actual** discovered filenames; never guess the source basename. Use `--window-minutes 10` (default), `--max-review 30`, or `--no-alignment` when the exact global metric is needed without expensive candidate alignment. For single-source coverage, omit `--secondary`. `local/` is ignored by Git. Inspect `summary.md` and `summary.json`, read **every primary window** to form narrative claims, and use `candidates.json` to target second-export disagreements; if claiming complete interpretive coverage of both exports, examine both throughout instead. All candidate classifications are **unverified hypotheses**. The command reads source files without modifying them; a matching existing output is reused, while changed inputs/options or partial outputs require a **different fresh output directory**, not silent replacement. Store paths/hashes and reviewed-window progress in the phase checkpoint. If Python execution is unavailable, follow the existing bounded-reader approach rather than claiming this script ran.

## 4. Write only the documentation justified by the episode

Create/update these layers **in priority order**, using existing adjacent episode conventions as examples:

**Core, almost always**
1. A source-first dossier in the appropriate namespace (see routing below): timestamped scene or topic sequence, actual cutoff, competing interpretations, and targeted listening questions.
2. A dated comparison report when independent exports exist: retain established names such as `reports/E###_ASR_COMPARISON_YYYY-MM-DD.md` for Wastes S1; qualify new report names by campaign/adventure, season and episode to avoid collisions. Log normalization/method, measurements, substantive disagreements and limitations. Update `project/MODEL_TESTS.md` with a compact experiment entry.
3. `project/REVIEW_QUEUE.md` or the established campaign queue: retain unresolved spellings/causality and a verified, campaign-qualified pointer to the **next source**, and mark the just-researched episode as **ASR-provisional**. If no next source is available, state that rather than inventing one.

**Wastes main-campaign follow-through (only material changes)**
4. `world/CHRONOLOGY.md` and `world/CONSISTENCY_LEDGER.md`: compact major-event/cutoff changes and previously unresolved statuses, avoiding repeated full retellings.
5. The appropriate narrative, `narrative/ARC_ONE.md` through `ARC_FIVE.md` (see `narrative/README.md` for boundaries): readable connected scenes for main episodes if warranted; prefer consolidation over adding a full duplicate dossier per chapter.
6. Affected `world/characters/*.md`, `world/places/*.md` and relevant artifact/thematic pages; edit only those whose evidence or current status changes.
7. `world/CHARACTERS.md`, `world/PLACES.md`, `world/README.md`, `narrative/README.md`, root `README.md`, or architecture document: update **only outdated navigation, spoiler horizon or summaries**, not every file automatically.

During each Wastes episode review, **record Vorel's titles and epithets as they are named** in [his source-indexed register](../../../world/characters/vorel-titles.md). Add each distinct title or wording variant with its earliest known episode, approximate timestamp/cue, speaker and source confidence. Preserve the wording supported by the source; mark ASR-only or uncertain wording as provisional. Distinguish self-proclaimed titles, companion usage, granted titles and formal recognition. Record repeat uses when wording or status changes, and do not backdate titles from later introductions. Follow the [editorial guide's title policy](../../../project/EDITORIAL_GUIDE.md#named-equipment-and-self-bestowed-titles-2026-10-22).

During each Wastes episode review, also **record Nash's improvised spellcasting phrases and rhymes** in the separate [phrase register](../../../world/characters/nash-spellcasting-phrases.md), linked from his main character page. Capture each distinct phrase or meaningful variant with corrected season/episode, approximate recording time/cues, source-supported wording, spell/ability or item when identifiable, performer/character attribution, exact source links and confidence. Preserve unfinished rhymes, interruptions, companion-supplied endings and competing ASR readings; never repair a rhyme or infer exact dialogue without listening. Distinguish performed/attempted casting, character abilities, item activations, proposed/rejected wording and retrospective recollection. Record unchanged repeats by reference, and keep later-season spoilers separate. The register owns the collection; do not expand Nash's biography with a duplicate list. Follow the [editorial phrase policy](../../../project/EDITORIAL_GUIDE.md#nashs-spellcasting-phrases-and-rhymes-2026-10-23) and keep older-episode backfill separate from the active episode-research pointer.

### Route by continuity and episode type

Use existing namespace conventions first. The locations below for new campaign/one-shot coverage are **fallback conventions, not claims that directories already exist**. If none exists, create only the needed dossier directory and a small discoverable index using an available write method; do not build empty world/narrative scaffolds. Retain exact season/episode identity and prevent filename collisions. Existing paths and owner IDs take precedence; do not migrate prior dossiers just to match a fallback.

| Material | Dossier location and follow-through |
|---|---|
| **The Wastes played sessions** | Existing S1 `episodes/E###.md`; later seasons use their established convention, or season-qualified `episodes/wastes/S2E###.md` / `S3E###.md` when none exists. Update Wastes chronology, ledger, arcs and affected profiles only as justified |
| **Inverse** | Existing `inverse/episodes/...` and `inverse/README.md`; keep its continuity and reference updates within `inverse/` |
| **Delvers** | Start with the [campaign index](../../../delvers/README.md), [source inventory](../../../delvers/SOURCE_INVENTORY.md), [documentation plan](../../../delvers/DOCUMENTATION_PLAN.md) and [Delvers queue](../../../delvers/REVIEW_QUEUE.md). Use `delvers/episodes/S<season>E<episode>.md` with the actual corrected ID, preserving S2E00. Its Wastes-scale world/narrative layers belong within `delvers/` and grow from researched evidence. Keep played evidence separate from guild handouts/planning; inventoried exports are not completed dossiers. The Delvers queue owns its next episode; preparation does not switch the Wastes pointer |
| **Standalone/holiday one-shots** | Retain existing special dossiers such as Wastes-numbered E043. For new unrelated adventures use an established namespace, or `oneshots/<adventure-slug>/episodes/<verified-id>.md`; keep a multipart adventure together and distinct adventures separate. Record GM, cast/characters, setting and outcome without assuming any Wastes/Delvers connection |
| **Out-of-game bonuses, roundups and production episodes** | Existing `episodes/BONUS-YYYY-MM.md` when that corrected ID applies; retain owner-normalized titles and date suffixes where needed to distinguish same-month recordings. Otherwise use a verified category-qualified ID. Organize by topics and attributed commentary, not fictional scenes; do not insert commentary into a campaign chronology or narrative chapter |

For played Inverse, Delvers and standalone material, apply the same evidence standard as Wastes to any existing campaign chronology, continuity ledger, narrative and affected profiles, within that campaign's namespace and only for material changes. Do not create those layers merely to fill a template.

For cross-campaign bonuses, tag each claim by campaign (or **unassigned**), evidence type and spoiler horizon. Reference affected profiles with dated retrospective attribution without backdating character knowledge. If a recording includes actual play, document that section under its supported continuity and cross-link it; a bonus label alone does not make played material commentary. Update root navigation only when a new index or coverage change needs discovery. Never use another campaign's dossier as lore corroboration without separately supported evidence of a connection.

Canonical spelling follows the project's tiered written/owner decisions (e.g., the **one Eye of Groxl**), but original raw ASR readings remain traceable. Cite the original episode source, appropriate dossier and comparison report with working **relative** links.

## 5. Bounded execution, resumability and guarded edits

**One episode is a research unit, not a required single-turn transaction.** For a high-latency workspace, complete at most the next feasible phase, persist a checkpoint, and stop cleanly when the remaining budget cannot cover another phase. A later `proceed` resumes the **same episode and first incomplete phase**; it must not restart all source reading or advance to a new episode. A fast local execution may complete several phases in one invocation. No background continuation is implied.

### Phases and completion gates

| Phase | Work | Completion gate |
| --- | --- | --- |
| **0. Resume and identify** | Inspect campaign queue, existing dossier/report, prior progress, Git status and exact sources; select the first incomplete phase. | Existing work and revisions understood; no unnecessary reread or overwrite. |
| **A. Source evidence** | Read the primary export across the entire recording, process independent exports as required for claimed scope, inventory provenance, calculate supported ASR measurements, and build timestamped evidence/cutoff notes. | Every claimed full-export source has verified beginning/end coverage; any unexamined windows or incomplete metrics explicitly recorded. |
| **B. Core publication** | Write or finish the source-first dossier and comparison report (where supported), compact model-test entry and appropriate campaign queue/pointer. | Core files read back; cutoff, evidence limitations and next-source pointer agree. Do not move the researched-episode pointer before this gate. |
| **C. Continuity and narrative** | Update only material chronology, consistency-ledger and arc narrative changes. | No contradictory prior cutoff/major status or duplicated episode retelling in the edited sections. |
| **D. Entity integration** | Update only changed subject pages, Vorel/Nash registers when a qualifying finding exists, and genuinely stale navigation. | Material entities and links reconciled; unrelated encyclopedia pages untouched. |
| **E. Bounded validation** | Reuse prior readbacks and source hashes; check only changed/new files and cross-document cutoffs, then run targeted checks only where a suitable runner exists. | **Editorial verification** and **automated validation** reported as separate statuses. Checkpoint pending checks without redoing phases A–D. |

**Durable checkpoint, not just chat state:** At each phase boundary, record campaign/season/episode/type; phase completed and next phase; source paths, hashes or equivalent revision IDs; which recording windows and exports were actually reviewed; computed-versus-pending comparisons; files created/edited; unresolved evidence and immediate next action. Prefer `local/episode-analysis/<campaign-and-id>.json` when a local filesystem can write private untracked files. If that route is unavailable, use a clearly marked, short `Research progress (provisional)` section in the existing/new episode dossier; create it inside an existing permitted directory when necessary. Do not claim that an in-chat summary or a failed/unavailable checkpoint was saved. Minimize checkpoint writes to phase boundaries or an imminent stop; do not repeatedly rewrite a large dossier per transcript chunk. Once complete, mark the checkpoint complete or remove a temporary in-dossier progress section without erasing research evidence.

**Restart rules:** Inspect current status/checkpoint before reading any full SRT. Check source hashes/revisions **once at source-preparation time** (or reuse a recorded, still-trustworthy fingerprint); reuse already-computed comparisons/evidence maps when valid. Do **not rehash or refetch entire sources during final validation** merely because the repository HEAD advanced: first determine whether the source paths changed; if genuinely uncertain, prefer one cheap workspace metadata/hash query per affected source. If sources changed, invalidate only dependent phases. If concurrent edits changed an output, reconcile that narrow area rather than clobbering it. For earlier incomplete work (including an existing dossier and report), continue the missing phase instead of starting over. **For a validation-only resume, inspect the saved validation checklist and outstanding items; never reread source transcripts or repeat phases A–D.** A provisional partial source review must not be described as full-episode coverage.

### Remote-call and context budgets

- Plan for **roughly 25 remote connector calls per invocation**, counting actual calls even when batched; this is an operational soft budget, not a reason to omit evidence. Stop at a safe checkpoint rather than starting a stage that cannot reasonably finish. For large source reads, checkpoint after a bounded set of recording-clock windows and resume the next window in a later invocation.
- Prefer **1–2 concurrent remote calls** (never more than 3 by default); keep sequential read/modify/readback operations on the same file. Limit transient error retries to one before checking the cause or switching to another valid route. Record call latency/size when measurable; do not invent timing data.
- Read one exact directory/prefix or file range instead of a repository-wide text scan. Prefer locally parsed SRTs, reusable source inventories, existing comparison artifacts and targeted timed excerpts over repeatedly moving entire exports through a high-latency connector. If the only route is chunked MCP binary reads, use the largest safe supported chunk with bounded recording-clock coverage and verify complete extraction.
- For large indexes, ledgers, narrative chapters and character files, inspect only the relevant headings and narrow change context; make one well-scoped replacement per changed section, not many micro-edits. Re-read changed passages for verification rather than fetching whole documents repeatedly. Do not fetch the same bytes through GitHub and MCP merely to exercise both routes.
- Keep an impact list before editing: **required core outputs**, **materially affected reference files**, **optional later consolidation**. An episode should not touch every character, place, index, and summary just because they exist. Explicitly defer nonessential editorial cleanup rather than silently skipping required canon corrections.
- **Validation-only remote budget:** reserve **at most about 8 additional connector calls** for phase E by default (one status, essential new-file/readback spot checks, and at most source-fingerprint checks for genuinely changed/uncertain inputs). Count the calls already spent on readbacks during phases B–D as verification; do not repeat them. If checks cannot fit, checkpoint the precise remainder and resume **only validation** later. Do not sacrifice a known material integrity issue just to meet the budget.

**Prefer local working-tree edits** when that checkout is current; direct patches and supported MCP edits are both valid. Do not silently commit, push, rebase or overwrite unrelated work. GitHub read access does not authorize remote writes. Keep each `replace_workspace_text` small, with a **unique old_text anchor**, and do reads/edits **sequentially for the same file**. A denied, ambiguous, missing or stale replacement is **not** a success: re-read the narrow affected range, retry only with an actually corrected unique anchor, or switch to an available authorized write route. Report a blocker only if no viable route remains.

For new nested folders, the local MCP `create_workspace_file` requires an existing Git-tracked parent directory. Use direct filesystem creation when available, or another supported authorized mechanism. If all available writes are restricted, supply a reviewable patch or draft and explain which files/directories still need applying; do not claim they exist. If local MCP checks only support **InfinityDB-specific** commands, **do not run them as The Wastes test suite**.

## 6. Validation and final response — fast, incremental, auditable

**Separate three outcomes rather than treating all validation as one blocking task:** **(1) editorial checks complete**, **(2) automated checks passed / failed / not run**, and **(3) optional full-repository audit deferred**. A source-backed episode may be *documented, ASR-provisional, editorially checked* when no general-purpose runner exists; it must **not** be described as having passed lint/tests. Known broken links, conflicting cutoffs, corrupted source inputs or incomplete critical edits are real blockers, not optional checks.

### E1. Mandatory bounded editorial checks (use prior readbacks)

1. Use the already-known list of edited/new files and **one final Git status**; confirm no original media/SRT appears changed. If a diff command is available, inspect the **changed hunks** (not entire files). If no diff is available, reuse the narrow readbacks from phases B–D and selectively inspect only previously unverified changed sections or newly created pages. Do not read back a page twice solely for reassurance.
2. For the **core dossier/report/queue**, check corrected episode ID, main narrative cutoff, uncertainty labels, source references and next-episode pointer. For high-risk integrations, check only the material changed claim or item custody, and the **relative link targets newly added or modified**. Check a representative/new Markdown table for column consistency. Do not rescan every character, index and long narrative chapter.
3. **Source fingerprint is a phase-A result, not an automatic phase-E task.** Reuse the recorded SHA-256/size. If HEAD advances or the working tree changes for unrelated files, note that fact without fetching source exports again. Only if a **source path actually changed or source equivalence remains unverified** do a narrow workspace metadata/size/hash query, once per affected source if available (not a full GitHub re-fetch); record any unavailable comparison as such.
4. If E1 risks exhausting the **~8-call phase-E budget**, record an explicit `validation pending` checkpoint listing exact files/checks remaining, stop and resume **only those checks** next turn. An already accepted/verified hunk stays verified unless the file changes again.

### E2. Automated checks when executable

- For changed maintained Markdown, prefer one **targeted local** command such as `npm run lint:markdown -- --files episodes/E125.md reports/E125_ASR_COMPARISON_2026-10-24.md world/CHRONOLOGY.md` (substitute the actual changed Markdown paths). The script accepts explicit maintained paths, checks only those files, and is **read-only** in this mode. `npm run lint:markdown` without arguments remains the **full** repository run for CI/release. The `.agents/skills/` tree is not in this maintained-docs linter scope; do not claim it was linted by that command.
- Run relevant Python/unit tests **only when Python/tools changed** and a suitable local runner exists. Do not run unrelated repository tests as episode-validation ritual. For new namespaces outside the maintained Markdown roots, report the linter coverage limitation and validate those files separately where a runner permits.
- If the connected tool offers **no general-purpose command runner**, establish that limitation **once** and write `automated checks not run (no suitable runner)`; do not repeatedly try InfinityDB-specific tests, distant CI queries, alternate shells or excessive connector reads as substitutes. Leave local/CI checks clearly pending without blocking the finished editorial integration.

### E3. Full or cross-repository audit (separate, optional)

Full Markdownlint, complete broken-link scans, wide consistency sweeps, security audits and all-suite Python checks run as **separately requested/release/CI work**, not automatically after every episode. When the user requests those checks, report their scope, results and unresolved errors instead of marking them silently passed.

**Final response:** State exact campaign/season/episode/type, new findings, changed files and calculated ASR disagreement when available, then report **editorial verification status**, **automated check status** and **deferred checks** separately. Do not claim a commit, push, audio confirmation, passing tests, or perfect link integrity without having performed them. Do not reopen completed research to replace a missing runner with additional transcript reads.

## Quick invocations

- `$twbd-episode-analysis E098` — process the corrected episode from both available ASR exports.
- `$twbd-episode-analysis Bonus 2020-05` — process a publication-month bonus as retrospective, not a main-story episode.
- `$twbd-episode-analysis next` — follow the verified research pointer and exact source directory.
- `$twbd-episode-analysis Inverse S1E02` — separate campaign, separate canon.
- `$twbd-episode-analysis Delvers S1E01` — resolve the actual source and season ID; keep Delvers separate from Wastes.
- `$twbd-episode-analysis Star Trek one-off` — find the exact corrected label and use a standalone adventure namespace.
- `$twbd-episode-analysis The Wastes Round Up` — classify retrospective discussion separately from played events.

For ordinary conversation with access to this repository skill: **"Use the twbd-episode-analysis skill for E098."**
