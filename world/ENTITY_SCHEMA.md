# Entity index convention

[`entities.json`](entities.json) is a starter machine-readable name index for future transcript consistency checks. Markdown pages remain the authoritative **editorial notes**; JSON provides stable IDs, aliases, types, source pointers and review status.

Each entity has:

- `id`: stable, ASCII slug that does not change when its display name is corrected.
- `display_name`: provisional written label for generated indexes.
- `type`: `person_character`, `person_npc`, `place`, `artifact_or_technology`, `organization`, `world_concept` or `race_culture` (introduced in v2 for intelligent peoples/cultures, **not** their factions or individual members).
- `aliases`: alternate recognition spellings/phrases that should match in searches; aliases do **not** establish canon.
- `name_status`: `working`, `needs_audio_spelling_check`, `spoken_name_confirmed`, `known_label` or `wiki_spelling_supported` (the latter is **not** audio verification).
- `description`: source-limited summary with careful attribution.
- `sources`: array of `{episode, time, evidence_type}` entries; episode/time is approximate and refers to source audio time.
- `external_sources`: optional array of `{url, evidence_type, chronology, checked_on}` for external orthography and other carefully attributed references.
- `questions`: explicit unresolved issues.
- `page_path` (optional, v2): repository-root-relative Markdown subject page; confirm that the file exists. It is a navigation target, not proof of comprehensive canon coverage.
- `relations` (optional, v2): an array of `{relation, entity_id}` directed from the containing record to another **existing** stable ID. For `race_culture`, `documented_individual` means the target character is an attested member; it neither asserts that every member of the people shares that individual's culture nor creates a membership list. Relation IDs must be unique within a source record, resolvable and type-appropriate.

The index does not claim that the listed spellings are externally official. Do not auto-replace words in old transcripts when a preferred name changes: create a separate reviewed editorial variant and retain the originals.

## Version 2 — extended, non-exhaustive population pilot (2026-10-31)

[Decision D-046](../project/DECISIONS.md) authorizes a Races domain distinct from characters, creatures and factions. The owner separately approved an **additive** `race_culture` data migration for exactly [Lizardfolk](races/lizardfolk.md) and [Tieflings](races/tieflings.md). `world/entities.json` now uses `version: 2`, `stage: extended-pilot` and `source_scope_policy: cited-episodes-only`. Every one of the original 16 v1 entity records is retained unchanged and in the same order; the two race IDs are appended. New records may use the optional `page_path` and `relations` fields described above; these are not mandatory on older records.

**Scope contract:** `source_scope` is the unique, explicitly listed set of episodes **actually cited by indexed records** (including the earlier E000/E001 pilot). It does *not* mean all characters, claims, peoples, or events in those episodes have been indexed; it does not mean recordings were independently verified by listening. The exact cited episodes of every record must belong to this list, and every listed episode must have at least one record citation. Source references retain approximate time codes and evidence classes; competing accounts, local customs and planned events must remain attributed, not become objective race-wide traits. The two records link to established reader studies but **do not synchronize or generate** those pages. **Lactids remain a research candidate without a standalone population study**. **Harlequinari already has a [published, source-limited people profile](races/harlequinari.md)**, but is **not** an indexed `race_culture` record in the two-race machine pilot. The existence of a Markdown study neither adds a JSON record nor verifies its full history or the Council of Clowns' complete membership.

**Compatibility and upgrade:** The top-level `entities` array and all v1 record fields (`id`, `display_name`, `type`, `aliases`, `name_status`, `description`, `sources`, `questions`, and optional `external_sources`) keep their original meaning. Type-agnostic readers that look up IDs, names and aliases can continue reading them; a consumer that **requires** `version == 1` or rejects unknown types/fields needs an explicit v2 upgrade. New relation targets must resolve to IDs in the same file, and `page_path` must resolve to an existing repository Markdown file. Never change older IDs or transcription spellings automatically.

[Decision D-044](../project/DECISIONS.md) makes **The Principal** the canonical display name (old `the Principle` is a wrong historical alias), **Khaervilon** the canonical location name (old `Kervalon` is a wrong historical alias), and confirms **T'ietkalla**, **Moag Ferhain**, **Ubere Mtaris** and the **Or'Nath** family forms. Before adding records, distinguish *owner-confirmed written form* from `spoken_name_confirmed` (actual audio verification); do not overload the latter to mean map-authoritative. Consider a separate status such as `owner_confirmed_written` or explicit provenance object when a versioned schema migration is approved. Stable IDs, previous paths and aliases must survive changes of display spelling. [Consolidation plan](../project/WASTES_CAMPAIGN_CLEANUP_PLAN.md).
