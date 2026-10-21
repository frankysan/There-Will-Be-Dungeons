# The Wastes — transcription and campaign-reference pilot

**Status:** The E000/E001 reader-edition pilot remains incomplete and not manually proofread. Processed Parakeet SRTs for subsequent episodes are included as source material; **E002–E054** (including E013.5 and the **separate holiday one-shot E043**) and the **March 2019 Year One Q&A bonus** now have preliminary, unverified **reference dossiers**, not publishable reader editions.

This package establishes a repeatable, **local-first** path from podcast audio to readable, speaker-labelled text, with a separate campaign reference that cites episode time positions. It covers the *There Will Be Dungeons* campaign described in the supplied files as *The Wastes*.

## Start here

1. [E000 — Introductions: reader-edited draft](transcripts/E000.reader-draft.md) ([machine draft](transcripts/E000.readable-draft.md), [edit log](transcripts/E000.reader-edits.json))
2. [E001 — The Campaign Begins!: reader-edited draft](transcripts/E001.reader-draft.md) ([machine draft](transcripts/E001.readable-draft.md), [edit log](transcripts/E001.reader-edits.json))
3. [Corrected episode numbering / original-label crosswalk](project/EPISODE_NUMBERING.md), [archive-owner's noncanonical episode notes](project/OWNER_EPISODE_NOTES.md), [External sources and chronology policy](project/EXTERNAL_REFERENCES.md), [Project charter](project/PROJECT_CHARTER.md), [workflow](project/WORKFLOW.md), [editorial rules](project/EDITORIAL_GUIDE.md) and [decision log](project/DECISIONS.md), [model test record](project/MODEL_TESTS.md) and [roadmap](project/BACKLOG.md)
4. [World reference index](world/README.md), [characters](world/CHARACTERS.md), [places](world/PLACES.md), [world history](world/WORLD.md), [chronology](world/CHRONOLOGY.md), and [consistency issues](world/CONSISTENCY_LEDGER.md), and [machine-readable entity index](world/entities.json)
5. [Episode dossiers](episodes/E000.md) and [E001](episodes/E001.md)
6. [Review queue](project/REVIEW_QUEUE.md), [automated file audit](reports/SRT_AUDIT.md), and [Qwen Q4/Q8/Canary variant evaluation](reports/QWEN_VARIANTS_2026-10-21.md)
7. **Expanded campaign context:** [E002 — Spiders](episodes/E002.md), [E003 — Soft Head Returns](episodes/E003.md), [E004 — The Oil Demon](episodes/E004.md), [E005 — Goblincide](episodes/E005.md), [E006 — Start your engines!](episodes/E006.md), [E007 — Bok Bok Keeping It Fresh](episodes/E007.md), and [E008 — Stupid Gnomes!](episodes/E008.md), [E009 — Surfacing](episodes/E009.md), [E010 — Shackles](episodes/E010.md), [E011 — Kick me as hard as you can](episodes/E011.md), and [E012 — Work Hours](episodes/E012.md), [E013 — Old One Eye](episodes/E013.md), [E013.5 — Supplemental](episodes/E013.5.md), and [E014 — That's Magic](episodes/E014.md), [E015 — The Darkness](episodes/E015.md), and [E016 — Dragon Mother](episodes/E016.md), [E017 — Fire in the hole!](episodes/E017.md), and [E018 — Into the storm](episodes/E018.md), [E019 — Elevator Action](episodes/E019.md), [E020 — Flaky Mushrooms](episodes/E020.md), and [E021 — The Mushroom Kingdom](episodes/E021.md), [E022 — The Charmed Lizard](episodes/E022.md), [E023 — Demon Hotel](episodes/E023.md), and [E024 — Monogamy Respected](episodes/E024.md), [E025 — Door Authority](episodes/E025.md), [E026 — The Hunt](episodes/E026.md), and [E027 — Lizard Party](episodes/E027.md), [E028 — It's A Cat Person!](episodes/E028.md), [E029 — Stanley's Choice](episodes/E029.md), and [E030 — The Worm Turns](episodes/E030.md), [E031 — Three Men and a P0d](episodes/E031.md), [E032 — The Great Bleaching](episodes/E032.md), and [E033 — Nashfree](episodes/E033.md), [E034 — Blood Ball](episodes/E034.md), [E035 — Genitals McReady](episodes/E035.md), and [E036 — High on Toes](episodes/E036.md), [E037 — Dirty Chalice](episodes/E037.md), [E038 — Don't lose Hope](episodes/E038.md), and [E039 — Taking up arms](episodes/E039.md). These are reference dossiers, **not publishable reader transcripts**, drawn from processed Parakeet SRTs; audio accuracy, names, and speaker assignments still need verification. E008 features guest players/characters, not substitute actors for the absent regular performers. See the [expanded chronology](world/CHRONOLOGY.md), [characters](world/CHARACTERS.md), [places](world/PLACES.md), and [consistency ledger](world/CONSISTENCY_LEDGER.md).

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

The [E029 dossier](episodes/E029.md) documents a special **Beau-and-Jon-only played session** in normal narrative sequence. Stanley restrains entranced Nash, investigates the old oil-sands prison with Buttons and rescues the group from a singing creature and hag. A blue figure naming himself **Diontalus, archfey of carnage**, proposes a violent bargain; **Stanley expressly refuses** and the entity **forces its light/energy into him**. **Do not mislabel this as Stanley voluntarily signing a second pact.**

The [E030 dossier](episodes/E030.md) records the regular cast's return, Nash freeing himself with **Reduce**, the group escaping a collapsing, oil-flooding complex, the **immovable rod being lost under oil**, and Buttons providing **Blink spell text** to Stanley. The adventurers plan to hide **Fate 4 outside the Teet** and enter cautiously; **no city infiltration or Guzzle Gang fight has occurred** by the end.

All details derive from **unverified processed Parakeet SRTs**, not audio listening; names from the owner note are noncanonical. The episode numbering remains the owner's [corrected scheme](project/EPISODE_NUMBERING.md). Original source files and entity data are unchanged.

## E031–E033: the Teet / Trashburg reference expansion (2026-10-21)

The [E031 dossier](episodes/E031.md) documents the party's **first visit into Trashburg**, its French-speaking host **Charlemagne**, a public announcement of **Jolt/Acrimonicar's forthcoming wedding** to Prince Alidwyr, and the discovery of a living pixie **P0D**. **P0D says Farmer Dewey's farm crushes pixies to manufacture Pixie Blush**; the party has *not inspected or liberated* that farm.

The [E032 dossier](episodes/E032.md) follows the **Twenty-Six Block gang**, led by **Monsoon Cabbage**, whose conditional offer trades information on entering the keep for the elimination of a **Toe Ripper** rival. Other possible entry plans involve **wedding catering** and **Blood Ball**, but none is completed. **Buttons confronts Stanley** about witnessing the E029 blue-light event; **Stanley uses Suggestion** to redirect him. The episode ends with the armed-dealer building's fanged-figure cliffhanger.

The [E033 dossier](episodes/E033.md) records the ensuing fight with a **regenerative vampire-like opponent**, the bite that **reduces Hope's maximum HP**, recovery of a **rocket launcher with two projectiles**, and an invitation to the **Trashburg Gray Socks**. Stanley's increasingly troubling conduct and statement that he is **“Stanley right now”** add uncertainty but **do not confirm an alternate identity or consensual archfey pact**. **Scott is absent** from the recording, rather than Nash disappearing from the campaign.

**Status:** All are **time-coded, processed-Parakeet-only reference dossiers**, not audio-verified transcripts. The original source SRTs remain unchanged; the owner's corrected episode numbering is in force, and personal spellings remain noncanonical. See [review queue](project/REVIEW_QUEUE.md) and [consistency ledger](world/CONSISTENCY_LEDGER.md).

## E034–E036: revealed Diontalus, Blood Ball practice and the Golden Gargoyle (2026-10-21)

The [E034 dossier](episodes/E034.md) records the **explicit Diontalus self-identification in Stanley's body**. The speaker acknowledges the **forced joining after Stanley rejected his offer**, though his claimed ancient history and consciousness/memory rules remain his account. The party **practices Blood Ball** for the Trashburg Gray Socks, receives jersey numbers **Vorel 1 / Hope 3 / Stanley 5 / Nash 7**, and discusses **future** compensation and a chance at the keep—**not yet a match or payment**.

The [E035 dossier](episodes/E035.md) follows **Charlemagne's grief over arms dealer Jedel McCready**, the party's suspicions about the Twenty-Sixers (not verified theft), and **Vorel initiating a violent encounter** with the Toe Rippers in east Trashburg. A building catches fire; **Nash's dragon-metal heart provides acid breath** without a full dragon transformation. The party withdraws while guards sound an alarm and **does not confirm the leader's death**. At episode's end they arrive inside the **Golden Gargoyle**, following an invitation from **Fango Rabbish**.

The [E036 dossier](episodes/E036.md) covers **Angel Ashi's performance**, a massive **Toe Ripper ambush involving Blunt Goliver** (leader's name still audio-unverified), the party's fight and **escape through Fango's backstage/sewer passage**. **Blunt Goliver is not shown dead or captured**, leaving **Monsoon Cabbage's proposed leader-kill bargain unfulfilled**. Angel Ashi elects to accompany Nash back to the inn. Nash receives **two exhaustion levels** for shifting, while the GM awards **level 5** out of game but explicitly **does not reset conditions or HP**.

