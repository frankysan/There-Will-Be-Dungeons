# Delvers S1E04 — ASR comparison (2026-10-24)

**Identity correction (2026-10-24):** Former `DELVERS_S1E03_ASR_COMPARISON_2026-10-24.md` report reassigned to **S1E04**. Both SRT inputs in the table retain **mislabeled `S1E03` source filenames** and capture S1E04; this report's **7.65% metric compares those two specific mislabeled exports**, not the correctly named S1E04 Parakeet/Qwen pair, which has not had an exact whole-record comparison here. The canonical S1E04 copies prepend ads. Authentic S1E03 sources are still missing; see [identity notice](DELVERS_S1E03_SOURCE_IDENTITY_2026-10-24.md).

**Scope:** two complete subtitle exports for **Delvers S1E04 — Where did this dungeon come from?**, read from private GitHub commit `d475a95ea7d4a69b79bfbd2fb93b643e2464ab20`, matching initially clean connected `main` working-tree HEAD. Primary Parakeet read chronologically through 02:46 outro; Qwen processed completely for metrics and cross-read in targeted high-stakes intervals. Neither export was checked against original audio. See [source-first dossier](../delvers/episodes/S1E04.md).

| Export | Exact SRT | Git blob | Cues | Last end | Normalized tokens |
| --- | --- | --- | ---: | --- | ---: |
| Parakeet processed (reference) | [source](../sources/Delvers%20S1E03.%20Raw%20End%20Of%20Joke%20Stick.parakeet.processed.srt) | `0a56deaad51f03734dabb441e31d47a843c8f8a9` | **2,381** | **02:46:02.390** | **21,105** |
| Qwen Q8/Canary CTC/Nemotron-labelled | [source](../sources/Delvers%20S1E03.%20Raw%20End%20Of%20Joke%20Stick.qwen-q8.canary-ctc.nemotron.srt) | `ca6611fd7992660be490876926f4292f9a80298e` | **3,852** | **02:46:02.120** | **21,098** |

## Exact ordered word comparison

**1,615 ordered unit-cost word edits / 21,105 Parakeet reference tokens = 7.65% text disagreement** (Qwen has seven fewer tokens). All SRT cues were parsed, indices/timecode lines ignored, `(speaker N)` labels removed, cue speech concatenated, lowercased, straight/curly apostrophes deleted to join contracted words, non-Unicode-letter/digit characters replaced with spaces, then split into word tokens. Computation uses Levenshtein substitutions/insertions/deletions, each with cost one, inside a **3,799-token diagonal band** (18% of longer sequence, rounded up). The optimal score **1,615 is below the band**, establishing that the optimum cannot leave it; hence the measured full-export distance is exact. This is **not** a transcript word-error rate, a listening test, accuracy, verified omission count or confirmation of either source's superior correctness. Model names and settings are inferred from filenames, not original run logs. `tools/prepare_episode.py` was **not executed**; no time-aware alignments or ASR reruns were claimed.

## Editorially important comparison windows

| SRT clock | Matched evidence and open distinction |
| --- | --- |
| ~00:00–00:06 | Both exports introduce the show as **Sunday January 31, 2021** and recap the party **already within a grick scouting job**. The recap is a **different preceding fictional scene** from S1E02's actual crypt-quest ending: do not silently manufacture a transition |
| ~00:17–00:50 | Both show a grick tearing Krandal's **vestments**, scattering candles/rations and confusing itself; Krandal later repairs the bag. Both support **two candles, four rations, vestments and tinderbox** lost, but final custody of every smaller tool is not exhaustively stated |
| ~00:40–01:03 | Both confirm Koh kills a climbing grick and then another **that knocks Krandal unconscious and drags him**; one failed death save, five-point Lay on Hands revival, ordinary rope detached from sash, and sash kept by Koh. Grick below remains alive until later |
| ~01:09–01:21 | Both identify **Veggie Sticks**, who falsely claimed to know every happening in his wood and prioritizes hippogriffs. Plant called `Bush` informally; later Qwen at ~01:20:38 says `Brador`, while primary resembles `Brad`. The plant is **left among his other walking shrubs**, not carried back to town |
| ~01:22–01:38 | Both support the short rest and **Koh using both hit dice**, the party deciding to return to try the remaining grick, and Veggie Sticks's limited first-room observations. Potential dungeon builders, hidden contents and number of gricks remain unknown |
| ~01:47–01:59 | Both show **Koh explicitly re-activating Daylight on the drift globe**, discovery of the **wax-encrusted grick** and Krandal killing it with a mace. **Four party kills** at return include one only in the opening recap |
| ~02:03–02:18 | Both confirm trap-pierced grick remains, wall button, floor needles, Koh's failed shield-sled and **11 HP damage (5 piercing + 6 poison)**; Evelyn spends Lay on Hands **to neutralize poison, not heal HP** |
| ~02:19–02:29 | Both support Evelyn traversing controls and pits and snatching a **rune-marked bladeless sword hilt** from an old stone chest. The chest does not yield a confirmed Sun Blade, despite a closing out-of-game suggestion |
| ~02:30–02:39 | Both show a successful dusk escape with centaur **Aegis**, handover of trophy and **hilt to Cassius for later inspection**, four slain gricks versus trap-killed carcasses, conditional dungeon claim and promotion **request to `Selinar/Selenar`** only |
| ~02:39–end | Both support **three jobs/three days weekly wood-rank limit**, **180 gold total/60 each**, promised level-three processing and unplayed four-day downtime. Koh says he will spend time with **his daughter/family** and maintain an aristocratic identity; Evelyn publicizes the party with a local bard borrowing her sing-song line |

## Evidence integrity and next tests

- Do **not** conflate names/campaigns with The Wastes or Inverse. The guild's reported symbols and audience Sun Blade speculation do not identify the object.
- **Primary read completely; secondary tokenized completely but editorially spot-checked only**. Numbers and timestamps are transcript-relative. An MP3 is inventoried under each filename, but neither was accessible for verification; their identities remain unknown; original input hashes/model run settings unknown.
- High-value listening targets: ~00:01–00:07 recap/previous-episode bridge; ~00:55–01:02 death-save and salvage; ~01:20:38 shrub name; ~02:15–02:24 poisoned versus cured; ~02:29–02:39 hilt/reward/custody; ~02:43 daughter, aristocratic persona and proposed downtime.
- Source bytes were not modified; no invented sound-verification or global Markdown test result. Carry bounded uncertainties forward in [Delvers queue](../delvers/REVIEW_QUEUE.md). **Next research priority is the genuine missing Delvers S1E03**, not a Wastes episode.
