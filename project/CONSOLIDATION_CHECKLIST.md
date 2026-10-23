# Arcs One–Two documentation consolidation — implementation checklist

**Status (2026-10-22):** **Phases A–D structurally consolidated as first editorial passes**. Audio/handout verification and comprehensive minor-entity review remain open. Follow [the architecture](DOCUMENTATION_ARCHITECTURE.md) for the full target design and source-evidence rules.

## Phase A — architecture, narrative and navigation

- [x] Define **research / reference / narrative / editorial** responsibilities in [architecture](DOCUMENTATION_ARCHITECTURE.md).
- [x] Draft the first cohesive narrative from researched E000–E054 dossiers, now split into [Arc One](../narrative/ARC_ONE.md) and [Arc Two](../narrative/ARC_TWO.md).
- [x] Publish a short [narrative index](../narrative/README.md) and route readers from [project README](../README.md) and [world portal](../world/README.md).
- [x] Archive pre-consolidation [root README](../research/legacy/2026-10-21/ROOT_README.md) and [world README](../research/legacy/2026-10-21/WORLD_README.md); maintain usable relative links in the snapshots.
- [x] Preserve E013.5 earlier-in-story scene, E043 one-shot, March Q&A bonus and owner-confirmed name decisions.
- [x] Preserve episode dossiers, SRTs, archived research and `world/entities.json` without content replacement.
- [x] Check **all internal file links** in the new portals/narrative/policy and both archives.
- [ ] **Audio-verify** all narrative milestones. This is an **ongoing editorial requirement**, not something claimed by the structural pass.
- [ ] **Review the Arcs One–Two synthesis with targeted source listening** for open chronology, claimed history and disputed name issues. See [review queue](REVIEW_QUEUE.md).

## Phase B — characters and places, first reference rewrite

Start with the **four protagonists**, then **major allies/adversaries**, then major sites. Archive the full current original reference file *before replacing it*, and preserve stable backlinks. **Completed first-pass (2026-10-21):** 10 character profiles and 5 place profiles now feed concise indexes; former 88k/65k research compendia are archived. This is not an audio verification or a claim that every minor entity has a standalone page. **Do not create parallel equally authoritative profiles**.

- [x] Reformat `world/CHARACTERS.md` as an **alphabetical/role-based index** with one concise paragraph per subject, linked to substantive entries (initially kept in a small number of files).
- [x] Produce consistent first profiles for **Nash Maggard**, **Hope Akmenos**, **Stanley Billings & Diontalus** (shared body but **distinct agency**), and **Vorel**, incorporating Arcs One–Two changes and correct episode source cutoffs.
- [x] Consolidate **Buttons** (GM Q&A motive revealed posthumously), **P0D** (involuntary transformation/death), **Tedna** (E048 rescue then E050 death), **Angelashi** (E048 mistaken death report, E054 rescue), **Bok Bok** and **Monsoon**.
- [x] Consolidate `world/PLACES.md` and first place entries: **Dusthill**, **Slavetown**, **Black Mine**, **Château Weir**, and **Tietkalla** including **Trashburg, Teet keep, Pit of Despair and ancient under-keep**.
- [x] Ensure **Eye of Groxl** one-artifact canonical name, cast-supported **Tietkalla** and unresolved proper-name variants are represented **only once per subject**, with provenance.
- [x] Validate links, correct imported relative references and mark **outstanding rather than resolved** source doubts.

## Phase C — world themes and chronology

**First-pass completed 2026-10-22:** Old ~91k / ~69k-character batch-appendices preserved in [dated archive](../research/legacy/2026-10-22/README.md). Active [world guide](../world/WORLD.md) is thematic and [chronology](../world/CHRONOLOGY.md) is one continuous 53-episode event sequence; all source time codes remain in per-episode dossiers. **Not audio-verified**.

- [x] Save dated snapshots of the existing long `world/WORLD.md` and `world/CHRONOLOGY.md`.
- [x] Reorganize `world/WORLD.md` into **ancient history (GM prologue), societies/factions, dragon technology, spellcraft/artifacts, religion/Weirlords and political structures**.
- [x] Keep **claims about distant history** attributed; distinguish Soulbroker/Monsoon/Kefeli/Nobiery views from directly played demonstrations.
- [x] Rewrite `world/CHRONOLOGY.md` as one integrated **timeline**, with scene order, historical backstory and publication exceptions clearly split. Keep timestamps in linked dossiers.
- [x] Ensure unique **scene/event links** rather than rewriting all episode scenes at length.

## Phase D — ledger and editorial cleanup

**Structural pass complete (2026-10-22):** Full [former consistency ledger](../research/legacy/2026-10-22/WORLD_CONSISTENCY_LEDGER.md) and [former review queue](../research/legacy/2026-10-22/PROJECT_REVIEW_QUEUE.md) archived before rewriting. Active [open/resolved index](../world/CONSISTENCY_LEDGER.md) and [prioritized review queue](REVIEW_QUEUE.md) now serve different purposes. **No new audio or handout verification**.

- [x] Refactor `world/CONSISTENCY_LEDGER.md` into **active uncertainty/index** with **resolved decisions linked to `DECISIONS.md`**, archiving the full original research ledger.
- [x] Remove or label outdated duplicate research passages; **never erase their archived evidence**.
- [x] Check inbound links to moved headings and keep redirects/anchors or update all references.
- [x] Verify **structural source coverage** across all E000–E054 dossiers, E013.5 and [Q&A bonus](../episodes/BONUS-2019-03.md) using the [review routing grid](REVIEW_QUEUE.md). **Full audio/handout-level completeness is not claimed** and remains open.
- [x] Validate no broken Markdown links or falsely completed items, and run available source/documentation checks where appropriate.

## Important migration rule

**“New page exists” is not a reason to declare every individual reference audio-verified or every minor NPC fully indexed.** Finish an entity only after its prior material has been reviewed for missing facts, provenance retained, contradictions tracked and crosslinks updated. Do not allow new narrative prose, retroactive Q&A revelations or wiki later-campaign spoilers to silently rewrite earlier character knowledge. This first consolidation does **not** certify an audio review or complete `entities.json` publication.
