# Editorial and canon-reference guide

## Transcript standard

**Goal:** readable without changing the meaning or making unverified claims about exactly what was said.

- Speaker labels identify human participants (`Scott`, `Beau`, `Kristen`, `Kyle`, `John`), not necessarily their characters. A role-played voice still belongs to its performer.
- Preserve meaningful hesitations, false starts, interruptions and uncertainty when they affect what was said. A later *reader's edition* may suppress purely mechanical disfluencies, but it must be clearly differentiated from the faithful transcript.
- Paragraph breaks and normal punctuation are allowed editorial improvements **only if checked**. Automated reflow of an existing processed SRT is labelled `draft`.
- Preserve scene dialogue, out-of-character game talk, banter and GM narration; don't summarize them away in a transcript.
- Keep one approximate start timestamp per paragraph; retain detailed cues in `sources/` and `*.turns.json`.
- If a phrase is impossible to determine, use a consistent marker such as `[inaudible, 00:xx:xx]` after actually listening—not an invented plausible phrase.
- Avoid silent ASR correction of uncommon names; check against audio and the spelling ledger.

## Reference standard

Every entry ideally includes:

- **Name / aliases / kind** (place, character, artifact, organization, event, term).
- **Status:** `confirmed from audio`, `supported by supplied transcript`, `speaker claim`, `inferred`, or `unresolved`.
- **Provenance:** episode identifier and approximate time, plus speaker/source role.
- **Content:** short factual description; distinguish what characters believe from what the GM established.
- **Open questions / contradiction notes.**

### Levels of source confidence

1. **Listener-confirmed:** explicitly verified against the audio by a listener (e.g. speaker 5 = Scott).
2. **Game-master setting statement:** DM's in-world exposition, subject to future in-story revelation.
3. **Episode narrative:** scene/action described during play; speaker identity/plot may need review.
4. **Character perspective:** a character's beliefs, hopes, aspirations, memories and claims; these are not guaranteed external reality.
5. **Machine transcript only:** uncertain until listening, especially unusual spellings.

Do not call a proposed spelling or character belief 'canon' until supported by clearer source. Where different editions disagree, preserve both source references and record how resolution was chosen.

## Illustration production and visual continuity (2026-10-25)

Use the [illustration guide](ILLUSTRATION_GUIDE.md),
[subject template](ILLUSTRATION_SUBJECT_TEMPLATE.md) and
[appearance register](ILLUSTRATION_REFERENCES.md) for the shared comic-book /
graphic-novel art direction and written, time-specific visual instructions.
Keep production records separate from ordinary in-universe world prose.

During episode and subject research, record material visual descriptions,
equipment changes, damage, transformations and changes to places or objects
in the relevant appearance record, with exact source links and approximate
clocks/cues when available. Distinguish when a feature applies in the story
from when it is first revealed. New evidence may require revision of an
earlier artistic choice; preserve that decision's history.

Keep source role, transcription/audio verification and artistic selection
separate. Existing fan art and end-era sheets do not establish early
appearances. The show takes priority over stylistic defaults, and generated
images never become evidence of show descriptions. Backfill older subjects
in bounded passes rather than implying a complete appearance audit.

## Name rules

