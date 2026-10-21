# The Wastes — transcription and campaign-reference pilot

**Status:** The E000/E001 reader-edition pilot remains incomplete and not manually proofread. Processed Parakeet SRTs for subsequent episodes are now included as source material; E002–E033 (including the E013.5 supplemental) have preliminary, unverified **reference dossiers**, not new publishable reader editions.

This package establishes a repeatable, **local-first** path from podcast audio to readable, speaker-labelled text, with a separate campaign reference that cites episode time positions. It covers the *There Will Be Dungeons* campaign described in the supplied files as *The Wastes*.

## Start here

1. [E000 — Introductions: reader-edited draft](transcripts/E000.reader-draft.md) ([machine draft](transcripts/E000.readable-draft.md), [edit log](transcripts/E000.reader-edits.json))
2. [E001 — The Campaign Begins!: reader-edited draft](transcripts/E001.reader-draft.md) ([machine draft](transcripts/E001.readable-draft.md), [edit log](transcripts/E001.reader-edits.json))
3. [Corrected episode numbering / original-label crosswalk](project/EPISODE_NUMBERING.md), [archive-owner's noncanonical episode notes](project/OWNER_EPISODE_NOTES.md), [External sources and chronology policy](project/EXTERNAL_REFERENCES.md), [Project charter](project/PROJECT_CHARTER.md), [workflow](project/WORKFLOW.md), [editorial rules](project/EDITORIAL_GUIDE.md) and [decision log](project/DECISIONS.md), [model test record](project/MODEL_TESTS.md) and [roadmap](project/BACKLOG.md)
4. [World reference index](world/README.md), [characters](world/CHARACTERS.md), [places](world/PLACES.md), [world history](world/WORLD.md), [chronology](world/CHRONOLOGY.md), and [consistency issues](world/CONSISTENCY_LEDGER.md), and [machine-readable entity index](world/entities.json)
5. [Episode dossiers](episodes/E000.md) and [E001](episodes/E001.md)
6. [Review queue](project/REVIEW_QUEUE.md), [automated file audit](reports/SRT_AUDIT.md), and [Qwen Q4/Q8/Canary variant evaluation](reports/QWEN_VARIANTS_2026-10-21.md)
7. **Expanded campaign context:** [E002 — Spiders](episodes/E002.md), [E003 — Soft Head Returns](episodes/E003.md), [E004 — The Oil Demon](episodes/E004.md), [E005 — Goblincide](episodes/E005.md), [E006 — Start your engines!](episodes/E006.md), [E007 — Bok Bok Keeping It Fresh](episodes/E007.md), and [E008 — Stupid Gnomes!](episodes/E008.md), [E009 — Surfacing](episodes/E009.md), [E010 — Shackles](episodes/E010.md), [E011 — Kick me as hard as you can](episodes/E011.md), and [E012 — Work Hours](episodes/E012.md), [E013 — Old One Eye](episodes/E013.md), [E013.5 — Supplemental](episodes/E013.5.md), and [E014 — That's Magic](episodes/E014.md), [E015 — The Darkness](episodes/E015.md), and [E016 — Dragon Mother](episodes/E016.md), [E017 — Fire in the hole!](episodes/E017.md), and [E018 — Into the storm](episodes/E018.md), [E019 — Elevator Action](episodes/E019.md), [E020 — Flaky Mushrooms](episodes/E020.md), and [E021 — The Mushroom Kingdom](episodes/E021.md), [E022 — The Charmed Lizard](episodes/E022.md), [E023 — Demon Hotel](episodes/E023.md), and [E024 — Monogamy Respected](episodes/E024.md), [E025 — Door Authority](episodes/E025.md), [E026 — The Hunt](episodes/E026.md), and [E027 — Lizard Party](episodes/E027.md), [E028 — It's A Cat Person!](episodes/E028.md), [E029 — Stanley's Choice](episodes/E029.md), and [E030 — The Worm Turns](episodes/E030.md), [E031 — Three Men and a P0d](episodes/E031.md), [E032 — The Great Bleaching](episodes/E032.md), and [E033 — Nashfree](episodes/E033.md). These are reference dossiers, **not publishable reader transcripts**, drawn from processed Parakeet SRTs; audio accuracy, names, and speaker assignments still need verification. E008 features guest players/characters, not substitute actors for the absent regular performers. See the [expanded chronology](world/CHRONOLOGY.md), [characters](world/CHARACTERS.md), [places](world/PLACES.md), and [consistency ledger](world/CONSISTENCY_LEDGER.md).

## New segmentation benchmark (2026-10-21)

[Five controlled CrispASR/Parakeet runs on E001's first ten minutes](reports/PARAKEET_SEGMENTATION_2026-10-21.md) cover no VAD, default Silero VAD, 700 ms padding, overlapping 30 s chunks and a chunked deduplication-off test. The two chunked JSON and SRT pairs are **byte-identical**, and transcription disagreements are **not yet audio-verified**. The existing episode drafts were not replaced.

## Important distinctions

- **Multi-pass review tooling:** [usage and limitations](reports/MULTIPASS_PIPELINE.md),
  [measured export pilot](reports/MULTIPASS_PILOT_2026-10-21.md). Compare preserved
  Parakeet/Qwen outputs, inspect time-coded disagreements, generate targeted jobs,
  and retain reviewer decisions without rewriting these reader editions.

  ```powershell
  python -m unittest discover -s tests
  python tools/pilot_asr.py --out local/multipass-pilot
  ```

  Use a new output directory. This command compares E000/E001 exports only; it
  does not launch recognition or process the archive. Model agreement is not
  audio verification.

  A [real 29.640-second E001 third pass](reports/TARGETED_VERIFICATION_2026-10-21.md)
  has also been executed and imported with source-hash verification and unchanged
  historical evidence. Its competing greeting wording remains awaiting listening.

- The **reader-edited drafts** normalize source-supported spelling (e.g. Dusthill, Nash Maggard, Vorel, Jimster and Shun'ti) and the cast speaker name **Jon**, with every edit logged. They are still **not audio-proofread**; ambiguous speech such as “Orifi or Orify?” remains as recognized. The machine-derived drafts and all original SRTs stay unchanged.

- **Readable draft** means subtitle lines have been grouped into paragraphs with named speakers and approximate timestamps. It does **not** mean every word or speaker boundary was checked against audio.
- The text source for these drafts is the supplied **post-processed Parakeet TDT 1.1B SRT**. The original unprocessed Parakeet output and other tested outputs are in [`sources/`](sources/), unchanged in content.
- Episode 1's numeric `speaker 5` is the same person as `speaker 0` (Scott, performing a voice), **verified by the archive owner**. This is a per-episode correction; don't generalize ID assignments to other episodes.
- Cohere's substantial omissions were **verified by listening** and its outputs are preserved for comparison only.
- The final spoken word of E000 is **“Now”**; the remaining audio is music. The processed Parakeet ending has unreliable timing, so the last cue is **not verified** even though the word is.
- The world's details are provisional reference entries. **A character's belief is not automatically objective world fact**, and uncertain spellings are deliberately flagged.

## Rebuild

Python 3.10+ is sufficient; the scripts use only the standard library.

```bash
python tools/build_transcripts.py
python tools/build_reader_editions.py
python -m unittest discover -s tests -p 'test_reader_editions.py'
python tools/audit_sources.py
# Optional: pip install rapidfuzz
python tools/evaluate_qwen_variants.py
```

The first command recreates the immutable machine-derived drafts; the second command recreates the *separate* wiki-spelling reader drafts and correction logs. Files produced by the first command: `transcripts/E000.readable-draft.md`, `transcripts/E001.readable-draft.md`, and `*.turns.json` containing original cue indexes for traceability. The second command creates `reports/SRT_AUDIT.md` and `reports/source_manifest.json`.

The original MP3 files are **not** bundled in the archive, to avoid duplicating the large uploads. The manifest records their SHA-256 digests and file sizes when they were available to build the pilot. Keep them in a separately backed-up, read-only audio collection.

## Production definition of done (per episode)

An episode is *drafted* after automatic transcription and readable rendering, but is *reviewed* only after checking flagged omissions, proper nouns, speaker IDs, beginning/end speech boundaries, broken cue boundaries, and audio-linked uncertain sections. This package is at the **drafted** milestone.

## Additional ASR tests (2026-10-21)

Six further **raw Qwen variants** are preserved under `sources/`. See [comparison](reports/QWEN_VARIANTS_2026-10-21.md) for exact-text results, timing-validity findings and discrepancies worth checking against audio. Neither the existing readable drafts nor the world reference were silently rewritten from these competing model outputs. This repository is the canonical project home; external fan-wiki and end-of-campaign character-sheet references are governed by the [external sources policy](project/EXTERNAL_REFERENCES.md).


## Newly archived visual references (2026-10-21)

The archive owner added **85 WebP images** downloaded from the fan wiki to [`sources/images/`](sources/images/). They are now indexed in the [image provenance and editorial register](project/IMAGE_ASSETS.md). Most are fan art or undated image assets; the two-page **Fate 4 vehicle design** explicitly credits **Kristen Ashton** and can inform E006–E010 vehicle references. The **Beyond the Deadfingers** regional map contains names including Dusthill and Slavetown, but may include **later campaign annotations**. Neither this map nor the **Teet** map is confirmed to be the exact player-facing map discussed in early episodes.

**Important:** Fandom's wiki-text license does **not** automatically license images. Original file-description pages, authors, individual media permissions and upload dates still require verification before public distribution. Visual corroboration never counts as **audio verification** of ASR output. The supplied image binaries and original SRTs have not been changed.

## E013–E014 expansion and unusual E013.5 chronology (2026-10-21)

The [E013 dossier](episodes/E013.md) records the **out-of-character GM background briefing** about Pristine/Slavetown, the **Lactid Cartel's** Sapphire assault and the colossal cyclops cliffhanger. The [E014 dossier](episodes/E014.md) covers the pursuit of its stolen `shiny`, the **Thorn Row house**, **Randall Owen**, and a ritualist claiming to serve **Catoblepraithe / the Soulbroker**, without asserting the patron appeared.

**E013.5 is special:** The [supplemental dossier](episodes/E013.5.md) separates a **Stanley in-character retrospective recap** from a **previously unused Hope/Vorel dialogue** set **during E008–E009**. Hope there states her intention to **go back in time to complete an ancient dark pact**, drawing on her beliefs about dragon engines. This is **character testimony**, not confirmed physics or an event staged in the original E008/E009 recordings. The inserted scene is **first available to listeners in E013.5**, though set earlier in the narrative.

All three source SRTs remain unchanged; source-specific evidence, transcription uncertainties and open listening tasks appear in [review queue](project/REVIEW_QUEUE.md) and [ledger](world/CONSISTENCY_LEDGER.md). A relevant archived [Catoblepraithe illustration](sources/images/Catoblepraithe_-_Audie_Norman.webp) is only a later/undated **fan-art spelling lead** with unverified individual media rights.

## Episode 15–16 reference expansion (2026-10-21)

[E015 — The Darkness](episodes/E015.md) continues E014's ritual-house threat: **Tylander Sullivan** escapes, the group retrieves no authentic mine deed (a purported document **vanishes into smoke**), later **kills Tylander**, and negotiates to keep cyclops **Orp** alive. The party separates into a **town-bound** pair (Hope/Stanley) and **desert/hunting** pair (Nash/Vorel) at the end.

[E016 — Dragon Mother](episodes/E016.md) develops **Vorel's encounter with a female lizardfolk priestess and a ritual vision involving Fuxi, Father of Fire**; the GM spells the divine name **F-U-X-I** in the recording. In Slavetown, the party witnesses **a severed animated arm, dead Toyota Host fighters, a black-dragon flyover and Nash's unexpected fire/scaling**. The magistrate **reports Tylander has returned**, and proposes a search of the **Black Mine** based on a claimed land record associating **Catherine Speckles** with its **999th level**. This is *reported official intelligence*, not an independently inspected record. The enslaved Dusthill citizens were reportedly **evacuated** to the Salivating Fields, **not yet freed**.

**Evidence:** These are **time-coded, unverified processed-ASR dossiers**, not reader transcripts or listening-confirmed corrections. The titular **Dragon Mother** does not establish a new character identity: a voice that addresses `Mother` is heard **privately by Nash**, while an external black dragon flyover is narrated. See the [consistency ledger](world/CONSISTENCY_LEDGER.md), [review queue](project/REVIEW_QUEUE.md) and [source evidence policy](project/EXTERNAL_REFERENCES.md). Both source SRTs remain immutable.

## Owner-supplied numbering and continuity notes (2026-10-21)

Two supplied exports, **`There Will Be Dungeons episodes.xlsx`** and **`There Will Be Dungeons.docx`**, are now summarized in [the episode numbering policy](project/EPISODE_NUMBERING.md) and [owner-note reference](project/OWNER_EPISODE_NOTES.md). **Existing archived files use the spreadsheet's corrected episode IDs**, especially its explicit **Column I normalized filename labels**. Original podcast-listing numbers are preserved as lookup aliases, **not** as replacement repository episode IDs.

This matters after Wastes Season 1 original **55**, which is a **Year One Q&A bonus**: original regular **56** is corrected **E055**. The two **Inverse** installments occupying original label **77** do not belong to the Wastes main-episode sequence; original **78** is corrected **E076**. Separate campaigns and bonus entries retain their own categories. **No files are being renamed by this import.**

The **DOCX is the owner's personal research log, not a canonical spelling authority or audio verification**. Terms such as `Kuromo Kishi`, `Laktid` and `Quizquoz` remain user-spelling/search candidates. Early event and first-mention notes inform the listening queue, not retroactive unverified transcript edits. Original spreadsheet and document exports remain outside the repository; the notes above are selective derived references.

## E017–E018 campaign-reference expansion (2026-10-21)

**[E017 — Fire in the hole!](episodes/E017.md)** records Nash's **Pixie Blush** symptoms, a **bank-robbery invitation to Vorel** (not an executed heist), the foundry confrontation, major fire in **Slavetown**, and the party fleeing toward the **Black Mine** in a **replacement station wagon**. **[E018 — Into the storm](episodes/E018.md)** follows the wagon into a desert sandstorm, the party's refuge inside a giant carcass, Nash's own account of the nail **“Freedom”** in his staff, and their arrival at the **Black Mine** and undead **elevator cliffhanger**.

**Important source boundaries:** **“Freedom”** is also the name of a **different firearm** previously found in **E014**; the E018 story is **Nash's first-person memory**, not a proved flashback. E018 dwarf-guard claims about an enslaved-miner uprising and deliberate starvation are **attributed testimony**, while an undead attack at the elevator is **played/GM narrated**. E017's explosion and urban fire are physical events; Nash's apparent green-elf companion is part of an **impaired experience**. The eventual total devastation or survival of every Slavetown resident is **not** established.

The [owner's noncanonical notes](project/OWNER_EPISODE_NOTES.md) supplied useful search leads for Pixie Blush and Nash's nail without replacing the SRT as the episode evidence. All navigation times are from **unverified processed Parakeet SRTs**; no audio or new reader transcript was produced.

## E019–E021: deep Black Mine reference expansion (2026-10-21)

The [E019 dossier](episodes/E019.md) records the lengthy undead elevator battle, reversal by the Oilbeard guards, free fall, **Stanley's Feather Fall**, and a hidden-lever **rockfall** cliffhanger. The [E020 dossier](episodes/E020.md) follows the survivors' rescue and **Tickles's death**, recovers **Tylander Sullivan's own day-245 journal**, and follows the group past a dangerous chasm and tainted displacer beast into opaque magical darkness. The [E021 dossier](episodes/E021.md) continues through **Hope's private whisper**, hostile mushrooms, **Dorothy** the talking door, and Tylander's chapel/followers to a final large speaking winged figure.

**Important distinctions:** Tylander's **journal is positively attributed** by the GM, but the old skeleton found near it is **not identified**. In E021 Tylander **magically impersonates Catherine Speckles**, while a separate imprisoned woman later **names herself Catherine** and gives a message for Bertrand the Jeweler before becoming unresponsive; the party judges her dead. **Tylander's accounts** of Pristine and turning enslaved miners into undead remain his testimony, to compare with earlier GM exposition and direct observed monsters. The final winged figure is **not conclusively identified as Catoblepraithe** at E021 cutoff. No deed is recovered, and the completed confrontation belongs to a later recording.

These are **unverified Parakeet-SRT-based reference dossiers**, not listener-checked dialogue or polished reader transcripts. [Review queue](project/REVIEW_QUEUE.md) and [consistency ledger](world/CONSISTENCY_LEDGER.md) preserve outstanding source disputes. Original SRT files remain unchanged; numbering uses the owner's corrected [archive identifiers](project/EPISODE_NUMBERING.md).

## E022–E024: Soulbroker pact and dragon-metal heart (2026-10-21)

The [E022 dossier](episodes/E022.md) follows the ritual chamber confrontation: the winged oil demon **Quizquaz** is separate from the **beholder** beneath the platform, which is defeated. Vorel fights companions under **magical charm** before he is subdued. **Quizquaz** then opens a rift to the goat-headed **Catoblepraithe / Soulbroker**.

The [E023 dossier](episodes/E023.md) covers the Soulbroker's **Château Weir** hospitality and **Hope's private mother-dream**, and records a critical party split: **Nash, Hope and Stanley sign** a pact to kill the Principle within **1,000 days and 1,000 nights**, risking their souls; **Vorel declines**. The contracted extra feat is **not** the level-four reward everyone earned in E022.

In the [E024 dossier](episodes/E024.md), the **GM explains Nash's custom dragon-metal heart**, whose working source name is `Kas de Jira`; Nash visibly becomes a **black dragon wyrmling**. The Soulbroker describes **Celestium**, **Fox and Scully**, **Elhendar**, and a possible route to Hope's father, but these are **quest leads/claims**, not fulfilled objectives. The party recovers the chapel chest's treasure and identified potions and sets **Dorothy's wooden door** burning, but **does not conclusively escape** the Black Mine by the episode end.

All findings are **time-coded, unverified processed-Parakeet evidence**. Names from the owner's notes are not canonical; original source subtitles, images and `world/entities.json` remain untouched. Review the [source hierarchy](project/EXTERNAL_REFERENCES.md) and [open listening queue](project/REVIEW_QUEUE.md).

## E025–E027: surface, rebuilt Fate 4 and new rival orders (2026-10-21)

The [E025 dossier](episodes/E025.md) shows the party **clearing the still-talking Dorothy passage**, using **Nash's enlarged dragon form** to escape the Black Mine shaft, fighting armed Oilbeard dwarves and **coercively torturing Scrolly before throwing him into the shaft**. It ends at a **locked prisoner room**, not with the contents resolved.

The [E026 dossier](episodes/E026.md) identifies **Bertrand the Jeweler, Trigger and Bok Bok** in the prison and documents how **Fate 4 has been repaired and brought back**. Bertrand offers *claims* about Tylander's earlier execution, a possible dragon-metal deed and a **Lactid** operative threatening Slavetown. The group arrives at the **Liberators' hidden camp**, where character disagreements over violence sharpen and Vorel hunts a bear.

The [E027 dossier](episodes/E027.md) documents attempted reconciliation with Stanley, the **Liberators' planned relocation**, a young stowaway **Tedna**, and a dangerous attack by **Sir Ranko of the Umbilical Order**. The episode ends with **Diptak of the Golden Land charging Vorel** over an alleged **Typalla/Tepala consort dispute**; no duel result has been established.

All dossiers remain **approximate, processed-Parakeet-only reference work**. Owner-provided corrected numbering remains the repository standard, while personal spellings are **research leads**, not canonical terms. The [continuity ledger](world/CONSISTENCY_LEDGER.md) and [listening queue](project/REVIEW_QUEUE.md) record open contradictions. Original transcripts, artwork and entity data remain unchanged.

## E028–E030: Golden Land pledge, Stanley's solo episode and the Teet approach (2026-10-21)

The [E028 dossier](episodes/E028.md) establishes **Diptak yielding and pledging Golden Land clan aid to Vorel**, the first appearance of **Buttons**, an educated speaking cat with a prosthetic leg, and the emergence of a **compelling song** that draws Hope toward the oil sands. The Teet's **Guzzle Gang, Suckmaster and Trashburg** are at this stage primarily **Buttons's secondhand descriptions and an older Dan Dakota map**, not direct party observation.

The [E029 dossier](episodes/E029.md) documents a special **Beau-and-Jon-only played session** in normal narrative sequence. Stanley restrains entranced Nash, investigates the old oil-sands prison with Buttons and rescues the group from a singing creature and hag. A blue figure naming himself **Dion Talus, archfey of carnage**, proposes a violent bargain; **Stanley expressly refuses** and the entity **forces its light/energy into him**. **Do not mislabel this as Stanley voluntarily signing a second pact.**

The [E030 dossier](episodes/E030.md) records the regular cast's return, Nash freeing himself with **Reduce**, the group escaping a collapsing, oil-flooding complex, the **immovable rod being lost under oil**, and Buttons providing **Blink spell text** to Stanley. The adventurers plan to hide **Fate 4 outside the Teet** and enter cautiously; **no city infiltration or Guzzle Gang fight has occurred** by the end.

All details derive from **unverified processed Parakeet SRTs**, not audio listening; names from the owner note are noncanonical. The episode numbering remains the owner's [corrected scheme](project/EPISODE_NUMBERING.md). Original source files and entity data are unchanged.

## E031–E033: the Teet / Trashburg reference expansion (2026-10-21)

The [E031 dossier](episodes/E031.md) documents the party's **first visit into Trashburg**, its French-speaking host **Charlemagne**, a public announcement of **Jolt/Acrimonicar's forthcoming wedding** to Prince Alidwyr, and the discovery of a living pixie **P0D**. **P0D says Farmer Dewey's farm crushes pixies to manufacture Pixie Blush**; the party has *not inspected or liberated* that farm.

The [E032 dossier](episodes/E032.md) follows the **Twenty-Six Block gang**, led by **Monsoon Cabbage**, whose conditional offer trades information on entering the keep for the elimination of a **Toe Ripper** rival. Other possible entry plans involve **wedding catering** and **Blood Ball**, but none is completed. **Buttons confronts Stanley** about witnessing the E029 blue-light event; **Stanley uses Suggestion** to redirect him. The episode ends with the armed-dealer building's fanged-figure cliffhanger.

The [E033 dossier](episodes/E033.md) records the ensuing fight with a **regenerative vampire-like opponent**, the bite that **reduces Hope's maximum HP**, recovery of a **rocket launcher with two projectiles**, and an invitation to the **Trashburg Gray Socks**. Stanley's increasingly troubling conduct and statement that he is **“Stanley right now”** add uncertainty but **do not confirm an alternate identity or consensual archfey pact**. **Scott is absent** from the recording, rather than Nash disappearing from the campaign.

**Status:** All are **time-coded, processed-Parakeet-only reference dossiers**, not audio-verified transcripts. The original source SRTs remain unchanged; the owner's corrected episode numbering is in force, and personal spellings remain noncanonical. See [review queue](project/REVIEW_QUEUE.md) and [consistency ledger](world/CONSISTENCY_LEDGER.md).
