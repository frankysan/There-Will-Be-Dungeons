# E091 — Going on a heist: two-ASR comparison (2026-10-23)

> **Text-only comparison** of two original subtitle exports for the same ~02:46:27 recording; **no audio listening or human reference transcript**. Neither original source SRT has been modified. [Episode dossier](../episodes/E091.md).

## Source inventory and method

| Export label from filename | SRT cues | Last cue end | Normalized word tokens |
| --- | ---: | --- | ---: |
| [Parakeet processed](../sources/The%20Wastes%20S1E091.%20Going%20on%20a%20heist.parakeet.processed.srt) | **2,506** | **02:46:29 approx.** | **21,829** |
| [Qwen Q8 / Canary CTC / Nemotron-labelled](../sources/The%20Wastes%20S1E091.%20Going%20on%20a%20heist.qwen-q8.canary-ctc.nemotron.srt) | *See source; cue count to confirm* | ~02:46:27 | *See source; token count to confirm* |

Method: remove SRT cue numbers/timecodes, concatenate cue dialogue in order, remove '(speaker N)' labels, lowercase, remove apostrophes (joining contractions), replace remaining punctuation with spaces while retaining Unicode letters/digits, tokenize on whitespace, and perform **unit-cost ordered word-token Levenshtein**. In the current calculation: **1,736 edit operations / 21,829 first-export tokens = 7.95% inter-ASR text disagreement**. This **is not audio-reference WER, a measured accuracy score, omission/hallucination counts, a diarization assessment, or a model ranking**. Exact ASR versions, parameters, hardware, source audio fingerprint and word-by-word human references were unavailable; the names in filenames are not proof of all internal pipeline settings.

## Material source-aligned findings

| Timestamp | Comparison, evidence boundary and priority |
| --- | --- |
| **~00:06–00:10** | Jelver escorts party; **Mind Master / Gerbken Shartlinger** visible in side office, with no interaction. A rune circle sends heroes to a **desert-like conjured fight**. Whether first presentation was a literal journey must be determined from the later reveal, not the scene's appearance alone. |
| **~00:10–00:45** | Four giant trolls appear in staged trial. Party briefly plays dead; **Nash Hastes only Stanley**, **Stanley animates a boulder**, Hope attacks, **Vorel grapples and damages a troll with E090 spiked boots**. Both transcripts convey scene despite battle/map segmentation differences. |
| **~00:45–01:10** | **Stanley kills Barnold**, **Vorel kills two-headed troll**, **Sicky bleeds poisons and dies through self-injury**. Nash's Fireball can still hurt allies despite Careful Spell. Stanley transforms low-health Nash into a **giant ape**, not a lasting character-form change. Exact troll nicknames and initiative/damage numbers need audio review. |
| **~01:17–01:36** | Gloria's boulder **downs Stanley**, breaking Polymorph concentration; Hope later **kills Gloria**. **Nash uses Stanley's healer kit to stabilize him** while he remains unconscious. The canyon fades to **a test room with hurt robed conjurers**, Jelver **confirms passing** and **heals Stanley 22 hp**. No death/resurrection or verified Earth excursion. |
| **~01:41–01:50** | Jelver names **Zorander's Fist**, source world **Drethiel/Dreftiel**, deity **Euphemius**, **Obsidian White** paladins (Peladric/Pelagic order adjective) and **Bishop Stevius Ritley/Rintley**. Both describe a **kidnapped bishop and changeling replacement**. Three PCs accept full-healing drinks; characters are no longer left wounded. Proper-name orthography unverified. |
| **~01:58–02:13** | **Stanley's Enthralling Performance and subsequent deceptions work** on the bishop. He gives **White Tower / Outlands** custody, reported **Mount Celestia transfer goal**, **pure-good soul wall** and locked box whose **key is worn by High Cleric Butar Thrun (?)**. Bishop's account may be sincerely believed but remains NPC testimony. **Aunt Eulonis/Julonis** safety request not fulfilled. |
| **~02:13–02:29** | Discussed alternatives include false paladins, tunnel, transport trick and dragon. Chosen **key-first + airship/tele-shoot** plan is **still future**. Jelver records **8 Dimension Door and 4 Reverse Gravity scrolls** and airship/crew procurement. Sealed **Lohar authorization actually offered/accepted**, outfits not made. |
| **~02:32–02:44** | **Potential gun loan and gnome bullets remain promised**, not transferred. **Jelver actually lends Vorel named +2 greatsword Shatter**, wants it returned; Nash requests a ring and magic blade without receiving them. **Sealed Harmonium pass offered**; not yet used. **Level 10 awarded** in outro, separate from fiction. |

## Important interpretation decisions

1. The **E090 unspecified retrieval job is now actually briefed**: a named gauntlet and a more specific two-stage robbery plan. **No heist has been performed**.
2. **Fist custody, locked box, tower's soul barrier, and the key** come through **the charmed captive bishop**, not a direct visit. No proved verified tower contents or guaranteed bypass.
3. **Troll combat is a magical competence test** with played damage and real postfight healing; don't treat the apparent desert as independently established geography.
4. Inventory and service state: **Vorel receives Shatter on loan; authorization notes/writ exist; airship, scrolls, arms, ammunition, manufactured clothing, spell-storing ring and dagger do not yet arrive**.
5. **Hope's Scully was gifted in E090**. Discussions of using Tobacho's guns or acquiring ammunition **do not restore Scully**.
6. The **Earth portal remains a conditional reward** only; no known usable door or completed passage. **Harmonium writ is not proof a gate accepted it**.
7. **Kidnapped Stevius remains a captive with an impersonator in place**. His concern for his aunt is a live thread; no promise of assistance is shown as completed.
8. At ~02:44 the **table is told to advance to level 10**; do not backdate this to combat at level 10.

**Further listening:** Resolve **Jelver/Jalver**, **Zorander**, **Drethiel**, the Obsidian White order wording, **Stevius Ritley**, **Butar Thrun**, **Eulonis** and troll names using actual audio. The raw machine-export disagreement is measurable but does not adjudicate them. **Next bounded story slice: E092**, subject to source filename verification before linking. [Review queue](../project/REVIEW_QUEUE.md) · [Model test log](../project/MODEL_TESTS.md).
