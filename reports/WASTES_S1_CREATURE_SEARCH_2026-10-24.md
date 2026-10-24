# Wastes Season One — creature candidate search

**Date:** 2026-10-24. **Status:** Initial discovery pass complete; candidate verification and bestiary expansion remain open. **Scope:** The Wastes Season One, using existing episode dossiers. [Category](../world/CREATURES_AND_MONSTERS.md) · [Scope policy](../project/WORLD_CREATURES_PLAN.md) · [Machine-readable inventory and shortlist](WASTES_S1_CREATURE_SEARCH_2026-10-24.json).

## What was searched

The keyword scan read all **130 available E-numbered dossiers**: E000–E128 plus E013.5. Broad creature, animal, anatomy, transformation and monster-name terms were followed by a supplemental name/parasite search. The companion JSON preserves exact patterns, per-file SHA-256 fingerprints, hit counts, continuity classifications and the curated candidates. Complete raw hit text is retained locally at `local/creature-search/wastes-s1-2026-10-24/dossier-keyword-hits.json`; it is a routing aid, not a canonical source.

This is **not** a claim to have manually interpreted every dossier or researched every original recording again. Targeted dossier passages were read to triage the leads below. No SRT export was reviewed in the **initial dossier pass**, no new ASR measurement was computed, and no audio was heard. The later sand-squid follow-up is separately documented below. The original shortlist's clocks are inherited approximate recording windows from the existing dossiers, not newly verified word timings. Keyword misses, compressed dossier descriptions and unresolved identities limit completeness. The scan uses corrected archive IDs, not publisher numbering.

### Continuity boundaries

- **127 dossiers** fall in the main-campaign/same-world corpus, including the in-character E013.5 supplemental and the E107–E109 Dunebreaker prequel. The prequel belongs **long before Dusthill**, not after the main-party events of E106.
- **E000** is setup/world introduction, not a played creature-encounter survey.
- **E043** is an alternate-setting Christmas adventure and is excluded from Wastes creature evidence; its blink dog must not identify E008's doglike creature.
- **E127** is a Christmas one-off **within a Wastes setting**, with no established position in the main-party calendar. Its two leads are isolated below.
- Delvers, Inverse, later Wastes seasons and bonus commentary are outside this scan.

## Initial result and drafting order

**31 additional candidate subjects or research clusters:** **12 suitable for bounded drafting from existing dossiers**, **17 requiring focused identity, behavior or continuity review**, and **2 separate Wastes-setting one-off leads**. These are editorial triage judgments, not verified species counts or intelligence classifications. Chicken Lords and Pixie Hulks already have pages and are not counted again.

The first ranked batch—**Chester the bearsaurus**, the **Dunebreaker fruit ooze** and the **tainted displacer beast**—is now published from the existing dossiers. Each has distinctive observed traits and a bounded individual outcome. The **brain-backed spiders** and **skeleton-spawning flesh giant** are now published as the second ranked batch. The **black puddings** and **basilisk of the under-Pit caves** are now published as the third ranked batch. Next are **luminous desert beetles** and the **stormland Tyrannosaurus**, preserving their observed traits and source limits. Some later draftable subjects warrant only short articles; do not pad an entry to match a major creature's history.

No canonical creature entry was added during the initial dossier search. After the sand-squid follow-up and three ranked publication batches, the cumulative list is **32 subjects/clusters: eight published, five draftable, 17 requiring focused review and two separately placed one-off leads**. Candidate IDs WSC-001–WSC-031 remain stable.

## Owner-supplied follow-up — sand squid

**WSC-032 — [Sand squid](../world/creatures/sand-squid.md), published.** The owner identified their recurring role as a food source and ingredient. [Targeted transcript review](SAND_SQUID_SOURCE_REVIEW_2026-10-24.md) found direct ecology and hunting evidence as well as repeated culinary uses: sandwiches, eggs, dried rations, canned supplies, soup, camp meals and creamy juice squeezed into coffee. The previous low-information ranking overlooked that cultural importance and the fuller E015 hunt.

