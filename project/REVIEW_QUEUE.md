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

**Targeted evidence added (2026-10-21):** a real 29.640-second Parakeet clip now
recognizes `hi kyle hi hi` around 01:40–01:42. Review the
[execution/import report](../reports/TARGETED_VERIFICATION_2026-10-21.md) and
listen to 01:39–01:43 before resolving the greetings row below. The additional
`there` around 01:39.640 is also unresolved. All earlier candidates and listening
tasks remain; successful execution does not count as audio verification.

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

## Owner-provided numbering and note verification (2026-10-21)

Two private source exports were reviewed: `There Will Be Dungeons episodes.xlsx` (**explicit corrected labels in Sheet2 Column I**) and `There Will Be Dungeons.docx` (**personal spelling and episode/event notes**, not canonical). Source provenance and examples: [numbering policy](EPISODE_NUMBERING.md) · [owner note index](OWNER_EPISODE_NOTES.md).

| Priority | Source / reference | Needed follow-up |
|---|---|---|
| High, before any automated filename importer | Spreadsheet: original **55** Year One Q&A bonus; original **56** → corrected **E055**; original **77** twice for *Inverse*; original **78** → corrected **E076** | Build/test **campaign+season+original full label ↔ corrected filename** mapping. **Use Column I**, not formula-valued `Episode` cells that can show `#NAME?` in snapshot |
| High, later season handling | Spreadsheet original **130** → Wastes **S1E128**; Wastes **S3E78 Electric Lizard** → **S3E08** | Preserve historical numbering mistakes, separate series and bonus files; don't shift all seasons using S1 offset |
| High, early events | Personal DOCX E003 “Hillmaster falls” | Recheck **E002 last scene vs E003 intro**, determine first *played* event rather than retrospective recap |
| High, first spoken names | Personal DOCX E003–E004 `Quizquoz`, `Elhandar`, `The Abyss`, `Dream Drinker`, `Friendship Fortress` | Listen to source episodes, record speaker and time, distinguish testimony and first mentions |
| Medium, dialogue marker | Owner note E005 first `Nash Maggard of the Solar Mines` | Compare E000–E004 before recording true first use |
| Medium, cliffhanger boundary | Owner note E007 “old man and lights” | Compare E006 ending vs E007 encounter; first sighting and recognition may be in different episodes |
| High, orthography | Owner note E010 `Kuromo Kishi`; E013 `Laktid` | **Owner search aliases**, not accepted canonical changes. Cross-check original audio and creator/written materials |
| High, first mention versus first usage | Owner note E011 **Pixie Blush** mention, E017 acquisition/use | Check both and earlier material; do not backfill future drug episode into early dossier without appropriate spoiler horizon |
| Medium, optional character detail | Owner E011 Nash's `lost member`, E016 Vorel **fire aura** | Identify exact wording and game action before creating character/ability facts |
| High, publication metadata | Original spreadsheet has **240 rows**, some calculated cells display `#NAME?` in import | Preserve original titles, normalized filenames, campaign/season and date fields; review bonus month-label discrepancies rather than overwriting them |

This is an **uncompleted listening/import queue**, not a set of confirmed new transcript corrections. Source XLSX/DOCX binaries and all raw/processed SRT files remain unchanged.

## Episodes 17–18: outstanding listening and continuity checks

**Status:** Open review tasks based on [E017](../episodes/E017.md) and [E018](../episodes/E018.md). The user's [personal notes](OWNER_EPISODE_NOTES.md) are **not canonical**, and neither episode was checked against audio during this dossier expansion. Use [corrected IDs](EPISODE_NUMBERING.md).

