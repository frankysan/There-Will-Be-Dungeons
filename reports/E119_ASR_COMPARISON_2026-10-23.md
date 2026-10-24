# E119 — complete Parakeet/Qwen ASR comparison (2026-10-23)

> **The Wastes, corrected S1E119 — Put Out The Fish Fire**; played Arc Five. [Episode dossier](../episodes/E119.md) · [Arc Five](../narrative/ARC_FIVE.md). **Both complete existing SRTs read through the 02:47:48 ending/credits** via bounded binary chunks in the connected workspace. **No source audio listened to**; original SRTs and MP3 files were not modified.

## Provenance, inputs and measurements

The connected **There Will Be Dungeons Transcripts** workspace had **clean `main` at HEAD `f0b4db7a5bf0a80652e4c0d55fab1bdb8adac2ae`** before documentation edits. Source files were retrieved as bytes using **`read_workspace_binary`** (separate 65,536-byte segments), decoded as UTF-8 and parsed as SRT cue bodies. File model labels are **inferred from filenames only**; model settings, run metadata, acoustic source fingerprint, diarization quality, computer performance and actual audio fidelity were not verified.

| Independent export | Bytes | Workspace SHA-256 | Cues | First cue | Final cue end | Normalized word tokens |
| --- | ---: | --- | ---: | --- | --- | ---: |
| [`The Wastes S1E119. Put Out The Fish Fire.parakeet.processed.srt`](../sources/The%20Wastes%20S1E119.%20Put%20Out%20The%20Fish%20Fire.parakeet.processed.srt) · processed Parakeet | 262,404 | `3294bca802624f97fa378bb0691e857eab502b0059687882f4284ee74ed2ad3d` | 2,690 | 00:00:10.320 | 02:47:48.900 | **23,943** |
| [`The Wastes S1E119. Put Out The Fish Fire.qwen-q8.canary-ctc.nemotron.srt`](../sources/The%20Wastes%20S1E119.%20Put%20Out%20The%20Fish%20Fire.qwen-q8.canary-ctc.nemotron.srt) · Qwen Q8/Canary CTC/Nemotron-labelled | 361,373 | `86d57644a4370ad08bf468ec44c40dd462b6e2c8a6e74c680ef099763142e27c` | 4,525 | 00:00:10.320 | 02:47:48.640 | **24,267** |

Primary full UTF-8 text was **262,404 characters**, secondary **361,314 characters**. Both cover introduction, gameplay and final outro; cue counts reflect very different segment lengths, **not independently measured speech recall**. Qwen ends **0.260 seconds earlier**. The matching endpoint does not independently establish that the underlying audio copies were identical.

**Normalization:** Extract SRT cue bodies in timestamp order; discard index/timing lines and optional `(speaker N)` tags; concatenate. Lowercase; remove straight and curly apostrophes (join contractions); replace other non-Unicode-letter/digit characters with whitespace; split words on whitespace. **Exact unit-cost ordered whole-sequence word Levenshtein distance** computed with arbitrary-width bit-vector dynamic programming over the 23,943 Parakeet-token sequence and 24,267 Qwen-token sequence, including the opening and closing credits.

**Result: 2,227 ordered word edits / 23,943 Parakeet words = 9.30% inter-ASR disagreement** (unrounded 9.3012588%). The secondary export has **324 more normalized word tokens**. **This is not WER, measured accuracy, confirmed hallucinations, missing spoken words or proof that Qwen is better.**

## High-value transcript distinctions, evidence boundaries and targeted listening

