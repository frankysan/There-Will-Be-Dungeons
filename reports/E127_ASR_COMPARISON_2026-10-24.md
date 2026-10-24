# E127 — Parakeet/Qwen full-export ASR comparison (2026-10-24)

> **Corrected The Wastes S1E127 — “Spider Claws”; original TWBD 129, Christmas one-off with Kyle Ferguson DM and new PCs**, not E126 desert-battle continuation. [Source-first dossier](../episodes/E127.md). Both complete UTF-8 subtitle exports read from GitHub at pinned `d9ff8e10a2092b81b8b985f9d7f110fcc868e2e4`, matching the repository's observed `main` HEAD before work; existing checkout had **26 unrelated/in-progress Markdown changes** and was **not clean**. No ASR/audio files edited. Both exports parsed to closing ~02:54, primary editorially reviewed across clock, Qwen sampled at important changes rather than full interpretive read.

| Source / label inferred from filename | Git blob SHA (not file SHA-256) | Cues | Final subtitle end | Normalized word tokens |
| --- | --- | ---: | --- | ---: |
| [Parakeet processed](../sources/The%20Wastes%20S1E127.%20Spider%20Claws.parakeet.processed.srt) | `451d6cfccd523877c1f0faaa638a65b3efed3074` | **2,454** | **02:54:06.700** | **22,027** |
| [Qwen Q8/Canary CTC/Nemotron-labelled](../sources/The%20Wastes%20S1E127.%20Spider%20Claws.qwen-q8.canary-ctc.nemotron.srt) | `93648a464d443b32ba919c7bd88d756fb8dc1243` | **4,136** | **02:54:06.420** | **22,195** |

**Exact ordered unit-cost Levenshtein distance = 1,476 edits / 22,027 Parakeet tokens = 6.70% inter-ASR text disagreement**, Qwen **+168 tokens**. Both full SRT sequences normalized by omitting cue numbers/timestamps and optional `(speaker N)`, joining text chronologically, lowercasing, deleting straight/curly apostrophes, replacing non-Unicode letters/digits with whitespace and splitting into tokens. Exact diagonal DP distance used (insertion, deletion or substitution cost 1 each); **five minimal oracle examples tested successfully**. This is **not WER, acoustic accuracy or verified omission/hallucination rate**. No audio playback, waveform/source hash equivalence, model settings or local `tools/prepare_episode.py` execution. Source sizes as fetched character counts **227,870 / 312,941**, **not byte sizes**; Git blob SHAs given rather than invented SHA-256 digests.

## Pivotal windows to compare or listen to

| Approx. recording time | ASR-supported / differing issue | Safe treatment |
| --- | --- | --- |
| 00:00–00:07 | **Kyle is the special DM, Beau absent**. PCs **Davanos/Devanos**, **Riley**, **Darnell Clovis**; doctor announces **Spinner's Council/Dr. Spider Christmas** | New Wastes one-shot characters; **no Nash, Hope, Vorel or Stanley played**; separate from E126. Speech about Dr. Spider does not identify an on-screen professor yet |
| 00:11–00:28 | Real vs painted doors/furnishings, **dead imp “elf on shelf”**, neglected stockings/fire/couch | Actual failed decoration adjudication; pudding spawned as punishment, not ordinary Christmas magic |
| 00:27–00:41 | Figgy-pudding ooze defeated by **Riley's butcher knife**, echo stabs, ranger arrows | Real ooze kill; Davanos' projected double is **not a second adventurer** |
| 00:42–01:00 | **Frosty/Bumble/Snow Miser** choice; snow activities pass, tube-goggle prize; names **painted onto Good list**, Santa chosen | No fight against Frosty/Bumble/Grinch/Krampus; altered list is performed rather than imagined |
| 01:10–01:35 | **Undead deer and engineered Rudolph**; powered nose's radiant beam **downs Riley**, Darnell **casts Cure Wounds**, **Davanos echo kills Rudolph**; costumed ogre opens passage | **Riley survives**, ogre **not attacked or killed**; distinguish reindeer group's deaths from Rudolph |
| 01:36–02:13 | Professor objects to **Nice-list cheating**, “gift” reveals concealed **coal/crusher trap**; rope/camera prevents deaths. Mage Hand and echo-swap enable passage; **Fly arrives from wild-magic roll after the climb** | No already-earned safe prize/freedom; no character crushed, no planned Fly used in advance |
| 02:14–02:44 | Ice-producing imps/creature pens; **Professor Spider**, minigun and **Ethereal Jaunt**, falls to ranged attacks and Earthen Grasp | **Professor dies**, not necessarily **Dr. Spider**; prisoners left caged |
| 02:44–02:54 | Infernal-menu black device Earth coordinate **47829873**; Riley enters it, three wake at home; closing credits | Actual exit and one-off close; no proof code is reusable for main campaign or an E126-resolution event |

**Priority audio review:** ~00:01–00:06 speaker names, Dr Spider vs Spinner's Council; ~01:20–01:31 Rudolph beam/0HP/heal; ~01:35–01:40 objections/Doctor vs Professor distinction; ~02:27–02:44 Professor identity/death; ~02:45–02:52 Infernal menu, exact code and physical homecoming. Research labels remain **ASR-only**; original audio, historic model settings and copy alignment unverified. **Next regular Arc Five source corrected E128 “Burrow”**, not a presumed direct E127 continuation.