| Priority | Timestamp | Questions to verify by listening |
|---|---|---|
| High | E017 ~00:00–00:04 | Is the proposed Nash/dragon connection clearly introduced as a **listener's theory**? |
| High | E017 ~00:32–00:57 | Confirm the apothecary **Maripol Bania**, the name **Pixie Blush**, Nash's subsequent symptoms, and Hope's reading. Owner notes distinguish an **E011 mention** from **E017 use** |
| High | E017 ~01:00–01:16 | Identify red-bandolier **Jolt/Joel Telagos**, the title **Acrimonicar**, the proposed bank heist, **Forbisher's Holdings** and meeting location. **No heist is observed** |
| Medium | E017 ~01:00–01:10 | Track **Bok Bok**, **Gita/Gitert**, and their whereabouts before and after the Slavetown fire |
| High | E017 ~01:16–02:25 | Track inventories and the difference between Nash's altered perceptions and the GM-narrated physical consequences |
| High | E017 ~01:40–02:08 | Verify the sequence involving the foundry's armed owner, Vorel, and Stanley's injuries |
| High | E017 ~02:25–02:53 | Determine exactly which streets and businesses are observed burning, who leaves town and in which **replacement station wagon**; never assume all civilians die |
| High | E018 ~00:09–00:37 | Confirm storm arrival, wagon burial, Vorel's help escaping and whether the vehicle is definitively unusable |
| Medium | E018 ~00:37–01:00 | Describe the giant carcass and approximately eight javelin-carrying strangers. **Species unknown**; listen to Hope's spell and their departure |
| High | E018 ~01:04–01:14 | Record **Nash's first-person Solar Mines story** about his staff's nail **Freedom**. Keep distinct from the E014 firearm **Freedom** |
| Medium | E018 ~01:12–01:29 | Does the storm's impact on **Slavetown's previous blaze** become observed fact, or remain speculation? |
| High | E018 ~01:29–02:16 | Confirm the dwarven overseer's **Scrolly/Scrawly Oilbeard** name, **Tickles**, the upper guard group and the slavers' account of the mine uprising |
| High | E018 ~02:08–end | Verify shaft descent, **Feather Fall**, the sign **23**, the early undead encounter and precise final elevator cliffhanger. The larger fight is **E019**, not yet described here |
| Medium | Future research | Seek historical show notes promised in E016 for dated name leads, not as a substitute for the episode audio |

Pending issues are logged in the [consistency ledger](../world/CONSISTENCY_LEDGER.md). No review item should be marked resolved merely because multiple ASR systems or owner's notes agree.

## E019–E021 listening and continuity priorities (open; 2026-10-21)

Sources are [E019](../episodes/E019.md), [E020](../episodes/E020.md), [E021](../episodes/E021.md). **No audio listening is recorded for this batch**. Owner notes are [noncanonical](OWNER_EPISODE_NOTES.md); use [corrected numbers](EPISODE_NUMBERING.md).

| Priority | Time | Review question |
|---|---|---|
| High | E019 ~00:05–02:09 | Reconstruct elevator **ascent → guards reverse → descent**, waves of undead and **Tickles's jump**. Distinguish GM recap E020 from E019's direct play |
| High | E019 ~02:09–02:30 | Verify damage to support chain / **Thunderwave**, passing **78**, eventual **Feather Fall**, Nash's recovered nail-staff and lack of identifiable terminal floor |
| High | E019 ~02:30–end; E020 ~00:06–00:18 | Track survival of Tickles to rockfall, subsequent **unresponsive/dead** verdict, rescued PCs and **Stanley's painful ribs** |
| Medium | E020 ~00:00–00:06 | Out-of-game **Vorel fire aura / animated sword** rule correction, not source for a global rules interpretation |
| High | E020 ~00:39–01:20 | Distinguish first trap lever from **second safety lever**, sealed study, **Tylander journal**, male skeleton and trapdoor |
| High | E020 ~01:00–01:08 | Listen to **journal day 245** precisely, names **Mariosa, Daisy, Tobyl/Tobel, Lily**, voice behind the deep door, woman in Slavetown, Tylander's **signature/author attribution** and encrypted page |
| Medium | E020 ~01:20–02:35 | Check chasm/mushroom/glyph geometry, displacer beast species and injured features, its **final defeat**, use of **Feather Fall** |
| High | E020 ~02:35–end; E021 ~00:04–00:09 | Magical darkness triggered by dead beast; **Hope's private “find me” voice** while other players have headphones removed |
| Medium | E021 ~00:09–01:20 | Hostile animate fungi vs ordinary mushrooms; glyph trigger conditions, enlarged-Vorel bridge across hazard |
| High | E021 ~01:20–01:55 | **Dorothy** metal-faced talking door: exact name, riddle, security promises and who opens/accesses the passage |
| High | E021 ~01:55–02:23 | **Tylander former mayor** confession vs E013 GM and E020 journal, **Fingers** name, confession about undead, illusion/projection of his physical presence |
| High | E021 ~02:12–02:17 and ~03:03–03:12 | **Tylander impersonating Catherine** versus separate captive woman who says **she is Catherine**; exact message to Bertrand and whether GM confirms death |
| High | E021 ~02:23–03:03 | Battle number/outcome of **eight Fingers** and distinction between follower defeat versus Tylander remaining free |
| High | E021 ~03:12–03:21 | Locked chest/deed **not recovered**, apparent **Tylander by cauldron** and ~20-ft **winged figure**. Is it explicitly called **Catoblepraithe** before E021 ends? |
| Medium | E019–E021 | Recorded podcast official **fan-art montage / Roll20 map** references can help find period visuals; permissions and dates need separate verification |

