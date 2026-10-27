# The Principal — related names, places and institutions audit

**Prepared:** 2026-10-27. **Status:** Targeted *repository-text* audit after owner-confirmed canonical spelling [D-044](../project/DECISIONS.md), **not** an exhaustive source-listening or map-coordinate verification. [Consolidation plan](../project/WASTES_CAMPAIGN_CLEANUP_PLAN.md) · [map source](WASTES_KNOWN_MAP_ORTHOGRAPHY_2026-10-27.md) · [active entity migration](../project/WASTES_CLEANUP_MANIFEST.md).

## Canonical editorial name rule

**The Principal** is the owner's confirmed canonical name for the antagonist formerly written **the Principle**. Compounds identifying *this same person or his named city/territory* must inherit **Principal**, not preserve the wrong spelling as a competing canonical option.

This means **Principal City**, not **Principle City**, and **the Principal's Lands**, not **the Principle's Lands**. The latter is **explicitly printed** on the large *Known Wastes* map. **Principal City is a well-supported referent in episode research and existing place indexes, but has NOT independently been verified as a printed label on that specific map**. Its display spelling follows the now-settled name of the associated ruler. The direct city name is not a claim that the heroes entered it, that all of its history was witnessed or that it shares the territory's geographical limits. Retain the old word forms as source/search aliases and stable URLs; do not rewrite recorded utterances or frozen research.

## Checked referents and boundaries

| Referent or term | Recommended written form | Evidence scope / distinction | Disposition |
| --- | --- | --- | --- |
| Antagonist / historical ruler | **The Principal** | Owner-confirmed map orthography. Elhandari use the personal name *Vladimir* in E115 per episode dossier, but exact full naming and spellings beyond **Principal** remain source-specific | Canonical; one antagonist; `world/characters/the-principle.md` retained as legacy path |
| City named for/associated with the ruler | **Principal City** | Existing [places index](../world/PLACES.md) already groups it with the Principal's Lands. [E026](../episodes/E026.md) records **Bertrand's account** of Lactids in the undercity of its spires. [E106](../episodes/E106.md) records interested statements of an attack. [S3E13](../episodes/S3E13.md) describes **heroes flying north toward the city's ruined vicinity and observing rifts**. [S3E019](../episodes/S3E019.md) says **the full planned city exploration and rail confrontation went unplayed** | Canonical editorial name; older `Principle City` only legacy ASR/working alias. **Visited vicinity ≠ explored city** |
| Wider map-labelled land | **The Principal's Lands** | **Direct** known-map label. The city and mapped territory are related but do not necessarily have equal boundaries; the map's time period/handout availability is not proven | Canonical geographical label; retain old variants as search aliases only |
| The Principal's government, soldiers, machinery and claims | **the Principal's regime**, **the Principal's soldiers**, **the Principal's chrome forces**, etc. | Ordinary possessive descriptions are not automatically formal names. Different factions (e.g. Koromukishi, Toyota Host, military/industrial hierarchy) need their own source-grounded identities | Correct possessive spelling in new editorial prose; **do not create fictitious titled entities** |
| Lactid Cartel, underground population | **Lactids**, **Lactid Cartel** (as supported by the source) | E026's reported association with Principal City and S3E019's GM description of **unexplored** subterranean society are distinct. Do not turn all the city's inhabitants into cartel members, or treat unused GM preparations as visited scenes | Keep separate race vs organization vs location references; flag under new Races audit |
| Three spires / upper and lower city / planned railway | **Principal City spires**, **proposed railway**, qualified prose | S3E019 GM retrospective about planned city exploration and three finger-named spires. Do not infer a complete played route, definitive spire names, social census, or the survival of an Arcanum Universalis citadel | `unused-prep`/retrospective-only fields; not newly played places |
| Solar Mines, adjoining rift/canyon, northern Leaden Fingers | Existing distinct geographical names | Played late-campaign footage observes damage near the city and at the Solar Mines; one does not prove these are part of a surveyed municipal boundary | Keep separate place identities, with verified spatial relations only |
| *Principal Dombrovski* in CHIDS-era accounts | **Principal Dombrovski** pending source verification | In [Cerinthala](../world/characters/cerinthala.md) and [CHIDS](../world/places/chids.md), the word appears to be a role/title in **ancient researchers'** history, not the named ruler **The Principal**. Cerinthala's history is attributed testimony | **Do not normalize to The Principal Dombrovski or merge identities** without evidence |
| Generic *principal* as an adjective | *principal* (ordinary word) | E.g. principal searchers, principal ambush, principal weapon; the lower-case term means primary/main | **Never global-find-and-replace** ordinary English |
| Delvers, Inverse, Star Trek one-off | Their own established names and terminology | Campaigns are separate fictional realities, including the joking Star Trek `USS Principal` references | Exclude from Wastes antagonist/entity bulk corrections |

