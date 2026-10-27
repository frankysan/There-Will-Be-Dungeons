# Delvers S1E05 — Maximum Montage ASR comparison (2026-10-24)

**Source-identity follow-up, 2026-10-27:** The [S1E07–S1E03 batch check](DELVERS_S1E07_S1E03_SOURCE_IDENTITY_2026-10-27.md#s1e05) verifies all comparison inputs listed in the historical report against their recorded Git blobs after CRLF-to-LF conversion only, and verifies their exact historical source paths in the recorded source commit. Raw bytes differ in line endings. This independently confirms local content correspondence with the originally pinned source revision. Earlier provenance statements remain dated history. Prior interpretive coverage, inter-ASR measurements, played cutoff and audio status are unchanged.

**Recording identity:** Played session **Delvers S1E05 — Maximum Montage**, nominally published **2021-02-08** in the podcast episode spreadsheet. It opens with a stylized exaggerated retelling of the grick mission, then plays out an extended sequence of downtime, assignments, promotion and shopping. Do **not** interpret the introductory retrospective as another played interrogation. This session follows corrected [S1E03](../delvers/episodes/S1E03.md) and [S1E04](../delvers/episodes/S1E04.md) in Delvers continuity.

| Export | Input under `sources/` | Git blob | Cues | Last cue end | Normalized tokens |
| --- | --- | --- | ---: | --- | ---: |
| P / processed Parakeet | [`Delvers S1E05. Maximum Montage.parakeet.processed.srt`](../sources/Delvers%20S1E05.%20Maximum%20Montage.parakeet.processed.srt) | `6e3ecaebc689ab19e465b48082745fe56d720050` | **2,395** | **02:34:40.670** | **21,070** |
| Q / Qwen Q8 Canary CTC Nemotron-labelled | [`Delvers S1E05. Maximum Montage.qwen-q8.canary-ctc.nemotron.srt`](../sources/Delvers%20S1E05.%20Maximum%20Montage.qwen-q8.canary-ctc.nemotron.srt) | `3ea4d625cde319a7aeec76abc404cd3b69b74281` | **3,869** | **02:34:40.340** | **21,099** |

**Exact full-export ordered distance:** **1,244 token edits / 21,070 P-reference tokens = 5.90% inter-ASR textual disagreement** (secondary has 29 more normalized tokens). Both files fetched from private GitHub at commit `a2fc719e9ea1997b7b5b679c0a9fec3a4c2f4864`, matching the initial clean connected workspace `main` HEAD. File names describe the pipelines but not verified inference settings. No original MP3 opened/heard, no audio timestamps aligned, no transcription job rerun and no `tools/prepare_episode.py` execution.

## Exact calculation method

The entire text of each SRT was split by subtitle cue blocks; cue indices and timecode lines were excluded. All text following each timecode was joined in cue order, `(speaker N)` decorations removed, converted to lowercase, straight and curly apostrophes deleted to join contractions, and all other runs of non-Unicode-letter/digit characters replaced with spaces. This produced chronological word sequences. Exact unit-cost Levenshtein dynamic programming was evaluated with a **3,500-token diagonal band**, using a rolling pair of rows. The optimum found (**1,244**) is **strictly less than the band**; no path crossing that diagonal boundary can have a lower cost, so the resulting score equals the unrestricted optimum. No score has been interpreted as WER, correct-word rate, audio-verified omission/hallucination or proof one ASR is better.

**Coverage:** Primary Parakeet transcript read chronologically from its 00:00:09 opening through the 02:34:40 outro in bounded timestamp windows. Both complete Qwen and Parakeet sequences were measured; Qwen passages specifically cross-read around the item identification, magical armor, promotion denial, hag encounter, character expenses, enchantment change and ending. **Qwen was not independently close-read for every word**. No diarization validation against the performers' voices.

## High-value parallel text checks

| SRT-clock range | What is supported, what remains open |
| --- | --- |
| ~00:00–00:06 | Framing interview is fictionalized recap. Krandal notices neglected **Yuri**, aids him and **passes him to Jimmy**; recovery after care remains unverified. Need audio for whether a specific promise was made |
| ~00:12–00:20 | **Lady Vestal** confronts Evelyn at finishing school after a classmate covers for her. Koh returns to his wife and pays caretaker/doctor; after subsequent long rest all PCs are **level three** |
| ~00:22–00:34 | **Carrie Underworld** presents **Soul Knife** ancient-Elvish hilt; alternative translated `mind sword / psi blade`. Koh conjures **cyan psychic blade** and incurs one point psychic damage from touching it; the tabletop stab leaves **no mark**. The **Masked Mage** calls him a scion, warns of others acquiring psychic relics. Identification is a performed scene, not pure speculation |
| ~00:35–00:43 | Buck Broscale is a **living red dragonborn, silver-ranked**. Krandal's **Cure Wounds** restores 10 HP but does **not** cure poison; **Lesser Restoration** then cures it. Avoid merging with S1E01 dead dragonborn/badge 542 on name similarity |
| ~00:45–00:50 | Qwen and P agree a school friend enchantment lets Evelyn **don chain mail as an action**. **Selenar/Celenar Everbloom** denies the first promotion based on poisoned/weakened gricks, directs community service; identity/spelling needs written/audio corroboration |
| ~00:54–01:18 | Silver-rank **Willamet/Wilibet Molly** is the hag hunter, not a member of the wood-rank party. Koh detects suspect tart vendor, Evelyn distracts/corrals shoppers, Krandal uses **Thaumaturgy**, and **Molly kills the hag** and takes horn/heartstone. Do not credit the party with the killing blow or horn |
| ~01:18–01:29 | Fire-resistant cloaks **issued for one fire assignment**, not permanent ownership. A hellhound causes the fire; Krandal rains water, Koh evacuates, Evelyn breaks openings. Later a real darkmantle in tannery, animated laundry and cranium rat are resolved as montage episodes; do not treat the two prior darkmantle alarms as real monsters |
| ~01:29–01:40 | GM establishes **1,800 gp montage earnings per person**, and **10/105/100 gp** respective living-expense deductions for Krandal/Koh/Evelyn (additional shopping separate). **Second promotion approved**, ceremony tomorrow; **not yet bronze badges in-hand** |
| ~01:40–01:48 | **Skull Keep / Witherskeep** chosen next, flameskull known from guild reports; orientation and Aegis cart scheduled for tomorrow. Actual fight does not start in S1E05 |
| ~01:52–02:20 | Purchases: Evelyn **200 gp pigments + 1,000 gp lightning javelin + 400 gp vicious hammer commission**, Koh **2 basic healing potions/100 gp total**, Evelyn **greater healing/200**, Krandal **fire-resistance potion/300** and **+1 armor/1,000**. Shopkeeper labels/inventory are ASR-provisional |
| ~02:20–02:31 | Koh replaces two daggers and buys 20 arrows; Krandal orders two ornamental face-maces (42 gp combined). **Koh initially pays for a Life Stealing shortsword** but later asks for **Corpse Slayer** with price to be negotiated off-air. Neither sword enchantment is shown completed before the episode cutoff |
| ~02:30–02:34 | **Brother Maynard** disapproves of Krandal's adventuring while other temple clergy admire him; party explicitly settles on **The Darkest Delvers**, despite impending full bronze status. Network outro present in both exports |

## Source integrity and listening handoff

No original transcript, MP3 or source media was changed. The two S1E05 SRT files share a compatible approximate endpoint (within ~0.33 sec), but that alone is **not** proof that they used an identical audio asset, nor that either matches a local MP3 clock. Prior S1E03/S1E04 relabeling errors are not transferred to S1E05. Verify item custody/charging against audio particularly around ~02:08–02:31, `Selenar` spelling around ~00:47 and ~01:37, and temple/student names around ~00:14–00:17 and ~02:31.

[Detailed episode dossier](../delvers/episodes/S1E05.md) · [Delvers review queue](../delvers/REVIEW_QUEUE.md). Next verified candidate archive: **S1E06 — The Tower**; not examined here.
