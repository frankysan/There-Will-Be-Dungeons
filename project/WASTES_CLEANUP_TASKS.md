# The Wastes cleanup — task register

**Single source of truth for work status and next action.** Updated 2026-11-02. The Wastes campaign is complete through S3E18; the eleven-arc reader edition is available inside the **private repository**, not on a public website.

The checkbox beside a task is its only **current** completion flag: **[x]** means that task's stated scope passed, not that every related page, original audio or browser check is complete; **[ ]** means open, deferred or blocked. Never reuse or renumber `WCL-###` IDs; preserve their Markdown heading anchors.

**Preserved completion history:** The full pre-compaction register, including **all 208 original WCL sections**, is retained as a [byte-identical archival snapshot](../research/legacy/WASTES_CLEANUP_TASKS_PRE_COMPACTION_2026-11-02.md) from clean `main` HEAD `8e34d1eb` (524,273 bytes; SHA-256 `acc1d797f19886d4bcee46867a9f3348d733f076106e471d86cfc311d11f04f5`). Archived checkboxes are *historical*: only this live register governs current status and next action. The archive and Git history preserve verbose source/validation notes without requiring them in every completed entry.

**Current next action:** [WCL-147](#wcl-147) — review Emenil's reader-first biography and shared character-index summary against cited sources, preserving uncertain spelling and historical cutoffs. Bok Bok's separate safety-blocked lint/edit limits remain in effect; do not bypass them. **Most recent:** [WCL-063](#wcl-063) completed the bounded 152-file world census, including **151/151 Markdown targets and 2,248 six-domain matching link instances**, and one explicitly non-Markdown JSON exception; not a native-browser, original-audio or full editorial acceptance. **Open gates:** [WCL-083](#wcl-083)–[WCL-092](#wcl-092) original audio, [WCL-103](#wcl-103) browser and [WCL-191](#wcl-191)–[WCL-193](#wcl-193) special validation. **Inventories:** 152 world files; 332 maintained matrix paths. Edition private; no public deployment claimed.

**How to maintain this register:** Give each new task a stable, never-reused WCL ID, clear completion criteria, dependencies and evidence links. Keep **open** tasks sufficiently detailed to resume safely. When an independently verified task is **completed**, reduce its entry to **one concise paragraph**: checkbox, outcome, parent and one or two useful evidence links, noting important scope limitations where needed. Do not repeat full logs, hashes, test transcripts, source quotations or batch reports here; retain detailed per-file evidence in the [world census](WASTES_WORLD_FILE_CENSUS.json), original source pages, review queue, one-time archives and Git history. Mark a task complete only when its own acceptance gate passes; parents with unfinished required children stay open. Continue using [D-082](DECISIONS.md) for dependency-safe grouped work. Keep the manifest for file dispositions and the changelog for meaningful decisions, not duplicate completion journals.

## Edition, compatibility and publication

### WCL-001

- [x] **Approve eleven-arc boundaries and canonical numeric arc paths.** D-045/D-049 cover the E101 split, historical prequel, one-offs and compatibility constraints. Evidence: [decisions](DECISIONS.md), [chapter map](WASTES_NARRATIVE_CHAPTER_MAPS.md).

### WCL-002

- [x] **Produce and integrate all eleven narrative arcs into the private reading edition.** The integrated edition was merged in private PR #6; this checkbox is not a claim of audio-perfect fidelity. Evidence: [narrative index](../narrative/README.md), [historical execution record](../research/legacy/WASTES_CLEANUP_MANIFEST_PRE_TASK_REGISTER_2026-10-31.md).

### WCL-003

- [x] **Preserve all six original word-form arcs and season compatibility access.** Do not replace their bytes when improving the new edition. Evidence: [narrative navigation](../narrative/README.md), [D-049](DECISIONS.md).

### WCL-004

- [x] **Integrate eleven-arc reader navigation and historical-edition pointers.** Private routing and Markdown navigation were checked; public-site deployment is separate. Evidence: [narrative index](../narrative/README.md), [Wastes portal](../wastes/README.md).

### WCL-005

- [x] **Perform offline rendered-Markdown/source-link prepublication review for the edition.** Completed within offline preview limits, with interactive browser verification explicitly deferred by D-078. Evidence: [decision](DECISIONS.md), [historical validation record](../research/legacy/WASTES_CLEANUP_CHANGELOG_PRE_TASK_REGISTER_2026-10-31.md).

### WCL-006

- [x] **Merge the edition in the private repository.** PR #6 merged 2026-10-30; this is not an external website release. Evidence: [campaign plan](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-007

- [ ] **Run deferred interactive browser/anchor and responsive reader-navigation verification.** Deferred under D-078, not silently passed. Only check after actual native/browser evidence is recorded; the offline renderer strips raw HTML heading aliases. **Identified subtasks:** [WCL-104](#wcl-104) · [WCL-105](#wcl-105).

### WCL-008

- [ ] **Make a separate public-distribution decision if a public release is wanted.** *Conditional; not required for the current private edition.* Choose destination, subset of distributable content and non-leakage controls first (D-080). No deployment is implied or scheduled.

## Races, schema and coverage

### WCL-009

- [x] **Establish the Races domain with its initial two source-backed people/culture articles.** Owner-approved pilot; completeness of all peoples is a separate task. Evidence: [Races index](../world/RACES.md), historical B261.

### WCL-010

- [x] **Integrate the pilot `race_culture` v2 entity contract and check consumer compatibility.** Source-backed additive pilot; not a complete relationship graph. Evidence: [schema](../world/ENTITY_SCHEMA.md), [entities](../world/entities.json), historical B263–264.

### WCL-011

- [x] **Complete the initial reciprocal race/culture navigation connections.** Eight-page pilot integration with targeted checks. Evidence: historical B265.

### WCL-012

- [ ] **Assess and add remaining evidence-backed peoples/cultures.** Inventory candidates (e.g. Lactids, Harlequinari, elves, orcs, dwarves) before creating pages; create separate child task IDs for distinct approved articles. Do not assign unverified racial traits. Existing profiles' **campaign-backed origin histories** are separately scheduled under [WCL-196](#wcl-196) / [D-084](DECISIONS.md) rather than mistaken for new population page coverage. **Identified subtasks:** [WCL-055](#wcl-055) · [WCL-056](#wcl-056) · [WCL-057](#wcl-057) · [WCL-058](#wcl-058) · [WCL-059](#wcl-059) · [WCL-060](#wcl-060) · [WCL-061](#wcl-061) · [WCL-196](#wcl-196).

### WCL-013

- [ ] **Complete a current per-file Wastes world/reference census and disposition inventory.** The source-limited 152-path inventory, current file hashes, source windows, structural D-048 statuses and bounded six-domain incoming-link counts are complete under [WCL-062](#wcl-062) and [WCL-063](#wcl-063). **Still open as an editorial parent:** [WCL-147](#wcl-147) and other recorded reader-first candidate/source-first exception decisions must be addressed or explicitly retained, without conflating the census with original audio, factual accuracy, or native-browser acceptance. **Evidence:** [census](WASTES_WORLD_FILE_CENSUS.json).

## Places and equipment

### WCL-014

- [x] **Rework the Harbor article into reader-first place history and validate its links.** Historical B267–268; preserved major-rewrite source in [legacy archive](../research/legacy/).

### WCL-015

- [x] **Rework Razak Val and reconcile its Omnom/chronology follow-up.** Historical B269–272; specific last-state questions retained as uncertainty rather than invented outcomes.

### WCL-016

- [x] **Rework T'ietkalla into a reader-first historical place profile.** Historical B273–274; preserve prior source evidence.

### WCL-017

- [x] **Complete the remaining place-profile rewrites.** All 23 current place pages were structurally reviewed; the outstanding reader-first rewrites [WCL-201](#wcl-201)–[WCL-208](#wcl-208) now have individual source-bounded validation and [census evidence](WASTES_WORLD_FILE_CENSUS.json). The final three are [Leaden Fingers](../world/places/leaden-fingers-stormlands.md), [Leopold facility](../world/places/leopold-facility.md) and [Slavetown](../world/places/slavetown.md). Original audio, native-browser verification and unresolved historical questions remain separate.

### WCL-018

- [x] **Reconcile the Known Wastes map and canonical place-name crosswalk.** Completed [WCL-068](#wcl-068) and [WCL-069](#wcl-069): verified the private v3 source hash, linked approved names to places and differentiated mapped territory, city testimony and unused creator prep. Unverified original audio, map era, other fine labels, geography and publishing rights remain open questions, **not invented facts**. **Evidence:** [cartographic crosswalk](WASTES_CARTOGRAPHIC_CROSSWALK.md).

### WCL-019

- [x] **Complete the Fate Six reader-first equipment/ship article and linked-index verification.** Historical B250–258, including baseline and protected heading/source links.

### WCL-020

- [x] **Complete the selected finale item-custody and technology corrections.** Scoped historical B205–251 (e.g. Chrome's Bane, windboards, Hollow Ring, syringes). This is *not* a claim that every artifact or final inventory was verified.

### WCL-021

- [x] **Audit outstanding equipment/technology profiles and unresolved final custody.**

### WCL-022

- [x] **Complete Monsoon Cabbage's reader-first biography and post-rewrite correction.** Historical B276–278.

### WCL-023

- [x] **Complete Diontalus's reader-first biography and Stanley-agency cross-check.** Historical B279–282; [original preserved](../research/legacy/DIONTALUS_PRE_BATCH281_2026-10-31.md).

### WCL-024

- [x] **Complete Angelashi's reader-first biography and finale apparent-Nash correction.** Historical B284–285; [original preserved](../research/legacy/ANGELASHI_PRE_BATCH284_2026-10-31.md).

### WCL-025

- [x] **Complete the Soulbroker's source-backed biography and pact-status reconciliation.** Historical B286; [original preserved](../research/legacy/SOULBROKER_PRE_BATCH286_2026-10-31.md). His death does not itself banish Worldbreaker.

### WCL-026

- [x] **Complete Squirts's chronological biography and separate two deaths from the dead-head graft.** Historical B287; [original preserved](../research/legacy/SQUIRTS_PRE_BATCH287_2026-10-31.md). Chunks lives.

### WCL-027

- [x] **Complete the Principal's reader-first biography and separate the original, lunar copies and coerced Nash successor.** Historical B288; [original preserved](../research/legacy/PRINCIPAL_PRE_BATCH288_2026-10-31.md).

### WCL-028

- [x] **Reconcile Principal/Nash/Soulbroker cross-page facts, canonical name and old heart/status cutoffs.** Historical B289. Corrected `world/CHARACTERS.md`, `world/characters/nash-maggard.md`, `world/CHRONOLOGY.md` and `world/HISTORICAL_EVENTS.md`; no fabricated biological paternity, original Principal revival or universal soul ownership.

### WCL-029

- [x] **Audit the structure of `world/characters/nash-maggard.md`.**

### WCL-030

- [x] **Restructure Nash's biography into a reader-first eleven-arc account.** **Evidence:** [live biography](../world/characters/nash-maggard.md).

### WCL-031

- [ ] **Audit remaining character profiles and specialist-register exceptions.** Complete separate per-subject outcomes or task IDs rather than a single “all characters done” assertion. **Identified subtasks:** [WCL-047](#wcl-047) · [WCL-048](#wcl-048) · [WCL-049](#wcl-049) · [WCL-050](#wcl-050) · [WCL-051](#wcl-051) · [WCL-052](#wcl-052) · [WCL-117](#wcl-117) (Hope's completed restructure) · [WCL-118](#wcl-118) (Vorel's completed restructure) · [WCL-119](#wcl-119) (Stanley's completed restructure) · [WCL-120](#wcl-120) (Badass T's completed profile/navigation). **Parent exit pending:** These child outcomes do not establish exhaustive per-file character coverage; reconcile remaining dispositions via [WCL-063](#wcl-063) before closing this parent.

### WCL-032

- [x] **Reconcile other character-family and antagonist finale states across directories.** **Evidence:** [Nash](../world/characters/nash-maggard.md) · [Angelashi](../world/characters/angelashi.md).

### WCL-033

- [ ] **Review remaining factions/creatures/history subjects for supported classifications and last-state claims.** [WCL-053](#wcl-053), [WCL-054](#wcl-054) and [WCL-070](#wcl-070)–[WCL-073](#wcl-073) are individually complete. **Parent remains open** for [WCL-013](#wcl-013) census-level disposition of outstanding faction, creature and historical subjects; these six scoped checks do not establish exhaustive classifications or final inventories. Keep species, named individuals, institutions and monsters distinct, and add individually tracked children for remaining actionable findings.

### WCL-034

- [x] **Finish canonical-name and stable-alias regression in active world navigation.**

### WCL-035

- [x] **Extend the pilot entity/relationship graph beyond the initial Races v2 entries.**

### WCL-036

- [x] **Distill active review questions from `project/REVIEW_QUEUE.md` and `world/CONSISTENCY_LEDGER.md`.**

### WCL-037

- [ ] **Triage and perform original-audio/handout checks for high-impact open issue keys.** Record actual listened windows, source identities and findings for [WCL-083](#wcl-083)–[WCL-092](#wcl-092); two ASR exports or rendered Markdown **do not** prove audio fidelity. [WCL-093](#wcl-093) is **completed as a source-boundary editorial pass**, not as original-audio verification. Keep this parent open until the outstanding source reviews actually pass.

### WCL-038

- [ ] **Complete maintained-document link/fragment verification beyond preview caps.** For example, Nash's profile has over 200 local links and the chronology over 300; the renderer checks at most 100 destinations per file. Verify remaining links and legacy anchors separately rather than recording “all valid.” **Identified subtasks:** [WCL-101](#wcl-101) · [WCL-102](#wcl-102) · [WCL-103](#wcl-103).

### WCL-039

- [x] **Complete D-048 reader-first checks on remaining top-level world and narrative indexes.**

### WCL-040

- [x] **Finish campaign-wide chronology, current-status and source-boundary acceptance sweep.** **Evidence:** [Elhandar's fall/exodus](../world/HISTORICAL_EVENTS.md#fall-of-elhandar--e125e128) · [Worldbreaker's Earth-only banishment](../world/HISTORICAL_EVENTS.md#worldbreakers-arrival-and-earth-only-banishment--e128-to-s3e17).

### WCL-041

- [ ] **Complete final whole-scope validation and disposition accounting.** Ensure every Wastes-maintained file has a documented accepted/pending/retained-exception status, active links checked, unresolved limitations listed, and private-distribution scope kept distinct from optional public deployment. **Identified subtasks:** [WCL-115](#wcl-115) · [WCL-116](#wcl-116).

## Workflow governance

### WCL-042

- [x] **Replace triple batch reporting with this indexed, checkboxed task register.**

### WCL-043

- [x] **Consolidate redundant intermediate cleanup snapshots without losing protected originals.** **Evidence:** [retention index](REPORT_SNAPSHOT_RETENTION_INDEX.json) · [campaign plan](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-044

- [x] **Inventory Nash's headings and incoming fragment targets.** **Parent:** [WCL-029](#wcl-029). **Evidence:** [Active biography](../world/characters/nash-maggard.md).

### WCL-045

- [x] **Separate Nash's historical cutoffs from campaign-end status.** **Parent:** [WCL-029](#wcl-029). **Evidence:** [Nash biography](../world/characters/nash-maggard.md) · [heart history](../world/technology/nash-dragon-heart.md).

### WCL-046

- [x] **Decide Nash biography's reader-first treatment.** **Parent:** [WCL-029](#wcl-029). **Evidence:** [biography](../world/characters/nash-maggard.md).

### WCL-047

- [x] **Audit Hope Akmenos's biography.** **Parent:** [WCL-031](#wcl-031). **Evidence:** [unchanged biography](../world/characters/hope-akmenos.md) · [S3E18 dossier](../episodes/S3E18.md).

### WCL-048

- [x] **Audit Vorel's biography.** **Parent:** [WCL-031](#wcl-031). **Evidence:** [unchanged 243-line biography](../world/characters/vorel.md) · [Title register](../world/characters/vorel-titles.md).

### WCL-049

- [x] **Audit Stanley Billings's biography.** **Parent:** [WCL-031](#wcl-031). **Evidence:** [Unchanged biography](../world/characters/stanley-billings.md) · [S2E02](../episodes/S2E02.md).

### WCL-050

- [x] **Complete Vorel's S3E019 title-recitation comparison and reconcile final-title source timing.** **Parent:** [WCL-031](#wcl-031). **Evidence:** [Titles register](../world/characters/vorel-titles.md) · [Vorel biography](../world/characters/vorel.md).

### WCL-051

- [x] **Extend Nash's spell-phrase register past the E111 candidate-backfill ceiling.** **Parent:** [WCL-031](#wcl-031). **Evidence:** [Register](../world/characters/nash-spellcasting-phrases.md) · [JSON source/candidate evidence inventory](../reports/NASH_PHRASE_BACKFILL_E112_E128_2026-10-31.json).

### WCL-052

- [x] **Determine Badass T's needed character coverage.** **Parent:** [WCL-031](#wcl-031). **Evidence:** [Tedna profile](../world/characters/tedna.md) · [E106](../episodes/E106.md).

### WCL-053

- [x] **Audit the distinct T'ietkalla historical study.** **Parent:** [WCL-033](#wcl-033). **Evidence:** [Historical study](../world/HISTORY_TIETKALLA.md) · [place profile](../world/places/tietkalla.md).

### WCL-054

- [x] **Audit the CHIDS crisis history and reference presentation.** **Parent:** [WCL-033](#wcl-033). **Evidence:** [History](../world/HISTORY_CHIDS_DRIVE.md) · [CHIDS site record](../world/places/chids.md).

### WCL-055

- [x] **Assess Lactids as a people/culture subject.** **Parent:** [WCL-012](#wcl-012). **Evidence:** [Races](../world/RACES.md) · [E013](../episodes/E013.md).

### WCL-056

- [x] **Assess Harlequinari as a people/culture subject.** **Parent:** [WCL-012](#wcl-012). **Evidence:** [E113](../episodes/E113.md) · [E088](../episodes/E088.md).

### WCL-057

- [x] **Assess elves as a people/culture subject.** **Parent:** [WCL-012](#wcl-012). **Evidence:** [Elves](../world/races/elves.md) · [Elhandar](../world/places/elhandar.md).

### WCL-058

- [x] **Assess dwarves as a people/culture subject.** **Parent:** [WCL-012](#wcl-012). **Evidence:** [Dwarves profile](../world/races/dwarves.md) · [E003](../episodes/E003.md).

### WCL-059

- [x] **Assess orcs and Kuromokishi culture coverage.** **Parent:** [WCL-012](#wcl-012). **Evidence:** [Razak Val](../world/places/razak-val.md) · [E010](../episodes/E010.md).

### WCL-060

- [x] **Assess illithids as a people/culture subject.** **Parent:** [WCL-012](#wcl-012). **Evidence:** [Charles Dickens](../world/characters/charles-dickens.md) · [E066](../episodes/E066.md).

### WCL-061

- [x] **Assess pixies as a people/culture subject.** **Parent:** [WCL-012](#wcl-012). **Evidence:** [Pixie Hulks](../world/creatures/pixie-hulks.md) · [E031](../episodes/E031.md).

### WCL-062

- [x] **Reconcile the historic 134/134 world-file first-pass census.** **Parent:** [WCL-013](#wcl-013). **Evidence:** [2026-10-27 134-path worklist](WASTES_CLEANUP_WORLD_WORKLIST_2026-10-27.json) · [Batch 40 final 308-line structural audit](../reports/WASTES_CLEANUP_PHASE0_VOREL_TITLES_GROUP_40_2026-10-27.md).

### WCL-063

- [x] **Reconcile the complete current world-file census and bounded incoming-link dispositions.** **Parent:** [WCL-013](#wcl-013). Confirmed **152/152 live world files and hashes**, 133 original paths retained plus 19 additions; all **151 Markdown pages** have individual six-domain inbound-link counts (**2,248 matching link instances**), and `world/entities.json` has a separate non-Markdown exception. All files have source-limited structural and D-048 presentation dispositions. Safety-restricted source files, historical archives, actual browser link clicks, original audio, full factual accuracy, technical JSON consumers and remaining editorial candidates are **not** falsely accepted; they remain separate tasks. **Evidence:** [world census](WASTES_WORLD_FILE_CENSUS.json) · [parent WCL-013](#wcl-013).

### WCL-064

- [x] **Review Planet Nash place coverage.** **Parent:** [WCL-017](#wcl-017). **Result:** one new, nonduplicated place. **Evidence:** [Planet Nash reader history](../world/places/planet-nash.md) · [places directory](../world/PLACES.md).

### WCL-065

- [x] **Review Pentel Weiss place/prison coverage.** **Parent:** [WCL-017](#wcl-017). **Result:** nonduplicated place and final prison-status boundaries. **Evidence:** [new prison history](../world/places/pentel-weiss.md) · [places index](../world/PLACES.md).

### WCL-066

- [x] **Review Mars settlements and terraforming-platform references.** **Parent:** [WCL-017](#wcl-017). **Result:** distinct Mars sublocations and time-bounded refugee presence. **Evidence:** [Mars regional place history](../world/places/mars-terraforming-colony.md) · [places index](../world/PLACES.md).

### WCL-067

- [x] **Solar Mines facility guide** **Parent:** [WCL-017](#wcl-017). **Evidence:** [11 evidence-tiered groups](../world/places/solar-mines.md#distinct-facilities-and-source-confidence) · [PLACES](../world/PLACES.md).

### WCL-068

- [x] **Build Known Wastes v3 map-label crosswalk.** **Parent:** [WCL-018](#wcl-018). **Result:** verified original private JPEG by size/SHA; recorded inscribed/owner-confirmed canonical labels, edition/provenance, regional inclusion, legacy aliases and unknown boundaries/rights, without invented coordinates or new map reproduction. **Evidence:** [cartographic crosswalk](WASTES_CARTOGRAPHIC_CROSSWALK.md) · [map review](../reports/WASTES_KNOWN_MAP_ORTHOGRAPHY_2026-10-27.md).

### WCL-069

- [x] **Distinguish Principal City from the Principal's Lands.** **Parent:** [WCL-018](#wcl-018). **Result:** the Lands is directly map-labelled territory; city name follows owner-approved D-044 but is not verified printed on v3. E026/E106 claims, S3E13 aerial rifts and S3E019 *unused* city/spire/rail plans are separated, without claiming an urban visit or measured boundaries. **Evidence:** [city-versus-territory crosswalk](WASTES_CARTOGRAPHIC_CROSSWALK.md#principal-city-is-not-the-mapped-territory).

## Identified subtasks — Factions and world-resolution events

### WCL-070

- [x] **Audit the Council of Earthly Defenders as a wartime coalition.** **Parent:** [WCL-033](#wcl-033). **Result:** added distinct faction index entry and source notes: S2E03 and S3E04 actual Mars councils, S3E05 deployed allies, no permanent unified government or automatic S3E18 continuity. **Evidence:** [faction directory](../world/FACTIONS_AND_POWERS.md#institutions-and-competing-powers).

### WCL-071

- [x] **Audit the lunar Council of Faces.** **Parent:** [WCL-033](#wcl-033). **Result:** clarified physically forced Nash successor and destroyed lunar facility versus unverified ancient-human identity, mandate, backup copies and association with other councils. **Evidence:** [factions](../world/FACTIONS_AND_POWERS.md) · [S3E18](../episodes/S3E18.md).

### WCL-072

- [x] **Audit the Umbilical Order as military faction and separate Clench facility.** **Parent:** [WCL-033](#wcl-033). **Result:** confirmed S3E06 Paladin confrontation and distinct Kuromokishi fighters; the S3E18 Clench-clearance mission remains an **unperformed commission**. **Evidence:** [factions](../world/FACTIONS_AND_POWERS.md) · [Solar Mines](../world/places/solar-mines.md).

### WCL-073

- [x] **Assess Arcanum Universalis as an institution.** **Parent:** [WCL-033](#wcl-033). **Result:** new [faction entry](../world/FACTIONS_AND_POWERS.md#institutions-and-competing-powers) separates Buttons's E028 scholarly/alteration claims, the E039 reported-mage accusation, proposed E059 exchanges, and the map's fictional affiliation from **unused S3E019 speculation** that a flying citadel might have survived. No visited academy, independently verified autonomy or proven postwar citadel. Source-limited to processed dossiers; original audio unverified.

### WCL-074

- [x] **Document the fall of Elhandar as historical event.** **Parent:** [WCL-040](#wcl-040). **Result:** source-bounded historical-event acceptance. **Evidence:** [historical account](../world/HISTORICAL_EVENTS.md#fall-of-elhandar--e125e128) · [Elhandar](../world/places/elhandar.md).

### WCL-075

- [x] **Reconcile Worldbreaker's entry and Earth-only permanent banishment.** **Parent:** [WCL-040](#wcl-040). **Evidence:** [historical-event account](../world/HISTORICAL_EVENTS.md#worldbreakers-arrival-and-earth-only-banishment--e128-to-s3e17) · [antagonist index](../world/ANTAGONISTS.md).

### WCL-076

- [x] **Reconcile S3E18 Earth's restoration and magic changes.** **Parent:** [WCL-040](#wcl-040). **Result:** shared WCL-075 historical cohort. **Evidence:** [restoration and spellcasting account](../world/HISTORICAL_EVENTS.md#earths-restoration-and-spellcasting-boundary--s3e18) · [Ruby device study](../world/technology/rubistic-triangulosphere.md).

### WCL-077

- [x] **Preserve uncertainty around the apparent second Nash.** **Parent:** [WCL-032](#wcl-032). **Result:** finale identity boundary. **Evidence:** [Nash](../world/characters/nash-maggard.md) · [Angelashi](../world/characters/angelashi.md).

### WCL-078

- [x] **Reconcile recording order, fictional chronology and time of knowledge.** **Parent:** [WCL-040](#wcl-040). **Result:** recording/event/knowledge separation. **Evidence:** [three-clock chronology contract](../world/CHRONOLOGY.md#three-clocks--archive-order-fictional-time-and-character-knowledge) · [CHRONOLOGY.md](../world/CHRONOLOGY.md).

### WCL-079

- [x] **Review the Rubistic Triangulosphere's last placement and activation.** **Parent:** [WCL-021](#wcl-021). **Result:** physical staging versus actually performed planetary effect. **Evidence:** [current Ruby custody and activation account](../world/technology/rubistic-triangulosphere.md#last-evidenced-location-controller-and-postwar-custody) · [Ruby's source-first dossier](../world/technology/rubistic-triangulosphere.md).

### WCL-080

- [x] **Reconcile Hand of the Voice versus the separate Fist.** **Parent:** [WCL-021](#wcl-021). **Result:** source-bounded custody, not inferred merging. **Evidence:** [two-relic custody table](../world/technology/hand-of-the-voice.md#two-physical-relics--custody-at-a-glance) · [artifact index](../world/ITEMS_AND_ARTIFACTS.md).

### WCL-081

- [x] **Inventory genuinely unresolved finale object custody.** **Parent:** [WCL-021](#wcl-021). **Result:** selected final inventory, not all-item certification. **Evidence:** [finale item-custody audit](../world/ITEMS_AND_ARTIFACTS.md#finale-custody-audit--witnessed-use-versus-unknown-inventory) · [item directory](../world/ITEMS_AND_ARTIFACTS.md).

### WCL-082

- [x] **Review E039 mind-reading potion transfer for Arc 03 relevance.** **Parent:** [WCL-040](#wcl-040). **Result:** no unsupported narrative insertion. **Evidence:** [Arc 03](../narrative/ARC_03.md) · [E024 acquisition](../episodes/E024.md).

### WCL-083

- [ ] **Verify the Principal's S3E14 longer self-spoken title.** Resolve Chrome Ascendantrix/Vladomotrix ASR variation only from original audio, preserving canonical display title. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](../episodes/S3E14.md).

### WCL-084

- [ ] **Resolve Worldbreaker's S3E15–16 conflicting fire rulings.** Review successful S3E15 Fireballs against S3E16 fire immunity before harmonizing any source claims. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](../episodes/S3E16.md).

### WCL-085

- [ ] **Resolve S3E17–18 Wish-recovery day discrepancy.** Check explicit seven-day stress versus four days elapsed and retain possible GM retcon until verified. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](../episodes/S3E18.md).

### WCL-086

- [ ] **Triage E000–E001 prologue and introduction audio windows.** Use existing issue IDs and exact recorded windows for consequential source/identity questions. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](REVIEW_QUEUE.md).

### WCL-087

- [ ] **Triage E022–E024 Soulbroker pact audio windows.** Check physical signatories, Vorel refusal and later contract/soul interpretations at their own source cutoffs. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](REVIEW_QUEUE.md).

### WCL-088

- [ ] **Triage E048–E054 deaths, rescue and coronation windows.** Distinguish false reports, actual rescues, competing claims and T'ietkalla chronology. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](REVIEW_QUEUE.md).

### WCL-089

- [ ] **Triage E066/E079–E081 CHIDS source windows.** Verify high-impact machine, chronology and knowledge-boundary claims from bounded evidence. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](REVIEW_QUEUE.md).

### WCL-090

- [ ] **Triage E101–E116 party-split source windows.** Preserve E101 boundary, private knowledge and simultaneous event distinction. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](REVIEW_QUEUE.md).

### WCL-091

- [ ] **Triage S2E01–S3E03 space-voyage source windows.** Focus on Nash regeneration, Principal paternity story, Hand seizure and shared dream provenance. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](REVIEW_QUEUE.md).

### WCL-092

- [ ] **Triage S3E12–S3E18 finale source windows.** Select consequential infernal, Worldbreaker, Nash resurrection and final warning questions by existing issue IDs. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](REVIEW_QUEUE.md).

### WCL-093

- [x] **Review S3E019 unused ideas versus played canon.** **Parent:** [WCL-037](#wcl-037). **Result:** audited the CHIDS single-sacrifice plan, unused western dungeon/Principal City rail/spire/Lactid stories, speculative Arcanum citadel, future headcanon and unresolved character outcomes against played references. Kept genuine T'ietkalla railway and Solar Mines dome events distinct; no unsupported played scene found in the targeted maintained corpus. **Evidence:** [source-boundary crosswalk](WASTES_CAMPAIGN_CLEANUP_PLAN.md#wcl-093--roundtable-versus-played-canon-2026-11-02) · [roundtable](../episodes/S3E019.md). Original audio not verified.

## Identified subtasks — Evidence maintenance, links and reader acceptance

### WCL-094

- [x] **Distill current actionable issues from REVIEW_QUEUE.md.** **Parent:** [WCL-036](#wcl-036). **Result:** current evidence routing without historical deletion. **Evidence:** [Nash phrase register](../world/characters/nash-spellcasting-phrases.md) · [reference](REVIEW_QUEUE.md).

### WCL-095

- [x] **Distill unresolved claims from CONSISTENCY_LEDGER.md.** **Parent:** [WCL-036](#wcl-036). **Result:** bounded ledger routing rather than wholesale rewriting. **Evidence:** [reference](../world/CONSISTENCY_LEDGER.md) · [entity evidence schema](../world/ENTITY_SCHEMA.md#version-3--provenance-bearing-relationship-and-custody-evidence-wcl-100-2026-11-02).

### WCL-096

- [x] **Audit Principal/Principle display spellings and aliases.** **Parent:** [WCL-034](#wcl-034). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-097

- [x] **Audit Khaervilon/Kervalon and mapped place-name aliases.** **Parent:** [WCL-034](#wcl-034). **Result:** owner-confirmed map orthography and alias reconciliation. **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-098

- [x] **Audit Or'Nath family and villa names.** **Parent:** [WCL-034](#wcl-034). **Result:** owner-confirmed identity and active editorial display. **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md) · [Jon-authored poem and owner clarification](../reports/DISCORD_NEW_SPELLING_2026-10-27.md#wastes-stanleys-original-elven-name--valiir-ornath).

### WCL-099

- [x] **Plan stable-ID index expansion beyond v2 Races pilot.** **Parent:** [WCL-035](#wcl-035). **Result:** inventory and compatibility plan, not data migration. **Evidence:** [reference](../world/ENTITY_SCHEMA.md) · [entities.json](../world/entities.json).

### WCL-100

- [x] **Add only documented relationships and custody edges.** **Parent:** [WCL-035](#wcl-035). **Result:** source-bounded v3 relationship and physical-transfer cohort. **Evidence:** [reference](../world/entities.json) · [P0D](../world/characters/p0d.md).

### WCL-101

- [x] **Validate Nash biography links past the renderer's 100-link cap.** **Parent:** [WCL-038](#wcl-038). **Evidence:** [WCL-030 revised biography](../world/characters/nash-maggard.md).

### WCL-102

- [x] **Validate chronology links past the renderer's 100-link cap.** **Parent:** [WCL-038](#wcl-038). **Evidence:** [source-keyed chronology](../world/CHRONOLOGY.md).

### WCL-103

- [ ] **Test legacy raw-HTML aliases in native reader rendering.** Verify original inbound fragments in actual GitHub/browser output; offline renderer strips aliases. **Parent:** [WCL-038](#wcl-038). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-104

- [ ] **Run deferred desktop interactive reader walkthrough.** Check all eleven private arcs, anchors, intra-page and compatibility navigation in an actual browser. **Parent:** [WCL-007](#wcl-007). **Evidence:** [reference](../narrative/README.md).

### WCL-105

- [ ] **Run deferred narrow/mobile reader walkthrough.** Check real responsive navigation and link behavior rather than inferring it from Markdown lint. **Parent:** [WCL-007](#wcl-007). **Evidence:** [reference](../narrative/README.md).

### WCL-106

- [x] **Audit root README reader-first ordering and campaign separation.** **Parent:** [WCL-039](#wcl-039). **Result:** reader-first root navigation and campaign separation audit. **Evidence:** [Wastes world](../world/README.md) · [Wastes narrative](../narrative/README.md).

### WCL-107

- [x] **Audit Wastes and narrative landing-page structure.** **Parent:** [WCL-039](#wcl-039). **Result:** focused reader navigation/compatibility audit. **Evidence:** [story guide](../narrative/README.md) · [Wastes portal](../wastes/README.md).

### WCL-108

- [x] **Audit world README and WORLD.md opening and final horizon.** **Parent:** [WCL-039](#wcl-039). **Result:** reader-first world landing pages. **Evidence:** [world portal](../world/README.md) · [setting overview](../world/WORLD.md).

### WCL-109

- [x] **Audit character and antagonist index presentations.** **Parent:** [WCL-039](#wcl-039). **Result:** bounded index reconciliation. **Evidence:** [characters](../world/CHARACTERS.md) · [antagonists](../world/ANTAGONISTS.md).

### WCL-110

- [x] **Audit places index reader navigation.** **Parent:** [WCL-039](#wcl-039). **Result:** scoped places-navigation and final-horizon review. **Evidence:** [Places index](../world/PLACES.md) · [played finale](../episodes/S3E18.md).

### WCL-111

- [x] **Audit items/artifacts index reader navigation.** **Parent:** [WCL-039](#wcl-039). **Result:** bounded artifact index audit. **Evidence:** [Items and artifacts](../world/ITEMS_AND_ARTIFACTS.md) · [played finale](../episodes/S3E18.md).

### WCL-112

- [x] **Audit faction/powers index reader navigation.** **Parent:** [WCL-039](#wcl-039). **Result:** reader-first institutional and wartime evidence separation. **Evidence:** [factions index](../world/FACTIONS_AND_POWERS.md) · [finale](../episodes/S3E18.md).

### WCL-113

- [x] **Audit creatures/monsters index taxonomy and ordering.** **Parent:** [WCL-039](#wcl-039). **Result:** creature index taxonomy and reading order. **Evidence:** [creature index](../world/CREATURES_AND_MONSTERS.md) · [scope policy](WORLD_CREATURES_PLAN.md).

### WCL-114

- [x] **Audit historical-events index presentation and exceptions.** **Parent:** [WCL-039](#wcl-039). **Result:** history index reader/navigation review. **Evidence:** [Historical Events](../world/HISTORICAL_EVENTS.md) · [S3E18 finale](../episodes/S3E18.md).

### WCL-115

- [x] **Develop bounded automatic reference/coverage diagnostics.** **Parent:** [WCL-041](#wcl-041). **Result:** bounded reference/coverage tooling. **Evidence:** [read-only checker](../tools/wastes_reference_diagnostics.py) · [seven synthetic tests](../tests/test_wastes_reference_diagnostics.py).

### WCL-116

- [x] **Create full-file acceptance/disposition matrix.** **Parent:** [WCL-041](#wcl-041). **Result:** accounting, not content certification. **Evidence:** [329-path full-file acceptance/disposition matrix](WASTES_FULL_FILE_ACCEPTANCE_MATRIX.md) · [146-path world evidence census](WASTES_WORLD_FILE_CENSUS.json).

### WCL-117

- [x] **Restructure Hope Akmenos's biography into the approved eleven-arc reader-first account.** **Parent:** [WCL-031](#wcl-031). **Evidence:** [Revised biography](../world/characters/hope-akmenos.md).

### WCL-118

- [x] **Restructure Vorel's biography as an eleven-arc reader-first character study.** **Parent:** [WCL-031](#wcl-031). **Evidence:** [Revised biography](../world/characters/vorel.md).

### WCL-119

- [x] **Restructure Stanley Billings's biography as an eleven-arc reader-first character study.** **Parent:** [WCL-031](#wcl-031). **Evidence:** [Revised biography](../world/characters/stanley-billings.md).

### WCL-120

- [x] **Create Badass T's dedicated reader profile and distinct character-index entry.** **Parent:** [WCL-031](#wcl-031). **Evidence:** [New profile](../world/characters/badass-t.md) · [Character index](../world/CHARACTERS.md).

### WCL-121

- [x] **Rewrite T'ietkalla's distinct historical study through the played S3E18 legacy.** **Parent:** [WCL-033](#wcl-033). **Evidence:** [historical study](../world/HISTORY_TIETKALLA.md) · [site profile](../world/places/tietkalla.md).

### WCL-122

- [x] **Rewrite CHIDS and the Traversal Drive crisis as a distinct reader-first historical study.** **Parent:** [WCL-033](#wcl-033). **Evidence:** [CHIDS history](../world/HISTORY_CHIDS_DRIVE.md).

### WCL-123

- [x] **Add a narrowly source-backed Harlequinari people profile and Council of Clowns cross-links.** **Parent:** [WCL-012](#wcl-012). **Evidence:** [world/races/harlequinari.md](../world/races/harlequinari.md) · [Races](../world/RACES.md).

### WCL-124

- [x] **Create a bounded Elves culture article anchored in Elhandari evidence.** **Parent:** [WCL-012](#wcl-012). **Evidence:** [world/races/elves.md](../world/races/elves.md) · [world/RACES.md](../world/RACES.md).

### WCL-125

- [x] **Create a cautious Dwarves people profile from the ancient ruin, Black Mine and Blast Belly Rock evidence.** **Parent:** [WCL-012](#wcl-012). **Evidence:** [world/races/dwarves.md](../world/races/dwarves.md) · [world/RACES.md](../world/RACES.md).

### WCL-126

- [x] **Write and cross-link a source-limited Orcs people reference distinct from the Koromukishi martial order.** **Parent:** [WCL-012](#wcl-012). **Evidence:** [world/races/orcs.md](../world/races/orcs.md) · [world/RACES.md](../world/RACES.md).

### WCL-127

- [x] **Add a source-limited Illithids people profile separating CHIDS invaders, virtual workplace and independent Sigil resident.** **Parent:** [WCL-012](#wcl-012). **Evidence:** [world/races/illithids.md](../world/races/illithids.md) · [world/RACES.md](../world/RACES.md).

### WCL-128

- [x] **Create a bounded Pixies people reference distinguishing exploitation, survivors and alternate-family life.** **Parent:** [WCL-012](#wcl-012). **Evidence:** [world/races/pixies.md](../world/races/pixies.md) · [world/RACES.md](../world/RACES.md).

### WCL-129

- [x] **Establish the live 146-path per-file world-census scaffold without inheriting false acceptance.** **Parent:** [WCL-013](#wcl-013). **Evidence:** [project/WASTES_WORLD_FILE_CENSUS.json](WASTES_WORLD_FILE_CENSUS.json) · [134-path original worklist](WASTES_CLEANUP_WORLD_WORKLIST_2026-10-27.json).

### WCL-130

- [x] **Review all twelve post-2026-10-27 added world paths at the current HEAD and record exact per-file disposition evidence.** **Evidence:** [eight Races people pages](../world/races/) · [world/RACES.md](../world/RACES.md).

### WCL-131

- [x] **Review the first current-baseline root world index cohort for WCL-063.** **Parent:** [WCL-063](#wcl-063). **Evidence:** [world/README.md](../world/README.md) · [ANTAGONISTS](../world/ANTAGONISTS.md).

### WCL-132

- [x] **Review four original-baseline world overviews and indexes for WCL-063.** **Parent:** [WCL-063](#wcl-063). **Evidence:** [PLACES](../world/PLACES.md) · [ITEMS_AND_ARTIFACTS](../world/ITEMS_AND_ARTIFACTS.md).

### WCL-133

- [x] **Reconcile stale active index descriptions discovered by WCL-131.** **Parent:** [WCL-013](#wcl-013). **Result:** four narrow current-index editorial fixes, no archive/rewrite.

### WCL-134

- [x] **Review and extend the historical-events index beyond Season One without misrepresenting its present source horizon.** **Parent:** [WCL-013](#wcl-013). **Result:** compact Season Two/Three historic-events expansion. **Evidence:** [world/HISTORICAL_EVENTS.md](../world/HISTORICAL_EVENTS.md) · [CHRONOLOGY](../world/CHRONOLOGY.md).

### WCL-135

- [x] **Current per-file disposition review of the three original historical world studies for WCL-063.** **Parent:** [WCL-063](#wcl-063). **Evidence:** [Ancient catastrophe](../world/HISTORY_ANCIENT_CATASTROPHE.md) · [T'ietkalla history](../world/HISTORY_TIETKALLA.md).

### WCL-136

- [x] **Review the two technical entity-index root files into the current Wastes census.** **Parent:** [WCL-063](#wcl-063). **Evidence:** [world/ENTITY_SCHEMA.md](../world/ENTITY_SCHEMA.md) · [world/entities.json](../world/entities.json).

### WCL-137

- [x] **Assess a reader-first revision of the ancient-catastrophe study without inventing ancient history or breaking old destinations.** **Parent:** [WCL-013](#wcl-013). **Result:** reader-first Ancient Catastrophe narrative, sources qualified. **Evidence:** [Ancient catastrophe](../world/HISTORY_ANCIENT_CATASTROPHE.md) · [WORLD overview](../world/WORLD.md).

### WCL-138

- [x] **Review the current full-campaign chronological root ledger as its own bounded WCL-063 cohort.** **Evidence:** [world/CHRONOLOGY.md](../world/CHRONOLOGY.md) · [146-path current census](WASTES_WORLD_FILE_CENSUS.json).

### WCL-139

- [x] **Review the 914-line consistency ledger as a separate evidence-register cohort for WCL-063.** **Parent:** [WCL-063](#wcl-063). **Evidence:** [world/CONSISTENCY_LEDGER.md](../world/CONSISTENCY_LEDGER.md) · [the current census](WASTES_WORLD_FILE_CENSUS.json).

### WCL-140

- [x] **Finish chronology target-path, fragment and reader-navigation checks left by the WCL-138 renderer limit.** **Parent:** [WCL-063](#wcl-063). **Evidence:** [world/CHRONOLOGY.md](../world/CHRONOLOGY.md) · [census entry](WASTES_WORLD_FILE_CENSUS.json).

### WCL-141

- [ ] **Verify the consistency ledger's rendered navigation and layout despite the blocked WCL-139 preview.** **Parent:** [WCL-063](#wcl-063); blocked dependency from [WCL-139](#wcl-139). The 914-line/316,386-byte ledger was read and linted, and all **280 distinct files targeted by 509 Markdown links** exist, but `render_workspace_markdown` returned a **safety-blocked result**, not a rendered page or 100-link sample. Use a permitted, appropriately bounded alternate render/checker or a segmented preview only when supported and not merely to bypass a safety restriction. Verify headings/tables and link rendering in a legitimate environment, including any dangerous HTML/asset cases if exposed, without pretending static path existence equals visual acceptance. Record exactly what can be checked; if still blocked, retain the rendered/browser gap and [WCL-103](#wcl-103) rather than asserting success. No entire-ledger rewrite or raw-ASR modification solely to make the renderer accept it.

### WCL-142

- [x] **Reconcile D-044 owner-confirmed T'ietkalla spelling against the ledger's historic D-027-only policy note.** **Parent:** [WCL-013](#wcl-013). **Evidence:** [current place profile](../world/places/tietkalla.md) · [reader-first history](../world/HISTORY_TIETKALLA.md).

### WCL-143

- [x] **Begin the character-domain per-file census with the Nash Maggard and Hope Akmenos profiles.** **Parent:** [WCL-063](#wcl-063). **Evidence:** [Nash](../world/characters/nash-maggard.md) · [Hope](../world/characters/hope-akmenos.md).

### WCL-144

- [x] **Review Stanley Billings and Vorel as individual current character-profile census records.** **Parent:** [WCL-063](#wcl-063). **Evidence:** [Stanley](../world/characters/stanley-billings.md) · [Vorel](../world/characters/vorel.md).

### WCL-145

- [x] **Review four smaller connected character profiles as individually evidenced WCL-063 census files.** **Parent:** [WCL-063](#wcl-063). **Evidence:** [Angelashi](../world/characters/angelashi.md) · [Bok Bok](../world/characters/bok-bok.md).

### WCL-146

- [x] **Review Tedna, P0D, Squirts and Nobieri as four separate WCL-063 census records.** **Parent:** [WCL-063](#wcl-063). **Evidence:** [Tedna](../world/characters/tedna.md) · [P0D](../world/characters/p0d.md).

### WCL-147

- [ ] **Review reader-first presentation of Bok Bok and Emenil and the remaining validation gap.** **Parent:** [WCL-013](#wcl-013); surfaced by [WCL-145](#wcl-145). Both current profiles remain chiefly source-first notes; consider source-backed narrative introductions and an explicit current-status section while preserving historical cutoffs, uncertain names and source links. Also review `world/CHARACTERS.md`'s older Emenil description against the profile's later source horizon. Bok Bok's targeted Markdownlint did not run because the request was blocked by safety checks; leave lint unverified unless a legitimately authorized check becomes available. Do not work around safety blocks or infer original-audio/native-browser acceptance. Any edits require scoped hashes, source review, readback and permitted validation.

### WCL-148

- [x] **Plan source-backed reader-first repairs for Tedna and Nobieri while preserving distinct factual cutoffs.** **Parent:** [WCL-013](#wcl-013). **Result:** two source-bound D-048/D-052 character restructures. **Evidence:** [Badass T](../world/characters/badass-t.md) · [census](WASTES_WORLD_FILE_CENSUS.json).

### WCL-149

- [x] **Review a D-082 adaptive cohort of fifteen connected identity/conflict character profiles.** **Parent:** [WCL-063](#wcl-063). **Evidence:** [census records](WASTES_WORLD_FILE_CENSUS.json).

### WCL-150

- [x] **Finish restricted verification for the two WCL-149 exceptional character files without bypassing tool safety.** **Parent:** [WCL-063](#wcl-063). **Evidence:** [current census](WASTES_WORLD_FILE_CENSUS.json).

### WCL-151

- [x] **Audit the next D-082 adaptive cohort of twelve pending character profiles.** **Parent:** [WCL-063](#wcl-063). **Result:** selected cohort (2026-11-01; completed audit). **Evidence:** [the current census](WASTES_WORLD_FILE_CENSUS.json).

### WCL-152

- [x] **Plan bounded D-048 reader-first conversion of source-led WCL-149 character profiles, without altering contested evidence.** **Parent:** [WCL-013](#wcl-013). **Result:** bounded editorial plan (completed).

### WCL-153

- [x] **Resolve Nothing's restricted Markdownlint validation without bypassing safety.** **Parent:** [WCL-063](#wcl-063). **Evidence:** [the census](WASTES_WORLD_FILE_CENSUS.json).

### WCL-154

- [x] **Plan source-backed D-048 reader-first follow-up for ten WCL-151 character profiles.** **Parent:** [WCL-013](#wcl-013).

### WCL-155

- [x] **Audit the six remaining short character profiles as the next source-limited WCL-063 census cohort.** **Parent:** [WCL-063](#wcl-063).

### WCL-156

- [x] **Audit the two dense character specialist registers as retained source-first exceptions.** **Parent:** [WCL-063](#wcl-063). **Evidence:** [the live census](WASTES_WORLD_FILE_CENSUS.json).

### WCL-157

- [x] **Restructure Diptak, Orp and Omnom Cinderborn as reader-first Razak Val character studies.** **Result:** verification after WCL-154 retry (closed).

### WCL-158

- [x] **Hell/Sigil companion character reader-first cohort.** **Result:** execution and independent validation (complete).

### WCL-159

- [x] **Contested supernatural agents reader-first cohort.** **Result:** execution and scoped validation (complete).

### WCL-160

- [x] **Nothing and Tungsten Wheel reader-first cohort.** **Result:** execution and validation (complete).

### WCL-161

- [x] **Reader-first Buttons and Kefeli, the early T'ietkalla conflict.** **Result:** execution and verification (completed).

### WCL-162

- [x] **Reader-first Elhandar characters Dilo, Lyrielle and Malhya.** **Result:** execution (complete).

### WCL-163

- [x] **Reader-first infernal trio Brett/Asmodeus, the hooded Voice and Steerious Business.** **Result:** execution (completed). **Evidence:** [146-path census](WASTES_WORLD_FILE_CENSUS.json).

### WCL-164

- [x] **Reader-first Union Wheel and Sprout, the S2/S3 companions.** **Result:** execution (completed). **Evidence:** [146-path census](WASTES_WORLD_FILE_CENSUS.json).

### WCL-165

- [x] **Reader-first Cerinthala CHIDS identity, contested history and last observed state.** **Result:** execution (completed).

### WCL-166

- [x] **Audit the next seven pending facility-related creature profiles as a D-082 source-limited census cohort.** **Parent:** [WCL-063](#wcl-063). **Result:** source-limited census completed. **Evidence:** [the current census](WASTES_WORLD_FILE_CENSUS.json).

### WCL-167

- [x] **Audit the next eleven pending wilderness and travel creature profiles as one adaptive D-082 source-limited census cohort.** **Parent:** [WCL-063](#wcl-063). **Result:** source-limited census completed. **Evidence:** [current census](WASTES_WORLD_FILE_CENSUS.json) · [winged-attackers](../reports/WINGED_ATTACKERS_SOURCE_REVIEW_2026-10-25.md).

### WCL-168

- [x] **Audit eight pending cavern, internal-monster and subterranean creature profiles as a D-082 source-limited census cohort.** **Parent:** [WCL-063](#wcl-063). **Evidence:** [world census](WASTES_WORLD_FILE_CENSUS.json) · [gut-inhabitants source review](../reports/GUT_INHABITANTS_AND_SWARM_SOURCE_REVIEW_2026-10-25.md).

### WCL-169

- [x] **Finish the six remaining pending creature profiles in the current world-file census.** **Parent:** [WCL-063](#wcl-063). **Result:** (source-limited).

### WCL-170

- [x] **Audit eight compact, still-pending place profiles as the first D-082 Places census cohort.** **Parent:** [WCL-063](#wcl-063). **Evidence:** [the 146-path census](WASTES_WORLD_FILE_CENSUS.json).

### WCL-171

- [x] **Audit four medium-length, still-pending Places files as the next adaptive D-082 census cohort.** **Parent:** [WCL-063](#wcl-063).

### WCL-172

- [x] **Resolve the three identified WCL-170 place-page defects as a separately checkable D-048 follow-up.** **Evidence:** [S3E13](../episodes/S3E13.md) · [P/Q report](../reports/WASTES_S3E13_ASR_COMPARISON_2026-10-27.md).

### WCL-173

- [x] **Resolve three WCL-171 source-boundary and reader-navigation issues without conflating structural audit with final D-048 editorial acceptance.**

### WCL-174

- [x] **Prepare and implement a source-limited, reader-first chronological restructure of the Château Weir place study as a separate D-048/D-052 editorial task.** **Parent:** [WCL-063](#wcl-063). **Result:** (bounded D-048/D-052). **Evidence:** [manifest](WASTES_CLEANUP_MANIFEST.md).

### WCL-175

- [x] **Audit two pending medium-to-large Places profiles as the next D-082 source-limited cohort.** **Parent:** [WCL-063](#wcl-063).

### WCL-176

- [x] **Audit two remaining medium-size Places profiles as the next source-limited D-082 census cohort.** **Parent:** [WCL-063](#wcl-063). **Result:** source-limited audit completed.

### WCL-177

- [x] **Resolve WCL-175 reader-navigation and chronological-presentation follow-ups separately from the first-pass census.** **Result:** with exact D-052 preservation and scoped validation.

### WCL-178

- [x] **Audit CHIDS and Solar Mines as the next coherent source-limited D-082 Places census cohort.** **Parent:** [WCL-063](#wcl-063).

### WCL-179

- [x] **Resolve WCL-176's Elhandar current-status horizon and T'ietkalla legacy-anchor issues as independently checkable D-048 follow-ups.**

### WCL-180

- [x] **Complete the final still-pending Places first-pass census: Sigil, as its own large D-082 cohort.** **Parent:** [WCL-063](#wcl-063).

### WCL-181

- [x] **Resolve WCL-178 CHIDS and Solar Mines D-048 reader-first editorial structure as independently tracked follow-up work.** **Result:** two source-limited D-048/D-052 reader-first restructures. **Evidence:** [manifest](WASTES_CLEANUP_MANIFEST.md).

### WCL-182

- [x] **Audit six compact, still-pending Technology profiles as the first D-082 Technology census cohort.** **Parent:** [WCL-063](#wcl-063).

### WCL-183

- [x] **Plan and perform a separately preserved D-048/D-052 reader-first reorganization of Sigil's extensive place study.** **Result:** , source-limited D-048/D-052 reader-navigation restructure. **Evidence:** [manifest](WASTES_CLEANUP_MANIFEST.md).

### WCL-184

- [x] **Audit six further compact-to-medium Technology profiles as the next D-082 source-limited census cohort.** **Parent:** [WCL-063](#wcl-063).

### WCL-185

- [x] **Audit four pending medium-size Technology profiles as the next D-082 source-limited census cohort.** **Parent:** [WCL-063](#wcl-063).

### WCL-186

- [x] **Audit two medium-to-large, pending Technology profiles as the next bounded D-082 cohort.** **Parent:** [WCL-063](#wcl-063).

### WCL-187

- [x] **Repair Fate 4's orphaned illustration-provenance footnote identified in WCL-185, without promoting a reconstruction to canon.**

### WCL-188

- [x] **Audit the final two non-Fate Six Technology studies as a bounded D-082 census cohort.** **Parent:** [WCL-063](#wcl-063).

### WCL-189

- [x] **Audit the final large Technology profile Fate Six as a dedicated, adaptive D-082 first-pass review.** **Parent:** [WCL-063](#wcl-063).

### WCL-190

- [x] **Reconcile the remaining nine non-full-render/lint world-census exceptions after 146/146 first-pass coverage.** **Parent:** [WCL-063](#wcl-063). **Result:** reconciliation, not false renderer/lint promotion.

### WCL-191

- [ ] **Validate native-reader navigation for the seven >100-link world profiles, without conflating prior static target existence with clickable rendering.** Child of completed [WCL-190](#wcl-190), coordinated with browser/legacy-anchor [WCL-103](#wcl-103). Exact files: `world/CHRONOLOGY.md`, `world/characters/hope-akmenos.md`, `nash-maggard.md`, `nash-spellcasting-phrases.md`, `stanley-billings.md`, `vorel-titles.md`, and `vorel.md`. All seven have valid independent static-target inventories, including **12 heading-fragment occurrences** whose target IDs were confirmed, but the safe preview rendered only **100 of each file's links** (700/1,825 occurrences; **1,125 not checked in the renderer**). Use **actual supported GitHub/native browser reading and navigation**, once such a capability is legitimately available, to test source-to-target clicks, heading fragments, legacy alias behavior, `<details>` handling and representative links past position 100 for each file. Do not rehash all existing static file paths as a substitute. Document exact tested paths/links and failures in the task register, update census levels only on legitimately complete checks, and keep full audio/factual/editorial acceptance separate. Native-browser tooling is **not currently available to the workspace MCP flow**; leave unchecked rather than claiming success.

### WCL-192

- [ ] **Resolve the safety-blocked Consistency Ledger rendered-preview gap only through an authorized capability or policy clarification.** Child of [WCL-190](#wcl-190). `world/CONSISTENCY_LEDGER.md`, latest verified **316,680 bytes**, SHA-256 `077c1f78fb84b223061fa132e54043a2751a3f460ac01b4289fc5d240a049677`; historical ledger audit already checked the **509 Markdown link instances to 280 existing local target files** and scoped Markdownlint. The preview renderer request was **safety-blocked**, so rendered headings, in-page fragments, footnote appearance and native reader usability remain unverified. **Do not bypass or repeatedly retry the safety restriction.** If the workspace provider later provides an expressly authorized renderer capability, clarify limits and perform its intended safe operation; otherwise leave `structural_paths_verified_render_blocked` unchanged, retain recorded evidence and request guidance through the normal server maintenance channel. A mere target-file-existence check is not renderer acceptance.

### WCL-193

- [ ] **Complete Bok Bok's safety-blocked Markdownlint check only when legitimately permitted, with separate D-048 editorial questions retained.** Child of [WCL-190](#wcl-190). `world/characters/bok-bok.md`, last verified **11,658 bytes**, SHA-256 `ce4ebffa24f9b0d38895edecdbd665c9e199cf2e7e5f9a46f23367a96891364e`; previously read through EOF and **35/35 local links rendered valid**. Its targeted Markdownlint request was **safety-blocked**, and a subsequent read was also restricted; **do not circumvent restrictions or claim lint success**. Wait for explicit authorized capability/policy resolution, then perform scoped lint if allowed, record output and current SHA in the census. Independent reader-first Bok Bok opening/review issues and ASR ambiguities do not disappear if lint eventually passes; plan any major rewrite with D-052 preservation separately. Do not commit/push/publish.

### WCL-194

- [x] **Repair one broken historical Vorel-title-audit report heading link without changing its evidence.** **Result:** minimal report-link repair completed. **Evidence:** [Vorel's maintained titles register](../world/characters/vorel-titles.md).

### WCL-195

- [x] **Align maintained subject-page filenames and titles with canonical or owner-agreed provisional names.** **Parent:** [WCL-034](#wcl-034). **Result:** Bounded navigation/link scope completed. **Evidence:** [Soulbroker](../world/characters/the-soulbroker.md) · [file-disposition matrix](WASTES_FULL_FILE_ACCEPTANCE_MATRIX.md).

### WCL-196

- [x] **Add campaign-backed origin histories to the Wastes peoples and cultures profiles.** **Parent:** [WCL-012](#wcl-012). **Result:** at its source-limited acceptance scope (D-084). **Evidence:** [Wastes people profiles](../world/RACES.md) · [E078](../episodes/E078.md).

### WCL-197

- [x] **After canonical page renaming, audit every link to the renamed subjects and remove redundant legacy-name placeholder pages.** **Parent:** [WCL-034](#wcl-034). **Result:** verified post-deletion census reconciliation. **Evidence:** [Stanley](../world/characters/stanley-billings.md) · [Diontalus](../world/characters/diontalus.md).

### WCL-198

- [x] **Restore or transparently qualify missing original-source links in maintained episode dossiers.** **Result:** at the eight-dossier reader-link scope. **Evidence:** [image provenance register](IMAGE_ASSETS.md).

### WCL-199

- [x] **Reconcile the historical image-provenance register's unavailable artifact links without altering its evidence.**

### WCL-200

- [x] **Implement the first evidence-backed additive expansion of the stable entity index.** **Parent:** [WCL-035](#wcl-035). **Result:** additive six-people, one-alias implementation. **Evidence:** [people profiles](../world/RACES.md) · [Dwarves](../world/races/dwarves.md).

### WCL-201

- [x] **Black Mine reader-first rewrite.** **Parent:** [WCL-017](#wcl-017). **Result:** rewrote [Black Mine](../world/places/black-mine.md) around E018–E026 arrival, forced labor, shaft failure, Tylander ritual, Soulbroker passage, dragon-flight escape and actual E026 prisoner rescue. Distinguished witnessed violence from rival deed/ownership claims, retained all three legacy headings and separated Leopold; **25/25 links and lint passed**. **Evidence:** [census](WASTES_WORLD_FILE_CENSUS.json) · [LF-normalized pre-edit text](../research/legacy/black-mine-pre-wcl201-2026-11-02.md). Original audio and deed unverified.

### WCL-202

- [x] **Dunebreaker E107–E109 historical-prequel rewrite.** **Parent:** [WCL-017](#wcl-017). **Result:** restructured the [landship history](../world/places/dunebreaker.md) with observed geography and leadership first, then E107 unsolved engineer murder, E108 hidden-daughter confession/Lamulkin's vent sentence, and E109 unresolved investigation, secret trade and defeated gelatin ooze. Confirmed **same Wastes, long before Dusthill**, no main-party crossover; all seven historic anchors, 11/11 links and lint passed. **Evidence:** [census](WASTES_WORLD_FILE_CENSUS.json) · [original text](../research/legacy/dunebreaker-pre-wcl202-2026-11-02.md). Original audio unverified.

### WCL-203

- [x] **Dusthill chronological place rewrite.** **Parent:** [WCL-017](#wcl-017). **Result:** [place history](../world/places/dusthill.md) now distinguishes E003 intake repair, E005 machinery/raid, E006 confirmed surface water and E059 actual **partial** captive return to T'ietkalla. Moag Ferhain map/site identity remains uncertain; owner-selected artwork provenance preserved **without re-embedding**. All four historic anchors and the footnote retained; 26/26 links and lint pass. **Evidence:** [census](WASTES_WORLD_FILE_CENSUS.json) · [pre-edit text](../research/legacy/dusthill-pre-wcl203-2026-11-02.md).

### WCL-204

- [x] **Gray Waste–Styx–Pandemonium reader-first route rewrite.** **Parent:** [WCL-017](#wcl-017). **Result:** [route history](../world/places/gray-waste-and-pandemonium.md) now separates witnessed E112 Gray Waste portal, E113 Pointless/Styx crossing and Council audience from Hesterbrook's past, serpent lore and Council prison testimony. Four actual ferry fares, untested E113 compass gift, unrecovered Eye and actual Sigil return retained. All four historic anchors, **9/9 links** and lint passed. **Evidence:** [census](WASTES_WORLD_FILE_CENSUS.json) · [pre-edit original](../research/legacy/gray-waste-pandemonium-pre-wcl204-2026-11-02.md).

### WCL-205

- [x] **Kaiser Casino reader-first rewrite.** **Parent:** [WCL-017](#wcl-017). **Result:** [place history](../world/places/kaiser-casino.md) now covers named E101–E102, E106 and E116 visits, while treating S3E12–S3E13 as an **unnamed VIP complex** of unproved identity. Kept first *Dispel Magic* revealing entrails/bats/insects, second leaving replacement meal unchanged, Brett’s disguise and Nash’s witnessed heart exchange; no fabricated pact, genuine Tarrasque meat or room 53C visit. **18/18 links**, lint and original heading anchor pass. **Evidence:** [census](WASTES_WORLD_FILE_CENSUS.json) · [original text](../research/legacy/kaiser-casino-pre-wcl205-2026-11-02.md).

### WCL-206

- [x] **Leaden Fingers/Stormlands reader-first rewrite.** **Parent:** [WCL-017](#wcl-017). [Place history](../world/places/leaden-fingers-stormlands.md) separates S3E14 scouting, S3E15 prepared canyon, S3E16 actual detonation and casualties, and later outcome; *Corvutican* remains provisional. **13/13 links**, four footnotes and lint passed. **Evidence:** [census](WASTES_WORLD_FILE_CENSUS.json) · [preserved original](../research/legacy/leaden-fingers-stormlands-pre-wcl206-2026-11-02.md).

### WCL-207

- [x] **Leopold facility reader-first profile.** **Parent:** [WCL-017](#wcl-017). [Facility history](../world/places/leopold-facility.md) distinguishes witnessed E008–E009 events from Leopold/tree testimony and retrospective unclaimed staff, without merging ancient sites. **15/15 links**, four footnotes and lint passed. **Evidence:** [census](WASTES_WORLD_FILE_CENSUS.json) · [preserved original](../research/legacy/leopold-facility-pre-wcl207-2026-11-02.md).

### WCL-208

- [x] **Slavetown reader-first chronological rewrite.** **Parent:** [WCL-017](#wcl-017). [Place history](../world/places/slavetown.md) separates observed slavery, fire and E059 partial survivor return from unproven sandstorm outcome, Principal self-exoneration and proposed labor/rail reform. **23/23 links**, seven footnotes and lint passed. **Evidence:** [census](WASTES_WORLD_FILE_CENSUS.json) · [preserved original](../research/legacy/slavetown-pre-wcl208-2026-11-02.md).

---

**Record-ownership rule:** This file is the only checklist and next-action pointer. [Manifest](WASTES_CLEANUP_MANIFEST.md) records *file dispositions and migrations*, not task statuses. [Changelog](WASTES_CLEANUP_CHANGELOG.md) records only meaningful dated decisions and milestones, with references to IDs here, not duplicate task detail. [Progress](WASTES_CLEANUP_PROGRESS.md) is a compatibility pointer, not a journal. [Decisions](DECISIONS.md) governs approvals; [review queue](REVIEW_QUEUE.md) and [consistency ledger](../world/CONSISTENCY_LEDGER.md) govern evidence issues. Historical B1–B289 execution detail remains in the three preserved pre-migration records.
