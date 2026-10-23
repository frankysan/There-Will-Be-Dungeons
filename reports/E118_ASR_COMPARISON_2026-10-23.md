# E118 — full-export Parakeet/Qwen ASR comparison (2026-10-23)

> **The Wastes corrected S1E118 — The Key · played Arc Five · Omnom and Stanley's father's study.** [Source-first episode dossier](../episodes/E118.md) · [Arc Five](../narrative/ARC_FIVE.md). **Both existing SRTs inspected through 02:19:49 ending/outro.** No audio listening, transcription reruns, source edits or automated listening verification.

## Source inventory and reproducible measurement

The connected workspace **There Will Be Dungeons Transcripts** started **clean on `main`, HEAD `6026d1ee944f76e3ce9ee060a508b67b320d6c19`**. The connected GitHub reader returned **“No commit found for the ref”** for that SHA; **no remote GitHub copy was substituted for the current workspace**. Complete raw contents were read from **workspace binary source calls** in 65,536-byte chunks. SHA-256 and size are the workspace's independently supplied binary metadata; **characters are JavaScript decoded UTF-8 string lengths, not raw bytes**. Pipeline/model names below **come from filenames**, not verified runtime config/precision/speed or audio version.

| Source export | File bytes | SHA-256 | SRT cues | First start | Last end | Normalized words |
| --- | ---: | --- | ---: | --- | --- | ---: |
| [The Wastes S1E118. The Key.parakeet.processed.srt](../sources/The%20Wastes%20S1E118.%20The%20Key.parakeet.processed.srt) · processed Parakeet | **208,006** | `ca402c7070dccc4be399430ce04f91c902014d40eefd2524c1cc31732e723781` | **2,104** | **00:00:13.120** | **02:19:49.760** | **19,146** |
| [The Wastes S1E118. The Key.qwen-q8.canary-ctc.nemotron.srt](../sources/The%20Wastes%20S1E118.%20The%20Key.qwen-q8.canary-ctc.nemotron.srt) · Qwen Q8/Canary CTC/Nemotron-labelled | **270,580** | `25a6ee5a663577d5234057496aacc8363c5657f695ef715dbcd32313d426f58a` | **3,275** | **00:00:05.840** | **02:19:49.520** | **19,244** |

Decoded primary string length **208,006 characters**, secondary **270,539 characters**. Both exports span the same session and end within **0.24 seconds**; Qwen begins **7.28 seconds earlier**. These timing edges do **not** prove transcription accuracy, identical audio file provenance or completeness against an unheard MP3.

**Normalization and exact method:** Extract chronological SRT cue bodies, discard index and clock lines, strip optional `(speaker N)` decorations; concatenate all speech text. Lowercase, **delete straight/curly apostrophes without spacing** (joining contractions), replace every other character except Unicode letters/numbers with spaces, trim/split on whitespace. Compute exact **unit-cost ordered word-level Levenshtein distance** by arbitrary-width bitvector procedure over **full sequences including intro and outro**. Reference is the Parakeet 19,146-token sequence.

**Result: 1,273 ordered word edits / 19,146 Parakeet words = 6.6489083882%, rounded 6.65% inter-ASR text disagreement.** Qwen contains **98 more normalized tokens**; this is **not** verified Parakeet omissions or Qwen correctness. No WER, audio accuracy, actual hallucination/omission count, or verified diarization can be inferred.

## Episode-specific uncertainties and listening checkpoints

