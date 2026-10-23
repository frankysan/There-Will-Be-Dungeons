# E093 — We're on a boat: two-ASR comparison (2026-10-23)

> **No audio listening or ground-truth WER evaluation.** Independent text-only comparison of two unchanged SRT exports of the **~02:54:05** E093 episode. [Full provisional dossier](../episodes/E093.md).

## Corpus and method

| Source | SRT cues | Last cue end | Normalized words |
| --- | ---: | --- | ---: |
| [Parakeet processed](../sources/The%20Wastes%20S1E093.%20We're%20on%20a%20boat.parakeet.processed.srt) | **2,833** | **02:54:05.840** | **24,570** |
| [Qwen Q8/Canary CTC/Nemotron-labelled](../sources/The%20Wastes%20S1E093.%20We're%20on%20a%20boat.qwen-q8.canary-ctc.nemotron.srt) | **4,839** | **02:54:05.740** | **25,045** |

Strip SRT numbers, timecodes and `(speaker N)` tags; combine spoken text in chronological cue order; lowercase; remove apostrophes (joining contractions); split on all non-Unicode-letter/digit characters; apply **unit-cost Levenshtein to full ordered word-token arrays** (not timestamp-paired independent segments). Recalculated **2,139 word edit operations / 24,570 Parakeet tokens = 8.71% inter-ASR disagreement**. **This is NOT audio-referenced WER, measured accuracy, validated omissions/hallucinations, or model ranking.** Model exact build, decoding parameters, original media hashes, VAD/segment boundaries, word reference and human listening were unavailable. Raw source SRTs unchanged.

## Particularly important source-sensitive readings

| Approximate window | Agreed account, ambiguity and treatment |
| --- | --- |
| **00:03–00:11** | E092 unnamed airship is **Traveler's Twin** in E093. Captain's proper name inconsistent (**Meart/Miart/Bjart/Yart**) and gender uses were confused in E092; described **loxodon pirate captain** is reliable. **E093 ship name not retroactively applied as an E092 utterance**. |
| **00:11–00:27** | **Mind Master Gerbken Shartlinger actually appears** with **four Crimson Moon-clad figures** and says he brokered ship for Tobacho. His agent offers **dragon-head Amulet of Health (CON set to 19)**. **Nash casts Detect Magic; Vorel declines to wear; Stanley takes and equips**, responding as healed/energized. Older assassin contract still not witnessed. |
| **00:29–00:34** | **Portal opens at end of Dark Below rails; Traveler's Twin actually crosses into Outlands** under power after a momentary drop. Huge central spire, distant Sigil-ring and various Outlands terrains actually observed; captain's cosmology remains her assertions. |
| **00:44–00:58** | **Captain provides sending stone** to contact her at pickup, and **Stanley looks through telescope at besieged White Tower**, confirming visible armies/trebuchets and location, **not relic custody/key box mechanics**. |
| **01:03–01:30** | **Nash transforms voluntarily into a young black dragon**, a distinct ability from **Stanley's E091 giant ape Polymorph**. **Two wyverns and many winged beastmen** attack ship, kill gnomes; dragon acid breath is **acid, not fire**, despite conversational “fire” or “acid fire” shorthand. **Hope hangs off stern** after impact. |
| **01:36–01:55** | **Stanley polymorphs an airborne wyvern into rat**; the rat drops beyond view, **death/reversion unconfirmed**. A beastman wounds Hope's hand and she **actually falls**, but **Nash flies after and catches her**; no fatality, permanent wings or end-state still falling. |
| **02:05–02:45** | **Hope rides dragon-form Nash and shoots**; **Vorel goes below decks to face injured wyvern**, takes real **sting/poison/bite damage** and **kills it with Shatter**. Nash **actually recharges and uses acid breath on boarders**. Any wood/acid damage causal claim remains **unverified**, even though direct wyvern-ram damage is observed. |
| **02:45–02:51** | GM adjudicates **Hope natural-1 misfire hitting Nash (18 damage)** and **natural-20 Scully shot killing flyer (31 damage)**. Scully's critical-hit **True Strike effect** is mentioned; check precise episode-era rules before canonizing beyond this adjudication. **Immediate attackers eliminated, ship still shakes, grey smoke and downward tilt**. No witnessed crash or landing. |

## Carry-forward controls

- **The White Tower is actually sighted and besieged**, an increase in confidence over E091 bishop-only location testimony. **No Fist/locked box viewed or key tried**.
- **Mind Master provides actual present support and a physical magical gift**; his claim of procuring ship and presence of Crimson Moon agents does not prove all past conspiracies. **Gift bearer is Stanley** despite its dedicatory inscription to Vorel.
- **Nash's young dragon form is voluntary** and survives Hope's friendly-fire shot; the dragon mount sequence ends before a documented return to ordinary form.
- **Vorel is poisoned/injured** in immediate combat and no full post-battle recovery is shown; **no claim that he dies or returns Shatter**.
- **The vessel is genuinely launched, and its descent is an unresolved cliffhanger**. No crash, exact damage cause, Fist recovery or Earth-portal crossing supported.

**Listening priorities:** actual proper names for captain/ship; 00:21–00:25 necklace identification/Stanley wearer; 00:45 sending stone recipient; 01:05 black dragon vs spell; 01:45–01:55 rescue mechanics; 02:27–02:44 wyvern poison and possible acid-on-wood damage; 02:46–02:51 friendly-fire/ship cliffhanger. [E094 source](../sources/The%20Wastes%20S1E094.%20Where%20did%20my%20ball%20go.parakeet.processed.srt) remains the next separately bounded episode.
