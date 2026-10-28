# Wastes Cleanup — Batch 93: eleven-arc filename, compatibility and E101 acceptance decision

**Date:** 2026-10-28. **Decision status:** **PROPOSED / OWNER APPROVAL REQUIRED**. **Batch disposition:** read-only source research and proposal preparation only, no public narrative/route/schema/decision-table edits and no implementation of an unapproved filename policy. The **eleven D-045 episode boundaries ARE approved**, but numeric filename selection, legacy-path handling, source editing, final chapter prose and cross-link publication are separate implementation decisions under D-047. D-044 canonical display spellings and D-048 reader-first presentation remain binding.

## Live state and source checks

- Re-evaluated access priority at batch opening: no directly mounted local Git checkout at `/local/There Will Be Dungeons Transcripts`, `/mnt/data/There Will Be Dungeons Transcripts`, `/workspace/There Will Be Dungeons Transcripts` or `/workspaces/There Will Be Dungeons Transcripts`; Keycloak-authenticated workspace **MCP connected**. GitHub, Git-generated patch and ZIP fallback not necessary. Repeat the full priority evaluation at each new file-access batch and on tool failure.
- Repository `There Will Be Dungeons Transcripts`, `main`, HEAD **`875625eba95369804be8f3ceba8d46daf4f8d998`**, beginning Git status **six existing visible Wastes Batch 91–92 changes / zero restricted** (four reports, two checkpoints), protected without staging, commit, push or reset.
- Live `narrative/` still contains **nine files only**: `ARC_ONE.md` through `ARC_SIX.md`, `README.md`, `SEASON_TWO.md`, `SEASON_THREE.md`. The numeric new arc files do not exist. The historical wording in `project/DOCUMENTATION_ARCHITECTURE.md` still wrongly says Arc Six is ongoing/reviewed through S3E01; `.agents/skills/twbd-episode-analysis/SKILL.md` likewise contains an older open-arc contract. Change these only in a coordinated approved release/update.
- Reviewed `project/DECISIONS.md` D-044/045/047/048, `project/WASTES_CAMPAIGN_CLEANUP_PLAN.md` L47–65, and the owner-accepted `project/WASTES_NARRATIVE_CHAPTER_MAPS.md` L14–30 plus proposed ch8 Arc07/Arc08 coverage. Earlier preservation audit ledgers remain: **217** original narrative paragraph identities in legacy One–Five plus **347** in legacy Six; original footnotes, notes and URLs are separate mandatory retention classes, not interchangeable with narrative paragraphs.

## Owner decision requested — recommended policy A

**Approve (A):** make `narrative/ARC_01.md` … `narrative/ARC_11.md` the **new canonical reader-facing sequence** of completed Wastes arcs, using the already accepted D-045 episode boundaries, while **retaining the six legacy word-form files `narrative/ARC_ONE.md` … `ARC_SIX.md` at their exact original paths, readable and byte-preserved, as the historical first edition**. A later index can label these as Legacy narrative edition; do not overwrite or redirect any historical file as part of initial publication. This avoids silently mapping old **ARC_SIX** (spanning current Season Two–Three) onto unrelated **new ARC_06** (E067–081).

Approval of **A is a naming/navigation/compatibility policy only**, **not** approval to rewrite, compress, reinterpret, delete, relocate historical text, or publish unreviewed new arc prose. All substantive prose/scene transfers and meaning-changing changes remain owner-gated. Owner may choose **B**, an alternative filename policy while keeping legacy preservation constraints, or revise A's legacy presentation before anything is implemented.

