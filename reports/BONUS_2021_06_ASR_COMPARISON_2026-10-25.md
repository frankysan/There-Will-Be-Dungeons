# BONUS-2021-06 — June 2021: exact complete-export ASR comparison (2026-10-25)

**Identity/type:** `Bonus 2021-06 - June 2021`, explicit June 2021 spoken by Scott Johnson, **cross-campaign out-of-game Q&A** with Jon, Kristen and Kyle; Bo absent. Recording/publication date not independently verified. [Source-first topic dossier](../episodes/BONUS-2021-06.md) · [shared bonus queue](../project/REVIEW_QUEUE.md).

**Source routing/revision caveat:** MCP `There Will Be Dungeons Transcripts` `main` started **clean** at `2e4538a62d5d4de03f434dbab95cecaeaa346a8d`. GitHub could **not resolve that local commit** (404), so full-export measurements refer to **remote default-branch Git file blobs below**, **not verified byte-identical local checkout blobs**. Local MCP beginning of P/Q independently matched remote openings, Q final lines matched remote ending; **complete byte-for-byte equality, aligned MP3 and exact audio inputs not confirmed**.

| Filename-derived pipeline label (runtime options unverified) | Source | Remote Git blob | Cues | Unicode normalized words | Last cue end |
| --- | --- | --- | ---: | ---: | --- |
| Parakeet processed | [P](../sources/Bonus%202021-06%20-%20June%202021.parakeet.processed.srt) | `0dc420335e620bea2aa79d82fd6264826052759e` | **643** | **6,183** | **00:33:57.590** |
| Qwen Q8 / Canary CTC / Nemotron-labelled | [Q](../sources/Bonus%202021-06%20-%20June%202021.qwen-q8.canary-ctc.nemotron.srt) | `956cd441a055c011e3ce0e81deae7b35c8998be8` | **980** | **6,317** | **00:33:57.500** |

**Exact full-remote-export unit-cost word Levenshtein distance = 514 / 6,183 = 8.31% textual disagreement**. Q has **134 more words**; Q final cue ends **0.090 s earlier**. **Not WER, accuracy, validated omission/hallucination count or evidence that Q is correct.**

**Algorithm:** Parse each complete SRT into chronologically ordered text cues, drop cue numbers, timestamp lines and `(speaker N)` labels; lowercase, remove straight/curly apostrophes (joining contractions), replace all non-Unicode-letter/digit characters with spaces, tokenize. Two-row DP bounded to **±650 word-token index band**: final cost **514 < 650** certifies no cheaper path leaves band, hence exact; matching prefix/suffix lengths zero. Full Parakeet in seven clock windows (~0–5, 5–10, 10–15, 15–20, 20–25, 25–30, 30–33:57); complete Q parsed for metric and selected independent Q interpretive windows ~0–2, 3–8, 8–12, 12–17, 17–23, 25–31 and 30–34. **Q not fully narrative-reviewed**; no original MP3 listening, wave seek offsets, listener submissions, publisher metadata, Discord image, model configs, hardware or performance timing measured.

| Clock | High-risk textual/audio targets |
| --- | --- |
| **00:00–00:02** | P begins `no welcome` at **00:00.480**, Q starts **`Welcome` at 00:03.520**, Q has more plausible opening but *not audio verified*; Bo explicitly absent. |
| **~00:03–00:06** | Potato growing **Scott player commentary, not farm mechanics**; kill/marry/one-night scenario **hypothetical**, no Delvers event. |
| **~00:06–00:09** | Kyle says **Apparatus of the Crab/Kwalish** and actual **published lever list**; original third-edition **Discord illustration not accessed**, do not claim invented visual. |
| **~00:09–00:13** | Wastes **Immovable Rod**, Dragon Orb, **Hand of Vecna** reminisced about; no new acquisition/loss evidence. |
| **~00:13–00:18** | Original character **Bob** self-corrected from Roger; **Kyrith** phonetic; druid/wolf Amadeus, tiefling Carrie biography are real-world old PCs, not lore crossovers. |
| **~00:18–00:23** | Waluigi rejected as playable main; **Nash Lucas, Stanley Robin/Mewtwo, Vorel Donkey Kong, Hope Dark Samus**, Delvers analogies. Real opinion, **not new canon**. |
| **~00:26–00:31** | Speaker unsure exactly what weapon mechanics were reskinned for Wastes guns/car. Cast discussing Deadlands/Starfinder/Monster of the Week, **no switch agreed**. |
| **~00:31–00:34** | DM rotation/return to Wastes **possibility not commitment**, **Garpoon** spelling uncertain, next July bonus **promised only**. |

**Next tests:** direct listening to unique high-risk proper-name and intro windows; inspect Discord crab drawing to tie visual version to played props; keep retrospective intent separate from historical campaign event. No existing SRT/MP3 modified.
