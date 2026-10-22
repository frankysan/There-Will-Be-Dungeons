# The Wastes — active audio, source and editorial review queue

**Status: OPEN tasks, updated 2026-10-22.** Full *Wastes* spoilers through corrected **E067**, with separate [March 2019 Q&A](../episodes/BONUS-2019-03.md), [April 2019 roundtable](../episodes/BONUS-2019-04.md), [June 2019 Q&A](../episodes/BONUS-2019-06.md) and [July-archived 2019 bonus](../episodes/BONUS-2019-07.md). **No new listening, SRT editing or handout verification occurred during consolidation.** The [consistency ledger](../world/CONSISTENCY_LEDGER.md) identifies **what remains uncertain versus resolved**. This queue tells reviewers **where to listen or which sources to compare**.

**Complete historical backlog preserved:** The entire ~73k-character pre-Phase-D [review queue, including its many timed episode-by-episode tasks](../research/legacy/2026-10-22/PROJECT_REVIEW_QUEUE.md), is frozen with functioning relative links. Its outstanding tasks were **not automatically closed** by omission from this shorter index. The original [consistency issue register](../research/legacy/2026-10-22/WORLD_CONSISTENCY_LEDGER.md) also preserves exact issue keys and status history.

## Priority and reporting

**Critical:** May change a death/survival outcome, main character identity, episode numbering, world-history truth level or legal/source rights. **High:** May affect important name, item, mechanics, political relationship, speaker identity or chronology. **Medium:** Detailed atmospheric wording, minor NPC aliases, maps or inventory whose ambiguity does not yet change a major conclusion. Avoid making all 1,000+ hours of audio a single unactionable “listen later” item.

When a review is completed, record **episode + absolute recording time/cue IDs**, exact source file/recording, **who listened or inspected the handout**, date, old/new wording or interpretation, whether audio truly verified it, changed documents and relevant test results. A different ASR model, wiki, cast-written spelling, old owner notes and a fan image are **not all the same evidence tier**. Only close the bounded task actually tested.

## 1. Pilot ASR transcription and diarization

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

## 2. Story-critical Year One listening and primary-handout review

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
| [BONUS-2019-04](../episodes/BONUS-2019-04.md) | Roundtable on early Year Two, character technique and GM's emergent Tietkalla design |
| [BONUS-2019-06](../episodes/BONUS-2019-06.md) | May-spoken/June-archived bonus; Stanley/Nash/Vorel/Hope goals, Principle origin, unused encounters and sand-fishing design |

**Publication crosswalk:** [Corrected episode numbering](EPISODE_NUMBERING.md). **Historical precision:** Timestamps and named questions for every group are in the frozen [full review queue](../research/legacy/2026-10-22/PROJECT_REVIEW_QUEUE.md). **Lore chronology:** [unified timeline](../world/CHRONOLOGY.md).

## 5. E055–E056 and April/June 2019 bonuses — focused checks

