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

- `Dust Hill` is the provisional editorial spelling (`Dusthill` occurs as an ASR variant).
- `Nash Maggard` is provisional; variants `Magard`, `Maghard` appear in transcripts.
- `Hope` is an explicitly preferred short name for the tiefling. Full name transcribed `Orifi`/`Orify` is **not spelling-verified**.
- `Vorel` is provisional; multiple spellings occur. The longer introduction name is uncertain and requires checking.
- A person identified as `Shun T` (well attendant) and `Gimster` (head mechanic) require spelling verification.
- `Bo` and `Beau` refer to the same presenter/DM in the supplied transcripts; verify preferred written rendering before canonicalizing publication metadata.

## World-building safeguards

- The character's *plan to travel back and change history* is a stated goal, not proof that time travel is possible.
- A character's claimed origin or background can be an unreliable narrator's account.
- A statement about a feature of Dust Hill may conflict with incidental player banter (e.g. mention of a tavern; DM later says there is no tavern). Record it as an issue, not a settled fact.
- D&D rules discussion is meta-play, not automatically an in-world rule.
