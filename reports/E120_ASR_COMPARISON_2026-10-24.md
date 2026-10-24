# E120 — complete Parakeet/Qwen ASR comparison (2026-10-24)

> **The Wastes corrected S1E120 — Fly Like An Eagle; Arc Five played episode, owner catalogue published September 28, 2020.** [Episode dossier](../episodes/E120.md) · [Arc Five](../narrative/ARC_FIVE.md). **Both existing exports read from first cue through closing FrogPants network outro** using bounded base64 binary reads on clean workspace `main` HEAD `76cb96b3cba5621e6ceaa63a8ea7ed7383bb597a`. **Text-only comparison, no listening or ASR rerun**, no source modifications.

## Source inventory

| Export (filename label only) | Size (bytes) | Workspace SHA-256 | SRT cues | First start | Last end | Normalized words |
| --- | ---: | --- | ---: | --- | --- | ---: |
| [`The Wastes S1E120. Fly Like An Eagle.parakeet.processed.srt`](../sources/The%20Wastes%20S1E120.%20Fly%20Like%20An%20Eagle.parakeet.processed.srt) · Parakeet processed | **276,126** | `b8fddbea23961df4284d024d444e741ca84accafc2107fedc2a56e89318d9144` | **2,817** | **00:00:14.960** | **02:45:12.020** | **25,127** |
| [`The Wastes S1E120. Fly Like An Eagle.qwen-q8.canary-ctc.nemotron.srt`](../sources/The%20Wastes%20S1E120.%20Fly%20Like%20An%20Eagle.qwen-q8.canary-ctc.nemotron.srt) · Qwen Q8/Canary CTC/Nemotron-labelled | **382,320** | `293b63cdc3ca53f82635618c8427bb4271b3bee887d66c6fed717b420f65803a` | **4,758** | **00:00:15.040** | **02:45:11.720** | **25,768** |

**UTF-8 decoded character lengths:** Parakeet 276,126; Qwen 382,274. The first cue start differs by **0.080 seconds** and final ending by **0.300 seconds**. They span corresponding sections, but **underlying audio file identity, sample-rate, exact ASR settings, performance and diarization are not independently verified**. The additional Qwen cues reflect segmentation differences, not more confirmed spoken content.

**Reproducible calculation:** Parse all SRT blocks containing timestamp arrows; discard cue indices, timing lines and optional `(speaker N)` labels; join cue bodies in chronological order. Lowercase; remove ASCII/curly apostrophes to join contractions; replace everything except Unicode letters/digits with whitespace; split into tokens. Compute **unit-cost ordered full-sequence word-level Levenshtein distance** (arbitrary-width bit-vector DP) using processed Parakeet as the reference, including prelude and credits.

**Result: 2,288 ordered word edits / 25,127 Parakeet words = 9.11% inter-ASR disagreement** (unrounded **9.1057428264%**). Qwen contains **641 more normalized word tokens**. **This is not measured WER, audio transcription quality, proved Parakeet omissions or Qwen superiority**.

## High-impact reading checkpoints, cross-export observations

