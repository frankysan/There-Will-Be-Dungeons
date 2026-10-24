# E113 — full-export ASR comparison (2026-10-23)

Source-first dossier: [E113](../episodes/E113.md). Two complete SRT exports were compared as text, through the end credits. No audio was heard or transcribed again.

**Measured result:** 1,455 exact ordered normalized word edits across 20,061 Parakeet words = **7.25% inter-model text disagreement**, not WER or audio-verified accuracy. Qwen has 144 more normalized tokens, not a confirmed omission count.

## Method and source identity

At the start of research, repository `main` was clean at commit `970f6a6ef8417034e75fe509377ce8d8783a7ab5`. Both complete source files were read through their final credits at that commit. For comparison, strip SRT cue numbers and time lines and speaker labels, lowercase, delete apostrophes, replace other non-letter/non-digit characters with whitespace, then tokenize. Exact ordered unit-cost word Levenshtein distance was computed over the complete normalized sequences.

| Source | Characters | Cues | First cue | Last cue | Normalized words |
| --- | ---: | ---: | --- | --- | ---: |
| [Parakeet](../sources/The%20Wastes%20S1E113.%20I%20Need%20To%20Smell%20Your%20Hand.parakeet.processed.srt) | 209,909 | 2,271 | 00:00:06.880 | 02:40:25.300 | 20,061 |
| [Qwen-labelled](../sources/The%20Wastes%20S1E113.%20I%20Need%20To%20Smell%20Your%20Hand.qwen-q8.canary-ctc.nemotron.srt) | 281,448 | 3,677 | 00:00:06.960 | 02:40:24.950 | 20,205 |

Git blob identifiers: Parakeet `6dc7b4298c240c6dd88bafdd98a6fa9bbd20840d`; Qwen `b7b2ceb5e67f8309124266f394cd0302bd7f6a55`. These are not raw-file SHA-256. Workspace binary reader independently identified the Parakeet source as **220,710 bytes**, SHA-256 `90e6aa00080cb3f8d0807f4fc6f6f30bed052d792be0a522546ebfb0d0f065ba`. Pipeline labels are inferred from filenames. No runtime settings or speeds are verified.

## Recording-clock discrepancies and listening priorities

| Recording clock | Issue requiring verification | Safe interpretation from existing transcripts |
| --- | --- | --- |
| 00:00–00:05 | Host says **August 2, 2020**; prior owner catalogue identifies August 3 publication | Recording and release dates are different |
| 00:13–00:35 | **Headsy/Hedzy** name, direction to **Pointless**, and responsive separated head | Orc is not confirmed dead |
| 00:32–00:43 | Hope also turns gray; Steerious retains color | E112's initial effects change during E113 |
| 00:43–01:04 | **Fox** versus Scully, Steerious's sword, Blood Skunk's toe, Dr. Spider's coat | All four ferry payments performed; no item returned |
| 01:13–01:29 | Serpent **Velithon/Velothan/Velathon (?)**, private hooded Voice and future meeting | The creature leaves peacefully; no reunion with its master |
| 01:29–01:52 | Arrival, recovery from Gray Waste, imp **Voxil/Varkso (?)**, Dario | Ferry journey and Council entry performed |
| 01:52–02:29 | Council's recognition by smell and Hope's descriptions of her history | Councillors' cosmological assertions and Hope's memories are attributed statements |
| 02:29–02:37 | Prison **Pentel Weiss/Pentelvice/Pentalvise (?)**, **Corinthian Nebula**, hope-keyed compass | Council gives possible location and physical compass, not the Eye |
| 02:37–02:40 | Hope's ring Gate returns all four to Tobacho's tavern | Actual departure from Pandemonium and arrival in Sigil |

**High-value audio checks:** names, meaningful fare and item custody, whether Hope's altered appearance reveals her patron to the serpent, the exact prison spelling/coordinates, possession of the wind-up compass and the completed return Gate. No audio checked. The host's preview of the next main-party session is **out-of-game**, not proof of its actual contents. Next corrected archive file has now been **verified** using the owner's numbering snapshot and both binary source inventories: [E114 — I hope that's a baby (Parakeet)](../sources/The%20Wastes%20S1E114.%20I%20hope%20that%27s%20a%20baby.parakeet.processed.srt) · [Qwen](../sources/The%20Wastes%20S1E114.%20I%20hope%20that%27s%20a%20baby.qwen-q8.canary-ctc.nemotron.srt). Owner publication identifier **TWBD 116**, date **August 10, 2020**; episode **not yet analyzed**.
