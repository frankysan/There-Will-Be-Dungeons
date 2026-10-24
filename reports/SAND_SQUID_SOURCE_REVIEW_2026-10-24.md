# Sand squid — targeted source review

**Date:** 2026-10-24. **Campaign:** The Wastes, Season One. **Result:** Owner-supplied candidate promoted to a published [creature article](../world/creatures/sand-squid.md). [Season-wide discovery](WASTES_S1_CREATURE_SEARCH_2026-10-24.md) · [Machine-readable evidence inventory](SAND_SQUID_SOURCE_REVIEW_2026-10-24.json).

## Scope and correction

The initial dossier-only scan grouped sand squid with an unidentified shelter carcass as low-information material. That assessment gave too much weight to direct creature encounters and too little to repeated food and ingredient use. **Sand squid qualify through their established role in everyday life**, even without many fights. Targeted transcript review also located a played hunt and explicit ecological information that the compressed E015 dossier did not preserve in detail.

The follow-up keyword scan parsed **279 available Wastes S1E subtitle exports** and found **226 matching cues** for `squid|squids|squiddy|squidy`. This includes multiple exports, split dialogue, unrelated squidlike organisms and ASR name errors: **226 is not a count of independent sand-squid mentions**. The JSON inventories every scanned file with its SHA-256, cue count, ending clock and matching cue indices; full matching cue text and generated context are retained locally at `local/creature-search/sand-squid-2026-10-24/search.json`.

Interpretive review is limited to the **18 windows below**, spanning nine primary-export episodes and Qwen checks in E012/E015. No complete episode was reanalyzed and no audio was heard. No full-export ASR metric was calculated. Export labels are inferred from filenames. Cue boundaries are subtitle timing, not word timing; cross-model agreement does not verify the audio.

## Findings supported by reviewed passages

| Evidence | Finding | Boundary |
| --- | --- | --- |
| [E010](../episodes/E010.md), ~02:01 | Sand-squid meat is thrown to the captive travelers as food; Vorel recognizes it. | First food reference located by this search, not a claim of first-ever occurrence. |
| [E012](../episodes/E012.md), ~00:24–00:28 and ~01:12–01:13 | Sandwiches and fried strips are offered; the magistrate and other diners eat squid with eggs. The meat is described as fatty, cheap and generally low quality. | Distinguish dishes offered from those actually served; Vorel enjoys what others regard as modest food. |
| E012, ~02:02–02:04 | Lattlebing visibly squeezes white creamy juice from a dead, tentacled, bulbous-headed squid into coffee. | Culinary juice, not evidence of mammalian milk production. |
| [E015](../episodes/E015.md), ~02:20–02:23 and ~02:29–02:31 | Sand squid move in schools through sand/dirt, feed on insects at habitual stops, and can be caught by waiting and grabbing them from the earth. A live specimen has two eyes and front tentacles; Vorel catches and kills it. Stanley separately takes dried stores from the hotel. | General behavior is narrated setting information; capture and kill are played actions. A gestured length cannot supply a numerical measurement. The E018 shelter carcass remains unidentified. |
| [E016](../episodes/E016.md), ~02:13–02:15 | Drying shrinks the animals, and several make a ration. The party assembles travel provisions; salt, pepper and squid-sauce flavorings are mentioned. | Ration counts and carrying weights are table-level provisioning details, not universal biology. |
| [E017](../episodes/E017.md), ~00:25 and ~00:55 | Cans appear in a general store; sand-squid soup is offered. | The soup offer is declined; do not claim the party ate it in that passage. |
| [E026](../episodes/E026.md), ~01:44–01:46; [E055](../episodes/E055.md), ~01:31–01:32 | Fried squid feeds a camp kitchen line; squid sandwiches remain on a Tietkalla inn's menu. | Establishes recurring food use across locations, not a complete trade network or supply chain. |
| [E082](../episodes/E082.md), ~02:12–02:15 | Vorel asks for squeezed-squid juice in Sigil coffee, and the server has none. | A remembered preference, not proof sand squid are sold or native in Sigil. |
| [E123](../episodes/E123.md), ~02:10 | Another pale breakfast drink is compared with sand-squid milk. | Familiar comparison only: it is not identified as actual squid juice or a fresh sighting. |

## Reviewed source windows

Each export link points to the exact local source basename. Hashes and full scan inventory are in the JSON. No source export was edited.