| Priority | Source time | What to review, and how to represent it |
|---|---|---|
| **Critical** | E055 ~00:04–00:22 | **Three months actually elapsed**, level-seven confirmation, Hope policy outcomes and Nash's **nightmare**. Confirm **Angelashi's pregnancy announcement is waking/in-fiction**, not part of the nightmare death. |
| **High** | E055 ~00:22–00:35 | Court **merit/houseless/Guzbucks rules**, disputing houses, engineer **resource shortage**, status of repaired walls/fleet and church. Verify **which reforms completed vs announced**, exact names. |
| **Critical** | E055 ~00:34–00:49 | **Carnage captured and ordered executed**, gnome **Softhead** returns as Principle envoy, **claimed release of Dusthill captives** and Ethanalia responsibility; **Hope has his tongue cut out while alive**. Check whether order/execution actually shown, envoy departure and exact name/title. |
| **High** | E055 ~00:54–01:12 | **Bedroom assassin**, repeated `Dollo Poppio` name, poison/radiant ammunition, Hope's wounds and guard killing. **Don't infer demon identity/employer solely from shouted name.** |
| **High** | E055 ~01:12–02:14 | **Golden Sands / Pillars of Decency**, Bok Bok duties, regional **merchant Joderty Strongnee/Diamond Stroke**, Esophageal Pass, Mogen Frogan, dwarven ruins and Principal City's **three spires**. Compare with contemporary **Roll20 map revision**. |
| **High** | E055 ~02:14–02:51 | Group's reaction to **demon-intrigue lore**, racially prejudiced tavern fight, **cometlike object** and falling stones. Do not assign confirmed culprit based on E056 NPC claims. |
| **Critical** | E056 ~00:06–01:03 | **Direct civilian casualties** including an endangered family/child, evacuation to manholes, identities of **Fibel**, **Tombo** and surviving bystanders, separate Hope's keep route. Avoid unsupported all-safe conclusion. |
| **High** | E056 ~01:03–01:20 | Ancient laboratory and **animated `47/49 Carnage`**. Reconcile E055 captive/execution vs E056 zombie identity; **Nobiery's ritual circle and restrictions**. |
| **Critical** | E056 ~01:18–02:07 | **George ghost** hostile/aged Vorel and dispersed by Nash, **Martha apparition** repelled, **P0D spirit**, Hope's ancestral tests and **Quizquaz** offer. Distinguish **spirit from revival**, witnessed ethereal scene from **interested claims**. |
| **Critical** | E056 ~01:57–02:07 | Exact **Andreeste, Dollo Poppio, Grim Council, dragon destroyed on entry** wording. Record all as **Quizquaz's asserted story** pending separate confirmation; Hope rejects **Melgor + fifty souls** offer. |
| **High** | E056 ~02:09–02:34 | Vorel **ages and is restored before ending**, Eye of Groxl's control contest, priestess `Emenil/Eminel`, diamond reagent/Greater Restoration and Stanley's **Fishbird created water**. |
| **Critical** | E056 ~02:33–02:42 and E057 ~00:08–00:19 | **Nobiery exposes demonic bargains**, threatens priestess, and a **Carnage bite lands in E057**. **Stanley heals her, Hope halts the zombies; Emenil alive at E058**. Verify precise cues, not the stale E056 cliffhanger death question. |
| **High** | Bonus April ~00:00–00:09 | **Diontalus switching on sleep**, dormant status, **Stanley's covert research through hospital/medical library**, Nash's choice not to interfere. **Player-retrospective explanations**, not a performed separation. |
| **High** | Bonus April ~00:09–00:14 | GM intended brief **Tietkalla 2 town / 3–4 keep episodes**, emergent royal history, **Mogen Frogan** production inspiration. Never retroactively assert a gnome city as real Tietkalla history. |
| **Medium** | Bonus April ~00:14–00:30 | Performer-versus-character choices: Jon's moral difficulty with Diontalus, Scott's dirty Nash, Kyle's Vorel vocabulary/Bok Bok, Kristen's emotional roleplay; **Waterworld** alternate-setting question is hypothetical. |
| **High** | Bonus June ~00:00–00:02:43 | Confirm **spoken May versus archived June** and timing/distribution; identify the **Leopold lab staff** and whether later passage supplies name/powers. Distinguish it from Stanley's **Immovable Rod**. [Dossier](../episodes/BONUS-2019-06.md) |
| **High** | Bonus June ~00:02:43–00:07:05, ~00:16:28, ~00:19:29–00:21:51 | Validate **Jon's Stanley guilt/atonement and Principle/slavery reservations**, **Scott's Nash “of the Solar Mines”**, **Kristen's god-destruction endgame**; these are **player interpretations and intended arcs**, not new played scenes. |
| **High** | Bonus June ~00:18:10–00:19:29, ~00:21:51–00:23:36 | Verify GM's **Principle >1,000 years/pre-Scorching/lich insufficiency** and **sand squid/shark/podcasting** context; **unused parodic fisherman and Mold Earth vehicle chase** are not direct encounters. |
| **High** | Whole archive | Reconcile corrected **E055/E056** against original publisher **56/57**, and the April/June bonus **title/date labels**. Spoken May/April dates are not independent distribution-date verification. |

