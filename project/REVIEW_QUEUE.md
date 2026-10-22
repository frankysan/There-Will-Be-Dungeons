# Year One — active audio, source and editorial review queue

**Status: OPEN tasks, as of 2026-10-22.** Full *Wastes* spoilers through corrected E054 and the separate [March 2019 Q&A](../episodes/BONUS-2019-03.md). **No new listening, SRT editing or handout verification occurred during consolidation.** The [consistency ledger](../world/CONSISTENCY_LEDGER.md) identifies **what remains uncertain versus resolved**. This queue tells reviewers **where to listen or which sources to compare**.

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

**Publication crosswalk:** [Corrected episode numbering](EPISODE_NUMBERING.md). **Historical precision:** Timestamps and named questions for every group are in the frozen [full review queue](../research/legacy/2026-10-22/PROJECT_REVIEW_QUEUE.md). **Lore chronology:** [unified timeline](../world/CHRONOLOGY.md).

## 5. Work completion checklist

- [ ] Listen to selected critical cues and create **audio-grounded transcript excerpts** with timestamps and performer attribution.
- [ ] Reconcile original contracts, house records and item handouts with spoken claims; if unavailable, record that explicitly.
- [ ] Update only the affected **active ledger key**, source dossier and consolidated reference entry, with evidence and date.
- [ ] Preserve raw SRT outputs and historical archived alternatives, never silently overwrite source recognition.
- [ ] Run relevant documentary/index validation after edits; where **local files or code** change, run their applicable test suites and pass before claiming completion.
- [ ] Continue episodic review after E054; the **Q&A is a bonus** and E055 is a new main-session file, not automatically examined during this Phase D cleanup.

**Editorial consolidation is not audio verification.** Full [legacy queue](../research/legacy/2026-10-22/PROJECT_REVIEW_QUEUE.md) remains available for every fine-grained pending subtask.
