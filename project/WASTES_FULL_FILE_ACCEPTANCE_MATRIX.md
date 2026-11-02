# The Wastes — full-file acceptance and disposition matrix

**Scope:** Private repository, 2026-11-01; clean `main` HEAD `d5df08f22bd2c9c3a4570038043cf4f3f940af25` at inventory. **Owning task:** [WCL-116](WASTES_CLEANUP_TASKS.md#wcl-116), child of [WCL-041](WASTES_CLEANUP_TASKS.md#wcl-041).

This is **per-file disposition accounting, not a new fact-review pass**. `A` accepts only a named *structural/routing deliverable* of the private edition. `P` is pending comprehensive editorial/source/technical acceptance, even where structure and links were audited. `E` retains a deliberate functional/compatibility exception; it does **not** mean evidence is verified. No category implies original-audio review, native browser success or a public website.

| Code | Disposition and precise limit |
| --- | --- |
| A-N | Accepted **numbered arc placement/route only**; not complete narrative fidelity |
| P-S | Pending full source/editorial acceptance, notwithstanding world structural/link audit |
| P-R | Pending reader-first presentation work expressly noted in world census |
| P-T | Pending source-first/compatibility exception **candidate**; no final acceptance |
| P-B | Pending blocked renderer/lint verification; do not bypass prior safety restrictions |
| P-N | Pending complete reader-portal acceptance (existing navigation is not full acceptance) |
| E-J | Retained machine-readable JSON technical record, not an ordinary prose article |
| E-L | Retained byte-protected historical word-form arc and its compatibility path |
| E-C | Retained historical season navigation compatibility entry |
| E-D | Retained **source-facing episode dossier**, not a D-048 reader-world article |

## Scope and counts

| Scope | Files | Inventory basis |
| --- | ---: | --- |
| Current `world/` reference paths | 150 | [150-file live census](WASTES_WORLD_FILE_CENSUS.json) |
| `narrative/` current, historic and index routes | 20 | Current directory listing |
| `README.md` and `wastes/README.md` | 2 | Maintained story portals |
| Wastes `episodes/` dossiers | 161 | `E000`–`E128`, `E013.5`, `S2E01`–`S2E12`, `S3E01`–`S3E18`, and nonplayed `S3E019` |
| **Total distinct maintained paths** | **333** | Enumerated below |

**Disposition totals:** 11 bounded `A` / 152 `P` / 170 `E`. The world census records **140 fully structural/renderer-checked Markdown**, **7 renderer-capped**, **1 renderer-blocked**, **1 lint-blocked**, **1 technical JSON**. These categories are verification coverage, not content acceptance.

**Out of scope:** Cross-campaign Delvers/Inverse pages; `episodes/STAR-TREK-S1E001.md`; generic `BONUS-*` episodes pending individual Wastes-source relevance classification; generated/transcript `sources/`, `local/`, maintenance scripts, protected original archives, research reports, source/illustration binaries, and project-control records. Relevant bonus evidence may still be cited by in-scope pages. Wastes-related one-off/prequel episode dossiers are included. This is an *editorial Wastes reading/reference* inventory, not an exhaustive repository file census.

## World/reference paths (150)

Four WCL-195 canonical/provisional primary additions currently coexist with temporary old-path compatibility copies: the Principal, Khaervilon, the Soulbroker and Grape's magical guitar. These legacy routes retain their full source text and are slated for WCL-197 post-rename review, with any redundant aliases removed only after full backlink audit.

This table **reuses**, rather than silently upgrades, [the detailed world census](WASTES_WORLD_FILE_CENSUS.json). Its individual records retain hashes, episode cutoffs, all open questions, source qualifications, examples of incoming links, footnote counts and link-validation details. `Renderer` means the offline preview's local-link scan (maximum **100 per page**); static file/fragment checks are separate from clickable native GitHub validation. The following source-window summaries are **not** proof that all cited material was independently checked.

| Maintained file | Status | Existing structural proof or specific gap | Depicted source window (as recorded) |
| --- | --- | --- | --- |
| `world/ANTAGONISTS.md` | P-S | Renderer 44 links; scoped lint recorded | E029 and earlier antagonists; final played S3E18 including lunar Council of Faces; S3E019 cast commentary distinct |
| `world/CHARACTERS.md` | P-S | Renderer 100 links; scoped lint recorded | E000–S3E18 played; S3E019 Q&A identified as retrospective; E107–E109 prequel distinct |
| `world/CHRONOLOGY.md` | P-T | Renderer 100/316 local links; static targets checked | E000–E128 main Season One, S2E01–S2E12 and S3E01–S3E18 played; 11-arc reader edition. E107–E109 is an earlier in-world prequel; E013.5 a misplaced supplemental scene; E043 and E127 non-main one-offs; S3E019 cast Q&A is nonplayed. |
| `world/CONSISTENCY_LEDGER.md` | P-B | Renderer safety-blocked; static target existence only | Episode/cutoff assessments across E000–E128, S2E01–S2E12 and S3E01–S3E18; E107–E109 prequel and multiple retrospective cast Q&As separately labeled. Later chapters add ASR-based evidence, not independent original audio. |
| `world/CREATURES_AND_MONSTERS.md` | P-S | Renderer 50 links; scoped lint recorded | Mostly E000–E128-era creature research; added S3E03 mind fluff and S3E05 Slow Peters |
| `world/ENTITY_SCHEMA.md` | P-T | Renderer 7 links; scoped lint recorded | v1 E000/E001 pilot and v2 2026-10-31 cited-episode race_culture addition; editorial contract, not an episode narrative |
| `world/FACTIONS_AND_POWERS.md` | P-S | Renderer 71 links; scoped lint recorded | E010–S3E15 selective historical faction snapshots, then S3E16 canyon detonations and Principal's betrayal, S3E17 Worldbreaker permanent banishment and collapse of chrome copies, S3E18 Elhandari/Ruby Earth restoration, Monsoon's voluntary daylight death, Moon Council of Faces destruction and postwar redistribution deliberations |
| `world/HISTORICAL_EVENTS.md` | P-S | Renderer 80 links; scoped lint recorded | Ancient retrospective and competing testimony, E000–E128 played Season One including prequel E107–E109 set long before E001; selected S2E01–S3E18 events with episode-bound source qualifiers, not complete per-episode timeline |
| `world/HISTORY_ANCIENT_CATASTROPHE.md` | P-S | Renderer 32 links; scoped lint recorded | E000 ancient GM prologue (undated), physically encountered ruins and CHIDS E073/E077/E079, attributed E067/E078/E081 testimony, Delit E118 journal and black dragon E122 warning; S3E17–S3E18 later Earth renewal as lasting legacy, not evidence for ancient chronology |
| `world/HISTORY_CHIDS_DRIVE.md` | P-S | Renderer 31 links; scoped lint recorded | E067–E082 investigation, Drive activation and immediate Sigil aftermath; S3E18 Earth restoration mentioned only as later contextual consequence |
| `world/HISTORY_TIETKALLA.md` | P-S | Renderer 32 links; scoped lint recorded | Material ancient city history E047–E051; E031–E059 rulership; E103–E118 invasion/Harbor; S3E18 played Earth restoration, Hope returns |
| `world/ITEMS_AND_ARTIFACTS.md` | P-S | Renderer 100 links; scoped lint recorded | Selected object and custody studies E050–S3E15, with explicitly limited S3E16–S3E18 finale-status updates including Monsoon's helmet |
| `world/PLACES.md` | P-S | Renderer 100 links; scoped lint recorded | Selected histories from E003 through S3E15; specific S3E18 finales for Razak Val, Fate Six, Solar Mines, Planet Nash and T'ietkalla; E107–E109 historical prequel treated separately |
| `world/RACES.md` | P-S | Renderer 33 links; scoped lint recorded | Wastes range; E013–S3E18 played evidence, S3E019 retrospective |
| `world/README.md` | P-S | Renderer 86 links; scoped lint recorded | E000–S3E18 main campaign; E107–E109 prequel; S3E019 Q&A separate |
| `world/WORLD.md` | P-S | Renderer 60 links; scoped lint recorded | Foundational E000 to E124 research, with selected E122 and played S3E17–S3E18 Earth-restoration and resettlement consequences; separately attributed creator retrospectives |
| `world/characters/alvert.md` | P-R | Structural audit recorded; detailed links in census | E071 direct appearance and self-presented underworld-bureau and Principal origin claims |
| `world/characters/angelashi.md` | P-S | Renderer 38 links; scoped lint recorded | E035–E054, E055–E056, E110–E128, S2E02–S2E05, S3E03–S3E05, S3E18; retrospectives separated as evidence |
| `world/characters/badass-t.md` | P-S | Renderer 30 links; scoped lint recorded | First appearance E106; last direct depiction S2E09; later absence through S3E18 |
| `world/characters/blood-skunk-hendrickson.md` | P-S | Structural audit recorded; detailed links in census | E102–E116 and S3E01–S3E02; later E113 Harlequinari self-identification and 2020 nonplayed bonus |
| `world/characters/bok-bok.md` | P-B | Lint safety-blocked; links rendered | E006–E117, E124, S3E05, S3E14–S3E15; no actual post-S3E15 final-personal-fate outcome claimed |
| `world/characters/brett-asmodeus.md` | P-S | Structural audit recorded; detailed links in census | See detailed world census |
| `world/characters/buttons.md` | P-S | Structural audit recorded; detailed links in census | See detailed world census |
| `world/characters/cerinthala.md` | P-S | Structural audit recorded; detailed links in census | See detailed world census |
| `world/characters/charles-dickens.md` | P-R | Structural audit recorded; detailed links in census | E070 virtual illithid office encounter and E071 computer follow-up |
| `world/characters/dick-pendleton.md` | P-R | Structural audit recorded; detailed links in census | S3E09 Solar Mines childhood reminiscence and played Walmart confrontation |
| `world/characters/dilenoria.md` | P-S | Structural audit recorded; detailed links in census | See detailed world census |
| `world/characters/diontalus.md` | P-S | Renderer 58 links; scoped lint recorded | E028–E059, E115–E128, S3E05–S3E08; 2022 Q&A ancient claims retrospectively attributed |
| `world/characters/diptak.md` | P-S | Structural audit recorded; detailed links in census | E028 arrival; E058–E060 Razak Val dispute |
| `world/characters/dr-spider.md` | P-S | Structural audit recorded; detailed links in census | E106–E116; S3E01–S3E02; independent E127 Christmas one-off and creator 2020 bonus |
| `world/characters/emenil.md` | P-R | Renderer 19 links; scoped lint recorded | E055–E059, E103, E115–E117, E123–E124, final observed S3E08 Solar Mines death |
| `world/characters/follow-sira-rorf.md` | P-R | Structural audit recorded; detailed links in census | E063–E066 three-person Razak Val flight and CHIDS abduction; Sira's observed rescue E081; July 2019 retrospective separate |
| `world/characters/general-carthax.md` | P-T | Structural audit recorded; detailed links in census | See detailed world census |
| `world/characters/henitar-grape.md` | P-R | Structural audit recorded; detailed links in census | E125 Elhandar siege, E126 combat, E128 surrender, execution and corpse dialogue |
| `world/characters/hope-akmenos.md` | P-S | Renderer 100/234 local links; static targets checked | E000–E128, S2E01–S2E12, S3E01–S3E18 played; separate cast Q&A and episode-era historical cutoffs |
| `world/characters/imprisoned-black-dragon.md` | P-S | Structural audit recorded; detailed links in census | E121 returned captive dragon, E122 ancient-history testimony and observed death |
| `world/characters/kefeli.md` | P-S | Structural audit recorded; detailed links in census | See detailed world census |
| `world/characters/lyrielle.md` | P-S | Structural audit recorded; detailed links in census | See detailed world census |
| `world/characters/malhya.md` | P-S | Structural audit recorded; detailed links in census | See detailed world census |
| `world/characters/monsoon-cabbage.md` | P-S | Structural audit recorded; detailed links in census | See detailed world census |
| `world/characters/nash-maggard.md` | P-S | Renderer 100/264 local links; static targets checked | E000–E128, S2E01–S2E12, S3E01–S3E18 played; separate cast retrospectives and earlier episode-specific cutoffs |
| `world/characters/nash-spellcasting-phrases.md` | P-T | Renderer 100/275 local links; static targets checked | 48 permanent NSP IDs, 42 S1 through E126 and six later-season findings/seeds; E112–E126/E128 candidate extension; played S3E18 endpoint, separate S3E019 retrospective; source labels point to processed P/Q ASR, not verified performances |
| `world/characters/nobieri.md` | P-S | Renderer 30 links; scoped lint recorded | E047/E048 Nobieri freed from book and unverified ancient Akmenos/Dead Tongue history; actual E054 armed tiefling return/crowning, E111/E115/E117 rescue/Harbor presence, E123–E124 limited sample investigation, S3E04 physical scout council testimony, last direct S3E05 vehicle boarding; no established S3E18 personal status |
| `world/characters/nothing.md` | P-S | Structural audit recorded; detailed links in census | E082–E088 direct kenku guide scenes; 2020 cast Q&As; E089 only research cutoff |
| `world/characters/omnom-cinderborn.md` | P-S | Structural audit recorded; detailed links in census | E062 earlier rocket, E115–E121 testimony and played reconciliation/death; November 2020 nonplayed bonus |
| `world/characters/orp.md` | P-S | Structural audit recorded; detailed links in census | E014 Slavetown; E059–E063 Razak Val Great Fang fight and aftermath |
| `world/characters/p0d.md` | P-S | Renderer 13 links; scoped lint recorded | Original played E031–E056 plus Year One Q&A; no later active living return |
| `world/characters/quizquaz.md` | P-S | Structural audit recorded; detailed links in census | E004 Dream Drinker conflict; E022–E023 distinct Soulbroker introduction; E056–E058 proposals; E081 Drive; S3E11 separate later manifested throne-room appearance |
| `world/characters/soulbroker.md` | P-T | Temporary legacy route with full preserved article; renderer 25/25 links valid | E022–E024 original three signatories, E048/E054 claims, E081 proposal, E122–E128 revived claims, S2E01 exorcism, S3E11–S3E12 death, later S3E17–S3E18 context |
| `world/characters/the-soulbroker.md` | P-S | Canonical title-aligned primary, originally a byte-exact copy; 7 renderer-escaped raw HTML alias tags removed, preserved in legacy copy; 24/24 links and lint passed | E022–S3E18 with S3E12 death and later planetary aftermath distinct; disputed personal-name spellings remain unresolved |
| `world/characters/sprout.md` | P-S | Structural audit recorded; detailed links in census | See detailed world census |
| `world/characters/squirts.md` | P-S | Renderer 49 links; scoped lint recorded | E082–E115, separate Hell reappearance E125, S3E01–S3E02 second death and postdeath graft; campaign ending does not show third revival |
| `world/characters/stanley-billings.md` | P-S | Renderer 100/243 local links; static targets checked | E000–E128, S2E01–S2E12 and S3E01–S3E18 played, plus separate S3E019 cast recap and out-of-game retrospective |
| `world/characters/stanley-diontalus.md` | P-T | Structural audit recorded; detailed links in census | See detailed world census |
| `world/characters/steerious-business.md` | P-S | Structural audit recorded; detailed links in census | See detailed world census |
| `world/characters/tedna.md` | P-S | Renderer 36 links; scoped lint recorded | Original Tedna E027–E050 with witnessed E048 rescue and E050 death; explicitly separate alternate Badass T S2E04–S2E09 appendix with March 2022 Q&A not treated as performed recovery |
| `world/characters/the-principal.md` | P-S | Canonical primary originally copied; 18 literal HTML alias tags removed from canonical only; 61/61 links and lint passed | E013–S3E18, with Principal/Vladimir historical claim boundaries retained |
| `world/characters/the-principle.md` | P-T | Structural audit recorded; detailed links in census | E013 and later Principal affairs, E128 claims, S3E01–S3E18 confrontation and lunar finale; bonus/creator accounts segregated |
| `world/characters/the-voice.md` | P-S | Structural audit recorded; detailed links in census | See detailed world census |
| `world/characters/tobacho-fleur.md` | P-S | Structural audit recorded; detailed links in census | E089–E125 Sigil portal, Hand/Fist custody, Hope bargain, later adversarial testimony |
| `world/characters/tungsten-wheel.md` | P-S | Structural audit recorded; detailed links in census | E125 initial lead, S2E02–S2E12 search/rescue, S3E01–S3E04 reunion and device |
| `world/characters/tylander-sullivan.md` | P-R | Structural audit recorded; detailed links in census | Early Wastes Slavetown and Black Mine context E013 and E019–E023 |
| `world/characters/union-wheel.md` | P-S | Structural audit recorded; detailed links in census | See detailed world census |
| `world/characters/vorel-titles.md` | P-T | Renderer 100/177 local links; static targets checked | First attestation vs repeated self-epithets/awarded titles through S3E18; S3E019 cast retrospective recitation not played conferral; S3E18 Friend title attributed to Stanley/Vorel, time window only P/Q cue alignment, still audio-provisional |
| `world/characters/vorel.md` | P-S | Renderer 100/316 local links; static targets checked | E001–E128, S2E01–S2E12 and S3E01–S3E18 played; separate earlier source cutoff and player Q&A interpretation |
| `world/creatures/basilisk-of-the-under-pit-caves.md` | P-S | Structural audit recorded; detailed links in census | E045 death; E051 remains/reversal |
| `world/creatures/black-headworms.md` | P-S | Structural audit recorded; detailed links in census | E058, E063–E064, E075 |
| `world/creatures/black-puddings.md` | P-S | Structural audit recorded; detailed links in census | E042 |
| `world/creatures/bloodsucking-desert-swarm.md` | P-S | Structural audit recorded; detailed links in census | E059 |
| `world/creatures/blue-black-chasm-flyers.md` | P-S | Structural audit recorded; detailed links in census | E076 |
| `world/creatures/brain-backed-spiders.md` | P-S | Structural audit recorded; detailed links in census | E073–E075 |
| `world/creatures/chester-the-bearsaurus.md` | P-S | Structural audit recorded; detailed links in census | E119 report; E120 direct hunt/death |
| `world/creatures/chicken-lords.md` | P-S | Structural audit recorded; detailed links in census | E107 prequel arena; E060 feast; E064 outbreak |
| `world/creatures/chids-hellhounds.md` | P-S | Structural audit recorded; detailed links in census | E070–E071 |
| `world/creatures/crater-wyvern.md` | P-S | Structural audit recorded; detailed links in census | E057 played encounter; E058 retrospective label |
| `world/creatures/dolo-popio-spawned-worms.md` | P-S | Structural audit recorded; detailed links in census | E080–E081 |
| `world/creatures/dunebreaker-fruit-ooze.md` | P-S | Structural audit recorded; detailed links in census | E109 same-world Dunebreaker prequel; bonus retrospective |
| `world/creatures/eight-legged-facility-predator.md` | P-S | Structural audit recorded; detailed links in census | E008 direct encounter; E009 later facility context |
| `world/creatures/froghemoth-gut-worms.md` | P-S | Structural audit recorded; detailed links in census | E052–E053 |
| `world/creatures/froghemoth-intestinal-ropers.md` | P-S | Structural audit recorded; detailed links in census | E053 |
| `world/creatures/gibbering-mouther.md` | P-S | Structural audit recorded; detailed links in census | E009 |
| `world/creatures/green-case-mimic.md` | P-S | Structural audit recorded; detailed links in census | E008 |
| `world/creatures/luminous-desert-beetles.md` | P-S | Structural audit recorded; detailed links in census | E006 initial lights; E007 witnessed beetles |
| `world/creatures/mushroom-pit-spider.md` | P-S | Structural audit recorded; detailed links in census | E044 |
| `world/creatures/outlands-wyverns.md` | P-S | Structural audit recorded; detailed links in census | E093 aerial battle against Traveler's Twin |
| `world/creatures/pale-tentacled-burrower.md` | P-S | Structural audit recorded; detailed links in census | E042 live underground encounter; E045 stone resemblance |
| `world/creatures/pixie-hulks.md` | P-S | Structural audit recorded; detailed links in census | E049 compelled transformation; E050 P0D death; E051–E052 swallowed hulks; E054 reversion |
| `world/creatures/purple-sands-tyrannosaurus.md` | P-S | Structural audit recorded; detailed links in census | E065 approach; E066 Fate 4 destruction and kill |
| `world/creatures/razak-val-invasive-worms.md` | P-S | Structural audit recorded; detailed links in census | E064 |
| `world/creatures/riding-raptors.md` | P-S | Structural audit recorded; detailed links in census | E027–E028 Diptak hunting mounts; E064 four escape mounts and release |
| `world/creatures/river-undead.md` | P-S | Structural audit recorded; detailed links in census | E045 river first sighting/attack; E046 final battle |
| `world/creatures/sand-squid.md` | P-S | Structural audit recorded; detailed links in census | E010–E055 food/hunt; E082 request; E123 analogy |
| `world/creatures/skeleton-spawning-flesh-giant.md` | P-S | Structural audit recorded; detailed links in census | E067 |
| `world/creatures/tainted-displacer-beast.md` | P-S | Structural audit recorded; detailed links in census | E020 |
| `world/creatures/tentacled-purple-fungi.md` | P-S | Structural audit recorded; detailed links in census | E021 |
| `world/creatures/translucent-wall-passers.md` | P-S | Structural audit recorded; detailed links in census | E070 |
| `world/creatures/white-filament-hunter.md` | P-S | Structural audit recorded; detailed links in census | E052 direct encounter; E053 host aftermath |
| `world/entities.json` | E-J | JSON schema and local targets checked | source_scope (seven cited episodes only): E000, E001, E028, E054, E060, E117, S3E18 |
| `world/places/black-mine.md` | P-R | Structural audit recorded; detailed links in census | E018–E026 |
| `world/places/chateau-weir.md` | P-S | Structural audit recorded; detailed links in census | E022–E025 first encounter; E048, E054 return and army; E083 retrospective; S3E11–S3E12 return, defeat and realm rupture |
| `world/places/chids.md` | P-S | Structural audit recorded; detailed links in census | E067–E069 location/entry; E069–E075 railway, Julia, VR/Charles, alarms, Cerinthala, portal device; E076–E079 biological containment, hive council and engineering entry; E080–E081 observed worm/Drive chamber events and all-four life-sacrifice/GM-declared deaths; E082 character consequences in Sigil, not CHIDS follow-up survey; February 2022 GM-retrospective creative intent kept distinct |
| `world/places/dunebreaker.md` | P-R | Structural audit recorded; detailed links in census | E107–E109 historical side-story prequel and 2020 Q&A retrospective |
| `world/places/dusthill.md` | P-R | Structural audit recorded; detailed links in census | E001–E007 source-town crisis; E010–E011 enslaved relatives; E058 promise and E059 actual returned survivor group |
| `world/places/elhandar.md` | P-S | Structural audit recorded; detailed links in census | E115 orbital sanctuary/first visits; E116–E124 family, Harbor and cave/dragon-heart developments; E125–E126 collapse and Villa protection; E128 rescue, Mars-bound departure and world-burrower sandstorm; S2E02 and S3E18 later horizon reviewed for stale-current-status boundary |
| `world/places/gray-waste-and-pandemonium.md` | P-R | Structural audit recorded; detailed links in census | E112–E113 Hope's separate Gray Waste, Pointless, River Styx, Pandemonium journey |
| `world/places/kaiser-casino.md` | P-R | Structural audit recorded; detailed links in census | E101–E102, E106; S3E12–S3E13 later infernal casino |
| `world/places/khaervilon.md` | P-S | Renderer 48 links; scoped lint passed; primary page migrated | E061–E081 keep, CHIDS and Drive, with E082 aftermath distinct |
| `world/places/kervalon.md` | P-T | Structural audit recorded; detailed links in census | E061/E064 warnings and approach; E065–E068 purple-sands/keep encounters; E069–E075 CHIDS interior and portal acquisition; E076–E081 actual engineering/Drive battle and E081 cliffhanger |
| `world/places/leaden-fingers-stormlands.md` | P-R | Structural audit recorded; detailed links in census | S3E14 reconnaissance and three-target setup; S3E15 one principal canyon revision and pre-ambush cliffhanger |
| `world/places/leopold-facility.md` | P-R | Structural audit recorded; detailed links in census | E008–E009 played visit; June 2019 bonus retrospective |
| `world/places/razak-val.md` | P-S | Structural audit recorded; detailed links in census | E059–E065 first arrival, challenge and parasitic outbreak; E104/E118–E121 Omnom later testimony and fate; S2E02 witnessed clan return and Mars departure; S3E09 Groxl claims; S3E18 rebuild journey begins |
| `world/places/sigil.md` | P-S | Structural audit recorded; detailed links in census | E081 declaration→E082 Sigil physical arrival and variant survivals; E083–E089 chapel, marionette contest, E088 resurrection and GM magic-rule correction, E089 portal-registry lead; E090–E093 Hive/Tobacho bargain and observed Outlands departure; E094–E097 White Tower events explicitly OUTSIDE Sigil; E105/E106 return/handover, E112/E113 Hope's secondary Sigil and Pandemonium route, E116 retconned Council-to-docks route, S3E15 Principal's temporary combat escape through Sigil; later GM bonus Q&As separately attributed |
| `world/places/slavetown.md` | P-R | Structural audit recorded; detailed links in census | E009–E018 central city arc, E026/E037 follow-up accounts, E058–E059 restitution testimony |
| `world/places/solar-mines.md` | P-S | Structural audit recorded; detailed links in census | E000/E024 remembered childhood; E117 recital/E118 Book/bonus creative retrospective; S2E03 unperformed council strategy; S3E04 scout estimates/unperformed assault plan; S3E05–S3E07 actual gate attack, rupture, Fate Six crushed and Ruby rescued; S3E08 giant generator and cable separate from Ruby; S3E09 camp and dome infiltration; S3E10 real child-labor/conditioning site and remote-custody discontinuity; S3E11 physical geothermal chamber and Ruby staged unactivated; S3E12 no return; S3E13–S3E15 allied occupation and actual core guards but continued nonactivation; S3E18 order, observed planet restoration, Nash monument, future township plans |
| `world/places/the-harbor.md` | P-S | Structural audit recorded; detailed links in census | E115 surviving community; E117 formal Harbor founding; E123–E124 continuity and lake rite; E126 impact casualties; E128 Mars-bound survivor departure |
| `world/places/tietkalla.md` | P-S | Structural audit recorded; detailed links in census | E028–E054 Trashburg/Teet keep, undercity and Hope coronation; E055–E059 reform, disaster, Principal promise and actual returned Dusthill persons; E103–E104 court/rail fire and Carthax raid; E110–E111 ruined keep/rescue; E115–E117 displacement and Harbor; S3E18 performed restoration and damaged-city return |
| `world/places/villa-ornath.md` | P-R | Structural audit recorded; detailed links in census | E115, E118 hidden study; E125–E126 impacts; E128 season-one survival; S2E01–S2E02 actual Fate Six departure and Mars landfall |
| `world/places/white-tower.md` | P-R | Structural audit recorded; detailed links in census | E093–E101 |
| `world/races/dwarves.md` | P-S | Renderer 29 links; scoped lint recorded | ancient ruins E003; communities through S3E02; E116 separate trade |
| `world/races/elves.md` | P-S | Renderer 28 links; scoped lint recorded | Elhandar E115–E128; subsequent S2E03–S3E18 |
| `world/races/harlequinari.md` | P-S | Renderer 15 links; scoped lint recorded | individual E102 onward; Council E113; later S3E02 |
| `world/races/illithids.md` | P-S | Renderer 30 links; scoped lint recorded | CHIDS E066–E081; independent Fax E087–E090 |
| `world/races/lizardfolk.md` | P-S | Renderer 18 links; scoped lint recorded | Vorel E000; community E016 onward; final S3E18 |
| `world/races/orcs.md` | P-S | Renderer 29 links; scoped lint recorded | E010 order contact; later S3E18 relocation |
| `world/races/pixies.md` | P-S | Renderer 35 links; scoped lint recorded | P0D E031–E056; alternate Pod E110 and S2E04 |
| `world/races/tieflings.md` | P-S | Renderer 19 links; scoped lint recorded | Hope E000; T'ietkalla E047 onward; final S3E18 |
| `world/technology/augmentation-cylinder.md` | P-S | Structural audit recorded; detailed links in census | S3E03 proposed operations/gear; S3E04 three completed surgery patients and Vorel's refusal; S3E05–S3E06 Vorel separately receives/equips +2 gear; S3E13 Nash heart intervention; S3E18 coercive chrome conversion/resurrection elsewhere |
| `world/technology/book-of-adjacencies.md` | P-S | Structural audit recorded; detailed links in census | E118 actual recovered responsive journal; E123 conversation about father's predictions; BONUS-2020-10 creative-process remarks |
| `world/technology/chromes-bane.md` | P-S | Structural audit recorded; detailed links in census | S3E04 +2 sword selected for Vorel; S3E05 actually handed over; S3E06 first battle use; S3E07 Vorel names weapon and kills flying patchwork dragon; S3E08 Groxl heart-cable cut; S3E09 explicit retention; S3E16 sword thrown; S3E17 sword again wielded; S3E18 retained in epilogue summary |
| `world/technology/diontalus-ocarina.md` | P-S | Structural audit recorded; detailed links in census | E125 physically handed to Stanley; E126 and E128 Diontalus' independent appearances and recovery; S3E08 spectral disintegration; S3E18 no separately documented artifact inventory |
| `world/technology/diplomacy.md` | P-S | Structural audit recorded; detailed links in census | E089 failed Parley recall; E110 alternate-history Diplomacy counterpart; S2E08 temporary Vorel loan and return; S3E03 Stanley physically transfers sword to Hope; S3E06 out-of-range loss, S3E07 renewed use; S3E09 Walmart out-of-range, S3E10 renewed use; S3E12 used as movement; S3E16 misses Principal and S3E17–S3E18 no final inventory |
| `world/technology/elhandari-enchanted-equipment.md` | P-T | Renderer 16 links; scoped lint recorded | S3E03–S3E18 |
| `world/technology/eye-of-groxl.md` | P-S | Structural audit recorded; detailed links in census | E052–E053 chest implantation; E077 CHIDS GR0X1 container; E080 flame-sword/shield; E124 Malhya recognition; S3E07 GM confirms Groxl identity through Eye; S3E08 Eye says NOT Groxl/abomination while generator and heart wiring are physically exposed and severed; S3E09 Groxl attributed historical warlock story; S3E17 visible Eye under chrome |
| `world/technology/eye-of-the-voice.md` | P-T | Renderer 21 links; scoped lint recorded | E106–S3E18 |
| `world/technology/fate-4.md` | P-S | Structural audit recorded; detailed links in census | E001/E006 constructed Dusthill recreational vehicle; E007–E028 modifications/repairs; E064 actual return by Follow/Rorf/Sira; E065 operating vehicle and T. rex warning; E066 actual crushing/explosion and separate Fang Fate Five salvage; E067 subjective memory only |
| `world/technology/fate-six.md` | P-S | Structural audit recorded; detailed links in census | E118 secret Villa Or'Nath study; E126 early unperformed ship transformation; S2E01 actually awakened after attunement; S2E02 Earth/Razak Val/Mars flight and first ghost crew; S2E04 first rift and family trip Planet Nash; S2E05–S2E07 Blast Belly Rock and Pentel Weiss, mortal orc losses; S2E12 rescue; S3E01–S3E03 Hell-vessel attack/escape, subsequent Mars arrival; S3E04 plans and S3E05 actual deployment; S3E07 performed cottage-to-ship change and first physical destruction by Groxl, Ruby saved separately; S3E13 actual ship rematerialization with incomplete ghost roster and Hope as navigator; S3E14 external-planar-Gate-only limit; S3E15 explosives delivery; S3E17 ship deliberately rams Principal copies and is destroyed again; S3E18 separate Moon ship, four-day Fate Six restoration, Hope pilots Planet Nash/Earth return and receives Mask/captaincy only afterwards; December 2021 GM ghost-stasis explanation kept retrospective |
| `world/technology/gem-of-tides.md` | P-S | Structural audit recorded; detailed links in census | E039 political Monsoon claim; E049–E050 actual artifact retrieval; E051 Vorel carrying stone to water-throne; E054–E056 plans/partial reconstruction; S3E18 planet restored by different Ruby device |
| `world/technology/hand-of-the-voice.md` | P-S | Structural audit recorded; detailed links in census | E100 Vorel takes separate gauntlet with living Hand from case; E101 Hope actually severs her own hand, attaches supernatural Hand and parts from group while gauntlet is resealed; E106 Tobacho receives Hand-less gauntlet; E118 private Voice pressure but no Eye acquisition; E123 Hope claims fatal removal consequence, untested; S2E04–S2E08 unperformed removal proposal/rumored patron origin/prison Eye speculation; S3E02 Principal physically steals living Hand, Hope survives via table death saves and Stanley Regenerate restores ordinary arm; S3E03–S3E04 no return; S3E12 Principal→Brett/Asmodeus→succubus assistant physical transfer; S3E13–S3E18 no further observed handoff; February/May 2022 creator Q&As separately reported |
| `world/technology/grapes-magical-guitar.md` | P-S | D-086 owner-approved **provisional** primary; Markdownlint zero, 11/11 rendered links, content preserves item/source uncertainties | E126 hostile guitar attack and contested seizure; E128 continued possession and musical test; S3E12 same guitar placed in Principal's dome, recharge unverified; subsequent custody not shown |
| `world/technology/henatar-guitar.md` | P-T | Legacy former primary with full original narrative and a canonical-page banner; 12/12 rendered links | Historic Henatar/Grape ASR label preserved; source-window details duplicate maintained Grape guitar primary pending WCL-197 compatibility disposition |
| `world/technology/hollow-ring.md` | P-S | Structural audit recorded; detailed links in census | S3E02 earlier theft from Hope by Principal; S3E11 physical return and modified Gate use; S3E12 confirmed ring on Hope and zero charge; S3E13 Asmodeus transports party without ring; S3E15 Principal portals through Sigil without ring; S3E16–S3E18 no further direct recharge or inventory check |
| `world/technology/mask-of-eltanfawr.md` | P-S | Structural audit recorded; detailed links in census | E118 Stanley discovers the mask and journal in Villa Or'Nath but does not wear mask; E126 actual donning/reshaping, failed lift and attunement requirement; S2E01–S2E02 achieved flight of villa/Fate Six to Mars; S3E05 mask's Peer into Plurality physically used to cast Foresight at 10 max-HP cost; S3E07 ship-to-house-and-back transformation and later ship destruction; S3E11 further Foresight; S3E13 actual mask summon/reappearance of vessel, incomplete ghost crew; S3E14 external Gate requirement; S3E15 Foresight again; S3E17 attempted but unproven remote command, ship second destruction; S3E18 four-day recovery and witnessed Stanley-to-Hope gift/crown |
| `world/technology/mask-of-elton-iv.md` | P-T | Structural audit recorded; detailed links in census | E118 actual discovery and inventory, E126 mask-linked spelljammer interface and canonical mask-of-eltanfawr.md owner spelling; legacy historical link only |
| `world/technology/nash-dragon-heart.md` | P-S | Structural audit recorded; detailed links in census | E121 engineered heart opens and mother-dragon apparition; E122 heart resumes Nash body while separate dead dragon's natural heart harvested; E128 natural heart actually recovered and travels toward Mars; S2E02 unfinished Ruby distinct; S2E12 Nash dies but implanted engine/eyestalk survives; S3E01 Stanley Regenerate rebuilds Nash, S3E02 full body and Sprout; S3E03 paternity dream and refused cylinder extraction; S3E10 remembered surgery site; S3E12 lightning/duplicate Nash incident with engine still implanted; S3E13 Brett/Asmodeus removes and keeps engine, fabricates organic heart; S3E14 failed partial dragon shape; S3E18 chrome conversion, death and Wish/True Resurrection without witnessed engine return; bonus creator theories separately qualified |
| `world/technology/noble-speeder.md` | P-S | Structural audit recorded; detailed links in census | E123 lodge keeper permits use, Hope tests and drives to Harbor; E124 vehicle actually left Villa Or'Nath; E125 three separately available biodome terminal vehicles ridden; E126 occupants survive; E128 separate four speeders attached to Villa |
| `world/technology/portal-device.md` | P-S | Structural audit recorded; detailed links in census | E075 secure vault and Vorel first acquisition; E075 portal pairing tests and transfer to Hope; E076 physical bugbear escape and handheld transfer to Nash; E077 Hope reuses device, discovers necrotic neutralization mode, collateral damage to Vorel; E078–E079 continued Hope use to bypass lock; E080 misses illithid; E081 separately operates major Drive console; E082 Hope in Sigil without handheld custody check |
| `world/technology/rejuvenation-syringe.md` | P-S | Structural audit recorded; detailed links in census | S3E03 four inventory doses assigned; S3E04/S3E05 no administered syringes; S3E10 discussion and regular short rest; S3E11 natural long rest; S3E17 Stanley actually injects his own dose, separate second held reported; S3E18 no observed further consumption |
| `world/technology/rubistic-triangulosphere.md` | P-T | Structural audit recorded; detailed links in census | E122–E128 proposal and separate natural black-dragon-heart extraction/recovery; S2E02 partly built Mars machine; S3E01–S3E03 Tungsten claims reagent possession and actual work; S3E04 completed device and brief tested spin; S3E05 Earth shipment aboard Fate Six; S3E07 dragon Nash rescue from ship; S3E08 lava generator NOT Ruby; S3E09 ally wagon camp; S3E10 GM resets custody with underground team; S3E11 placed unactivated at geothermal core; S3E13 orders elite security, S3E14/S3E15 actual guards; S3E17 Worldbreaker banishment, S3E18 activation order and planetary restoration |
| `world/technology/traversal-drive.md` | P-S | Structural audit recorded; detailed links in census | E067 and E070 reported ancient planetary purpose; E079 first physical Drive chamber, E080 interrupted battle, E081 actual machine controls and four-person life sacrifice, E082 Sigil aftermath |
| `world/technology/windboards.md` | P-S | Structural audit recorded; detailed links in census | S3E14 five boards physically offered, Hope's tests; S3E15 speed/use and Hope board physically ground up; S3E15 Principal makes two portals through Sigil; S3E16 three working boards with four riders at canyon opening; S3E17 Hope carries Nash during Banishment; S3E18 no final board inventory |

## Narrative edition and reader portals (22)

| Maintained file | Status | Accepted portion / remaining limitation |
| --- | --- | --- |
| `narrative/ARC_01.md` | A-N | Approved eleven-arc private structure/placement; source/audio fidelity still open |
| `narrative/ARC_02.md` | A-N | Approved eleven-arc private structure/placement; source/audio fidelity still open |
| `narrative/ARC_03.md` | A-N | Approved eleven-arc private structure/placement; source/audio fidelity still open |
| `narrative/ARC_04.md` | A-N | Approved eleven-arc private structure/placement; source/audio fidelity still open |
| `narrative/ARC_05.md` | A-N | Approved eleven-arc private structure/placement; source/audio fidelity still open |
| `narrative/ARC_06.md` | A-N | Approved eleven-arc private structure/placement; source/audio fidelity still open |
| `narrative/ARC_07.md` | A-N | Approved eleven-arc private structure/placement; source/audio fidelity still open |
| `narrative/ARC_08.md` | A-N | Approved eleven-arc private structure/placement; source/audio fidelity still open |
| `narrative/ARC_09.md` | A-N | Approved eleven-arc private structure/placement; source/audio fidelity still open |
| `narrative/ARC_10.md` | A-N | Approved eleven-arc private structure/placement; source/audio fidelity still open |
| `narrative/ARC_11.md` | A-N | Approved eleven-arc private structure/placement; source/audio fidelity still open |
| `narrative/ARC_FIVE.md` | E-L | Protected legacy word-form arc; preserve source bytes and route |
| `narrative/ARC_FOUR.md` | E-L | Protected legacy word-form arc; preserve source bytes and route |
| `narrative/ARC_ONE.md` | E-L | Protected legacy word-form arc; preserve source bytes and route |
| `narrative/ARC_SIX.md` | E-L | Protected legacy word-form arc; preserve source bytes and route |
| `narrative/ARC_THREE.md` | E-L | Protected legacy word-form arc; preserve source bytes and route |
| `narrative/ARC_TWO.md` | E-L | Protected legacy word-form arc; preserve source bytes and route |
| `narrative/README.md` | P-N | Reader navigation reviewed; comprehensive source and browser review pending |
| `narrative/SEASON_THREE.md` | E-C | Compatibility season portal; not an additional story |
| `narrative/SEASON_TWO.md` | E-C | Compatibility season portal; not an additional story |
| `README.md` | P-N | Cross-campaign front door and Wastes navigation (WCL-106); comprehensive source/browser review pending |
| `wastes/README.md` | P-N | Wastes reading route in private edition (WCL-004); full factual/browser acceptance pending |

## Wastes evidence-facing episode dossiers (161)

These source-oriented files retain per-episode **knowledge as of that recording/dossier**. Listing them verifies their place in the directory, **not** their text, audio, source quality, rendered links or actual events. `S3E019` is a postcampaign cast conversation, **not** a new played episode.

| Maintained file | Status | Verified scope and unresolved limitation |
| --- | --- | --- |
| `episodes/E000.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E001.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E002.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E003.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E004.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E005.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E006.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E007.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E008.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E009.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E010.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E011.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E012.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E013.5.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E013.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E014.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E015.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E016.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E017.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E018.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E019.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E020.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E021.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E022.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E023.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E024.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E025.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E026.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E027.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E028.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E029.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E030.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E031.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E032.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E033.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E034.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E035.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E036.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E037.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E038.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E039.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E040.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E041.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E042.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E043.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E044.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E045.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E046.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E047.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E048.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E049.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E050.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E051.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E052.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E053.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E054.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E055.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E056.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E057.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E058.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E059.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E060.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E061.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E062.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E063.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E064.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E065.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E066.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E067.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E068.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E069.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E070.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E071.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E072.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E073.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E074.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E075.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E076.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E077.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E078.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E079.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E080.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E081.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E082.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E083.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E084.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E085.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E086.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E087.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E088.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E089.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E090.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E091.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E092.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E093.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E094.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E095.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E096.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E097.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E098.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E099.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E100.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E101.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E102.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E103.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E104.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E105.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E106.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E107.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E108.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E109.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E110.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E111.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E112.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E113.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E114.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E115.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E116.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E117.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E118.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E119.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E120.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E121.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E122.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E123.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E124.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E125.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E126.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E127.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/E128.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S2E01.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S2E02.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S2E03.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S2E04.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S2E05.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S2E06.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S2E07.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S2E08.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S2E09.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S2E10.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S2E11.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S2E12.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E01.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E019.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E02.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E03.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E04.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E05.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E06.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E07.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E08.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E09.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E10.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E11.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E12.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E13.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E14.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E15.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E16.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E17.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |
| `episodes/S3E18.md` | E-D | Listed source-facing dossier only; original-audio, per-file content and link checks not performed here |

## Outstanding work and acceptance boundaries

- **World presentations:** Existing source-first and compatibility candidates remain `P-T`; `P-R` pages still need D-048 editorial review. No `P-S` page receives full factual or audio acceptance solely because the census read it through EOF.
- **Limited/blocked verification:** Seven world files have only the first 100 local links rendered (WCL-191), while `world/CONSISTENCY_LEDGER.md` has a safety-blocked preview (WCL-192) and `world/characters/bok-bok.md` a safety-blocked lint (WCL-193). Previously verified independent static path existence is not a new renderer pass. Native browser, legacy anchors, external bookmarks and responsive navigation remain WCL-007/WCL-103.
- **Naming and history:** Canonical/provisional filename migration WCL-195 must precede full incoming-link review and redirect-only placeholder removal WCL-197. Campaign-backed peoples' origin histories are separately open under WCL-196. The campaign-wide chronological/current-status/source-boundary review remains WCL-040.
- **Narratives and episodes:** Accepting the 11 numbered arc routes does not certify every scene or the underlying `episodes/` dossiers. Legacy arcs stay protected. No original recording was listened to and no per-episode dossier was individually audited for this matrix.
- **Private scope:** A merged private reading edition is not a public deployment; WCL-008 remains conditional. No commit, push, new public URL, or browser acceptance is claimed by this matrix.

**Maintenance:** After a real canonical rename, deletion or new maintained file, reconcile this path list with the world census and the task register; update exact unique counts only after confirmed changes. Keep WCL checkboxes and *next action* solely in [the task register](WASTES_CLEANUP_TASKS.md), detailed per-file structural evidence solely in [the census](WASTES_WORLD_FILE_CENSUS.json), and artifact compatibility in [the manifest](WASTES_CLEANUP_MANIFEST.md). Do not duplicate full issue text here.

**Provenance:** WCL-002–WCL-004, WCL-106, [Wastes campaign plan](WASTES_CAMPAIGN_CLEANUP_PLAN.md), [artifact manifest](WASTES_CLEANUP_MANIFEST.md), world census and current directory listings. There was no new complete Markdown/body read for the other in-scope groups, no audio/source canon adjudication, and no public release.
