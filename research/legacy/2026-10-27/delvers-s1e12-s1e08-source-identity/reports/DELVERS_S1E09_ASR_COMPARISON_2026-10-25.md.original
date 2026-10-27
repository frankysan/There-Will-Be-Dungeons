# Delvers S1E09 — Once a Month Goat: ASR comparison (2026-10-25)

**Sources:** Played Delvers S1E09, archive title *Once a Month Goat*, exact matching basename in the [Delvers inventory](../delvers/SOURCE_INVENTORY.md); private GitHub `frankysan/There-Will-Be-Dungeons-Transcripts` pinned commit **`33372182a7cd6518355ffd4dff93c036ca82574a`**, same as initial clean connected workspace `main`. **No source audio listened to or MP3/SRT alignment proven.**

| Filename-inferred pipeline | Source | Git blob SHA | Cues | Last cue end | Normalized word tokens |
| --- | --- | --- | ---: | --- | ---: |
| Primary Parakeet processed | [Parakeet SRT](../sources/Delvers%20S1E09.%20Once%20a%20Month%20Goat.parakeet.processed.srt) | `5912bf61d92f7908e2a8b351847473ca2cfc9525` | **2,467** | **02:52:48.130** | **22,206** |
| Secondary Qwen Q8/Canary CTC/Nemotron-labelled | [Qwen SRT](../sources/Delvers%20S1E09.%20Once%20a%20Month%20Goat.qwen-q8.canary-ctc.nemotron.srt) | `9e142de2b0ae4eed5270a355212e702394a3eb13` | **4,009** | **02:52:47.840** | **22,239** |

## Exact full-export ordered word comparison

**1,551 edits / 22,206 Parakeet words = 6.98% inter-ASR textual disagreement**, **not WER, accuracy or verified missed/hallucinated words**. Qwen contains 33 more normalized words; last subtitle ends **0.290 seconds earlier**, insufficient to verify shared source audio. No model run settings, GPU usage or time performances inferred.

Method: Split SRT into cues; discard cue numbers and times; strip optional `(speaker N)`, join all cue contents in recording order; Unicode lowercase; remove straight/curly apostrophes (join contractions); replace runs of characters other than Unicode letters and digits with spaces; tokenize. Calculate **unit-cost ordered word Levenshtein distance** using two dynamic-programming rows and a **3,500-word diagonal band**. Returned **1,551** is below the band bound and so matches the unrestricted optimal edit distance; independent of time-aware alignments. The metric is computed from **complete inputs**, not representative excerpts.

**Review coverage:** Entire Parakeet text inspected chronologically from sponsor intro through network outro, at approximate 35–47 minute recording chunks. Complete Qwen source tokenized for metric; Qwen semantic close-reading **targeted** the cube/piercer/grick outcome, hook horror fight, courier/horn handoff, guild reward and temple, sash and shopping, wife/family, and casting/level-up scenes; **not a second complete semantic reading**. No audio/window was listened to, no original map/handout inspected, no `tools/prepare_episode.py` or local script/check run.

## Material differences and interpretation boundaries

| Approximate Parakeet clock | Cross-reading and conservative conclusion |
| --- | --- |
| ~00:01–00:30 | **Cube defeated by Evelyn's Javelin of Lightning**, releasing **living Faelan**; Koh's psychic attacks/First Sons' strikes precede final blow. A separate **grick drags away piercer**. Intermixed dramatic sound rendering and 'piercer' spellings are not independently audio-certified. Do not classify all underground creatures dead. |
| ~00:36–01:02 | Creature identified from sparse old guild drawing as **hook horror**; **Evelyn's second Horn of Blasting use deals 21 thunder**, makes it apparently lose sensory navigation, **Koh's double-20 bow shot kills**. Qwen supports distinct **second living hook horror** glimpsed by Koh while retrieving large hook limb. Other grick survives; rock pile obstructs local side passage, not global cave seal. |
| ~01:04–01:09 | **Important custody correction** to S1E08: horn **handed by Evelyn to Carrie**; she delegates item carriage to a monk. Hook appendage, bottled cube gelatin and **one psychic shaft** submitted by Koh as evidence. No verified permanent confiscation or return. |
| ~01:10–01:24 | The reports from squads differ, and casting Fireball into a well is not proof its water is clean. Cassius takes responsibility for ensuring Delvers **do not owe temple damages**. GM explicitly narrates **300 gp to each** at acquisitions. Kuo-toa **planned next-day job**, not a fight or departure. |
| ~01:26–01:48 | **Hidden main-altar shaft** in temple is different from prior **Hall of Penance stair**. Carving and physical structure echo woodland ruins, but no demonstrated identical site/cosmology. A drone becomes audible, an elf collapses; cause **not proven**; **wooden cover is restored**, no descent attempted. Sultan appears with wood badge; tells Koh he wants to see sash, but **it is not yet retrieved at that moment**. |
| ~01:48–02:21 | **Koh later physically retrieves the sash** in the neighborhood square; his repair proposal becomes **actual studded leather purchase for 45 gp**, old buckles passed to shop. All three buy **Water Breathing potions**. Krandal's **+1 shield / Detect Thoughts scroll** checkout and offered prices contain contradictions in dialogue, final checkout **1,000 + 200**, while **+1 shield physical pickup is promised tomorrow**. Evelyn purchases **Goat of Travail for 300 gp**, **not summoning it**; +1 armor left for enchantment and due morning, **not currently worn**. Do not substitute high-priced Goat of Terror or invent magic +3 shield purchase from user-interface bookkeeping. |
| ~02:22–02:49 | Koh notices possibility of reaching **unconscious wife through Psionic Whispers**, but use is spent, **no contact**. Brother Maynard's **Rianu Keeves** spelling and repeated finger-tap remain text-only, pattern transcription unsettled; **two elves unresponsive**, not demonstrated common cause. Maynard gives Krandal **Amulet of the Devout +1** as historic **Dain Proudface** heirloom (attribution is his testimony). Evelyn and Margaret discuss possible Alter Self cover for noon bronze ball meeting, **not carried out**. |
| ~02:49–02:53 | **Level four confirmed by GM for next episode** and rest planned; not a played detailed level-up, chosen feat, overnight scene or mission to fish people. Episode audio has the out-of-game show/network outro to near **02:52:48**. |

## Listening targets and limitations

Audio/SRT alignment is prerequisite for ~00:24–00:30 cube death; ~00:49–00:55 hook horror final blow and horn's condition; ~01:04–01:09 horn/trophy submission; ~01:17–01:24 paid amounts and fish job; ~01:34–01:46 ancient-carving/shaft and sound; ~02:08–02:21 purchase prices and delivered-versus-pending; ~02:31–02:48 **Rianu Keeves, Dain Proudface, the tap sequence**, and ~02:49 level four. The use of repetitive/hum/cue distortions is text evidence only, **not audio-confirmed omissions**. Never infer biological relationship among monster types or cause of elves' unresponsiveness from mere temporal association.

[Episode dossier](../delvers/episodes/S1E09.md) · [Delvers queue](../delvers/REVIEW_QUEUE.md). Original SRTs/MP3 unmodified.
