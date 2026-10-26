# Wastes S2E09 — inter-ASR comparison (2026-10-26)

**Episode:** *The Wastes*, Season Two **S2E09 — The Call of Meats is Strong** (played session), [source-first dossier](../episodes/S2E09.md). **Two independently labeled text outputs; no audio listening or reference transcript.** Local workspace initial `main` HEAD `7fee3074ea130e6f7c0d26418ec3042fa935f920`, clean visible status; remote default-branch blobs below fetched after the workspace HEAD failed remote-ref resolution. Matching **local beginnings** checked; local/remote entire-byte equivalence not independently verified. Source MP3 not listened to.

| Source (filename label, not run metadata) | Git blob | SRT cues | Unicode-normalized word tokens | Last cue end | Text characters |
| --- | --- | ---: | ---: | --- | ---: |
| [Parakeet processed](../sources/The%20Wastes%20S2E09.%20The%20Call%20of%20Meats%20is%20Strong.parakeet.processed.srt) | `4c03ea4188f370914d72ce1c151fd30499ae2d21` | **2,300** | **20,482** | **02:23:18.030** | **212,679** |
| [Qwen Q8 / Canary CTC / Nemotron](../sources/The%20Wastes%20S2E09.%20The%20Call%20of%20Meats%20is%20Strong.qwen-q8.canary-ctc.nemotron.srt) | `2cb83f6e5a8f1c8c5a25cfac5a24197f50da2a89` | **3,888** | **21,005** | **~02:23:17** (verify milliseconds in exact file) | **294,858** |

**Method:** Parse complete SRTs chronologically; discard cue indices and timestamps; remove optional `(speaker N)` markers; join only cue speech; lowercase, remove straight and curly apostrophes (joining contractions), replace all characters other than Unicode letters/digits with spaces and split into word tokens. Then compute **unit-cost ordered global word Levenshtein distance** (substitute/insert/delete), with Parakeet as denominator. A two-row dynamic-programming diagonal band of ±4,800 word positions gave **2,432 edits**, strictly less than band width and therefore equal to the unrestricted optimum.

**Result:** **2,432 / 20,482 = 11.87% inter-ASR textual disagreement**; Qwen contains **523 more normalized tokens**. This is **NOT WER, measured transcription accuracy, or verified model omissions/hallucinations**. Difference does not by itself establish which transcription is right.

## Specific unverified listening risks

| Recording window | Text-only observation / review question |
| --- | --- |
| **~00:01:55–00:03:20** | GM explicitly maps six shapeshifters to names and forms. Cross-check **Ziptyree/Zippyree, Daniel/Danielle, Torbeer, Rugrish** against cast audio/handouts. S2E08 final mapping was unresolved; don't reverse-map from hallucinated cue labels. |
| **~00:19:20–00:21:05** | Nash declares *Chromatic Orb* and rolls as if successful, then GM reminds him it fizzles and **third-level slot burns**. Do not write actual damage or a newly spoken rhyme. |
| **~00:57:30–01:13:00** | GM says weretiger reverts to “Morton” and later clarifies he had used **Morton's token instead of Daniel's**. Pair opening identities and later ***Diplomacy* killing of the wereboar** before resolving victim names. |
| **~01:18:15–01:39:50** | Tilly escapes drowning, orders surrender; **Badass T receives failed death save, is stabilized and visibly grows fur, then ACTUALLY stays in camp**. NPC assertion of lycanthropy not proof of full transformation or safe eventual outcome. |
| **~01:49:10–01:50:10** | New self-proclaimed Vorel title **“grand adventurer and defeater of the meat sad people”** is ASR-vulnerable. Ralston/Rolston (surname Beer?) also unsettled. |
| **~01:55–02:02** | Tungsten is visually present and embraces Union; he recognizes family/Selle Prime. Verify canonical Elhandari and patronymic orthography if original character sheet exists. |
| **~02:02:55–02:05:30** | *Diplomacy*'s *Parley* levitation fails while physical magic blade/other features work; Tungsten proposes inherent magic vs conjured arcane distinction and old collector **suppression-bypass rings**. Avoid universal claims beyond testimony and observed functions. |
| **~02:07–02:11** | Tungsten's suspected betrayal list is **Vladimir/Principle, Delit Ornath, Groxl, Monsoon**, not proven culpability. Rumored captured collector/thing from beyond appears in **“Northwestern/northeastern”** phrasing, possible in-speech repair; direction remains OPEN. |
| **~02:18–02:22** | Stanley intimidation 9 → inspiration reroll 16 disperses crowd; Vorel hits **Rolston** with **empathy grenade as club**, no reported explosion, magic activation or confirmed lethal injury. |

**Editorial source coverage:** Entire **Parakeet** transcript manually reviewed chronologically in ~25-minute blocks, beginning through final FrogPants cue. Entire **Qwen** export parsed for global counts/metric, with independent text inspected at opening, rat kill, conflicting token surrender, Tilly's ceasefire/Badass stabilization and field/ring explanation. **Not** full Qwen editorial reading. **No original audio listened to**, no speaker identities acoustically verified, no ASR source altered. Comparison is primarily a *listening prioritization tool*, not an adjudication of every error.
