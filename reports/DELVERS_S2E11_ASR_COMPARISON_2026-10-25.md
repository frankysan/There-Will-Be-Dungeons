# Delvers S2E11 — New High Score: exact complete-export ASR comparison (2026-10-25)

**Source-identity follow-up, 2026-10-27:** The [S2E12–S2E08 batch check](DELVERS_S2E12_S2E08_SOURCE_IDENTITY_2026-10-27.md#s2e11) verifies both complete local exports against their recorded Git blobs after CRLF-to-LF conversion only, and verifies both source paths in the recorded source commit. Raw bytes differ in line endings. This independently confirms local content correspondence with the originally pinned source revision. Earlier provenance statements remain dated history. Prior interpretive coverage, inter-ASR measurements, played cutoff and audio status are unchanged.

**Played episode:** [Delvers S2E11](../delvers/episodes/S2E11.md), last session before advertised [S2E12 finale](../delvers/SOURCE_INVENTORY.md). **A direct continuation of S2E10**, with Koh's wife awake; gala only upcoming. [Delvers queue](../delvers/REVIEW_QUEUE.md).

**Source revision:** Workspace MCP `main` HEAD `ce23faa581b0584917ac5256be1c634e5d28ba7b`, three unrelated uncommitted Stanley-illustration doc edits at start. **Both exact source exports fetched from GitHub at the same verified commit** and local MCP initial cues match. Recording/publishing date, matching audio file content, model flags and run metadata not checked.

| Filename-derived export | File | Pinned Git blob SHA | Cues | Unicode normalized tokens | SRT last end |
| --- | --- | --- | ---: | ---: | --- |
| Parakeet processed | [P](../sources/Delvers%20S2E11.%20New%20High%20Score.parakeet.processed.srt) | `bcf95e175155955297dfeca97298b6a0c48a150f` | **2,289** | **20,850** | **02:32:16.420** |
| Qwen Q8 / Canary CTC / Nemotron-labelled | [Q](../sources/Delvers%20S2E11.%20New%20High%20Score.qwen-q8.canary-ctc.nemotron.srt) | `856968710298341a9a6510ae87ddfd8222c32d3c` | **3,844** | **20,946** | **02:32:16.110** |

**Exact complete-export unit-cost Levenshtein word distance: 1,765 / 20,850 = 8.47% textual disagreement.** **NOT WER, accuracy or audio-confirmed omission/hallucination rate**; Q has **96 more** normalized words, ends **0.310 seconds earlier**.

**Method:** Parse complete SRT files; discard cue indices and timestamps plus `(speaker N)` tags, concatenate cues in order, lowercase, remove straight/curly apostrophes (join contractions) and tokenize Unicode letters/digits, punctuation otherwise separator. Identical prefix **51** and suffix **2** tokens removed for speed; two-row dynamic programming **±1,800-token-index band**, optimal edit score **1,765 <1,800** certifies global shortest edit route remains in band and is therefore globally exact. **Every primary Parakeet 10-minute recording-clock block** interpreted through complete ending 02:32:16.420 (0–10 through 140–150, then 150–152); entire Qwen exported source parsed, **selected independent Qwen text checked around 0–8, 13–22, 27–39, 42–56, 58–72, 73–80, 86–101, 106–119, 125–137, 139–150 min**, some excerpts bounded; **not full alternate interpretive read**. **No original audio listened, GM illustration or board handout inspected**.

| Approx. timestamp | ASR-sensitive evidence / required future listening |
| --- | --- |
| **0–8** | GM's “shade / projection / manifestation” clarifies S2E10 battle **did NOT conclusively kill true Khalazar**. Evelyn produces **red shard in S2E11** despite S2E10 giving Carrie a shard; compare actual handoffs—**unresolved continuity**. “Cure disease” is Evelyn's mistaken recap of actual **Remove Curse**. |
| **~19–32** | Kuo-toa **Gleepo Ma** (phonetic) asks job after banishment; Chad/Brad skull-name mismatch; farm implements **present**, trial employment actually performed, eats vermin. |
| **~35–45** | Koh **confesses guild and Chuck work** to now-awake wife; her **Chuck at home** claim needs exact time/attribution. Psychic Whispers accompanies her to sleep without mindscape. |
| **~47–56** | Pink ribbon **8 ft→50 ft**, magical glow/6-inch pieces and directional affinity; mirrored idealized **possible deity**, no canonical speaker identity or proven future traveler appearance. |
| **~65–80** | **Silver already approved**, placements forthcoming; **Maynard reports FIVE elf patients all awake**, Rianu first morning of Anthela's cure; Maynard testimony, **not direct examination**. |
| **~85–105** | Examiner titles **Numalari, Giga Shark, Zoltar, Warden, Min Maximus, Hoffle** phonetics. Krandal **B/S/C**, alias **Splenderbelt the Efficient**. |
| **~105–120** | Evelyn **S/S/A**, **Grinkeeper the Defender**, Gallant Traveler story, healing slap from earlier Bronze Ball two years ago; expected encounter this Ball **not yet shown**. |
| **~120–139** | Koh **S/A/A**, **One Shot**. Min Maximus says his divination grouped characters; ambiguous “situation two”. Rankings not ordinal. |
| **~140–152** | Actually posed Bellows Box portrait at guild beside recovered red-dragon skull, which is **auction staging / not sold**. No Bronze Ball itself before episode cutoff. |

**Outstanding:** source audio/cross-source handoff of red crystal, Rianu/Maynard awakening attribution, glowing ribbon apparition/divine messenger identity, examiner and kuo-toa names. All original sources unmodified.
