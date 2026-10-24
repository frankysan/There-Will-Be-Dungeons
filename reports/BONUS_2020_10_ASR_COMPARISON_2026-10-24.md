# October 2020 public bonus — full Parakeet/Qwen ASR comparison

**Episode ID:** `BONUS-2020-10`, public-release-month label October 2020, owner publication index October 7, 2020 (**not** recording date). **Type:** listener Q&A, cast reflections and production invitation, **not** the played E121 session. [Source-first dossier](../episodes/BONUS-2020-10.md). Research at connected workspace `There Will Be Dungeons Transcripts`, branch `main`, HEAD `54798e82fb9b68722b39730045c9da852a8edbb2`, with **10 unrelated changes already present** before this pass. Raw ASR untouched.

## Complete-export inventory

| Export | Exact path | Bytes | Workspace SHA-256 | SRT cues | First cue | Last cue end | Normalized tokens |
| --- | --- | ---: | --- | ---: | --- | --- | ---: |
| Processed Parakeet | [`Bonus 2020-10 - October 2020.parakeet.processed.srt`](../sources/Bonus%202020-10%20-%20October%202020.parakeet.processed.srt) | **83,833** | `d0cc3dc95e725e8818779ccd873aef42657b5306bbc6532ed597e55b4833ece2` | **841** | **00:00:06.000** | **00:41:31.930** | **7,899** |
| Qwen Q8 / Canary CTC / Nemotron-labelled | [`Bonus 2020-10 - October 2020.qwen-q8.canary-ctc.nemotron.srt`](../sources/Bonus%202020-10%20-%20October%202020.qwen-q8.canary-ctc.nemotron.srt) | **106,139** | `bb6822ff0ec89f268cf151da1e441d0a2a02a3d62c676fad472e2774816ae26d` | **1,254** | **00:00:06.000** | **00:41:31.920** | **8,034** |

Both existing SRT files were read through the **last farewell cue** in bounded binary chunks from the connected workspace. The end timestamps differ by **0.010 seconds**. Exact ASR labels are **only inferred from filenames**; inference does not verify upstream model weights, prompts, VAD/diarization, run flags or matching waveform provenance. No source audio, external pages or visual handouts were independently verified; no new transcription pass was run.

**Method:** Parse complete SRT cue blocks and join spoken text in recording order; remove optional `(speaker N)` markup, timestamps and numeric cue indices; lowercase Unicode text; remove straight and curly apostrophes (joining contractions), substitute whitespace for all other non-Unicode-letter/digit characters, split nonempty tokens. Compute **exact unit-cost ordered word Levenshtein distance** using arbitrary-width bit-vector dynamic programming. All metrics use the **Parakeet** sequence as denominator.

**Result: 498 ordered word edits / 7,899 Parakeet tokens = 6.30% inter-ASR text disagreement (6.3046% unrounded).** The Qwen-labelled sequence contains **135 more normalized tokens**. **These are not verified transcription errors, WER, missing speech, word accuracy, hallucinations or proof one system is better.** A preliminary comparison using byte-decoded rather than proper Unicode text gave **508**; it was **discarded** after correctly decoding UTF-8, and the final dossier/model log consistently use **498**.

## Timestamped points needing audio or source confirmation

