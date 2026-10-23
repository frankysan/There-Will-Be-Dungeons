# E108 — full-export Parakeet/Qwen ASR comparison (2026-10-23)

> **The Wastes S1E108 — Save The Two · Dunebreaker prequel part 2 of 3, same Wastes long before E001.** [Source-first E108 dossier](../episodes/E108.md) · [Dunebreaker reference](../world/places/dunebreaker.md). Complete **text-only ASR export comparison**; neither original audio nor cast handouts were independently listened to, and no source SRT was edited or ASR model run.

## Exact source inventory

Workspace identity on entry: **There Will Be Dungeons Transcripts**, clean **main** at HEAD **`78179550f7ed9d70931fd6b81542c4f03a6311c0`**. The pre-existing Parakeet and Qwen SRT files were read via bounded chunks of the connected workspace's **binary reader** through the complete network sign-off, not just the played-session ending. The source reader supplied the sizes/hashes below.

| Export (model names inferred from file basename) | Bytes | SRT cues | First cue start | Final cue end | Unicode-normalized words | SHA-256 |
| --- | ---: | ---: | --- | --- | ---: | --- |
| [The Wastes S1E108. Save The Two.parakeet.processed.srt](../sources/The%20Wastes%20S1E108.%20Save%20The%20Two.parakeet.processed.srt) — primary processed Parakeet | **236,741** | **2,398** | **00:00:03.920** | **02:37:48.310** | **22,243** | `dc9989918e807568fc53e6028cabc86c75e3899a4c45f0b7e2ce8c19a6d96e36` |
| [The Wastes S1E108. Save The Two.qwen-q8.canary-ctc.nemotron.srt](../sources/The%20Wastes%20S1E108.%20Save%20The%20Two.qwen-q8.canary-ctc.nemotron.srt) — Qwen Q8/Canary CTC/Nemotron-labelled | **314,276** | **3,849** | **00:00:09.760** | **02:37:48.090** | **22,395** | `c0570e8cd3ab714a41a759ce3126d59b36373aaf6033f8ab98203893c6d78722` |

The pipeline labels **do not authenticate model versions, quantization configuration, diarization, decoder settings, processing hardware or audio-copy linkage**. No timing benchmark or MP3-to-SRT correspondence was measured. First-cue difference is **5.84 seconds** (Qwen starts later) and is an opening-listening review candidate, not a confirmed omitted spoken span.

## Exact established lexical method and result

For each complete SRT, parse cues in order; discard cue numbers/time rows; strip optional `(speaker N)` decorations; join cue content; lowercase; **remove straight/curly apostrophes without introducing a word separator**; replace every other non-Unicode-letter/digit with whitespace and split into word tokens. Compare full ordered sequences using the same **arbitrary-width bit-parallel, unit-cost Levenshtein method** used in E105–E107; neither speaker timing nor word alignment affects the edit count.

**Parakeet → Qwen: exactly 1,047 ordered word edits / 22,243 Parakeet tokens = 4.7071% ≈ 4.71% text disagreement.** Qwen has **152 more normalized words**. This is **not audio-based word error rate (WER), accuracy, a confirmed word omission count or validation that one export correctly transcribes difficult dialogue**. The bit-vector approach follows the project's prior validation; **no new independent audio reference test** was conducted here.

## Critical ambiguity and listening windows