**Every earlier Year One review subtask remains available** in [historic queue](../research/legacy/2026-10-22/PROJECT_REVIEW_QUEUE.md) and current categories above; the new episode section is an **active extension**, not a new separate append-only encyclopedia.

## 6. E057–E060 — newly opened focused checks

| Priority | Approximate episode time | Specific validation task and evidence tier |
|---|---|---|
| **Critical** | E057 ~00:08–00:30 | **Emenil bite, Stanley's healing, Hope stopping the zombies**; Nobiery's **admission of Soulbroker preservation and Matamaru cover story**. Distinguish admissions, his older sacrifice account and verified mechanics. |
| **High** | E057 ~00:40–01:25 | **Royal monster truck vs Fate 4**, crater stones/plant growth, **bugbear-size tracks dragging object onto vehicle**, any evidence independently identifying a dragon. The crater may follow E055/E056 storm without proving Quizquaz's account. |
| **High** | E057 ~01:23–02:08 | `Coopen/Coupon` lucky leprechaun, **Diontalus killing and magical feeding**, **Lucky Coin in Hope's possession**. Verify exact item effects from character sheet rather than only GM-recited one-charge mechanic. |
| **High** | E057 ~02:05–end / E058 ~00:08–01:12 | Winged pet **killed E057** (Stanley), **remaining bugbears E058**, worm in bugbear brain and **Dollo Poppio/Wormfather connection**. Audit which mage escapes and which fighters/worms actually die. |
| **High** | E058 ~01:30–01:50 | Actual **banana trail**, Nash's dragon expiry and **royal search pickup**. Do not claim unplayed two-day walk or an indefinitely missing Nash. |
| **High** | E058 ~02:10–end | **Principle appearance**/ten rings and blue-etched body, names/titles for **Steel God, Jesus Chrome, Ethanelia, Buttons and Relium Vanch**; what was only **offered** rather than completed. |
| **Critical** | E059 ~00:00–01:02 | **Paid voluntary railway labor**, treaty/embassy/prayer building terms, **Augury woe**, **Diontalus physically extracted into crystal** and taken by Principle. No space launch observed; check alleged **New York** destruction is ruler claim. |
| **Critical** | E059 ~01:23–01:53 | **Dusthill survivors physically return**: Talia, child Bruce Bane, Jimster, Shun'ti and other people; alleged death/raid names, **Salivating Fields forced labor**, all surviving vs absent. Hospital checks not all proved complete. |
| **High** | E059 ~01:50–end | **Fate 4** plus lizard mounts to **Razak Val**, bloodsucker storm and Tiny Hut, **Orp** Great Fang and shackled captives, observed killing. |
| **Critical** | E060 ~00:20–00:37 | **Formal scaling challenge**, **Orp directly kills Diptak by critical blow**, and remove Diptak from active-living indexes. |
| **High** | E060 ~00:37–02:14 | Razak Val settlement/map names, **Mirion**, **Fengar**, **Council of Twelve**, **Typalla/Fuxi**, **Bramie/Zercil**, **Toxar/Skrot**, **Demon Vold** and number of clans; distinguish dynastic testimony from concrete politics. |
| **Critical** | E060 ~02:08–end | **Orp agrees sunrise duel without having fought it**, banquet snake/chicken lord details. **Scarless red-eyed Nash-like figure claims future identity in isolated private scene**; don't retroactively give that knowledge to the other PCs. |
| **High** | Episode and sheet reconciliation | Confirm **Coopen Lucky Coin** custody/recharge, **Diontalus crystal** custody, **Eye of Groxl** owner-confirmed single identity, **Diptak corpse** and court-level **Fate 4 vs monster truck** equipment. |
| **High** | All 4 source files | Validate **E057–E060** corrected names and story-time offsets; check SRT cues vs original audio for disputed unusual words and narrator-voice clustering. Comparisons of ASR runs alone are not audio verification. |

