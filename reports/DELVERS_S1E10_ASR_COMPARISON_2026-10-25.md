# Delvers S1E10 — Fish Wizards!: ASR comparison (2026-10-25)

**Source-identity follow-up, 2026-10-27:** The [S1E12–S1E08 batch check](DELVERS_S1E12_S1E08_SOURCE_IDENTITY_2026-10-27.md#s1e10) verifies both complete local exports against their recorded Git blobs after CRLF-to-LF conversion only, and verifies both source paths in the recorded source commit. Raw bytes differ in line endings. This independently confirms local content correspondence with the originally pinned source revision. Earlier provenance statements remain dated history. Prior interpretive coverage, inter-ASR measurements, played cutoff and audio status are unchanged.

**Identity:** played *Delvers* Season 1 Episode **S1E10 — Fish Wizards!**, from exact owner-normalized [source inventory](../delvers/SOURCE_INVENTORY.md), not extrapolated from later episode title. Private `frankysan/There-Will-Be-Dungeons-Transcripts` at pinned initial clean `main` commit `aabee4ffbdba2ff981522294c9dc0e62bfb0553d`. Original audio **not listened to**, SRT-to-MP3 seek alignment and equal input audio **not verified**.

| Export (filename inferred pipeline) | Link | Git blob SHA | Complete cues | Final cue end | Normalized tokens |
| --- | --- | --- | ---: | --- | ---: |
| Parakeet processed | [SRT](../sources/Delvers%20S1E10.%20Fish%20Wizards!.parakeet.processed.srt) | `941924c983b27ba8f81ed77a7d550befd6dcf6f0` | **2,759** | **03:05:52.270** | **24,984** |
| Qwen Q8 / Canary CTC / Nemotron-labelled | [SRT](../sources/Delvers%20S1E10.%20Fish%20Wizards!.qwen-q8.canary-ctc.nemotron.srt) | `8ae4c5ab3a6e2868c477d86de97521248ae96b33` | **4,519** | **03:05:51.960** | **25,124** |

## Exact whole-export word comparison

**2,066 ordered unit-cost word edits / 24,984 Parakeet words = 8.27% inter-ASR textual disagreement**. Qwen is **140 normalized tokens longer**, ending 0.310 seconds earlier. The number represents **textual disagreement only, not WER, ASR accuracy or audio-certified hallucination/omission**. The clocks do not prove input audio identity.

Procedure: parse **all cues** per export; strip numbers/times and optional `(speaker N)`; join content in order, lowercase Unicode text, remove straight/curly apostrophes (join contractions), replace non-Unicode-letter/digit runs with spaces, and tokenize. Calculate **unit-cost substitution/insertion/deletion Levenshtein distance** across entire token sequences using two-row dynamic programming and **4,000-token diagonal band**. Result **2,066** is interior/below bound and therefore the globally optimal full ordered-word distance. Not time-aware/cue-paired word error rate.

**Scope and integrity:** Entire primary Parakeet SRT examined in sequential bounded recording-clock windows, including opening staged recap, 8 AM guild meeting, lake village and underwater final conversation/outro. Both entire exports parsed for metric. Qwen **selectively close-read** at spouse/black sand, Elven code, guild instructions, lake approach, mimic, underwater chamber, ring and final ritualist claims; **not full independent Qwen close-reading**. No source audio listened, original encounter maps/handouts or historic D&D Beyond states inspected, `tools/prepare_episode.py` rerun, run configurations/hardware measured or local tests executed.

## Material points where transcript interpretation matters

| Approximate clock | Text-level result / limitation |
| --- | --- |
| ~00:00–00:04 | **Staged/edited interrogation recap** is production framing, not a fresh canonical arrest. **Margaret makes an actual Evelyn decoy with Nolzur's Marvelous Pigments**, unlike unperformed prior Alter Self suggestion; whether Vestal is fooled not played. |
| ~00:16–00:26 | **Rianu Keeves** taps an uncertain-code signal; GM spells possible Roman-letter form **E-I-S-T-H** and Evelyn says **funeral dirge**. Direct source audio needed for pronunciation and name. **Koh makes genuine psychic contact with unconscious wife**, hears her say she stays to protect the town, experiences **drone and moving dunes**, then waking-world **black sand physically falls from her clenched hands** into vial. Wife name sounds **Anthela** in Parakeet, **Anthea** in Qwen; **do not fix spelling** or infer proven realm/identity of captors. |
| ~00:28–00:40 | **Peaceful guild diplomacy**, not sanctioned slaughter; each team's gift matches named group (kuo-toa = stinking fish/pearls), borrowed horses and optional **stirge-repelling cones**. Claimed repellent effect not absolute; Koh kills feeding stirge later. Purchases **physically retrieved from Gruber's shop** in travel montage, contrasting S1E09's pending delivery. |
| ~00:46–01:19 | Kuo-toa population/village initially startles then worships Koh when telepathy is mistaken for divine speech; his disclaimer does not immediately stop worship. **Glepo Ma** sounds/spellings provisional; trader barters for shovel and gives Koh **small fishing pole** to care for their horses. He **requests a staff from the underwater ruins** and mentions an unclear enemy/phrase; no quest completion proven. |
| ~01:39–01:57 | **+1 armor and weapons left ashore** deliberately, not lost; **all three water-breathing potions are consumed**. Aquatic mimic (slow-swimming treasure chest) is spotted by Koh and avoided alive; no kill. Fresh one-hour underwater telepathy connection used. |
| ~02:00–02:12 | Identical-layout flooded ruin holds **hidden Ring of Protection**, recognized through psychic activation and **worn by Krandal** with **+1 AC/saves**. Six spear shafts remain in chamber; **not looted** by episode cutoff. Earlier horn remains with guild. |
| ~02:20–02:55 | Ritualist beside familiar glyph/dark ooze creates **vortex**; Koh takes two 8-point bludgeoning injuries, escapes using anchored sash; Krandal Command (“grovel”) **does not end concentration**, Evelyn rides vortex and lands nonlethal punch. Enemy lives, casts **Tongues** to beg; group binds him and confiscates staff and wand. No defeated corpse or spell-staff identification. |
| ~02:55–03:05 | Fish ritualist claims carving means **“the Dunes”** where **“the god” sleeps**. Relationship to Enzo's Dawnless Dunes and Koh's vision remains **possible thematic parallel, not verified identity/cosmology**. Staff is **self-made**, not ancient Elven. Group opts to escort captive to trader rather than kill him; **still underwater at cutoff**, with not-yet-expired but finite Water Breathing time and deep route to surface. |

## Targeted follow-up listening

Verify MP3/SRT offset and original audio at ~00:16 Elven code spelling, ~00:20–00:25 wife's name/vision and physical sand, ~00:34 guild peace mandate, ~01:11–01:28 trader and staff/“big blubs”, ~01:42 gear left on shore, ~02:06 ring and actual wearer, ~02:20–02:55 vortex/nonlethal combat, ~03:00–03:04 Dunes and transport cutoff. Confirm written maps/guild guide without treating later data as introduction knowledge. **No original media or transcription files altered.**

[Episode dossier](../delvers/episodes/S1E10.md) · [Review queue](../delvers/REVIEW_QUEUE.md).
