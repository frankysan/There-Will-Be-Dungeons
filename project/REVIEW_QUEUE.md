# The Wastes — active audio, source and editorial review queue

**Status: OPEN tasks, updated 2026-10-22.** Full *Wastes* spoilers through corrected **E085**, with separate [March 2019 Q&A](../episodes/BONUS-2019-03.md), [April 2019 roundtable](../episodes/BONUS-2019-04.md), [June 2019 Q&A](../episodes/BONUS-2019-06.md), [July public-release 2019 bonus](../episodes/BONUS-2019-07.md), [August public-release 2019 bonus](../episodes/BONUS-2019-08.md) (spoken July 27), and [September public-release 2019 bonus](../episodes/BONUS-2019-09.md), plus [October public-release Q&A](../episodes/BONUS-2019-10.md) (recording day not verified) and [November public-release Q&A](../episodes/BONUS-2019-11.md) (host actually calls it October; original publication metadata needs checking) and [December public-release Q&A](../episodes/BONUS-2019-12.md) (four ASR outputs from two audio copies; exact recording date unverified) and [January 2020 public-release Q&A](../episodes/BONUS-2020-01.md) (**host actually calls it December 2019; two ASR exports, exact recording date unverified**). **No new listening, SRT editing or handout verification occurred during consolidation.** The [consistency ledger](../world/CONSISTENCY_LEDGER.md) identifies **what remains uncertain versus resolved**. This queue tells reviewers **where to listen or which sources to compare**.

**Complete historical backlog preserved:** The entire ~73k-character pre-Phase-D [review queue, including its many timed episode-by-episode tasks](../research/legacy/2026-10-22/PROJECT_REVIEW_QUEUE.md), is frozen with functioning relative links. Its outstanding tasks were **not automatically closed** by omission from this shorter index. The original [consistency issue register](../research/legacy/2026-10-22/WORLD_CONSISTENCY_LEDGER.md) also preserves exact issue keys and status history.

## Priority and reporting

**Critical:** May change a death/survival outcome, main character identity, episode numbering, world-history truth level or legal/source rights. **High:** May affect important name, item, mechanics, political relationship, speaker identity or chronology. **Medium:** Detailed atmospheric wording, minor NPC aliases, maps or inventory whose ambiguity does not yet change a major conclusion. Avoid making all 1,000+ hours of audio a single unactionable “listen later” item.

When a review is completed, record **episode + absolute recording time/cue IDs**, exact source file/recording, **who listened or inspected the handout**, date, old/new wording or interpretation, whether audio truly verified it, changed documents and relevant test results. A different ASR model, wiki, cast-written spelling, old owner notes and a fan image are **not all the same evidence tier**. Only close the bounded task actually tested.

## 1. Pilot ASR transcription and diarization

**2026-10-22 batch follow-up:** Listen to the [first Qwen Q8 + Canary + Nemotron
intake examples](../reports/QWEN_CANARY_INTAKE_2026-10-22.md), especially March
2019 bonus **00:40:29–00:40:33 / 02:09:59–02:10:03**, April bonus
**00:19:06–00:19:07 / 00:27:31–00:27:34**, and E039
**02:39:17–02:39:21 / 03:31:02–03:31:06**. Compare Qwen-only and Parakeet-only
wording with context and agreed controls. All are unverified alignment
candidates, not confirmed omissions. Check the six Qwen cue-overlap pairs listed
by cue ID in the accompanying JSON separately from speech recognition.

| Priority | Recording / time | What to verify, and what not to misstate | Evidence |
|---|---|---|---|
| **Critical** | **E000 ~00:13:07–00:13:28** | Listener confirmed **“Now” is final spoken word**; align it to audio, exclude trailing music. Content resolved, **timestamp not**. | [E000](../episodes/E000.md), [archived pilot queue](../research/legacy/2026-10-22/PROJECT_REVIEW_QUEUE.md) |
| **Critical** | **E001 00:47–00:48 and 01:55–01:56** | Listener confirmed substantial **Cohere omissions**. Verify Parakeet/Qwen wording/audio; keep omissions as **regression checks**, not claims all later model words are accurate. | [model tests](MODEL_TESTS.md), [E001](../episodes/E001.md) |
| **High** | **E001 00:00–00:13** | Compare `no m h`, actual greeting and music; VAD baseline/padding effects. | [segmentation report](../reports/PARAKEET_SEGMENTATION_2026-10-21.md) |
| **High** | **E001 01:23–01:42** | Multiple Parakeet runs disagree on overlapping greetings. **29.640-second targeted clip** may include `hi kyle hi hi` and extra `there`; clip export is **not** listener verdict. | [third-pass execution](../reports/TARGETED_VERIFICATION_2026-10-21.md), [multi-pass evaluation](../reports/MULTIPASS_PILOT_2026-10-21.md) |
| **High** | **E001 02:17–03:08 and 10:00 boundary** | Resolve extra words, duplicate `if`, exact chunk overrun/timestamp clamping; compare words, alignments and speaker tags separately. | [segmentation experiment](../reports/PARAKEET_SEGMENTATION_2026-10-21.md) |
| **High** | **E001 ~00:58, 01:17, 02:31; throughout** | **Scott performing a different voice is listener-confirmed**, not a sixth person. Verify remaining switch **boundaries**, keep raw diarizer provenance; do not globally map `speaker 5` in future episodes. | [workflow](WORKFLOW.md), [D-006](DECISIONS.md) |
| **Medium** | **E001 00:23:21, 01:51:13, 02:13:40** | Compare Qwen Q4/Q8 extra text, especially possible `voodoo and the steeple and the antenna`; model-only insertions must **not** be silently accepted. | [model tests](MODEL_TESTS.md), [original queue](../research/legacy/2026-10-22/PROJECT_REVIEW_QUEUE.md) |
| **Medium** | **E001 04:13–08:45, other pilot cues** | Check character/place spellings, interruptions and 924 speaker-ID changes reported between Q4 and Q4+Canary. Beware WER claims from unverified automatic comparisons. | [pilot reports](../reports/MULTIPASS_PIPELINE.md) |
| **High** | **Whole archive, before scaling editing** | Build small **audio-verified controls**, keep model/run/aligner/VAD/diarization hashes and candidate IDs, and evaluate omissions/hallucinations and word timing independently. | [workflow](WORKFLOW.md), [pipeline report](../reports/MULTIPASS_PIPELINE.md) |