Keep original ASR intact; mark every eventual audio-confirmed correction with a timestamp and do not replace in-episode claims with fan-wiki or owner's retrospective notes.

## E022–E024 listening and source audit (pending)

All tasks below are **uncompleted**, based on machine SRT and [episode dossiers](../episodes/E022.md), [E023](../episodes/E023.md), [E024](../episodes/E024.md). Corrected episode identifiers from the user's [numbering spreadsheet](EPISODE_NUMBERING.md); [owner notes](OWNER_EPISODE_NOTES.md) not canonical.

| Priority | Episode/time | Specific audio/source question |
|---|---|---|
| High | E022 ~00:00–00:22 | Confirm **Quizquaz** = E021 winged figure and **not Catoblepraithe**; tail-triggered glyph/rockfall, door closure and group positioning |
| High | E022 ~00:22–01:35 | Trace force field, crystals, eye-stalk linkage, hidden **beholder** and which attacks/attunements occur; no invented unified glyph rule |
| High | E022 ~01:35–03:05 | Exact **Vorel charm/sleep/incapacitation** and beholder defeat; **Quizquaz gem removal** and portal/arrival of goat-headed patron |
| Medium | E022 outro, E023 pact | **Level 4 all characters** versus **extra feat only contract signatories** |
| High | E023 ~00:10–00:39 | Soulbroker's spoken/name orthography, action **healing Vorel**, realm and **Château Weir** title; separate observed city from moral/metaphysical claims |
| High | E023 ~00:39–01:45 | Hotel **Baba, Chef Dan**, food/wavier details, bath/guest-room scenes; **hospitality waivers not contract** |
| High | E023 ~01:45–02:20 | **Hope private mother dream**—exact **Haven**, afterlife exchange, **red bullet woman and Dead Men** name; Vorel's outside-knock scene, dream versus actual evidence |
| High | E023 ~02:35–02:47 | Obtain exact pact **1,000 days and nights**, three **named signers**, **Vorel non-signer**, soul-forfeit clause, extra ability/feat and unilateral exit/return conditions |
| High | E023 end ↔ E024 beginning | Locate exact **Nash private reveal** boundary; other PCs remove headphones only in E024 |
| High | E024 ~00:06–00:51 | Audit **Solar Mines vision** for Warden, Bulger, dragon-sun-mage experiment, captive tanks, roles of persons and whether any material is explicitly hallucination/memory |
| High | E024 ~00:51–01:09 | Find contemporary **Dragon Metal Heart of Kas/Cas de Jira** item spelling/text; GM-confirmed wyrmling power, exhaustion restriction, broodmother identity vs private dragon memories; **do not use current end-of-campaign build** |
| High | E024 ~01:09–01:29 | Artifact names `Fox and Scully`, Teet `Acrimonicar`, `Elhendar`, `Celestium` strategy and 100-ft keys; distinguish offered item vs actually acquired |
| High | E024 ~01:23–01:29 | Soulbroker's **qualified agent report** about Hope's father, statement **mine deed used as reagent**, promised captives' liberation (not yet carried out) |
| High | E024 ~01:34–02:50 | Vorel **mundane beholder-tooth shield**, time in other realm, original chamber/corridor, Catherine's remains, **E024 chest actually opened** |
| High | E024 ~02:45–02:53 | Itemize **60 gold, 2 bloodstones, 2 citrine, 1 jasper, 1 quartz, potion of clairvoyance + potion of mind reading**, test ownership, pocketing and spell identification |
| High | E024 ~02:50–end | **Burning Dorothy** results, smoke, still-speaking voice, bone test and **exit not yet achieved**. E025 may resolve but must not be retroactively assumed |

