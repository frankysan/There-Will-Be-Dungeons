# Review queue — pilot

These are **outstanding checks**, not completed corrections. References give approximate positions in the original episode audio.

**Generated queue available:** run the [multi-pass comparison](../reports/MULTIPASS_PIPELINE.md)
to obtain `comparison.md`, detailed `comparison.json`, `jobs.json` and a separate
decision ledger. The [pilot report](../reports/MULTIPASS_PILOT_2026-10-21.md) records
counts and representative candidate IDs. Generated records are hypotheses, not
resolutions of the listening tasks below. Nearby records may overlap and several
run pairs may flag the same speech; review consolidated audio jobs to reduce
duplicate work. Untimed records remain in a separate unlocated-job list.

First generated-queue listening targets: opening `no m h` / greeting, the extra
Qwen `Oops` near 00:22, greetings around 01:40, the padded-VAD `if if` at
03:08.510–03:08.760, and chunk overruns beyond 10:00. No new audio verification
or canonical correction was performed by this comparison run.

| Priority | Episode / time | Concern | Suggested action |
|---|---|---|---|
| High | E000 00:13:07–00:13:28 | “Now” is the last word; processed Parakeet cue is placed at 13:20–13:28 while raw ends by 13:11 | Retimestamp final word from audio; exclude musical tail |
| High | E001 00:00–00:13 | Baseline/chunked Parakeet recognize `no m h` in intro; default VAD misses `hello everybody` while baseline and padded VAD capture it | Listen for genuine speech versus music/noise; verify opening greeting |
| High | E001 01:23–01:42 | Five Parakeet runs disagree on short conversational speech; chunked runs substitute `i guess` for other runs' greetings to Kyle; turning LCS dedup off changes nothing | Verify turn-by-turn dialogue and overlap against original audio |
| High | E001 02:17–03:08 | Variants differ in `yeah`, `you're sweating`, `armpit`, `finality`; 700 ms VAD duplicates near-simultaneous `if` | Listen and build a verified transcription regression sample |
| Medium | E001 04:13–08:45 | Variants disagree around reactions, false starts and the Dusthill setting narration; `Dusill` and concatenated words recur | Compare audio and external spelling references without overwriting raw output |
| Medium | E001 10:00 boundary | Both 30 s chunked runs timestamp their final word to 10:00.800, beyond the requested 600 s window | Check chunk-alignment timestamp clamping |
| High | E001 00:47:00–00:48:00 | Listener-confirmed Cohere omission; Parakeet/Qwen cover more speech | Verify Parakeet wording against audio; add passage to ASR regression suite |
| High | E001 01:55:00–01:56:00 | Second listener-confirmed Cohere omission | Verify Parakeet wording against audio; add regression sample |
| High | E001 throughout, notably 00:58, 01:17 and 02:31 | Sixth diarization cluster is Scott doing a voice | Check short boundaries; use `Scott` in final draft but preserve cue provenance |
| High | E000 00:03:49–00:07:18; E001 01:09 | Nash family name transcribed Maggard/Magard/Maghard | Wiki spelling **Nash Maggard** documented; verify individual audio wording |
| High | E000 00:11:41–00:13:11 | Vorel name and longer name; Verithica/Caegro uncertain | Wiki confirms written **Vorel Rasvim Kurik**; listen to introduction for phonetics and other geographic names |
| Medium | E001 00:15:31–00:15:43 | Tiefling's personal name Orifi/Orify uncertain; “Hope” confirmed as desired name | Wiki supports **Oriphi “Hope” Akmenos**; retain original ASR naming exchange until listening review |
| Medium | E001 00:18:03 and 00:41:27 | Gimster/Gymster; Shun T and related spellings | Later-episode wiki summary supports **Jimster** and **Shun'ti Stoutbarrel**; verify early audio and avoid retroactive surname insertion |
| Medium | E001 00:16:13 and 00:42:15–00:42:44 | Tavern mentioned in player dialogue; DM later states there is no tavern | Treat as discrepancy/scene revision; do not canonize a tavern |
| Medium | E001 03:01–03:02 | Dramatic ending includes a gun, light, a skull wall; precise actor and actions require careful review | Confirm detailed sequence before definitive scene summary |
| Medium | E001 entire | Post-processed Parakeet transcript has changed cue boundaries and text relative to separate raw run | Sample-check against raw and source audio; identify systematic changes |
| High | E001 00:23:21 and 01:51:13 | Q4/Q8 recognize different amounts of conversational speech, including a possible Scottish-accent aside | Listen to audio, determine which extra words are genuine |
| High | E001 02:13:40 | Q8 includes an additional phrase absent from Q4 (`voodoo and the steeple and the antenna`) | Verify with audio; do not insert into canonical transcript automatically |
| Medium | E001 throughout | Q4 and Q4+Canary yield identical words but 924 word-level speaker-ID differences | Compare selected turn boundaries against audio; keep diarization correction independent of aligner choice |
| Medium | E001 Q4/Q8 raw | Q4 without Canary has 56 invalid durations; Q8 raw has 64, while Q4+Canary has zero | Validate Q8+Canary only if Q8 wins lexical accuracy comparison |
| Medium | E000 00:04 and 00:07 | Q4 `Nash Magard` versus Q8 `Nash Maggard` | Wiki supports **Nash Maggard**; retain all original model outputs |
| Medium | All future episodes | More voice acting may split individuals into additional diarizer IDs | Track per-episode aliases only; never map an ID globally |