| Approximate recording clock | Specific evidence, disagreement, or attribution risk | Conservative outcome |
| --- | --- | --- |
| **~00:30–03:12** | Beau invites community designs for a prison pronounced **Pentelvice / Pentel Dece / Pentel Weiss (?)**. Naming, requested Prime Material origin, CR guideline, and fan artist **R. C. Tang (?)** need exact audio | **Community-submission proposal**, not actual accepted prisoners or constructed map; Eye not recovered |
| **~05:35–06:50** | Jon reads abbreviated notes listing **four gray-elven therapists**, with ASR spellings `Zanzaphir`, `Tyndalanthalos`, `Mahasibi`, `Joam Anathar`; uncertain who treats whom | **Player's notepad recollection**, not canonical written names or new E120 visitors |
| **~08:15–10:05** | Separate **Jon one-off**, Scott's notes about `Rivia/Serfax (?)`, allergy to cats and Garpoon's secret protection assignment | **Authorial one-shot backstory**, not Wastes geography or a new played hire; verify proper one-off source |
| **~10:25–14:10** | Character-informed note-taking, Beau's three-hour sessions and week-to-week retention; in-head imaginary Stanley discussions | **Playing/GM practice**, not extra dialogue played by Stanley |
| **~17:30–21:50** | Scott and Jon refer to the **same-day E120** mushroom-eating and T. rex transformation while debating improvisation and survival-minded play | **Retrospective reference**, not second Polymorph, mushroom dose or session |
| **~22:30–26:40** | Dice collection counts and joking suggestion of a biased digital roll app; Kyle's E119 craft list | **Out-of-game banter**, no proven cheating, changed loot or crafted item |
| **~26:45–27:55** | Jon says Stanley's dictionary carries an **old, earlier-owner “Stanley Billings” inscription**; previous owner undisclosed | **New creator backstory detail**, not verified physical journal evidence or evidence it belonged to Dalit |
| **~28:05–31:25** | Nash's fatherhood and shapeshifting anxieties are discussed by Scott; personal-life examples mixed with creative decisions | **Player interpretation/future possibility**, not another infant transformation or fixed destiny |
| **~31:35–34:25** | Kyle's alternate **paladin** character path and Vorel's privately felt response to **Squirts's death** | **Counterfactual build and creator-motive interpretation**, not played level change or title award |
| **~34:40–38:40** | Beau's account of branching “time barf,” original personal note adapted as **Dalit's book entry**, physics and Eric Weinstein inspiration | **Authorial provenance and deliberate thematic intention**; not established physical cosmology or scientific fact |
| **~38:45–41:31** | Kristen speculates whether Hope might fully embrace the Voice or turn and kill him; Beau praises a battle for someone's soul | **Unplayed alternatives**; Hope still alive captive at E120 |

**Notable source differences:** The two exports split speakers into very different numbers of cues (841 versus 1,254); **cue count is not independent speech recall**. Pronunciations and proper names remain weak across models, including **Pentelvice**, therapists, **Garpoon one-off place names** and possible fan illustrator **R. C. Tang**. Out-of-game "today" ties the subjects to E120 but **does not specify calendar recording date**. Qwen's diarization IDs label utterances but **do not independently verify individuals without audio**. The final cue reaches the same farewell in both; no asserted Qwen-only speech after the outro.

## Editorial decisions

- **Do not extend Wastes played chronology beyond E120** from a bonus/Q&A. E121 remains separate and unresearched here.
- Record **Stanley's dictionary inscription** in his person/item context, **Beau's time-barf inspiration** on the Book page, **Kyle's Squirts-related protectiveness** on Vorel, and **Scott's tentative parenting interpretation** on Nash with explicit authorial-source marking.
- Record **Pentelvice community-design invitation** as **production process only**; the cast's suggested dungeon contents and abandoned possibilities are not new canon.
- **No new Vorel title/epithet** is conferred; **no performed Nash casting phrase** occurs. The previously played *Haste* in E120 is discussed, not cast again.
- Keep the Garpoon anecdote in a **separate one-off context** until its exact recording is matched to a dossier.

**Priority original-audio verification:** ~00:45–02:55 prison name and submissions; ~05:45–06:55 therapists; ~08:30–10:00 one-off clues; ~26:45–28:00 dictionary; ~34:40–38:40 time origin; ~39:00–40:15 Hope hypotheticals. Audio accuracy remains unmeasured.

**Next publication pointer:** corrected *The Wastes* **S1E121 — The Heart of The Matter** (owner catalogue October 12, 2020); source existence should be verified before creating its dossier.
