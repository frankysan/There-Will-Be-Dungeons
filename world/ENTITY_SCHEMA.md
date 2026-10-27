# Entity index convention

[`entities.json`](entities.json) is a starter machine-readable name index for future transcript consistency checks. Markdown pages remain the authoritative **editorial notes**; JSON provides stable IDs, aliases, types, source pointers and review status.

Each entity has:

- `id`: stable, ASCII slug that does not change when its display name is corrected.
- `display_name`: provisional written label for generated indexes.
- `type`: `person_character`, `person_npc`, `place`, `artifact_or_technology`, `organization` or `world_concept`.
- `aliases`: alternate recognition spellings/phrases that should match in searches; aliases do **not** establish canon.
- `name_status`: `working`, `needs_audio_spelling_check`, `spoken_name_confirmed`, `known_label` or `wiki_spelling_supported` (the latter is **not** audio verification).
- `description`: source-limited summary with careful attribution.
- `sources`: array of `{episode, time, evidence_type}` entries; episode/time is approximate and refers to source audio time.
- `external_sources`: optional array of `{url, evidence_type, chronology, checked_on}` for external orthography and other carefully attributed references.
- `questions`: explicit unresolved issues.

The index does not claim that the listed spellings are externally official. Do not auto-replace words in old transcripts when a preferred name changes: create a separate reviewed editorial variant and retain the originals.

## Planned completed-campaign extension (2026-10-27)

This is a **planned change**, not an assertion that the existing `entities.json` has been migrated. The JSON currently reports `stage: pilot-seed` and source scope E000/E001. [Decision D-046](../project/DECISIONS.md) requests a new **Races** domain under `world/`, distinguishing intelligent peoples from individual characters, creatures and factions. A future schema revision should introduce an explicit race/culture type and relation fields while preserving existing ID semantics and compatibility with old consumers.

[Decision D-044](../project/DECISIONS.md) makes **The Principal** the canonical display name (old `the Principle` is a wrong historical alias), **Khaervilon** the canonical location name (old `Kervalon` is a wrong historical alias), and confirms **T'ietkalla**, **Moag Ferhain**, **Ubere Mtaris** and the **Or'Nath** family forms. Before adding records, distinguish *owner-confirmed written form* from `spoken_name_confirmed` (actual audio verification); do not overload the latter to mean map-authoritative. Consider a separate status such as `owner_confirmed_written` or explicit provenance object when a versioned schema migration is approved. Stable IDs, previous paths and aliases must survive changes of display spelling. [Consolidation plan](../project/WASTES_CAMPAIGN_CLEANUP_PLAN.md).
