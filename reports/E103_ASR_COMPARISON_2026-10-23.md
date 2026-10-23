# E103 — Parakeet/Qwen complete transcript comparison (2026-10-23)

> [E103 episode dossier](../episodes/E103.md). **Text-only dual-ASR review; no audio listened, no human reference transcript, no verified model ranking or speaker diarization.** Corrected Wastes **S1E103 — When in doubt, burn it**; host states **Sunday, May 10, 2020**.

## Full-text inventory and metric

| Input SRT | Subtitle cues | Last cue | Normalized word tokens | Git blob SHA |
| --- | ---: | --- | ---: | --- |
| [Parakeet processed](../sources/The%20Wastes%20S1E103.%20When%20in%20doubt%2C%20burn%20it.parakeet.processed.srt) | **2,639** | **02:44:12.950** | **23,243** | `e0005ca635cbb78cca98c73c1cbc713ea93be4d7` |
| [Qwen Q8/Canary CTC/Nemotron-labelled](../sources/The%20Wastes%20S1E103.%20When%20in%20doubt%2C%20burn%20it.qwen-q8.canary-ctc.nemotron.srt) | **4,551** | **02:44:12.760** | **23,672** | `f9176fa23fb60865979b3ece53047450604cd11c` |

**Method:** Read both complete SRTs from GitHub default branch. Split numbered blocks; discard cue indexes/timestamps and `(speaker N)` markers; join cue text chronologically, lowercase, delete straight/curly apostrophes, replace any non-Unicode letter/digit sequence by space, split into tokens. Exact ordered **unit-cost Levenshtein word edits** using two rolling rows: **2,198 edits / 23,243 Parakeet words = 9.46% text disagreement**. Qwen has **429 more normalized tokens**; this is **not** a verified count of Parakeet omissions, transcript accuracy, audio WER, hallucinations or model superiority. Cues are independently segmented.

**Reproducibility limits:** Git SHAs identify SRT Git objects, **not audio fingerprints**. Workspace was clean at **`fac605a28583cb194ca0999713d11baa132b1db2`** when E103 analysis began; these source contents were read from connected GitHub, **not byte-compared against the checkout**. No new transcription run, decoding/VAD/build/version log, runtime metric, GPU resource record or direct audio listen. Separate [E103 ARK evaluation](E103_ARK_EVALUATION_2026-10-23.md) concerns different pipeline experiments, not a third gold/reference transcript in this comparison. **No raw SRT was changed.**

## Critical source-to-source observations

| Recording time | ASR alternatives or notable interpretation |
| --- | --- |
| 00:00–00:05 | Both preserve **May 10, 2020** as spoken episode date. Alliterative recap concerns **E102**, not E103 gameplay. |
| 00:04–00:20 | **Spatulo actually follows** Hope/henchmen through Tietkalla bedroom portal. **Steerious Business** is the **user-confirmed spelling** of Jon's minotaur **steer/serious** joke; machine readings include “Serious,” “Sterius” and “Mysterious Business.” Dr. Spider has equipment with a baby-containing tank; nature unverified. |
| 00:18–00:30 | **Celibus Stump** is the prior [E011](../episodes/E011.md) working name for the Slavetown businessman; E103 ASRs alternate “Celivus”, “Syllabus”, etc. Craft-house speaker's name sounds “Keith Ickshil (?)”. **Hope's “Touch of Death” is corrected at table to Finger of Death**; she really kills the chancellor with **54 reported damage**. |
| 00:30–00:52 | Hope shoots **Kuromakishi (?) guards**, casts **Slow**; Dr. Spider's **Guardian of Faith** manifested golden spectral infants kills charging men; **Steerious** cuts men down, **Rages with scorpion tail** and deploys an **echo**. Custom subclasses and DCs require sheet/audio verification. |
| 00:52–01:36 | Blood Skunk's custom **Critical Fortunes** sends swords away after natural one, then he **conjures a giant snake**. ***Hunter's Mark* considered but not cast** because concentration on snake. Hope **successfully grapples** a fleeing orc and renders him unconscious rather than killing him initially. |
| 01:36–01:50 | **Steerious kills the prisoner** during an attempted interrogation; Blood Skunk finishes last other guard. **Dr. Spider actually casts Speak with Dead on Celibus**; corpse says queen absent **three months**, alleges **Principle owns everything**, speaks of Liberators/Jeweler. ***Speak with Dead* does not force truth**, and chancellor remains dead. |
| 01:51–02:10 | Sky crack, unusual rain, **Jimster** and active **Golden Sands**. **Emenil** says political quarrel with **Nobiery**, Principle-linked Celibus interim rule, disrupted incoming train shipments, possible **inquisition** and **three alleged disappearances**. Banker/house name **Grimoire Macab (?)** uncertain. This is **attributed testimony, not witnessed kidnapping**. |
| 02:10–02:15 | Hooded Voice orders Hope to murder **Emenil** then a stranger; **Hope refuses**. GM says Hand powers **locked until an evil act**; precise feature subset not independently exercised here. |
| 02:14–02:24 | **Blood Skunk's flaming arrow ignites the empty railway station**; **Dr. Spider uses Wall of Fire** to surround it. Residents mount bucket brigade. **No on-screen deaths, rebuilding, citywide war or post-act Hand-power test**. |
| 02:24–02:41 | Ship officer/elf captain name variants **Bubbin Walls / Bubbinwols / Balinwols (?)**; orc mercenaries separate from ship operators. Nash Arcana **16** suggests falling moon, no measured trajectory. Stanley denies **other** memory edits while admitting **Alentris's E102 alteration**; no further edits shown. **Saucer squadron and cloaked heavy craft open fire** at airship: action begins, outcome unplayed. |
| 02:41–02:44:13 | Cast teases upcoming encounter, then outro. Both SRTs include a separated **~02:44:11 “Awesome show today, you guys!”** cue after FrogPants network credit; audio placement not listened to. |

## Research boundaries

**Not the same as an event timeline:** In-fiction **Celibus, Jimster and Emenil** tell competing histories of recent politics; missing citizens, true culprits and the legitimacy of chancellorship remain to be reconciled. The later [June 2020 bonus](../episodes/BONUS-2020-06.md) contains retrospective spoilers, not played E103 actions. **The moon collision and hostile saucer battle continue in E104**, not already resolved in E103. Next priority audio: **~00:04–00:10** names/Spatulo, **~00:18–00:30** chancellor, **~00:40–01:05** custom powers, **~01:38–01:50** corpse, **~02:00–02:14** politics/patron, **~02:14–02:24** station fire, **~02:24–02:41** moon/captain/UFO, **~02:44:11** outro cue. [Review queue](../project/REVIEW_QUEUE.md) · [model testing log](../project/MODEL_TESTS.md).
