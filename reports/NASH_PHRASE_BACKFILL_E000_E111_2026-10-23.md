# Nash's spellcasting phrases — E000–E111 discovery pass

**Date:** 2026-10-23. **Continuity:** The Wastes, Season 1, corrected archive order. **Hard ceiling: E111.** **Result:** 25 entries added to the [separate phrase register](../world/characters/nash-spellcasting-phrases.md), with exact recording clocks, cue references, spell/ability context and competing ASR readings. **Text-only, ASR-provisional; no listening or exhaustive full-episode review.**

## Scope, inputs and preservation

The search began with **E000** and proceeded forward through **E111**, including **E013.5 Supplemental** and its alternate copy. The [JSON evidence inventory](NASH_PHRASE_BACKFILL_E000_E111_2026-10-23.json) records **228 source exports across 113 corrected archive IDs**, their exact paths, filename model labels, cue counts, final cue-end times and SHA-256 hashes. These are export counts, not 228 independent recordings. Original publisher numbers were not substituted for archive IDs.

The files were read through the direct local checkout, starting HEAD `379bee3094466b07a14bb177d222b337a4b0926d`. Concurrent E111 work advanced the shared checkout to `6a15ecc07a038fb61905334f44f2f2c57ab944c6` before these edits were applied. Its **NSP-015 / E111 dragon rhyme** and the earlier register IDs were preserved. This pass adds **NSP-016 through NSP-040**, sorted into recording order without renumbering earlier entries. The collection now has **40 entries**, **37 within the ceiling** and **three prior later-season seeds**. Those prior seeds and the existing roundup note were retained; **no source after E111 was opened for this pass**.

Both **`.parakeet.processed.srt`** and **`.qwen-q8.canary-ctc.nemotron.srt`** exports were available within this inventory. Their names identify pipeline labels, not verified model versions or independent recording provenance. Audio files were not opened, listened to or associated with a particular export. No original SRT/audio was edited.

## Search and review method

The discovery view parsed SRT cue text in recording order, preserving cue IDs, recording-clock timestamps and performer/diarizer labels. Temporary reading views joined adjacent turns while retaining label changes; original files remained unchanged.

1. Starting at the opening episodes, search spell names, casting descriptions and Scott's labelled turns. In later episodes, numeric speaker IDs were treated as local hypotheses, not a global Scott mapping.
2. Search Parakeet exports in ascending episode order for **rhyme, magic-word and incantation language**, plus speech cues such as **“I say,” “and say,” “I shout,” “I yell,” “I mutter,” “I chant” and “I whisper.”** For generic speech cues, use nearby spell/casting text within approximately **90 seconds** as a discovery filter; strong rhyme/magic-word hits need no proximity match. Inspect selected surrounding turns to identify the caster and action.
3. Perform a secondary motif search across **both exports** for `hocus`, `pocus`, `abracad`, `alakaz`, `bipp`, `bibb`, `presto`, `rhym`, `poem`, and spell/words co-occurrence. This recovered additional candidates where Parakeet's wording differed, including the E100 Haste poem, E101 failed minotaur rhyme and E110 Chromatic Orb verse.
4. Compare each added entry's passage against the matching second export. Extend the context when needed to distinguish the declared spell from a finishing description, an NPC's line, or another character's magic. Record differences rather than select a polished reconstruction.

**Limits:** This is keyword discovery and contextual selected-passage comparison, not full reading of every recording through its outro. Search misses do not establish absence. Agreement between exports does not prove words or speaker identity. Cue-split phrases, unexpected spell wording, diarization errors and ASR deletions can still hide additional items. No full-export edit-distance comparison or audio-accuracy measurement was made for this task.

## Additions in recording order

The register owns the phrase text and detailed evidence; this table identifies the newly populated material without duplicating the full collection.

