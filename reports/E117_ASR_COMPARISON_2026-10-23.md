# E117 — complete Parakeet/Qwen ASR comparison (2026-10-23)

> **The Wastes corrected S1E117 — The Fireside Stories · played Arc Five reunion and Harbor naming.** [Dossier](../episodes/E117.md) · [Arc Five](../narrative/ARC_FIVE.md). **Both complete existing ASR exports were read through ending credits**, not independent source audio. No ASR model reruns, editing of input SRTs or recording replay.

## Sources, reproducibility and measured disagreement

Connected repository **There Will Be Dungeons Transcripts** began clean on `main`, HEAD `d3648c6c4c6a38f72f46d3b90fbcfed48ac3e589`. Both full source texts were fetched read-only via connected GitHub pinned to that exact commit; independently inventoried workspace files report **Parakeet 224,840 bytes, SHA-256 `45560643510e01f7a9ab46a5d2be00f985c4d494ccc110ba78dc8be04446cf63`**, **Qwen 300,860 bytes, SHA-256 `e3a29e547812006393bd4a55c77e7f0e470c80dbf141737c41dccbf99c969579`**. Git blob SHA below is **not** SHA-256; retrieved characters are **not** raw bytes. Model/pipeline naming is inferred **only from filenames**, not verified executable, settings, quantization, GPU or audio version.

| Existing SRT | Characters | Parsed cues | First start | Last end | Normalized tokens | Git blob SHA |
| --- | ---: | ---: | --- | --- | ---: | --- |
| [The Wastes S1E117. The Fireside Stories.parakeet.processed.srt](../sources/The%20Wastes%20S1E117.%20The%20Fireside%20Stories.parakeet.processed.srt) · processed Parakeet | 213,887 | 2,288 | 00:00:07.840 | 02:48:20.020 | 20,832 | `f3efb8378158ca67d527725e48bb3c822122dda6` |
| [The Wastes S1E117. The Fireside Stories.qwen-q8.canary-ctc.nemotron.srt](../sources/The%20Wastes%20S1E117.%20The%20Fireside%20Stories.qwen-q8.canary-ctc.nemotron.srt) · Qwen Q8/Canary CTC/Nemotron-labelled | 285,993 | 3,702 | 00:00:01.120 | 02:48:19.810 | 21,011 | `d25fcb8e8b74460e8eb032081853425035e71a08` |

**Normalization / exact metric:** Extract every SRT cue body in sequence, strip cue indices/timecodes and optional `(speaker N)` labels, join speech as text. Lowercase, delete straight/curly apostrophes without replacing with spaces (join contractions), replace characters other than Unicode letters and digits with space, split into normalized word tokens. Compute **exact unit-cost ordered word-level Levenshtein distance** across *whole* sequences, using arbitrary-width bit-vector implementation and **Parakeet as denominator**.

**Result: 1,597 word edits / 20,832 Parakeet words = 7.6660906298% ≈ 7.67% ordered inter-ASR text disagreement.** Qwen has **179 more words**, not a verified Parakeet omission count. This is **not WER, true accuracy, proof of hallucination or diarization reliability**; no word has been directly checked against audio. Qwen's first cue begins 6.72 seconds before Parakeet's, final cue ends 0.21 seconds earlier; these edges do not establish audio correctness.

## Key listening windows / ambiguity map