- `Dusthill` is the wiki-supported written form; `Dust Hill` is an ASR/search alias.
- `Nash Maggard` is wiki-supported; `Magard`, `Maghard` are preserved ASR variants.
- `Oriphi “Hope” Akmenos` is documented by the wiki. The name-pronunciation exchange with ASR `Orifi`/`Orify` remains unchanged until an audio listening review; Hope is the preferred short name.
- `Vorel Rasvim Kurik` is wiki-supported; multiple recognition variants remain aliases and require listening for phonetic fidelity.
- `Shun'ti Stoutbarrel` and `Jimster` are wiki-supported by **later** episode material. For E001, edit the name spelling only; never insert the later-disclosed surname into dialogue that lacks it.
- `Beau` is the established DM name in external credits; `Bo` may occur in ASR speech. `Jon Jagger` is wiki-supported and labelled `John` in the source ASR, so reader editions use `Jon`.
- **Canonical Wastes map orthography, owner-confirmed 2026-10-27 (D-044):** **The Principal**, not earlier **the Principle**, is the definitive recurring antagonist's *written display name*. **Khaervilon**, not earlier **Kervalon**, is the definitive place name. The large *Known Wastes* map establishes **T'ietkalla**, **Moag Ferhain**, **Ubere Mtaris** and **The Principal's Lands** as canonical labels for the corresponding referents. Use these forms in **new curated editorial prose** and review existing live editorial prose for replacement; do not retain the incorrect forms as equally acceptable alternatives. Historic generated ASR/source quotations, release titles, frozen research versions, `the-principle.md`/`kervalon.md`/`tietkalla.md` path slugs and search aliases remain preserved. Distinguish written-name authority from independent audio verification, plot truth, mapped extent and episode-era awareness. [Map register](../reports/WASTES_KNOWN_MAP_ORTHOGRAPHY_2026-10-27.md) · [D-044](DECISIONS.md).
- **Canonical Or'Nath family orthography:** Jon's illustrated poem and the owner confirm that **Valiir Or'Nath** is Stanley Billings's original elven name, with **Delit Or'Nath** as his father and **Villa Or'Nath** as the associated home. Retain `Stanley Billings` as the familiar character name, the old file slugs and `Ornath` as a historical alias; do not duplicate identities. [Discord register](../reports/DISCORD_NEW_SPELLING_2026-10-27.md).

## World-building safeguards

- The character's *plan to travel back and change history* is a stated goal, not proof that time travel is possible.
- A character's claimed origin or background can be an unreliable narrator's account.
- A statement about a feature of Dust Hill may conflict with incidental player banter (e.g. mention of a tavern; DM later says there is no tavern). Record it as an issue, not a settled fact.
- D&D rules discussion is meta-play, not automatically an in-world rule.

## External reference and spoiler safeguards

Consult [External references and chronology policy](EXTERNAL_REFERENCES.md) when using the fan wiki or linked D&D Beyond sheets. Wiki-supported spelling is evidence for orthography, not independent proof of audible dialogue. The character sheets are end-of-campaign snapshots, not episode-one builds. Do not introduce later developments into early-episode transcripts, dossiers or lore without a time-qualified, clearly marked spoiler section. Preserve raw ASR spellings and source URLs.

## Two owner-provided research sources (2026-10-21)

The user-supplied [episode numbering crosswalk](EPISODE_NUMBERING.md) documents the source's **original podcast numbers** separately from the **corrected archive IDs** already used in repository paths. **Archive path IDs always follow the corrected column-I spreadsheet labels**; do not blindly extrapolate from the original number, as numbered bonuses and *Inverse* episodes cause shifts.

The [owner episode notes](OWNER_EPISODE_NOTES.md) contain useful time-uncertain **owner interpretations/first-mention hypotheses** and **personal spellings**, not canonical or audio-verified language. Add a **user-note candidate** provenance class and preserve independent labels for **ASR**, **wiki spelling**, **GM-spelled term**, **audio-verified**, and **fan art**. Never silently normalize source dialogue to the owner's spelling. Owner notes may identify *where to listen* but do not satisfy the listening requirement.

## Discord and linked-document name provenance (2026-10-21)

Use [the Discord spelling register](../reports/DISCORD_SPELLING_2026-10-21.md) alongside this guide and the [consistency ledger](../world/CONSISTENCY_LEDGER.md). The archive attributes cast messages to participants but does **not** independently authenticate their accounts, and nobody listened to audio for that report. Use named source tiers: **creator-accepted spelling**, **cast-written form**, **creator GM outline**, **cast-posted handout**, **cast-shared recap**, **archived-link preview**, **fan inventory**, **ASR**, **wiki art** and **audio-verified**. Never conflate the tiers.

