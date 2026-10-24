# Decisions and rationale

Decisions marked **provisional** remain open to revision after listening tests.

| ID | Status | Decision | Why / evidence |
|---|---|---|---|
| D-001 | Agreed | Primary deliverable is human-readable transcripts for all episodes | Project goal; 1,000+ hours of primarily English audio |
| D-002 | Agreed | E000 and E001 are the first end-to-end milestone | Demonstrates short and long episode handling |
| D-003 | Provisional | Use Parakeet TDT 1.1B for initial readable transcript drafts | Faster than Qwen on user's hardware; appeared to preserve speech missing from Cohere |
| D-004 | Provisional | Use Qwen3-ASR 1.7B Q8 for difficult-passage comparison | Q8 notably faster than F16 in user testing; comparable draft coverage |
| D-005 | Confirmed | Do not use tested Cohere run as primary output | Listener verified it skips substantial speech |
| D-006 | Confirmed, per E001 | Merge numeric speaker 5 into Scott for reader-facing transcripts | Listener identified Scott doing a voice; source files stay unchanged |
| D-007 | Confirmed | E000 ends with spoken “Now”; remaining audio is music | Listener confirmation; raw and processed Parakeet timing differs |
| D-008 | Agreed | Keep original output files and explicit post-processing status | Model results changed across runs; reversibility and auditability matter |
| D-009 | Agreed | Separate speaker, role, and in-world identity | Same person can narrate, play a character, or perform an NPC voice |
| D-010 | Agreed | Keep source-cited world, character and location reference docs | Prevent later spellings and plot details from drifting |
| D-011 | Pilot implementation | Drafts use the available post-processed Parakeet text, reflowed but not corrected | Already readable punctuation and speaker names; retained raw for comparison |
| D-012 | Deferred | Choose final archival model by audio-grounded accuracy benchmark | Agreement among models is not a reference WER |
| D-013 | Provisional | Test Q4 + Canary CTC as a timing configuration | E001 invalid cues 56→0 and overlaps 19→1, while text stays identical |
| D-014 | Agreed | Keep alignment and speaker-quality decisions separate | E001 924/32,007 word positions have different speaker IDs between Q4 and Q4+Canary despite same text |
| D-015 | Deferred | Compare Qwen Q4 and Q8 against audio before choosing quantization | E001 differs by 1,070 token edits; Q8 has 237 more tokens, neither proves accuracy |

| D-016 | Agreed | Create reproducible *reader-edited* transcripts separately from generated machine drafts | Proper-name spelling improvements must not alter raw recognition data or get overwritten by the next build |
| D-017 | Agreed | Normalize documented names with per-turn edit logs and episode timestamps | Fan-wiki spellings are external orthography evidence, not word-by-word audio verification |
| D-018 | Agreed | Prefer cast label Jon in reader editions; retain John in original output | Wiki identifies Jon Jagger; speaker identities were already established by the pilot |
| D-019 | Agreed | Preserve the “Orifi or Orify?” name discussion pending audio check | Replacing both alternatives would erase actual pronunciation uncertainty |

| D-020 | Provisional | Retain no-explicit-VAD/no-chunk Parakeet as the E001 recognition baseline | Default VAD plausibly omits the greeting; 700 ms padding creates a boundary duplicate; chunked output loses other brief responses. No audio-grounded ranking yet. [Evidence](../reports/PARAKEET_SEGMENTATION_2026-10-21.md) |
| D-021 | Experimental result | Don't attribute the chunked missing greetings to LCS deduplication | 30 s chunks/3 s overlap with LCS auto vs off yielded identical JSON and SRT byte-for-byte. [Evidence](../reports/PARAKEET_SEGMENTATION_2026-10-21.md) |

## Decision changes