**Additional checks:** Publisher show-era artwork, maps, creature stat text and D&D Beyond custom items (if accessible) can corroborate **spellings and original mechanics** but are not licenses for redistribution. Keep model comparisons separate from **listening verification**.

## E025–E027 open listening and provenance audits (2026-10-21)

[E025](../episodes/E025.md), [E026](../episodes/E026.md), [E027](../episodes/E027.md) were reviewed against **processed Parakeet SRT only**, *not listened to*. Corrected numbering from [owner source](EPISODE_NUMBERING.md), individual owner spellings not canon ([notes](OWNER_EPISODE_NOTES.md)).

| Priority | Approximate source | Unresolved verification |
|---|---|---|
| High | E025 ~00:07–00:24 | Smoking **Dorothy** exit, **Nash pit fall/rescue**, what door actually says, whether intact or merely voice persists |
| High | E025 ~00:50–01:19 | Nash dragon **Enlarge**, harness, carrying capacity/flight and exhaustion; original contemporaneous Dragon Metal Heart rule text vs table adjustments |
| High | E025 ~01:19–02:20 | Dwarf numbers, **Bessie** Gatling, Nash human reversion, individual fatalities and escaped motorcycle dwarf |
| High | E025 ~02:20–02:35 | **Scrolly interrogation/torture**, healing/reinjury, fall down shaft and whether final death explicitly narrated; avoid moral sanitization |
| High | E025 ending → E026 ~00:07–00:25 | Prison lock versus release, **Bok Bok, Bertrand, Trigger**, their capture/repair-of-**Fate 4** stories |
| High | E026 ~00:25–00:35 | Bertrand's account of **Tylander stoning in Pristine** and **deed/dragon metal** suspicion; reconcile **NPC testimony** with E021 Tylander claims and Soulbroker E024 |
| High | E026 ~00:37–01:00 | Identity of **armored buggy arrival**, stolen keys; **Lactid** correct name, mind-control assertions and reported specialist at Slavetown |
| High | E026 ~01:20–02:15 | Liberators camp location/timing, **Vorel bear kill/trophy**, Nash's visible Fire Bolt and secret-camp exposure risk |
| High | E026 ~02:15–02:42 | **Slippery Brent/Brint** assault and final physical condition, coerced statements vs Pixie Blush confusion; party moral conflict |
| High | E026 ~02:42–end and E027 ~00:31–00:46 | Blind **former Koromukishi orc's** self-blinding and chosen namelessness, plans for a pass closure, camp's actual military readiness |
| High | E027 ~00:00–01:19 | Stanley's departure/reconciliation, camp **compromise** source, **Tedna/Ted** name, age/intent, Fate 4 first-time driving |
| High | E027 ~01:19–02:23 | **Sir Ranko / Umbilical Order** spelling/affiliation, powered armor/equipment, demon-taint accusations, **flare**, final death, whether E026 visitor the same |
| High | E027 ~02:23–02:40 | Blast/recovery of Fate 4 and **Tedna found alive but unconscious**; who else survives |
| High | E027 ~02:40–end | **Diptak of Golden Land**, **Typalla/Tepala** names, disputed consort status, size of hunting party/raptors, challenge ritual details and **no duel result yet** |

**Reminder:** Before claiming a term canonical, seek a reliable show-era written source or listen. Separate owned personal notes, ASR, GM explanation, NPC testimony, propaganda, private visions, and confirmed actions.

## E028–E030: pending audio and continuity checks (2026-10-21)

[E028](../episodes/E028.md), [E029](../episodes/E029.md), [E030](../episodes/E030.md): **processed Parakeet-only dossiers**. Owner [numbering corrections](EPISODE_NUMBERING.md) applied; [personal spellings](OWNER_EPISODE_NOTES.md) are noncanonical.