**Status corrections:** E056 Emenil cliffhanger **resolved by E057**, E058 prisoner-release promise **resolved as actual named return E059** (not whole population), and E059 Diptak **alive** changes to **dead E060**. These are **provisional processed-source cutoffs** and still warrant targeted listening.

## 7. E061–E063 — Great Fang succession, mysteries and humanitarian consequences

| Priority | Source / approximate recording time | Specific verification and evidence boundary |
|---|---|---|
| **Critical** | E061 ~00:05–00:25, ~01:03–01:14, ~02:50–02:56 | **Apparent future-Nash identity**, time-barf explanation, egg request, **Knock**, Nash's **Sleep** on guards, **Bramie alive after theft** and conditions of Nash's secrecy/confession. Do not upgrade alleged time travel to a physical fact or merge **theft** with **murder**. |
| **Critical** | E061 ~01:30–02:14, E062 ~00:08–00:35 | **Tyrant's Bane in Bramie's back**, three identical footprints plus separate lizard tracks, guard testimony, and Vorel's **appointed sheriff** role. **Killer unconfirmed as of E063**; **Rorf confesses E065**, superseding Vorel's suspicion of Zercil. See E065 review below. Check preserved **Fengar egg** ownership/powers as oral prophecy, not a verified magic item sheet. |
| **High** | E061 ~00:25–01:03 | Exact **Vorel Rasvim Kurik**, family god-killer vs **Eye of Groxl**, **Closthi/Telestar** legend, Zark envoy (**Kervalon/Demon Vold/Dollo Poppio**) and Hope's proposed Tietkalla support. Distinguish clan religious/historical claims from actual meetings or deployment. |
| **Critical** | E062 ~00:35–00:48, ~01:11–01:32 | **Zercil's proposed marriage/subordinate succession** and Vorel's refusal; abrupt transition from **planned sunrise scaling** to actual fight; whether **Mawstorm sword is absent** and **Eye of Groxl flaming shield** used. Distinguish self-bestowed vs externally conferred titles in [Vorel register](../world/characters/vorel.md). |
| **Critical** | E062 ~01:32–02:13 | **One-use Hope rocket redirects onto Vorel via Eye of Groxl**, 60-foot blast, exact **Mirion, Typalla, Elder, Toxar, Seeman Featherscale, Mola Janda** fatality rolls and **Omnom/Yomi/guard/drummer survivors**. Avoid assuming 30–40 equals audited total or no innocent victims. |
| **Critical** | E062 ~02:13–02:34, E063 ~00:08–00:31 | **Vorel kills Orp with Eye shield**, publicly acclaimed Great Fang E062. **Zercil alive at E062 cutoff**, tries E063 leadership gift/transfer but crowd chooses Vorel. Confirm exact **formal recognition vs self-awarded titles** and who witnesses it. |
| **Critical** | E063 ~00:29–01:18 | **Stanley's hidden Healing Word**, Nash dragon/bowing crowd, **Vorel's worm-behind-eyes observation**, **nonlethal intent vs Hope's lethal Obsidian Nail**, lucky coin charge, witnessed dishonorable interference and crowd's renewed acclaim. **Zercil is actually dead E063**. |
| **High** | E063 ~01:17–01:34 | **Private young disappearing human girl** (Stanley only), **Necklace of Fireballs with five beads physically recovered** from Orp, not merely proposed; corpse harvesting/role of Vorel's meat blessing. |
| **Critical** | E063 ~01:35–02:15, ~02:30–02:53 | **200–300 starving humans in man's pit**, sun-witness claims/language, **planned freedom vs completed transport**, Nash's improvised exam rooms, and Stanley's **Follow/Follo** examination, distinct temporary confinement, possible supernatural impression. **No verified identity reveal/parasite in Follow**. |
| **High** | E063 ~02:15–02:30 | **Live black worm captured from Zercil's bed**, method/host status unknown; **three surviving Fengar children including Felcha** learn both parents died; exact family relations and guards' exposure must be checked. |
| **High** | E061–E063 / item and clan sheets | Verify **Bramie/Baymie**, **Zercil**, **Mola Janda/Yomi Zantlar**, **Kervalon**, **Demon Vold**, **Follow**, **Tyrant's Bane**, remaining Lucky Coin use, **Mawstorm** creator spelling and **Eye of Groxl** combat effects against original audio/handouts. No direct edit to source SRTs. |