| Episode / export label | Recording window | Source |
| --- | --- | --- |
| E010 / parakeet | 02:00:00–02:02:15 | [Export](../sources/The%20Wastes%20S1E010.%20Shackles.parakeet.processed.srt) |
| E012 / parakeet | 00:24:15–00:28:30 | [Export](../sources/The%20Wastes%20S1E012.%20Work%20Hours.parakeet.processed.srt) |
| E012 / parakeet | 01:12:15–01:13:40 | [Export](../sources/The%20Wastes%20S1E012.%20Work%20Hours.parakeet.processed.srt) |
| E012 / parakeet | 02:01:55–02:04:20 | [Export](../sources/The%20Wastes%20S1E012.%20Work%20Hours.parakeet.processed.srt) |
| E015 / parakeet | 02:20:05–02:23:45 | [Export](../sources/The%20Wastes%20S1E015.%20The%20Darkness.parakeet.processed.srt) |
| E015 / parakeet | 02:28:50–02:31:20 | [Export](../sources/The%20Wastes%20S1E015.%20The%20Darkness.parakeet.processed.srt) |
| E016 / parakeet | 02:13:00–02:15:05 | [Export](../sources/The%20Wastes%20S1E016.%20Dragon%20Mother.parakeet.processed.srt) |
| E017 / parakeet | 00:24:40–00:26:00 | [Export](../sources/The%20Wastes%20S1E017.%20Fire%20in%20the%20hole%21.parakeet.processed.srt) |
| E017 / parakeet | 00:55:20–00:56:25 | [Export](../sources/The%20Wastes%20S1E017.%20Fire%20in%20the%20hole%21.parakeet.processed.srt) |
| E026 / parakeet | 01:44:15–01:45:55 | [Export](../sources/The%20Wastes%20S1E026.%20The%20Hunt.parakeet.processed.srt) |
| E055 / parakeet | 01:31:10–01:32:15 | [Export](../sources/The%20Wastes%20S1E055.%20My%20Standards%20Are%20Very%20Lizard.parakeet.processed.srt) |
| E082 / parakeet | 02:11:50–02:14:50 | [Export](../sources/The%20Wastes%20S1E082.%20Binch%20Better%20Have%20My%20Money.parakeet.processed.srt) |
| E123 / parakeet | 02:09:55–02:10:50 | [Export](../sources/The%20Wastes%20S1E123.%20No%20Floating%20Forks.parakeet.processed.srt) |
| E012 / qwen | 00:27:50–00:28:25 | [Export](../sources/The%20Wastes%20S1E012.%20Work%20Hours.qwen-q8.canary-ctc.nemotron.srt) |
| E012 / qwen | 02:02:15–02:04:00 | [Export](../sources/The%20Wastes%20S1E012.%20Work%20Hours.qwen-q8.canary-ctc.nemotron.srt) |
| E015 / qwen | 02:20:18–02:21:05 | [Export](../sources/The%20Wastes%20S1E015.%20The%20Darkness.qwen-q8.canary-ctc.nemotron.srt) |
| E015 / qwen | 02:23:00–02:23:48 | [Export](../sources/The%20Wastes%20S1E015.%20The%20Darkness.qwen-q8.canary-ctc.nemotron.srt) |
| E015 / qwen | 02:29:10–02:30:10 | [Export](../sources/The%20Wastes%20S1E015.%20The%20Darkness.qwen-q8.canary-ctc.nemotron.srt) |

## Exclusions and unresolved details

- E078–E079's small squidlike organisms in a CHIDS pool are not identified as sand squid. Do not merge them on shape alone.
- Several Qwen hits in E083/E084/E086, and a hit in E088, concern the NPC **Squirts** or uncertain name recognition rather than zoology.
- E010's early jet/squid analogy is not a creature encounter. Other located cooking, food and remembered-hunt references outside the reviewed windows remain discovery leads, not fully interpreted passages.
- The [June 2019 bonus](../episodes/BONUS-2019-06.md) discusses sand-fishing as setting design; the [July 2020 bonus](../episodes/BONUS-2020-07.md) does not confirm a lineage from the Dunebreaker's gelatin. These are commentary sources, not new played hunts or proven ancestry.
- Species-wide size, reproduction, lifespan, taxonomy and exact physiology beyond the described features remain unsupported. No official D&D baseline comparison was made.

## Integration

Published a short subject-focused article with ecology, food use and current role, source details in footnotes and **Current status** last. Added it to the category index, corrected the discovery report's low-information grouping, and recorded the broader food/ingredient criterion in the shared category policy. The season-wide inventory remains an initial dossier scan; this follow-up is explicitly separate. No campaign research pointer, character biography, original transcript or media file was changed.
