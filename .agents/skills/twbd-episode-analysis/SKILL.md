---
name: twbd-episode-analysis
description: Analyze and document the next or a specified There Will Be Dungeons episode (The Wastes, a monthly bonus Q&A, or Inverse) from local MCP ASR transcripts. Use for "proceed with episode", new episode dossiers, Parakeet/Qwen comparisons, narrative and continuity updates, and targeted review queues. Do not use for unrelated podcast questions or generic D&D research.
---

# TWBD episode analysis — source-first, incremental MCP workflow

## Trigger and scope

When asked to "proceed", "continue", or analyze a named episode, **complete one bounded source episode or bonus per pass** unless the user explicitly requests a different batch. Treat an explicitly supplied corrected episode ID or bonus label as authoritative. Resolve vague "next" against the current documentation's **next bounded research** pointer and the actual source directory; never manufacture filenames or extrapolate publisher episode numbers.

This skill follows the repository's existing policies. Consult only the applicable parts of:
- [Transcription workflow](../../../project/WORKFLOW.md)
- [Editorial/canon guide](../../../project/EDITORIAL_GUIDE.md)
- [Documentation architecture](../../../project/DOCUMENTATION_ARCHITECTURE.md)
- [Corrected numbering](../../../project/EPISODE_NUMBERING.md)
- [Open research queue](../../../project/REVIEW_QUEUE.md)
- [ASR experiment log](../../../project/MODEL_TESTS.md)
- [Active consistency ledger](../../../world/CONSISTENCY_LEDGER.md)

**Important:** Those relative links are from this SKILL.md inside .agents/skills/twbd-episode-analysis; the project documents themselves use repository-relative links appropriate to their own directory.

## 1. Establish the state before reading sources

1. Read Git status/branch/HEAD first; preserve unrelated edits and never assume the checkout is clean. Note the current documented last episode and the next unresolved ID, the last episode dossier, active narrative arc and any relevant profile/ledger entries.
2. Find the **exact** source filenames. Main Wastes files resemble `sources/The Wastes S1E###. Title.parakeet.processed.srt`; other exports may contain `qwen-q8.canary-ctc.nemotron`. Bonus files use public-publication-month labels `Bonus YYYY-MM - ...` but **not necessarily recording dates**. Inverse belongs to an entirely separate fictional continuity with its own indexes.
3. Locate every export for that episode, including alternate copies or different ASR passes. Compare each to the right audio/copy if multiple sources exist. Do not silently substitute a transcript for the wrong episode, label, year, season or campaign.
4. Prefer local MCP access through the connected **InfinityDB OAuth Probe** (despite its name it exposes multiple repositories), with repository-prefixed paths such as `There Will Be Dungeons Transcripts/sources/...`.
   - `git_status`: get branch and existing changes.
   - `list_workspace`: discover sources and existing documentation.
   - `read_workspace_file`: bounded numbered UTF-8 reads.
   - `search_workspace`: **narrow directory and query**; do not scan the entire `local/` audio collection unnecessarily.
   - `read_workspace_binary`: only for needed original media metadata/content under policy. Do not pretend reading binary means listening.
   - `replace_workspace_text`: one unique/stale-safe tracked-text replacement.
   - `create_workspace_file`: only for a new UTF-8 file in an **existing Git-tracked directory**.
5. If local MCP becomes slow/unavailable, **limit retries** and use the connected GitHub `fetch_file` for **tracked, synchronized** source versions when appropriate. GitHub cannot replace local-only, ignored or newer uncommitted files. Never silently mix different revisions.

## 2. Research the entire recording within one source episode

Read both processed SRTs **through the final speech/outro**, not just opening excerpts. Chunk by **recording clock** (e.g., 5–12 minutes per excerpt) to avoid truncation. Collect who acts, how scene transitions occur, what the GM declares, whether characters are together or apart, and what actually remains true **at the episode cutoff**.

Maintain a working evidence map with approximate timestamp, speaker/role if supportable, claim/action, confidence and cross-source conflicts. Keep separate:
- **Observed/GM-adjudicated played actions and outcomes**.
- **NPC testimony and character beliefs**, including lies or errors.
- **Player speculation, jokes, unused branches and game-rule discussion**.
- **Retrospective GM/cast statements**, which may illuminate past events but aren't additional played scenes.
- **Unresolved ASR wording/proper-name alternatives**, pending listening.

Do not fill unexplained gaps with presumed offscreen actions. Distinguish **intended**, **attempted**, **scheduled/promised**, **performed**, **observed** and **completed**. Explicitly track item custody, spell-scroll usage, deaths and resurrection, physical locations, private versus shared knowledge, rituals, contracts, and changes to an earlier cliffhanger. Do not use future bonus-episode spoilers to assert outcomes in earlier main-story episodes.

Keep **The Wastes**, **Inverse**, other campaigns and the **bonus-Q&A timeline** separate. Bonus publication labels do **not** prove recording dates.

## 3. Independently compare ASR exports

For each input, record the exact filename, cue count, last end timestamp, normalized token count, and model/pipeline label **as inferred from the filename** (do not invent build flags, model versions, GPUs, performance, hashes or audio provenance).

For the project's established reproducible full-episode comparison:
1. Extract SRT cue content in chronological order, discarding cue indices and timing lines.
2. Remove optional `(speaker N)` decorations; join cue text.
3. Lowercase; remove straight/curly apostrophes (join contractions); replace characters other than Unicode letters and digits with whitespace; split into word tokens.
4. Compute **unit-cost ordered word-level Levenshtein distance** between complete token sequences, using a reliable exact implementation or a rigorously validated bounded optimization; report edits / **primary Parakeet token count** and percentage.
5. Describe **specific high-risk disagreements with recording timestamps**: divergent names, apparent deletions, stage/cure mechanics, speaker mapping, scene boundaries, contradictory dialogue and stray ending cues. Keep findings **text-only** until audio is checked.