| Recording clock | Competing wording / editorial risk | Conservative decision |
| --- | --- | --- |
| 00:00–00:02 | Host says **Sunday September 13**; owner catalogue has Monday **September 14, 2020** | Spoken session/day and published episode date kept distinct |
| ~00:15–00:39 | Five Elhandar arrivals including admiral, four assigned therapists, apprentice candidate. Doctor spellings **Zanzafir/Zanzapyer, Tindalanthalas, Mahasiabi, Joam Emantha**, additional care for family | Assignment **required**, actual sessions **optional**; casual dinner is not attended therapy |
| ~00:26–00:29 | Admiral says **Omnom is alive and nearby**, injured, struggling to adapt; reports ~12–15 demons downed | Initially **NPC report**, later **played Omnom appearance** resolves survival |
| ~00:34–00:40 | Female therapist **physically hands Stanley his father's key**, says opens something in this cottage; key inventoried | Actual transfer, not merely promised father search; giver/parent spellings need listening |
| ~00:49–00:55 | Young elf **Dilenoria/Dylanoria (?) (“Dilo”)** requests Stanley apprenticeship based on pirate-boarding fight, studies unarmed Earth styles | Stanley only requests **return next morning / group discussion**, not appointment or combat participation |
| ~01:02–01:11 | **Omnom Cinderborn** emerges with damaged face/scales and casts; Razak Val “chicken lords” and vermin wounds; charges **Hope**. **Stanley casts *Hold Person***, and Vorel runs him aside | Physical reunion and actual restraint; no kill, no invented healed appearance |
| ~01:11–01:27 | Omnom accuses Hope of **rocket-arm deaths at Razak Val**, burning the Principle train station and **deliberately importing demons to Tietkalla**; Hope admits shot and fire but says **Hand attracted demons and she fled to draw them off** | **Contrasting accounts**, not proof Hope ordered invasion. Vorel refuses Omnom's request to kill him, postpones hunt |
| ~01:31–01:46 | Father-key search unsuccessful until **Stanley's childhood poem** activates it, floats up to **invisible landing lock**, **turns, stairs descend**, impossible extra floor | Actually entered hidden father study; lullaby exact wording needs audio |
| ~01:46–01:57 | **Book of Adjacencies**: endless-looking pages, authorized-name/topic query, Stanley allowed to **add to inventory**; Hope unable to read Elvish | Real artifact and accessible entries, **not an encyclopedia or automatic shared knowledge** |
| ~01:53–02:02 | Letter addressed **Valier/Vale Ornath (?)** from **Dalit/Daliot (?)**; future death claimed foreseen; **N4SH (“N-for-SH” vs “N4SH”) anomaly**, mother **Krista (?)** and future Feywild reunion | Qwen distinctly gives **N4SH**; use provisional spelling, do not assume all predictions true |
| ~02:00–02:05 | Privately seen **hooded Voice** makes Hope's Hand hurt, urges **Pentelvice/Pentalvise (?)** | Actual private visitation / pain, but no travel, Eye, fulfilled pact or other party members seeing figure |
| ~02:06–02:14 | Dalit's journal hypothesizes **Weir breach distorts Earth's time**; “N4SH” linked to possible **future Principle technologies**, near Solar Mines; globe marks corresponding location | Distinguish **an unfinished scientist's hypotheses** from authoritative narrator-confirmed cosmological fact or actual time travel |
| ~02:14–02:18 | **Mask of Elton IV / Elton Four / Eltenvor (?)** physically listed in Stanley's inventory, **four long rests to attune**, ***Peer into Plurality*** psychic-cost d20 influence (first 30 damage, doubling on further number picks), potential fatal nonresurrection without *Wish* | Mechanics **read aloud, not used**; no long-rest attunement, activated mask roll, harm or confirmed item spelling |
| ~02:18–02:19:49 | Stanley remains in secret study; Nash attends children, hunt planned for tomorrow | **No hunt actually begun**, no Dilo return, no trip to Solar Mines/Feywild |

**High-priority audio windows:** ~00:20–00:42 therapist names and key handover; ~00:50–00:55 elf Dilo; ~01:02–01:28 Omnom's injuries/claims, *Hold Person*, Hope's answers; ~01:37–01:47 exact parental poem/door opening; ~01:48–02:02 book, birth/father/mother names, **N4SH** and private letter; ~02:00–02:06 private Voice; ~02:06–02:19 full journal theory and mask name/stat-block wording. Audio has **not** been reviewed.

**Research sequence:** Owner's catalogue places **Bonus 2020-09 — September 2020 (September 15, 2020)** after E118 before **E119 — Put Out The Fish Fire (September 21, 2020)**. The next bonus's **specific source basename was not resolved in this pass**, so no fabricated file link appears. [E118 dossier](../episodes/E118.md) · [active review queue](../project/REVIEW_QUEUE.md).