| Approx recording time | Evidence and potential model/editorial confusion | Safe provisional conclusion / next check |
| --- | --- | --- |
| **00:00–00:05** | Cast's alliterative prior-episode recap says **Diontalus “had been released and ready to return”**, a **retelling of Stanley's prior fear**, not a depicted E120 escape | Do **not** independently canonize possession or crystal release from recap |
| **~00:20–00:29** | **Stanley polymorphs into T. rex**, chest-height bear with **deer antlers**, enormous hind legs, small bear forelimbs and reptile-like head; creature “Chester” named | **Observed monster**; exact bearsaurus/Beirasaurus spelling still uncertain, lab history unproven |
| **~00:24–00:27** | **Nash readies and actually triggers *Haste*** on Vorel when combat starts; recognizable improvised rhyme in both exports; ***Haste* requires concentration and does not run for many forest minutes first** | Preserve distinct performed magic-phrase evidence in [Nash phrase register](../world/characters/nash-spellcasting-phrases.md); do not count declined *Reduce* as cast |
| **~00:27–00:54** | Critical T. rex bite and grapple, Chester's 50-foot tree jump, multiple wounds and dangling entrails; **Hope pulls on entrails and brings him down**, causing a tree fall; **the GM explicitly narrates Chester dead**. Hope **pinned alive/suffocating**, Vorel **actually lifts carcass and frees her** | Do not report Chester escaped or only knocked unconscious; do not report Hope killed by fall |
| **~00:59–01:12** | Omnom calls Vorel **Great Fang** and explicitly withdraws his own doubts he might deserve the rank; Dilo feels outclassed; murderous sparring **proposed then rejected** | **Renewed Great Fang recognition**, not a second formal coronation or actual Omnom/Dilo duel |
| **~01:12–01:35** | A “grateful” group of **six talking deer** with a stag leader seeks food and points to mushrooms in a northern cave | All six prove **disguised hostile elves**, making their deer testimonies unreliable worldbuilding |
| **~01:31–01:39** | Private insight prompts Stanley's ***Dispel Magic***, one deer changes into elf with **red eyes/black veins**; remaining five reveal elf identities and attack | **Actual magical concealment broken**; no proven Diontalus possession from red eyes |
| **~01:39–02:05** | Hope's blade silences one caster but its blood blinds her; Dilo lands unarmed strikes. ***Mass Suggestion*** compels **Hope/Omnom to imitate squirrels**; other ally saves, *Cone of Cold* frees Hope and kills/injures one enemy; *Entangle* holds Hope/Stanley | Separate **short-lived magical behavior** from permanent shapechanging or departure; Dilo's apparent aid precedes his betrayal |
| **~02:00–02:10** | Nash's ***Chain Lightning*** aimed at **four separate hostile elves**; Stanley's announced ***Destructive Wave*** begins and then triggers a pre-readied hostile action | Nash **does not target allies**; observed effect and game-table roll rulings, not guaranteed official RAW |
| **~02:06–02:12** | **Dilo calls a cue**, elf casts a **sealed moving sphere around Hope**, and **throws a wand/controller to Dilo**, who **flees with her**. Stanley's ***Destructive Wave*** resolves after they exit; GM reports **six hostile elven bodies**, not seven | **Dilo visibly betrays and kidnaps Hope**; **Dilo not hit or killed by Stanley's wave**. No proof his identity equals Diontalus |
| **~02:09–02:15** | **Private scene:** Hope tries ***Teleport* via Hand**, aiming at party and using a slot; **it fails while Hope remains breathing inside moving sphere** | No successful escape, no arrival with friends, no certainty *why* the sphere defeats teleport |
| **~02:12–02:30** | Stanley ***Polymorphs into giant eagle***, watches blue sphere run into mountain opening; Vorel finds **unusually long elf tracks** and signs of long-ago large creature | Scout truly finds cave; does not independently prove bear reanimated or second specimen |
| **~02:33–02:45** | Nash **cuts then ingests glowing mushroom**; particles induce sneeze, then **mouth emits blinding light when open**. He volunteers to illuminate as party proceeds | Real mouth-light effect; do **not** assume edible species safe, permanent ability, hallucination or successful delivery for Nobieri |

### Specific transcript caution

- The **recap's Diontalus release** sounds declarative but refers back to **Stanley's E119 inference from a Principle warning**; E120's Dilo betrayal increases suspicion, **not confirmation of entity identity**.
- The casts' casual combat use of “lightning damage” for ***Destructive Wave*** competes with the character's read-aloud spell text specifying **thunder plus radiant/necrotic**. The GM uses a lightning visual. **Separate visual flavor/table narration from rules text and physical outcomes**.
- The **second fight's count** is **six illusory deer/caster elves**, all killed, with **Dilo an additional separate agent who escapes**. Do not infer seven mage casualties or resurrect frozen mage to preserve tally.
- Exact ASR proper-name spellings **Dilenoria/Dylanoria/Dillinoria**, **Chester's bearsaurus name**, and **the north cave/Elhandar regions** still require original audio or maps.
- Distinguish **Stanley's performed T. rex and eagle Polymorphs** from Nash's **unperformed plan to become a dragon** or *Reduce*.

**Highest-value listening:** ~00:24–00:26 performed ***Haste* incantation**; ~00:48–00:57 fall / rescue; ~01:30–01:38 deer/elf magical identity; ~02:05–02:14 Dilo wand handoff, ***Destructive Wave*** six kills and Hope ***Teleport* failed**; ~02:34–02:45 fungal visual/saving throws/mouth light. No source audio has been verified.

**Publication pointer:** E119 (September 21, 2020) → **E120 (September 28, 2020)** → **BONUS-2020-10 — October 2020**, public-release bonus **not yet documented in an episode dossier** → corrected **S1E121 — The Heart of The Matter** (owner catalogue October 12, 2020). Their later descriptions are **not proof of E120's unseen outcomes**.