The follow-up scanned 279 available Season One subtitle exports for squid-related cues, then interpreted selected windows in nine primary-export episodes and cross-read core E012/E015 descriptions in Qwen. It is not full-episode or audio verification. The unrelated E018 shelter carcass remains unidentified; CHIDS's squidlike pool organisms are not identified as sand squid, and no ancestry from the Dunebreaker ooze is established. The companion shortlist JSON now records WSC-032 and links its separate source inventory.

## First ranked publication batch

**2026-10-24:** Created these three subject pages, added category navigation and marked their stable candidate IDs published in the companion JSON. This is synthesis of the existing E020, E109, E119 and E120 dossiers, not a new episode-analysis or transcript/audio review. Each page introduces its subject, explains meaningful traits and changes, and closes with Current status; episode IDs, inherited clocks and source limits remain in footnotes. Chester's reported laboratory origin, the ooze's historical chronology and individual identity, and the beast's unexplained condition retain their boundaries.

| ID / published article | Dossier and approximate window | Supported lead | Boundary retained |
| --- | --- | --- | --- |
| **WSC-001 — [Chester the bearsaurus](../world/creatures/chester-the-bearsaurus.md)** | [E119](../episodes/E119.md) 00:36–00:48<br>[E120](../episodes/E120.md) 00:20–01:12 | Bear-like, antlered predator with massive hindquarters, small forelimbs and a partly reptilian head; climbs by leaping and dies during the hunt. | Laboratory creation, age and ecological damage are Dilo's account. Use bearsaurus as the existing display form; preserve barosaurus as an ASR variant in notes. A name alone does not make this observed animal a reasoning NPC. |
| **WSC-002 — [Dunebreaker fruit ooze](../world/creatures/dunebreaker-fruit-ooze.md)** | [E109](../episodes/E109.md) 00:39–01:08; 01:51–02:43 | Fruit-speckled gelatin escapes through drains and grows by absorbing waste, debris and bodies; steam breaks it apart and the final cherry-bearing globule is destroyed. | Treat as one individual. Its growth explanation is retrospective GM confirmation; faint fiend-like detection does not identify it as a demon. |
| **WSC-003 — [Tainted displacer beast](../world/creatures/tainted-displacer-beast.md)** | [E020](../episodes/E020.md) 01:31–02:43 | Wounded, tentacled cat-like predator with deceptive shifting position and exposed brain tissue; killed in the Black Mine chasm. | Describe the observed specimen and apparent displacer-beast identity; do not invent why it was altered or claim a sourced D&D deviation. |

## Second ranked publication batch

**2026-10-24:** Published WSC-004 and WSC-005 from the existing E067, E073, E074 and E075 dossiers, without new transcript or audio review. The spider article distinguishes the giant's mental control from the smaller swarms' venom and preserves the uncertainty around Cerinthala's pouch. The flesh giant remains an unnamed individual whose death ends its spawning; no creator, standard species or cleared keep is inferred. Both articles use in-universe prose, evidence footnotes and Current status last.

| ID / published article | Dossier and approximate window | Supported lead | Boundary retained |
| --- | --- | --- | --- |
| **WSC-004 — [Brain-backed spiders](../world/creatures/brain-backed-spiders.md)** | [E073](../episodes/E073.md) closing shaft encounter<br>[E074](../episodes/E074.md) 00:08–01:20<br>[E075](../episodes/E075.md) 00:32–00:47 | Giant spider with exposed pulsing brain and smaller brain-marked swarms; poison and domination make the shaft encounter distinctive. | The giant dies in E074. Separate large and small forms; Cerinthala's pouch does not by itself prove their origin, breeding or control mechanism. |
| **WSC-005 — [Skeleton-spawning flesh giant](../world/creatures/skeleton-spawning-flesh-giant.md)** | [E067](../episodes/E067.md) 01:39–02:27 | Malformed flesh-and-bone body produces skeletons through shoulder cavities and fresh wounds; its death ends further spawning. | Use a descriptive name. No official species, creator or claim that every skeleton at Kervalon came from it is established. |