| Recording-clock window | Observed text / uncertain wording | Source-first safeguard |
| --- | --- | --- |
| ~00:04–00:17 | Nash and Hope reappear after E116 **true Elhandar return**; snake on Nash's cloak, Nash explains the station and children, gives confused “two days” claim countered by **four E115 days** | No false unified time interval, no second visit to Hell, no new birth |
| ~00:12–00:31 | Nash retrieves **Vorel, Stanley, Bok Bok and Chunks** from hunt; **Stanley asks for station shield precautions** and approaches armed | Shield request **not confirmed actual activation**; no demon fleet materializes |
| ~00:31–00:49 | Hope ugly-cries; Stanley questions Hand, demon responsibility, trust, Squirts's death; **returns disguise ring using rapier**; Nash and Vorel mediate | Causation and blame voiced by characters, **not automatically GM-confirmed orders by Hope**; no reconciliation yet |
| ~00:55–01:09 | **Bok Bok now offers to remain with family**, wishes Vorel to take **Chunks** as apprentice; **alternate Tedna/Badass T** conflated with original late Tedna in casual speech | Distinguish E115 caretaking versus E117 travel plan; no adoption, marriage or death reversal |
| ~01:08–01:21 | **Nobieri** and **Emenil/Emmanil (?)** present in refugee clearing, ~8 houses, 12–24 survivors, Hope acknowledges actions; **Gretchel/Gretchil (?)** supporter versus departing dissenter with wife/son | Some remain and one family physically leaves; no precise surviving census or voluntary consensus of all historical Tietkalla |
| ~01:20–01:31 | Ash rite: Stanley **refuses**, Nash/Vorel/Hope **participate**, left real Hand receives ash; **flaming 10-foot Abegir/Abigrier (?) apparition** | Apparition is played. Its **self-declared divine identity and afterlife promises** remain uncorroborated beyond ritual |
| ~01:31–01:40 | Abegir gives Hope leadership/forgiveness counsel, tells Nash little about other Nashes | This is **manifestation's testimony**, no demonstrated planet restoration, no absolution contract |
| ~01:43–01:52 | Tiefling ranger's **Zalna/Salma (?)** spouse killed beneath collapsed building, distant demon-view claims; **Emenil** calls for water | Survivor firsthand **testimony**, not new playable scenes or observed water miracle |
| ~01:50–02:07 | Stanley birth **Valier/Vale Ornath (?)**, father **Daliot/Dalit (?)**, human mother **Cristopher/Kristopher (?)** ASR uncertain, faith crisis; Nash describes **Solar Mines enslavement/uprising**, unknown early fire powers | Keep disclosure **attributed**; Scott says foreman name **“Pedro” was just invented out of game**, **NOT a settled canon name** |
| ~02:07–02:11 | Vorel long self-title recital, ending **“Keeper of Stories”**; exact wording/variants already mapped in [title register](../world/characters/vorel-titles.md#source-indexed-titles-epithets-and-disputed-labels) | Repeat old epithets not granted as new offices; **no Nash improvised casting phrase** in E117; fire in backstory is retrospective |
| ~02:11–02:17 | **Hope chooses “the Harbor,” its residents “Harborers,” and help for those lost in the universe**; Nobieri announces as local founding declaration | **Name established here**, not just future proposal, but **no operating multi-world Harbor has been built** |
| ~02:19–02:36 | Emenil **explicitly confesses love for Stanley** in private, Stanley rejects beginning relationship for now, leaves; Perception 29 tells him **she smashed her Malhaya shrine and bowls** | Separation is actual; broken altar based on GM's sound/perception adjudication, not witnessed in same room. No reciprocal romance |
| ~02:38–02:47 | Vorel smells **lizardfolk**, briefly follows north, cannot reliably track; plans **after-supper night outing** | **No lizardfolk encounter**, Omnom remains only previously reported alive; proposed search not enacted |
| ~02:47–02:48 | After-show and upcoming bonus discussion | Production notes **not fictional chronology** |

**Priority audio checks:** divine name and exact appearance/voice (~01:27–01:40), founder name **the Harbor** (~02:11–02:16), complete Vorel epithets (~02:07–02:09), **Emenil's private confession and smashed shrine** (~02:19–02:37), Nash's **Pedro** meta-interruption (~02:01–02:06), Bok Bok travel/caretaker plans, the survivor's bereavement name and Stanley's parent names. **No listening performed**.

**Next verified:** [E118 — The Key, Parakeet](../sources/The%20Wastes%20S1E118.%20The%20Key.parakeet.processed.srt) · [Qwen](../sources/The%20Wastes%20S1E118.%20The%20Key.qwen-q8.canary-ctc.nemotron.srt), owner crosswalk **TWBD 120, September 14, 2020**, two exact nonempty SHA-256-identified SRT files in workspace. **Not yet analyzed**.
