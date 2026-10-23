# E094 — Where did my ball go: dual-ASR comparison (2026-10-23)

> **Text-only inter-ASR comparison. No audio listened to; no reference transcription; no audio-verified WER.** [E094 dossier](../episodes/E094.md).

## Exact input inventory and reproducible comparison

| Source SRT | Cues | Final end | Normalized words |
| --- | ---: | --- | ---: |
| [Parakeet processed](../sources/The%20Wastes%20S1E094.%20Where%20did%20my%20ball%20go.parakeet.processed.srt) | **2,386** | **02:42:42.330** | **21,574** |
| [Qwen Q8/Canary CTC/Nemotron-labelled](../sources/The%20Wastes%20S1E094.%20Where%20did%20my%20ball%20go.qwen-q8.canary-ctc.nemotron.srt) | **3,729** | **02:42:42.280** | **21,699** |

Parse each SRT into chronological cues; strip cue ID/timecode and `(speaker N)` labels, concatenate transcribed text, lowercase, remove apostrophes (joining contractions), replace non-Unicode-letter/digit characters with spaces, split into tokens, compute a unit-cost **ordered word-token Levenshtein distance** over the full episode. Reproduced **1,324 edit operations / 21,574 Parakeet tokens = 6.14% inter-ASR disagreement**. It measures **recognizer disagreement, not correctness, omissions, hallucinations, WER or diarization quality**. Source audio, gold reference, model exact version/build, decoding/VAD/segmentation parameters, and hardware timing were **not** available; original SRTs unchanged.

## Major source-confirmed outcomes and high-risk details

| Approximate time | Provisional source-backed reading, and audio concerns |
| --- | --- |
| **00:03–00:22** | **Traveler's Twin in descending distress**; captain promises contact; **Nash reverts from young black dragon to humanoid**, pairs **Stanley/Hope and Nash/Vorel** leap and **use Dimension Door scrolls**. Ship seems to crash beyond ridge (**not inspected**); later contact supersedes any inference that everyone died. |
| **00:22–00:30** | **Hope only** rejected by protective tower ward, takes **4 necrotic** and **49 falling bludgeoning damage**, survives; **+2 dagger actually used to try and hold wall**, then she is taken by winged doglike soldiers to **General Carthax (?)**. Three other PCs **teleport inside**. |
| **00:30–00:40** | **Ulvert (?)** recognizable from UBI/Solar Mines intervenes. Demons of Abyss and devils of Nine Hells **assert temporary alliance**. Hope conditionally agrees to retrieve Fist for promised Earth return for **all four**, without proof of later compliance; **GM explicitly changes alignment to lawful good by magic** and describes its maintain-by-good-behavior condition. The forces send her inside, warn an evil act will cause ward ejection; no assured rescue plan for three companions. |
| **00:40–01:03** | **Sir Samson / Sir Clotchup (?) / Walnut** meet Stanley, Nash, Vorel inside tower's closet hallway; Hope **actually arrives later**. Vorel's **divine pregnancy claim is an attempted lie**, not canonical Hope pregnancy. Stanley persuades paladins not to kill her; **Hope tells truth about her demonic encounter**, spurring disarmament. |
| **~01:03–01:30** | **Nash hands over his ball to Walnut** (not a permanent loss); Vorel headbutts knight, companion paladin **fumbles and seriously wounds Samson**, **Stanley heals Samson (8 HP Healing Word)**. Nash grabs Walnut but **he escapes with ball**; broader knights intervene. Do not claim Samson killed or gratuitous party slaughter. |
| **~01:35–02:06** | **Female Knight Commander** and **visible hexagonal chest** inside tower. **Fist custody is her statement, not physically opened/seen**. She **sentences all four to death and immediately stays execution** after Stanley proposes helping bring Fist to **Mount Celestia** with knights. **All four equipment sets returned including Nash's ball**; the **key medallion is inspected then handed BACK to Stanley**, purposefully separate from chest. Golden Euphemius totem **offered/shown**; exactly who accepts/holds it needs audio review. |
| **~02:06–02:20** | **Captain actually calls on sending stone and is alive**; ship needs **about one week of repairs after bad landing/crash**, not total loss. **Walnut escorts party to rooms and kitchen Gregor (?)**. |
| **~02:20–02:38** | **Stanley/Vorel clash over the means of returning home**; Nash pledges to follow Hope; **Stanley leaves medallion key in bag and retires**, not transferring to Vorel. Hope is affected by lawful-good spell, **privately hears “bring us the Fist”**. Voice's identity, origin and supernatural influence **unresolved**. |

## Editorial decisions

- Change E093 **airship descending without known impact** to **E094 seen disappearing beyond ridge with smoke, captain alive reporting one-week repairs**. Never claim permanent destruction, all-crew death or immediate return.
- Track two separate **Dimension Door paired casts and three-inside/one-expelled result**. **Hope really falls for damage but survives**, is captured and returns under **alignment-altering magic**, not original entry. There is **no confirmed change to her biological species or pregnancy**.
- **The hexagonal box is observed; the Fist is not**. The Knight Commander's account and Ulvert's statements are **conflicting interested testimony** about what should happen; don't turn artifact power or divine intent into objective fact without corroboration.
- The Knight Commander **pronounces death but does not execute**; Stanley's argument actually wins time, room/board and returned arms. **Walnut returns Nash's spell ball**. Key pendant **briefly changes hands to commander and returns to Stanley**, and is **later left in his bag**; the dangerous relic's chest **stays in commander's control**.
- **Mind voice at episode end unassigned**: neither Ulvert nor the general is explicitly identified as speaker. Audio verification priorities include the caster/alignment restrictions, ball handover, chest/key custody, golden totem handoff, captain contact and the identity (if spoken) of the final voice.

**Next bounded source:** [E095 — A Cloudy Day](../sources/The%20Wastes%20S1E095.%20A%20Cloudy%20Day.parakeet.processed.srt), exact filename verified; E095 not incorporated here.