## Third ranked publication batch

**2026-10-24:** Published WSC-006 and WSC-007 from the existing E042, E045 and E051 dossiers, without new transcript or audio review. The pudding article uses demonstrated splitting, corrosion and the cave encounter's final outcome rather than importing the full rules list. The basilisk article preserves the sequence of death, bone-javelin crafting, later ingredient retrieval and two consumed preparations that restore Hope and Vorel. It does not backdate an extracted antidote to E045 or establish a universal formula. Both entries use in-universe prose, footnotes and Current status last.

| ID / published article | Dossier and approximate window | Supported lead | Boundary retained |
| --- | --- | --- | --- |
| **WSC-006 — [Black puddings](../world/creatures/black-puddings.md)** | [E042](../episodes/E042.md) 01:42–03:10 | Two corrosive cave masses split under slashing attacks and damage Hope's equipment. | Nash supplies the identification. Keep demonstrated corrosion and splitting separate from the full rules list discussed at the table. |
| **WSC-007 — [Basilisk of the under-Pit caves](../world/creatures/basilisk-of-the-under-pit-caves.md)** | [E045](../episodes/E045.md) 00:43–01:28; 02:02–02:12<br>[E051](../episodes/E051.md) 02:01–02:29 | Eight-legged reptile with a petrifying gaze; its remains later contribute to restoring petrified companions. | The beast dies in E045. Later preparation is not a second kill; do not backdate extraction of a finished cure to the earlier digestive-oil discussion. |

## Suitable for bounded drafting

A candidate here has enough dossier support for a concise, qualified article. The label does not assert that it is campaign-original, non-intelligent by a rules score, or audio-confirmed.

| ID / candidate | Dossier and approximate window | Supported lead | Boundary / next check |
| --- | --- | --- | --- |
| **WSC-008 — Luminous desert beetles** | [E007](../episodes/E007.md) 00:06–00:40 | Large beetles with luminous fleshy appendages surround Fate 4 at night; travelers use noise and movement to avoid them. | Exact dimensions, diet and eventual departure remain listening questions. Suitable for a short entry; no need to invent a species name. |
| **WSC-009 — Stormland Tyrannosaurus** | [E065](../episodes/E065.md) 02:29–02:38<br>[E066](../episodes/E066.md) 00:06–00:45 | Huge predator crushes Fate 4, falls into a storm-drain pit and is killed; teeth and bones become tools and salvage. | Keep this animal distinct from Polymorph forms of Vorel or Stanley. No cause for its enormous size or connection to the storm is established. |
| **WSC-010 — Outlands wyverns** | [E093](../episodes/E093.md) aerial battle, approximately 00:57–02:51 | Flying predators ram the Traveler's Twin and attack with bites and venomous stings. | Separate wyverns from the accompanying winged beastmen. One is turned into a falling rat with no witnessed final landing or reversion; do not resolve every individual's fate. |
| **WSC-011 — Tentacled purple fungi** | [E021](../episodes/E021.md) 00:09–00:58 | Large animate purple mushrooms grapple and strike in the Black Mine. | Unidentified hostile fungi, not a confirmed named fungal species; harmless mushroom beds and later Elhandar fungi are separate. |
| **WSC-012 — Lizardfolk riding raptors** | [E027](../episodes/E027.md) 02:40–02:50<br>[E028](../episodes/E028.md) 00:07–01:42<br>[E064](../episodes/E064.md) 01:23–02:40 | Raptor-like animals serve hunters and carry the party during the escape from Razak Val; their hides are also used for repairs. | Separate wild behavior, mounts, individual deaths and the raptor named Mawstorm from Vorel's similarly named sword. Exact species remains descriptive. |