- **Accepted:** **Diontalus** is creator-authoritative on Jon's character and archive-owner approved. Use it in curated reference prose and future reader-edited orthography **with an explicit replacement/source log**; retain `Dion Talus`, `Deontalus`, `Diantalus`, `Diontalis` in alias/search records and original machine outputs. The in-world speaker and exact spoken words remain unverified until listening.
- **Written support with limits:** **Nash Maggard**, **Stanley Billings**, **Tietkalla** (historically cast-written; now a legacy alias for canonical **T'ietkalla** under D-044), **Teet**, **Slavetown**, **Talia**, **Tedna**, **Pentael Wise** and **The Eye of Groxl**. For this city's names, preserve both the map-backed form and the cast-written form for the same referent; **Tiat Cala** may be an ASR form but requires context matching. **The Eye of Groxl** is **now owner-confirmed as one and the same item** as the processed E053 `Eye of Grojil` and E054 `Eye of Groxel`; **Groxl** is the canonical item spelling. **In E067 specifically**, the owner separately confirms that **“god killer Grojil” directly means the Eye of Groxl**; `Grojil` is a pronunciation approximation. No separate entity should be inferred **from this phrase**. The Eye's alleged historical feats remain the spirit's testimony. Keep ASR forms searchable. See [D-034](DECISIONS.md). See [D-028](DECISIONS.md). **Pentael Wise** is not automatically fan `Pentelvice`.
- **Remain unresolved:** **Catoblepraithe/Catobelpraithe**, **Angel Ashi/Angelashi**, `P0D` capitalization and other conflicting creator/recap/fan spelling variants. Show variants and uncertainty instead of selecting an unsupported favorite. Cast-written **Hope** and **Vorel** do not certify their full expanded wiki names.
- **Campaign namespace:** Jon's **Inverse** GM outline and Kyle's **Delvers** guild PDF are **not Wastes sources**. An Inverse planning name is not proof a character was actually performed. Archived sheet preview titles are observations, not historical snapshots of character dialogue.
- **New recovered-source register (2026-10-27):** [additional Discord map/diary/guide spellings](../reports/DISCORD_NEW_SPELLING_2026-10-27.md) provide **Delvers** written-source `Aytmer`, `Lake Obsul`, `Ambermore`, `Mickle's Farm` and `Chaos-Phage`, with established `Atomer`, `Absul`, `Ambermoor` aliases. **Owner-confirmed, player-authoritative Wastes name:** Jon's illustrated poem gives **Valiir Or'Nath**, which the archive owner identifies as **Stanley Billings's original elven name**. These are **two names for one character**, not separate entities. Preserve the exact apostrophe and capital N; keep the established `Stanley Billings` slug and use his original name only where contextualized. **Owner-confirmed family spelling:** **Delit Or'Nath** (Stanley's father) and **Villa Or'Nath** (his family's home) share **Valiir Or'Nath**'s surname. Prefer apostrophized **Or'Nath** in new curated references. Retain older `Delit Ornath`, `Villa Ornath`, and first-name ASR variants as search aliases; preserve existing `villa-ornath.md` slug, original audio transcripts, direct quotations and archived comparison reports. The same map is now owner-confirmed as the definitive editorial orthography for **T'ietkalla**, **The Principal**, **Khaervilon**, **Moag Ferhain**, **Ubere Mtaris** and **The Principal's Lands**. Written canon does **not** authorize silent modification of preserved dialogue or a claim of audio verification; see [D-044](DECISIONS.md).

Do not change original SRTs or silently edit a generated transcript from this report. Existing reader-edition name-edit logs and repeatable builds remain authoritative for what was actually altered.

## Bonus Q&A / retrospective testimony policy (March 2019 Year One Q&A)

The [March 2019 Year One Q&A](../episodes/BONUS-2019-03.md) is original publisher **#55**, and must be **indexed as a separate bonus**, never as corrected **Wastes E055** (the next original **#56** maps to that corrected ID). Preserve the full source title and separate **bonus publication order** from **campaign-event chronology**.

For each claim, name its evidence type: **GM retrospective intent/setting clarification**, **player's interpretation or private character concept**, **possible/abandoned prep**, **unresolved in-world mystery**, **future plan/teaser**, **audience hypothetical**, **production process**, or **previously played event referenced**. GM testimony can clarify creation and hidden motives (e.g., **Buttons loved Stanley**, Beau's intended Arcanum rescue, Nash's engine-heart genesis) but **does not create a previously unplayed event or imply all characters knew it**. Character fan theories about P0D, divine afterlife or the Toyota host do not become canon unless affirmed by adequate evidence. Exact day/time claims in other filenames still need their own evidence. **For bonus filenames versus dates stated in the bonus dialogue, however, [D-033](DECISIONS.md) establishes that the filename is the public publication month/date**, distinct from recording and early member availability; this **limited convention does not apply to unrelated episode numbering or date metadata**.

Treat rare names in the **processed SRT** as **ASR hypotheses**, and carry forward confirmed **Diontalus** and **Eye of Groxl** while preserving the actual spoken/transcribed variant in source. The machine file is untouched and the Q&A has **not yet been audio-verified**. [Decision D-029](DECISIONS.md) and [review queue](REVIEW_QUEUE.md).

## Layered documentation and narrative synthesis (researched arcs)

The **source/research, reference, narrative, and editorial-control layers** now have different responsibilities. Follow [documentation architecture](DOCUMENTATION_ARCHITECTURE.md) and [migration checklist](CONSOLIDATION_CHECKLIST.md); the [Arc One](../narrative/ARC_ONE.md), [Arc Two](../narrative/ARC_TWO.md) and [consolidated Arc Three](../narrative/ARC_THREE.md) narratives are **interpretive, time-qualified stories** backed by existing episode dossiers, not an official transcript. Do not add another E###-batch recap to the root README or world portal. Each new reference entry should live under **one subject** and link to the already recorded episode time evidence.

For narrative prose, describe **observed events as events** but attribute **Kefeli/Monsoon/Nobiery/Soulbroker claims**, privately experienced memories and **retrospective Buttons motive** to their source. Put the main spoiler horizon near the top; do not repeatedly interrupt prose with identical ASR disclaimers. Keep arc-summary main text in-universe and focused on the narrative. Place episode numbers, timestamps, ASR uncertainties, spelling provenance and retrospective production commentary in Markdown footnotes attached to the relevant passage; preserve natural attribution of character claims and private experiences in the story itself. **No invented dialogue**, and no acceptance of an unplayed Q&A plan as though it occurred during E054 downtime. Save a frozen research copy before replacing major historical compendia, preserve known aliases and issue keys, and retest links and source references. [Decision D-030](DECISIONS.md).

For arc summaries, aim for **about 400 words per numbered chapter**, normally **350–450 words**, so chapters across the five arcs have comparable reading lengths. Count story prose only, excluding headings, footnotes, navigation and unnumbered prologues or epilogues. Add supported scene detail to shorter chapters and condense incidental mechanics or repetition in longer ones; do not invent events or add filler to meet the range. Preserve the eight-chapter structure and source footnotes. See the [chapter prose balance report](../reports/NARRATIVE_PROSE_BALANCE_2026-10-24.md).

## World reference prose — in-universe narrative with source notes (2026-10-24)

**Owner directive:** [World narrative style](WORLD_NARRATIVE_STYLE.md) applies by default to reader-facing `world/` subject histories, thematic setting descriptions and historical essays. The opening describes the subject **as first encountered**; the body traces meaningful developments in chronological arcs; the final narrative section reports **current in-world status**. Keep the main text free of **episode numbers, recording clocks, ASR/model uncertainties, research instructions and out-of-character review language**. Use the project's existing Markdown `[^note]` convention to attach provenance, transcript alternatives, caveats and source dossier links to the relevant passage. Footnote definitions appear after the final status **without creating a later narrative heading**.

Natural in-story attributions are mandatory where needed: “the Soulbroker claimed…” or “Stanley believed…” keeps contested knowledge contested. A polished story must never convert uncertain testimony, player/GM hypotheticals or late revelations into earlier witnessed facts. Preferred owner-approved spellings such as **Eltanfawr**, **Diontalus** and **Groxl** belong in the main prose; ASR alternatives belong in a footnote.

**Functional exceptions** include [Nash's phrase register](../world/characters/nash-spellcasting-phrases.md) and [Vorel's title register](../world/characters/vorel-titles.md), as well as indexes, source-keyed chronology/ledger, technical schema and redirect stubs when episode/cue metadata is integral to their purpose. Do not strip their source tables. This rule applies immediately to new writing; existing pages receive a **separate presentation pass** during the arc-oriented cleanup. No audio/source verification is inferred from style cleanup.

### Character-biography focus and balance (2026-10-24)

**Character profiles are not shortened copies of the arc narratives.** In the [world reference directive](WORLD_NARRATIVE_STYLE.md), biographies now prioritize **temperament, motivations, values, bonds, allegiances, abilities, private revelations, identity and lasting personal growth**. Describe the *impact* of a major event on a character, not its blow-by-blow mechanics; refer to the arc narrative and episode evidence in footnotes for the full plot.

The **350–450 words per chapter** recommendation above applies **only to arc-narrative chapters**. For major character profiles, begin with a flexible **150–300 main-prose words per substantive arc**, and review disproportionate sections relative to similarly important arcs (a section above roughly **2× the substantive-arc median** deserves editorial attention). These are diagnostic ranges, not requirements: one-appearance arcs may be short and genuine pivotal changes may deserve longer treatment. Do not manufacture motives, filler or arbitrary equal sections. Preserve nuanced moral decisions, relationships and evidence distinctions. [Character template](WORLD_REFERENCE_PAGE_TEMPLATE.md).

**Planned Races domain (D-046):** Add population-level studies of intelligent peoples (Lizardfolk, Tieflings, Lactids, Harlequinari and later evidence-backed candidates) in `world/races/` with a `world/RACES.md` directory. A race/culture profile describes supported society, appearance, customary practices, changing history and relations, not a condensed version of a single hero's journey or every combat involving a member. Keep individuals in Characters, non-intelligent specimens/monstrous forms in Creatures, and organizations in Factions. Apply the same in-universe prose, evidence-footnote and last-supported-status rules; distinguish one unusual individual from a race-wide property. The files are *planned*, not yet published. [Consolidation plan](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### Domain-specific subject focus and proportionality (2026-10-24)

**Extend the character-centered principle to every ordinary `world/` domain, using its own subject criteria** ([D-039](DECISIONS.md)). Place references should describe atmosphere, geography, inhabitants, social/political identity and change in the place; item/technology pages should describe origin, nature, custody, demonstrated versus claimed capabilities and changing significance; faction pages should explain aims, organization, leadership, alliances and influence; historical studies should explain causes, transformative developments and enduring consequences; thematic context should clarify world systems and competing accounts. Do **not** write abbreviated versions of every scene that happened near, involved or mentioned the subject.

**Balance sections of comparable importance within a given page**, especially when a long section is merely a recap of battles or travel. There is **no domain-wide word target** for places, artifacts, factions or history studies, and the character-only 150–300-word guidance does not transfer to them. Shorter developments may be genuinely short. A founding, destruction, transfer of power, transformation or major revelation can justify a larger section. Do not invent details or equalize by filler. Historical studies can close with **Lasting legacy** rather than Current status. Preserve in-universe perspective, exact source footnotes and distinct levels of evidence. [World narrative style](WORLD_NARRATIVE_STYLE.md) · [reference template](WORLD_REFERENCE_PAGE_TEMPLATE.md).

## Phase D — consistency questions and source-review triage

The [active consistency ledger](../world/CONSISTENCY_LEDGER.md) is a **current open/resolved index**; it is no longer a dumping ground for one table per new episode. The [review queue](REVIEW_QUEUE.md) is a **prioritized list of listening, handout, and provenance tasks**, not an archive of every past speculation. Preserve and consult the complete old [ledger](../research/legacy/2026-10-22/WORLD_CONSISTENCY_LEDGER.md) and [review queue](../research/legacy/2026-10-22/PROJECT_REVIEW_QUEUE.md) for exact old keys and timestamps. **An item absent from the shorter active lists was not thereby resolved.** After the E081 arc ending, the [newest preserved third-arc ledger/queue snapshots](../research/legacy/2026-10-22/README.md) contain the full E055–E081 issue rows and timestamps; the active files now group current questions by **topic or listening priority**. Consult the [consolidation report](../reports/THIRD_ARC_CONSOLIDATION_2026-10-22.md) before assuming a removed interim checkpoint was a substantive retcon.

Distinguish decisions confirmed **by owner/creator** (such as **Diontalus** and the singular **Eye of Groxl**), later **source-cutoff evidence** (such as Angelashi's E054 rescue), **listening-verified dialogue**, and **unverified lore/character testimony**. Retain aliases for searching, record editor/date/episode/time/source version when resolving a disputed cue, and do not alter an earlier character's point of knowledge on the basis of a later episode or retrospective Q&A. New E055+ findings should update existing subject pages/chronology first, and create a stable issue key only where genuine uncertainty remains. [D-032](DECISIONS.md).

## Named equipment and self-bestowed titles (2026-10-22)

When a participant **self-assigns a title or epithet**, preserve the **claim and its author** rather than converting it to a universally recognized office. Add each distinct title/variant to that character's **single subject-page register**, with **earliest known episode, approximate time/cue, exact wording if audio-supported, source-confidence tier**, and a note whether it is *self-proclaimed*, *spoken by a companion*, *granted by another authority* or *formally recognized*. Record repeat uses of an existing title only when they meaningfully change wording or status. A list of titles in a later introduction may be retrospective, not proof all titles existed in earlier episodes. In particular, maintain [Vorel's evolving register](../world/characters/vorel.md), distinguishing Bok Bok's **“Lizard King”** address in [E006](../episodes/E006.md), Vorel's stated intent in [E026](../episodes/E026.md), and his self-identification in [E028](../episodes/E028.md), before the later E036 declaration; see the [title audit](../reports/VOREL_TITLE_AUDIT_2026-10-23.md). Do not mistake Diptak's clan pledge for Vorel's own title.

For **unique weapons and artifacts**, record **identity separately from orthography, provenance and mechanics**. The archive owner considers **Mawstorm** likely for Vorel's E037 chainsaw-edged greatsword; processed sources recognize variants such as `Ma Storm`, `maw storm` and `moss storm`. Use **Mawstorm (provisional)** in active reference prose, preserve recognition aliases and original SRT bytes, and queue a creator-written handout/audio check before calling the spelling verified. The [June 2019 bonus](../episodes/BONUS-2019-06.md) did not independently name the sword and should never be cited as if it did.

Retrospective bonus discussion can explain character intentions, creator world-building and unplayed encounters; **do not place those statements into main-event chronology** without episode evidence. The **June bonus's spoken May** label and **public-publication June** filename describe **different stages**, not conflicting dates. The same rule applies to the **July filename versus spoken June recording** and to other bonuses ([D-033](DECISIONS.md)); exact spoken timings remain processed ASR pending audio checks.

## Nash's spellcasting phrases and rhymes (2026-10-23)

During Wastes episode review, capture **Nash's improvised casting phrases and rhymes** alongside the existing Vorel-title check. Keep the collection on the separate **[Nash spellcasting phrase register](../world/characters/nash-spellcasting-phrases.md)**, linked from his main profile. It is the single home for the growing phrase list; do not duplicate the table into the character biography or episode summaries.

For each distinct phrase or meaningful variant, record **corrected season/episode, approximate recording clock and cue IDs, wording supported by the source, spell/ability or item when identifiable, performer/character attribution, exact source links and confidence**. Preserve incomplete rhymes, interruptions, companion-supplied endings and conflicting ASR readings. Use earliest **located** evidence without claiming an exhaustive first occurrence. Distinguish **performed/attempted magic**, **item activation**, **proposed or rejected wording**, and **retrospective recollection**; rhyming does not establish a successful spell or a fixed verbal-component rule. Leave original SRTs unchanged, and call words audio-verified only after listening. Keep later-season examples visibly separated from the main profile's spoiler horizon. **Maintain the phrase register in episode/time order regardless of NSP discovery-ID order. Add qualifying findings as one row in the existing chronological table; never prepend a standalone episode section. Use the same four fields (ID/episode/clock; ASR wording; performance status/context; linked P/Q evidence, cues and disputes). Put episodes with no new phrase in the compact negative-review table, and non-casting poems/proposals/retrospectives in their own table. Update coverage counts and preserve stable IDs, references, wording uncertainties and audio-verification labels.** Older episodes remain a bounded backfill task in the [review queue](REVIEW_QUEUE.md#nashs-spellcasting-phrase-register).

## Separate campaign realities — Inverse versus The Wastes (2026-10-22)

**The Jon Jagger–run *Inverse* adventure is a different fictional continuity from Beau's *The Wastes*.** Shared podcast performers, use of D&D, similar-sounding magic or monsters, and discussion in the same bonus recording **do not establish shared lore, geography or a timeline**. The Inverse GM calls its own constructed refuge **Inverse**, with a barrier separating it from its own **human world** and the **Anathema**. Do not identify that human world with **Wastes Earth**, nor treat flux, waystations or Eventide Assembly as CHIDS/Scorching/Traversal Drive equivalents without explicit authoritative evidence.

**File and reference separation:** Research **Inverse S1E01** at [inverse/episodes/S1E01.md](../inverse/episodes/S1E01.md) and future episodes in the **inverse/** directory, with [inverse/README.md](../inverse/README.md) as the campaign portal. The unprefixed corrected episode IDs (E000–E081) and [Wastes chronology](../world/CHRONOLOGY.md) remain **exclusively The Wastes**. Do not append Inverse person/place/technology references to Wastes world indexes. Avoid cross-links except for **clearly labeled editorial/comparative references** or out-of-character Q&A provenance.

**Evidence tiers:** The Inverse GM's opening premise, observed Inverse events, an Inverse NPC's explanation, out-of-character retrospective comments, and processed-ASR spelling guesses are **distinct**. For example, Zia Rosewood's claim that unbranded humans sabotaged the waystation is not direct sabotage evidence; a witnessed giant **flux** rift and shipwreck are. The premiere **does not** resolve the waystation's malfunction or identify the missing engineer's fate. No later *Inverse* episode, Wastes wiki or end-era character sheet should be silently used to write the first-episode dossier.

**Migration discipline:** No new global world index that mixes two fictional realities. If a future creator source explicitly describes a crossover, document the **source and the precise extent of the connection**, rather than retrospectively merging campaigns.

## Delvers presentation scope (2026-10-24)

The revised world-reference and narrative direction applies equally to `delvers/world/` and `delvers/narrative/`: [campaign-specific application](WORLD_NARRATIVE_STYLE.md#delvers-world-and-narrative). Reference prose explains its subject; narrative prose follows the story. Use in-universe prose and source footnotes in both, with the researched horizon in a note. Preserve Delvers-only chronology, private knowledge and attributed testimony. Functional indexes and research ledgers keep essential source metadata. Ongoing fragments do not require completed-arc chapter counts or padding.