| Corrected recording | New entry IDs | What was captured |
| --- | --- | --- |
| **E015** | NSP-016–017 | Short Enlarge casting word; Nash's changing magic-word coaching while the NPC speaks and Nash casts |
| **E022** | NSP-018 | Named song/cane performance accompanying Sleep; no imported or invented lyrics |
| **E025** | NSP-019 | Spoken flourish before dragon transformation, distinguished from required spell words |
| **E044** | NSP-020 | Rocks rhyme while closing the camp entrance |
| **E047** | NSP-021 | All/wall rhyme while moving earth aside |
| **E049** | NSP-022 | Dig/big rhyme for enlarging Vorel during the Podzilla fight |
| **E056** | NSP-023–024 | Filler/George Miller finishing verse; rushed/crushed diamond-pulverizing verse |
| **E061** | NSP-025 | Peanuts/feet/sleep verse against two guards |
| **E063** | NSP-026 | Hurt/dirt verse while creating screening rooms |
| **E064** | NSP-027–028 | Distinct hurt/dirt and came/flame verses for two separate castings |
| **E070** | NSP-029 | Tatters/matters verse for Enlarge |
| **E071** | NSP-030 | Told/cold verse for Ray of Frost |
| **E075** | NSP-031 | Moby/Toby finishing verse; conflicting following spell-name transcription retained |
| **E076** | NSP-032 | Whore/door verse for Dimension Door |
| **E095** | NSP-033 | Abandoned teleport-scroll rhyme, with unfinished alternatives retained |
| **E098** | NSP-034–035 | Caper/paper and high/guy scroll verse; dragon-voice Banishment verse |
| **E100** | NSP-036, NSP-038 | There/underwear Fireball verse; taste/haste poem |
| **E101** | NSP-039 | Failed minotaur rhyme alongside a cold Chromatic Orb hit |
| **E104** | NSP-037 | Scary/Larry Reduce verse, introduced as spoken in Draconic |
| **E110** | NSP-040 | Chromatic Orb verse and the table's discussion of its interrupted rhyme |

The first new lexical casting word located in this pass is **E015's Enlarge shout**. That is **earliest located by this search**, not a certified first use. Early scenes include gesture and sound-effect descriptions, such as **E002 ~00:28:22** and **E005 ~01:26:11**; these need listening before treating an ASR `Whoop` / `U h` as intelligible spell words. Generic declarations, dice-rolling banter and threats to cast a spell were not automatically added.

## Attribution and scope exclusions

- **E000** is introductory narration, not a played Nash casting sequence. **E013.5** supplies Stanley's recap and a Hope–Vorel scene while Nash is absent; recap references to his magic do not establish new spoken phrases.
- **E019 ~00:16:43–00:17:11:** the no-thumbs/feet insult accompanies **Stanley's Vicious Mockery**; Nash's wish that it rhymed does not make the insult his.
- **E043** is the alternate-setting holiday one-shot. Scott is absent as a player; Beau's character's magic is not Nash's spellcasting.
- **E044's earlier songs** are Vorel's performance, distinct from Nash's late-episode rocks verse. **E045's George eulogy** is not automatically a casting incantation.
- **E056's George verse** has a 0 → 5 → 0 diarizer transition in both exports. The surrounding declaration, Dexterity save and 8d6 discussion identify **Fireball**; attribution of the second rhyming line still needs listening. It must not be silently assigned to either Scott or a helpful companion.
- **E100's Haste introduction:** Qwen separates a companion's **“I like poems”** from Nash's verse, while Parakeet folds it into one labelled turn. Preserve the distinction.
- **E105 ~02:04:43–02:05:01:** the glove/love/above rhyme accompanies **Vorel's gauntlet use**, not Nash. Nash's earlier rejected fly/stealth proposal stays in its existing separate classification.
- **E106's portal poem** is supplied by Badass T and read by **Stanley**; Nash participates by eating the required plant. It is not an improvised Nash verse. **E107–E109** follow different characters in the Dunebreaker prequel; their rhyming recaps are not Nash's magic.

## Listening and continuation

Prioritize the bounded wording and attribution checks already attached to each row, especially **E044 ~02:43:26–02:43:39**, **E047 ~02:18:55–02:19:14**, **E056 ~01:48:47–01:49:03**, **E095 ~02:29:01–02:29:31**, **E098 ~02:18:39–02:18:50**, **E101 ~00:19:50–00:19:59**, and **E104 ~01:44:45–01:44:59**. The existing E111 ingredient disagreement remains open.

The keyword-discovery pass has reached **E111**. For deeper recovery, resume sequential reading at **E001**, with a **hard stop at E111**; do not treat the search inventory as completed full-episode coverage. This phrase work does not advance the separate full-episode or ASR-comparison research queues. [Active phrase-review task](../project/REVIEW_QUEUE.md#nashs-spellcasting-phrase-register).
