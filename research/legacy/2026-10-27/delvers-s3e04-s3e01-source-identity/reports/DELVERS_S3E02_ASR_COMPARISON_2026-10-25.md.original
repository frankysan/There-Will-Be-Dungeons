# Delvers S3E02 — Call your Mummy: exact full-export ASR comparison (2026-10-25)

**Identity:** [Delvers S3E02 dossier](../delvers/episodes/S3E02.md), a **played Season Three episode** whose opening says recording Saturday **2021-08-14** (not independently verified publication date). The full three-month time jump **concludes during this episode**; last played event is the public Silver City announcement, not a new dungeon expedition. [Queue](../delvers/REVIEW_QUEUE.md).

**Provenance and limitation:** First MCP workspace `main` HEAD `2e82c5bacffa26ce23e6ce7e28290134fe940108` with four **unrelated pre-existing illustration-skill edits**. GitHub **404** for that exact local commit, so both inputs fetched from **GitHub default branch**, with **remote blob SHAs below**. Workspace P **beginning/end** and Q beginning match, but **full local/remote byte identity was not proven**. Distinct source paths and exports labelled by filename only; no MP3, source audio alignment, original transcription settings, runtime logs/commands, hardware or publisher metadata verified.

| Export / inferred pipeline | Source | GitHub blob SHA | Complete SRT cues | Normalized word tokens | End |
| --- | --- | --- | ---: | ---: | --- |
| Parakeet processed (reference) | [P](../sources/Delvers%20S3E02.%20Call%20your%20Mummy.parakeet.processed.srt) | `f554c9314ffe5dd2bfcdc5a13b93c7f8dbf920e5` | 2,596 | **23,797** | 02:53:14.120 |
| Qwen Q8 / Canary CTC / Nemotron-labelled | [Q](../sources/Delvers%20S3E02.%20Call%20your%20Mummy.qwen-q8.canary-ctc.nemotron.srt) | `729433798f9b7a0f4788b5fedf5a3bd548d9bdd0` | 4,133 | **23,925** | 02:53:13.840 |

**Exact complete-export ordered unit-cost Unicode word Levenshtein = 1,648 / 23,797 = 6.93% inter-ASR TEXTUAL DISAGREEMENT.** Q has **128 more normalized words**; its last cue ends **0.280 seconds earlier**. **Not** WER, transcription accuracy, proven omission/hallucination counts or an audio-verified winner.

**Method:** Chronologically parse all SRT cues; remove cue numbering/timing and `(speaker N)` prefixes, join cue lines; lowercase, join contractions by deleting apostrophes (straight/curly), replace non-Unicode letters/digits with spaces and tokenize. Matching **31-token prefix and 2-token suffix** removed before two-row dynamic programming. **±2,600-token index diagonal band** score **1,648** is below band, certifying the exact full optimal edit distance (any better path leaving band would require at least 2,600 indel steps). P interpreted sequentially in recording-clock **0–28, 28–55, 55–83, 83–112, 112–140, 140–173:14**, including final post-show ident. Complete Q input parsed for metric; independent Q excerpts around **0–4, 5–12, 35–42, 45–53, 54–59, 60–70, 75–82, 84–90, 90–95, 95–103, 105–112, 116–123, 125–130, 132–140, 143–153, 154–160, 165–173** read selectively, some output-clipped. **No complete second interpretive Q reading or audio listening.**

| Time (recording clock) | Specific transcript risk / listening target |
| --- | --- |
| **~00–09** | Spoken recording date; continued daily curse-removal work despite endless intake; Sean **donkey/mule** terminology, 8 gp paid, farm new worker roles. |
| **~18–33** | Repeated Anathala blood draws, Bullywug **Muck Muck** name and probation, farm layout & Pelor book author. |
| **~34–53** | Proposed Julian Thomas marriage **not accepted**; Carrie **asserts Evelyn delivered red shard** and combines it with Anathala blood, **hypothesizes Dolbluth lineage**. Amulet actually transferred to Koh. |
| **~53–59** | Possession aftermath vocal injury, **Cure Wounds attempted but FAILS in throat**, affected people's name variants; **no general success** despite treated bodies. |
| **~61–73** | Construction wall vs repairs, city's house purchase **offer**, first amulet alert, **nonlethal psychic knockout**, medallion goes dark. |
| **~76–82** | Evelyn directly rejects Julian, confesses paladin identity and god's name **Lesty (?)** to parents; response is disbelief, not acceptance. |
| **~83–89** | 8/20 initial crop result, **3,500 gp committed** to barn, structure **actually finished** within week; no Goodwine land investment. |
| **~91–112** | Thin naked figure's force/tendril spells, bat crest, telepathic **high reward to kill Splenderbelt**, necrotic surgery, **head smashed and spiders emerge**. Spider *robot* merely player joke; Carrie later guesses motive. |
| **~113–123** | Earlier elf wakes **from knockout without dream Remove Curse**, shallow vs deep compulsion distinguished. Veggie Sticks plan not yet executed in this segment. |
| **~125–140** | Cassius heroic-pamphlet campaign played, not immediate acquittal; Julian bedroom request re-rejected; **real vampire invasion** and first bite, no armour. |
| **~140–153** | Evelyn's radiant assault and thrown javelin impale vampire, **but he is still groaning until Gold League slayer later stakes**; parents see magic. |
| **~153–164** | Koh **persuades actual Veggie Sticks**, arrives via Tree Stride, **completed amulet direction enchantment**, Veggie Sticks leaves. |
| **~164–173:14** | Final **three-month** confirmation, construction complete, Koh **purchased house**, paid elf hunting, Evelyn returns on summoned elk; in-universe recorded/cast-performed **Silver City licensing/raid announcement** vs actual party adventures. |

**Research verdict:** Primary text full-cover, Q complete-input computational comparison with independently reviewed selected windows; no human audio confirmation. Do not backfill future raid decisions or treat Carrie's ancestry hypothesis as proven genealogy. Source files unchanged. **Next [Delvers S3E03 — Thank You For The Deposit](../delvers/SOURCE_INVENTORY.md)**.