| Proposed new reader path | Owner-approved episode coverage / key exception | Preliminary title from D-045 (not final authoring approval) |
| --- | --- | --- |
| `narrative/ARC_01.md` | E000–E009; E013.5 supplementary in fictional time | Beginnings in Dusthill |
| `narrative/ARC_02.md` | E010–E026 | Chains and Bargains |
| `narrative/ARC_03.md` | E027–E040 | Road to a Lost Kingdom |
| `narrative/ARC_04.md` | E041–E054; E043 one-off excluded | The Crown of T'ietkalla |
| `narrative/ARC_05.md` | E055–E066 | Kings and Consequences |
| `narrative/ARC_06.md` | E067–E081 | Beneath the World |
| `narrative/ARC_07.md` | E082–E101 **through Hope's completed portal departure** | The City of Doors |
| `narrative/ARC_08.md` | E101 **after departure**, E102–E106 and E110–E114; E107–109 separate historical prequel | Separate Paths |
| `narrative/ARC_09.md` | E115–E126 and E128; E127 one-off excluded | The Fall of Elhandar |
| `narrative/ARC_10.md` | S2E01–12, S3E01–03; season break is not arc boundary | Across the Stars |
| `narrative/ARC_11.md` | S3E04–S3E18; S3E019 is nonplayed cast Q&A | The Last War |

**Key count contract:** the crosswalk represents **155 arc-row episode contributions** but **154 unique main/introduction episode IDs** because **E101 appears in two arcs but has one recording and dossier**. Keep E013.5 supplemental, E043/E127 one-offs and E107–109 *Dunebreaker* earlier historical prequel discoverable separately. No fictional time jump invented to cover the publication-number gaps.

## Compatibility contract — what must work after eventual publication

1. **Old word-form paths:** all six `ARC_ONE.md`–`ARC_SIX.md` stay reachable, with current contents and footnotes retained, even after the new index promotes numeric files. Archived exact source snapshots under `research/legacy/` remain mandatory **before touching any existing maintained source**; old paths are not disposable aliases, redirects, or renamed into new numbering. Old Arc Six in particular spans **new Arcs 10 AND 11**. Historical report links should continue to cite original historical source.
2. **New navigation:** only once all **eleven complete, reviewed narrative files** and their links exist, change `narrative/README.md` and `wastes/README.md` to show eleven canonical numbered arcs. Keep a clearly identified **Legacy six-arc edition** link section and a coherent previous/next reading sequence inside new `ARC_XX.md` pages. The current indexes remain unchanged before acceptance; do not publish partial links to missing files.
3. **Season compatibility stubs:** retain `narrative/SEASON_TWO.md` and `SEASON_THREE.md`. When the new paths are accepted, guide Season Two to **new Arc 10**, and Season Three **S3E01–03 to new Arc 10, S3E04–18 to new Arc 11**. Retain the old Arc Six source link as historical reference and label S3E019 only as post-campaign Q&A.
4. **World and research links:** preserve direct legacy links used by `world/HISTORICAL_EVENTS.md`, `world/CHRONOLOGY.md`, `world/FACTIONS_AND_POWERS.md`, subject pages, `project/DECISIONS.md`, the old narrative footnotes and historical report evidence. New references may point to verified new pages, but old labels should not be silently rewritten as if historical six-arc references never existed. Use D-044 spelling in *new* editorial copy while retaining old slugs/source quotations.
5. **Coverage and evidence:** preservation baseline comprises **217** One–Five and **347** Six original narrative paragraphs, **104** original One–Five footnote definitions, **214** original One–Five Markdown link occurrences / **148** distinct paths (all repository destinations confirmed in Batch92), and **67** original Six link occurrences / **54** distinct readable file targets (Batch90). All original headings, research/source footers, scene chronology, epistemic limits and original backups must survive the migration. The new sources need an explicit paragraph-content-to-scene disposition ledger, with no unexplained omissions.
6. **Rollout:** Phase 1 choose naming/compatibility; Phase 2 build bounded source-to-arc scenes and reviewed prose in new paths while preserving old pages; Phase 3 independently validate all new chapters, evidence links, scene boundaries, table-of-contents navigation and accessibility, then promote numeric reading index in a controlled change with recovery path. Do not auto-delete old pages after migration.

## E101 dual-arc original-paragraph disposition pilot (no text rewritten)

The user-approved **split is after actual portal crossing and closure around 01:57–01:59 in *E101 — A New Hope***, **not** after the choice around 01:44, when Hope attaches the Hand, or at the E101/E102 file boundary. See `episodes/E101.md` L11–27 and [Batch92 E101 verification](WASTES_CLEANUP_D045_E101_HANDOFF_AND_SEASON_ONE_LINK_TARGETS_92_2026-10-28.md). The following is a **provisional scene allocation ledger**, not an authorization to transplant entire condensed paragraphs.