All three are **provisional processed-Parakeet-SRT reference dossiers, not audio-verified**. Original subtitles, artwork and structured entity records remain unchanged. Check [consistency ledger](world/CONSISTENCY_LEDGER.md) and [review queue](project/REVIEW_QUEUE.md) for unresolved names and speaker claims.

## E037–E039: a secret heist, Hope's crisis and Monsoon's ambitions (2026-10-21)

[E037 — Dirty Chalice](episodes/E037.md) includes **Vorel secretly receiving and burying a trunk of Jolt-associated Slavetown safe loot** (the earlier heist is reported by a contact), and **Angel Ashi's magic reacting to Nash's dragon-metal heart**. The episode continues with **Charlemagne evacuating**, **Tedna's in-world letter from inside the Teet keep**, **Monsoon's first visit and marked underground route**, **replacement weapons including Vorel's custom Ma Storm sword**, and finally **a monk returning Hope's fired rocket directly into her** at the episode's explosion/cave-in cliffhanger.

[E038 — Don't lose Hope](episodes/E038.md) begins in the **aftermath of the already-fired rocket**, with hazardous smoke, injuries and the party's rescue attempts. **Nash, Stanley and Vorel defeat Blunt Goliver, and Vorel beheads him**; the party takes his head to **Monsoon Cabbage** and seeks urgent treatment for Hope. **Dr Dickles** and the companions must amputate her shattered **left arm and leg** before subsequent prosthetic fitting.

[E039 — Taking up arms](episodes/E039.md) shows **Hope's new mechanical left arm/leg and integrated rocket mechanism**, a **public Teet security accusation naming Stanley/Dion as a wanted mage attacker**, and the party's clandestine reunion with Monsoon. He **claims Buttons provided their names, Tedna is detained, a Lactid controlled Blunt Goliver**, and that a route through the **Pit of Despair** could lead into the Teet. His personal **Tiat Cala/Kefeli** history, alternate name and **Gem of Tides** theory remain **interested NPC testimony**. Monsoon also **admits ordering Hope's caregivers killed** after surgery—a grave character confession that must not be conflated with an independent forensic finding.

**Continuity gate:** The original rocket shot is in **E037**, consequences and Blunt's death in **E038**, and working cybernetics and expanded faction history in **E039**. No Teet keep raid, wedding heist, pixie release, Blood Ball match or Principle defeat has occurred by E039 cutoff. All are **machine-SRT-derived reference dossiers, not audio-verified**. [Review queue](project/REVIEW_QUEUE.md) and [consistency ledger](world/CONSISTENCY_LEDGER.md) track outstanding claims and names; original source SRTs are untouched.

## E040–E042: pursuit, the Pit of Despair and black puddings (2026-10-21)

[E040 — The Tale of The Two Phillips](episodes/E040.md) picks up the attempt to reach the **Pit of Despair** following **Monsoon's E039 briefing**. The party departs Twenty-Six Block, but the **Teet Guard and Guzzle Gang house searches**, sweeping keep spotlights and **Hope's limited prosthetic-leg mobility** make stealth difficult. **Diontalus**, directing Stanley's body, uses illusionary guard disguises while **Vorel carries Hope**. A failed encounter with suspicious guards becomes a huge street fight. Men known as the **two Phillips** are sent into a magical dark zone, but their precise fates are **not directly verified**. The characters end the episode **running toward the pit**, still under active search.

[E041 — Only take one egg](episodes/E041.md) sees the party **enter the enormous barred pit**, descend on a rope and survive the deep fall with magic. **George**, a frightened Teet Guard, accompanies them into the depths. The party actually sees the enormous **froghemoth** Monsoon had previously described; **Vorel draws its attention**, aided by **Stanley's Phantasmal Force illusions**, while the others find and force open a **rusted side-crevasse hatch** into deeper oily tunnels. **Nash takes an unidentified luminous sphere** from a cluster nearby. After entering the caves **Stanley argues against killing Buttons**, and a distant **singing self-described king** is heard but not met.

[E042 — Anyone for some black pudding](episodes/E042.md) continues in the caves. Nash **cuts open the sphere**, spilling its membrane and retaining a **soft black core**—the object has **not been confirmed to be an egg**. The group encounters a **separate pale tentacled cavern creature**, passes **stone-like boots** suggestive of—but not proven to be—petrification, and finds an **Infernal inscription Hope privately receives the translation of**. They recover an old **supply cache** with a mysterious smooth wooden stick and other provisions; no finished Identify result is established. Two **black puddings** then ambush them and are defeated after a prolonged battle. **George accidentally shoots his own foot**; before his care is resolved, Vorel calls out to the **still-unseen singer**.

**Evidence boundary:** These are **time-coded scene-reference dossiers derived from processed Parakeet SRT, not listening-verified transcripts**. The **sphere's state changes in E042**, the froghemoth, cave worm and puddings are **separate entities**, and the unseen singer is **not confirmed as an actual king**. No Teet keep infiltration, **Tedna/pixie rescue**, royal wedding, Gem of Tides retrieval or Buttons resolution occurs by E042 cutoff. See [chronology](world/CHRONOLOGY.md), [character notes](world/CHARACTERS.md), [place notes](world/PLACES.md), [consistency ledger](world/CONSISTENCY_LEDGER.md), and [audio review queue](project/REVIEW_QUEUE.md). Original SRTs and structured `entities.json` were not modified.

## E043–E045: holiday special, river toll and dangerous new revelations (2026-10-21)

[E043 — Merry Chromeness!](episodes/E043.md) is a **standalone holiday one-shot**, **not an intervening session of the main Wastes storyline**. Jon/John serves as **guest DM** for Beau, Kyle and Kristen, while Scott is absent as a performer but represented fictionally. A Christmas-themed magical house, animated nutcrackers, ghosts, jukebox/gift puzzles, a fantasy transformation machine and a self-referential Vorel action figure belong **only to the one-shot setting**. Its ending includes a machine **reversal cliffhanger**. The main campaign therefore resumes **E042 → E044**, not through the holiday story.

[E044 — Poke it with your Mage Hand](episodes/E044.md) resumes after **George's E042 foot wound**: Stanley treats him, the party continues through underground caves and meets the formerly unseen singing giant calling himself **Hungui/Hungooey** (spelling unverified), a self-styled river king. They exchange treasures including the **E042 ruby and a firearm** for permission/rent, but the king **conditions river crossing on dealing with his “headache man” rival**. Another route yields **bats, dangerous green mushrooms and a large spider** and a **bag with seven magical beans and skeleton-marked key**. The E042 rucksack's preserved wood is revealed as a **Wand of Scowls**, then passed to Nash. In a protected rest camp, **Stanley reveals “Stanley Billings” is a chosen name** and urges his companions toward better ethics. **George remains alive at this cutoff**.

[E045 — Those Eyes](episodes/E045.md) begins after the long rest. **Diontalus is in control of Stanley's body and deliberately stabs George to death**, despite Hope's effort to prevent it. George's belongings include a love note **signed “Martha Miller”** and a child's stuffed rabbit. Elsewhere, **Vorel kills a petrifying-gaze basilisk** and fashions a bone javelin. The **black core** Nash carried after rupturing the unknown sphere in E042 **animates, bites him, then is destroyed by Nash's Fire Bolt**. A separate **attacking wall shadow disperses**; a **horned tiefling skeleton** has diamond earrings and writing shared only by GM private message. At another river the group encounters and **kills a dark humanoid whose gaze/proximity causes headaches and necrotic harm**, strongly suggesting—but not separately proving—it is the king's hated **“headache man.”**

**Evidence gate:** E043's events **must not populate canonical Wastes character history**. George's injuries and death are **distinct events in E042, E044 and E045**. The glowing sphere/core sequence is **E041 pickup → E042 opening → E045 animated core destroyed**. The keeper's **rent/bargain is not yet a completed river crossing**; no Teet keep entry, Tedna or pixie rescue, royal wedding, Blood Ball result or Gem of Tides retrieval has occurred. [World chronology](world/CHRONOLOGY.md), [characters](world/CHARACTERS.md), [places](world/PLACES.md), [consistency ledger](world/CONSISTENCY_LEDGER.md) and [review queue](project/REVIEW_QUEUE.md) track provisional claims, original private handouts and names requiring listening. Only documentation was edited; original processed SRTs and `entities.json` are unchanged.


## Cast-written name and spelling evidence (2026-10-21)

The [Discord spelling report](reports/DISCORD_SPELLING_2026-10-21.md) inventories cast-attributed messages, a cast-shared episode recap, later sheet-link previews, an **Inverse** GM outline and a **Delvers** guide. It establishes an **archive-owner-approved creator spelling: Diontalus** (written by Jon twice). Older machine forms such as `Dion Talus`, `Deontalus`, and recap `Diantalus`/`Diontalis` are **aliases, not equal canon**. These changes affect curated reference prose, **not the original machine SRTs or already-generated reader drafts**.

Other supported written forms include **Nash Maggard, Stanley Billings, Teet, Slavetown, Tedna, Talia, Pentael Wise**, and **The Eye of Groxl** (**owner-confirmed canonical artifact name**, same item as ASR `Grojil`/`Groxel`; not proof of a separately named deity's identity). **Tietkalla** is a cast-supported candidate for matching `Tiat Cala` references, **not** a universal replacement without identifying the referent. The **Catoblepraithe/Catobelpraithe** and **Angel Ashi/Angelashi** questions remain open. **Inverse/Delvers names are kept out of the Wastes references**, and cast-shared or fan sources do not themselves audio-verify words or episode events. See [ledger](world/CONSISTENCY_LEDGER.md), [editorial guide](project/EDITORIAL_GUIDE.md), and [decisions](project/DECISIONS.md).

## E046–E048: enchanted underground access, imprisoned book scholar and prison rescue (2026-10-21)

The latest provisional episode dossiers are [E046 — There's a Patch For That](episodes/E046.md), [E047 — 50 Shades of Grain](episodes/E047.md) and [E048 — George Style](episodes/E048.md). All are **processed-Parakeet-only research notes**, not new proofread transcripts.

**E046:** The E045 headache-creature kill **does not clear the threat**; more such creatures attack immediately. **Nash** finds the **Robe of Useful Items**, an enchanted finite-patch garment, and the E045 tiefling-skeleton earrings are revealed as **ear-enlarging**. A riddle and **E044's recovered enchanted beans and skeleton key** provide a **green beanstalk / keyed hatch route upward**, after a cautious visit to the original froghemoth pit grate. The party accesses centuries-old **tiefling chambers** under the keep, encountering enchanted armor and a book with disturbing moving images.

**E047:** The book is first restrained. The party explores an old **Infernal-language library**, fights an **animated book swarm**, and—using **P0D's scouting**—reaches a secret bureau. A private **Akmenos-lineage text** is encountered but not publicly transcribed; Vorel gets a **+1 lizardfolk-skull helmet**; a scroll signed `N` to `M` discusses a protective book, without verified names. Hope's ritual with a preserved head lets an aged tiefling try to escape the animated book; **Nash casts Reduce** and **Vorel hauls him out**. The man's initial “queen” greeting to Hope is explained/qualified in E048.

**E048:** The released elder, **Nobiery/Nobieri** (name not settled), claims **Hope's Akmenos heritage**, a **Dead Tongue** role guiding souls to the **Night Pasture**, a forgotten council of vampires, and a hidden **thousand-person army from twelve houses** secured through a **Soulbroker deal involving twenty sacrificed newborns**. He *infers* Kefeli may have become a Medusa and tells Nash he is like a **crystal of arcane power**. None of these historical or metaphysical assertions is verified merely by his testimony. After discussion, the **elder travels through Nash's Château Weir portal alone**, with his claimed troops uncollected. Following a long rest **Stanley regains the shared body**, speaks about George's murder and proposes a later family visit. The group uses the **Robe's 24-foot ladder patch** to climb into the keep prison; **Nash incapacitates and severely drugs two guards (no confirmed death)**, and **Tedna and Bok Bok are both directly freed alive**. **Tedna reports** Angelashi was taken to the pit/“Fragger”; **her death remains unverified**.

**Boundary:** The old E045 reference pages correctly stated **no keep entry or prisoner rescue as of that earlier cutoff**. **By E048 this has changed**: two prisoners are liberated, but no Gem of Tides, completed wedding/Jolt resolution or verified supernatural army has been obtained. **Diontalus** is creator-approved spelling; **Tietkalla** cast-backed but matched contextually to the old `Tiat Cala` name; **Nobiery** and **Angelashi/Angel Ashi** remain spelling-review questions. Sources stay untouched. See [world chronology](world/CHRONOLOGY.md), [characters](world/CHARACTERS.md) and [review queue](project/REVIEW_QUEUE.md).

## E049–E051: the warehouse betrayals, Pillars of Decency and Kefeli's petrification (2026-10-21)

The new [E049 — Podzilla](episodes/E049.md), [E050 — The Pillars of Decency](episodes/E050.md) and [E051 — Tripping Is Not A Standard Action](episodes/E051.md) dossiers extend the **provisional, time-coded processed-ASR coverage through E051**. They are **not listener-proofread reader editions**.

**E049:** The party's E048 prisoner rescue flows into a **keep storeroom trap**, after Stanley spots **Softhead alive**, despite his earlier apparent disappearance in a subterranean river. **Jolt and Buttons** discuss a changed **Monsoon/Principal deal** over the **Gem of Tides**, but those future promises remain **Buttons' claims**. Monsoon commands **P0D** over a radio and she **involuntarily enlarges into a dangerous monster**. During the ensuing fight, **Vorel kills Buttons**. **P0D and Jolt remain alive at this episode's cutoff**.

**E050:** **Diontalus kills P0D** while Nash is trying to calm/save her; her body **disperses as pixie dust**. **Tedna**, alive on rescue E048, **dies of the injuries sustained in battle** despite temporary stabilization, while Hope is impaired by pixie-blush hallucinations. **Dashington shoots Hope then is killed**, and **Jolt is killed by Hope**; the dreamlike **“steel heaven”** scene is **not confirmed in-world afterlife travel**. Stanley regains control later, **questions Buttons' corpse** and the party **recovers the glowing Gem of Tides**. **Vorel proposes “Pillars of Decency” (POD)** as a memorial standard. **Hope obtains the named Fox and Scully revolvers and Smokey's ammunition belt**. The secret ancient crypt route brings the party into the **old tiefling water-throne area** and a meeting with **Kefeli**.

**E051:** **Kefeli's** claims about her status, Akmenos origins and **Andreeste** are **NPC testimony**, even though her **gaze, serpent-hair attacks and water magic demonstrably work**. **Vorel and Hope are petrified**; **Stanley's reflected-gaze maneuver petrifies Kefeli**, after which Nash and Stanley destroy her stone form and other old statues. Destruction **does not reverse the PCs' petrification**. By returning to the **E045 basilisk corpse** and using preserved eyes from the old bureau, Nash and Stanley prepare a one-time restorative mixture and **bring both Hope and Vorel back alive during E051**. The party then reaches siege stairs: **Nash's attempted trip accidentally kills a fleeing guard**, and **multiple other giant pixies enter the fight**. **No conclusion to the siege or Principal is yet shown**.

**Review gates:** The **Gem is back in the party's hands E050**, but exact emplacement/water-flow status in E051 should be checked. P0D's death is not evidence she willingly betrayed Nash; the **E051 giant pixies are others**. Tedna's E048 rescue is not negated retrospectively by E050 death. **Diontalus** is creator-accepted written spelling, **Tietkalla** a context-qualified cast-supported place spelling; remaining identities/phrases require listening. See the updated [chronology](world/CHRONOLOGY.md), [characters](world/CHARACTERS.md), [consistency ledger](world/CONSISTENCY_LEDGER.md) and [review queue](project/REVIEW_QUEUE.md). Original SRTs and `entities.json` were not changed.

## E052–E054: the froghemoth, Eye of Groxl, and Hope's coronation (2026-10-21)

New source-qualified dossiers are [E052 — Hear me, Froghemuth!](episodes/E052.md), [E053 — Snacks of Power](episodes/E053.md), and [E054 — Blow the walls down](episodes/E054.md). These extend **unverified processed-SRT reference coverage through E054**, not polished, audio-checked transcripts.

**E052:** The party battles and is swallowed by a hugely altered **froghemoth**, wandering through digestive chambers and other internal organs. **Spell anomalies** include a small extra hand for Nash. At episode end **Vorel contacts the brain telepathically**, but **command and landing remain unresolved**.

**E053:** Vorel requests that the creature expel them before what it describes as astral ascension. The beast **splits**: an **upper cocoon-like segment escapes into the sky**, while the **lower body falls to the desert** and ultimately decays, trapping the party until they escape by **rowboat patch through the bowel outlet**. Vorel obtains a **living sentient eye grafted to his chest**, canonically the **Eye of Groxl**, as explicitly confirmed by the archive owner and supported by Kyle's written item title; E053 ASR `Eye of Grojil` and E054 ASR `Eye of Groxel` are **aliases for this same item**. The identity of a separately named deity or legendary warrior still needs independent evidence. His **color-changing scales are a separate pixie/froghemoth effect**, not the eye's ability. Vorel recovers a **previously hidden desert gold hoard**, of which only part is taken; Nash becomes a **young black dragon** and flies the team back.

**E054:** The group observes **devastated Trashburg and breached Teet keep**. Many giant pixies **revert to small form**. Nash **smashes open the throne-room wall** and discovers **Monsoon** with **dead Prince Aladweir**, captured **Suck Master Din**, and **Angelashi alive as hostage**. Vorel attacks Monsoon, who **escapes as mist rather than dying**. The party **frees Angelashi alive**, refuting her earlier presumed death. **Nobiery returns through a portal with hundreds of armed tieflings**, and **Hope is publicly crowned Queen of Tietkalla**. **Din is executed by Vorel at Hope's signal**; new leaders begin organizing security, farms and repairs, and some express anti-human prejudice. **Monsoon's future Andreeste warning is his testimony**. The GM announces the **end of this story arc**, **future months-long downtime** and level-7 advancement; **those prospective reforms and individual projects are not already completed within the E054 scene**.

**Cross-cutting status:** Angelashi **alive**, Hope **crowned**, promised army **substantially materialized** (exact old numbers unverified), **Monsoon escaped**, **Principal and Andreeste still unresolved**, and airborne froghemoth **upper segment fate unknown**. See [chronology](world/CHRONOLOGY.md), [characters](world/CHARACTERS.md), [ledger](world/CONSISTENCY_LEDGER.md) and [review queue](project/REVIEW_QUEUE.md). Raw SRTs and `entities.json` remain unchanged.
