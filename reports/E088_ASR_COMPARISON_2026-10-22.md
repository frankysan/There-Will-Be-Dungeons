# E088 — Shopping Day: dual-ASR comparison and explicit GM correction (2026-10-22)

> **Comparison of two machine-generated texts, NOT audio-verification.** [E088 first-pass dossier](../episodes/E088.md). Original SRT files unchanged; no models rerun, no human-reference words, no verified speaker assignments.

## Sources and text distance

| Filename-labelled source | Cues | Approx. last cue | Normalized word tokens |
| --- | ---: | --- | ---: |
| [Parakeet processed](../sources/The%20Wastes%20S1E088.%20Shopping%20Day.parakeet.processed.srt) | **2,618** | **02:50:31.45** | **23,066** |
| [Qwen Q8 / Canary CTC / Nemotron-labelled](../sources/The%20Wastes%20S1E088.%20Shopping%20Day.qwen-q8.canary-ctc.nemotron.srt) | **4,105** | **02:50:31.22** | **23,127** |

Method: extract SRT cue text; remove `(speaker N)` decorations; lowercase, remove apostrophes/punctuation, preserve Unicode letters/digits, normalize spaces, and perform unit-cost whole-episode **word-token Levenshtein**. **1,362 operations / 23,066 Parakeet words = 5.90% first-export-relative text disagreement**. This is **not a word error rate**, omission/hallucination estimate or evidence the Qwen-labelled output is more accurate. Subtitle-cue count does not show speech coverage. The version strings, inference commands, decoding options, audio checksum, speed, hardware use and independently verified performance of either model are not provided; the speaker roles here were inferred from context and episodic recaps, not machine-certified diarization.

The host identifies the show as **for the weekend of January 19, 2020**, which is **spoken episode metadata**, not independent verification of original release or recording date.

## High-impact interpretation and listening windows

| Time | Grounded episode evidence and unresolved ASR concerns |
| --- | --- |
| **00:02–00:13** | Temple **Chapel of Laughter** and **Hall of Reflections** are entered; priest **Carr/Karr (?)** guides group to Kidigree. Mirrors show alternate forms of the same hooded man and projected alley; retain uncertainty in proper names. |
| **00:13–00:20** | **Mind Master directly appears in Kidigree's mirror with Crimson Moon ninjas**, threatens **Kanja** with **100,000gp demanded within seven days** and **one miniature inhabitant killed per week** thereafter; **Kidigree extracts “tears of a civilization.”** This is shown via the priest's mirror, not direct contact in the alley; no explicit proof he previously ordered the E086 assault. |
| **00:19–00:30** | **Kidigree says he could have betrayed Vorel**, but elects to honor pact; **separate private roleplayed soul choices** for **Jon's Stanley and Kristen's Hope**. Newly formed returnees **emerge from mirrors** while **original inert bodies remain on slabs**. Preserve timing and distinguish original corpses, new organic Hope (mechanics absent but scars retained), old bodies' *proposed* disposal, and player-level identity doubts. |
| **00:31–00:40 — critical** | **Beau declares prior Sigil negation rule a DM mistake and says field does NOT apply within Sigil.** Nash demonstrably **casts Fire Bolt successfully**, without buying a school-specific key. Prior E085 failed casts, E086 vendor and E087 500gp gift were played under superseded adjudication, **not proof a key is required now**. Exact other-plane conditions remain unspecified. **Audio check the exact negation-field wording first**, without inventing a larger universal retcon. |
| **00:43–01:03** | Hope borrows clothes, Stanley uses red cape and Bill's old bowling clothes, **Prestidigitation** works. **Nothing and Squirts no longer active Jon/Kristen PCs**; Squirts stays temple and Nothing mentions **seven-day Pelvis commission** still impending. They are not killed/erased. |
| **01:03–01:40** | Newly restored PC memory of **void without elapsed-time awareness**; **Bill** calls Sigil the **Cage**, suggests **Clerk's Ward records of portal transit/owners** as possible Earth-return lead, reacts strongly to **Kintobal/Kentoval Bray / Weirlords**, while PCs discuss **Beltnotch, purgatory and youth**. Treat as NPC/PC testimony, no proven portal key, travel or cosmology. |
| **01:42–02:05** | Hope wants guns and armor, Stanley equipment; **gun market search unsuccessful** and detailed purchases deferred offline. Vorel's spectrometer goal is to **inspect Weir soul markings**, not an objectively completed identity test. |
| **02:05–02:23** | Two shop quotes: first **consumer 100 / professional 700** order, separate premium **Treverson spectrometer at 1,400gp**; **Vorel sees identical white soul outlines and a glowing Infernal “Stanley Billings” neck mark**. Needs audio/spelling and independent lore review; **no spectrometer purchased**. |
| **02:24–02:41** | Vorel pays **1,250gp total** at wealthy equipment dealer for **1,200gp pro sixteen-fighter BMF cabinet + 50gp skull-shaped focus for Nash**. Shopkeeper name sounds **Lodess/Largess Appleton**, shop sign **Large S / Largess**, brand and personal name need listening. Machine **later arrives and is installed**, not merely ordered. Owner's prejudiced opinions about poor people are hers, not setting law. |
| **02:40–02:49** | Tailor **Lohar/Lorhar** fits three suits for Vorel/Hope/Stanley at **10gp each**, takes **15gp deposit** and **15gp on delivery**, garments arrive during a **short montage**. Nash postpones outfitting until full regrowth. **Eight-day recuperation talked through/planned**, no recorded complete anatomical endpoint. |
| **02:45–02:50** | **Clerk's Ward proposed, not yet visited**; machine installation Bill approves in exchange for possible future earnings, **inn purchase not signed**, no new Earth portal, spell key or gun found. |

## Decisions

1. **Make resurrection unambiguous in all live references** from E088 onward: Hope and Stanley physically return from mirrors with player agency, rather than remaining petitioners in custody. **Original corpses remain with Kidigree**, and Weir/Infernally marked souls appear still marked.
2. **Record the corrected spell ruling with explicit priority:** E088 **overrides** prior DM explanation about general magic suppression within Sigil. Do not erase historically played failed spells, the key seller or Vorel's gift to Nash; just mark them **superseded as present general rules**.
3. Differentiate **Mind Master's newly directly observed Crimson Moon association** (via mirror) from **not-yet-proved employer of E086 attack**; preserve threats to Kanja's miniature population as source-viewed acts.
4. Update money with **actual 1,250gp checkout** and **two 15gp tailor payments**, no spectrometer or inn purchase, and **no unspecified off-air gear**.
5. **Next focused source:** [E089 — It has an umbrella in it](../sources/The%20Wastes%20S1E089.%20It%20has%20an%20umbrella%20in%20it.parakeet.processed.srt), whose filename is confirmed in the repo tree. Verify purported eight-day skip and possible Nash recovery *from that source*, rather than presupposing either here.

[Review queue](../project/REVIEW_QUEUE.md) · [Model-test log](../project/MODEL_TESTS.md).
