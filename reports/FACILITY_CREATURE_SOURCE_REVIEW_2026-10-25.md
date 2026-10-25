# E008 facility creatures — targeted source review

**Date:** 2026-10-25. **Campaign:** The Wastes, Season One. **Candidates:** WSC-013 green-case mimic and WSC-014 doglike facility predator. **Result:** Both now support short creature articles. [Candidate search](WASTES_S1_CREATURE_SEARCH_2026-10-24.md) · [Machine-readable source inventory](FACILITY_CREATURE_SOURCE_REVIEW_2026-10-25.json).

## Scope and method

The initial shortlist left the mimic's defeat and the doglike animal's anatomy/movement unresolved. This follow-up examined **nine selected Parakeet windows** and **six selected Qwen windows** in the exact E008 exports below. It also used the existing [E009 dossier](../episodes/E009.md) for the later facility collapse; no E009 transcript was newly reviewed.

Both complete files were parsed to locate passages and record cue counts, ending clocks and SHA-256 fingerprints. **Parsing is not complete interpretive review:** the window list records the extent of manual reading, and cross-reading covers only selected overlapping passages. The two exports were not fully compared. No original audio was heard and no full-export disagreement metric was computed. Model/pipeline labels are filename-derived. Cue clocks are subtitle intervals, not word timings. Both source exports remain unchanged.

## Findings and source distinctions

| Subject | Supported evidence | Boundary |
| --- | --- | --- |
| Mimic's disguise | ~01:59:46–02:01:20: large green military-style case, straps, handle, combination lock and hazard marking; it opens into teeth and tongue. | No universal shapechanging ability list or working lock mechanism inferred. |
| Grappling and injury | ~02:28:30–02:29:29: Stanley breaks one hinge and releases Chance, but the case still moves. ~02:32–02:33: its tongue pulls Nash's leg, causing him to hit his head and fall unconscious. | Nash's spoken “dead” is immediately resolved as unconsciousness and death saves; he later becomes stable, not healed. |
| Mimic's death | ~02:41:24–02:42:25: Stanley's blade breaks the remaining hinge; the two halves and tongue fall apart and cease moving. ~02:51:39 onward explicitly calls it a corpse. | Death is now text-supported; it is not attributed to the doglike creature. |
| Corpse contents | ~02:52–02:55: a metal tube is pried from a fleshy fold in the corpse. | Purpose/contents remain unknown. This is separate from the two pieces of metal floating inside a laboratory glass chamber. |
| Doglike anatomy | ~02:16:14–02:16:26: large, doglike, many legs, described standing six feet tall. ~02:21:48: all eight legs are on the table. | A description of this animal, not an identified species or general adult size. |
| Actual teleporting movement | ~02:21:38–02:22:04: it vanishes at the door and reappears on a table in front of Nash. Later disappearances and returns recur. | Movement is directly narrated; a player's Nightcrawler analogy is unnecessary to establish it. Range, plane and limits remain unknown. |
| Sleep and food | ~02:27–02:31: Sleep subdues it until shouting wakes it. ~02:43–02:49: Chance offers the severed mimic tongue; it eats, remains wary, is soothed, recoils from petting and teleports into a corner with the food. | Feeding does not instantly unblock the doorway or establish lasting friendship/domestication. |
| Latest condition | ~02:49 and ~02:51:39: alive, eating the tongue; ~02:57:10: still in the room. | E009's later collapse does not prove this animal dies or escapes. The E043 blink dog belongs to a separate setting and is not identification evidence. |

Qwen corroborates the core initial teeth/tongue description, eight legs, the first doorway/table relocation, final hinge destruction and feeding/retreat. Some mechanical bookkeeping and the metal-tube extraction were read only in the selected primary passages. Small transcript differences such as “blinks/boinks” and “bamf/banff” do not remove the explicitly described disappearance and reappearance. Neither agreement nor greater detail proves acoustic accuracy.

## Reviewed windows and source fingerprints

- [Parakeet export](../sources/The%20Wastes%20S1E008.%20Stupid%20Gnomes%21.parakeet.processed.srt): 4815 cues; last end 03:02:23; SHA-256 `5fe30a230d81d38b56a032ef518f95b60fa0f207b04c0afa6ac11e68fa25e1bf`.
- [Qwen export](../sources/The%20Wastes%20S1E008.%20Stupid%20Gnomes%21.qwen-q8.canary-ctc.nemotron.srt): 5743 cues; last end 03:02:23; SHA-256 `f226bd00c5b008d2662c1e07c3587574be6054d7464f131f5eeceb546c2764c4`.

| Export label | Recording window | Cue range inspected |
| --- | --- | --- |
| Parakeet | 01:59:20–02:03:20 | 3133–3226 |
| Parakeet | 02:15:45–02:16:50 | 3570–3595 |
| Parakeet | 02:20:55–02:22:40 | 3693–3740 |
| Parakeet | 02:49:00–02:50:40 | 4463–4501 |
| Parakeet | 02:27:10–02:31:15 | 3865–3970 |
| Parakeet | 02:32:00–02:35:10 | 3990–4085 |
| Parakeet | 02:40:50–02:49:15 | 4236–4465 |
| Parakeet | 02:51:00–02:53:00 | 4512–4566 |
| Parakeet | 02:52:45–02:57:30 | 4561–4677 |
| Qwen | 02:00:55–02:02:30 | 3768–3818 |
| Qwen | 02:15:55–02:16:50 | 4275–4304 |
| Qwen | 02:21:20–02:22:20 | 4449–4486 |
| Qwen | 02:41:20–02:42:40 | 5113–5152 |
| Qwen | 02:43:25–02:44:30 | 5175–5207 |
| Qwen | 02:47:10–02:49:15 | 5290–5340 |

Overlapping windows are retained as actually read; they are not separate corroborating sources. The initial keyword/context discovery also located repeated case/tongue/dog references outside these windows, but no uninterrupted full-episode interpretation is claimed. Full parsed cue text is retained locally at `local/creature-search/facility-e008-2026-10-25/sources.json`.

## Integration and remaining work

Created [Green-case mimic](../world/creatures/green-case-mimic.md) and [Eight-legged facility predator](../world/creatures/eight-legged-facility-predator.md), linked them from the category and marked WSC-013/WSC-014 published. The E008 dossier's compressed fight window is extended through the mimic's actual defeat, followed by distinct feeding/withdrawal and corpse-search entries. Its new follow-up note makes clear that these are selected dual-export checks, not a fresh full dossier analysis. The wider episode-research pointer remains unchanged.

The next focused candidates are WSC-015 gibbering mouther and WSC-016 concealing mushroom-pit spider. Remaining listening questions include exact anatomy, object/corpse contents, the dog's species and teleportation limits, and its ultimate fate. These unknowns do not require an invented name or a falsely resolved death to write the bounded observed accounts.