## Focused review before drafting

Resolve these particular questions rather than promoting a vague encounter label into a named species. Cross-episode clusters may need to split into several entries or remain dossier material.

| ID / candidate | Dossier and approximate window | Supported lead | Boundary / next check |
| --- | --- | --- | --- |
| **WSC-013 — Green-case mimic** | [E008](../episodes/E008.md) 02:00–02:41 | A sealed green case becomes a tongue-bearing attacker in Leopold's facility. | Recheck its defeat and anatomy in targeted SRT windows before drafting; the accompanying doglike threat is a separate creature. |
| **WSC-014 — Doglike facility predator** | [E008](../episodes/E008.md) 02:00–02:41 | Animal-like creature menaces the party during the mimic encounter and may teleport. | Do not name it a blink dog or phase creature on the current dossier alone, or import the unrelated E043 blink dog. |
| **WSC-015 — Gibbering mouther** | [E009](../episodes/E009.md) 02:15–03:00 | Named attacker during the attempted escape from Leopold's collapsing facility. | The dossier offers limited anatomy and final-fate detail. Keep separate from the E020 displacer beast; check targeted transcript passages. |
| **WSC-016 — Concealing mushroom-pit spider** | [E044](../episodes/E044.md) 01:42–02:09 | Large partly hidden or invisible spider attacks amid luminous mushrooms; legs are harvested after its defeat. | Do not silently call it a phase spider, merge it with CHIDS brain-spiders or attribute the mushroom spores to the spider itself. |
| **WSC-017 — Pale tentacled cavern organism** | [E042](../episodes/E042.md) 00:53–01:08<br>[E045](../episodes/E045.md) 02:02–02:12 | Long worm-like creature blends with pale wall strands; a later body of the apparent same kind is petrified. | A warning sound and retreat are observed, not a kill. Name, ecology and exact relation between the two specimens remain unknown. |
| **WSC-018 — River headache creatures** | [E045](../episodes/E045.md) 02:28–02:55<br>[E046](../episodes/E046.md) 00:00–01:01 | Dark humanoid river figures cause dread, headache and necrotic or psychic harm. | Utterances are untranslated and personhood is unresolved. Check reasoning/NPC fit before creating a bestiary article; do not assign a standard undead identity. |
| **WSC-019 — Froghemoth gut inhabitants** | [E052](../episodes/E052.md) 01:16–02:23<br>[E053](../episodes/E053.md) 00:20–01:58 | Light-avoiding digestive organisms and larger thread-bearing or tentacled roper-like inhabitants occupy the interior. | Several descriptions may indicate different organisms. Reconcile the sequence and distinguish incidental digestive fauna from distinct subjects before naming pages. |
| **WSC-020 — Bloodsucking desert swarm** | [E059](../episodes/E059.md) 02:04–02:20 | Vast dark swarm forces the travelers to shelter in Tiny Hut. | No confirmed species or individual morphology in the dossier; do not identify it as stirges, mosquitoes or another standard monster. |
| **WSC-021 — Parasitic headworms and related worm forms** | [E058](../episodes/E058.md) 00:30–00:55<br>[E063](../episodes/E063.md) 02:15–02:30<br>[E064](../episodes/E064.md) 01:03–01:23<br>[E075](../episodes/E075.md) 00:47–01:06<br>[E080](../episodes/E080.md) 00:51–01:00<br>[E081](../episodes/E081.md) 00:03–00:19 | Observed head parasites, a captured bedchamber worm, an outbreak of host transformation and later explosive or exhaled worms. | This is a research cluster, not one established species. Separate host testimony, observed parasites, spawned forms and transmission hypotheses; Dolo Popio remains a reasoning antagonist. |
| **WSC-022 — Translucent psychic wall-passers** | [E070](../episodes/E070.md) 00:29–00:56 | Glowing tentacled creatures pass through walls, respond to strong emotion and recoil from the squeaking plush toy. | Keep the toy separate from living creatures. Recheck agency and identification rather than inventing a standard species. |
| **WSC-023 — CHIDS hellhounds** | [E070](../episodes/E070.md) 02:00–02:16<br>[E071](../episodes/E071.md) continuing conference-room fight | Flaming hounds with fire breath attack inside the facility. | Review the continuing fight for last observed survivors and distinguish observed behavior from baseline rule assumptions. |
| **WSC-024 — Corpse-bearing ice constructs** | [E072](../episodes/E072.md) 02:25–02:29<br>[E073](../episodes/E073.md) opening continuation | Four enormous animated ice bodies enclose preserved corpses and attack around the resting party. | No universal ice-golem identity or explanation for every enclosed person is established; not all four are confirmed destroyed in the continuation. |
| **WSC-025 — Blue-black hooked-tail flyer** | [E076](../episodes/E076.md) 01:09–01:37 | Leathery winged attacker with a hooked tail causes fear and is killed by Hope. | Species and origins remain unidentified. Do not merge with the speaking winged vessel occupant encountered in E077. |
| **WSC-026 — Wormfather party's winged stinging pet** | [E057](../episodes/E057.md) 02:04–02:45 | Dragon-like winged pet fights alongside the crater attackers and is killed by Stanley. | Not the retrieved skyfall creature; no automatic wyvern classification or identity with E076's flyer. |
| **WSC-027 — Six-limbed desert burrower** | [E128](../episodes/E128.md) 01:25–01:37 | Immense gear-scaled creature falls through a rift and burrows into Earth as a violent sand front forms. | Morphology and entry are witnessed; planetary conversion purpose is the Soulbroker's claim. Name, intelligence, origin and full mechanism remain unknown; no invented species or lethal outcome. |
| **WSC-028 — Pit froghemoth and altered upper form** | [E039](../episodes/E039.md) 02:45–03:00, testimony<br>[E041](../episodes/E041.md) 00:50–02:11<br>[E046](../episodes/E046.md) 01:59–02:18<br>[E052](../episodes/E052.md) 00:00–03:04<br>[E053](../episodes/E053.md) 00:00–00:20 | Three-eyed pit predator and later enormous many-eyed form with an inhabitable digestive tract and separating upper cocoon. | E053 contains private mental bargaining and the creature's claim of intended ascent. Resolve form/NPC routing, continuity of specimens and attribution first. The upper portion escapes; the entire organism is not confirmed dead. |
| **WSC-029 — Red memory-devouring organisms** | [E074](../episodes/E074.md) 02:35–02:49<br>[E075](../episodes/E075.md) 00:07–00:20<br>[E080](../episodes/E080.md) 00:51–01:00<br>[E081](../episodes/E081.md) 00:40–01:13 | Many-faced red mass makes tethered lookalikes and inflicts a persistent penalty; later red growths attack and burrow. | Copies can appear to speak. Check agency and whether later red organisms are the same kind before treating this as one non-reasoning species. |

