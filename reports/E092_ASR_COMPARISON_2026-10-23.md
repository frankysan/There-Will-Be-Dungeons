# E092 — He's So Handsome: dual-export ASR comparison (2026-10-23)

> **Text-only machine-transcript comparison**, not original-audio checking. [E092 episode dossier](../episodes/E092.md). Both unchanged source exports refer to the same **~02:44:03** show. **No speech was listened to, decoded again or corrected in the source files.**

## Inventory and reproducible method

| File | Parsed SRT cues | Final cue ends | Normalized tokens |
| --- | ---: | --- | ---: |
| [Parakeet processed](../sources/The%20Wastes%20S1E092.%20He's%20So%20Handsome.parakeet.processed.srt) | 2,546 | 02:44:03.320 | 22,086 |
| [Qwen Q8 + Canary CTC + Nemotron labelled](../sources/The%20Wastes%20S1E092.%20He's%20So%20Handsome.qwen-q8.canary-ctc.nemotron.srt) | 4,306 | 02:44:03.260 | 22,268 |

Read each SRT in cue order, discard numbers/timecodes and `(speaker N)` prefixes, concatenate spoken lines, lowercase, delete apostrophes (joining contracted words), replace non-Unicode-letter/digit characters with spaces, split on whitespace, and calculate **unit-cost ordered word-token Levenshtein**. Reproduced **1,674 operations / 22,086 Parakeet words = 7.58% inter-ASR disagreement**. This is **NOT word error rate against audio**, true omissions or hallucinations, an accuracy ranking, a source-quality score or verified diarization. The filenames do not document full decoding settings, model build identifiers, source audio hashes, segmentation, VAD or alignment options; those remain unavailable.

## Time-aligned disputed spellings and critical outcomes

| Window | Both-transcript understanding, and what remains to verify by ear |
| --- | --- |
| **00:09–00:23** | **Tobacho sealed Hive writ genuinely accepted** by Harmonium; **Nash's Reduce frees three trapped guards**; leader **Sir Lipso Tuxis/Texas (?)** threatens revenge *if* their vows were violated. Do not call actual violence/arrest or failed exit. |
| **00:25–00:35** | **Lohar redeems voucher** for four new cleric costumes, has delivered to coach. No recorded payment. |
| **00:35–01:09** | **Amber Cutlet**: **5sp drinks paid**; separate **1gp tip left behind**; later **three ale casks 15gp + 3gp tip purchased**. Separate **drinking and in-world anxiety** from unplayed future war. |
| **01:09–01:39** | Impersonating **Bishop Stevius Rintley/Ritley (?)** is an actual **changeling**, helps at safehouse; group **long rests** and uses **temporary appearance disguises**: **Nash/Horace Saddlesworth**, **Vorel/Goliath**, **Hope/Candice or Candace**, **Stanley unchanged**. Reported Lady of Pain cosmology is **NPC theory**. |
| **01:40–01:59** | **Unwavering House** physically visited. **Sister Anulak/Annulac (?)** initially refuses unprecedented fifth blessing; **Stanley's “Gaetor” plea convinces her**. Ancient **High Cleric Butar/Buntar Thrun (?)** physically appears; both exports show blessing ceremony. “Gaetor” is a **cover story**, not new verified campaign geography. |
| **02:00–02:09** | **Telekinesis hides inside prayer, real medallion falls and Stanley swaps it for a false one**, which Thrun **actually takes and clasps on**. Hope/Vorel distract from partially exposed real pendant. High cleric keeps **Hope/Candice** for supposed spiritual examination. No successful ritual blessing as a class feature established. |
| **02:14–02:22** | **Stanley casts Modify Memory on sister and describes a false release decision**; she **actually follows it, summons Candice, and all four exit**. The **spoken “success” concerning Wisdom save vs DC17 is internally confusing** relative to a proceeding spell effect. The recorded outcome of Hope's release is solid; **save mechanic needs audio and table-level review**, not an invented outcome. The group later confirms pendant in custody. |
| **02:23–02:30** | Strong *custody reversal*: **8 Dimension Door scrolls, 4 Reverse Gravity scrolls, Nash ring, +2 magic dagger assigned to Hope, two guns Fox and Scully, bullets and adventuring kit are physically in the carriage**. **Smokey's belt missing**. E091 called magic dagger a Nash request, and E089–E091 called second pistol **Mulder**: track these as **explicit cross-source inventory/name inconsistencies**, rather than merging into a third gun. **Nash fills ring with three L1 and one L2 Chromatic Orbs (5 levels total)**; first idea was four or five L1, superseded. |
| **02:30–02:44** | Party **arrives at Dark Below airship hangar** and actually visits/tours ship, sees enormous **departure-side portal**. **Elephant-like captain's improvised “Meart/Miart” name and pronouns unstable on microphone**, original ship name forgotten/deferred. **No launch or Outlands trip yet**. |

## Editorial decisions and risks

- **Advance E091's “planned” key theft to E092's “played and succeeded”**; the **authentic-looking pendant is obtained**, while its capability to open the divine box still lacks field verification.
- **Move equipment states** from *promised* to *physically supplied* for the exact stated items, but don't silently reconstruct bearer-of-every-item inventory; **Scully is reacquired in the coach after it truly left Hope's custody in E090**. Resolve **Fox versus Mulder** with original item documentation or audio.
- **Do not conflate high cleric with bishop**: the real **Stevius remains the captive in Tobacho's compound**; an **impostor changeling** escorts the party in E092. **Sister Annulac is persuaded by an actual played spell effect** to release Hope.
- **Temporary shapeshifts are not in-world species changes** and “Gaetor” is not proved geography. The identity and mechanism of the White Tower's magical box still rest on the E091 bishop's testimony.
- **The airship and crew are now encountered**, but **portal travel, siege, infiltration, fist acquisition, trade with Tobacho and Earth crossing remain future**.
- The **outro/captain naming contains direct production uncertainty**: don't canonize Captain Meart's longer name or assume ship has a stated name.

**Listening priorities:** 02:16–02:18 Modify Memory save/adjudication, 02:24–02:26 **Fox/Scully/Mulder**, 02:25 **+2 dagger recipient**, 02:27–02:29 charged spell mix, ~02:35–02:41 improvised captain and ship name omission. The actual live audio is necessary to verify spell-level and inventory attribution. Next story [E093](../sources/The%20Wastes%20S1E093.%20We're%20on%20a%20boat.parakeet.processed.srt).
