# E121 — full Parakeet/Qwen ASR comparison (2026-10-24)

> **The Wastes corrected S1E121 — The Heart of The Matter; main Arc Five session**, following E120's mushroom-cave cliffhanger. [Source-first dossier](../episodes/E121.md). Both **entire SRT exports** retrieved by bounded binary reads through **02:52:19** on clean connected workspace `main` HEAD `8ee81c26c196ade687ae4435715a2565bc534757`. No audio listening, source modification, external handout or ASR rerun. Labels inferred **only from source filenames**; source waveform equivalence, settings, speaker assignments and performance are unverified.

## Provenance and reproducible measurements

| Export | Source and hash (workspace SHA-256) | Bytes | Cue count | First start | Last end | Normalized words |
| --- | --- | ---: | ---: | --- | --- | ---: |
| **Processed Parakeet** | [`The Wastes S1E121. The Heart of The Matter.parakeet.processed.srt`](../sources/The%20Wastes%20S1E121.%20The%20Heart%20of%20The%20Matter.parakeet.processed.srt) · `4740fc72f76e2f5f51a123db3f209c990afeae98727a9a9f425fe37c103a3456` | **259,738** | **2,645** | **00:00:12.960** | **02:52:19.630** | **23,724** |
| **Qwen Q8/Canary CTC/Nemotron-labelled** | [`The Wastes S1E121. The Heart of The Matter.qwen-q8.canary-ctc.nemotron.srt`](../sources/The%20Wastes%20S1E121.%20The%20Heart%20of%20The%20Matter.qwen-q8.canary-ctc.nemotron.srt) · `8a59b36d47a918c4f619883c55dfc924aad98d7095f3ebf2d7312a9d0bd58bf5` | **361,817** | **4,533** | **00:00:13.040** | **02:52:19.280** | **24,074** |

Decoded UTF-8 character lengths: Parakeet **259,738**; Qwen **361,755**. First-cue clocks differ by **0.080 seconds**, last-cue endings by **0.350 seconds**; similar coverage does **not** prove exact upstream acoustic identity. Each full export includes host introduction, prior-episode recap, gameplay, break/intermission, session ending and network outro. Cue density reflects independent segmentation, not measured recognition recall.

**Normalization:** Parse every SRT block containing a timestamp arrow; remove index/timing lines and optional `(speaker N)` markers; concatenate speech in order; lowercase; remove straight and curly apostrophes (joining contractions); replace all remaining non-Unicode-letter/digit characters with spaces; split nonempty words. Compute **exact unit-cost full-sequence ordered word Levenshtein** using arbitrary-width bit-vector dynamic programming, normalized by Parakeet token count.

**Result: 2,284 ordered word edits / 23,724 Parakeet words = 9.63% inter-ASR text disagreement** (9.6274% unrounded). Qwen has **350 more normalized tokens**. **This is not WER, audio accuracy, verified omitted speech or hallucination, and no model can be declared superior by token volume**.

## Source-critical distinctions