| Priority | Episode/time | Listening or other verification |
|---|---|---|
| High | E028 ~01:17–01:35 | Confirm **Diptak yields alive**, oath terms and commitment to Vorel, **Golden Land** and **Razhak Val** spellings, brothers' names, **Typala** relation; ensure raptor killed by **Hope** is distinct |
| High | E028 ~01:35–01:55 | Roof patch from raptor skin versus new small blast hole; exact Tedna/Nash/Stanley confrontation and young passenger's welfare |
| High | E028 ~01:55–02:36 | **Buttons's first name and identity**, **Arcanum Universalis**, wizard `Darguth/Jarguth`, prosthetic leg, claimed ordinary-cat parentage, old Dan Dakota Teet map |
| High | E028 ~02:10–02:49 | Teet/Trashburg spellings **Guzzle Gang, Suckmaster, Andreeste, Milinar's, Pit of Despair**, first written/dated map, whether Buttons actually hands over 10 gold |
| High | E028 ~02:49–end | Hope's exact compulsion onset, blue lights, who witnesses departure and true episode break |
| High | E029 00:00–00:04 | Special **Beau/Jon-only session**, absence of main actors versus continuing in-story party |
| High | E029 ~00:04–01:07 | **Stanley ties Nash to workbench**, follows Tedna/party with Buttons, map/prison geography and retreat code “lemon tree” |
| High | E029 ~01:07–02:13 | Hag/worm `Blort`, song and “mana waves,” who is enthralled, death of monster and hag, dynamite/Feather Fall/Bok Bok injury |
| Critical | E029 ~02:18–end | Name `Dion Talus`, claimed archfey/old elven war, **Stanley's explicit refusal** versus **forced Charisma-save energy entry**, unknown continuing effect. Do **not call consensual pact** |
| High | E030 ~00:04–00:22 | Nash rope escape by **Reduce**, others' shared dream narration and player-vs-character knowledge |
| High | E030 ~00:22–01:13 | Collapse sequence, Hope/Tedna and Vorel/Stanley rescues, **immovable rod left under oil** and whether salvage attempted |
| Medium | E030 ~01:13–01:40 | Regroup at shoreline, what Stanley actually discloses about archfey/hag to companions |
| High | E030 ~01:40–02:09 | Buttons's cat/thumb/wizard story, offered **Blink spell text** versus successfully learnt/cast, Tedna's driving/role |
| High | E030 ~02:09–end | Teet outer approach, RV concealment, whether anyone **actually enters Trashburg**, status of `Fox and Scully` and Celestium quest clues |

**Carryover:** E027 ends on Diptak's charge. E028 resolves challenge, *not* oil-lake mystery. E029 solo ends on forced energy transfer. E030 escapes collapse and heads toward the Teet; do not infer later city encounter. Only promote corrected spellings after audio or reliable show-era written corroboration.

## E031–E033 open audio and primary-source review (2026-10-21)

[Episode 31](../episodes/E031.md), [Episode 32](../episodes/E032.md), [Episode 33](../episodes/E033.md): **machine-transcript-derived only**. Owner's [corrected numbering](EPISODE_NUMBERING.md), [noncanonical spellings](OWNER_EPISODE_NOTES.md).

| Priority | Approximate source position | Review goal |
|---|---|---|
| High | E031 ~00:20–00:54 | First-person Teet entry, **26 tattoos**, **Charlemagne** and `Jolt Elegos/Bellicose` name/title |
| High | E031 ~00:54–01:10 | Suckmaster **Din Bottle-Bite**, son **Alidwyr**, bride **Jolt Acrimonicar**, **Friday Blood Ball / Saturday wedding**, announced non-work days, and **Pit tongue** |
| Medium | E031 ~01:11–01:55 | Hotel map/rates, **guzbucks**, Mayor **Tonkules Herman**, guard chief **Penepole**, gang territories |
| Critical | E031 ~01:55–02:15 | Confirm label **P0D** (zero), **Farmer Dewey**, pixie aquariums and production of **Pixie Blush**, which facts are P0D testimony |
| High | E031 ~02:15–end | Precisely record debate on **rescuing pixies** and using *existing* Pixie Blush; do not infer a performed drugging/bleaching |
| High | E032 ~00:05–01:16 | **Monsoon Cabbage** gang, **Forty-Two Carnage**, Toe Ripper rivalry, conditional **assassination for keep route** and no fulfillment |
| Critical | E032 ~01:37–01:46 | **Buttons witnessed E029 blue entry**; **Stanley casts Suggestion**. Compare E029 refusal and later E033 ambiguous identity |
| Medium | E032 ~01:46–02:18 | **Tedna catering** route, **Bok Bok toe necklace**, uncertain formal affiliation and safety |
| High | E032 ~02:35–end | Shelter for **P0D**, Charlemagne's parcel to **Jedel McCready**, body and fanged figure, cliffhanger |
| Critical | E033 ~00:05–01:22 | Unnamed **vampire-like attacker**: any explicit GM species identification, regeneration, disappearance and Hope's exact **maximum-HP reduction** |
| High | E033 ~01:04–01:39 | Actual **launcher case** contents/count, custody, dead body's identification, parcel/delivery outcome |
| Medium | E033 ~01:39–01:58 | Town legal announcements, **well-armed bar visitor** identity, security restrictions |
| High | E033 ~01:58–02:21 | **Gray Socks / Pounders** schedule, participants, guarantee (if any) of keep access |
| Critical | E033 ~02:21–end | Exact **Stanley “right now”** wording and any other self-identity statement, character state versus drink, **Scott's absence vs Nash character** |

