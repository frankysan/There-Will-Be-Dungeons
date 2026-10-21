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