| ID | Status | Decision | Why / evidence |
|---|---|---|---|
| D-022 | Experimental implementation, 2026-10-21 | Compare primary Parakeet and independent Qwen Q8 with time-constrained anchors and bounded edit alignment | Preserves possible omissions and scales to multi-hour exported transcripts; [implementation and limits](../reports/MULTIPASS_PIPELINE.md) |
| D-023 | Implemented safeguard, 2026-10-21 | Keep original runs, source timing precision, alternatives and explicit reviewer decisions; no automatic transcript reconciliation | Agreement/majority and confidence do not establish audible speech; SRT cues do not supply word timing |
| D-024 | Evaluation pending, 2026-10-21 | Generate bounded targeted jobs and import third passes as additional evidence | A listening reference and independent deletion/insertion/substitution measures are required before claiming improved accuracy; [export pilot](../reports/MULTIPASS_PILOT_2026-10-21.md) |
| D-025 | Execution/import verified, 2026-10-21 | Retain the first real 29.640 s Parakeet clip as an additional unreviewed run | Original audio hash matched; 101 words imported with explicit clip offset; all prior runs, alignments and 971 candidate IDs preserved. Wording decisions remain pending listening. [Evidence](../reports/TARGETED_VERIFICATION_2026-10-21.md) |

When changing a decision, append a dated entry with reasons and affected episodes. Do not erase the original rationale; instead mark it superseded.

## Written-name evidence decisions (2026-10-21)

