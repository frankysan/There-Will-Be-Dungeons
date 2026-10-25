# Delvers S2E02 — Why Palor When you Can Pay Later: ASR comparison (2026-10-25)

**Corrected archive ID:** **Delvers S2E02**, a **played Hooper–Goodwine “Wight Wedding”** session featuring guest Bo Schwartz as the Great Daufante (name ASR provisional), not out-of-game bonus or Season One. Episode explicitly says **May 1, 2021** on air; release metadata not independently audited. Initially **clean connected `main`** and pinned GitHub SHA **`e82cc0d9ec5ae818c044ae0fcffdcd7593589238`**.

| Input | Exact source | Git blob | SRT cues | Normalized tokens | Final end |
| --- | --- | --- | ---: | ---: | --- |
| Primary | [Parakeet processed](../sources/Delvers%20S2E02.%20Why%20Palor%20When%20you%20Can%20Pay%20Later.parakeet.processed.srt) | `ed501751e06a63c6567359f318ddc8633f174341` | **2,660** | **24,426** | **02:48:54.060** |
| Independent secondary | [Qwen Q8 / Canary CTC / Nemotron-labelled](../sources/Delvers%20S2E02.%20Why%20Palor%20When%20you%20Can%20Pay%20Later.qwen-q8.canary-ctc.nemotron.srt) | `8e2a08d1f4a192b2513f678f9327deb898663cd7` | **4,328** | **24,555** | **02:48:53.970** |

**Exact full-export normalized ordered word Levenshtein: 1,835 edits / 24,426 primary words = 7.51% inter-ASR disagreement.** Secondary is **+129 normalized words**, final timestamp **0.090 seconds earlier**. **NOT WER, accuracy, audio-confirmed omissions, hallucination count or time-aligned substitution rate**.

Method: parse both complete SRT cue bodies in their order, drop cue indices and timecodes; remove optional `(speaker N)` decorators, Unicode lowercase; delete straight/curly apostrophes without spaces; replace all non-Unicode letters/digits with separators, split normalized words. Two-row unit-cost ordered edit-distance dynamic program constrained to **4,500-token diagonal band**. Obtained **1,835 edits strictly below band**, so no path exiting band (which already requires at least 4,500 insert/delete operations) can be better: **exact global edit distance**. Entire Parakeet chronologically reviewed; Qwen parsed completely for metric and **selected high-stakes windows read**, not exhaustive independent semantic Qwen review. No audio listening or run-settings confirmation.

## High-risk disagreements and boundaries

| Source clock | Question / verified-text boundary |
| --- | --- |
| ~00:03–00:28 | Guest stage title **Daufante/Daufonte**, extended hall epithet, **Grandfather Aurelli/Orilli Hooper**, family names and payment. Both exports support **separate contract, 27 × 10 gp advance for wizard**; exact guest total vs three Delvers share not reconciled. **W-I-G-H-T explicitly spelled** for quest, rather than ordinary “white.” |
| ~00:28–00:31 | Snake Island **volcano/gnome** fragment plus **two psychic daggers unlock**; not proof gnome permanently died or curse identity. |
| ~01:20–01:30 | Evelyn proposes **Find Steed elk**, then player corrects 10-minute casting and **actually deploys Goat of Travail** with Daufante Invisibility. **Twenty doves already dead, two lifted for visual effect**; missing birds' cause not proved. |
| ~01:30–01:57 | Glowing red eyes **knife-duck slain by Krandal Sacred Flame**, no hit on Goodwine. Unseen moving black footprints near tents not identified. Krandal collects **220 gp equivalent**, not 220 coins plus all gem value. |
| ~01:56–02:21 | Hamlet hears **murder and Deck of Many Things rumors**; under **Charm Person** old Goodwine **confesses beating/hanging older Hooper and leaving corpse unburied**. **Confession is NPC account**, not an independent flashback. Deck later recovered, not merely rumored. |
| ~02:21–02:36 | Animated tree **controlled/conducted through noosed wight**, Krandal critical separates and stops tree, **Daufante's two seven-missile volleys kill wight**. Evelyn grapple **fails**, Koh mostly defends Goodwine and is struck. |
| ~02:36–02:48 | Wizard **Mage Hands deck and carries in bag without drawing**, agrees **forfeit payment share to Delvers**. Goodwine/Connor **actually bury corpse**, no trial/public announcement. **Koh possibly pockets severed right hand**: right hand missing and jacket movement observed, precise cut not unequivocal. **Black sludge at tree roots** is observed, but no source confirms same mechanism as Dawnless Dunes slime. |
| ~02:48 | Wizard departs **following morning**, future theatre invitation to Evelyn only; guest farewell and future teased episode **out-of-game**. |

Audio verification remains essential for exact proper nouns, timing and item handoff. [Dossier](../delvers/episodes/S2E02.md) · [queue](../delvers/REVIEW_QUEUE.md). Original `sources/` untouched.
