# E125 — Parakeet/Qwen full-export ASR comparison (2026-10-24)

> **The Wastes · corrected S1E125 — A Case of Malpractice**. [Episode dossier](../episodes/E125.md). Two available sources were retrieved as text from GitHub **at the same revision `14b04dd8b33c14af058293a25f9bb34f591cb61b`** recorded in the clean connected workspace. Both exports parsed entirely through the closing network outro; full primary text editorially reviewed by recording window; Qwen **selectively** examined for contested names and pivotal scenes, **not comprehensively interpreted across the whole recording**. No audio listening, ASR re-execution, or source edits. Acoustic waveform identity and historical model/settings not established.

## Inventory and exact comparison

| File / filename-inferred model | Bytes / workspace SHA-256 | Cues | First cue | Last cue | Normalized word tokens |
| --- | --- | ---: | --- | --- | ---: |
| [Parakeet processed](../sources/The%20Wastes%20S1E125.%20A%20Case%20of%20Malpractice.parakeet.processed.srt) | **248,432** / `12d09ca21cc7ee3b1081b81415ee1e1d928e363aa1acb4441c5ab6b9365b0eaf` | **2,527** | 00:00:08.160 | **02:34:08.740** | **22,800** |
| [Qwen Q8/Canary CTC/Nemotron-labelled](../sources/The%20Wastes%20S1E125.%20A%20Case%20of%20Malpractice.qwen-q8.canary-ctc.nemotron.srt) | **345,229** / `04a9e8c1e486101f956f8a9db5e5c39f6d01f0fba0bad71307c03e981982f731` | **4,292** | 00:00:08.240 | **02:34:08.440** | **23,383** |

**Exact result: 2,506 ordered word edits / 22,800 Parakeet words = 10.99% inter-ASR textual disagreement** (10.9912% unrounded); secondary has **583 additional normalized words**. The metric uses the shared project's `asr_metrics.py` algorithm reproduced as an exact arbitrary-precision bit-vector Levenshtein operation over the fetched full exports. Normalization: concatenate text from every cue in chronological order, exclude cue numbers/timestamps and optional `(speaker N)` prefix, lowercase, **delete straight/curly apostrophes** (join contractions), convert characters other than Unicode letters/digits to spaces, and split into word tokens. **This is not WER, correctness, speech omissions or hallucination counts**. Time-aligned candidate operations use a different method and must not be substituted for the exact global metric.

The existing `tools/prepare_episode.py` was **not executed in this connector-only environment**; these figures came from the same specified normalization and exact calculation applied to full remote text. Model labels inferred from filenames, not metadata; close beginning/end SRT clocks do not prove equivalent audio inputs. No runtime/GPU benchmark or original audio verification.

## Critical transcript comparisons and episode-specific risks

| Approximate recording clock | Cross-source reading / evidence concern | Safe editorial treatment |
| --- | --- | --- |
| 00:04–00:11 | E124 Diontalus accord restated; Elhandari High Elf rendered **Amanthalodar/Amenthalodar/Amethyst Lodor (?)**. New engineer in both exports **Tungsten Wheel** | High Elf reports suitable but absent engineer; name still ASR-only. Not an actual meeting or construction. |
| 00:12–00:17 | Lover's improvised name rendered roughly **Dungstil/Dungilsta Ravensbread (?)** in Qwen; Parakeet **Dung Still / Dung Star Ravens Bread**. Mars terraforming tree and toxic outside | Preserve alternatives pending audio or GM notes; two **teleportation glyphs actually supplied**, no teleportation performed. |
| 00:18–00:22 | Diontalus demands future killing blow against Principle; gives **wooden ocarina**. Both exports distinguish ethereal appearance from physical solidification | Actual artifact custody to Stanley, **unplayed** summon and still-conditional help against Principle. |
| 00:24–00:26 | Diontalus **admits deer mage coercion** and claims phantom pirates served as his transport during his escape | First is antagonist admission, not earlier observed intent; second is his retrospective claim, not proof of all individual pirate deeds. |
| 00:29–00:39 | Floating castle, large fleet and hundred Hive combatants. Commander name **Henitar/Henatar Grape (?)**, army **Asphyxiant (?)**; says Mind Master **Gerbkin/Gerbken Shartlinger** hired him and **Tobacho Fleur** has been maze-imprisoned | Existing historical spelling **Gerbken Shartlinger**, **Tobacho Fleur**; claim of informing Lady of Pain and exact contract is mercenary testimony, not independently observed Sigil history. |
| 00:42–01:14 | Destructive Wave, Hope's attack, High Elf's living trees/wind wall, Diontalus's ghost-reaping; berries **grant Haste-like effect** | Distinguish table rulings, the two Destructive Wave castings and physical damage from reliable body/death census. |
| 01:01–01:02 | Nash's performed Chain Lightning couplet approximates **'Here I float above your heads / May all these volts put you to bed'** | ASR-only new casting phrase; verify exact vowels/words against audio, then source-index the phrase register. |
| 01:23–01:27 | Nash adds Haste to the berry effect with phrase approximately **'Hey Vorel, have a taste / It's time for a little bit more of the haste'**; proposed **Stinking Cloud** refused/uncast | Explicit table-specific stacked Haste and one-spell ruling; preserve performed/attempted distinction and audio-review phrase wording. |
| 01:37–01:45 | Station starts falling; High Elf urges villa shelter. **Diontalus teleports out and visibly attacks multiple hostile airships**; elevator scene verbally misidentifies family member **Squirts**, then explicitly corrects to **Chunks** | Diontalus actually helps in fleet battle; no false local Squirts resurrection on Elhandar. |
| 01:47–02:03 | Elevator cable snaps; Feather Fall **performed**; Vorel's first roof-cut fails, second succeeds with aid | Family escapes car alive; do not imply Feather Fall alone stopped the heavy metal car. |
| 02:13–02:21 | Stanley **readies/proposes** Resilient Sphere but does not cast it; Lyrielle **casts Wall of Force**, enabling speeders to reach villa. Safe-room seats manifest and a loud impact follows | Actual spell and physical flight separated from **unused** contingency; no confirmed post-impact survival/death or completed Mars mission. |
| 02:22–02:31 | Played Hell group meets Brent, Mysteriosa and a **newly awakened kobold named Squirts**. Brent **claims** to have obtained her soul and had the body modified | On-screen reappearance and leadership appointment in Hell; do not undo E111 killing or E124 roster conflict retroactively. |

## Source status, next work and listening queue

Prioritize listening for 00:10–00:16 engineer/lover and station names; 00:33–00:39 fleet/contract/Sigil revelations; 01:01–01:02 and 01:23–01:27 **Nash spellcasting words**; 01:40–01:45 **Diontalus observed intervention and Chunks correction**; 02:13–02:21 **Wall of Force and crash**; 02:29–02:31 **Squirts's reappearance**. These are **text-only review targets, not verified dialogue or confirmed ASR errors**.

**Next main-session corrected number expected E126, exact source basename/title and availability not independently checked here.** Keep the separate monthly-bonus pointer unaffected. No original SRTs or media were edited.