| ID | Status | Decision | Why / evidence |
|---|---|---|---|
| D-026 | **Accepted canonical spelling, 2026-10-21** | **Diontalus** is the curated project display spelling; keep `Dion Talus`, `Deontalus`, `Diantalus` and `Diontalis` as source/search aliases | Two Jon cast messages spell his own character **Diontalus**; the archive owner explicitly accepted creator authority for this spelling. [Discord report](../reports/DISCORD_SPELLING_2026-10-21.md). **This does not audio-verify any dialogue or certify the character's statements**. |
| D-027 | **Agreed provenance policy, 2026-10-21** | Keep **cast-written, creator-document, cast-posted handout, cast-shared recap, archived-link preview and fan inventory** distinct, and assign **Inverse** / **Delvers** references to those campaigns rather than **The Wastes** | [Discord report](../reports/DISCORD_SPELLING_2026-10-21.md) records source disagreements. **Tietkalla** is cast-supported, while **Catoblepraithe/Catobelpraithe**, **Angel Ashi/Angelashi** and other variants are still unresolved; orthography does not prove identity or chronology. |
| D-028 | **Owner-confirmed canonical item identity, 2026-10-21** | **Eye of Groxl** is the canonical display name for **one artifact**, also called `Eye of Grojil` in E053 processed ASR and `Eye of Groxel` in E054 processed ASR. Retain variants as source/search aliases; do **not** split them into separate items | **Archive owner explicitly confirmed** the variant names refer to **one item**, with **Groxl canonical**; this resolves the earlier cross-source uncertainty. Kyle's cast-written [Discord item title](../reports/DISCORD_SPELLING_2026-10-21.md) corroborates the spelling. The confirmation **does not independently identify every potentially separate deity or legendary warrior reference**, and **does not count as audio verification**. **E067's particular “god killer Grojil” occurrence is explicitly identified as the Eye of Groxl by later owner clarification ([D-034](#owner-clarifications-2026-10-22)); it is not such a separate referent.** Affects [E053](../episodes/E053.md), [E054](../episodes/E054.md) and [ledger](../world/CONSISTENCY_LEDGER.md). |

## Bonus episode curation decisions (2026-10-21)

| ID | Status | Decision | Why / evidence |
|---|---|---|---|
| D-029 | **Agreed, 2026-10-21** | Index **March 2019 The Year One Q&A!** as **BONUS-2019-03**, separate from Wastes E###. Original publisher **55** is a bonus, and original **56** becomes corrected **E055**. Treat bonus claims as **retrospective GM/player testimony, plans or speculation** according to provenance, not automatic played scenes | The archive's [episode crosswalk](EPISODE_NUMBERING.md) explicitly excludes the Q&A from main-story numbering. The [bonus dossier](../episodes/BONUS-2019-03.md) records valuable GM clarification (**Buttons/Stanley motives**, **Order 26**, **Nash's heart**) alongside **unplayed alternate routes, audience hypotheticals and future plans**. Keep old character knowledge/cutoffs intact; no audio verification was performed. |

## Reference and narrative consolidation decisions (2026-10-21)

| ID | Status | Decision | Why / evidence |
|---|---|---|---|
| D-030 | **Agreed; Phase A implemented, 2026-10-21** | Adopt **four layers**: immutable source/research dossiers, **subject-focused world reference**, **arc-oriented narrative**, and editorial controls. **Preserve legacy append-only indexes** in `research/legacy/` and keep source-time uncertainties/retrospective Q&A distinct. Introduce the narrative now split into [Arc One](../narrative/ARC_ONE.md) and [Arc Two](../narrative/ARC_TWO.md), a [short project index](../README.md), [world portal](../world/README.md), [architecture](DOCUMENTATION_ARCHITECTURE.md) and [tracked phased migration](CONSOLIDATION_CHECKLIST.md) | The first 54 played episodes and Year One Q&A have produced valuable but **repetitive, batch-organized appendices**. A narrative account and deduplicated reference pages serve different reading tasks. Prior research remains accessible through archived indexes, original dossiers and Git history. **This decision does not claim Phases B–D or audio verification are complete**. |

## Phase C world-reference consolidation (2026-10-22)

| ID | Status | Decision | Reason and evidence |
|---|---|---|---|
| D-031 | **Implemented, first editorial pass, 2026-10-22** | Replace append-only `world/WORLD.md` with a **thematic setting guide** and `world/CHRONOLOGY.md` with **one continuous corrected Arcs One–Two timeline** (E001–E054 excluding standalone E043; E000 as introduction). Keep **E013.5** at its earlier story-time position despite its release between E013 and E014. The March Year One Q&A remains a **non-narrative bonus** | Long-form original [world history](../research/legacy/2026-10-22/WORLD_HISTORY.md) and [chronology](../research/legacy/2026-10-22/WORLD_CHRONOLOGY.md) were preserved **before** rewriting. The new structure separates **GM setting exposition, direct episode events, interested NPC testimony and later creator explanation**, with individual dossiers retaining timed evidence. **Phase D ledger migration and all audio checks remain pending**. [Architecture](DOCUMENTATION_ARCHITECTURE.md) · [checklist](CONSOLIDATION_CHECKLIST.md) |

## Phase D consistency-ledger and review triage (2026-10-22)

| ID | Status | Decision | Rationale and scope |
|---|---|---|---|
| D-032 | **Implemented as structural first pass, 2026-10-22** | Use the [active consistency ledger](../world/CONSISTENCY_LEDGER.md) to distinguish **genuinely open uncertainty** from **owner/creator resolutions and later episode-cutoff resolutions**. Use a [prioritized review queue](REVIEW_QUEUE.md) for actionable listening/handout work. Preserve complete historical [consistency](../research/legacy/2026-10-22/WORLD_CONSISTENCY_LEDGER.md) and [review queue](../research/legacy/2026-10-22/PROJECT_REVIEW_QUEUE.md) documents before replacement. | Original append-only registers exceed 170k characters and contain older unsettled statuses alongside later resolutions (e.g., Angelashi alive, Tedna/P0D dead, froghemoth divided, Groxl spelling owner-confirmed). **None of this structural cleanup audio-verifies the processed ASR or closes omitted archival questions.** [Architecture](DOCUMENTATION_ARCHITECTURE.md) · [checklist](CONSOLIDATION_CHECKLIST.md) |

## Owner clarifications (2026-10-22)

Current narrative numbering also follows the later [owner-approved E026/E027 split](#narrative-arc-split-and-renumbering-2026-10-23); original episode and source-publication identifiers are unchanged.

| ID | Status | Decision | Evidence and effect |
|---|---|---|---|
| D-033 | **Owner-confirmed archive convention, 2026-10-22** | For **bonus episodes**, a difference between the **archive filename date/month and a date stated in the recording** arises because the **filename reflects public publication**, **not the recording date or private-member publication date**. **This clarification applies only to such bonus filename-versus-spoken-date comparisons, not to other episode or spreadsheet date metadata**. Record each separately: (1) public-release date or month from the basename; (2) spoken recording date when stated; (3) member-release/early-access timing when supported. A bonus named `2019-06` can legitimately be called **May's show** in the recording, and `2019-07` can be called **June's show**. This is **not a contradictory filename**. | The archive owner explicitly clarified the general naming rule. The opening dialogue and description of early supporter access remain **processed-ASR observations** until audio verified, and filenames with only a month do **not establish a precise day/time**. Applies to [bonus numbering](EPISODE_NUMBERING.md), [April](../episodes/BONUS-2019-04.md), [June](../episodes/BONUS-2019-06.md), [July](../episodes/BONUS-2019-07.md), and all later bonus dossiers. |
| D-034 | **Owner-confirmed referent, 2026-10-22** | In **E067**, the dragon's **“god killer Grojil”** means **the Eye of Groxl itself**, not a separately introduced deity, warrior, other object, or unresolved person. **Groxl** is the correct name; **Grojil** is an ASR approximation of its pronunciation. Normalize editorial reference prose to **Eye of Groxl** and retain `Grojil` only as a searchable source/ASR variant, explicitly linked to the Eye. | The archive owner directly identified the E067 referent. Supplements **[D-028](#written-name-evidence-decisions-2026-10-21)** and resolves the previous E067 referent question in [E067](../episodes/E067.md), [Vorel](../world/characters/vorel.md), [world](../world/WORLD.md), [chronology](../world/CHRONOLOGY.md), [ledger](../world/CONSISTENCY_LEDGER.md) and [review queue](REVIEW_QUEUE.md). This **does not audio-verify** the spirit's exact words, or independently prove the Eye's alleged historical god-killing deeds or rules/mechanics. |

## Narrative arc split and renumbering (2026-10-23)

| ID | Status | Decision | Evidence and effect |
| --- | --- | --- | --- |
| D-035 | **Owner-approved and implemented, 2026-10-23** | Split the former E000–E054 narrative after **E026**: [Arc One](../narrative/ARC_ONE.md) is **E000–E026 plus E013.5**; [Arc Two](../narrative/ARC_TWO.md) is **E027–E054 excluding standalone E043**. Former Arcs Two, Three and Four become [Three](../narrative/ARC_THREE.md), [Four](../narrative/ARC_FOUR.md) and [Five](../narrative/ARC_FIVE.md). Keep narrative changes limited to those needed for the split. | E026 ends at the Liberators with the **Heroes of the Wastes** naming and a wider mission; E027 begins the next road sequence. The owner accepted this transition and requested project-wide renumbering. **E101 still spans two arcs**, now Four/Five, at Hope's departure. Original episode numbers, cast/source titles, historical issue IDs and existing snapshots stay unchanged. [Migration report](../reports/ARC_SPLIT_2026-10-23.md) and [pre-split narrative](../research/legacy/2026-10-23/ARC_ONE_PRE_SPLIT.md). No new audio verification. |

## Owner-confirmed mask display spelling (2026-10-24)

| ID | Status | Decision | Evidence and effect |
| --- | --- | --- | --- |
| D-036 | **Owner-selected preferred spelling, 2026-10-24** | Use **Mask of Eltanfawr** as the canonical reference display and slug, for the single jewel-studded mask discovered in E118 and worn in E126. Retain **“Mask of Elton IV,” “Elton Four,” “Eltenvor”** as discoverable transcription aliases. The historical [mask-of-elton-iv.md](../world/technology/mask-of-elton-iv.md) path becomes a stable **compatibility reference**, and [mask-of-eltanfawr.md](../world/technology/mask-of-eltanfawr.md) is the canonical subject page. | The archive owner explicitly selected **Eltanfawr**. Qwen's E126 export also represents this rendering while other ASR drafts do not; **the editorial spelling choice does not constitute listening, proof of spoken pronunciation or verification of the original GM item card**. Do not alter immutable E118/E126 episode transcription evidence, interpret these as separate items, or imply Stanley has completed its four-night attunement at E128. [E118](../episodes/E118.md) · [E126](../episodes/E126.md) · [migration manifest](WORLD_ARC_MIGRATION_MANIFEST.md). |

## In-universe world-reference presentation (2026-10-24)

| ID | Status | Decision | Rationale and scope |
| --- | --- | --- | --- |
| D-037 | **Owner-directed editorial policy, accepted 2026-10-24** | For ordinary reader-facing `world/` articles, use **in-universe, narrative-focused main prose**: introduce the subject as first known, follow changes by arc, and end with current status. **Episode numbers/ranges, timestamps, transcription uncertainty, name variants and review/citation apparatus belong in linked Markdown footnotes**, not the main text. Maintain true in-story uncertainty through natural attribution. **Nash's spellcasting phrases and Vorel's titles** are explicit source-register exceptions, as are functional ledgers, chronologies, technical schemas and navigation/compatibility pages when metadata is essential. | The archive owner explicitly requested a fictional-world reading experience without ASR/episode noise in the main body, while preserving research transparency. [World narrative style](WORLD_NARRATIVE_STYLE.md) is the binding detailed directive, supported by the [page template](WORLD_REFERENCE_PAGE_TEMPLATE.md), [editorial guide](EDITORIAL_GUIDE.md) and [migration plan](WORLD_ARC_CLEANUP_PLAN.md). The three existing structural pilots **Nash, Elhandar and Eltanfawr** now require subsequent **presentation-only passes** to comply; no claim is made that the current `world/` has already been rewritten or audio-verified. |

## Character biography emphasis and proportion (2026-10-24)

| ID | Status | Decision | Rationale and application |
| --- | --- | --- | --- |
| D-038 | **Owner-directed editorial policy, accepted 2026-10-24** | Character pages are **character studies**, not shortened arc recaps. Give primary attention to **personality, traits, motivations, values, relationships, changing allegiances, abilities, identity revelations and lasting personal development**. Maintain a **reasonably balanced amount of prose between similarly substantive arcs**, drawing on the narrative chapter rebalancing practice but using **character-specific, flexible proportions** rather than the same chapter word budget. Treat battles, journeys and episode actions as examples of character traits or changes, not independent recap obligations. | The [World narrative style](WORLD_NARRATIVE_STYLE.md), [reference template](WORLD_REFERENCE_PAGE_TEMPLATE.md) and [editorial guide](EDITORIAL_GUIDE.md) now provide a soft 150–300 main-prose word starting range per substantive arc for major recurring characters, with an editorial review if an arc is roughly more than twice the median of similarly substantive arcs. Short minor arcs and extended pivotal transformations are justified exceptions; **no padding, invented psychology or loss of meaningful nuance**. Nash's current Arc Five has around 1,050 prose words versus roughly 80–240 for its other arcs and is a **candidate for later, separately archived character-centered rebalancing**. Source footnotes, chronology boundaries and specialist-register exceptions from D-037 remain in force. |

## Subject-first world reference prose across domains (2026-10-24)

| ID | Status | Decision | Rationale and application |
| --- | --- | --- | --- |
| D-039 | **Owner-directed editorial policy, accepted 2026-10-24** | Extend **D-038's subject-centered, proportionally balanced treatment** beyond biographies to the ordinary `/world` domains, **without applying character word budgets universally**. Places emphasize geography, inhabitants, atmosphere, function and social/physical change; artifacts and technology emphasize physical nature, provenance, actual versus claimed powers, custody and limitations; factions emphasize goals, organization, membership, leadership, allegiances and influence; historical-event studies emphasize causes, competing accounts, decisive changes and lasting consequences; thematic setting studies emphasize how the world works and which claims are uncertain. In every domain, events are included chiefly to explain **what changes about the subject and why it matters**, not to re-create the episode narrative. | The [World narrative style directive](WORLD_NARRATIVE_STYLE.md), [domain-specific template](WORLD_REFERENCE_PAGE_TEMPLATE.md), [editorial guide](EDITORIAL_GUIDE.md) and [cleanup plan](WORLD_ARC_CLEANUP_PLAN.md) now require a **subject-specific relevance and balance review**. Compare prose lengths only across similarly important arc/phase sections within that subject; no padding, mandated equal sizes or blanket 150–300-word target outside major characters. Keep introduction-time viewpoint, in-universe prose, research footnotes, knowledge boundaries and last known condition; a historical study may end in **Lasting legacy**. Functional registers, indexes, chronologies, ledgers, schemas and compatibility stubs retain their specialized form. Existing pages require bounded follow-up reviews; this decision does **not** claim they were all rewritten. |