| Historical original paragraph | Scope / source status | Proposed destination and fidelity gate |
| --- | --- | --- |
| **`ARC_FOUR.md` L101**, footnote `[^four-15]` | E100 prior siege/cliffhanger; Fist + severed Hand first exposed | Keep in new Arc07 **preceding E101** scene, preserve E097–100 evidence and don't backdate E101 hand joining |
| **`ARC_FOUR.md` L105** | E101 Stanley survives; Fist rejected by tower ward; Hope alone hears Voice | New Arc07 last chapter, E101 predeparture; privately received information is not party knowledge |
| **`ARC_FOUR.md` L107** | E101 performed amputation/Hand joining, actual Eye of Groxl restoration and expressed godhood desire | New Arc07 last chapter; physical events vs patron testimony |
| **`ARC_FOUR.md` L109** | E101 performed Hand powers/Finger of Death; separate Fist returned to still-open chest | New Arc07 last chapter; **do not say the chest is locked yet** |
| **`ARC_FOUR.md` L111** | E101 chooses solitude and **demons actually withdraw**, limited armistice | New Arc07 last chapter; wider Blood War continues |
| **`ARC_FOUR.md` L113–115** | E101 invitation, Spatulo follows, completed physical portal crossing/close, other three left at White Tower | **End new Arc07**. Preserve exact E101 split citation `[^four-16]`, dossier/audit `[^four-17]`, historical notes `[^four-18]` |
| **`ARC_FIVE.md` L7** | Brief postportal recap + E101 friends' grief/hope for return | **Begin new Arc08** as a short continuity bridge; do not count portal crossing twice as a fresh new event. E101 friends' different emotional interpretations retained |
| **`ARC_FIVE.md` L9** | **E101** visible Prith-mark removal, travel to Kaiser Casino, meeting with the Asmodeus-claiming Brett, no completed pact; **E102** appearance necklace and replacement Gate ring | **Split E101 scene from E102 gifts** within new Arc08 ch1; no gift backdating or universal contract-freedom inference |
| **`ARC_FIVE.md` L11** | Postportal White Tower state from late E101; **E102** Tunga saucer crash, Alentris memory alteration, airship departure | New Arc08 ch1 E101+E102 **distinct scenes**; preserve actual E101 re-locking chest/key to Stanley, distinguish planned flight from E102 real takeoff; do not count one long rest twice |
| **`ARC_FIVE.md` L13** | **E102** Brett's three employees and performed Gate to Hope's chambers; **E103** Celibus Stump's performed death and guard fight | Split by episode/played scene before Chapter 1–2 allocation; no E103 event assigned to E101 |
| **`ARC_FIVE.md` L15**, `[^five-2]` | **E103** Hope's discussions, privately demanded evil, declined murders, actual railway-station arson; concurrent Tunga airship threat | Keep under E103, with split viewpoints and ASR claims attributed. **Original `[^five-2]` cites E101/E102/E103 together** and needs source-specific relinking, not deletion |
| **`ARC_FIVE.md` L19–27**, `[^five-3]` | **E104–106** later events and historical E107–109 prequel qualifier | New Arc08 later chapters, **not** part of E101 |

**Additional essential source notes:** legacy `[^four-15]` E097–100, `[^four-16]` exact handoff time, `[^four-17]` E101 dossier+dual-ASR audit, `[^four-18]` out-of-game commentary and uncertainty; legacy `[^five-1]` cross-arc E101 and E128 scope, `[^five-2]` grouped E101–03, `[^five-3]` later E104–06/earlier Dunebreaker prequel. These footnote bodies are still in the old published sources, and destination notes must be rebuilt with **episode-level** precision before publication. No old footnote definitions modified.

**E101 final played custody / speaker knowledge at cutoff:** Hand of the Voice permanently attached to Hope; *separate* Zorander's Fist gauntlet sealed in a levitating chest; medallion **key with Stanley** after Nash relocks it *postportal*; Eye of Groxl physically restored to Vorel; the patron's identity/private demands not communicated to the other three; Hope has not signed Brett's pact, reached her kingdom or rejoined the party. E102 gifts and performed memory alteration and E103 political violence must not be imported backward. Handoff is one recording/dossier with two narrative arcs, not two E101s.