## Resolution format

When a question is settled, record `resolution`, `evidence/audio checked`, `correction applied`, and `date`, then transfer spelling resolution into `world/CONSISTENCY_LEDGER.md` and the episode-specific correction log.

For full settings, measures, and evidence qualifications, see the [Parakeet segmentation benchmark](../reports/PARAKEET_SEGMENTATION_2026-10-21.md).

## E002–E005 follow-up listening and source checks

The E002–E005 [dossiers](../episodes/E002.md) ([E003](../episodes/E003.md), [E004](../episodes/E004.md), [E005](../episodes/E005.md)) were derived from **processed Parakeet SRT only** on 2026-10-21, without manually reviewed audio or independent ASR comparisons. Their source text is preserved.

| Priority | Episode/time | Check before any accepted spelling/canon update |
|---|---|---|
| High | E002 ~00:17–01:07 | Distinguish Dharma, Holga, Thomas, Billy and player Hill Guard; listen to the scene and later explanations for loyalties and deaths |
| High | E002 ~00:50–01:20; E003 ~01:20–01:38; E005 ~00:03–00:40 and ~02:45 | Separate dragon-engine chamber, lower pump/intake and **surface-well confirmation**; resolve exact sequence |
| High | E003 ~00:58–01:21 | Softhead's return, pipe attack and fall; no unverified declaration that he died |
| High | E003 ~02:45–03:09; E004 ~00:07–00:55; E005 ~00:01 | Audio-check `Moag Ferhain`, `Amelda`/`Emelda`, `Quizquaz` and whether title `Dream Drinker` is spoken |
| High | E003 ~02:35–02:57 | Check alphanumeric medical droid designation `C4N-D13` vs output `C4M-G13`, and whether droid voice is an existing performer |
| Medium | E004 ~00:55–01:57 | Verify whether Stanley cuts the dream tube/pipe and how Queen Amelda and the skeletons react after Quizquaz's defeat |
| High | E004 ~02:45–02:53; E005 ~00:04–00:12 | Verify Peter identity and what he *claims* about original Hillmaster line, magic and blood-powered engines |
| Medium | E004 ~02:13–02:15; E005 ~01:00–01:03 | Distinguish observed wrench shape-changing from Nash's theory of a sentient/transformed person |
| High | E005 ~01:07–02:43 | Inspect raid/missing-civilian counts, child Bruce Bane, Jimster/Shun'ti and timing of promised town meeting |
| High | E005 ~02:30–02:34 | Acquire and check original in-show regional map; do not lock in ASR spellings for nine newly heard locations |
| Medium | All E002–E005 | Build each episode's **independent** participant-to-speaker map; numeric speaker IDs shift and roles/performances vary |

