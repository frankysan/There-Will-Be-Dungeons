# Chasm flyers and crater wyvern — targeted source review

**Date:** 2026-10-25. **Campaign:** The Wastes, Season One. **Candidates:** WSC-025 and WSC-026. [Exact source inventory and windows](WINGED_ATTACKERS_SOURCE_REVIEW_2026-10-25.json) · [Season-one backlog](WASTES_S1_CREATURE_SEARCH_2026-10-24.md).

## Scope and method

Interpreted eleven selected Parakeet windows and eleven selected Qwen cross-readings. The played encounter evidence is in E057 and E076; a short E058 recap window in each export resolves the crater pet's source label. Six complete subtitle exports were parsed and fingerprinted once for cue lookup, without interpreting every cue. The JSON records source paths, SHA-256 fingerprints, cue counts, end times and actual window/cue bounds. The ignored cache is `local/creature-search/winged-attackers-2026-10-25/sources.json`.

The existing E077 dossier was read for the separate speaking vessel occupant's identity boundary, without new E077 transcript or audio review. No audio was heard, full-export ASR disagreement computed, original export changed or episode-research pointer advanced. Agreement between exports is not accuracy or audio verification. Clocks are approximate recording navigation, not word alignment, and speaker labels are not verified diarization.

## WSC-025 — blue-black chasm flyers

Published [Blue-black chasm flyers](../world/creatures/blue-black-chasm-flyers.md). The descriptive article title accommodates the explicitly encountered second flyer and additional calls; it does not assert a named species or fixed population. Original discovery wording remains in the shortlist JSON.

| Evidence | Supported reading | Boundary |
| --- | --- | --- |
| [E076](../episodes/E076.md), ~01:09:22–01:11:38 | Large leathery-winged creature descends behind Nash; slick blue-black skin, a large mouth and an eerie moan are described. | No individual name or intelligible dialogue. Batlike comparison does not establish a bat species or demon type. |
| E076, ~01:18:49–01:20:25; ~01:32:48 | Nash's Sleep has no effect; Nash and Vorel become frightened, then recover before the kill. | No sleep-immunity rule follows from one casting. Their existing memory penalty is separate, not a new flyer effect. |
| E076, ~01:31:38–01:32:18 | The large tail has rose-thorn-like projections and a jagged arrowhead; it strikes Nash. | More specific than the discovery shorthand “hooked tail.” The damage is slashing; no venom is established. |
| E076, ~01:34:08–01:34:40 | Vorel learns through the Eye of Groxl that bright light offers a route to defeating the creature. | Artifact-supplied information, not a witnessed light test, fixed radiant vulnerability or instant sunlight death. |
| E076, ~01:36:40–01:37:20 | Hope's shotgun shot passes through the eyes; the creature falls into the darkness. | Explicit kill of that individual, not a cleared chasm. |
| E076, ~01:46:40–01:47:23 | More creatures cry above. A second dives toward the portal, loses its head as the endpoint is changed/closed, and the fallen head still bites briefly. | One local portal adjudication, not a universal weapon rule. The residual-current comparison is not an electrical attack, regeneration or proof of lasting independent life. |

The apparent group is kept separate from E077's named, speaking, armed vessel occupant Lethanphius. Wings, proximity and hostility do not identify the flyer as that reasoning actor. The chasm creatures also have no established identity with the crater pet or the Outlands wyverns. Their observed attacks support a creature account without an intelligence score or an assertion of mindlessness.

## WSC-026 — crater wyvern

Published [Crater wyvern](../world/creatures/crater-wyvern.md).

| Evidence | Supported reading | Boundary |
| --- | --- | --- |
| [E057](../episodes/E057.md), ~02:10:39–02:11:55 | A robed figure calls it his pet; the bugbears call it the Wormfather's. A large winged lizardlike beast circles and dives at Hope. | Ownership and Wormfather association are attributed wording. An initial “not a dragon” remark is immediately walked back as knowledge the characters would not have. No training history or identification with Dolo Popio. |
| E057, ~02:16:35–02:18:33 | A scorpionlike tail injects liquid into Hope, causing named poison harm; a bite hits her shoulder/chest. | Poison is directly supported here, unlike the chasm flyer's thorned tail. No standard poison formula or full stat block. |
| E057, ~02:33:28–02:33:59; ~02:37:01–02:37:25 | The sting hits dragon-form Nash, but the successful save prevents poison harm; a claw swipe misses. | Piercing harm still occurs. Narrative blood/venom reversal is not universal dragon immunity or a reproductive/feeding mechanism. |
| E057, ~02:41:31–02:41:47; ~02:43:59–02:44:57 | The wounded pet lands fatigued. Stanley's Booming Blade/Diplomacy strike kills it with a thunderous rupture, and it falls before Nash. | Vorel's preceding kill at ~02:43:07 is a different combatant. No second wyvern death or innate death-explosion ability. |
| [E058](../episodes/E058.md), ~00:07:49–00:08:14 | The recap explicitly calls the defeated pet a wyvern. | This resolves the source label through retrospective recap wording, not a new live encounter or an anatomical guess. It does not turn the removed skyfall body into this pet. |

The title combines the later recap's explicit label with the locality. The initial warning against automatic wyvern classification is resolved by that source wording, not ignored. No official D&D comparison, new creature origin or same-individual relationship with E093's Outlands animals is inferred. The existing E057 dossier supplies the earlier tracks/removed body context; the existing E058 dossier supplies the continuing bugbear battle. Those are separate from the pet's demonstrated death.

## Persisted work and next review

Added both articles, short category rows and policy/backlog mappings. Narrow E057/E058 follow-ups distinguish the played kill from the recap identification; the E076 amendment refines tail anatomy, artifact information and the partial portal outcome. Original discovery evidence and source fingerprints remain preserved. No existing reasoning NPC is moved into the bestiary.

There are now **26 published search subjects/clusters represented by 30 articles**, excluding the original Chicken Lords and Pixie Hulks; one cluster remains routed to character context, three need focused review and two are separately placed one-off leads. Next are WSC-027 six-limbed desert burrower and WSC-028 Pit froghemoth/altered upper form. The former requires separating observed incursion from the Soulbroker's claims; the latter requires a form/personhood check around its private mental bargaining and escaping upper cocoon.

## Validation

Targeted Markdownlint passed for nine changed Markdown files. The scoped link check resolved 284 relative file links; article footnotes, Current status placement, metadata separation, the 32 stable candidates, 30 article mappings, next-work pointer and all 22 recorded windows passed checks. Source fingerprints were checked against the once-parsed local cache, without rehashing or claiming a full interpretive export review. Scoped `git diff --check` passed for this batch.

The unscoped diff check returned exit 2 for trailing whitespace at `delvers/world/CONSISTENCY_LEDGER.md:67`, in concurrent work outside this pass. It also emitted LF-to-CRLF conversion warnings. This pass did not edit that ledger; the result does not invalidate the scoped Wastes check.