## Wastes-setting one-off leads — separate chronology

| ID / candidate | Dossier and approximate window | Supported lead | Boundary / next check |
| --- | --- | --- | --- |
| **WSC-030 — Figgy-pudding ooze** | [E127](../episodes/E127.md) 00:27–00:41 | Sugar-decorated hostile pudding appears in the laboratory Christmas test and is cut apart by Riley. | Wastes-setting one-off with no supplied main-campaign calendar placement. Do not merge it with the E109 fruit ooze. |
| **WSC-031 — Undead reindeer and powered Rudolph** | [E127](../episodes/E127.md) 01:00–01:32 | Mutilated undead flying deer and a separate battery-equipped red-nosed attacker threaten the test subjects. | Keep the undead herd and powered individual distinct; Rudolph is destroyed. This is a constructed test environment, not evidence of a literal North Pole or a universal reindeer type. |

## Exclusions and low-information leads

| Lead | Evidence | Routing decision |
| --- | --- | --- |
| Blort and his hag mother; the vampire-like stranger | [E029](../episodes/E029.md), [E032](../episodes/E032.md), [E033](../episodes/E033.md) | Blort negotiates and addresses his mother; the hag is a reasoning antagonist. The stranger's nature is unresolved. Unusual shape, fangs or aggression do not establish a non-reasoning creature. |
| Hungui, the CHIDS tree/hive, Lethanphius, Dollo Poppio, the Pandemonium leviathan and Malhya | [E044](../episodes/E044.md), [E009](../episodes/E009.md), [E077](../episodes/E077.md), [E080](../episodes/E080.md), [E113](../episodes/E113.md), [E124](../episodes/E124.md) | Reasoning, speaking or bargaining actors; route to character/faction/world treatment. Do not merge E077's speaking winged subject with E076's unnamed flyer. |
| Named dragons, demons, kobolds and other reasoning NPCs | [Character index](../world/CHARACTERS.md) | Their anatomy or hostile role is not grounds for reclassifying their biographies as beasts. Existing NPC exclusions in the category policy still apply. |
| Ritual sand sharks | [E016](../episodes/E016.md), ~01:35–01:51 | Vorel's experienced vision/trial, not an independently witnessed wild population. Preserve vision evidence separately. |
| Huge shelter carcass | [E018](../episodes/E018.md), ~00:37–00:46 | The shelter animal remains unidentified. Sand squid have been separated and promoted to WSC-032 after targeted review; do not identify this carcass as a squid, dinosaur or another candidate without evidence. |
| Early giant spiders, cave bats, live-snake appetizers, mundane fish and ordinary hunting remains | [E002](../episodes/E002.md), [E044](../episodes/E044.md), [E060](../episodes/E060.md), [E119](../episodes/E119.md) | Real animal leads, but this initial pass found too little distinctive subject information to prioritize separate articles. No claim that they are absent from the world. |
| Reanimated miners and other undead bodies | [E014](../episodes/E014.md), [E015](../episodes/E015.md), [E018](../episodes/E018.md), [E019](../episodes/E019.md), [E021](../episodes/E021.md), [E114](../episodes/E114.md) | Separate constructed/compelled bodies from reasoning undead and victims' identities; the skeleton-spawning giant and ice constructs already have specific leads above. Do not assume all undead share an origin or lack agency. |
| Character transformations, disguises, summons, toys, vehicles and place names | [E068](../episodes/E068.md), [E070](../episodes/E070.md), [E103](../episodes/E103.md), [E120](../episodes/E120.md) | Polymorphed dinosaurs, the plush mind flayer, a temporary summoned snake and disguised elf “deer” do not independently establish new creature species. “Monster truck,” Golden Gargoyle and Dr. Spider likewise produce keyword false positives. |

## Next bounded work and publication checks

1. Continue with WSC-008 luminous desert beetles and WSC-009 stormland Tyrannosaurus; the first seven ranked subjects are published. Use targeted source windows only where a material claim remains unresolved; do not mark a complete episode reanalysis from excerpts.
2. For each subject, check first appearance, distinguishing traits and last known state across the cited dossiers. Preserve testimonial origins, alternative spellings and uncertain individual outcomes in notes.
3. Publish subject-focused in-universe prose under `world/creatures/`, with source/ASR details in footnotes and **Current status** last. Add only brief descriptions to the category index. Keep people and transformed forms distinct.
4. Resolve the froghemoth's bargaining mind, red-organism agency, worm-type relationships and E127's separate chronology before expanding those clusters. Do not convert source uncertainty into a fictional universal rule.
5. Run targeted Markdownlint, new relative-link and footnote checks, and `git diff --check`. A full transcript sweep, audio verification and full-repository audit remain outside this initial search.

The existing episode-research pointer and all source media/transcripts remain unchanged. This report is a bestiary discovery backlog, not an ASR accuracy result or a claim that every season-one creature has been found.