**Status/cutoffs as of E063:** **Orp alive E060 → dead E062; Zercil challenger E061/E062 → dead E063; Vorel publicly recognized Great Fang E062**. **Bramie's murder was not solved by E063**, but an admitted culprit appears **E065**; promised emancipation is overwhelmed by **E064's catastrophe**. New dossier prose is processed-ASR research, not audio-verified.

## 8. E064–E065 and July-archived 2019 bonus — fresh listening queue

| Priority | Source / approximate recording time | Evidence and validation target |
|---|---|---|
| **Critical** | E064 ~00:20–01:15 | **Follow's telepathy**, mental identification of the singled-out Sun's Witness, prisoner's **Dollo Poppio-triggered mutation**, worm spray and party saves, Vorel's fire cleansing. Check whether **every** captive is shown changing, what the party knows, and that **Stanley did not detect a worm in regular exam**. |
| **Critical** | E064 ~01:10–01:29 | **Chicken-lord transformations, Nash's Fireball and Mold Earth**, **six-armed lizardfolk**, departure from Razak Val, and Omnom's **ongoing living status**. Track **Necklace of Fireballs transferred to Omnom** and **survival unknown**, rather than treating him as killed. |
| **High** | E064 ~00:37–00:43, ~02:34–02:38 | Guard assertion that **Zarks delivered Sun's Witnesses**, party's suspicion of deliberate taint, and GM's out-of-character clarification that **Orp's infected flesh** explains the spread (not that all Demon Vold cuisine is universally infected). Verify actual causation where possible, not guilt by association. |
| **High** | E064 ~01:26–02:00 | **Mawstorm as new raptor name versus sword**, mounted escape, Scully's Obsidian Nail usage, *Dimension Door* with raptor, collapsed bridge and number of monster fatalities. **Do not invent a new Vorel self-title** from vows to return as existing Great Fang. |
| **High** | E064 ~02:40–02:57 | **Fate 4 reappearance and post-credit scene are played events**; Follow, apparently invisible young daughter and orc **hotwire/drive party RV**, with no ownership transfer. Confirm earliest names and exact status of car fittings. |
| **Critical** | E065 ~00:08–00:33 | **Follow/Follo, Sira/Sera, Rorf** exact orthography and abilities (mind-reading/influence, invisibility, shapeshifting); lost settlement **Home**, survivor status, Sira's cropped ears and Elvish comprehension. Attribute difficult historical claims to **Follow**, not neutral narrator. |
| **Critical** | E065 ~00:22–00:27 | **Rorf explicitly confesses killing Bramie** and Follow says they deliberately removed elder heirs to create scaling opportunities. Reclassify the E061–E063 murder uncertainty at **E065 cutoff**. **Nash stole the egg but did not perform the confessed killing; Zercil's earlier accusation was unsupported**. |
| **High** | E065 ~00:34–00:43, ~01:43–01:49 | Hope's **Tietkalla asylum offer** and Follow's acceptance **in principle**, no completed arrival; Stanley's **Elvish song for Sira** and private Tietkalla **sending-stone report** (Principle's workers not yet arrived). |
| **High** | E065 ~00:43–01:38 | Rare **rain over purple sands**, Hope driving Fate 4, Nash's *Mold Earth* freeing rear wheels and building a storm-drainage basin, Stanley's **Augury weal-and-woe**, and distant silhouette. Avoid extrapolating map scale or general spell legality from a session ruling. |
| **Critical** | E065 ~02:04–02:30 | **Three/four apparent Nash variants and two Fengar egg copies**, contradictory **egg/leg** explanation, alleged **winged employer** and planet explosion. Verify exact egg **handoffs** and item count, keeping **time travel unverified**. |
| **High** | E065 ~02:30–02:38 | **T. rex approaches RV** in driving rain, Vorel camouflaged underneath. Cliffhanger **ends before combat**, car is not destroyed. |
| **High** | Bonus 2019-07 ~00:00–00:03 | **Archive July vs spoken June bonus**, Scott's **June 29, 2019 recording-date claim**, 1,000-day **Catoblepraithe** pact with only approximate **80–90% remaining**, no reliable exact calendar. |
| **High** | Bonus 2019-07 ~00:03–00:21 | Jon/Scott/Kyle's **roleplay reasoning**, Kyle's **Tyrant's Bane rejection**, Omnom's character-design purpose, **Stanley cleric and Vorel paladin multiclass ideas not taken**; no retrospective in-world inventory changes. |
| **High** | Bonus 2019-07 ~00:21–00:26 | Beau's **Dollo Poppio Lord of Madness** and intended Orp corruption, tentative **nonidentity of Sira and Nash's Solar Mines dream-girl**, and acknowledgement **Hope's rocket changed preparation**. Separate creator intention from witnessed mechanics. |