## Where the old city spelling was found

A focused GitHub code search for `"Principle City"` returned **37 files** in `main` (including episodic source/research and historical archives), whereas `"Principal City"` returned **79** (including many original SRTs). Search indexing and file-result ranking are **not exhaustive occurrence counts** and these results were inspected as discovery leads only. Examples of **active, maintained** pages using the older city spelling at the inspected baseline:

- [Arc Six narrative](../narrative/ARC_SIX.md): late-war damage near the ruined city.
- [Solar Mines](../world/places/solar-mines.md): S3E13 rift reconnaissance and S2E03 council forecasts.
- [Leaden Fingers / Stormlands](../world/places/leaden-fingers-stormlands.md): the canyon and northern rift near the ruined city.
- [Vorel biography](../world/characters/vorel.md): a creator retrospective about a scholar associated with the city.
- [World consistency ledger](../world/CONSISTENCY_LEDGER.md): late played observations and historical-claim registers.
- [Review queue](../project/REVIEW_QUEUE.md) and [S3E019 roundtable dossier](../episodes/S3E019.md): unused city plans, title aliases and source-listening tasks.
- [E026](../episodes/E026.md), [S3E13](../episodes/S3E13.md) and other **episode dossiers**: important for original timestamped evidence.

**Priority:** Update live **reader-facing world/narrative** prose and compact indexes first, with deliberate source-note preservation. Episode dossiers, original ASR, complete research reports, pre-edit archives, tools that search historical spellings and quoted primary-source phrases should be handled by separate reviewed passes or preserved as-is. A raw ASR occurrence of “Principal City” is not proof the map printed that label.

## Do not overclaim the city's history

1. **E026:** Bertrand's account of Lactid undercity/spires is **NPC testimony**, not a party visit or definitive demographic survey.
2. **E106:** A reported attack on Principal City is not itself direct eyewitness access to every impact or claim in the Principal's staged historical visions.
3. **S3E13–S3E14:** The protagonists travel toward or near the ruined city's region and **witness planetary rifts/lava**; do not equate that with exploring the city or recovering its civic plans.
4. **S3E019:** Beau describes **unused** planned city, three spires, rail battle and underground culture. This is creator testimony about design, not previously unknown played scenes. The city's *existence and later ruin* can be established elsewhere without treating the omitted exploration as completed.

## Migration checklist and verification

- [x] Record **Principal City** as canonical derivation from D-044 and distinguish it from **the Principal's Lands**.
- [x] Identify examples of the wrong spelling in active reader-facing pages, dossiers and historical material.
- [x] Record **Principal Dombrovski** as an unrelated/ambiguous title that must not be rewritten by name normalization.
- [ ] Do **full current-tree case-sensitive and case-insensitive** token inventory for `Principle`, `Principle City`, `Principle's`, `Principal`, and longer compounds; label each match *editorial prose*, *primary quotation*, *generated text*, *legacy alias*, *unrelated homograph*, or *retrospective*. GitHub code-search hit counts do **not** replace this census.
- [ ] Update every unambiguous **live editorial** occurrence after source review, including world profiles, indexes, arc prose, and any navigation anchors. Keep source files, frozen archives and appropriate specialist-register raw quotations intact.
- [ ] Create a dedicated **Principal City** place article **only if** source coverage justifies a distinct subject beyond the combined index entry; do not populate it with S3E019 unused design as played urban history.
- [ ] Add Principal City's confirmed place identity and alias to a future full `world/entities.json` schema migration without inventing a map coordinate or new entity.
- [ ] Run changed-file Markdownlint and full incoming link/anchor checks during actual page migration; verify final-state claims independently.

**Scope note:** This targeted report documents canonical spelling, sampled affected references and research boundaries. It is not an audio-derived city history and does not certify complete repository spelling normalization.