## Illustrative reader navigation after acceptance — examples ONLY, not file mutations

This is intended to preview link directions, not imply the files exist:

- New end-of-Arc07 page (`narrative/ARC_07.md`): `[Previous arc](ARC_06.md) · [All eleven arcs](README.md) · [Next arc — Separate Paths](ARC_08.md)`.
- New beginning of Arc08 (`narrative/ARC_08.md`): brief continuity note, *“The remaining events of E101 begin immediately after Hope's departure through the closed White Tower portal.”* Then `[Previous arc — The City of Doors](ARC_07.md) · [All eleven arcs](README.md) · [Next arc](ARC_09.md)`.
- In the eventual new guide only, two consecutive entries `[07 — The City of Doors](ARC_07.md)` and `[08 — Separate Paths](ARC_08.md)` with a succinct source footnote that both include E101 but its recording is counted **once**. The old guide stays active until all targets have passed validation.
- Legacy `ARC_FOUR.md` and `ARC_FIVE.md` retain their original `ARC_THREE.md`/`ARC_FIVE.md` and `ARC_FOUR.md`/`ARC_SIX.md` previous/next links: these are **legacy-edition** route relationships, not broken canonical-number relationships.

## Publication acceptance checklist (tests to run, not claimed performed)

1. Verify Git HEAD and restricted/dirty changes before **each** implementation batch; re-evaluate local/MCP/GitHub/patch/ZIP. Archive exact **then-current working source bytes** before any edits; independently hash both archive and source before changing source. Preserve original CRLF, byte order and raw source quotes. No routine full suite by assistant; targeted checks only, owner/CI runs broad suite.
2. All eleven new `ARC_XX.md` files exist at the **approved** paths; chapter titles, density, notes, scene handoffs and reader-first presentation reviewed. The historic six word-form arcs remain accessible, with **unchanged source SHA** unless a new explicit owner decision changes them. Existing season compatibility paths remain valid.
3. Every original paragraph digest has a traceable *disposition* (retained in target, faithfully summarized with corroborating source, or archived with intentional omission rationale). No forced mechanical 350–450 word cap; verify unique details, character agency, testimony and chronology. E101 across Arc07/08 exactly once as a recording, with end/begin boundary correct; E013.5/E043/E107–109/E127/S3E019 properly classified.
4. Link checker verifies all new and previously published relative file links, footnote uses/definitions, new navigation previous/next semantics, chapter heading labels, and the **214** original Season One and **67** original Six link occurrences still accessible in legacy source. Validate link rendering and directory-link behavior in the actual Markdown client, not only filesystem presence.
5. `narrative/README.md`, `wastes/README.md`, `world/` entry points, `SEASON_TWO.md` and `SEASON_THREE.md` switch coherently to canonical numbered arcs at release; legacy and historical links preserved. Update old “Arc Six ongoing” wording in `project/DOCUMENTATION_ARCHITECTURE.md` and `.agents/skills/twbd-episode-analysis/SKILL.md` as coordinated doc maintenance, without rewriting historical D-042/043 decision records.
6. After launch check user-facing paths and broken links, old direct bookmarks within hosted repository, Git status, targeted formatting checks (e.g. Markdownlint / `git diff --check` only where available), and rollback recovery to exact backups. Do not assert successful release from a report/proposal alone.

**Next action:** ask the owner to decide **“Approve A”** (numeric eleven-arc paths and *immutable, readable* old six word-form paths; approved episode boundaries unchanged) or specify changes. On approval, record a new decision in the project decision log **without silently writing new prose**. The first new-arc authoring/migration pilot still requires its own scene-fidelity/content acceptance and exact-source backup. If no approval, continue only non-mutating research and source-evidence planning.

**Not run:** audio listening, actual Markdown rendering, full inbound backlink corpus, independent navigation click tests, Markdownlint, full tests, `git diff --check`. This report and cleanup tracker pointers are the only Batch93 written changes; no commit or push.
