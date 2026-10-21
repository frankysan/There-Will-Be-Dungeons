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

## Name rules

- `Dusthill` is the wiki-supported written form; `Dust Hill` is an ASR/search alias.
- `Nash Maggard` is wiki-supported; `Magard`, `Maghard` are preserved ASR variants.
- `Oriphi “Hope” Akmenos` is documented by the wiki. The name-pronunciation exchange with ASR `Orifi`/`Orify` remains unchanged until an audio listening review; Hope is the preferred short name.
- `Vorel Rasvim Kurik` is wiki-supported; multiple recognition variants remain aliases and require listening for phonetic fidelity.
- `Shun'ti Stoutbarrel` and `Jimster` are wiki-supported by **later** episode material. For E001, edit the name spelling only; never insert the later-disclosed surname into dialogue that lacks it.
- `Beau` is the established DM name in external credits; `Bo` may occur in ASR speech. `Jon Jagger` is wiki-supported and labelled `John` in the source ASR, so reader editions use `Jon`.

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
- **Written support with limits:** **Nash Maggard**, **Stanley Billings**, **Tietkalla**, **Teet**, **Slavetown**, **Talia**, **Tedna**, **Pentael Wise** and **The Eye of Groxl**. For **Tietkalla**, use the cast-backed spelling as a candidate for the relevant entity only; **Tiat Cala** may be an ASR form but requires context matching. **The Eye of Groxl** is **now owner-confirmed as one and the same item** as the processed E053 `Eye of Grojil` and E054 `Eye of Groxel`; **Groxl** is the canonical item spelling. The **identity of a separately named deity or legendary warrior** cannot be inferred solely from that item confirmation. Keep ASR forms searchable. See [D-028](DECISIONS.md). **Pentael Wise** is not automatically fan `Pentelvice`.
- **Remain unresolved:** **Catoblepraithe/Catobelpraithe**, **Angel Ashi/Angelashi**, `P0D` capitalization and other conflicting creator/recap/fan spelling variants. Show variants and uncertainty instead of selecting an unsupported favorite. Cast-written **Hope** and **Vorel** do not certify their full expanded wiki names.
- **Campaign namespace:** Jon's **Inverse** GM outline and Kyle's **Delvers** guild PDF are **not Wastes sources**. An Inverse planning name is not proof a character was actually performed. Archived sheet preview titles are observations, not historical snapshots of character dialogue.

Do not change original SRTs or silently edit a generated transcript from this report. Existing reader-edition name-edit logs and repeatable builds remain authoritative for what was actually altered.

## Bonus Q&A / retrospective testimony policy (March 2019 Year One Q&A)

The [March 2019 Year One Q&A](../episodes/BONUS-2019-03.md) is original publisher **#55**, and must be **indexed as a separate bonus**, never as corrected **Wastes E055** (the next original **#56** maps to that corrected ID). Preserve the full source title and separate **bonus publication order** from **campaign-event chronology**.

For each claim, name its evidence type: **GM retrospective intent/setting clarification**, **player's interpretation or private character concept**, **possible/abandoned prep**, **unresolved in-world mystery**, **future plan/teaser**, **audience hypothetical**, **production process**, or **previously played event referenced**. GM testimony can clarify creation and hidden motives (e.g., **Buttons loved Stanley**, Beau's intended Arcanum rescue, Nash's engine-heart genesis) but **does not create a previously unplayed event or imply all characters knew it**. Character fan theories about P0D, divine afterlife or the Toyota host do not become canon unless affirmed by adequate evidence. Date/location claims in filenames need independent release-date validation for a chronological publication catalog.

Treat rare names in the **processed SRT** as **ASR hypotheses**, and carry forward confirmed **Diontalus** and **Eye of Groxl** while preserving the actual spoken/transcribed variant in source. The machine file is untouched and the Q&A has **not yet been audio-verified**. [Decision D-029](DECISIONS.md) and [review queue](REVIEW_QUEUE.md).
