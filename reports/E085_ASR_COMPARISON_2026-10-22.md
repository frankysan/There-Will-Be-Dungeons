# E085 — Always High Kick: two-ASR source comparison (2026-10-22)

> **Text-only comparison, not audio verification.** The two SRT exports refer to **the same episode**. No listening, manual reference transcript, model rerun, WER measurement, audio file hash, run command, performance test or source modification. The purpose is **source triangulation and triage** for the [E085 dossier](../episodes/E085.md). The distinct cue counts **do not measure actual ASR accuracy**.

## Inputs and normalized agreement

| Source under `sources/` | Claimed pipeline based on filename, not recorded configuration | Cues | Caption start/end approx. | Normalized word tokens |
| --- | --- | ---: | --- | ---: |
| [E085 Parakeet processed](../sources/The%20Wastes%20S1E085.%20Always%20High%20Kick.parakeet.processed.srt) | Parakeet processed; model version/settings **unknown here** | **2,855** | 00:00:09.3 / 02:45:54.9 | **24,683** |
| [E085 Qwen](../sources/The%20Wastes%20S1E085.%20Always%20High%20Kick.qwen-q8.canary-ctc.nemotron.srt) | Qwen Q8, Canary CTC, Nemotron per filename; model version/settings **unknown here** | **4,883** | 00:00:03.7 / 02:45:54.5 | **25,001** |

**Method:** extract each SRT's cue text, strip speaker decorations `(speaker N)` and collapse all utterances into original sequence. Unicode lowercasing, removal of punctuation and apostrophes, and whitespace splitting gives token arrays. Compute **unit-cost word Levenshtein distance** (substitution/insertion/deletion minimum) over the whole episode, including introduction, recap and outro. **Result: 2,009 operations; relative to 24,683 Parakeet tokens, 8.14% inter-ASR disagreement**. It is **not WER against audio** and cannot establish which recognizer hallucinated or omitted speech. The six-second disparity in first-caption timestamp is **not itself an audio omission**, since the first audible phrase is substantially aligned.

## High-priority source interpretations and listening work

| Approx. show time | Candidate / disagreement or other risk | Editorial treatment |
| --- | --- | --- |
| **00:03–00:09** | Kanja/Kenja/Conja **unbeaten overall player**; priest **Kidigree/Kidagri**, **Ventro/Ventr(o)-like** name for Royce's **local champion**. The GM occasionally says he has forgotten Ventro's own name, calling him by other comedic near-names. | **Do not conflate Ventro and Kanja**. The played defeat is **Ventro in the qualifier**; Kanja remains the target of next-day finals. Wording of “quarterfinals” and top-four stage needs audio if a precise bracket is maintained. |
| **00:04–00:07** | **1,000 original + 4,000 anonymous additional = 5,000 gold** advertised pool, explicit in E085 GM recap. | **Not a payout**, and anonymous donor unidentified. E084's additive amount gains later source-cutoff clarification, rather than an E084 payment. |
| **00:28–00:40** | Two “sick-sticks” applied to Ventro, stealth/invisibility begins imperfectly; Squirts also injects **Nash** after pairings. | **Nash saves CON 20 and is not poisoned**. The GM later declares the needles **all used up**, but count (punning “six sticks” and other numeric descriptions) still not audited with a prop handout. |
| **00:41–01:06** | Vorel and Nash actually play, and Vorel **wins using Kung**. Nash's stated willingness to throw the match is **not followed by a declared thrown game**. | Preserve played result, distinguish in-game death from actual character harm. The table revises blocking/daze/stagger arithmetic during the rules lesson. |
| **01:06–01:19** | **Minno/Minnow** (gray elf opponent of Ventro), announcers' Royce location label; Ventro **wins their match**, then **Vorel beats Ventro in the marionette qualifier final**. | **Vorel wins Royce local title and advances to larger finals tomorrow**, not the overall BMF championship or a gold payout. |
| **01:19–01:48** | Nash's Enlarge, Minor Illusion and Ray of Frost attempts are **externally negated**; Squirts' Command, Calm Emotions and Word of Radiance are **observed working**. A **large green woman-like figure/statue** manifests and **Ventro is removed through a pinhole in reality**. | **Direct event** supports Sigil's enforcement threat, but **entity's name/source, suppression cause and Ventro's survival/death remain unconfirmed**. Never infer Nash has lost magic permanently or that the figure literally speaks. |
| **01:49–02:08** | Team **“Mighty Squirts”** becomes Vorel/Squirts' **public media claim**; sponsor brands **Arcane Spice** and controller maker **Angry Dawgz/Dogs** propose **200 and 500 gp per month**. | **Neither contract signed**. Coaching offers unaccepted; strategy book handed to a fan after being stolen in E084; custody beyond transfer unknown. |
| **02:13–02:25** | **Nash earned 1 gp wage and 20 gp tips**, yet GM immediately says “now have twenty gold.” **Nothing swindles 24 gp**, is separately credited wages/tips; Squirts obtains **two unknown gems, three colored elixirs and sketchbook**. | Keep **accounting inconsistency** rather than silently choosing a new wallet total. Party gets income from inn work, **not championship or sponsorship**. |
| **02:25–02:39** | Vorel **clearly refuses further sexual attention** and escapes through a broken upper-floor window after lighting a curtain; Nash invents **“Stinky Weenie”** to divert admirers. | The inn is **not burned down**; any admirer success or future visitation is unknown. Do not plot the invented destination as a proven place. |
| **02:39–02:45** | **Nothing's warning sword**, audible movement above room, then **two armed ninja-like figures come through a window**. End-of-episode recap/outro begins without attack resolution. | **No fight resolved, NPC identities or connection to the Abyss kidnapping demonstrated**. Out-of-character “Ode to Hope and Stanley” is a later show teaser. |

## Next test

Use the recording, not majority vote, to settle **Ventro/Kanja/Kidagri/Minno** and the place title; independently listen to the **~01:45–01:49 disappearance** and **~02:39–02:45 ninja cliffhanger** before moving either event to an audio-confirmed tier. Cross-check official character sheets/notes before canonizing a specific *magic-vs-divine suppression* rule. Keep original SRTs intact, append verified corrections and timestamps to the [review queue](../project/REVIEW_QUEUE.md), and reference this report from the project's [model log](../project/MODEL_TESTS.md).

[E085](../episodes/E085.md) · [E084 comparison](E084_ASR_COMPARISON_2026-10-22.md) · [Arc Three narrative](../narrative/ARC_THREE.md).
