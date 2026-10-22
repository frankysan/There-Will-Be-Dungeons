# February 2020 bonus — dual-ASR text comparison (2026-10-22)

> **Two ASR exports of one cast/GM Q&A (~34:01); not a played adventure and not independently audio verified.** [Bonus dossier](../episodes/BONUS-2020-02.md). Source subtitles have not been changed; no independent human truth text, recording checksum or ASR rerun.

## Transcription inventory and method

| Source | SRT cues | First cue / last end | Normalized words |
| --- | ---: | --- | ---: |
| [Parakeet processed](../sources/Bonus%202020-02%20-%20February%202020.parakeet.processed.srt) | **674** | **00:06.56 / 34:01.29** | **6,322** |
| [Qwen Q8 / Canary CTC / Nemotron-labelled](../sources/Bonus%202020-02%20-%20February%202020.qwen-q8.canary-ctc.nemotron.srt) | **1,042** | **00:06.64 / 34:01.32** | **6,457** |

Extract the cue content in timestamp order from both SRTs, strip `(speaker N)` labels, lowercase, remove apostrophes and punctuation but keep Unicode letters/digits, normalize whitespace and compute **unit-cost Levenshtein distance on complete word-token sequences**, including intros and outros. Result: **459 minimum token edits / 6,322 Parakeet normalized tokens = 7.26% first-export-relative text disagreement**. **This is *not* audio-referenced word error rate, an accuracy ranking, or a verified false-positive/omission count.** Word counts and caption counts reflect each ASR's segmentation/output, not independently known words actually spoken. Precise Qwen/Parakeet decoding, training/model versions, hardware, time use and source audio checksum are unknown from these files. Labelled model names are derived solely from filenames.

## Comparative reading: high-stakes terms and meanings

| Recording time | What the two texts suggest | Status / required evidence |
| --- | --- | --- |
| **00:06–00:45** | Parakeet renders the program's actual title clearly; Qwen garbles **“There Will Be Dungeons”** as **“Roby Dungeons”**. Both hear host framing this as **“January and early February 2020.”** | The February archive filename is **release label**, not proof of exact recording date; Scott says non-members wait about a week. Check release metadata separately if precise chronology matters. |
| **01:00–04:30** | Backup name **Hack Loman/Hackloman** and roleplaying advice; both report Scott prefers character voice/heart over min-maxing. | **Backup design not active PC**. Exact alternative name spelling needs audio/written character sheet. |
| **04:30–12:00** | Beau's arguments against **DMPC**, inspiration as encouragement for quieter players, and remarks on starting D&D. | Production commentary, no rules correction to the played Wastes sessions. |
| **11:45–12:30** | Both quote cast as being **at episode 91 that night**, nine episodes away from E100. | This is a **spoken production-position claim**, not exact recording day, future narrative plans or a played E091 scene. Bonus knowledge is chronologically later than currently documented E089. |
| **14:40–17:10** | Beau describes topical **Neimoidian/Newt Gunray voice** imitation; **Lizardfolk/Game of Thrones families and names**; one voice's phrase **“podcasting was fishing”** ambiguous. | Safe to attribute inspirations without creating canonical in-world adaptations or specific real-world NPC identities. |
| **17:30–21:15** | Scott/Beau discuss **Nash's Solar Mines**, **Master Beltnotch**, name **“Slow Peters,” already used in [E073](../episodes/E073.md) for fire elementals at the Solar Mines**, and a built **“micro sun”**. Both agree on broad sense but exact term and engineering remain unverified. Beau says he knows **Nash's parentage**, not the details. | Distinguish **E089 Nash's in-character memory of forced radioactive energy** from **out-of-game creative shorthand**. No return expedition or baby/parentage revelation performed. |
| **21:10–25:00** | Kyle/Beau discuss **Eye of Groxl**, shield→flaming sword, and alleged **“God Killer”**; transcripts supply several phonetically inconsistent **Grojil/Grozil/Grogil** variants. | **Groxl canon spelling independently user-confirmed**, do not create separate named gods. The god-killer label is deliberately unresolved, not a verified divine feat. |
| **25:00–28:05** | Jon says **Nothing was intentionally limited in spontaneous speech/planning**; question asks for alternate humiliation if Vorel lost to Kanja. Cast admits **no coordinated backup trick**, with a pantsing joke. | This is **retrospective non-played hypothetical**; E087 result remains Vorel's win plus magic disc. |
| **28:00–29:20** | Listener wonders whether Nash's future elven/dragon-heart child might be a hybrid; **Beau explicitly refuses to reveal information**. | Do not assert the child is **dragonborn**, born, or any other confirmed physical condition. |
| **29:15–30:40** | Jon says **Diontalus's three-month absence after Tietkalla was his choice** so the cynical patron could await Stanley's downfall; actual future **“told you so” never delivered before extraction/removal**. Both ASRs align on the core statement. | **Player motivation/interpretation**, not a new three-month in-world dialogue, prophetic guarantee or proof of extracted crystal's present location. |
| **30:45–33:25** | Beau recalls **16 fighter concepts** and reads ideas for **Archibald, Scrumptious, fencer Fochirolass/Forcirullas (?) and Buster Balls McBuster**. Specific species of chef is garbled, likely **arakocra**; Archibald's demon patron **Abaddon** belongs to the sketch. | **Draft/unused combatant bios**, not asserted playable encounters or actual Sigil Abyss cosmology. Original character/DM design document required for definitive spellings. |

## Consequential discrepancies and further experiments

**ASR names:** test listener-audio recognition of **Hack Loman**, **Slow Peters**, **Fochirolass**, **the chef arakocra**, **Nash's child's earlier elf partner name**, and “Groxl.” Repeated cross-model disagreement around unusual lore and invented names **does not establish which recognizer is correct**. For *Groxl*, user-supplied canon spelling already resolves the label without treating phonetic machine spellings as distinct entities.

**Transcription process decision:** Preserve both SRT outputs unedited. The current material cannot measure genuine audio omissions, hallucinations or diarization reliability; **do not report 7.26% as ASR accuracy** or assign one model superiority from this. Audio listening should prioritize **~17:45–21:10**, **~21:20–24:00**, **~28:15–30:40** and **~31:00–33:15**, ideally with original Beau character notes for unused concepts.

**Documentation scope decision:** Treat February bonus as **cast/GM retrospective at E091-era production**, not another episode after E089 and not a license to backfill E090 or mark the teased Solar Mines trip/child genetics as accomplished. [Review queue](../project/REVIEW_QUEUE.md) · [model tests](../project/MODEL_TESTS.md).