**Existing validated facts to preserve:** E000 ends in **“Now”**; E001 diarizer's extra Scott-character voice is **not a sixth cast member**; Cohere speech omission exists. **Unverified:** exact time of “Now,” word-by-word Parakeet accuracy and broad quantitative WER.

## 2. Story-critical Arc One listening and primary-handout review

| Priority | Source / approximate recording time | Specific review target | Related open key |
|---|---|---|---|
| **Critical** | **E000 ~00:01–00:04; E001 ~00:04–00:08** | Read/listen to **original world prologue**, dragon-war timescale, Dusthill setting and speech versus dramatic retelling. | `history.dragon_war` |
| **High** | **E002 ending → E003 opening; E005 end → E006 ~00:24** | Distinguish **Hillmaster fall**, engine restart, intake repair, and **actual surface water test E006**. Don't redated event on a recap alone. | source-cutoff checks; [E002](../episodes/E002.md)–[E006](../episodes/E006.md) |
| **High** | **E006 ~01:19–01:52** | Actual names/roles and raid figures (**Shun'ti, Tetsuo, Jimster**, 45 dead/25 abducted); confirm as **spoken report**, not census. | `names.dusthill_regions`, `plot.prisoners` |
| **High** | **E008–E009, E013.5 opening** | Guest **Chance and Eddie**'s actual last sighting; distinguish GM out-of-character reassurance from in-story rescue/death; confirm E013.5 **release versus event position**. | `plot.guest_chance_eddie` |
| **High** | **E010–E013 (especially E013 ~00:05–00:12)** | **Pristine→Slavetown** GM exposition, `Principle/Principal`, **Toyota Host vs Koromukishi**, magistrate and factions; written maps/cast usage. | `names.principle`, `names.koromukishi` |
| **High** | **E012–E016, E020–E021, E026** | **Mine deed**, Catherine Speckles `999th level`, Tylander alias/death reports, journal, claims about Pristine and mining/soul pacts. | `plot.mine_deed`, `plot.tylander_reports`, `sources.diary_and_maps` |
| **High** | **E017 ~00:10–01:20 and E018 opening** | Pixie Blush's effects, **real foundry/fire destruction**, whether any later sandstorm **actually saved** Slavetown. | Scene outcome and `plot.prisoners` |
| **Critical** | **E022–E024, especially E023 ~02:30–02:50** | Separate **Quizquaz/beholder/Soulbroker**, exact **three signers vs Vorel refusing**, soul-pact text, **1,000 days/nights** terms and feats versus levels. | `rules.soulbroker_pact`, `names.catoblepraithe` |
| **Critical** | **E023 private visions; E024 Nash Solar Mines scene** | Listener/source check speaker privacy and wording; **Nash's implanted dragon heart** vs contradictory memories, **Hope's mother vision** and unshared claims. | `history.solar_mines`, `sources.private_handouts`, `lore.afterlife` |
| **High** | **E028–E030; E034 ~00:59–01:39** | **Diptak alive oath** versus rumored clan force; **Stanley refusing Diontalus** and involuntary control; Buttons' behavior prior to retrospective disclosure. | `names.secondary_people`, character-cutoff evidence |
| **High** | **E031–E039** | **Angelashi** joined/separated name, `P0D` spoken “Pod,” **wedding not held/Blood Ball not played**, Monsoon/gang alliances, **Hope missile injury** and contemporaneous prosthetic mechanics. | `names.angelashi`, `items.hope_prosthetics` |
| **Critical** | **E041–E045, especially E045 ~00:18–00:24** | **George Miller** self-wound vs actual **Diontalus murder**, private papyrus, disputed magic eggs/core, cave king, basilisk body. | `plot.george_radio`, `sources.private_handouts` |
| **High** | **E046–E048, especially E047 late and E048 elder explanation** | **Nash casts Reduce**, Vorel retrieves elder; old **royal book and initials M/N**, **Nobiery** orthography, **Akmenos genealogy**, twelve houses, Weir troop pact as speaker testimony. | `names.nobiery`, `history.tietkalla_royalty` |
| **Critical** | **E048 prison → E049–E050 warehouse** | **Tedna and Bok Bok rescued alive E048**, **P0D forced transformation E049**, **Buttons killed by Vorel E049**, **P0D and Tedna dead E050**; hear actual lines and whose player controls shared body. | Resolved cutoff rows; transcription still pending listening |
| **High** | **E050–E051** | **Gem of Tides recovered** vs installation, **Fox and Scully** ammunition, **Pillars of Decency**, Kefeli claims, both Hope/Vorel **restored alive before E051 end**. | `plot.gem_installation`, `items.gem_fox_scully` |
| **High** | **E052–E053, especially split ~E053 00:10–00:20** | **Upper cocoon escapes; lower half dies**, froghemoth telepathy/spell anomalies, **Eye of Groxl** homebrew power wording, robe rowboat use, different **chameleon-scale** effect. | `plot.froghemoth_upper`, `rules.eye_groxl_powers`, `items.robe_patches` |
| **Critical** | **E054 ~00:21–01:18** | **Angelashi alive and rescued**, **Monsoon mist escape**, **returned armed tieflings** and **Hope's coronation**, prince's death/name, **Din's execution at Hope's signal**. Confirm return troop count not “1,000” without evidence. | `history.tietkalla_royalty`, `names.secondary_people`, `plot.monsoon_next` |
| **High** | **E054 ~01:18–end** | House names, orders versus completed security/farm rebuilding, civic inclusion, heir discussion, and **future downtime** announced, not already enacted. | `plot.monsoon_next`, court names |
| **Critical** | **Bonus 2019-03 ~02:35–02:40** | Beau's **Buttons loved Stanley / Arcanum / remove Diontalus** explanation, cast reaction, precise attribution. **Do not backdate motive into E049 dialogue.** | [Q&A](../episodes/BONUS-2019-03.md) |
| **High** | **Bonus ~00:10–00:16, ~00:40–00:43, ~01:07–01:23, ~02:17–02:20, ~02:40–02:49** | **Toyota host deliberately withheld**, unchosen pixie route and Order 26, uncertain gods/heaven, Nash heart invention, **George's missed radio clue**, missing Blink scroll. | `plot.toyota_host`, `plot.george_radio`, `items.nash_blink_scroll`, `lore.afterlife` |

**Further scene-level checks** (all unresolved unless explicitly tagged previously as listened) remain by episode and cue in the [archived E002–E054 sections](../research/legacy/2026-10-22/PROJECT_REVIEW_QUEUE.md). This grouping is for **work prioritization**, not a claim that all secondary items have been settled.

## 3. Name, artwork, inventory and specialist handout queue

| Priority | What to obtain or verify | Sources and scope |
|---|---|---|
| **High** | **Angelashi/Angel Ashi** exact word division; **Nobiery/Nobieri**, **Catoblepraithe**, **Kefeli**, **Prince Aladweir**, **Lazlo**, **Melgor/Fula/Relium**, **Pentael Wise** vs fan `Pentelvice`. | [Discord report](../reports/DISCORD_SPELLING_2026-10-21.md), [ledger](../world/CONSISTENCY_LEDGER.md), [E048](../episodes/E048.md), [E054](../episodes/E054.md) |
| **High** | **Mawstorm** sword's exact orthography and homebrew item mechanics (owner-suggested; `Ma Storm`/`maw storm`/`moss storm` in ASR); check E037 ~02:19–02:46 and E038 recap ~00:03:54, preferably against a cast-written item sheet. Also index **Vorel's self-awarded titles**, beginning with **“Lizard King”** in E036 ~00:53–01:10, with speaker, cue, verbatim/uncertain wording and recognition status. | [E037](../episodes/E037.md), [E036](../episodes/E036.md), [Vorel title register](../world/characters/vorel.md), [June Q&A](../episodes/BONUS-2019-06.md) |
| **High** | **Eye of Groxl mechanics** via GM item sheet; **NOT its identity/spelling** (owner resolved one item). Preserve separate skull helmet, changing scales and other artifacts. | [D-028](DECISIONS.md), [E053](../episodes/E053.md), [Vorel](../world/characters/vorel.md) |
| **High** | **Soulbroker contract** image/text and precise conditions, Weir guest waivers versus three character soul signatures. | [E023](../episodes/E023.md), [Weir reference](../world/places/chateau-weir.md) |
| **High** | **Robe of Useful Items** finite patch counts, items truly used E048/E051/E053; **Fox and Scully / Smokey's belt**, Vorel's hoard actual carried/reburied totals, Nash **Blink scroll**. | [E046](../episodes/E046.md)–[E054](../episodes/E054.md), [Q&A](../episodes/BONUS-2019-03.md) |
| **High** | **Secret house record E047, E045 private papyrus, M/N scroll, Tylander diary**, **Tedna's letter**, and other withheld audio/handouts. Record **unavailable** rather than reconstructing words. | [E020](../episodes/E020.md), [E037](../episodes/E037.md), [E045](../episodes/E045.md), [E047](../episodes/E047.md) |
| **Medium** | **Regional/fortress/Fate 4 maps and wiki images** with original version, creator, reuse license and early-episode handout match. Do not infer copyright permission. | [image provenance](IMAGE_ASSETS.md), [archived visual queue](../research/legacy/2026-10-22/PROJECT_REVIEW_QUEUE.md) |
| **Medium** | All other proper names, one-time NPC nicknames, spell adjudications, offscreen prisoner deaths, guest-campaign boundaries and encounter inventories from E002–E054. | [full archived queue](../research/legacy/2026-10-22/PROJECT_REVIEW_QUEUE.md), [original ledger](../research/legacy/2026-10-22/WORLD_CONSISTENCY_LEDGER.md) |

**Already resolved project-level spellings:** **Diontalus** ([D-026](DECISIONS.md)) and the singular **Eye of Groxl** item ([D-028](DECISIONS.md)). **Tietkalla** is cast-written with referent-specific support, **not blanket audio-certified**. Do not reopen the same-item identity question merely because `Grojil` and `Groxel` survive in historical ASR strings.

## 4. Coverage register — every researched main episode and exception

This is a **batch routing grid**, not a statement that every cue within a listed episode was scrutinized afresh in this Phase D pass.

| Episode span | Main tasks and active file |
|---|---|
| [E000](../episodes/E000.md)–[E001](../episodes/E001.md) | Audio-grounded ASR pilot, performer versus character voice, prologue, short greetings and known omissions |
| [E002](../episodes/E002.md)–[E005](../episodes/E005.md) | Dusthill old guards, original names, engine/pump/intake, Hillmaster falling, E005 outlet not yet tested |
| [E006](../episodes/E006.md)–[E009](../episodes/E009.md) | Surface water check, raid count and leadership, Bok Bok, facility/guests' fate and 24-hour countdown |
| [E010](../episodes/E010.md)–[E012](../episodes/E012.md) | Slave town map and patron names, Principle/Koromukishi hierarchy, disputed deed and imprisoned people |
| [E013](../episodes/E013.md)–[E016](../episodes/E016.md) | GM Pristine exposition, **E013.5 earlier-in-story** supplement, Orp/Tylander/reported death and official claims |
| [E017](../episodes/E017.md)–[E021](../episodes/E021.md) | Pixie Blush, foundry fire, Black Mine lift/rockfall, diary, unidentified skeleton and character visions |
| [E022](../episodes/E022.md)–[E027](../episodes/E027.md) | Distinct beholder/Quizquaz/Soulbroker, signatures vs refusal, dragon heart, escape, Liberators, Tedna |
| [E028](../episodes/E028.md)–[E033](../episodes/E033.md) | Diptak's living surrender, Buttons' arrival, Diontalus forced entry, Teet arrival, P0D and drugs |
| [E034](../episodes/E034.md)–[E039](../episodes/E039.md) | Diontalus admission, unplayed Blood Ball, guns and gangs, Angelashi, rocket explosion, Hope amputations and prosthetics |
| [E040](../episodes/E040.md)–[E045](../episodes/E045.md) | Pursuit into pit, froghemoth eggs/sphere, cave king, **E043 one-shot excluded**, George's actual murder, basilisk |
| [E046](../episodes/E046.md)–[E048](../episodes/E048.md) | Beanstalk/key, ancient library/papers, freed tiefling elder, **Tedna/Bok Bok live rescue**, Angelashi death *report* |
| [E049](../episodes/E049.md)–[E051](../episodes/E051.md) | Buttons betrayal, P0D involuntary change, Tedna/P0D deaths, Gem and guns, Kefeli, restored petrification |
| [E052](../episodes/E052.md)–[E054](../episodes/E054.md) | Froghemoth fission, Eye of Groxl powers, alive Angelashi, Monsoon escape, returned host and coronation |
| [BONUS-2019-03](../episodes/BONUS-2019-03.md) | Q&A retrospective cast/GM testimony; **not corrected E055** |
| [BONUS-2019-04](../episodes/BONUS-2019-04.md) | Roundtable on early Arc Two, character technique and GM's emergent Tietkalla design |
| [BONUS-2019-06](../episodes/BONUS-2019-06.md) | May-spoken/June-archived bonus; Stanley/Nash/Vorel/Hope goals, Principle origin, unused encounters and sand-fishing design |
| [E055](../episodes/E055.md)–[E060](../episodes/E060.md) | Second-arc time jump, Tietkalla and Principle, skyfall, parasites and Orp's initial rule; see focused checks in section 5–6 |
| [E061](../episodes/E061.md)–[E063](../episodes/E063.md) | Future-Nash egg theft, Bramie death, Orp slain, Vorel Great Fang, Zercil and prisoners; see the archived detailed queue |
| [E064](../episodes/E064.md)–[E065](../episodes/E065.md) | Razak Val collapse, Fate 4 recovery, Rorf's murder confession, storm and alleged future egg copies; see the archived detailed queue |
| [E066](../episodes/E066.md)–[E067](../episodes/E067.md) | Fate 4 destruction, Follow/Rorf deaths, Sira abducted, Kervalon infiltration and planet-engine report; see the archived detailed queue |
| [E068](../episodes/E068.md) | Actual T. rex Polymorph, illithid skin, sealed guards, magical shaft, hidden biting-panel doors; see the archived detailed queue |
| [BONUS-2019-07](../episodes/BONUS-2019-07.md) | Public July bonus, spoken June 29 recording, character/GM retrospective |
| [BONUS-2019-08](../episodes/BONUS-2019-08.md) | Public August bonus, spoken July 27 recording, Solar Mines radiation, artifacts and shaft-clue explanation |
| [E069](../episodes/E069.md)–[E071](../episodes/E071.md) | CHIDS entrance/funicular and ID systems, illithid office, Charles upload, Hell's UBI imp, Principle allegations, archive and frozen data center; see the archived detailed queue |
| [E072](../episodes/E072.md)–[E073](../episodes/E073.md) | Cerinthala and four preserved humans in frozen data center; +1 AC cursed necklace; ice constructs, Slow Peters and Careful Spell; service tunnels, bio-labs, broken focus, elevator spider; see the archived detailed queue |
| [BONUS-2019-09](../episodes/BONUS-2019-09.md) | Public September bonus: Solar Mines official-map existence versus Nash's potentially unreliable memories, Stanley feat revision, future Fate 5; see the archived detailed queue |
| [E074](../episodes/E074.md)–[E075](../episodes/E075.md) | Spider matriarch and brain-backed swarms; Cerinthala crushed and later resurrected/betrays; red memory-drain creature, body worms, secure red/green portal device, unexplored back-room vent and bugbear charge; see the archived detailed queue |
| [E076](../episodes/E076.md)–[E077](../episodes/E077.md) | **Actually executed portal escape**; containment chasm, winged predator, phantasms, rocket/tonic supplies, anti-dragon suit, neural reprogramming, Lethanphius, device necrotic beam, hive council and disputed Wall Nash; see the archived detailed queue |
| [BONUS-2019-10](../episodes/BONUS-2019-10.md) | October public-release cast Q&A: Nash's baby hand as optional dragon claw, family themes and **separate Inverse** library/DM history; see the archived detailed queue |
| [E078](../episodes/E078.md)–[E079](../episodes/E079.md) | **Actual limb repair and long rest E078**, hive cache and physical transport, Chance/Eddie rescue; **short rest and illithid disguise E079**, first actual Drive-chamber sighting, Hope's two-rocket strike, Cerinthala body disintegrates again and larger alien survives; see the archived detailed queue |
| [BONUS-2019-11](../episodes/BONUS-2019-11.md) | November public-release filename, **October spoken introduction**; spell-ring/diamond flavor, acid-breath and Monster Mender restrictions, Eye intent, GM's limb house ruling, cast's E079 reaction; see the archived detailed queue |
| [BONUS-2019-12](../episodes/BONUS-2019-12.md) | **December bonus, four-export ASR comparison**: GM states Hope/Stanley are **Weir-bound petitioner soul manifestations**, explains unplanned four-person sacrifice and lost gear, discusses **Dolo/Andreeste** contract, preserves unknown Tietkalla outcome and Nash's nature. See [ASR comparison](../reports/BONUS_2019_12_ASR_COMPARISON_2026-10-22.md); no listening verification |
| [BONUS-2020-01](../episodes/BONUS-2020-01.md) | **January 2020 public-release file; host calls it December 2019**: Beau calls E085's green intervention **Lady of Pain**, confirms **Nash's regrowth toward his prior body** and **external (not permanent) spell suppression**, Jon clarifies **Nothing's internal voice/kenku curse**, and Beau recalls **Principle studying crystal-bound Diontalus** rather than launching him into space. **Steel Heaven question and spell-suppression cause unanswered**. [Two-ASR comparison](../reports/BONUS_2020_01_ASR_COMPARISON_2026-10-22.md), **no audio verified** |
| [E080](../episodes/E080.md) | Continued engineering fight: Mirror Image, black-dragon Nash, red memory-eaters/green chain-exploding worms, animated pipes, **Eddie and Chance rescued from death saves**, commander killed, Eye of Groxl flame blade, starry-space transition and **unresolved Dolo Popio breath**; see the archived detailed queue |
| [E081](../episodes/E081.md) | **Arc conclusion:** Dolo breath spawns worms; Chance floats away unrecovered; Vorel binds dragon-worm mouth with nanoweave; **Hope kills Dolo with radiant dart**; Quizquaz offers to sacrifice Earth; Sira/Eddie released, **four protagonists enter red beam and GM explicitly declares them dead**, ultimate permanence open; see the archived detailed queue |
| **[E082](../episodes/E082.md)** | **Arc 3 in Sigil:** Vorel physically survives; **Eye of Groxl splits to save him**; Nash conscious in a floating heart/eyeball/finger; **Hope/Stanley bodies recovered**, Binch/Dustmen, newcomer vouchers, two unnamed new characters, cleric not visited. **ASR-only, no audio verification** |
| **[E083](../episodes/E083.md)** | **Arc 3 in Sigil:** **Squirts, Chunks and Nothing** identified; trickster priest uses a crystal to diagnose **Weir-associated petitioners** and accepts Hope/Stanley's bodies into crypts under **conditional ritual proposal**; Nash gains **mouth and hand**; Pelor factorum advises; **Vorel, Nash, Nothing register for BMF** and seek a strategy book. **No resurrection, match, bounty or prize. ASR-only** |
| **[E084](../episodes/E084.md)** | **Arc 3:** strategy-book theft and **nonlethally disabled halfling**, untested forgetfulness potion, **priest's match-rigging and sick-needle scheme**, further Nash regrowth, **Nothing privately commissioned for an Abyss-linked kidnapping (unperformed)**, magical screening and qualifiers: **Vorel/Nash win, Nothing double-forfeits**. **Two ASR pipelines** with important Godsmen/Guardsmen discrepancy; no audio verification. [E084 comparison](../reports/E084_ASR_COMPARISON_2026-10-22.md) |
| **[E085](../episodes/E085.md)** | **Royce BMF qualifier concludes**: GM narrates intermediate wins; Squirts **injects Ventro twice and Nash once (CON saved)**; **Vorel beats Nash**, then **defeats local champion Ventro**, earning **next-day larger finals place, not the 5,000-gp pool**. Ventro violently attacks; **Nash magic suppressed, Squirts magic works**; huge **green woman-shaped apparition removes Ventro (fate unknown)**. Mighty Squirts publicly claimed, **sponsors unsigned**, Nash/Nothing actually earn inn pay, party sleeps, **two armed intruders enter before fighting**. Two-ASR provisional. [E085 comparison](../reports/E085_ASR_COMPARISON_2026-10-22.md) |

**Publication crosswalk:** [Corrected episode numbering](EPISODE_NUMBERING.md). **Historical precision:** Detailed E055–E081 timestamps and every prior batch question are in the [full pre-second-arc queue snapshot](../research/legacy/2026-10-22/REVIEW_QUEUE_PRE_SECOND_ARC_CONSOLIDATION.md) (and older [Phase-D snapshot](../research/legacy/2026-10-22/PROJECT_REVIEW_QUEUE.md)). **Lore chronology:** [unified timeline](../world/CHRONOLOGY.md).

## 5. Priority listening — second arc E055–E081

This is a **triage queue**, not a complete record of every ASR timestamp. Dates and ranges below refer to **approximate position in the original recording**. The [episode dossiers](../episodes/) and [pre-consolidation full queue](../research/legacy/2026-10-22/REVIEW_QUEUE_PRE_SECOND_ARC_CONSOLIDATION.md) retain hundreds of exact questions. Mark an issue **audio-verified** only after actually listening; source-to-source agreement is not the same as listening.

### P0 — conclusions, irreversible-looking events and competing narrators

| Source window | What to verify by listening or original handout | Current safe editorial stance |
| --- | --- | --- |
| **[E081](../episodes/E081.md) ~01:33–01:41** | Hope's **fire-truck/radiant attack** that kills **Dolo Popio's manifested body**, GM's exact demonic permanence caveat, Chance's absence when arena resets | **Manifestation killed; immortal essence not proven ended. Chance missing, not certified dead** |
| **[E081](../episodes/E081.md) ~02:03–02:10, ~02:35–02:40** | **Eddie released** from central beam, **Sira's invisible exit and later visible farewell**, any condition or timing distinction | **Sira physically freed alive beside Eddie**; no demonstrated homecoming or later safety |
| **[E081](../episodes/E081.md) ~02:22–02:45** | **Stanley's Augury**, Quizquaz's described controls, Eddie operating them, **four protagonists' Constitution saves**, transformation and exact GM death statement | **All four enter, disperse, and are explicitly GM-declared dead at E081 cutoff**; their permanence, souls and Earth's state unseen |
| **[E080](../episodes/E080.md) ~01:54–02:04** | **Nash's acid breath killing commander**, Dolo's alleged contractual counterparty and **scene change into floating void** | Commander defeated; the contract name and literal nature of transportation **unverified** |
| **[E079](../episodes/E079.md) ~01:36–01:49, ~02:29–02:36** | Exact **Sira/dragon-worm/commander** placement, **both Hope rockets**, Cerinthala and illithids hitting beam | Physical chamber reached; **rockets spent**, three illithids and visible Cerinthala body disintegrate; **permanence uncertain** |
| **[E077](../episodes/E077.md) ~02:33–03:21** | **Hive council / Wall Nash identity and claims**, old-world GR0X1 connection, alleged future, 1-person Drive shutoff, GM level/rest instruction | Speakers appear, but **future claims not verified**; announced E077 repair/rest **actually performed E078** |
| **[E066](../episodes/E066.md) ~final half** | Distinct **Rorf and Follow deaths**, **Sira abduction**, illithid's actual allegiance/bargain, Fate 4 destruction | Two companions die and child kidnapped; speaker's infernal offer **not accepted** |
| **[E062](../episodes/E062.md)–[E064](../episodes/E064.md)** | **Hope's redirected rocket casualty names/count**, Zercil interference, Orp kill and council recognition, prisoners' partial release vs outbreak | **Great Fang achieved at high civilian cost**, full liberation and outbreak ending unshown |
| **[E059](../episodes/E059.md)** | **Principle extraction of Diontalus into crystal**, Dusthill captives arriving alive, exact terms of paid-labor / rail negotiation | Extraction and returnees observed, rail/political outcomes **not yet executed** |

### P1 — unusual mechanics, custody and source contradictions

| Source window | Specific issue to reconcile | Do not assume |
| --- | --- | --- |
| **[E075](../episodes/E075.md)–[E077](../episodes/E077.md)** | Single **portal gun** acquisition/custody; E076 actual escape, E077 **dual-trigger necrotic mode** and friendly fire | Distinct guns, invisible handoff or unlimited damage/charge |
| **[E076](../episodes/E076.md)–[E081](../episodes/E081.md)** | **Blue Bull and Monster Mender** counts, potion/poison interaction, **Hope's two rockets**, suit and harpoon parts | Doubling up E077's prospective repair and the performed E078 repair |
| **[E077](../episodes/E077.md) ~00:35–01:04 and ~01:03–02:30** | **GR0X1 and Lethanphius** vat labels, Eye's response, Vorel losing hand/digits, neutralization-beam damage to both | Proof every lizardfolk or Vorel's Eye was created in lab |
| **[E078](../episodes/E078.md) ~00:26–00:56** | **Actual hand reattachment** and eight-hour Tiny Hut rest, **20 laser swords/two bracer pairs/~11 kits**, two Rings of Spell Storing, loaded spells | E077 completed same healing/rest, exact bag weights without sheet |
| **[E079](../episodes/E079.md) ~00:12–01:36** | Stimulant consumption and vomiting, illithid-head disguise, **Stanley bringing Hope through Dimension Door**, portal pair bypassing hand lock | The handprint lock was actually unlocked |
| **[E080](../episodes/E080.md) ~00:34–01:54** | Stuns, Feather Fall, red memory penalty, green worm explosions, **magical laser swords rejected by Animate Objects** in favor of pipes, **gnome death saves** | Magical swords consumed, Eddie/Chance permanently dead in E080 |
| **[E081](../episodes/E081.md) ~00:20–01:25 and ~02:32–02:40** | **Vorel removes suit as mouth tie**, Hope leaves detachable horn, **Stanley heals Eddie**, **Eddie steals Bowie knife** | Items are automatically returned/kept by the four after disappearance |
| **[E070](../episodes/E070.md)–[E071](../episodes/E071.md)** | Whether the **VR upload actually affects physical Drive** and fate of snail-transformed security ape | Claimed Charles Dickens success equals independently measured sabotage |

### P2 — orthography, provenance and earlier unresolved stories

| Focus | Where to verify | Current rule |
| --- | --- | --- |
| **Names and lore** | [Discord spelling report](../reports/DISCORD_SPELLING_2026-10-21.md), creator handouts, E066–E081 audio: **Dolo Popio, Kervalon, Ovaxiad, Cerinthala, Kitobol Prith, Andreeste, Sira** | Distinguish provisional ASR and **owner-confirmed Eye of Groxl**; avoid inventing official variants |
| **Family and lost city** | [E063](../episodes/E063.md)–[E066](../episodes/E066.md), [E081](../episodes/E081.md): **Follow/Rorf/Sira**, Bramie confession, **Razak Val**, Omnom, surviving human prisoners | Sira is **freed E081**; full fate of Razak Val or sanctuary not shown |
| **Hope's court, survivors and politics** | [E055](../episodes/E055.md)–[E059](../episodes/E059.md) with contemporary notes and maps | Tietkalla reforms, returned survivors and actual railroad are **distinct events** |
| **Competing machine testimony** | [E067](../episodes/E067.md), [E070](../episodes/E070.md)–[E071](../episodes/E071.md), [E077](../episodes/E077.md)–[E081](../episodes/E081.md) | Spectral dragon, Charles Dickens, Alvert, hive, Wall Nash and Quizquaz **are not omniscient** |
| **2019 bonus date mismatch** | [November bonus](../episodes/BONUS-2019-11.md), original RSS/producer archive; also other six bonus date notes in full queue | Public-release month **not necessarily recording date**; November-named file has spoken October intro |
| **December 2019 bonus ASR divergence** | [Dossier](../episodes/BONUS-2019-12.md) · [four-export comparison](../reports/BONUS_2019_12_ASR_COMPARISON_2026-10-22.md), standard recording ~00:03–00:06, 00:15–00:19, 00:23–00:33 | **CHIDS/Cedus**, Soulbroker spelling, **Cerinthala-like elf name**, **Dolo/Andreeste**, **God Killer/Groxl**, scoutmaster/data-core custodian and Qwen-only outro tail. **No majority vote or verified omissions**; alternate audio adds ~1 minute of ads |
| **January 2020 bonus spoke December** | [January dossier](../episodes/BONUS-2020-01.md) · [two-source comparison](../reports/BONUS_2020_01_ASR_COMPARISON_2026-10-22.md), ~01:07 / 04:55 / 07:00 / 09:30 / 15:30 / 20:00 | Confirm **spoken “December 2019” vs public-release January**, **Ventro/Lady of Pain** retrospective naming, **Nash bodily restoration vs spell suppression**, **kenku curse ASR contradiction**, **Diontalus crystal vs Vorel's hypothetical space shot**. Do not count player future intentions as played events. |
| **Private records and mechanics** | Soulbroker contract, item/stat sheets, E045/E047 handouts, map revision register; see [editorial guide](EDITORIAL_GUIDE.md) | Do not reconstruct secret readings or exact custom stats from wiki or processed ASR alone |

## 5A. Arc 3 opening — E082–E085 priority audio review

**Related retrospective source:** [December 2019 Q&A](../episodes/BONUS-2019-12.md) discusses the same E081–E083 aftermath **after the sessions**, and its [two-model/four-file comparison](../reports/BONUS_2019_12_ASR_COMPARISON_2026-10-22.md) identifies places to listen. **Beau's explanations are not fresh E083 scenes.**

| Window | Check against audio/primary source | Editorial boundary |
| --- | --- | --- |
| **[E082](../episodes/E082.md) ~00:03–00:17** | Vorel's cosmic passage, **giant still head**, return to sewer and black speck; clarify any cosmological name | **Unidentified face**, no external-world elapsed-time measurement |
| **E082 ~00:17–00:38** | Nash heart/eye morphology, long rests, floating, and **Eye of Groxl rupture/protective membrane** | Owner-confirmed **Groxl**; distinguish heart-form Nash from destroyed Eye and prevent unsupported total restoration |
| **E082 ~00:47–01:15** | Hope/Stanley corpse recognition, missing prosthetics, **nonlethal vs lethal collector injuries**, Nash ram | **Both bodies found**, **no resurrection**, deaths/status not all interchangeable |
| **E082 ~01:15–01:41** | **Binch Lory, Jarver, Dead Book/Dustmen, 100 gp** and origins of Sigil / possible map details | Source character assertions vs observed payments/routes |
| **E082 ~01:41–02:05** | Curved Sigil landscape, Nash's new finger, clerk giving **Nash's name**, three days assistance and **50 Gums Road** | A **referral**, no demonstrated clerical intervention |
| **E082 ~02:05–02:32** | **Jon's kenku / Kristen's kobold** descriptions and any genuinely spoken personal names, **Bill, Pam, Soggy Feather**, Lady of Pain lore | New player characters are **not Hope/Stanley resurrections**; do not import Planescape inference |

| **[E083](../episodes/E083.md) ~00:08–00:18** | **Squirts, Chunks, Nothing**, new-PC descriptions and trickster deity's name; distinguish infant Chunks from another adult PC | Do not assign E082 character names retroactively to that recording's dialogue or confuse the new PCs with Hope/Stanley |
| **E083 ~00:26–00:48** | **Kidigree (?)**, crystal device and **Weir/Wyr** markings, **Far Realm** claim, Su(s)u, conditions of the humiliation bargain | Cleric's petitioner diagnosis and two crypted bodies are played; **no resurrection** and **no firm cosmology validated** |
| **E083 ~00:48–01:07** | Transfer of Hope/Stanley to crypts, church street disappearing, **Nash's two regrowth choices and resulting mouth/hand** | Not ordinary revival, not restored spellcasting; the church must not be automatically equated to the clerk's earlier **50 Gums Road** |
| **E083 ~01:07–01:38** | **Mereen, Frail, Belthuzad** names, Pelor factorum and claims about Lady of Pain; Vorel's refusal of hands-on intervention | No healing or employment completed; retain source-claim status for planar legal descriptions |
| **E083 ~02:03–02:57** | **BMF, Terrence, 76 Mulberry Lane, Royce Gymnasium**, registration IDs **142746–142748**, competitor names and strategy author **Kenja/Kanja/Conja** | No official team registration, no practice, no qualifying fight or prize, no acquired treatise at cutoff |

| **[E084](../episodes/E084.md) ~00:03–00:40** | Halfling reader theft, checked unconsciousness, **Kidigree's target and sick-sticks**, exact preliminary count, the forget-me drink's limitations | **Halfling is alive**; memory effects not confirmed; **bracket manipulation planned**, not all match changes demonstrated |
| **E084 ~01:02–01:10, ~01:23–01:35** | **Pelvis** and **“Ebon Skulker,” 47 Castamere/Castlemere Lane, Stevius Ronkly, “Godsmen” versus “Guardsmen,” 10 Belshamer Lane**, one-hour portal and seven-day deadline | **Actual private client/portal meeting**, but **no abduction/delivery**, no proof companions know; [two-model comparison](../reports/E084_ASR_COMPARISON_2026-10-22.md) |
| **E084 ~01:20–01:24, ~01:43–02:09** | Nash **second hand/forearm and foot**, magic item swallowing at gate, **Cloak of Shadows provisional ruling**, venue **Royce Colosseum/Gymnasium**, three characters and extra 4,000-gold announcement | **No full Nash body, spell or award.** Separate homebrew adjudication from source-text rules |
| **E084 ~02:08–02:49** | Vorel vs **Randorf** with observed **needle injection**, Nash vs **Farfrid/Farcred**, Nothing vs **Bockip/Bakit**; precisely identify winners and double forfeit | **Vorel/Nash win first qualifiers**, **Nothing/kenku rival both time out**. No champion encounter or prize |

| **E085 ~00:03–00:39** | Distinguish **Ventro (Royce local)** vs **Kanja (overall)**, confirm priest/champion names, **2 Ventro injections**, **Nash injected but CON save** | GM narrates intermediate rounds; not all sabotages individually shown; Nash not poisoned |
| **E085 ~00:40–01:19** | **Vorel defeats Nash**, then **Ventro** in actual marionette games; local title vs next day's **Great Colosseum finals**; award vs **5,000-gp advertised pool** | **No overall title/prize**, Squirts' role in earlier rounds does not imply fixed final game damage |
| **E085 ~01:20–01:49** | Nash's three spells **externally suppressed**, Squirts magic succeeds; woman-shaped **green apparition**, **Ventro vanishes through pinhole** | **Do not identify as literal Lady of Pain, verify enforcement effects and survival against audio** |
| **E085 ~01:49–02:26** | **Mighty Squirts media claim**, **200/500 gp sponsor offers unsigned**, returned/stolen strategy book to lizardfolk admirer, inn wages/tips vs GM's **20-gp wallet contradiction**, Squirts loot | No signed sponsorship, tournament prize or verified elixir effect |
| **E085 ~02:28–02:45** | Vorel escapes intrusive fans via burning curtain and broken window; Nothing's warning sword and **two ninja-like room intruders** at cutoff | **No attacker identity, attempted-hit results or connection to Pelvis established** |

**Next slice:** Research corrected [E086](../sources/The%20Wastes%20S1E086.%20Don%27t%20be%20such%20a%20Berk.parakeet.processed.srt) independently once its exact source filename is verified. **No listening verification was performed for E085.**

## 6. Arc coverage and previous detailed questions

The **research coverage register in section 4** records every source reviewed. The earlier **13 episode-specific E055–E081 review sections (formerly sections 5–17)** were **not silently dropped**: all their timestamps, proposed spellings, named casualties, puzzle rules, inventory arithmetic and character-source caveats are retained in the [frozen full queue](../research/legacy/2026-10-22/REVIEW_QUEUE_PRE_SECOND_ARC_CONSOLIDATION.md). The [CHIDS consolidation audit](../reports/CHIDS_ARC_CONSOLIDATION_2026-10-22.md) and [current consistency ledger](../world/CONSISTENCY_LEDGER.md) explain how open source-era claims become closed at later cutoffs.

For future research, start at the **highest-priority applicable row**, open the corresponding episode dossier and the archived precise question, then **listen to the recording**, update only the affected canonical subject page and active ledger row, and cite what was checked. Do not mark the whole arc as audio-verified merely because it has been researched, consolidated and linted.

## 7. Work completion checklist

- [ ] Listen to and independently validate story-critical ASR windows; record timestamps and speaker attribution.
- [ ] Reconcile original campaign contracts, special item handouts, episode-era maps and character sheets; preserve uncertainty when absent.
- [ ] Revise a narrow **episode dossier + canonical profile + current ledger topic row** for each corroborated correction.
- [ ] Preserve **raw source SRT files** and both generations of archived research; never silently overwrite recognition.
- [ ] Validate Markdown links, headings and tables; run applicable source/document checks after edits.
- [ ] Research **E086 onward** in separate bounded batches; **E082–E085 are provisionally documented but still need listening**. E084 has **Parakeet and Qwen inter-ASR disagreement documented**, not audio-verified. All indexed 2019 bonuses and the **January 2020 bonus dual-export comparison** likewise remain ASR-based. Verify high-impact disagreement candidates before claiming canonical utterances.

**Consolidation is not verification.** The active questions are intentionally shorter than the archives they replace.