No open item is resolved by agreement between multiple ASR outputs or the owner's retrospective notes alone.

## E034–E036 source audit priorities (2026-10-21)

[Episode 34](../episodes/E034.md), [Episode 35](../episodes/E035.md), [Episode 36](../episodes/E036.md): **provisional processed SRTs, not audio-confirmed**. [Corrected owner numbering](EPISODE_NUMBERING.md); [owner spellings](OWNER_EPISODE_NOTES.md) noncanonical.

| Priority | Time | Review question |
|---|---|---|
| Critical | **E034 ~00:59–01:39** | Listen to **Dion Talus's explicit identity/control disclosure**, acknowledgement of **Stanley's earlier refusal and forced union**, difference between observed control and his self-claimed history/mana-wave needs; exact transfer back to Stanley |
| High | E034 ~00:28–00:37 | `Dashington` gunman, alleged threat to Stanley, Vorel's intended private meeting |
| High | E034 ~00:37–00:59 | **Hope's reflection** and lingering max-HP effect after E033 bite; no vampire diagnosis from folklore |
| High | E034 ~01:39–02:41 | Coach **Marlboro/Marlborough**, `Camel/Camille`, team numbers **1,3,5,7**, custom game skill rolls, practice hours and **200 guzzbolts not paid yet** |
| Medium | E034 ~02:41–end | Blood Ball vs pixie assistance, campaign commitments still pending |
| High | E035 ~00:13–00:20 | Promoter **Fango Rabbish/Ravish**, Golden Gargoyle evening invitation, card game and singer **Angel Ashi** |
| High | E035 ~00:20–01:05 | **Buttons remains missing**, parcel status, **Charlemagne's grief**, what is and is not independently known of the deceased at **Jedel McCready's**, suspicions about Twenty-Sixers |
| High | E035 ~01:15–02:40 | Exact first attack by **Vorel**, gang fighter/civilian casualty count, **Nash acid breath** without shifting, who starts fire, extent of building collapse |
| High | E035 ~02:33–end | Teet Guard siren, whether the party is seen, Golden Gargoyle **entry not Angel Ashi performance** |
| Critical | E036 ~00:28–00:53 | **Angel Ashi stage story** vs factual testimony, raiders' entry, **Blunt Goliver** name/title and the shaman's role |
| High | E036 ~00:53–02:40 | **Vorel claims Toe Ripper leadership**, Nash wyrmling, unique influence resistance, toe eating/buff claim, who is alive as fight ends, total enemy losses if possible |
| Critical | E036 ~02:40–03:13 | **Fango's backstage/sewer escape route** and explicitly verify **Blunt Goliver is not declared defeated**; Angel Ashi opting to leave with Nash |
| High | E036 ~03:13–end | **Nash's two exhaustion levels**, no immediate sexual/romantic event presumed, OOC **level-5 award** without recovery |

**Carryover:** E035 violence and E036 bigger battle are **separate engagements**; neither proves Monsoon's assassination condition achieved. Do not backdate E036 performance to E035 or confuse Dion's admitted physical control with claims about ancient fey cosmology.