A later [Episode 6 fan-wiki recap](https://twbd.fandom.com/wiki/Episode_6) can support some *later* spellings and outcomes, but not a prior episode's exact audible phrasing or first-disclosure timestamp.


## E006–E008 audio and external-artifact review queue

New source-only references: [E006](../episodes/E006.md), [E007](../episodes/E007.md), [E008](../episodes/E008.md). **No audio checked** during this documentation expansion. Keep source SRTs immutable. Listener approval is a separate later action.

| Priority | Episode / approximate time | Needed confirmation |
|---|---|---|
| High | E005 ~02:45; E006 ~00:00–00:01, ~00:24–00:26 | Nail down **engine-on**, GM retrospective summary and the first **directly observed surface well flow**; do not backdate E006's test |
| High | E006 ~01:19–01:52 | Verify **45 dead / 25 kidnapped**, Shun'ti as interim townmaster, Tetsuo's leadership versus Jimster's support, and unresolved Wilma accusation |
| High | E006 ~00:33–00:45 and ~01:08–01:18; E007 ~00:24–00:35 | Confirm **Bok Bok** and variants, captured/voluntary status, `fresh`, and old man's actual return |
| High | E006 ~01:56–02:28 | Audio-check **Zorenthelas**, **Elhandar**, claim about dragon engines/return to sky and handling of C4N-D13 data core |
| Medium | E006 ~02:12–02:17 | Translate Hope's speaking Dwarven wrench carefully; distinguish directly responsive behavior from conjectured soul/person |
| Medium | E006 ~00:45–01:06 | Check Jenjen/Thomas, Aaron's stabbing/Stanley's self-defense account and identity of second attacker; preserve viewpoints |
| High | E006 ~02:15–02:35; E007 00:00 | **Find contemporary official Fate 4 drawing/vehicle rules and Wastes map** referenced on original show website; preserve URLs, permissions, observation date |
| Medium | E006 ~02:49–03:10; E007 ~00:06–00:40 | Check the old man, first sighting vs identification of luminous beetles, and whether insects departed unharmed |
| Medium | E007 ~00:42–01:53 | Confirm trail divergence, exact intercepted vehicles, fight outcome, Fate 4 damage/repair, and inferential nature of goblin delaying tactics |
| High | E007 ~01:54–02:16; E008 ~00:10–01:11 | Establish antenna/metal tree action chronology and where **Nash and Stanley** are relative to **Hope/Vorel** at the cut; keep complexes distinct |
| High | E008 ~00:00–00:02, ~00:15–00:17 | Check **Carter Johnson / Edison Manchester III / Eddy**, **Ben Bumhofer / Chance**, and the explicitly guest-only casting; do not swap regular performers |
| High | E008 ~00:06–00:10 and ~01:23–01:49 | Separately identify Nash's vision speakers; verify Leopold's name and **claims**, projection/contact illusion, facility's reported security role |
| High | E008 ~02:00–03:00 | Verify mimic and dog encounter, Nash's failed/successful death saves and stable condition, lab artifacts and who retains them, final locked-door threat |
| Medium | All E006–E008 | Independently map human speaker to source numeric speaker IDs, handling GM voices, NPC dialogue and guest accents |

The fan wiki's E006 summary is a useful **retrospective spelling and continuity aid**, not audio verification. Preserve original references and never silently amend the recognized SRT on its authority.


## E009–E012 research and listening priorities

Reference: [E009](../episodes/E009.md), [E010](../episodes/E010.md), [E011](../episodes/E011.md), [E012](../episodes/E012.md). All time windows derive from **processed Parakeet SRTs; none has been newly checked by listening**.

| Priority | Episode / time | Confirmation before accepting canon or editing transcript |
|---|---|---|
| High | E009 ~00:22–03:12 | Reconstruct Leopold's ID badges, warden AI controls, self-destruct **24 hours vs minutes remaining** and exact state of security/doors |
| High | E009 ~01:03–01:14, ~03:02–03:12 | Verify tree's alleged elven origin and promise, escape sequence, staff custody, **Eddy/Chance disappearance without death**, and black dragon emergence |
| Medium | E009 ~00:12–00:50, ~01:14–01:40 | Track portable hole, two floating rods, immovable rod, staff — user, owner, loss, appearance and mechanical use |
| High | E010 ~00:00–00:25 | Verify Kyle/Kristen regular cast return and survivor reunion; distinguish guest gnomes from regular PCs |
| High | E010 ~00:25–02:06 | Listen to large caravan/intercept, enforcer titles, surrender, manacles, inventory seizure and **length of captive transport** |
| High | E010 ~02:01–03:19; E011 ~00:06–00:15 | Verify Slavetown, Principle (`principal` variants), Koromukishi and `Toyota` chants, elven magistrate's name, adjudication, party-only release |
| High | E010 ~02:06–02:22; E011 ~01:45–02:15 | Match prisoner sightings to **25 reported Dusthill captives** and recognition of **Talia Bane**, mother of Bruce; never count all as freed |
| Medium | E011 ~00:15–00:44 | Recover **contemporaneous Slavetown street map** and compare with E005 regional map; verify `Slippery Brent`, street/place spellings |
| High | E011 ~01:30–02:24 and E012 ~01:35–01:48 | Audio-verify **Celibus Stump**, `Buxom Confederate`, Talia's coercive circumstances, private conversation, temporary hotel respite versus release |
| High | E011 ~02:47–02:58; E012 ~00:46–01:10 | Check **Nash/Jeweler fight**, spells, unconsciousness/possible robbery and exact inventory/gold disappearance |
| High | E012 ~02:28–03:10 | Confirm whether deed is for **copper** or **gold** mine; record who claimed ownership, holders, brokers and explicit conditions for freeing people |
| High | E012 ~02:55–03:08 | Cross-check **Hillmaster/Softhead betrayal accusation**, `Pristine`, Trentard/Mabruk Oilbeard, Timber McClellan, Catherine Speckles against other in-episode evidence |
| Medium | E012 ~03:02–03:10 | Avoid conflating notorious woman in red bandolier with alleged deed holder Catherine; exact identification and alleged gang |
| Medium | E011–E012 all | Check S. J. Lattlebing/hotel, Owen's garage, foundry/weapon work, spell/periapt effects and the real status of Talia and Bok Bok at session end |
| Medium | E009–E012 | Build **episode-specific speaker maps**, separating multiple NPC voices and E009 guest cast; compare other preserved ASR outputs where available |

Do not alter the original SRT or promote machine-only phrasing into approved dialogue. Record audio verification with timecode, listening outcome and any spelling/source changes in the consistency ledger and correction log.


## Image-provenance and visual-reference follow-up (new assets 2026-10-21)

- **High — copyright/provenance:** For all **85 archived WebP images** in [image inventory](IMAGE_ASSETS.md), capture the original wiki **File:** page or original artist/creator URL, uploader, original date/version and **media-specific license or permission**. The public Fandom text license is **not a blanket image license**. Decide inclusion in future public releases independently for each file. The current copies are in a private repository, not publication-cleared.
- **High — vehicle sheet now found:** [Fate 4 main sheet](../sources/images/Fate_4_Character_Sheet.webp) and [continued sheet](../sources/images/Fate_4_Character_Sheet_Continued.webp) explicitly credit **Kristen Ashton** and give period vehicle details. Compare E006 ~02:15–02:30 creator presentation, E007 vehicle chase and E010 caravan combat. Verify exact public version/date; don't conflate sheet rules with play outcomes.
- **Medium — layout reconciliation:** Compare independent [floorplan](../sources/images/Fate_4_Floorplan.webp) (2-foot tiles) against creator sheet's inner-layout drawings; document differences as separate representations, not silently corrected facts.
- **High — regional map found, but not dated:** [Beyond the Deadfingers](../sources/images/Map_BeyondTheDeadfingers_resized.webp) includes Dusthill, Moag Ferhain, Slavetown and later annotations. Audit small-print spellings and chronology, then compare with **E005's in-session map** without assuming identical provenance.
- **High — Slavetown plan still absent:** E011 ~00:15–00:44 **town street map** is **not** the Beyond the Deadfingers regional map or [The Teet](../sources/images/Map_-_The_Teet.webp); seek an actual contemporary town map before declaring its street labels confirmed.
- **Low — illustration-only cross-index:** Artist-labelled images such as [Bok Bok portrait](../sources/images/Bok_Bok.webp), [Fate 4 action](../sources/images/Audie_Norman_Fate_4_Action_Shot.webp) and [gibbering mouther](../sources/images/Scott_Johnson_-_Gibbering_Mouther.webp) can serve future visual navigation **after** verifying rights and episode-era spoilers. Do not treat fan depictions as listener-checked canon.

No audio review completed during this visual-source pass.

## E013 / E013.5 / E014 review targets (not listened to)

| Priority | Recording/time | Task |
|---|---|---|
| High | E013 ~00:05–00:12 | Confirm GM **Pristine→Slavetown** history, roughly 10–20 year shift, Toyota Host vs Koromukishi vs sheriff vs magistrate; distinguish direct GM exposition from Jeweler claim |
| High | E013 ~00:10–00:21 | Compare Stump and Jeweler mine deed motives and what the **Lactid Cartel** says the Jeweler owed it; never assume the promised item was the deed |
| High | E013 ~00:19–01:52 | Verify **Cartel** spelling, name **Bertrand**, combat sequence and **Donk dead / Jeweler healed**, illusion of Quizquaz vs genuine demon |
| Medium | E013 ~01:05–02:12 | Sheriff **Randy Clementine**, fate of the attacker, Stump's cartel origin/business explanation |
| Medium | E013 ~02:12–end | Pickpocket gnomes not Eddie/Chance, purple-hatted man, giant at hotel, name and roughly 60–70 foot height |
| High | E013.5 ~00:00–00:10, ~00:23–end | Verify **supplemental** music, Stanley's **in-character** recap including E010 old man's fate; don't contradict E009 host statement that Eddy/Chance are alive |
| High | E013.5 ~00:10–00:23 | Verify inserted **Hope–Vorel** scene set ~E008–E009: actual dark-pact/time-travel goal, Exantos, dragon/star and lizardfolk hearsay, possible jetpack test, omitted/garbled ending. Track separate *release* and *story* dates |
| High | E014 ~00:00–00:49 | Confirm Jeweler surname **Mulg (?)**, **Robert/Thailander/Tylander** identities, sheriff and cyclops behaviors and the “shiny” |
| High | E014 ~00:49–01:23 | **Thorn Row** address/street names, upstairs corpse **not yet identified**, note to **Timber**, “Red Scarlet” signature, magical glyph trap |
| Medium | E014 ~01:23–01:40 | Liberators pamphlet, woman portrait, **Freedom** gun, silver bullets, money amount and inventories |
| High | E014 ~01:40–02:32 | Trap/mechanical route, ruby necklace **five vs six** question, true identification of freshly dead **Randall Owen** |
| High | E014 ~02:32–03:00 | Untouchable gnome-like decoy, gas/portcullis, ritualist identity, **Catoblepraithe / Soulbroker** pronunciation, reanimated corpses, exact unresolved cliffhanger |
| Medium | E014 artwork | Check [Catoblepraithe image](../sources/images/Catoblepraithe_-_Audie_Norman.webp) original wiki File: page/date/artist/media rights; do not treat it as proof of the creature appearing in E014 |

**Carryover:** Mine deed “copper” versus “gold”, Stump's claims, the E011 Slavetown street map and original 25 captives remain unresolved. These episode dossiers are not audio-verified. [E013](../episodes/E013.md) · [E013.5](../episodes/E013.5.md) · [E014](../episodes/E014.md).

## E015–E016 uncompleted audio and reference review (2026-10-21)

Source links: [E015](../episodes/E015.md) and [E016](../episodes/E016.md). This batch is from **processed Parakeet SRT only**, with **no newly listened-to audio**. Confirm name phonetics independently of later fan art and retrospective recaps.

| Priority | Approximate source position | Target |
|---|---|---|
| High | E015 ~00:02–00:06 | Verify GM recap's **Tylander Sullivan**, **Orp** and **Sheriff Randy death in E014**. Correct earlier E014 provisional status only as **later source clarification**, not original dialogue |
| High | E015 ~00:06–00:43 | Portcullis/undead combat, **immovable rod**, glyphs, escape route and whether Tylander physically projects or stands in basement; his offer of **parchment deed** versus no confirmed handover |
| High | E015 ~00:53–01:11 | Necklace to Orp, **Feather Fall** catch, charm and magical incapacitation of giant; inventory control |
| High | E015 ~01:11–01:46; E016 opening | Orp's necklace **custody sequence** and **Tylander declared dead**, Vorel's possible persistent curse, alleged mine deed **disappears into smoke** |
| High | E015 ~01:44–02:06 | Lady Saltbubble/Sir Chickenfinger say Tylander opposed slavers; **their faction perspective**, debate and decision not to kill Orp |
| Medium | E015 ~02:10–02:36 | Orp fed sand squid; exact **party split**. Suggestions to target goblins do not become observed actions |
| High | E016 ~00:09–00:38 | Verify route name **Esophageal Pass**, ordinary dagger **presented falsely as magic** and danger to actual travelers; what Orp was told versus what the group intended |
| High | E016 ~00:31–00:40, ~01:25–01:52, ~02:33–02:39 | Vorel follows scout, **female priestess/Tepala**, **Kurik lineage**, **Fuxi (GM spells F-U-X-I)**, ritual shark/fire vision versus real camp, exact flaming-rage mechanics and Bok Bok reunion |
| High | E016 ~00:38–00:51, ~02:27–02:33 | **Randall Owen** family home body: identify woman, context; child death according to official. Do not collapse adult/child/Randall deaths |
| High | E016 ~01:08–01:26, ~01:52 | Ruined **Thorn Row** building, around eight **Toyota Host** dead, active severed arm / burning; identity not positively verified |
| High | E016 ~02:03–02:10 | **Externally observed dragon flyover and Nash transformation/fire** versus only-Nash **“Mother”** voice. Listen for exact words and any explicitly named parent/source |
| High | E016 ~02:19–02:33 | Magistrate's exact name, **Tylander-return report**, exact nature of possible pact, **Black Mine** land record for **Catherine Speckles / 999th level**, mine identity versus copper/gold deed |
| High | E016 ~02:23–02:33 | Conditions of promised **Dusthill prisoner release** and protection from future raids, magistrate's claimed authority, group's **conditional** acceptance pending Vorel/rest |
| Medium | E016 ~02:39–end | Host says linked **episode blog posts/show notes** to start with this episode; retrieve contemporary publisher record to corroborate credits and spelling, not as audio evidence |

**Carryover:** The **Salivating Fields evacuation is not prisoner freedom**, and the Black Mine/999th level is not known to be the mine title sought earlier. Orp's pending actions and Tylander's true post-E015 survival remain **open**. Preserve all raw/processed SRTs and label audio-confirmed findings separately.