| Recording-clock span | Text finding / risk | Conservative E108 interpretation |
| --- | --- | --- |
| ~00:00–00:04 | Host opens with **Sunday the 28th of June**, while owner release catalogue lists **TWBD 110 on 29 June 2020**; two ASRs begin at different points. | A host-stated day is not a publisher upload time, and the archive's publication date is not a proved recording time. |
| ~00:15–00:24 | Complex wet engineering fork with red lighting; more liquid and **Ramilda finds blood among condensation**. | The group pursues a physical blood trace, not an identified killer from E107's first notebook. |
| ~00:25–00:39 | An elderly stowaway **calls surrender first**; Ramilda's **actual Guiding Bolt 15 damage**, and attempted morningstar versus stunned defendant; name later rendered **Lamulkin/Lamalkin/Limulkin Farthing**. | Surrender precedes the player's attack; he survives, offers a dagger and initially confesses. Do not claim immediate execution or that a second person actually attacked the guards. |
| ~00:40–01:07 | Elder says engineer threatened him; GM reaffirms **four stab wounds in BACK**; hidden people are discovered. Two starving daughters, approximately **16–17 and 10**, come from **Slavetown**. Several discussed options include amputating the father's arm and a *Feather Fall* escape jump. | The man's first self-defense account is **testimony**, not a replayed combat. **Neither amputation nor Feather Fall occurs**, and the hidden children are **not physically taken away** at this stage. |
| ~01:06–01:18 | Older daughter admits **“what I did”**; father confirms **she stabbed the engineer**, and later Jon's recap corroborates his deliberate false confession. Hack's farewell Perception **24**. | The offscreen crime is resolved as a **GM-supported confession**, while precise initiation and degree of self-defense remain unobserved. Father is **not actual knife-wielder**, but chooses to be blamed to save children. |
| ~01:18–01:35 | **Al keeps the surrendered dagger**, introduced before Lotho/Ember; Hack lies man acted alone, **Deception 17**, and offers cheap labor; persuasion **12** then Ramilda **23**. | **Actual knowingly false report accepted** at episode cutoff. **Ember spares father, sends him to tumbler-vent “rat” work**, alive but facing hazards; daughters are not exposed. |
| ~01:34–01:41 | **Strum** volunteers engineering knowledge; DM jokes about removing NPC from party. | **Real occupational transfer of Strum, no death**, still on board and subsequently seen. |
| ~01:43–02:06 | Rooms **3A, 3B, 3C**, *Dipshit* stew counter, Ramilda wants mead. **Hack shows distinctive poorly healed circlet-like facial scar** by removing his see-through veil privately. | Scar is a character description, **cause and original injury remain unknown**. Serving bowl is not conjured or magically materialized; “Dipshit” is an in-world handle, not proven birth name. |
| ~02:06–02:26 | **Strum worries about girls**; **Al explicitly declines** follow-up journey; Hack and Ramilda escort Strum to deliver **two actual bowls and drink**. | Girls **eat and are alive/hidden**. Do not conflate immediate delivery with permanent rescue or pretend all three PCs went back to engineering. |
| ~02:26–02:37:48 | Card game roughly breaks even; special mead bottle from gnome after consulting Ember; Hack whittles; Al works on his equipment. Last played day ends before cast's outro. | **No new murder, ship departure, Fleece payment or E109 outcome**. |

### Unverified names, mechanics and source conclusions

High priority: **Lamulkin Farthing** spelling, older daughter's first-person confession and father/GM correction, the precise *Guiding Bolt* hit and reason she attacks a surrendering figure, **Deception 17 and two persuasion results**, what a **tumbler “rat”** worker actually does, daughter ages/any spoken names, Hack's facial scar description, **Strum engineering reassignment**, exact food handoff, and the host's date. Other pre-existing names still ASR-provisional: **Ember Shalisper, Captain Lotho, Ramilda Gloryfaded**. The [review queue](../project/REVIEW_QUEUE.md) tracks priority listening. Audio may correct words and timing; it cannot settle unspecified character motives not supplied by played scenes.

**Next exact verified source:** [The Wastes S1E109. Sand Jell-O.parakeet.processed.srt](../sources/The%20Wastes%20S1E109.%20Sand%20Jell-O.parakeet.processed.srt) and [Qwen-labelled counterpart](../sources/The%20Wastes%20S1E109.%20Sand%20Jell-O.qwen-q8.canary-ctc.nemotron.srt), both present, **subsequently analyzed in [E109](../episodes/E109.md)**, but not part of the E108 comparison. Owner catalogue: **TWBD 111, 6 July 2020**, conclusion of the three-part prequel. [E108 dossier](../episodes/E108.md) · [E107](../episodes/E107.md).