| Clock | Text comparison and importance | Safe claim / review |
| --- | --- | --- |
| **00:24–00:42** | Dilo greets **Valier Ornath (?)**, says he wants Hope's body/Hand, admits deceptive Chester hunt; **Stanley directly identifies Diontalus**. Opponent claims Principle's help and restoration in Feywild | **Identity now physically confirmed E121** through direct apparition, not merely suspicion; **Principle aid and completed reconstruction are unverified adversarial claims** |
| **00:30–00:35** | Stanley rolls 18 on ***Dispel Magic*** but **sphere remains**, triggering empathy-grenade threat | **Spell attempted and played result fails**, not a broken sphere or a confirmed printed spell interaction |
| **00:43–00:52** | Hope's engineering 17/13 reveals **red/white/green wires**, she **pulls white**, grenade triggers/blinds, others don't automatically explode | White was an **actual failed attempt**; planned protective *Alter Self* not completed as a warforged transformation |
| **01:03–01:09** | Stanley giant-ape fist **knocks Dilo's body aside**, and a **blue ghost-like Diontalus stands separately**; corpse later confirmed breathless | **Separate physical Dilo corpse and active Diontalus**, not Dilo surviving as a willing party member; former consent unknown |
| **01:09–01:22** | Ethereal scythe and necrotic hits; GM adjudicates lasting **Str/Dex reductions**; ***Destructive Wave* hurts Diontalus** with legendary resistance | **Played condition** without assuming permanent post-session rules; radiant vulnerability independently identified later by Eye |
| **01:22–01:26** | ***Dimension Door*** to Hope's ledge, Stanley takes device but **does not press detonator**; shouts **“lemon tree”** | **Party intervention starts**, no sphere release or detonator experiment |
| **01:24–01:41** | Nash **rejects casting *Enlarge* on Vorel**, casts adult-black-dragon ***Polymorph***; Vorel attacks; **Omnom's grab fails**; roots restrain party | Keep contemplated spell distinct from actual *Polymorph* and failure to hit ghost |
| **01:45–02:02** | Vorel takes **entire Necklace of Fireballs** from Omnom, with **initial fumbled roll and no-attunement rule explicitly rewound**. Approx **five beads** adjudicated, resolved as seventh-level **12d6** fireball, damaging foes/allies and burning off roots | **Whole necklace is thrown/spent**, no unused necklace remains; exact charge count was **retroactive approximation**, arithmetic chatter inconsistent |
| **02:04–02:15** | Diontalus's **necrotic/lightning chain** hits three; subsequent GM/characters acknowledge **Omnom destroyed, only feet/stumps remain** | **Omnom actually dies**; not just unconscious, though no later resurrection known at this cutoff |
| **02:10–02:22** | Vorel's **Eye of Groxl** reveals **radiant vulnerability**, scythe scores persist; dragon invades, grapples Diontalus, is mortally wounded | **Diontalus flees through wall alive**, no banishment/kill, new black dragon helps voluntarily |
| **02:22–02:29** | Nash uncontrollably erupts in **fire then acid**; Stanley reaches 0 HP; Nash collapses into private heart/fire vision | **Uncontrolled effect**, not another deliberately worded Nash spell; Stanley not dead |
| **02:29–02:40** | Vorel expends **all ten uses** of Stanley's healer's kit; injured dragon restores **73 HP each to Stanley, Vorel and Nash** | Real stabilization and subsequent restorative magic; **Omnom and Dilo not revived**, Hope not released |
| **02:39–02:48** | Dragon identifies itself as **earlier Earth-desert captive**, claims Nash's heart has **its mother's dragon signature**; says messages involved involuntary eruptions | Dragon's testimony and physical scars observed, **ancient rescue plan merely offered, not explained** |
| **02:47–02:52** | Name ambiguities: mother **Kaz Desiree / Cas de Jurey (?)**; son **Yoshalar / Shallar (?)**. Nash's mechanical heart actually opens, golden-orange maternal dragon manifests, soothes son and sings | **Spectral emergence shown**. Audio/handout required for correct orthography and whether heart contains the entire dragon versus essence/signature |

### Editorial hazards

- *E119–E120 versus E121:* prior **Dilo/Diontalus concern was genuinely unverified** at its earlier cutoff. E121's **direct spectral emergence identifies Diontalus**; never rewrite prior dossiers to pretend characters then knew the truth.
- *Diontalus is not killed:* he survives the dragon's assault, moves through solid rock and threatens to return.
- *Two apparent deaths, different outcomes:* **Dilo's breathless physical body and Omnom's burned/severed remains** remain on the ground. **Stanley goes down but is stabilized and then healed**. Do not conflate the physical Dilo body with the separately moving Diontalus.
- *Hope's prison persists:* **attempted white-wire disarm, further successes/another failed device, scratching and stabbing, third-level *Dispel Magic*, broken wand and unpressed detonator** do not free her. No evidence to claim all grenades disarmed.
- *Item inventory:* **entire necklace discharged** as one Fireball; GM's final five-bead approximation is not a reliable pre-action inventory census. **Healer's kit all ten uses spent**. Wand **snapped but sphere intact**, detonator not pressed.
- *Speaker/private knowledge:* Nash's **heart/fire vision is private**; later dragon's visible speech and spectral phenomenon are shared with present listeners but no automatic knowledge to **Hope** in sealed soundproof sphere or characters back in cottage.
- *Spell interpretation:* GM's ability loss, magical scythe, necklace level/damage, black-dragon uncontrolled breath and dragon healing are **episode outcomes**, not external validation of official D&D mechanics.
- *No title/rhyme overreach:* Vorel's **Eye of Groxl and Great Fang history** are not a newly awarded title. Nash performs *Polymorph* and involuntary discharge, **without new improvised rhymed spell speech**.

**Priority listening:** ~00:36–00:42 **Diontalus bargain/Principle claims**; ~01:06–01:10 **separate Dilo ghost**, ~01:45–02:01 **rewound whole-necklace Fireball and counts**, ~02:04–02:15 **Omnom destruction**, ~02:20–02:29 **dragon assault and involuntary blast**, ~02:35–02:52 **healing, Earth-desert identity, mother/son names, heart apparition**. All are **transcript-only**.

**Next source:** correct Wastes S1E122 expected by series ordering; **exact basename not independently verified here**, do not invent a link.
