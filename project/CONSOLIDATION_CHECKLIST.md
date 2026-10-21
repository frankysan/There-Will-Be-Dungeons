# Year One documentation consolidation — implementation checklist

**Status (2026-10-21):** Phase A completed as a **first editorial pass**. Phases B–D remain pending. Follow [the architecture](DOCUMENTATION_ARCHITECTURE.md) for the full target design and source-evidence rules.

## Phase A — architecture, narrative and navigation

- [x] Define **research / reference / narrative / editorial** responsibilities in [architecture](DOCUMENTATION_ARCHITECTURE.md).
- [x] Draft the first cohesive [Year One narrative](../narrative/YEAR_ONE.md) from researched E000–E054 dossiers.
- [x] Publish a short [narrative index](../narrative/README.md) and route readers from [project README](../README.md) and [world portal](../world/README.md).
- [x] Archive pre-consolidation [root README](../research/legacy/2026-10-21/ROOT_README.md) and [world README](../research/legacy/2026-10-21/WORLD_README.md); maintain usable relative links in the snapshots.
- [x] Preserve E013.5 earlier-in-story scene, E043 one-shot, March Q&A bonus and owner-confirmed name decisions.
- [x] Preserve episode dossiers, SRTs, archived research and `world/entities.json` without content replacement.
- [x] Check **all internal file links** in the new portals/narrative/policy and both archives.
- [ ] **Audio-verify** all narrative milestones. This is an **ongoing editorial requirement**, not something claimed by the structural pass.
- [ ] **Review the Year One synthesis with targeted source listening** for open chronology, claimed history and disputed name issues. See [review queue](REVIEW_QUEUE.md).

## Phase B — characters and places, first reference rewrite

Start with the **four protagonists**, then **major allies/adversaries**, then major sites. Archive the full current original reference file *before replacing it*, and preserve stable backlinks. **Do not create parallel equally authoritative profiles**.

- [ ] Reformat `world/CHARACTERS.md` as an **alphabetical/role-based index** with one concise paragraph per subject, linked to substantive entries (initially kept in a small number of files).
- [ ] Produce consistent first profiles for **Nash Maggard**, **Hope Akmenos**, **Stanley Billings & Diontalus** (shared body but **distinct agency**), and **Vorel**, incorporating Year One changes and correct episode source cutoffs.
- [ ] Consolidate **Buttons** (GM Q&A motive revealed posthumously), **P0D** (involuntary transformation/death), **Tedna** (E048 rescue then E050 death), **Angelashi** (E048 mistaken death report, E054 rescue), **Bok Bok** and **Monsoon**.
- [ ] Consolidate `world/PLACES.md` and first place entries: **Dusthill**, **Slavetown**, **Black Mine**, **Château Weir**, and **Tietkalla** including **Trashburg, Teet keep, Pit of Despair and ancient under-keep**.
- [ ] Ensure **Eye of Groxl** one-artifact canonical name, cast-supported **Tietkalla** and unresolved proper-name variants are represented **only once per subject**, with provenance.
- [ ] Validate links, correct imported relative references and mark **outstanding rather than resolved** source doubts.

## Phase C — world themes and chronology

- [ ] Save dated snapshots of the existing long `world/WORLD.md` and `world/CHRONOLOGY.md`.
- [ ] Reorganize `world/WORLD.md` into **ancient history (GM prologue), societies/factions, dragon technology, spellcraft/artifacts, religion/Weirlords and political structures**.
- [ ] Keep **claims about distant history** attributed; distinguish Soulbroker/Monsoon/Kefeli/Nobiery views from directly played demonstrations.
- [ ] Rewrite `world/CHRONOLOGY.md` as one integrated **timeline**, with scene order, historical backstory and publication exceptions clearly split. Keep timestamps in linked dossiers.
- [ ] Ensure unique **scene/event links** rather than rewriting all episode scenes at length.

## Phase D — ledger and editorial cleanup

- [ ] Refactor `world/CONSISTENCY_LEDGER.md` into **active uncertainty/index** with **resolved decisions linked to `DECISIONS.md`**, archiving the full original research ledger.
- [ ] Remove or label outdated duplicate research passages; **never erase their archived evidence**.
- [ ] Check inbound links to moved headings and keep redirects/anchors or update all references.
- [ ] Review completeness against all E000–E054 dossiers and [Q&A bonus](../episodes/BONUS-2019-03.md).
- [ ] Validate no broken Markdown links or falsely completed items, and run available source/documentation checks where appropriate.

## Important migration rule

**“New page exists” is not a reason to declare an entire reference category complete.** Finish an entity only after its prior material has been reviewed for missing facts, provenance retained, contradictions tracked and crosslinks updated. Do not allow new narrative prose, retroactive Q&A revelations or wiki later-campaign spoilers to silently rewrite earlier character knowledge. This first consolidation does **not** certify an audio review or complete `entities.json` publication.