| Recording clock | Textual evidence / uncertain wording | Conservative editorial treatment |
| --- | --- | --- |
| **~00:09–00:23** | Both exports show **Pipe** missing, an eye-locator showing a cloth enclosure, and Nash later finding a **pipe-shaped Pipe in his pocket** | **Real discovery and return to infant form**; not an abduction, offworld trip or confirmed abilities for all newborns. Confirm child names and vision dialogue by listening |
| **~00:22–00:35** | Apprentice full name varies (`Dilenoria`, `Dylanoria`, `Dillinoria`/other ASR forms); **Dilo** nickname heard, competing colloquial joke-name through scene | **Attends one hunt as prospective apprentice**, not permanent enrollment. Confirm full written spelling against handout/audio |
| **~00:37–00:43** | **Stanley to Vorel**, alone: reports the Principle's **E115 warning** that the dangerous figure who killed George may be loose and return; he suspects Dilo could be **possessed** | **A secondhand, privately exchanged fear**, not seen Diontalus/crystal escape or evidence Dilo is possessed; keep identity of the alleged escaped entity qualified |
| **~00:43–00:49** | Hybrid name is rendered `Beirasaurus`/`barosaurus`/`bearsaurus`, Dilo calls it **Chester**; claim of bear/dinosaur gene mixture and century-long ecological threat | **Chester** fairly clear in both exports; hybrid's exact spelling awaits listening/written GM material. Laboratory history and past losses are **NPC testimony** |
| **~00:50–00:55** | Omnom **produces the Necklace of Fireballs**, previously given by Stanley, from under his scales; Vorel **declines** to take it | Actual retention by **Omnom**, no transfer back to Vorel or demonstrated remaining charges |
| **~01:03–01:09** | Roll20 map labels vary: **Villa Ornath (?)**, **Gatherers' Lodge**, hunting grounds **`Grushen/Grousen/Grushene (?)`**, other forest and lake names | Map is spoken-table navigation only; verify screenshot/source map before canonizing orthography or hex distances |
| **~01:13–01:22** | Tiefling **Fitz** greets Hope as queen and proposes mushrooms for Nobieri after handing out berries | Played Fitz encounter and request; **mushrooms not picked**, alleged vision effects untested |
| **~01:22–01:37** | Four squirrels actually exchange comprehensible speech and ask for nuts; Hope gives rations | No performed **Speak with Animals** spell or confirmed squirrel guidance to Chester |
| **~01:44–01:56** | Fishing elf's name sounds **`Tranquilar / Tranquila (?)`** across exports; speaks about lost hunters and offers chewing grass | Actual fisherman, borrowed place/color; anecdotal hunters' deaths **not direct observation** |
| **~01:58–02:10** | Camp fish and bait quantities: **10 fish / 10 heads**, one head missing an eye; GM settles on **250 fish eggs** in Nash's inventory | Fish actually caught, cooked and bait packaged; small number is a table adjudication, **not biological evidence** |
| **~02:12–02:35** | Creature's cry/steps cannot be identified by unsuccessful Nature/Perception checks; Dilo marks **nine possible search regions** | **No identified or visible Chester**, and nine marks are possible investigation areas, not sightings |
| **~02:36–02:46** | Vorel's **Storm Soul** ignites a wax-wrapped fish-head lure, thrown **150 feet**; Stanley's ***Prestidigitation*** extinguishes a small growing fire. Heavy steps approach | **Fire put out**; do not call this a forest wildfire, successful lure, kill or completed hunt |

**Audio-review priority:** ~00:38–00:46 **Diontalus warning vs actual E115 dialogue and Dilo identity** (critical); ~00:43–00:50 species/item phrasing; ~01:03–01:08 map spellings; ~02:35–02:47 *Storm Soul*, *Prestidigitation* and final unseen-creature cutoff. Secondary priority: Pipe's ability ~00:14–00:24, Omnom necklace ~00:50–00:55, Fitz/mushrooms ~01:14–01:22 and Tranquilar name ~01:47–01:55. **None have been audio verified**.

**E119 title boundary:** “Put Out The Fish Fire” refers to **Stanley actually extinguishing the burning fish bait at the end**, not destruction of all fish, a creature immolated, or a fire allowed to spread. After the cut, the host asks players to **prepare encounter positions** for next week; that is **out-of-game planning, not an enacted E119 combat turn**.

**Release/order:** A separately researched [September 2020 bonus](../episodes/BONUS-2020-09.md) precedes E119 in the owner's publication catalogue. A **successor main Wastes S1E120** is expected in corrected numbering, but **its exact transcript basename and availability were not independently checked here**. Do not fabricate an episode link until that source is resolved. [Review queue](../project/REVIEW_QUEUE.md).
