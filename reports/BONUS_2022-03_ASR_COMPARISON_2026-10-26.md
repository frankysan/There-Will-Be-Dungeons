# Bonus 2022-03 — March 2022: full-export ASR comparison (2026-10-26)

**Type:** Out-of-game **monthly listener Q&A**, not a Wastes campaign episode. [Source-first bonus dossier](../episodes/BONUS-2022-03.md). Filename's **March 2022** is the owner-approved **public publication month**, not independently verified recording day or supporters' release date.

**Version/provenance:** Workspace `main` initial HEAD `50c587bf5ffd5b1f450add6f14df76e982ac1f98` with **two unrelated Delvers files already modified**, not overwritten. GitHub default-branch source Git blobs P `6f382e56fbe14d2101d3dcf11b3a6d9320573632`, Q `a4342f3af30465807998e7191a8865a812e7e12e`. Neither MP3 audio nor public RSS listened/checked; **no local entire-byte comparison against GitHub copies**. Filename labels do not attest actual run parameters or model version.

| Independently labeled export | Git blob SHA | SRT cues | Normalized words | End timestamp | Text length |
| --- | --- | ---: | ---: | --- | ---: |
| [Parakeet processed](../sources/Bonus%202022-03%20-%20March%202022.parakeet.processed.srt) | `6f382e56fbe14d2101d3dcf11b3a6d9320573632` | **734** | **6,852** | **00:36:35.270** | **69,438 characters** |
| [Qwen Q8 / Canary CTC / Nemotron](../sources/Bonus%202022-03%20-%20March%202022.qwen-q8.canary-ctc.nemotron.srt) | `a4342f3af30465807998e7191a8865a812e7e12e` | **1,114** | **6,972** | **00:36:34.940** | **89,077 characters** |

**Exact method:** Independently parse ALL SRT blocks, discard numeric cue indices/timing lines and optional `(speaker N)` tags; join only spoken cue text in recording order. Lowercase, strip straight and curly apostrophes (joining contractions), replace any other non-Unicode-letter/digit characters with spaces and split into word tokens. Ordered global **unit-cost word Levenshtein** with insertions/deletions/substitutions 1, two DP rows and diagonal band ±3,000. **Observed optimal distance 505 is strictly below band width, establishing that the banded result equals the unrestricted global distance.** Parakeet denominator: **505 / 6,852 = 7.37% inter-ASR TEXTUAL disagreement**, Qwen has **120 more normalized words**. **Not WER or a claim of relative accuracy**; differences are not independently confirmed omissions, hallucinations or corrections.

## Text-only risk and disagreement map

| Time | Review question / ASR-risk |
| --- | --- |
| **~00:00:40–00:02:15** | Beau's reply about Badass T's **unexpected bite and unknown lip regrowth** is fairly clear in both exports; note Beau **speculates** about magical meat dangers and exploding mushroom eater, not a played past massacre. |
| **~00:02:15–00:12:30** | Rapid turn-taking among cast discussing DM fright, breathing and improv; **speaker attribution** depends on context and is ASR-provisional, not diarization-verified. |
| **~00:12:35–00:13:25** | Listener question remembers Nash INT **4**, while played S2E05 establishes **3** (and DEX 3). Keep both with proper scope rather than “repairing” original question. |
| **~00:14:00–00:20:10** | Jon discusses **Stanley low-WIS strategy**, Scott recalls **Nash's dragon instincts and temporary higher INT**; verify player voice if reusing direct quotes. No newly played dragon-form activation occurs in the bonus. |
| **~00:20:55–00:24:45** | Beau separates roleplay latitude from adjudicated rolls; Jon states **baseline Stanley INT 14/WIS 16 and Nash INT 16/WIS 12**. These are table claims, not verified character-sheet snapshots. |
| **~00:25:00–00:28:33** | Scott regrets a disability-stereotype performance, Beau uncertain of rule threshold for extreme stats. Don't endorse a stereotypical equivalence between cognitive disability and low D&D scores, or make an uncited D&D rules claim. |
| **~00:28:33–00:34:25** | Proposed **Stanley snapdragon / Hope yellow carnation**, personal stargazer lily / red rose; other flower-meaning legend and Nash mushroom-flower are loose jokes. Audio may resolve lavender speaker. No acquired in-world motifs. |
| **~00:34:25–00:36:35** | Free-form pop-culture banter and actual show signoff; do not tag it as a second played episode or campaign finale. |

**Coverage:** Complete primary P sequence manually reviewed in two bounded recording-clock passes **00:00–00:15** and **00:15–00:36:35**; full independent Q sequence parsed/counts/distance, selected Q passages independently examined at **00:00–00:03, 00:12–00:15, 00:17–00:27, 00:28–00:33**; **not full secondary editorial review**. No original audio verification. The metric describes transcription disagreement only.

**Next verified bonus:** [April 2022](../sources/Bonus%202022-04%20-%20April%202022.parakeet.processed.srt), not analyzed in this pass. 
