# E105 — complete Parakeet/Qwen ASR comparison (2026-10-23)

> **The Wastes · corrected S1E105 — The Fright Elevator · played session.** [Source-first episode dossier](../episodes/E105.md). This is a **full-export text comparison**, not listening verification, WER, a certified transcript, or a new ASR run. Both existing SRTs were decoded and parsed to their final cues, including the outro; selected spans were compared scene by scene. No source was edited.

## Input inventory and identity

At start the current **InfinityDB OAuth Probe** checkout reported repository **There Will Be Dungeons Transcripts**, clean **main**, HEAD **`a8abb2bfac17a7b24303faebe42d6a8d1afe369c`**. The MCP's binary reader supplied entire source bytes in sequential bounded 65,536-byte chunks; its normal text reader refused the large SRTs. No separate direct filesystem checkout, recording playback or audio-byte provenance was available in this session. The owner-preserved local catalogue maps public **TWBD 107** / **25 May 2020** to corrected **E105**; catalogue metadata is not an independently checked platform posting.

| Export / filename-inferred pipeline label | Source | SRT cues | First start | Final end | Normalized words |
| --- | --- | ---: | --- | --- | ---: |
| Processed Parakeet — **primary** | [The Wastes S1E105. The Fright Elevator.parakeet.processed.srt](../sources/The%20Wastes%20S1E105.%20The%20Fright%20Elevator.parakeet.processed.srt) | 2,900 | 00:00:10.640 | **02:52:14.240** | **25,467** |
| Qwen Q8 / Canary CTC / Nemotron-labelled — **second recognizer** | [The Wastes S1E105. The Fright Elevator.qwen-q8.canary-ctc.nemotron.srt](../sources/The%20Wastes%20S1E105.%20The%20Fright%20Elevator.qwen-q8.canary-ctc.nemotron.srt) | 4,976 | 00:00:03.360 | **02:52:14.300** | **26,042** |

- **SHA-256 from workspace binary reader:** Parakeet `8c898ff479073ec29d23bc766a25b9bffe04968d9610697b35f2342639dcc11b`; Qwen `8e8e470b365789a832e64fc6e3af59f3dc61b6877c121e153f80680e0ad203d8`.
- The label **Qwen Q8 + Canary CTC + Nemotron** is **inferred from basename**, not a verified build, VAD, diarizer, model release, precision configuration or hardware log. Both are independent recognition-labelled outputs, but independently verified ASR jobs/audio association are unavailable.
- No audio was heard. The source-to-audio hash, recording duration/MP3 tags, performance and word-boundary precision were **not measured**. Cue timestamps are not per-word alignment.

## Exact text-only measurement

Each SRT was parsed in cue order; index and time rows were removed; optional `(speaker N)` tags stripped; cue text joined. Lowercase Unicode text, **remove straight and curly apostrophes without a separating space**, substitute whitespace for every other non-letter/non-digit codepoint, then split on whitespace. This matches the project's established comparison normalization. A pure-JavaScript arbitrary-width **bit-vector Levenshtein** computed the **exact ordered unit-cost word edit distance** across both whole sequences; it was checked against rolling-row dynamic programming on **500 deterministically seeded random short pairs** with no disagreements.

**Parakeet → Qwen: 2,536 edits / 25,467 Parakeet words = 9.96% text disagreement.** Qwen has **575 more normalized words**. Neither number is the count of missing audio words or proof of a recognizer's accuracy. The metric ignores speaker identities and timings.

## Disagreement and risk windows

| Recording clock | Text evidence / limitation | Canonical research treatment |
| --- | --- | --- |
| ~00:00–00:10 | Qwen begins **7.28 seconds before Parakeet**; both reach the portal aftermath and the arrival scene. | Opening difference is a review candidate; do not call it a confirmed Parakeet omission without audio. |
| ~00:12–00:16 | The wet official's expected admiral is rendered with **Walls/Wals** variants; **Hidden Stinker** ship label is phonetic. | Harbor officer expected original leased ship but a small surviving craft returns; admiral's reported death is **not an observed body**. |
| ~00:16–00:25; ~02:19–02:42 | Rickshaw name appears as **Fambo/Famo/Bambo Joe**; the player and GM joke about a **Friday** missed engagement. | Single identifiable driver, not multiple people; his injury, stabilization, recovery and reconciliation have distinct played phases. Confirm orthography. |
| ~00:25–00:35 | Both recognize the **100,000-gold insurance/captaincy issue**, with looser monetary-unit wording. | Harbor official **claims** inherited uninsured debt; neither collection nor a universal maritime law is proven. |
| ~00:40–00:53 | Names of helpful lizardfolk driver vary **Bungor/Bungo/Bunger**; affection for Squirts follows **Charm** action and friendly roleplay. | Keep name provisional and respect actual charm limits; no permanent contract, adoption or NPC allegiance established. |
| ~01:16–01:32 | Hamster note's threatening sender is not independently named. *Banishment*, shrinking and spell-concealment are extensively discussed; the hatch hits concrete. | **Discussed spells are not cast**. Threat and elevator sabotage are observed; **who arranged it** remains open. |
| ~01:31–01:52 | Bandana-wearing assailant's commands, ogres and multiple dagger attacks emerge amid crowded overlapping speaker turns; orcs, two rickshaw women and guide are different participants. | Armed trap and casualties real; **do not assign all deaths to hostile thugs**, merge defenders with enemies or assert an unseen employer. |
| ~01:55–02:14 | Squirts's **70-point Heal** is described as a **spell resembling trash**, not a physical scroll; Nash's *Fireball* invokes *Careful Spell*. Both depict elderly gnome destroyed in blast. | Spell actually cast; damage and civilian/attendant casualty are distinct from contemplated Banishment and from casualties caused by attackers. |
| ~02:18–02:34 | Both depict **Spare the Dying**, **Mass Healing Word** and renewed activity by the previously wounded Fambo. Ogre fates occur after further melee/paralysis. | Fambo **survives**; don't confuse stabilization with a conventional resurrection or with the victim's earlier apparent death. |
| ~02:34–02:43 | Broken elevator floor, **Feather Fall**, flight and Vorel-assisted escape through lower door. | Named party and rickshaw helpers emerge alive, but elevator is destroyed and not every passenger is individually counted. |
| ~02:45–02:52 | Return to **Hive** and quiet frontage, downstairs music and **blue dragon Tobacho** at bar. Final short spoken phrase is garbled, Qwen ends with stray **“Walnut”** after network sign-off while Parakeet's end differs. | **Actual arrival and dragon sighting**, not performed Fist exchange or Earth return; ending and last cue require listening. |

## Review plan and boundaries

Prioritize audio checks for **Fambo/Bungor/Walls spelling**, the **100,000-gold term**, the **unknown threat's author**, assassin target, the gnome's death, all named allies' final rescue, final Tobacho speech and Qwen's stray closing **“Walnut.”** Compare original audio against **both** ASR versions, with separate speaker attribution checks and controls before editing canonical speech. No recording was listened to and no ASR SRTs, MP3s, archived sources, or local catalogue were modified.

The [episode dossier](../episodes/E105.md) gives the **E105 cutoff**; the [review queue](../project/REVIEW_QUEUE.md) tracks audio tasks. The next verified, **unread** episode is corrected [E106](../sources/The%20Wastes%20S1E106.%20I%20Took%20An%20Arrow%20Thru%20The%20Brain.parakeet.processed.srt).