**Never call inter-model disagreement WER, accuracy, confirmed omissions or hallucinations.** Neither agreement nor token-count advantage proves correctness. If computational tools or a complete source are unavailable, **say comparison not computed** instead of fabricating a figure. If manually listening, identify exactly which windows and evidence were checked and distinguish them from untouched windows.

## 4. Write only the documentation justified by the episode

Create/update these layers **in priority order**, using existing adjacent episode conventions as examples:

**Core, almost always**
1. `episodes/E###.md` for the main series, `episodes/BONUS-YYYY-MM.md` for bonuses, or `inverse/episodes/...` for Inverse: concise source-first scene sequence with timestamp ranges, actual cutoff, competing interpretations, and targeted listening questions.
2. A dated `reports/E###_ASR_COMPARISON_YYYY-MM-DD.md` or appropriately named bonus/Inverse report when multiple exports exist. Log normalization/method, measurements, substantive disagreements and limitations. Update `project/MODEL_TESTS.md` with a compact experiment entry.
3. `project/REVIEW_QUEUE.md`: retain unresolved spellings/causality and a verified pointer to the **next source**, and mark the just-researched episode as **ASR-provisional**.

**Main-campaign follow-through (only material changes)**
4. `world/CHRONOLOGY.md` and `world/CONSISTENCY_LEDGER.md`: compact major-event/cutoff changes and previously unresolved statuses, avoiding repeated full retellings.
5. The ongoing `narrative/ARC_ONE.md`, `ARC_TWO.md` or `ARC_THREE.md`: readable connected scenes for main episodes if warranted; prefer consolidation over adding a full duplicate dossier per chapter.
6. Affected `world/characters/*.md`, `world/places/*.md` and relevant artifact/thematic pages; edit only those whose evidence or current status changes.
7. `world/CHARACTERS.md`, `world/PLACES.md`, `world/README.md`, `narrative/README.md`, root `README.md`, or architecture document: update **only outdated navigation, spoiler horizon or summaries**, not every file automatically.

**Bonuses and Inverse**
- For Q&A bonuses, record GM/player claims and speculation as retrospective commentary. Add references to affected earlier profiles, but **do not insert a bonus as a fictional chronology row or narrative chapter**, and do not silently backdate later information.
- For Inverse, update `inverse/` only unless there is a separately supported cross-campaign reference; its reality is not The Wastes.

Canonical spelling follows the project's tiered written/owner decisions (e.g., the **one Eye of Groxl**), but original raw ASR readings remain traceable. Cite the original episode source, appropriate dossier and comparison report with working **relative** links.

## 5. MCP edits, latency safeguards and checkpoints

**Prefer local tracked-file edits** when source is current; do not silently commit, push, rebase or overwrite unrelated work. Keep each `replace_workspace_text` small, with a **unique old_text anchor**, and do reads/edits **sequentially for the same file**. A denied, ambiguous, missing or stale replacement is **not** a success: re-read the narrow affected range, retry only with an actually corrected unique anchor, and otherwise report a blocker.

The MCP repository collection may have high end-to-end latency. Avoid dozens of micro-requests when one safe well-scoped replacement is sufficient:
- Work in **bounded slices**: (A) sources + evidence map, (B) dossier + ASR report, (C) chronology/ledger/narrative, (D) affected profiles + navigation, (E) verification.
- Keep parallel remote calls **small (typically 2–3 maximum)**, and don't launch a dozen concurrent reads for final verification.
- Prefer a **single Git status** at start and end. Re-read only changed passages, rather than rereading every long file. If performance degrades, **finish the core dossier/report first**, preserve the partial state and clearly list remaining updates.
- For new nested folders, the local MCP `create_workspace_file` cannot create parent directories; use an authorized mechanism or request a directory setup rather than faking a completed skill/file.
- If local MCP checks only support **InfinityDB-specific** commands, **do not run them as The Wastes test suite**.

## 6. Validation and final response

Before claiming completion:
1. Read back each newly created file and verify critical edits and episode IDs. Check actual branch/diff/status and that **no original SRT/MP3s changed**.
2. Check links, typoed paths, headings, duplicate markers, Markdown table column counts, stale prior cutoff/next-episode pointers, and contradictions in who possesses an item or which episode established a fact.
3. Run `npm run lint:markdown` **only when a suitable command-execution environment is available**, and report its actual result. Do not confuse link/structure spot checks with Markdownlint, CI, or audio verification.
4. Do not claim a commit, push, passing tests, full review or verified spoken dialogue without having performed it.
5. Conclude briefly with exact episode, core developments, files changed, numerical ASR disagreement **only if calculated**, outstanding audio checks, and whether files are local edits or committed.

## Quick invocations

- `$twbd-episode-analysis E098` — process the corrected episode from both available ASR exports.
- `$twbd-episode-analysis Bonus 2020-05` — process a publication-month bonus as retrospective, not a main-story episode.
- `$twbd-episode-analysis next` — follow the verified research pointer and exact source directory.
- `$twbd-episode-analysis Inverse S1E02` — separate campaign, separate canon.

For ordinary conversation with access to this repository skill: **"Use the twbd-episode-analysis skill for E098."**