**Source cutoff correction:** **E064** depicts the Razak Val mass outbreak; **E065** identifies **Rorf as confessed Bramie killer**; **Omnom and the valley's future remain unknown**. The July-archived bonus is **separate retroactive commentary**, not a playable E066. All conclusions are provisional ASR research.

## 9. E066–E067 — audio, handout and consequence checks

| Priority | Source / approximate time | Precise review target and status boundary |
|---|---|---|
| **Critical** | E066 ~00:08–00:33 | **T. rex crushes Fate 4 and wreck explodes later**; Nash's **deep storm-pit** and Fireball, **Vorel's Eye of Groxl shield kill**, exact timing vs any repair proposal. Verify **Fate 4 definitively destroyed** and **Fang Fate Five** is only a bone/cart salvage effort. |
| **High** | E066 ~00:33–00:46, ~01:40–01:55 | Vorel crafts **T. rex tooth dagger**, assembles wheel/bone **Fang Fate Five** rickshaw, and later leaves it rather than physically passing through dense black trees. **Does not replace Mawstorm sword**. Verify whether his "Fang" phrases use **existing Great Fang office** or an **additional self-bestowed title**; update [register](../world/characters/vorel.md) with literal wording if confirmed. |
| **Critical** | E066 ~00:50–01:17 | Exact **mind flayer's name** (`Oubvayx/Ovaxiad` ASR), **Dollo Poppio / wizened wyrm titles**, supposed **Andreeste/Catoblepraithe/Principle arrangement**, **Hope's refusal**, **Sira held in the air**, immune/pass-through Scully Puckle round and resisted *Command*. **Enemy speech is a proposed bargain, not a verified contract**. |
| **Critical** | E066 ~01:13–01:23 | **Rorf shapeshifts into bird and is folded/crushed to death**, **Follow thrown down, dies following Stanley's rescue promise**, and **Sira abducted alive**. Verify all three distinct life statuses before adding later characters. **No completed asylum in Tietkalla**. |
| **High** | E066 ~01:17–01:42 | **Eyeball forest generation**, apparent living/suffering eyes, Nash's acid attack and test lick (possible bug ingested **but no diagnosed infection**), **Stanley's mouse polymorph on Nash**, subsequent rest and persistent unnatural darkness and storm. |
| **High** | E066 ~01:55–02:33 | Skeleton-like crew's **Sgt T'Lupa, Commander Piker, Ensign Broccoli**, their **Bosen Seven/Rigel Five** story, scans and Earth disagreement, alleged **warp-drive coil handoff**, green spectral **wheel-less carriage**. Confirm equipment custodian and differentiate *speaker's claims* from objective cosmic travel. |
| **Critical** | E067 ~00:09–00:37 | **Hope's subjective Dusthill Jimster/Fate 4 memory**, then the **spectral starfield dragon encounter** shared by group; verify **Kazdejira/Kazdeshira**, *god killer Grojil* statement, dragon's alleged death, **planet-moving machine**, **other-realm incursion**, Dollo Poppio embodiment through Sira and limited lifespan of spirit. No second Eye of Groxl item. |
| **High** | E067 ~00:44–01:21 | Precise difference between **hypothetical T. rex polymorph, Dimension Door dragon entry, Greater Invisibility and stealth** vs **Nash's actual Mold Earth tunneling**. OOC correction of **Nash's spell sheet/feat** and **Tiny Hut rules** must not be backdated as character action or official mechanical clarification. |
| **Critical** | E067 ~01:22–01:40 | **Nash/Hope 20-foot-deep approach beneath ruin**, wall/foundation excavation adjudication, temporary sighting of unused chamber, later tunnel sealing (air pipe) and **four PCs' entry**. Check actual map scale vs narrative, do not declare a surveyed structure. |
| **High** | E067 ~01:40–02:27 | **Flesh-and-bone giant spawns successive skeletons**, **Stanley's Diplomacy killing blow**, Scully **radiant ammunition**, Nash's **Minor Illusion**, **Ray of Frost** and **Fireball**, Vorel **Eye-shield attacks**, and total minion elimination within room—not the entire keep. |
| **Critical** | E067 ~02:27–end | Guarded corridors and **Hope's spotting rifle-carrying lizardfolk concealed at corner**; no battle with that guard, machine reached, Sira freed or Dollo Poppio defeated in episode. |
| **High** | Name/source handouts | Search for original spellings of **Kervalon/Kaer Valon**, mind flayer **Oubvayx**, dragon **Kazdejira**, **Sergeant T'Lupa**, and name **Fang Fate Five** in cast documents / independent audio. Preserve **Mawstorm** provisional and **Eye of Groxl** owner confirmed. |

**E067 checkpoint:** **Fate 4, Follow and Rorf are lost in E066; Sira is alive when abducted and still missing**. The **spectral dragon's planet-moving machine** remains unverified testimony; the party **is actually below Kervalon**, not at the climax of the machine. Audio/cast-written verification not performed.

## 10. Work completion checklist

- [ ] Listen to selected critical cues and create **audio-grounded transcript excerpts** with timestamps and performer attribution.
- [ ] Reconcile original contracts, house records and item handouts with spoken claims; if unavailable, record that explicitly.
- [ ] Update only the affected **active ledger key**, source dossier and consolidated reference entry, with evidence and date.
- [ ] Preserve raw SRT outputs and historical archived alternatives, never silently overwrite source recognition.
- [ ] Run relevant documentary/index validation after edits; where **local files or code** change, run their applicable test suites and pass before claiming completion.
- [ ] Continue source-backed review **after E067**; E055–E067 and all four currently reviewed 2019 bonus recordings have provisional dossiers, **not independently listened/verified**.

**Editorial consolidation is not audio verification.** Full [legacy queue](../research/legacy/2026-10-22/PROJECT_REVIEW_QUEUE.md) remains available for every fine-grained pending subtask.
