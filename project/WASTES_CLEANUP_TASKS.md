# The Wastes cleanup — task register

**Single source of truth for work status and next action.** Updated 2026-10-31. The Wastes campaign is complete through S3E18; the eleven-arc reader edition is available inside the **private repository**, not on a public website.

The checkbox beside a task is its only completion flag. **[x]** means the defined deliverable was checked at its stated scope, *not* that the whole phase, every linked page or original audio is verified. **[ ]** means open, including deliberately deferred or conditional work. Stable `WCL-###` IDs must **never be reused or renumbered**; refer to a task as [WCL-029](#wcl-029) in any other document. The bare heading keeps its link stable even if the title changes.

**Current next action:** [WCL-060](#wcl-060) — assess illithids as a people/culture subject, versus creatures and CHIDS-specific invaders, before creating any new Races page. [WCL-059](#wcl-059) (Orcs/Koromukishi evidence assessment) and [WCL-126](#wcl-126) (source-backed Orcs profile and cross-links) are complete; parent [WCL-012](#wcl-012) remains open. Standing D-081 authorizes `/world` and `/narrative` work; native-browser verification remains deferred [WCL-103](#wcl-103). Historical B1–B289 batch IDs do not substitute WCL IDs.

**How to maintain this register:** Add a task when an independently verifiable work item is discovered; choose its stable next ID and a precise outcome. Check it off only after reading back the actual changed files and recording relevant evidence, validation and limits in that **same task's entry**. An interruption leaves it unchecked with a short recovery note. Split broad tasks into new IDs before performing individual deliverables; do not mark a whole group done because a sample passed. Cite an existing owner decision for substantive work. Do **not** append the same batch recap to the manifest, changelog and progress file. Existing source dossiers, decision records, review issue keys and one-time original archives remain independent evidence.

## Edition, compatibility and publication

### WCL-001

- [x] **Approve eleven-arc boundaries and canonical numeric arc paths.** D-045/D-049 cover the E101 split, historical prequel, one-offs and compatibility constraints. Evidence: [decisions](DECISIONS.md), [chapter map](WASTES_NARRATIVE_CHAPTER_MAPS.md).

### WCL-002

- [x] **Produce and integrate all eleven narrative arcs into the private reading edition.** The integrated edition was merged in private PR #6; this checkbox is not a claim of audio-perfect fidelity. Evidence: [narrative index](../narrative/README.md), [historical execution record](../research/legacy/WASTES_CLEANUP_MANIFEST_PRE_TASK_REGISTER_2026-10-31.md).

### WCL-003

- [x] **Preserve all six original word-form arcs and season compatibility access.** Do not replace their bytes when improving the new edition. Evidence: [narrative navigation](../narrative/README.md), [D-049](DECISIONS.md).

### WCL-004

- [x] **Integrate eleven-arc reader navigation and historical-edition pointers.** Private routing and Markdown navigation were checked; public-site deployment is separate. Evidence: [narrative index](../narrative/README.md), [Wastes portal](../wastes/README.md).

### WCL-005

- [x] **Perform offline rendered-Markdown/source-link prepublication review for the edition.** Completed within offline preview limits, with interactive browser verification explicitly deferred by D-078. Evidence: [decision](DECISIONS.md), [historical validation record](../research/legacy/WASTES_CLEANUP_CHANGELOG_PRE_TASK_REGISTER_2026-10-31.md).

### WCL-006

- [x] **Merge the edition in the private repository.** PR #6 merged 2026-10-30; this is not an external website release. Evidence: [campaign plan](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-007

- [ ] **Run deferred interactive browser/anchor and responsive reader-navigation verification.** Deferred under D-078, not silently passed. Only check after actual native/browser evidence is recorded; the offline renderer strips raw HTML heading aliases. **Identified subtasks:** [WCL-104](#wcl-104) · [WCL-105](#wcl-105).

### WCL-008

- [ ] **Make a separate public-distribution decision if a public release is wanted.** *Conditional; not required for the current private edition.* Choose destination, subset of distributable content and non-leakage controls first (D-080). No deployment is implied or scheduled.

## Races, schema and coverage

### WCL-009

- [x] **Establish the Races domain with its initial two source-backed people/culture articles.** Owner-approved pilot; completeness of all peoples is a separate task. Evidence: [Races index](../world/RACES.md), historical B261.

### WCL-010

- [x] **Integrate the pilot `race_culture` v2 entity contract and check consumer compatibility.** Source-backed additive pilot; not a complete relationship graph. Evidence: [schema](../world/ENTITY_SCHEMA.md), [entities](../world/entities.json), historical B263–264.

### WCL-011

- [x] **Complete the initial reciprocal race/culture navigation connections.** Eight-page pilot integration with targeted checks. Evidence: historical B265.

### WCL-012

- [ ] **Assess and add remaining evidence-backed peoples/cultures.** Inventory candidates (e.g. Lactids, Harlequinari, elves, orcs, dwarves) before creating pages; create separate child task IDs for distinct approved articles. Do not assign unverified racial traits. **Identified subtasks:** [WCL-055](#wcl-055) · [WCL-056](#wcl-056) · [WCL-057](#wcl-057) · [WCL-058](#wcl-058) · [WCL-059](#wcl-059) · [WCL-060](#wcl-060) · [WCL-061](#wcl-061).

### WCL-013

- [ ] **Complete a current per-file Wastes world/reference census and disposition inventory.** Account for active files, domain, first/last observed episode, historical cutoff, D-048 presentation state, incoming links and remaining omissions. The older 134-path baseline was `listed_only`, not full coverage. Split actual review into stable file/group task IDs rather than marking the census done after sampling. **Identified subtasks:** [WCL-062](#wcl-062) · [WCL-063](#wcl-063).

## Places and equipment

### WCL-014

- [x] **Rework the Harbor article into reader-first place history and validate its links.** Historical B267–268; preserved major-rewrite source in [legacy archive](../research/legacy/).

### WCL-015

- [x] **Rework Razak Val and reconcile its Omnom/chronology follow-up.** Historical B269–272; specific last-state questions retained as uncertainty rather than invented outcomes.

### WCL-016

- [x] **Rework T'ietkalla into a reader-first historical place profile.** Historical B273–274; preserve prior source evidence.

### WCL-017

- [ ] **Audit the remaining place profiles for reader-first history, final status and aliases.** Complete a per-file disposition against WCL-013; create individually addressable tasks for any major rewrite. **Identified subtasks:** [WCL-064](#wcl-064) · [WCL-065](#wcl-065) · [WCL-066](#wcl-066) · [WCL-067](#wcl-067).

### WCL-018

- [ ] **Reconcile the Known Wastes map and canonical place-name crosswalk.** Preserve map-backed Khaervilon/T'ietkalla/Moag Ferhain labels and distinguish Principal City from the Principal's Lands; source pronunciation or unstated coordinates remain unresolved. **Identified subtasks:** [WCL-068](#wcl-068) · [WCL-069](#wcl-069).

### WCL-019

- [x] **Complete the Fate Six reader-first equipment/ship article and linked-index verification.** Historical B250–258, including baseline and protected heading/source links.

### WCL-020

- [x] **Complete the selected finale item-custody and technology corrections.** Scoped historical B205–251 (e.g. Chrome's Bane, windboards, Hollow Ring, syringes). This is *not* a claim that every artifact or final inventory was verified.

### WCL-021

- [ ] **Audit outstanding equipment/technology profiles and unresolved final custody.** Use the live item directory, open evidence keys and task IDs for individual candidate rewrites; do not infer unobserved final owners. **Identified subtasks:** [WCL-079](#wcl-079) · [WCL-080](#wcl-080) · [WCL-081](#wcl-081).

## Characters and relationships

### WCL-022

- [x] **Complete Monsoon Cabbage's reader-first biography and post-rewrite correction.** Historical B276–278.

### WCL-023

- [x] **Complete Diontalus's reader-first biography and Stanley-agency cross-check.** Historical B279–282; [original preserved](../research/legacy/DIONTALUS_PRE_BATCH281_2026-10-31.md).

### WCL-024

- [x] **Complete Angelashi's reader-first biography and finale apparent-Nash correction.** Historical B284–285; [original preserved](../research/legacy/ANGELASHI_PRE_BATCH284_2026-10-31.md).

### WCL-025

- [x] **Complete the Soulbroker's source-backed biography and pact-status reconciliation.** Historical B286; [original preserved](../research/legacy/SOULBROKER_PRE_BATCH286_2026-10-31.md). His death does not itself banish Worldbreaker.

### WCL-026

- [x] **Complete Squirts's chronological biography and separate two deaths from the dead-head graft.** Historical B287; [original preserved](../research/legacy/SQUIRTS_PRE_BATCH287_2026-10-31.md). Chunks lives.

### WCL-027

- [x] **Complete the Principal's reader-first biography and separate the original, lunar copies and coerced Nash successor.** Historical B288; [original preserved](../research/legacy/PRINCIPAL_PRE_BATCH288_2026-10-31.md).

### WCL-028

- [x] **Reconcile Principal/Nash/Soulbroker cross-page facts, canonical name and old heart/status cutoffs.** Historical B289. Corrected `world/CHARACTERS.md`, `world/characters/nash-maggard.md`, `world/CHRONOLOGY.md` and `world/HISTORICAL_EVENTS.md`; no fabricated biological paternity, original Principal revival or universal soul ownership.

### WCL-029

- [x] **Audit the structure of `world/characters/nash-maggard.md`.** Read-only audit closed 2026-10-31 against `main` HEAD `076e1d5` and the preserved pre-task-register WCL-044 working-tree edit. [WCL-044](#wcl-044) inventories full file headings, footnotes and fragment/link limits; [WCL-045](#wcl-045) separates historical cutoffs, hearsay and the played S3E18 ending; [WCL-046](#wcl-046) selects **a separately gated major reader-first restructure**. **No biography text changed or claimed fact/audio/anchor-perfect.** Follow-up [WCL-030](#wcl-030) holds preservation, source-sensitive rewrite and compatibility verification.

### WCL-030

- [x] **Restructure Nash's biography into a reader-first eleven-arc account.** Completed 2026-10-31 with the owner's explicit “Proceed,” against `main` HEAD `076e1d5`; [live biography](../world/characters/nash-maggard.md), [exact pre-WCL030 baseline](../research/legacy/NASH_MAGGARD_PRE_WCL030_2026-10-31.md). Preservation copy is **69,804 bytes**, SHA-256 `19b74c2936531f48fdf0b67d41f514a4eece82ec363e7ac76adefc225d5cfb6b`, verified identical to the working-copy original *before edits*. New manuscript is **85,458 bytes**, SHA-256 `a041a4c2081ece18b4d274b4d8fc29ff446bb10d8035e2fa197edf57af220d38` (after lint repair).

  - **Result:** New opening in-world introduction, approved 11-arc chronological character study, relationships/abilities synthesis and campaign-final `Current status` before `Sources and project notes`. Nash's flesh-heart exchange, unsuccessful full-dragon recovery, lunar chrome death, Stanley's off-Earth *True Resurrection* and unknown cupboard double are distinguished from historical speculation and prior cutoffs. The **entire pre-existing episode/bonus/equipment research body, original five-arc prose and all 26 original footnote definitions were retained verbatim** except renaming the archival `## Introduction` to `## Earlier five-arc introduction` to avoid an MD024 duplicate; the live original `#introduction` fragment now targets the new introduction. The other original research headings remain unchanged, with **all 38 prior heading texts still represented** somewhere in the new page, and no original Markdown link occurrences removed. Added 12 new paired footnote definitions, retaining every existing definition and referenced source; the specialist spellcasting register and technology page remain separate and unchanged.
  - **Evidence and checks:** Automated comparison of numbered UTF-8 text readback against the preserved original confirmed the old source section after the first `## S3E18` is **text-identical after reversing only that single heading rename**; original byte integrity is separately established by the preservation SHA-256; all 26 prior footnote IDs retained, 12 added, no missing reference definitions. All **48 distinct paths** used by **55 newly written Markdown links** were confirmed present. Offline renderer: 54 headings, key new and old anchors present; **100/264 local link occurrences checked, 0 broken and 164 beyond renderer cap**. Markdownlint `world/characters/nash-maggard.md` exit 0, 0 violations; `git diff --check HEAD` exit 0 (existing line-ending warning on task register). Pre/post SHA-256 measured from file bytes. **Not claimed:** source-audio listening, native GitHub fragment/alias browser fidelity ([WCL-103](#wcl-103)), or remaining-link verification ([WCL-101](#wcl-101)); no publication, commit or push. The preserved original is added as a distinct archive file, not an automatic per-batch snapshot.

### WCL-031

- [ ] **Audit remaining character profiles and specialist-register exceptions.** Complete separate per-subject outcomes or task IDs rather than a single “all characters done” assertion. **Identified subtasks:** [WCL-047](#wcl-047) · [WCL-048](#wcl-048) · [WCL-049](#wcl-049) · [WCL-050](#wcl-050) · [WCL-051](#wcl-051) · [WCL-052](#wcl-052) · [WCL-117](#wcl-117) (Hope's completed restructure) · [WCL-118](#wcl-118) (Vorel's completed restructure) · [WCL-119](#wcl-119) (Stanley's completed restructure) · [WCL-120](#wcl-120) (Badass T's completed profile/navigation). **Parent exit pending:** These child outcomes do not establish exhaustive per-file character coverage; reconcile remaining dispositions via [WCL-063](#wcl-063) before closing this parent.

### WCL-032

- [ ] **Reconcile other character-family and antagonist finale states across directories.** Compare witnessed endings against later mentions; preserve mysteries such as the final apparent second Nash. **Identified subtasks:** [WCL-077](#wcl-077).

## Evidence, integration and acceptance

### WCL-033

- [ ] **Review remaining factions/creatures/history subjects for supported classifications and last-state claims.** Use WCL-013 inventory and separately addressable child tasks; do not merge races, characters and monsters without source support. **Identified subtasks:** [WCL-053](#wcl-053) · [WCL-054](#wcl-054) · [WCL-070](#wcl-070) · [WCL-071](#wcl-071) · [WCL-072](#wcl-072) · [WCL-073](#wcl-073).

### WCL-034

- [ ] **Finish canonical-name and stable-alias regression in active world navigation.** Do not rename historical files, frozen source quotations or raw transcripts. Principal/Principle targeted WCL-028 corrections are completed but are not project-wide closure. **Identified subtasks:** [WCL-096](#wcl-096) · [WCL-097](#wcl-097) · [WCL-098](#wcl-098).

### WCL-035

- [ ] **Extend the pilot entity/relationship graph beyond the initial Races v2 entries.** Stable IDs, members, relationships and artifact custody only where backed by source; keep schema migration separately reviewable. **Identified subtasks:** [WCL-099](#wcl-099) · [WCL-100](#wcl-100).

### WCL-036

- [ ] **Distill active review questions from `project/REVIEW_QUEUE.md` and `world/CONSISTENCY_LEDGER.md`.** Retain existing issue keys, frozen source records and unresolved evidence, removing superseded *active* “next” instructions without deleting history. **Identified subtasks:** [WCL-094](#wcl-094) · [WCL-095](#wcl-095).

### WCL-037

- [ ] **Triage and perform original-audio/handout checks for high-impact open issue keys.** Record each actual listened window, source identity and interpretation. Two ASR exports or rendered Markdown are *not* audio verification; split into individual issue tasks. **Identified subtasks:** [WCL-083](#wcl-083) · [WCL-084](#wcl-084) · [WCL-085](#wcl-085) · [WCL-086](#wcl-086) · [WCL-087](#wcl-087) · [WCL-088](#wcl-088) · [WCL-089](#wcl-089) · [WCL-090](#wcl-090) · [WCL-091](#wcl-091) · [WCL-092](#wcl-092) · [WCL-093](#wcl-093).

### WCL-038

- [ ] **Complete maintained-document link/fragment verification beyond preview caps.** For example, Nash's profile has over 200 local links and the chronology over 300; the renderer checks at most 100 destinations per file. Verify remaining links and legacy anchors separately rather than recording “all valid.” **Identified subtasks:** [WCL-101](#wcl-101) · [WCL-102](#wcl-102) · [WCL-103](#wcl-103).

### WCL-039

- [ ] **Complete D-048 reader-first checks on remaining top-level world and narrative indexes.** Subject directories and portals should start with reader-facing story or context; keep technical indexes explicitly classified as exceptions. **Identified subtasks:** [WCL-106](#wcl-106) · [WCL-107](#wcl-107) · [WCL-108](#wcl-108) · [WCL-109](#wcl-109) · [WCL-110](#wcl-110) · [WCL-111](#wcl-111) · [WCL-112](#wcl-112) · [WCL-113](#wcl-113) · [WCL-114](#wcl-114).

### WCL-040

- [ ] **Finish campaign-wide chronology, current-status and source-boundary acceptance sweep.** Include S3E18 Earth restoration, Worldbreaker's permanent-for-Earth banishment, Nash's death/resurrection and the unresolved finale warning, without inferring untold future events. **Identified subtasks:** [WCL-074](#wcl-074) · [WCL-075](#wcl-075) · [WCL-076](#wcl-076) · [WCL-078](#wcl-078) · [WCL-082](#wcl-082).

### WCL-041

- [ ] **Complete final whole-scope validation and disposition accounting.** Ensure every Wastes-maintained file has a documented accepted/pending/retained-exception status, active links checked, unresolved limitations listed, and private-distribution scope kept distinct from optional public deployment. **Identified subtasks:** [WCL-115](#wcl-115) · [WCL-116](#wcl-116).

## Workflow governance

### WCL-042

- [x] **Replace triple batch reporting with this indexed, checkboxed task register.** Historical manifest, progress and changelog preserved byte-for-byte once before reorganization; active manifest owns *artifact disposition only*, changelog *meaningful milestones/decisions only*, and progress is a compatibility redirect. Workflow instructions point here for completion and recovery. Evidence: [legacy manifest](../research/legacy/WASTES_CLEANUP_MANIFEST_PRE_TASK_REGISTER_2026-10-31.md), [legacy log](../research/legacy/WASTES_CLEANUP_CHANGELOG_PRE_TASK_REGISTER_2026-10-31.md), [legacy progress](../research/legacy/WASTES_CLEANUP_PROGRESS_PRE_TASK_REGISTER_2026-10-31.md).

### WCL-043

- [x] **Consolidate redundant intermediate cleanup snapshots without losing protected originals.** Earlier owner-approved, hash-verified 34-file reduction; the immutable original/history inventory remains [retention index](REPORT_SNAPSHOT_RETENTION_INDEX.json), historic B116–117. No new per-batch full copies.

---

**Previously identified subtasks:** The concrete follow-ups below were extracted from the active [campaign plan](WASTES_CAMPAIGN_CLEANUP_PLAN.md), [review queue](REVIEW_QUEUE.md) and preserved [historical cleanup record](../research/legacy/WASTES_CLEANUP_MANIFEST_PRE_TASK_REGISTER_2026-10-31.md). They are **not new completion claims or automatic rewrite approvals**. Each has an immutable ID and parent. A parent checkbox remains open until its defined exit gate and relevant children are satisfied. Further per-file or issue work can be added under subsequent new IDs as discovered; this list is a register of identified candidates, not a claim that all current source issues have been exhaustively extracted.

## Identified subtasks — Character biographies and specialist registers

### WCL-044

- [x] **Inventory Nash's headings and incoming fragment targets.** Completed 2026-10-31 at clean `main` HEAD `076e1d5` (read-only, 243/243 numbered source lines); parent [WCL-029](#wcl-029). [Active biography](../world/characters/nash-maggard.md) · [2026-10-24 source baseline](../research/legacy/NASH_MAGGARD_PRE_IN_UNIVERSE_PASS_2026-10-24.md) · [2026-10-22 research baseline](../research/legacy/2026-10-22/PROFILE_NASH_MAGGARD_BEFORE_2026-10-23.md).

  - **Live structure:** 38 headings with 38 unique renderer-generated GitHub-compatible fragments; no raw HTML alias anchors. Ten source/bonus headings appear before `## Introduction` (L47). The final `##` is the historical Season Two cutoff (L181), not a campaign-end `Current status`; the page mixes story-first arc sections with later reverse-chronological research headings. This is a presentation/compatibility audit, **not** a rewrite or factual acceptance.
  - **Current fragment inventory (source line, level, exact offline-rendered slug):**
  - L1 # `#nash-maggard`
  - L3 ## `#s3e18--actual-death-as-new-principal-true-resurrection-retirement-mysterious-double`
  - L7 ## `#s3e17--talks-to-father-about-grandchildren-permanently-banishes-worldbreaker`
  - L11 ## `#s3e15--shoulder-self-acceptance--active-fireballs-no-full-dragon-form`
  - L15 ## `#s3e14--tested-dragon-transformation-after-surgery-partial-flesh-change-no-full-dragon`
  - L19 ## `#s3e13--engineered-heart-actually-removed-survives-with-flesh-heart-firebolt-and-floating`
  - L23 ## `#s3e12--51328095120-nashes-god-defeated-nearly-sacrificed-to-asmodeus`
  - L27 ## `#s3e11--actually-meets-principal-nana-truffled-gate-to-weir-new-light-phrase`
  - L31 ## `#s3e10--confronts-abusive-childhood-classroom-physical-relic-heart-slab-and-waiting-guards`
  - L35 ### `#s3e10-recovered-keepsakes--a-vhs-cassette-and-an-old-anatomical-remnant`
  - L43 ## `#may-2022-bonus--scott-on-risk-taking-costly-regrowth-and-the-hearts-unknown-failure-point`
  - L47 ## `#introduction`
  - L53 ## `#development-by-arc`
  - L55 ### `#arc-one--from-wanderer-to-companion`
  - L61 ### `#arc-two--attachment-and-the-fear-of-loss`
  - L67 ### `#arc-three--responsibility-and-sacrifice`
  - L75 ### `#arc-four--a-body-remade-in-sigil`
  - L81 ### `#arc-five--family-identity-and-difficult-choices`
  - L91 ## `#relationships-and-abilities`
  - L97 ### `#the-finite-robe-patches-and-multiple-staffs-are-separate-inventories`
  - L105 ## `#december-2021-retrospective--character-tone-and-unrevealed-mines-story`
  - L109 ## `#season-two--reunion-on-mars-and-a-new-possible-refuge`
  - L113 ## `#s2e03--the-solar-mines-account-before-the-war-council`
  - L119 ## `#s2e06--temporary-dragon-cognition-but-no-cure`
  - L123 ## `#s2e11--recovers-and-wears-possible-collector-ring`
  - L129 ## `#march-2022-bonus--low-intelligence-interpretation-out-of-game`
  - L133 ## `#february-2022-bonus--hypothetical-alternate-nash-coalition-out-of-game`
  - L137 ## `#april-2022-qa--class-features-and-conditional-regeneration-out-of-game`
  - L141 ## `#s3e09--revived-and-aided-by-white-nash-childhood-bully-general-motors`
  - L145 ## `#s3e08--refreshed-dragon-form-generator-extraction-and-eye-blinded-physically`
  - L149 ## `#s3e07--black-dragon-duel-enlarge-on-vorel-and-ruby-salvaged`
  - L153 ## `#s3e06--stinking-cloud-reversed-injury-poison-kill-and-unfolded-dragon-wings`
  - L157 ## `#s3e05--returns-to-solar-mines-giant-alternate-hamster-detachment-and-three-real-ice-storms`
  - L163 ## `#s3e04--augmented-protected-with-his-family-before-war-99-other-nashes-assigned-tower`
  - L167 ## `#s3e03--mars-reunion-ninety-nine-variants-and-challenged-origins`
  - L173 ## `#historical-s3e02-cutoff--completed-human-body-and-sprout`
  - L177 ## `#historical-s3e01-cutoff--adult-dragon-incomplete-human-regeneration`
  - L181 ## `#historical-season-two-cutoff-after-s2e12`
  - **Historical fragment risk:** the byte-preserved 2026-10-24 pre-pass file has 12 headings, 10 slugs absent from today's page; the 2026-10-22 research baseline has 54 headings, 53 slugs absent today. Across both originals there are **63 distinct historical-only slugs**; retain source baselines and assess whether any require compatibility aliases under [WCL-046](#wcl-046)/[WCL-030](#wcl-030). These historical headings are **not** evidence that those old fragments still resolve in the live biography.
  - **References and inbound links:** 26 footnote definitions / 26 reference occurrences; 209 local Markdown links, including 119 episode-link occurrences (85 distinct destinations). Offline renderer checked **100/209** local links (0 broken, **109 untested** due to cap): remaining link validation is [WCL-101](#wcl-101), not complete. Literal `nash-maggard.md#` searches found **no live inbound fragment links** in `world/`, `narrative/`, `wastes/`, `episodes/`, `research/`, `reports/`, `delvers/`, `inverse/`, `oneshots/`, `transcripts/` or `bonuses/`; `project/` contained two *historical discussion* mentions rather than active links. `sources/` search was truncated; root README, external deep links and native GitHub alias behavior were not verified. The native browser/alias check remains [WCL-103](#wcl-103). **Risk:** a future heading rename may break unobserved external/history links even though no active in-repository fragment links were found.

### WCL-045

- [x] **Separate Nash's historical cutoffs from campaign-end status.** Read-only cross-check completed 2026-10-31 at `main` HEAD `076e1d5`; parent [WCL-029](#wcl-029). Evidence: [Nash biography](../world/characters/nash-maggard.md), [heart history](../world/technology/nash-dragon-heart.md), played [S3E03](../episodes/S3E03.md), [S3E10](../episodes/S3E10.md), [S3E11](../episodes/S3E11.md), [S3E13](../episodes/S3E13.md), [S3E14](../episodes/S3E14.md), [S3E18](../episodes/S3E18.md) dossiers; no original audio listened.

  - **Physical and custody sequence:** The engineered metal heart remained implanted through S3E12 after S2E12 heart/eyestalk survival and S3E01–02 regenerated bodily restoration; Brett/Asmodeus physically removed it in S3E13 and made Nash a beating heart from Nash's *own* flesh. Brett is its **last witnessed holder**, not a proven original manufacturer. Nash successfully used *Firebolt* and innate floating afterward. The separate natural black-dragon heart recovered for Ruby is **not** his engine.
  - **Transformation and finale:** The S3E13 statement “not yet tested” is true **at that cutoff only**; a partial, incomplete dragon attempt was played in S3E14 and full adult-dragon restoration was not shown by the finale. In S3E18 Earth/Moon ordinary spellcasting was suppressed but floating persisted. Council of Faces forcibly made Nash a chrome Principal successor; Nash independently resisted its murder order, evacuated the allies, detonated the moon facility, and **actually died** as his chrome body melted. Stanley later used *Wish* to produce *True Resurrection* away from Earth; Nash returned to familiar flesh **without equipment**, reunited with Angelashi and four children and stayed on Planet Nash. No witnessed reimplantation of the metal engine, anatomical examination of his resurrected heart or successful new dragon transformation. An apparent second Nash in the final cupboard scene remains unidentified.
  - **Origin provenance:** S3E03's alleged childhood, paternal seed and 78-body origins are **parasite-mediated dream claims**; S3E10's operating slab is physically observed but Nash's suggested implantation location is inference; S3E11's test-tube/weapon/adjacency account is the Principal's testimony; S3E12's alleged loan comes from Asmodeus; S3E18's Council-of-Faces ancestry account is also interested testimony. None proves biological paternity, exact construction or full timelines. Early dragon-mother/Clench accounts likewise remain attributed, not independent facts.
  - **Cutoff classification:** S2E08/S2E11/S2E12, S3E01/S3E02 and the pre-removal S3E03–12 possession, powers and family locations are historical snapshots, **not live present state**; S3E13 “not tested,” S3E17 “Ruby unactivated” and older heart-magic durability theories are superseded/qualified by later played evidence. The story-first `Development by arc` currently ends after the old Arc Five and does not itself narrate the later campaign, while latest-first research sections above and below it contain those events. The factual page largely distinguishes cutoffs already; the unresolved deficiency is **reader presentation and coverage**, not license to replace uncertain testimony with fact. WCL-046 determines treatment; WCL-030 remains a separate edit gate.

### WCL-046

- [x] **Decide Nash biography's reader-first treatment.** **Disposition (2026-10-31): a separately scoped major single-page reader-first restructuring is warranted; not a retained technical exception or unplanned cosmetic shuffle.** Parent [WCL-029](#wcl-029); execution belongs to open [WCL-030](#wcl-030), **not performed by this audit**. Evidence: [biography](../world/characters/nash-maggard.md) and [WCL-044](#wcl-044)/[WCL-045](#wcl-045).

  - **Why:** Ten research/bonus source headings precede the actual `Introduction`; the main developmental narrative covers old Arc One–Five only, while later played seasons and the finale live in densely annotated, reverse-chronological episode headings. A reader following the in-world story cannot reach a chronological campaign-end `Current status` at the end of the subject narrative. The 11-arc private edition must not be conflated with the page's older named arc headings without checking the approved chapter maps.
  - **WCL-030 execution plan/gates:** Before any material reordering, preserve **one exact working-copy original** with path, SHA-256 and approved scope, and verify the copy. Plan a new chronological in-world narrative using the accepted eleven-arc crosswalk, ending with **Current status** (resurrection, family retirement, unresolved double). Move source-first episode/bonus research to a clearly labeled **Sources and project notes** section, preserving each distinct factual qualification, direct episode/report link, all 26 footnote references/definitions, spellcasting-register link and the separate heart reference; avoid duplicating unverified claims as prose fact. Preserve the 38 existing live heading fragments where possible **as unchanged headings at the same file path**, and assess the 63 historical-only fragments before any aliases; native GitHub HTML-anchor behavior remains unverified [WCL-103](#wcl-103). Finish outstanding 109 untested local links under [WCL-101](#wcl-101) before claiming complete compatibility. Source-backed facts, quote/provenance gates, historical snapshot dates, confidentiality and protected older editions remain unchanged.
  - **Authorization and verification boundary:** This is a **read-only structural disposition**, not approval inferred from a checked box to publish or rewrite. Apply the repository's substantive-owner authorization rule and existing explicit owner directions to the *specified* WCL-030 change before editing. Verify the new page with targeted Markdownlint, rendered navigation, link/footnote checks, scoped diff and factual comparison; browser-only checks remain independently deferred. No new original audio checked.

### WCL-047

- [x] **Audit Hope Akmenos's biography.** Completed **read-only structural/source-boundary review** 2026-10-31 at `main` HEAD `076e1d5`; [unchanged biography](../world/characters/hope-akmenos.md), **177/177 numbered lines**, **52,517 bytes**, SHA-256 `4f818286069774fb88475fa56443ba491292edeaa1f8a1ab6c748650d9088863`. **Parent:** [WCL-031](#wcl-031). **Disposition:** a separate source-backed **eleven-arc reader-first restructure** is warranted under [WCL-117](#wcl-117); this audit does not authorize or perform the rewrite.

  - **Structure/links:** 37 unique offline-rendered heading IDs; the first ten S3E18–S3E10/bonus research headings precede `## Introduction` at L43. `Development by arc` L49–71 still uses the former five-arc thematic partition, not D-045's eleven numeric arcs. After L73, equipment history, bonus/source studies and reverse-order S2/S3 cutoffs continue; the last substantive heading L153 is *historical Season Two*, not `## Current status` at the played campaign ending. All **8 footnote definitions and 8 references pair** (no orphan/unresolved); **171 local links**, **145 distinct file paths**, **0 explicit `#fragment` destinations**. Offline renderer checked **100**, **0 broken**, **71 beyond cap**; targeted Markdownlint exit 0, 0 violations. A workspace-wide literal `hope-akmenos.md#` search returned 0 among a **truncated** scan, so neither complete inbound-link coverage nor native/browser alias compatibility was demonstrated.
  - **Continuity findings:** [S3E18 dossier](../episodes/S3E18.md) and L3–5 substantiate Hope **alive**, accepting survivors into **T'ietkalla's future reconstruction**, Monsoon's witnessed sun-death and helmet custody, Stanley's transferred Mask of Eltanfawr **worn as a crown**, and **prospective Fate Six/ghost-crew control after attunement**—not a completed city rebuild or proven command mastery. The L3 heading's **“restored T'ietkalla” overstates its rebuilding status**; correct in a separately scoped source-backed edit, preserving legacy fragment risk. Her organic limbs are distinct from earlier prosthetics, the stolen Hand of the Voice (taken S3E02, handed to Brett's assistant S3E12), the spent Hollow Ring, *Diplomacy* and changing ship/weapon custody. The S3E10 embedded father-head death is witnessed; the father's wider afterlife, the mother's fate and any uncertain nickname remain unresolved. Keep NPC claims, private Voice instructions, cast retrospectives and episode-specific states attributed, not promoted to established facts.
  - **Preservation/gates:** Do not erase the earlier five-arc prose, technical item details, bonus commentary, research timelines, original footnotes or original stable path. Before major WCL-117 work, preserve exactly the *then-current working-copy bytes* once with SHA-256; the older 2026-10-22 profile baseline is historical evidence, not a substitute. Split eleven-arc story from source appendix, retain legacy heading destinations where feasible, add campaign-end `Current status` and validate all links/footnotes separately. No original audio heard, browser inspection performed, or biography content changed by WCL-047.

### WCL-048

- [x] **Audit Vorel's biography.** **Read-only structural/continuity audit completed 2026-10-31** against `main` HEAD `076e1d5`; [unchanged 243-line biography](../world/characters/vorel.md), **73,157 bytes**, SHA-256 `08a508f6c35d4fdb8b7a0a65be69e6ccb43cdad2829df3f28e99cf8c789bf2d2`. **Parent:** [WCL-031](#wcl-031). **Disposition:** a separately scoped [WCL-118](#wcl-118) reader-first eleven-arc restructure is warranted; do not treat this checked audit as an edit or new factual/audio verification.

  - **Structure/navigation:** The source opens with S3E18/S3E17 research, portrait/performer metadata and many reverse-chronological episode/bonus headings; the in-world origins first appear at L139, with historical thematic sections and E119–E125 research following. **44 distinct rendered heading IDs**; there is **no opening in-world `Introduction`, no approved eleven-arc character progression and no final `Current status`** (last heading is a November 2020 retrospective). One footnote reference and one definition pair; **205 local Markdown links / 148 distinct destination paths**, zero explicit fragment destinations. Offline renderer checks the first **100/205** with **0 broken**, leaving **105 occurrence-level destinations unchecked by the renderer**; no link completeness claimed. Scoped `world/` literal search for `vorel.md#` had zero hits across 139 files; other directories, historical aliases and external deep links remain unchecked. Targeted Markdownlint passed **0 violations**.
  - **Source/ending boundaries:** [Played S3E18](../episodes/S3E18.md) establishes Vorel **alive**, +2 protective chrome plating on his scales **not shown removed** (and no demonstrated possession), in possession/use of *Chrome's Bane* by S3E17; he supports restoring Earth, commissions a memorial while Nash is presumed dead, sees Nash actually resurrected, then **begins** the overland journey with approximately 50–60 lizardfolk and integrating Kuromokishi toward **Razak Val**, **not** already settled in a rebuilt city. **Stanley confers** the new interpersonal title **“Friend”** and Vorel accepts/expands **“Friend Till the End of His Days”**, distinct from his earlier self-awarded grand titles or a state office. [Title register](../world/characters/vorel-titles.md) places the title event at **~02:07–02:10**, while the [S3E18 episode dossier](../episodes/S3E18.md) places the departure and conferral in its **~02:13–02:21** scene block; neither exact clock is audio-confirmed—retain as a [WCL-050](#wcl-050) source-alignment check, not a silent correction or doubt about the played act. Preserve the Eye of Groxl's changing functionality, Mawstorm sword vs separately named released raptor, distinct helmets, lost/borrowed items, Bok Bok and Omnom histories, CHIDS experiment claims as claims and Stanley/Diontalus agency separation. Performer Q&As and dream/possible alternate lives do not count as played facts.
  - **Next-step safeguards:** For [WCL-118](#wcl-118) preserve one exact *then-current* pre-rewrite original with SHA-256, retain all 44 original live heading texts/fragment targets where practical, all 205 original link occurrences, titles-register cross-link and surviving episode/bonus/source notes; use the approved eleven-arc crosswalk and an actual final personal status. Avoid rewriting the technical titles register while restructuring the biography. No original audio heard, native browser aliases tested, biography changed, Git commit or publication performed.

### WCL-049

- [x] **Audit Stanley Billings's biography.** Completed **read-only structural/source-boundary audit, 2026-10-31**, against `main` HEAD `1185b17` with the existing D-081/Vorel changes preserved. [Unchanged biography](../world/characters/stanley-billings.md): **189/189 numbered lines**, **56,817 bytes**, SHA-256 `1aef7e33b1999a8acb42f9f6176d83772194a6ed38b509c7b60c44983dddea0c`. **Parent:** [WCL-031](#wcl-031). **Disposition:** separately scoped eleven-arc reader-first restructure under [WCL-119](#wcl-119), **already authorized by D-081**; no new approval request required. Audit selected alone because the dense 56 KB profile and separate source checks warrant a bounded slice; the unrelated titles/spell registers were not grouped.

  - **Structure/census:** Full contiguous reading L1-44, L45-86, L87-124, L125-152 and L153-189, with intermediate checkpoint after L124. Original-name provenance L3 and nine retrospective/late-episode headings precede Introduction L45. The five thematic historical arc sections L51-79 do not implement the eleven D-045 arcs. The last substantive H2 is `Historical Season Two cutoff (after S2E12)` at L163, followed by earlier cutoffs; **no final `Current status` heading**. **38 unique heading texts**, no tables, one existing Wish-recovery review marker, **9 footnote definitions / 9 references**, all paired with no orphans. **154 local Markdown links / 136 distinct local paths, all present**. One explicit local fragment to the written-name report matches that report's source-heading spelling; native browser behavior remains untested. The one external Discord link was **not fetched**. Scoped `rg` across `world/`, `narrative/`, `project/`, `wastes/` and root README found one historical prose mention of `stanley-billings.md#`, but **0 Markdown destination matches**; this is not exhaustive external/archival inbound-link coverage.
  - **Identity, agency and contract evidence:** The [written-name report](../reports/DISCORD_NEW_SPELLING_2026-10-27.md#wastes-stanleys-original-elven-name--valiir-ornath) L45-59 confirms owner/player-authoritative **Valiir Or'Nath = Stanley Billings**, father **Delit Or'Nath**, and **Villa Or'Nath**; preserve slugs and distinguish identity from unknown poem timing. [S2E02](../episodes/S2E02.md) L13-14/L33 depicts a speaking father-shaped ship-mind, with life-essence and maternal-death history attributed to the voice, not witnessed parental resurrection or independently shown ancient events. The existing Stanley/Diontalus agency separation and already corrected **Vorel kills Buttons** passage must survive. [S2E01](../episodes/S2E01.md) L23/L33 explicitly removes Stanley's **last Weir obligation while retaining original pact benefits**; the older soul-claim statements are historical cutoffs, not final status. This does not establish that Stanley destroyed the Soulbroker himself or signed a new Hell pact.
  - **Private knowledge and ending evidence:** [S2E03](../episodes/S2E03.md) L29-30 establishes public election/appearance change, but the Nash-must-die revelation is **Stanley-private**; [S3E13](../episodes/S3E13.md) L11-12 recalls it privately without an attempted murder or disclosure. [S3E019](../episodes/S3E019.md) L12/L26/L32-38 is **nonplayed retrospective/headcanon**: Beau interprets Nash's actual temporary moon-base death as fulfilling the prophecy although Stanley did not kill him and later resurrected him; Jon's possible fake-death retirement is not Stanley's ending. [S3E18](../episodes/S3E18.md) L19-25 establishes off-Earth *Wish* producing *True Resurrection*, Nash restored, Vorel awarded Friend, **mask physically transferred to Hope**, Stanley leaving on **another Elhandari vessel**, farewell on Mars and **actual Feywild crossing as Solely Prime** with many, not all, Elhandari. The four-versus-seven-day Wish recovery discrepancy remains the original review marker; retained Wish access is distinct from recovery, remaining slots and new stress. No original audio heard; read source windows are dossier/report evidence, not independent transcription verification.
  - **Validation/recovery:** Temporary local census and micromark/GFM-footnote render checked all local destination paths, paired notes and **38 rendered headings / 18 resolving generated footnote/backlink fragments**. `node scripts/lint-markdown.mjs --files world/characters/stanley-billings.md`: exit 0, 0 violations. The targeted incoming Markdown-destination search returned exit 1 for zero matches, not a failed content check. Biography SHA-256 remained unchanged after the audit; no full-file backup is needed for read-only work. Native GitHub rendering, disclosure/alias behavior, external Discord contents, whole-page claim/audio verification and broader inbound-link coverage are **not verified**. No source, biography, narrative, title/phrase register, commit/push or publication changes. Next operation: WCL-119's separately checkpointed rewrite, preserving one exact then-current major-rewrite baseline before editing.

### WCL-050

- [x] **Complete Vorel's S3E019 title-recitation comparison and reconcile final-title source timing.** Completed **2026-10-31 at timed-export scope**, under D-081, `main` HEAD `1185b17`; **Parent:** [WCL-031](#wcl-031). [Titles register](../world/characters/vorel-titles.md): **67,913 bytes**, SHA-256 `27990629a0c3afc498ba1a1be6d13e6e0b5f77c44d65f6e0636d39bd976a597a`. [Vorel biography](../world/characters/vorel.md), one contemporary status-footnote replacement only: **98,994 bytes**, SHA-256 `1185662783fe8d554a9cfbe08298acce576f8d988f1e99454f34bb32f0a0c50e`. Initial register was 62,646 bytes / 308 lines, SHA-256 `cc0edee65e116cf9b2fea4627b28c537c506d099a6ee1f3f57668ed73c502126`. Existing D-081 and biography work preserved; no whole-file backup required for these bounded additions/timing notes.

  - **Roundtable outcome:** Existing retrospective paragraph and source-indexed rows already covered the recited labels; this task did **not** discover or manufacture dozens of new titles. Directly read local P/Q recitation including its start: **P 1505-1528, 01:15:44.850-01:17:13.180; Q 2506-2532, 01:15:44.825-01:17:12.870**, with surrounding request/commentary. Corrected the register's approximate **01:16-01:19** locator, added an eight-group ordered crosswalk to the existing entries and clarified that omissions from the late recital do not revoke older labels. The **46 working phrase slots exclude the personal name**, keep Shieldless Dasher together and treat Savior/Survivor of the Universe as one ambiguous slot; they are **not an audio-verified count of distinct titles**. Every slot matched an existing entry or documented variant, with no new conferral date/office. P/Q name and proper-noun variants, Q's `intumere`, Savior/Survivor ambiguity and Shieldless/Dasher segmentation remain provisional. S3E019 remains **nonplayed retrospective**, not 46 new awards or a second Friend conferral.
  - **Finale timing outcome:** The actual Friend offer is **P1982 02:09:35.070-02:09:37.820 / Q3172 02:09:35.095-02:09:37.600**; Vorel's expansion/acceptance is **P1983 02:09:40.665-02:09:43.330 / Q3173 02:09:41.920-02:09:48.000**. The overview now uses **~02:09:26-02:09:48** with cue IDs. The former broad **02:07-02:10** and truncated **02:09:25-02:09:40** locators are retained as provenance, beside the dossier's later grouped **02:13-02:21** range; no silent choice between unsupported headings. The distinct **Stanley-to-Hope** greatest-friend remark at **~02:14:10-02:14:14, P2063/Q3284**, explains why matching the word friend to that later section would be wrong. These are **local subtitle clocks**, not heard speech boundaries, verified diarization, punctuation or frame accuracy. The original audio/wording review marker remains open; the contemporary biography footnote now reflects the completed local alignment while all older research-body bytes remain unchanged.
  - **Exact local evidence inputs:** S3E019 P: **248,170 bytes / 2,541 cues**, SHA-256 `20b5e913cba98d87caaa35db65f68ff348fd39736ee91b1635dddf7f49d874cd`; Q: **333,158 bytes / 4,098 cues**, SHA-256 `c67090f3610d6e9d8121a661ac2bd135634e8ed5252adf2e6cab1e26c10346f4`. S3E18 P: **224,034 bytes / 2,304 cues**, SHA-256 `e576aefc7ff52d966d367fced897881b4b24d49e4aee6a87fa50687a805f3f97`; Q: **297,556 bytes / 3,667 cues**, SHA-256 `d4206c38eae302ec80a1f633d9ae8c45d1b0b4073c5e2e2b6a503f6ba1ef29db`. Actual filenames/relative links are in the register's two source captions. **4/4 post-check source hashes unchanged**. Read only the named/nearby cue windows, not a new full semantic review of either episode or an ASR accuracy measurement. Existing dossiers and comparison reports provide context but were not rewritten.
  - **Validation and recovery:** Register retains **47/47 headings in identical order**, all existing review markers and **172 original link occurrences**, plus five new links. All **177 local occurrences / 135 distinct paths** resolve; its four locally rendered GFM tables each have consistent three-column rows. Vorel retains **316 local occurrences / 168 distinct paths**, all present, **15 definitions / 15 references** paired and **30/30 rendered footnote/backlink fragments resolving**. A reverse-delta SHA check proves the biography differs from the prior WCL-118 version by **exactly one source-note replacement**. Local micromark/GFM-table/GFM-footnote rendering and targeted Markdownlint for both files: exit 0, no violations; scoped `git diff --check` exit 0. Task-register lint/whitespace and final persisted readback close the control change. No source-audio listening, native GitHub/browser testing ([WCL-103](#wcl-103)), original source mutation, episode-dossier change, new archive/report, commit/push/publication. Next selected work: [WCL-051](#wcl-051), preflight the live Nash spell-phrase ceiling before extending its later-source coverage.

### WCL-051

- [x] **Extend Nash's spell-phrase register past the E111 candidate-backfill ceiling.** Completed **2026-10-31 at targeted discovery scope**, under D-081, `main` HEAD `1185b17`. **Parent:** [WCL-031](#wcl-031). [Register](../world/characters/nash-spellcasting-phrases.md): **69,754 bytes / 245 lines**, SHA-256 `37ced797355f58fa3946f2e8f5dae67749a53ca27a8631eea536687e65678882`; initial working-copy input **63,127 bytes / 224 lines**, SHA-256 `90ea59068cff8e5809eeba90b84d6d03e7cf875b934299f1ece399f13a94765e`. One [JSON source/candidate evidence inventory](../reports/NASH_PHRASE_BACKFILL_E112_E128_2026-10-31.json): **83,873 bytes**, SHA-256 `23626292957047360daf82bd5dcbcff9af704f6ccad539cb24b04750caf97a98`. Prior approval/biography/title work preserved. No full-register backup required for these bounded additions, evidence corrections and delimiter repairs.

  - **Scope and method:** Reused the [historic E000-E111 discovery method](../reports/NASH_PHRASE_BACKFILL_E000_E111_2026-10-23.md), keeping that report and its hard ceiling historically intact. Computationally parsed **32 complete local P/Q exports for 16 corrected Wastes episodes, E112-E126 and E128**; excluded E127's separate one-off. **9,218,724 source bytes**, exact per-file paths, byte sizes, cue counts, final clocks and SHA-256 values in the new JSON. Strong rhyme/incantation/magic-word motifs plus generic speech cues within 90 seconds of spell/casting terms yielded **238 cue candidates: 115 P and 123 Q**. Read **all 115 primary-candidate contexts and all 22 secondary strong-motif contexts**, plus named paired passages for E112's other-character rhymes and **NSP-041/042/043/044/012**. **738 distinct source cues** occur in the read windows. Generic secondary candidates were indexed but **not all independently read**. Source reading/checkpoints proceeded in E114-E116, E117-E119, E120-E121, E122-E124, E125-E126/E128, then E112-E113 contextual groups, with supplemental paired windows and durable cue records. This is targeted keyword discovery, **not** full semantic/audio review or proof of absence/first use.
  - **Finding/attribution outcome:** **No new original-Nash incantation located; all 48 permanent NSP IDs retained**, without duplicate discoveries for already indexed later spells. E112's rhyming *Conjure Animals* is **Scott as Blood Skunk**, demonstrating why actor/speaker label does not establish Nash. E113 remains Hope's separated party. E114's two labor poems and E115's Jon frog joke retain their non-casting/other-performer classifications. E116 kneeling/ear-offering dialogue is not a spell. Strengthened the E118 Stanley/Hope childhood-song/key ritual, E119 recap of that ritual and E128 **Stanley** incantation exclusions; E123 mending invocation belongs to another caster. The inventory records each episode's actual disposition, including false motif hits such as `presto` inside the descriptor `Preston`. Existing S2/S3 regular reviews/seeds were retained, not re-researched by this S1-only extension; deeper sequential/listening review remains separate.
  - **NSP-041 precision repair:** Local P **457-459** (~00:26:28.730-00:26:43.930) reads an excerpt beginning `this / punt ... and now give / real ... haste`; local Q **737-739** (~00:26:31.560-00:26:43.720) gives `hunt`, `Vorrel` and `I now give`. Both have surrounding actual *Haste* adjudication (P457-463 / Q735-746), distinct from earlier preparedness/verbal-component discussion. Added exact cue IDs, quoted current local wording without fixing the grammar/name, and **retained the prior P hunt/Vorel rendering as prior-note provenance**. Did not claim identical older remote bytes, source-file drift, audio accuracy or a new cast. All **47 other finding rows remain text-identical**.
  - **Validation and baseline repair:** 48 unique unchanged finding IDs, all **7 headings**, all previous inline/reference link occurrences and source-reference definitions preserved. **275 local link occurrences / 218 distinct destination paths**, all present; two fragment URLs matched to source-heading spelling, with native browser behavior untested. JSON parses, contains 32 unique source paths / 16 episode IDs, and every expected primary/secondary-strong candidate is represented in the recorded read windows; **32/32 source SHA-256 values unchanged**. Local micromark/GFM-table rendering: four consistent tables (**43 rows x 4 columns, 7 x 4, 6 x 3, 45 x 3**, including headers). First changed-file Markdownlint exposed **four pre-existing MD056 defects** in S3E12-S3E15 evidence rows; verified their two-cell form in HEAD, then inserted **only the missing evidence-column delimiter in each**, preserving wording and links under D-047/D-081. Final register Markdownlint exit 0, 0 violations; scoped Git whitespace check exit 0. Final task/manifest control checks and persisted readback close the record.
  - **Limits and next action:** No original audio listened to, source/ASR mutation, new ASR run, complete secondary semantic read, accuracy/WER measurement or exhaustive spell/phrase claim. Native browser/alias behavior remains [WCL-103](#wcl-103). No episode/biography/narrative/title-register/entity-data changes in this slice, no per-stage reports or duplicate snapshots, no commit/push/publication. Next selected task: [WCL-052](#wcl-052), inventory Badass T's existing coverage and later appearances before proposing any duplicate/additional page.

### WCL-052

- [x] **Determine Badass T's needed character coverage.** Completed **read-only inventory and source-boundary decision, 2026-10-31**, `main` HEAD `1185b17`. **Parent:** [WCL-031](#wcl-031). **Disposition:** a dedicated Badass T reader profile is warranted, separately tracked as [WCL-120](#wcl-120) under existing D-081 approval. Do not merge him with original Tedna or presume a later rescue/cure. Existing [Tedna profile](../world/characters/tedna.md) remains **8,336 bytes / 37 lines**, SHA-256 `33b91821dfadbce459e9e75762d04d32dc0d8f834bb4d61486178459d8d7ff67`, all 37 lines read; no pre-audit backup needed.

  - **Existing coverage/gap:** No dedicated Badass T filename or entity-pilot record found. `tedna.md` gives the original youthful follower's E027-E050 life/death, followed by six reverse-chronological S2E04-S2E09 alternate-counterpart studies and March 2022 creator commentary. The character index has original Tedna and a combined **P0D/Tedna alternate counterparts** E110 row, but no dedicated Badass T navigation and no current last-state summary. New coverage should supply the missing **E106 masked guide / E110 identity and custody** history, chronological development and final supported condition, while keeping the old Tedna path/source notes compatible.
  - **Identity and actions checked:** [E106](../episodes/E106.md) L12-21 introduces the masked contractor, directly witnesses his killing of the Mangler, performs the portal rite and only **implies** the frog vendor's killing; [E110](../episodes/E110.md) L15-18/L38-39 physically unmasks an alternate Tedna, leaves him and alternate P0D at First Nash's tower and entrusts Hope's weapons/belt to him. This does not resurrect original Tedna. [S2E04](../episodes/S2E04.md) L26-27/L31 encounters Badass T again at Planet Nash and actually returns the ammunition belt; [S2E05](../episodes/S2E05.md) L11-20/L27 contains later **NPC testimony** about a Chronos-connected helper moving him between realities, actual boarding and his claimed older age/Liberator training. Do not treat the S2E04 unresolved travel question as an eternal absence of explanation, or NPC cosmic exposition as witnessed mechanics. Pistols and returned belt remain distinct items.
  - **Last direct state versus mentions:** [S2E06](../episodes/S2E06.md) L15/L27-28/L36 frees him from raider cages; [S2E07](../episodes/S2E07.md) L12/L20-22/L28 ends at his voluntary shaft jump; [S2E08](../episodes/S2E08.md) L11/L14/L17-25 shows him alive and assisting the rope rescue. [S2E09](../episodes/S2E09.md) L12-18/L28 establishes severe injury, **Stanley's actual stabilization**, visible fur and **Tilly's lycanthropy claim**, then the party leaving him unconscious in their care. Werefolk name/token assignments are muddled in the dossiers; do not certify a disputed attacker identity. S2E10/S2E11/S2E12 and S3E01/S3E02 only retain that unresolved state; **S2E12 explicitly leaves him out of the successful teleport/escape roster**. S3E13's proposed consultation is not a visit or rescue. E111/E117/E123 mentions are remembrance/custody dialogue, not new physical appearances. February 2022 intake discussion reveals no fate; March 2022 regrowth discussion remains undecided creator preparation; April's drink recipe and Vorel transformation idea are jokes/counterfactuals, not Badass T developments. July/August 2020 comments likewise do not restore the original dead Tedna or add a played reunion.
  - **Scope/limits and follow-up:** Dossier alias inventory checked Badass T/Bad Ass T/Badass Tea/Badast/Tedna references in the available episode Markdown, with matched later windows read and bonus evidence classified. This is **curated-dossier coverage**, not fresh full-recording/ASR or original-audio verification, exhaustive alias completeness or proof no unindexed appearance exists. A malformed read command raised Python SyntaxError before executing; reread through the still-viable local route, with no partial write or lost source operation. WCL-120 may share this completed evidence to create a separate in-world profile plus bounded character-index integration, leaving Tedna's exact bytes, historical source notes and entity pilot unchanged. The parent WCL-031 remains open.

### WCL-053

- [x] **Audit the distinct T'ietkalla historical study.** Completed **2026-10-31**, read-only structural/source-horizon audit at `main` HEAD `d13b9c5`, **25/25 lines**, **3,305 bytes**, SHA-256 `0201712ec682befe13888df477cccc74d025aa092b1f171aa20bc3767a6be220`. **Parent:** [WCL-033](#wcl-033). [Historical study](../world/HISTORY_TIETKALLA.md) is a **distinct thematic history**, not a duplicate of the [place profile](../world/places/tietkalla.md): its ancient royal testimony, conflicting Akmenos/Kefeli/Monsoon accounts, legitimacy, social reform, invasion and displacement warrant separate treatment. The city profile already covers site detail, the earlier government, refugee evidence and the **played S3E18** return. The history study currently stops at **E118**; its `Tietkalla` display title (rather than map-backed **T'ietkalla**), opening ASR/spoiler apparatus, visible episode IDs, obsolete `Principle` name and absent post-E118 final legacy do not meet D-048 or the campaign-end horizon. The [historical-events index](../world/HISTORICAL_EVENTS.md) also still uses the older display and ends at E128; handle its comprehensive index audit under [WCL-114](#wcl-114), not as an invented full update here.

  - **Evidence/limits:** Compared complete 25-line history and 111-line city page, plus [E117](../episodes/E117.md), [E118](../episodes/E118.md) and [S3E18](../episodes/S3E18.md) dossiers; compared governing [reader-first standard](READER_FIRST_PRESENTATION.md) and historical study style. Original historical body has **five headings**, **zero footnote definitions**, and a final `Open:` process/uncertainty line instead of `Lasting legacy`; no demonstrated need to merge or delete it. Literal `HISTORY_TIETKALLA.md#` searches found **0** matches in `world/` (140 files), `narrative/` (20 files) and `project/` (227 files), not proof of absent external anchors. No audio listening, exhaustive link/other-directory scan or browser alias verification. **Disposition:** approved standalone reader-first rewrite [WCL-121](#wcl-121) under standing D-081, preserving one exact pre-edit working-copy baseline and original distinct uncertainty/source links. No change to the historical article was made by this audit.

### WCL-054

- [x] **Audit the CHIDS crisis history and reference presentation.** Completed **2026-10-31** as a read-only 21/21-line structural/source-cutoff audit, `main` HEAD `d13b9c5`, **2,769 bytes**, SHA-256 `88cc1640d342ccacec1ca4833dab334a41cfae5ec34e0f461a7bccb8e7ee36a7`. **Parent:** [WCL-033](#wcl-033). [History](../world/HISTORY_CHIDS_DRIVE.md) is a **separate historical study** of CHIDS's abusive institutional program, conflicting accounts and the group's sacrifice; its scope differs from the [CHIDS site record](../world/places/chids.md) (complex/layout/encounters) and [Traversal Drive technical entry](../world/technology/traversal-drive.md) (physical controls and operating cutoff). It is **not** an intentional source-first register exception: the current introduction is metadata-first, headings and body show recording episode IDs, the ending is `Open:` and research limitations are in main prose rather than footnotes. The original three H2 headings are useful stable anchors. Recommend a distinct **reader-first historical rewrite** [WCL-122](#wcl-122), authorized by D-081, with an exact working-copy original preserved first, and original heading/link compatibility retained.

  - **Observed evidence and limits:** Read full history, full 25-line Drive technical entry, relevant CHIDS facility/location reference sections and focused [E077](../episodes/E077.md)–[E082](../episodes/E082.md) source dossiers. Actual laboratory lizardfolk training/memory-conditioning systems and GR0X1-labelled vessel are observed; alleged species creation, divine projects, human archive origins, future Wall Nash and ancient planet-moving mechanisms remain attributed to Cerinthala, the hive or the dragon. Portable paired portal apparatus **is not the Traversal Drive**. E081 documents Dolo Popio's manifested defeat, Sira's rescue, Chance's unlocated disappearance and the four heroes' actual voluntary crimson-beam exposure and **GM death declaration**. [E082](../episodes/E082.md) separately shows **Vorel alive**, **Nash conscious as a floating heart**, **Hope motionless** and **Stanley cold and described dead**; no claim all four revived then. Subsequent played [S3E18](../episodes/S3E18.md) restores Earth's environment but does **not** directly demonstrate the ancient Drive's final mechanism or physical shutdown. The GM's later retrospective accounts are not new played CHIDS events. Literal deep-link search for `HISTORY_CHIDS_DRIVE.md#` returned **0** matches in `world/` and `narrative/`, not a guarantee about external or all inbound links. Original audio, a complete site-source census and browser navigation remain unchecked. No CHIDS article changes were made as part of this audit.

## Identified subtasks — Peoples, inventory and places

### WCL-055

- [x] **Assess Lactids as a people/culture subject.** Completed 2026-10-31. **Parent:** [WCL-012](#wcl-012). **Disposition:** defer a new race/culture article; retain the Lactid Cartel as a faction, not as a stand-in for a population. Updated [Races](../world/RACES.md) with source-linked distinctions between played activity, NPC testimony and unused GM preparation. No new entity records or assumed cultural traits.

  - **Evidence and limits:** [E013](../episodes/E013.md) documents cartel-linked activity and Stump's interpretation; [E026](../episodes/E026.md) reports Bertrand's alleged Principal City underworld and mental influence; [E039](../episodes/E039.md) records Monsoon's disputed exile account; [E054](../episodes/E054.md) discusses a possible later threat rather than a direct encounter. [S3E019](../episodes/S3E019.md) gives Beau's retrospective description of a cockroach-like underground society and other **unused Principal City plans**, not a played visit. The owner's `Laktid` spelling in [owner notes](OWNER_EPISODE_NOTES.md) remains unconfirmed; [name audit](../reports/PRINCIPAL_RELATED_NAMES_AUDIT_2026-10-27.md) recommends the current editorial `Lactid`. The focused episode, narrative, existing Races/Factions and reference searches do not establish population-wide social institutions, traits or direct observations. This is a dossier-level assessment; exhaustive source ASR and original audio remain unverified.

  - **Checks and recovery:** Changed only the Races index's closing notes, preserving its two published people rows and Harlequinari's separate open question. Revised `world/RACES.md`: 3,479 bytes, 24 lines, SHA-256 `9958d14d1586f52f5e58e82d6af904be24f37e5a543a5bb21b2970968bf846a1`. Markdownlint exit 0 (zero violations); offline renderer checked 23 local links, 0 broken, and all three original H2 headings remain. No race article, entity migration, backup, source edit, commit or publication. **Next:** [WCL-056](#wcl-056); parent [WCL-012](#wcl-012) remains open.

### WCL-056

- [x] **Assess Harlequinari as a people/culture subject.** Completed **2026-10-31**, dossier and targeted dual-ASR review at `main` HEAD `d13b9c5`, with explicit consideration of the owner's **Council of Clowns–Harlequinari hypothesis**. **Parent:** [WCL-012](#wcl-012). **Disposition:** distinct people/culture coverage is supported, but **the Council's complete species membership is not proved**. Author a narrowly qualified reader-first culture page under follow-up [WCL-123](#wcl-123), linking the Council as an affiliated institution, not equating a faction's entire membership with a people.

  - **Evidence:** [E113](../episodes/E113.md) explicitly shows Blood Skunk identifying himself as Harlequinari to ferryman Hesterbrook (about **01:04**), being treated as an exile (**01:10–01:11**), and telling the Council of Clowns that he had **left the Harlequinari long ago and no longer served them** (about **02:23**). Bobo and the council speak of a wider **Harlequinari world**, and mention **many Harlequinari** who could attend a proposed humor workshop (about **02:17**), so an in-world cultural community and connection with the Council are evidenced. The potentially misleading line **“a Harlequinari on your council”** (about **02:22**) is directed **to Hope about Blood Skunk among her companions**; it is not identification of all thirteen official Council members. Both [Parakeet](../sources/The%20Wastes%20S1E113.%20I%20Need%20To%20Smell%20Your%20Hand.parakeet.processed.srt) and [Qwen-labelled](../sources/The%20Wastes%20S1E113.%20I%20Need%20To%20Smell%20Your%20Hand.qwen-q8.canary-ctc.nemotron.srt) SRT windows were read and compared for those lines. [E088](../episodes/E088.md) establishes the Council's valued cruel trickery through Kidigree's account; [E103](../episodes/E103.md) features a **Blood Skunk-specific** `Critical Fortunes` mechanic, not a verified universal trait. The [September bonus](../episodes/BONUS-2020-09.md) has an ASR-disputed identity clause that cannot nullify E113's later direct self-identification. The Council itself appears in Pandemonium and is distinct from the broader population; no population census, uniform physiology, inherited rules, place of birth or racial status of each councilor was provided. No original audio audition, complete SRT concordance or independent designer rules sheet; spellings/attributions remain provisional.

  - **Result:** The race-versus-faction distinction is better supported than the original tentative Races-index note suggested. [WCL-123](#wcl-123) owns the source-footnoted new article and careful navigation/cross-link repairs. The audit itself makes no world-article changes; completed only after this source comparison. **Next dependent work:** [WCL-123](#wcl-123), then [WCL-057](#wcl-057).

### WCL-057

- [x] **Assess elves as a people/culture subject.** Completed **2026-10-31**, bounded played-source and existing-world review at `main` HEAD `d13b9c5`. **Parent:** [WCL-012](#wcl-012). **Disposition:** source evidence supports a **limited elves-as-a-people study centred on the observed Elhandari community**, rather than equating all elves with the Elhandari institution or turning an isolated biography into a species-wide rule. Add a separate reader-first [Elves](../world/races/elves.md) profile under [WCL-124](#wcl-124), keeping named individuals' pages, [Elhandar](../world/places/elhandar.md) and [Elhandari faction](../world/FACTIONS_AND_POWERS.md) separate.

  - **Evidence and boundaries:** [E115](../episodes/E115.md) observes an elven space station, **thousands** welcoming the company, a living biodome, advanced transport/medical care, Admiral Chrysorius, a spiritual elder, voluntary therapeutic attendance after assignment, and the elder's **attributed** ideas on ancient history, ecology and elven death. [E118](../episodes/E118.md) reveals Stanley's Or'Nath family links, not all elves' lineage; [E119](../episodes/E119.md)–[E121](../episodes/E121.md) include individual hostile/disguised elves, not proof the whole sanctuary conspires. [E125](../episodes/E125.md)–[E128](../episodes/E128.md) actually show defense, devastation, survival, refugees boarding Elhandari ships for Mars, and departure; a completed Martian arrival **does not** occur in E128. [S2E03](../episodes/S2E03.md) shows the existing Mars community, council and the **public election of first half-elf Stanley** to the Prime office; [S2E04](../episodes/S2E04.md) documents his delegation to Amanthalodar. [S3E18](../episodes/S3E18.md) closes with **some Elhandari entering the Feywild with Stanley, others remaining on Mars or returning to Earth**. Distinguish a local civic history and political ecology from inherited universal elf physiology, magic, lifespans or beliefs. Cerinthala and the hostile Dilo group are separate individuals; their membership or deeds cannot define Elhandari society. The supporting [Elhandar site](../world/places/elhandar.md) itself stops its current-status narrative at E128: its later-source-horizon review belongs to the independent world-file inventory [WCL-063](#wcl-063), not silently rewritten here. No new audio listening or exhaustive elf concordance; claims remain dossier/ASR provisional. Audit no change to subject prose; the separately checkable creation/cross-link work is [WCL-124](#wcl-124).

### WCL-058

- [x] **Assess dwarves as a people/culture subject.** Completed **2026-10-31** from focused existing episode dossiers, narrative and world indexes at `main` HEAD `d13b9c5`. **Parent:** [WCL-012](#wcl-012). **Disposition:** a bounded dwarven people/culture profile is justified by **multiple distinct witnessed settlements**, but no one clan, mining company, ruin, trade crew, ruler or character represents all dwarves. A separately checkable source-footnoted [Dwarves profile](../world/races/dwarves.md) and reciprocal navigation are assigned to [WCL-125](#wcl-125).

  - **Evidence:** [E003](../episodes/E003.md)–[E005](../episodes/E005.md) show an ancient underground **dwarven settlement**, skeletons continuing ordinary routines, an active medical automaton C4N-D13 and a queen under Quizquaz's control. **Moag Ferhain** is owner-accepted map spelling, but the mapped place's identity with the ruins is **not proved**; Quizquaz's historical explanation is attributed, not accepted wholesale. [E018](../episodes/E018.md), [E019](../episodes/E019.md), [E025](../episodes/E025.md) and [E026](../episodes/E026.md) show the **Oilbeard dwarf guards/ownership at Black Mine** and actual cruel coercion of captive Tickles, together with allegations of a miner uprising and later confrontations; the Oilbeard clan's conduct is **not a dwarven norm**. [S2E05](../episodes/S2E05.md)–[S2E06](../episodes/S2E06.md) witness **Burp on Blast Belly Rock**, dwarf innkeeper Ailboon Hardbottom at the Wet Whistle, an old mithril economy, abandoned banking institutions, surviving residents captured by raiders and freed, and a signed **Tungsten Wheel employment agreement**; source-specific town history and innkeeper's older recollections remain distinct. [S3E02](../episodes/S3E02.md) establishes the dwarves have departed from Burp by the later visit, without proving deaths or destination. [E098](../episodes/E098.md) has an individual dwarf weaponsmith; [E116](../episodes/E116.md) a **dwarven trade frigate** whose resisting crew is attacked by Hope's separate party and whose ship is **not seized**. These demonstrate craft and commerce in specific contexts, not an inherited universal dwarf identity or a common political culture. Dossier/processed-ASR evidence only; original audio, complete species census and independent historical interpretation not newly checked. Separate page and notes: [WCL-125](#wcl-125).

### WCL-059

- [x] **Assess orcs and Kuromokishi culture coverage.** Completed **2026-10-31** from targeted played episode dossiers, the Races/Factions indexes and place references at `main` HEAD `d13b9c5`. **Parent:** [WCL-012](#wcl-012). **Disposition:** create a **bounded Orcs people profile** via [WCL-126](#wcl-126), documenting differentiated allegiances rather than inventing common species customs or assigning all orcs to a chrome military caste. **Koromukishi/Kuromukishi** is first described as a **Principal-aligned martial order with initiates, a trial-by-combat role and an invitation to outsiders**; it is therefore a faction/career, not an independent race. Its later elite orc fighters operate within a technologically armed regime, but no universal chrome implantation or inherited racial mechanic was proved.

  - **Evidence:** [E010](../episodes/E010.md) sees armed orc-led Principal forces seize travelers, then five orc initiates opposed in the Rusty Cage. [E011](../episodes/E011.md) shows Lady Saltbubble and Sir Chickenfinger offering membership after a ceremonial acquittal. [E013](../episodes/E013.md) gives the GM's out-of-character distinction between the broader **Toyota Host** army and fewer Koromukishi honor-code officers. [E026](../episodes/E026.md)–[E027](../episodes/E027.md) present the **sightless, voluntarily nameless former member** who says he renounced the order's teachings and sides with the Liberators; his views on orcish culture and reform remain his testimony. Separate non-order orcs include mixed-faction armed escorts to [Sigil](../episodes/E102.md)–[E105](../episodes/E105.md), the **Green Vale/Greenveil** marauders and three surrendering new sailors in [S2E06](../episodes/S2E06.md), their actual deaths during [S2E07](../episodes/S2E07.md), and a Gray Waste orc whose detached head stays responsive in [E113](../episodes/E113.md), not proof of universal orc immortality. [S3E06](../episodes/S3E06.md) directly fights eight Kuromokishi with an Umbilical Order Paladin; [S3E09](../episodes/S3E09.md) and [S3E10](../episodes/S3E10.md) show additional squads. The **S3E18 played council** assigns captured/surviving Kuromokishi to Vorel's lizardfolk to pursue social reintegration, and a group **actually begins the journey** toward [Razak Val](../world/places/razak-val.md), without a completed settlement, coerced universal conversion or species census. Existing written forms `Koromukishi`, `Kuromukishi`, `Kuromokishi`, `Kuro-makishi` vary in ASR, and exact orthography/individual lineage still awaits original-audio or owner-source confirmation. No original recordings freshly listened to. Scope and navigation delivery tracked separately as [WCL-126](#wcl-126).

### WCL-060

- [ ] **Assess illithids as a people/culture subject.** Determine whether observed evidence supports a people entry, creature classification or cross-link only. **Parent:** [WCL-012](#wcl-012). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-061

- [ ] **Assess pixies as a people/culture subject.** Separate P0D/Diontalus-specific biography from evidenced Feywild/pixie cultural claims. **Parent:** [WCL-012](#wcl-012). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-062

- [ ] **Reconcile the historic 134/134 world-file first-pass census.** Confirm actual 2026-10-27 first-pass work without falsely treating it as full current inventory or D-048/audio acceptance. **Parent:** [WCL-013](#wcl-013). **Evidence:** [reference](../research/legacy/WASTES_CLEANUP_MANIFEST_PRE_TASK_REGISTER_2026-10-31.md).

### WCL-063

- [ ] **Reconcile today's world file list and per-file dispositions.** Enumerate present paths and added subjects with type, first/last source, reader-first state, links and unknowns. **Parent:** [WCL-013](#wcl-013). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-064

- [ ] **Review Planet Nash place coverage.** Assess existing page versus end-of-campaign family residence/retirement evidence; avoid duplicate entry. **Parent:** [WCL-017](#wcl-017). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-065

- [ ] **Review Pentel Weiss place/prison coverage.** Assess chronology and final condition against existing references and decide page/index treatment. **Parent:** [WCL-017](#wcl-017). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-066

- [ ] **Review Mars settlements and terraforming-platform references.** Differentiate actual Mars sites, refugee resettlement and Elhandari presence without fabricated geography. **Parent:** [WCL-017](#wcl-017). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-067

- [ ] **Review smaller Solar Mines facilities and locations.** Separate the core, guarded Ruby room and other facilities into appropriately linked subjects. **Parent:** [WCL-017](#wcl-017). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-068

- [ ] **Build Known Wastes v3 map-label crosswalk.** Record labels, regions, map edition/source and evidence limits without invented coordinates or release permissions. **Parent:** [WCL-018](#wcl-018). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-069

- [ ] **Distinguish Principal City from The Principal's Lands.** Reconcile city testimony versus map territory and S3E019 unused prep, without claiming a played city visit. **Parent:** [WCL-018](#wcl-018). **Evidence:** [reference](../episodes/S3E019.md).

## Identified subtasks — Factions and world-resolution events

### WCL-070

- [ ] **Audit the Council of Earthly Defenders as faction.** Check actual wartime council scenes, membership and already existing index/page coverage. **Parent:** [WCL-033](#wcl-033). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-071

- [ ] **Audit the Council of Faces as a faction.** Separate witnessed coercive successor process from Council's self-reported ancient-human origin. **Parent:** [WCL-033](#wcl-033). **Evidence:** [reference](../episodes/S3E18.md).

### WCL-072

- [ ] **Audit the Umbilical Order as faction/facility.** Distinguish finale commission to clear the facility from a completed witnessed operation. **Parent:** [WCL-033](#wcl-033). **Evidence:** [reference](../episodes/S3E18.md).

### WCL-073

- [ ] **Assess Arcanum Universalis survival and coverage.** Keep real in-story observations distinct from unused Principal City creator preparation. **Parent:** [WCL-033](#wcl-033). **Evidence:** [reference](../episodes/S3E019.md).

### WCL-074

- [ ] **Document the fall of Elhandar as historical event.** Distinguish structural destruction, survivor evacuation and later Elhandari continuation. **Parent:** [WCL-040](#wcl-040). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-075

- [ ] **Reconcile Worldbreaker's entry and Earth-only permanent banishment.** Trace E128, S3E15–17 actual events and completion, distinct from restoration in S3E18. **Parent:** [WCL-040](#wcl-040). **Evidence:** [reference](../episodes/S3E17.md).

### WCL-076

- [ ] **Reconcile S3E18 Earth's restoration and magic changes.** Document actual Triangulosphere activation, green Earth and on/off-world spellcasting evidence. **Parent:** [WCL-040](#wcl-040). **Evidence:** [reference](../episodes/S3E18.md).

### WCL-077

- [ ] **Preserve uncertainty around the apparent second Nash.** Check character/family/antagonist pages do not assert the final visitor's or warned-of person's identity. **Parent:** [WCL-032](#wcl-032). **Evidence:** [reference](../episodes/S3E18.md).

### WCL-078

- [ ] **Reconcile recording order, fictional chronology and time of knowledge.** Check E013.5, E043/E127, E107–109 and E101 with explicit distinct temporal interpretations. **Parent:** [WCL-040](#wcl-040). **Evidence:** [reference](../world/CHRONOLOGY.md).

## Identified subtasks — Technology and source verification

### WCL-079

- [ ] **Review the Rubistic Triangulosphere's last placement and activation.** Separate guarded but unactivated core period from S3E18 witnessed use, unknown final physical custody. **Parent:** [WCL-021](#wcl-021). **Evidence:** [reference](../episodes/S3E18.md).

### WCL-080

- [ ] **Reconcile Hand of the Voice versus the separate Fist.** Check Tobacho, Hope, Principal and Brett custody while preserving two distinct physical items. **Parent:** [WCL-021](#wcl-021). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-081

- [ ] **Inventory genuinely unresolved finale object custody.** Identify remaining uncertain holders/charges for windboards, Hollow Ring, syringes, staffs and other items without repeating completed corrections. **Parent:** [WCL-021](#wcl-021). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-082

- [ ] **Review E039 mind-reading potion transfer for Arc 03 relevance.** Identify downstream actual use or story consequence before proposing any narrative insertion. **Parent:** [WCL-040](#wcl-040). **Evidence:** [reference](../episodes/E039.md).

### WCL-083

- [ ] **Verify the Principal's S3E14 longer self-spoken title.** Resolve Chrome Ascendantrix/Vladomotrix ASR variation only from original audio, preserving canonical display title. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](../episodes/S3E14.md).

### WCL-084

- [ ] **Resolve Worldbreaker's S3E15–16 conflicting fire rulings.** Review successful S3E15 Fireballs against S3E16 fire immunity before harmonizing any source claims. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](../episodes/S3E16.md).

### WCL-085

- [ ] **Resolve S3E17–18 Wish-recovery day discrepancy.** Check explicit seven-day stress versus four days elapsed and retain possible GM retcon until verified. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](../episodes/S3E18.md).

### WCL-086

- [ ] **Triage E000–E001 prologue and introduction audio windows.** Use existing issue IDs and exact recorded windows for consequential source/identity questions. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](REVIEW_QUEUE.md).

### WCL-087

- [ ] **Triage E022–E024 Soulbroker pact audio windows.** Check physical signatories, Vorel refusal and later contract/soul interpretations at their own source cutoffs. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](REVIEW_QUEUE.md).

### WCL-088

- [ ] **Triage E048–E054 deaths, rescue and coronation windows.** Distinguish false reports, actual rescues, competing claims and T'ietkalla chronology. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](REVIEW_QUEUE.md).

### WCL-089

- [ ] **Triage E066/E079–E081 CHIDS source windows.** Verify high-impact machine, chronology and knowledge-boundary claims from bounded evidence. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](REVIEW_QUEUE.md).

### WCL-090

- [ ] **Triage E101–E116 party-split source windows.** Preserve E101 boundary, private knowledge and simultaneous event distinction. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](REVIEW_QUEUE.md).

### WCL-091

- [ ] **Triage S2E01–S3E03 space-voyage source windows.** Focus on Nash regeneration, Principal paternity story, Hand seizure and shared dream provenance. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](REVIEW_QUEUE.md).

### WCL-092

- [ ] **Triage S3E12–S3E18 finale source windows.** Select consequential infernal, Worldbreaker, Nash resurrection and final warning questions by existing issue IDs. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](REVIEW_QUEUE.md).

### WCL-093

- [ ] **Review S3E019 unused ideas versus played canon.** Keep cast retrospective and unused Principal City western dungeon/railway ideas clearly outside played history. **Parent:** [WCL-037](#wcl-037). **Evidence:** [reference](../episodes/S3E019.md).

## Identified subtasks — Evidence maintenance, links and reader acceptance

### WCL-094

- [ ] **Distill current actionable issues from REVIEW_QUEUE.md.** Keep stable issue IDs, retire stale next-episode instructions and distinguish ASR-complete from audio-verified. **Parent:** [WCL-036](#wcl-036). **Evidence:** [reference](REVIEW_QUEUE.md).

### WCL-095

- [ ] **Distill unresolved claims from CONSISTENCY_LEDGER.md.** Separate genuinely open identity, contract and custody questions from historical already superseded cutoffs. **Parent:** [WCL-036](#wcl-036). **Evidence:** [reference](../world/CONSISTENCY_LEDGER.md).

### WCL-096

- [ ] **Audit Principal/Principle display spellings and aliases.** Extend scoped character/chronology corrections across remaining maintained prose without modifying stable slugs or original sources. **Parent:** [WCL-034](#wcl-034). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-097

- [ ] **Audit Khaervilon/Kervalon and mapped place-name aliases.** Use confirmed map orthography, preserving compatibility path and distinguishing written spelling from pronunciation. **Parent:** [WCL-034](#wcl-034). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-098

- [ ] **Audit Or'Nath family and villa names.** Keep Valiir, Delit and Villa Or'Nath distinct and backed by owner-authored evidence. **Parent:** [WCL-034](#wcl-034). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-099

- [ ] **Plan stable-ID index expansion beyond v2 Races pilot.** Inventory consumer compatibility and missing entity types, IDs, aliases and relationships without silent schema breakage. **Parent:** [WCL-035](#wcl-035). **Evidence:** [reference](../world/ENTITY_SCHEMA.md).

### WCL-100

- [ ] **Add only documented relationships and custody edges.** Validate kinship, membership, observations and item ownership with episodes and avoid disputed genealogy. **Parent:** [WCL-035](#wcl-035). **Evidence:** [reference](../world/entities.json).

### WCL-101

- [x] **Validate Nash biography links past the renderer's 100-link cap.** Completed 2026-10-31 at `main` HEAD `076e1d5` against the [WCL-030 revised biography](../world/characters/nash-maggard.md), measured 85,458 bytes / SHA-256 `a041a4c2081ece18b4d274b4d8fc29ff446bb10d8035e2fa197edf57af220d38`. Full 320-line source enumerated **264 local Markdown-link occurrences** (165 distinct paths) outside fenced blocks. Offline renderer already checked **100/264**, **0 broken**; independently checked the other **164 occurrences** across **122 distinct paths** using four bounded batches of 40/40/40/2 `verify_workspace_files` entries: **122 measured, 0 absent/incomplete**. There are **0 explicit `#fragment` destinations** in these 264 links, so no linked-heading fragments to validate under this task. All 48 distinct newly authored link paths had also passed WCL-030 preflight. **Limit:** file existence and offline renderer coverage, not native GitHub/browser click-through or legacy alias behavior ([WCL-103](#wcl-103)); no audio/factual review. **Parent:** [WCL-038](#wcl-038).

### WCL-102

- [x] **Validate chronology links past the renderer's 100-link cap.** Completed 2026-10-31 at `main` HEAD `076e1d5` for the unchanged [source-keyed chronology](../world/CHRONOLOGY.md) (302 lines, **188,159 bytes**, SHA-256 `01ebcc89072df41033f12e6bb13a76ba85523eabc44e87db57abdfa5f650c42d`). Enumerated **310 local Markdown-link occurrences** (252 distinct paths) outside fenced blocks. Offline renderer checked **100/310**, **0 broken**; the other **210 occurrences** span **178 distinct paths** and were independently checked using `verify_workspace_files` in four bounded batches (45/45/45/43): **178 measured, 0 missing/incomplete**. Exactly **one explicit heading fragment** occurs in the whole file, `../narrative/README.md#historic-first-edition--six-arcs` (among the first 100); independently confirmed the rendered destination contains `id="historic-first-edition--six-arcs"`. **Limit:** file existence and offline-renderer heading compatibility, not an actual native GitHub/browser walkthrough or legacy raw-HTML alias behavior (still open [WCL-103](#wcl-103)). No source chronology, date cutoffs or narrative prose changed; no audio/factual verification implied. **Parent:** [WCL-038](#wcl-038).

### WCL-103

- [ ] **Test legacy raw-HTML aliases in native reader rendering.** Verify original inbound fragments in actual GitHub/browser output; offline renderer strips aliases. **Parent:** [WCL-038](#wcl-038). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-104

- [ ] **Run deferred desktop interactive reader walkthrough.** Check all eleven private arcs, anchors, intra-page and compatibility navigation in an actual browser. **Parent:** [WCL-007](#wcl-007). **Evidence:** [reference](../narrative/README.md).

### WCL-105

- [ ] **Run deferred narrow/mobile reader walkthrough.** Check real responsive navigation and link behavior rather than inferring it from Markdown lint. **Parent:** [WCL-007](#wcl-007). **Evidence:** [reference](../narrative/README.md).

### WCL-106

- [ ] **Audit root README reader-first ordering and campaign separation.** Keep shared Delvers/Inverse entry points while moving Wastes project metadata after reader navigation. **Parent:** [WCL-039](#wcl-039). **Evidence:** [reference](../README.md).

### WCL-107

- [ ] **Audit Wastes and narrative landing-page structure.** Preserve accepted eleven-arc order, historic compatibility links and bottom Sources/project notes. **Parent:** [WCL-039](#wcl-039). **Evidence:** [reference](../narrative/README.md).

### WCL-108

- [ ] **Audit world README and WORLD.md opening and final horizon.** Check world overview reader sequence, S3E18 developments and intentional technical exceptions. **Parent:** [WCL-039](#wcl-039). **Evidence:** [reference](../world/WORLD.md).

### WCL-109

- [ ] **Audit character and antagonist index presentations.** Check actor identities and final-status summaries without rewriting already verified content needlessly. **Parent:** [WCL-039](#wcl-039). **Evidence:** [reference](../world/CHARACTERS.md).

### WCL-110

- [ ] **Audit places index reader navigation.** Reconcile new place articles, regional aliases and latest known status after individual place audits. **Parent:** [WCL-039](#wcl-039). **Evidence:** [reference](../world/PLACES.md).

### WCL-111

- [ ] **Audit items/artifacts index reader navigation.** Favor meaningful equipment summaries and source footnotes over research-state headings. **Parent:** [WCL-039](#wcl-039). **Evidence:** [reference](../world/ITEMS_AND_ARTIFACTS.md).

### WCL-112

- [ ] **Audit faction/powers index reader navigation.** Separate institutions and sourced historic testimony across endgame changes. **Parent:** [WCL-039](#wcl-039). **Evidence:** [reference](../world/FACTIONS_AND_POWERS.md).

### WCL-113

- [ ] **Audit creatures/monsters index taxonomy and ordering.** Avoid treating intelligent peoples as generic monsters and retain first/last observation sources. **Parent:** [WCL-039](#wcl-039). **Evidence:** [reference](../world/CREATURES_AND_MONSTERS.md).

### WCL-114

- [ ] **Audit historical-events index presentation and exceptions.** Surface S3E18 world outcomes while preserving useful evidence-facing history functions. **Parent:** [WCL-039](#wcl-039). **Evidence:** [reference](../world/HISTORICAL_EVENTS.md).

### WCL-115

- [ ] **Develop bounded automatic reference/coverage diagnostics.** Test canonical name drift, missing final statuses, orphaned footnotes, broken fragments and unsupported high-impact claims; automated checks cannot settle canon. **Parent:** [WCL-041](#wcl-041). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-116

- [ ] **Create full-file acceptance/disposition matrix.** Document accepted/pending/technical-exception outcomes and actual verification limits for every in-scope maintained file. **Parent:** [WCL-041](#wcl-041). **Evidence:** [reference](WASTES_CAMPAIGN_CLEANUP_PLAN.md).

### WCL-117

- [x] **Restructure Hope Akmenos's biography into the approved eleven-arc reader-first account.** **Completed 2026-10-31**, owner-authorized `$twbd-wastes-cleanup` continuation and prior owner approval for `/world` edits; prerequisite [WCL-047](#wcl-047), parent [WCL-031](#wcl-031). [Revised biography](../world/characters/hope-akmenos.md): **69,817 bytes**, SHA-256 `04ec19efd3c2b6d072fcf96b5b805972c0d5bb75b3d5a305f4a9e1ebb73db66d`. The exact **52,517-byte** then-current original was preserved *before editing* at [pre-WCL117 baseline](../research/legacy/HOPE_AKMENOS_PRE_WCL117_2026-10-31.md), both original and copy SHA-256 verified `4f818286069774fb88475fa56443ba491292edeaa1f8a1ab6c748650d9088863`.

  - **Content/outcome:** New introduction, **eleven D-045 approved chronological arc sections**, character-focused relationships/abilities synthesis and S3E18 `Current status` (Hope alive as queen; **T'ietkalla still needs rebuilding**, Monsoon's actual helmet, Stanley's mask actually reshaped into a crown, future Fate Six control **after attunement**). Retains all differences among earlier prostheses, natural arms, stolen Voice Hand, Hollow Ring, *Diplomacy* and original firearms. Earlier five-arc text, equipment custody studies, retrospective/bonus notes and S2/S3 episode cutoffs are kept under `Sources and project notes` as historical research, not asserted as current. No original research claims upgraded to verified ancestry, maternal fate, Voice motive or future reunions.
  - **Preservation/anchors:** Numbered-line readback of **254/254 new lines** versus **177/177 exact baseline lines** confirmed the entire former source section after the first S3E18 heading remains **text-identical after reversing precisely two intentional heading edits**: `## Introduction` became `## Earlier five-arc introduction` (the legacy `#introduction` ID now belongs to the new main opening), and historical `## S3E18 — ... restored T'ietkalla ...` became `... rebuilding T'ietkalla ...` to correct the unsupported implication that city restoration was complete. **36/37 original heading texts still occur**, plus the live `#introduction` target; the old S3E18 fragment changed, so external/legacy browser links to that single original heading are **not confirmed compatible** and are deferred under [WCL-103](#wcl-103). The one exact pre-rewrite archive preserves its source and heading.
  - **Validation and limitations:** All **8 original footnote definitions** retained, **12 new** definitions added (20 total), all refs paired with definitions, none orphaned. All **171 original Markdown-link occurrences** preserved and **63 new** added: **234 local links / 171 distinct paths**. Independently measured existence for **all 171 distinct paths** via four bounded batches (45+45+45+36), **0 missing**; **no explicit `#fragment` links** on this page. Offline render: 53 unique headings, key current/legacy headings present, first 100 links checked with 0 broken, **134 occurrences above renderer cap** (their destination file existence independently checked). Targeted Markdownlint: exit 0, **0 violations**. Original audio and native GitHub/browser fragment behavior were **not** tested; the original-source body comparison is decoded-text equivalence, while the archived original's bytes were independently SHA-verified. No protected episode/narrative/other-character files were changed; no commit/push/publication.

### WCL-118

- [x] **Restructure Vorel's biography as an eleven-arc reader-first character study.** Completed **2026-10-31** under the owner's explicit standing approval for **all changes in `/world` and `/narrative`**, [D-081](DECISIONS.md#standing-approval-for-world-and-narrative-changes-2026-10-31). The earlier preflight approval hold is resolved and must not be requested again. **Parent:** [WCL-031](#wcl-031); prerequisite [WCL-048](#wcl-048). [Revised biography](../world/characters/vorel.md): **98,892 bytes / 369 lines**, SHA-256 `ffffeac4fc99443eb87b3ff3b34be631a7aa0236e859388fa094a02433934f09`. Reconciled against `main` HEAD `1185b17` after the prior Nash/Hope changes were committed externally; those pages and baselines were not edited by this slice.

  - **Preservation and trace:** Before biography edits, preserved the exact then-current working-copy original once at [pre-WCL118 baseline](../research/legacy/VOREL_PRE_WCL118_2026-10-31.md), **73,157 bytes / 243 lines**, SHA-256 `08a508f6c35d4fdb8b7a0a65be69e6ccb43cdad2829df3f28e99cf8c789bf2d2`; original/copy bytes independently compared. Read all original L1-243 in bounded windows and checked relevant early E001/E006/E023/E026/E027/E028/E036/E037/E049/E051-E054 and late S3E16/S3E18 dossier windows, with the D-045 crosswalk. The original body from its first S3E18 heading through its final original footnote remains **byte-identical**, including CRLF, in the closing collapsible historical-research appendix. The original H1 remains at the top. No old paragraph, source qualification, link occurrence or heading was removed or renamed.
  - **Outcome:** Opening introduction, eleven approved arc sections, relationship/principle synthesis and closing in-world `Current status`. Character development distinguishes Bok Bok's initial captivity from later companionship; refusal of soul pacts from acceptance of tools/help; actual Great Fang recognition from boasts; Stanley from Diontalus; early weapons and both helmets from final inventory; independent scale changes from the Eye. S3E18 state retains surviving Vorel, chrome plating, Eye/custody limits and Chrome's Bane; Nash's commissioned memorial precedes his actual resurrection; the journey **toward** rebuilding Razak Val includes surviving lizardfolk and Kuromokishi. Stanley's interpersonal Friend award remains distinct from offices and self-epithets. Original source-first studies and the one original footnote are intact in the research appendix; the separate titles register is unchanged. Arc prose counts **127, 156, 161, 191, 184, 186, 180, 168, 209, 217, 283**: the quiet opening is shorter and the multi-stage final war is longest, without exceeding twice the substantive-arc median. No episode IDs/ASR/GM labels occur in the new main story.
  - **Validation:** Full persisted-file comparison confirms **44/44 original heading texts retained**, **59 total unique heading texts**, all **205 original Markdown-link occurrences retained**, **111 added / 316 total**. All **168 distinct local destination paths** checked independently with **0 missing**; no explicit fragment URLs on the page. **15 footnote definitions / 15 references**, all paired, none orphaned, including the original `march21`. Local **micromark plus GFM-footnote** rendering yields 59 headings, a correctly bounded research disclosure, last main H2 `Current status`, and **30/30 generated footnote/backlink fragments resolving**. Targeted `node scripts/lint-markdown.mjs --files world/characters/vorel.md project/DECISIONS.md project/WASTES_CLEANUP_TASKS.md`: exit 0, 0 violations. `git diff --check` for those paths: exit 0. A shell-quoting parse failure in the first ad-hoc census ran no Python and made no writes; the same checks then completed from a temporary script. Final control-only lint/whitespace checks cover the updated task register, manifest and milestone log.
  - **Limits and next action:** Source-audio listening and native GitHub/browser behavior were not tested; preserved heading text and local rendered footnotes do not certify native anchors or disclosure behavior ([WCL-103](#wcl-103)). The exact S3E18 Friend-title clock discrepancy remains [WCL-050](#wcl-050); S3E019 stays nonplayed commentary. No narrative, other-character, title-register, original-ASR/audio or entity-data changes, commit/push/publication. Next selected work is the separately scoped [WCL-049](#wcl-049) Stanley biography audit under D-081.

### WCL-119

- [x] **Restructure Stanley Billings's biography as an eleven-arc reader-first character study.** Completed **2026-10-31** under standing [D-081](DECISIONS.md#standing-approval-for-world-and-narrative-changes-2026-10-31) owner approval for all `/world` and `/narrative` changes. **Parent:** [WCL-031](#wcl-031); prerequisite [WCL-049](#wcl-049). [Revised biography](../world/characters/stanley-billings.md): **82,956 bytes / 319 lines**, SHA-256 `18c2a4b37f3b87f4ca21cb3b2b6c30c5fb7fdb57ea12953c6c4f35ac64e46857`. Selected WCL-119 alone at `main` HEAD `1185b17`, preserving prior D-081/Vorel edits.

  - **Preservation and source trace:** Before editing, captured one exact then-current working-copy original at [pre-WCL119 baseline](../research/legacy/STANLEY_BILLINGS_PRE_WCL119_2026-10-31.md), **56,817 bytes / 189 lines**, SHA-256 `1aef7e33b1999a8acb42f9f6176d83772194a6ed38b509c7b60c44983dddea0c`; independently compared original/copy bytes. Reused WCL-049's complete original/source audit because the input hash was unchanged, then checked focused E000/E029/E054-E057/E059/E063/E065-E066/E069/E078/E081/E088-E089/E097/E101-E102/E110/E115/E117-E118/E124/E128 dossier passages and the D-045 crosswalk for the new boundaries. The entire original body after the H1 is retained in a collapsible historical-research appendix, **byte-identical after reversing exactly two unique heading-label changes**: old `## Introduction` becomes `## Earlier five-arc introduction`, and old `## Development by arc` becomes `## Earlier five-arc development`. Their original heading texts and source-derived fragment names now belong to the corresponding new main sections; all other original headings and every original source paragraph/footnote remain unchanged. The exact baseline preserves both original labels and original bytes independently.
  - **Reader outcome:** Introduction-time half-elf bard, eleven approved chronological character sections, friendship/consent/leadership synthesis and final in-world `Current status`. Distinguishes voluntary Soulbroker compact from coerced Diontalus joining, Stanley's agency from the archfey's killings and **Vorel's killing of Buttons**. Clarifies the **E066 promise to dying Follow**, actual Sira rescue/shared sacrifice, mirror restoration versus the old corpse, **E102 Alentris memory alteration before E110 replacement possessions**, and E117 mistrust versus later cooperation. Retains Valiir/Delit/Villa Or'Nath as canonical forms without claiming a newly learned birth name at an unverified date. Separates father's ship-mind testimony from independently witnessed family history; **S2E01 releases the last pact obligation while benefits remain**. Nash prophecy stays private and later GM interpretation stays retrospective. Finale preserves actual off-Earth Nash resurrection, Vorel's Friend award, mask transfer to Hope with prospective attunement, another ship for Stanley's departure and actual Feywild crossing as Solely Prime. Fake-death retirement, four/seven-day Wish recovery and uncertain ancient claims remain unresolved/headcanon as appropriate. Main arc prose counts **113, 158, 153, 175, 178, 176, 175, 180, 225, 252, 292**; quiet opening shorter, final multi-stage developments longer, none over twice the substantive-arc median. No episode/ASR/GM markers appear in the new main story.
  - **Validation:** Full persisted-file census/source comparison: **38/38 original heading texts represented**, **53 unique total heading texts**, all **155 original Markdown-link occurrences retained**, **89 added / 244 total** (243 local occurrences plus one unchanged external Discord link). **147 distinct local destination paths checked, 0 missing**, plus the written-name report's explicit fragment matched to its source heading; Discord was not fetched and native browser fragments remain untested. **23 definitions / 23 footnote references**, all paired, no orphans; all nine original definitions and the original Wish-recovery review marker retained. Local **micromark + GFM-footnote** render: 53 headings, a bounded research disclosure, `Current status` last in the main story, **46/46 generated footnote/backlink fragments resolving**. Final manuscript targeted Markdownlint exit 0, 0 violations; task/manifest lint and scoped Git whitespace checks recorded at closure. The identity wording received one source-boundary refinement after the first draft; final retention/link/note/render/lint checks were rerun on the resulting hash above.
  - **Limits and next action:** Audio was not listened to; existing ASR/dossier distinctions remain. Exact preservation/source-heading correspondence and local HTML checks do not certify native GitHub/browser disclosure or anchor behavior ([WCL-103](#wcl-103)). No new Soulbroker pact, absolute Diontalus erasure, fulfilled future reunion or fake-death ending asserted. No narrative, other-character, title/phrase-register, original recording/ASR, entity-data, commit/push or publication changes. Next selected task: [WCL-050](#wcl-050), the distinct Vorel S3E019 title-list and final-title source-timing reconciliation.

### WCL-120

- [x] **Create Badass T's dedicated reader profile and distinct character-index entry.** Completed **2026-10-31**, D-081 authorized, following independently completed [WCL-052](#wcl-052). **Parent:** [WCL-031](#wcl-031). Shared-source WCL-052 -> WCL-120 cohort; preserved other pending cleanup work at `main` HEAD `1185b17`. [New profile](../world/characters/badass-t.md): **8,477 bytes / 38 lines**, SHA-256 `cab8934a23acba1f56cb6b2ea29fbd621dd2a5dbd664c38cbb87fb84f88bf2be`. [Character index](../world/CHARACTERS.md): **22,442 bytes**, SHA-256 `17f3a6c82f1c2f0df9b28039b096d624700244689cc80b999bb4a51c8cb8f012`; pre-edit **21,507 bytes**, SHA-256 `b605895a2fd430dbf25cf648b84aad324845204100e046f72073e1c02e45d572`. New-page archival stage **inapplicable**, with absent path confirmed before exclusive creation; no unnecessary whole-index snapshot.

  - **Outcome and trace:** New in-world introduction as a masked guide, chronological guide/alternate-identity/companionship/prison development and final `Current status`, with eight source notes drawing on WCL-052's checked dossier windows. Direct Mangler killing remains distinct from the implied vendor killing; lip mutilation and cross-reality explanations remain attributed claims. The older alternate is not original Tedna resurrected; returned ammunition belt does not prove returned pistols. Actual shaft survival, rope rescue, bite, stabilization, fur and departure remain distinct from unperformed cure/transformation/regrowth/rescue. Last direct condition is S2E09, alive but unconscious in werefolk care; later absence/consultation mentions and creator Q&As do not advance it. No uncertain werefolk attacker-name mapping or speculative class/powers were imposed.
  - **Navigation and preservation:** Index now has a dedicated Badass T row/link and a separate P0D-counterpart row with the **E110 horizon**. Original Tedna's death/profile row stays unchanged. Original combined-row footnote ID `characters-final-alternate-p0d-tedna` and E110 destination remain, with its historical scope made explicit; one new Badass T footnote added. [Tedna's complete page](../world/characters/tedna.md) remains **byte-identical**, 8,336 bytes / SHA-256 `33b91821dfadbce459e9e75762d04d32dc0d8f834bb4d61486178459d8d7ff67`, retaining every source study and heading route. No move, redirect, source-note migration, duplicate archive or entity-pilot expansion. Active file/compatibility disposition recorded once in the manifest.
  - **Validation:** Guarded persisted readbacks, source/identity/status review, and reverse-delta comparison prove the index changed only the one split row, its existing footnote and the one new note; all unrelated index lines, heading texts, original links and original note IDs retained. **New profile: 8 definitions / 8 references, 30 local links / 26 distinct paths, 0 missing. Index: 32 definitions / 32 references, 92 local links / 83 distinct paths, 0 missing.** Local micromark/GFM-table/GFM-footnote render: profile **6 headings / 16 resolving note/backlink fragments**, final heading Current status; index **8 headings / 3 consistent tables / 64 resolving fragments**. New story prose has no episode/ASR/GM apparatus. Targeted Markdownlint for profile/index/task register: exit 0, 0 violations; scoped Git whitespace checks exit 0. Final task/manifest lint/readback closes controls. These are structural/source-scoped results, not exhaustive factual/audio acceptance or native GitHub/browser verification ([WCL-103](#wcl-103)).
  - **Next action:** [WCL-053](#wcl-053), the separate T'ietkalla historical-study audit. WCL-031 remains open: this cohort and its listed children do not establish an exhaustive per-file character audit; remaining dispositions require [WCL-063](#wcl-063) reconciliation. No recording/ASR, episode, narrative, other biography, entity-data, commit/push or publication changes.

### WCL-121

- [x] **Rewrite T'ietkalla's distinct historical study through the played S3E18 legacy.** Completed **2026-10-31** under standing [D-081](DECISIONS.md#standing-approval-for-world-and-narrative-changes-2026-10-31), following the independently completed [WCL-053](#wcl-053) audit; **parent:** [WCL-033](#wcl-033). The revised [historical study](../world/HISTORY_TIETKALLA.md) is **8,312 bytes / 57 lines**, SHA-256 `a13d9125f8d9c79fc7ec5976d2fbfda8bd55aad10701fe6f3696c592ea0e6dda`, at `main` HEAD `d13b9c5` (uncommitted). The single exact [pre-WCL121 original](../research/legacy/HISTORY_TIETKALLA_PRE_WCL121_2026-10-31.md) was copied **before editing** and original/copy both independently hash-verified at **3,305 bytes**, SHA-256 `0201712ec682befe13888df477cccc74d025aa092b1f171aa20bc3767a6be220`. No repeated per-stage archive was made.

  - **Reader outcome:** Canonical T'ietkalla title and a historical lens distinct from the [site profile](../world/places/tietkalla.md). In-world sections cover the disputed ancient Akmenos dynasty/Kefeli/Monsoon testimony, exploitation and the contested crown, Hope's partial reforms and real returned prisoners, the inhabited-station fire and demonic assault, Elhandari rescue/Carthax captivity, displaced survivors and Omnom's attributed allegations, then the **played S3E18** legacy: Earth restored but keep and ruins not rebuilt; Monsoon's actual sunlight death, Hope's surviving court, prospective welcome to refugees and mask-to-crown transfer. No fabricated census, fulfilled reconstruction, ancient genealogy, invasion motive or completed political settlement. Main prose has no displayed episode identifiers or ASR/process notes; the ending is `## Lasting legacy`, followed by source footnotes rather than a new substantive heading.

  - **Source/compatibility trace:** All **18 original Markdown-link occurrences** retained as destination occurrences, with **32 final local links**; all distinct old destinations still occur, including the world portal, place profile, episodes and ledger. Four previous H2 heading destinations are retained as inline raw-HTML aliases at the same file path (`before-the-party`, `contest-for-the-keep-e031e054`, `reforms-and-pressure-e055e059`, `arc-five-devastation-and-rescue`), but the offline preview disables raw HTML and **native browser alias behavior is unverified** [WCL-103](#wcl-103). Original historical article remains available by exact SHA-verified preservation copy; the revised prose retains its unique factual qualifications, not an unchanged word-for-word research appendix. Ten new descriptive footnote IDs are referenced once each and all ten definitions are present with no unused or undefined notes. The city article, history index and older source material were not edited; [WCL-114](#wcl-114) owns the index's separate stale display/source horizon.

  - **Validation and limits:** Persisted current-article and preserved-original reads compared all **25 original** against **57 revised** numbered lines. Targeted Markdownlint `world/HISTORY_TIETKALLA.md` exit **0, 0 violations** on the final version. Offline Markdown render checked **32/32 local link occurrences**, **0 broken, 0 beyond limit**, ten rendered footnote items and references and the five new H2 headings; all old link destinations retained by independent text comparison. Original audio was not listened to, external websites were not fetched, native GitHub/browser heading aliases and incoming external anchors were not tested. No narrative, original ASR/recordings, city profile, entity graph, commit, push or publication changes. Next selected action: [WCL-054](#wcl-054), the separate CHIDS historical-study audit.

### WCL-122

- [x] **Rewrite CHIDS and the Traversal Drive crisis as a distinct reader-first historical study.** Completed **2026-10-31** under standing [D-081](DECISIONS.md#standing-approval-for-world-and-narrative-changes-2026-10-31), after independently closed audit [WCL-054](#wcl-054). **Parent:** [WCL-033](#wcl-033). Current [CHIDS history](../world/HISTORY_CHIDS_DRIVE.md): **9,363 bytes / 49 lines**, SHA-256 `aaebb96688f7a9daf5ae07d08720fbf7165fbb68d059d040e96e282f1ddcb539`, at `main` HEAD `d13b9c5` (uncommitted). **Preserved before editing:** [exact original](../research/legacy/HISTORY_CHIDS_DRIVE_PRE_WCL122_2026-10-31.md), **2,769 bytes / 21 lines**, original/copy SHA-256 independently verified `88cc1640d342ccacec1ca4833dab334a41cfae5ec34e0f461a7bccb8e7ee36a7`. No repeated per-operation archive.

  - **Reader and source outcome:** A distinct CHIDS institutional history rather than a second technical equipment or site log. The opening and four historical H2 sections cover its real observed laboratories, control/conditioning systems, Cerinthala's betrayal, the hive's attributed old-human/anti-dragon story and contested future Wall Nash, the **portable portal device distinct from the Drive**, direct entry into the engineering chamber, Dolo Popio's manifested defeat, Quizquaz's **attributed** destructive-world proposition, the heroes' refusal and **actually performed E081 crimson-beam sacrifice**, then the **differing E082 statuses** of Vorel (conscious/live body), Nash (aware/floating heart), Hope (motionless) and Stanley (GM-described dead). The closing `## Lasting legacy` acknowledges S3E18 Earth's restoration but does **not** assert a physical CHIDS shutdown, conclusive ancient engineering theory, proven whole-species origin, completed planetary survey or permanent unreturned deaths. Chance remains unlocated at the E081/E082 cutoff; Eddie and Sira survive outside the beam at E081. Historical research/source qualifications reside in nine paired descriptive footnotes rather than the story's opening.

  - **Compatibility and checks:** Same live path, **all three original H2 heading texts/IDs unchanged** (`discovery-of-the-ancient-complex`, `entering-and-operating-the-drive`, `the-later-cutoff`); one raw-HTML old H1 alias inserted, **native GitHub/browser behavior unverified**. Compared **21/21 preserved original** with **49/49 final** numbered lines; **14/14 original Markdown-link destination occurrences retained**, **31 local links total, no removed original destinations**. Offline Markdown renderer: **31/31 links checked, 0 broken, 0 beyond cap, 0 external links**; four final H2 IDs present, nine footnote definitions and **ten rendered references** (legacy note referenced twice), no undefined/orphaned notes. Final targeted Markdownlint exit **0, 0 violations**. Neither site nor device pages, original episodes/ASR/audio, entity graph, narrative edition, historical index, review ledger or chronology were modified. No new original-audio listening, comprehensive historical validation, native browser deep-link confirmation, commit, push or publication. Next task [WCL-055](#wcl-055), assess Lactids as a people/culture subject.

### WCL-123

- [x] **Add a narrowly source-backed Harlequinari people profile and Council of Clowns cross-links.** Completed **2026-10-31** under D-081, after separate assessment [WCL-056](#wcl-056), at `main` HEAD `d13b9c5` with pending uncommitted changes preserved. **Parent:** [WCL-012](#wcl-012). Created reader-first [world/races/harlequinari.md](../world/races/harlequinari.md), **5,891 bytes**, SHA-256 `5d85a39b4bf1f4e759a9835cfd13e38e09ed9654a461365dce17e31674e7fbd1`. Four H2 sections end at `## Current status`, followed by six paired footnotes (seven references). The narrative differentiates recognized/self-named Harlequinari Blood Skunk, his attributed exile and former service, documented Council of Clowns behavior and wider society references; **does not identify every councilor as Harlequinari or extrapolate a universal appearance, culture or Critical Fortunes trait**. The potentially misleading E113 `a Harlequinari on your council` statement addresses **Hope** about Blood Skunk rather than establishing the Council's full membership.

  - **Cross-links/disposition:** Added an index row and final source-status correction in [Races](../world/RACES.md) (3,927 bytes; SHA-256 `9852fdf095dec02f8fdee1ef39a48aaa1727cea21a1b526e431ae5b7b6a87c34`), a qualified culture connection in [Factions](../world/FACTIONS_AND_POWERS.md), and reconciled the earlier ambiguous bonus wording against E113 self-identification in [Blood Skunk](../world/characters/blood-skunk-hendrickson.md). Also removed one pre-existing extra blank line in the latter to satisfy MD012. Added only a new-file disposition in [manifest](WASTES_CLEANUP_MANIFEST.md). No existing culture page was renamed or rewritten, no episode/ASR/audio altered, no legacy backup warranted for one new and bounded existing-file edits. `world/entities.json` and schema **unchanged** (original two limited race/culture records only).

  - **Validation and limits:** Targeted Markdownlint passes for new profile, Races index, Factions and Blood Skunk: all zero violations after the single blank-line fix. Offline Markdown renderer checks: new profile **15/15 links, 0 broken**; Races index **26/26 links, 0 broken**. Six footnotes, seven rendered references, all four H2 sections and one final Current status heading confirmed. Existing names and original directory routes remain. This is a source-backed **partial** culture study based on E088/E103/E113 and the earlier creator bonus; native browser and original-audio verification remain deferred, council-member species unconfirmed. No commit/push/publication. **Next:** [WCL-057](#wcl-057), assess elf people/culture evidence; parent WCL-012 remains open.

### WCL-124

- [x] **Create a bounded Elves culture article anchored in Elhandari evidence.** Completed **2026-10-31** under standing D-081, following separately completed [WCL-057](#wcl-057). **Parent:** [WCL-012](#wcl-012). Added reader-first [world/races/elves.md](../world/races/elves.md), **8,007 bytes**, SHA-256 `8b1620dab98f0142674fcc129f42646bdb6c87693d71c263bc2d8198c8b1e95b`, on uncommitted `main` HEAD `d13b9c5`. Four substantive H2 sections end in `## Current status`, followed by **nine paired footnotes with nine rendered references**. The page describes the Elhandari's observed population, biodome, leadership, therapy/refuge, the attributed spiritual/environmental history, Stanley's specific family, the station's destruction, actual Mars migration, Stanley's elected Prime office and finale passage through Feywild for some elves while others remain on Mars or Earth. Other elves (including Cerinthala and Dilenoria) are not automatically made Elhandari, nor are the High Elf's assertions or an individual's abilities presented as universal species traits.

  - **Navigation/disposition:** Added the Elves row and Elhandar community navigation in [world/RACES.md](../world/RACES.md) (4,174 bytes, SHA-256 `4c48cc2ccc136275e3cce331be82b8e820299d500b63ce00bf5ebb15e8a4fdf0`), linked the distinction between Elhandari faction and broader elven people in [Factions](../world/FACTIONS_AND_POWERS.md) (11,242 bytes, SHA-256 `8cdf2ee3feee41a4db00814eb6025c74c00d7469356b06f5f3f2bb1cfa589bb7`) and appended a single contextual culture link at the top of [Elhandar](../world/places/elhandar.md) (18,433 bytes, SHA-256 `f9058ce223a89ea55ff32d6e3c07622c009e7197a520ecc78e8ce30e42da07ab`). The old site profile's **E128 cutoff stays unchanged** pending separate inventory [WCL-063](#wcl-063), rather than silently updating its final status; source episodes, existing routes, established race articles and `entities.json` unchanged. Added one manifest file-disposition row, no repeated progress report or major-rewrite archive needed for a new profile and bounded navigational edits.

  - **Verification and limits:** Targeted Markdownlint exit 0, zero violations for new Elves, Races, Factions and Elhandar pages after adding one required final newline to the new profile; independent render of new page checked **28/28 local links**, 0 broken or beyond limit, and produced all four H2 IDs and nine footnotes/references; Races index renderer checked **28/28 local links**, 0 broken. No new source audio audition, exhaustive universal elf census, direct GitHub/browser inspection, commit, push or publication. Next [WCL-058](#wcl-058), assess dwarf cultural evidence. Parent WCL-012 remains open for other peoples.

### WCL-125

- [x] **Create a cautious Dwarves people profile from the ancient ruin, Black Mine and Blast Belly Rock evidence.** Completed **2026-10-31** under D-081 after [WCL-058](#wcl-058). **Parent:** [WCL-012](#wcl-012). Created reader-first [world/races/dwarves.md](../world/races/dwarves.md), **7,756 bytes**, SHA-256 `a4e6d47619cfe0ef9406fad7813dc74301b620891d9efd5dddc3021935574d04`, on uncommitted `main` HEAD `d13b9c5`. The profile separates the E003–E005 ruined dwarven settlement, Oilbeard-run E018–E026 Black Mine and S2E05–S2E06 Burp mining town, with limited E098 weaponsmith and E116 frigate context; it closes with the S3E02 dwarf departure from Burp. **No claim** that the mapped Moag Ferhain is proved identical to the ancient ruins, that Oilbeard coercion reflects all dwarves, that Tungsten's bank contract proves present employment, or that all dwarves belong to one state/culture. Four main H2 headings with `## Current status` last, and **nine paired descriptive footnotes/nine rendered references**. No original-audio or native-browser verification.

  - **Navigation and verification:** Added one race row in [world/RACES.md](../world/RACES.md), a contextual Oilbeard/dwarf distinction in [world/places/black-mine.md](../world/places/black-mine.md), and a Burp cross-link in [world/PLACES.md](../world/PLACES.md), with one file-disposition row in [manifest](WASTES_CLEANUP_MANIFEST.md). Verified revised files: Dwarves **7,756 bytes** SHA above; Races **4,410 bytes** SHA-256 `02416f3882629720fc0e9fb863e1b948bc8746edfce8eaeca2c7ab3350569673`; Places **21,195 bytes** SHA-256 `26b6f52576fa84c3d38a2bdc0a451b1c6b089d3ead67c50e359b85d7c43d6dca`; Black Mine **3,188 bytes** SHA-256 `c8e879d52885e1c687328767298e57d6adaf442302d922dcab684915b15ce9d4`. Targeted Markdownlint returned **zero violations** for each; independent offline rendering checked new Dwarves page **29/29** local links and Races index **30/30**, 0 broken. No source, `entities.json`, existing major narrative, new research backup or unrelated working-tree item was altered. Parent [WCL-012](#wcl-012) remains open; **next [WCL-059](#wcl-059)**, distinguish orcs and Kuromokishi.

### WCL-126

- [x] **Write and cross-link a source-limited Orcs people reference distinct from the Koromukishi martial order.** Completed **2026-10-31** under D-081 after [WCL-059](#wcl-059). **Parent:** [WCL-012](#wcl-012). Created [world/races/orcs.md](../world/races/orcs.md), **8,381 bytes**, SHA-256 `4a3792575a0f3767534659998cd4a85725760cd4324e38bb716935d22aaa738d`, on uncommitted `main` HEAD `d13b9c5`. Five H2 narrative sections end at `## Current status`, followed by **ten paired source footnotes and ten rendered references**. The page distinguishes Principal-aligned Koromukishi order membership from orc ancestry; E026/E027's nameless ex-member's account from group consensus; Tobacho-associated escorts from mixed ship operators; the **three S2E06 raider surrenders and all three S2E07 voyage deaths**; E113 Headsy's exceptional state from universal physiology; and S3E18 Kuromokishi resettlement with Vorel as a begun journey, not completed social rehabilitation. Elite chrome-associated equipment and inconsistent ASR spellings are qualified; no standard ancestry abilities or generic orc civic code invented.

  - **File disposition and verification:** Added Orcs row in [world/RACES.md](../world/RACES.md) (**4,599 bytes**, SHA-256 `48468af166f9b2dfeb4e64d2ccab44b37bdb8629a2ea0a0fb964209c3b451acd`); refined the existing grouped Koromukishi/factions and later S3E06 military rows in [Factions](../world/FACTIONS_AND_POWERS.md) (**11,562 bytes**, SHA-256 `a85fee953eff6b62624285fb184bacd1c8addcbfcf823fa9adb1e331168851cf`); added an institution-versus-people contextual link in [Slavetown](../world/places/slavetown.md) (**4,363 bytes**, SHA-256 `aa42b58c88471c3c8be0744492d721a76c27d2b4a7ef638cef89cfe68bcf2432`). One [manifest](WASTES_CLEANUP_MANIFEST.md) disposition row, no duplicated progress/changelog. Targeted Markdownlint on all four relevant world Markdown files: **zero violations**; offline renderer: Orcs profile **29/29 local links, 0 broken**; Races **31/31, 0 broken**, all five heading IDs and ten footnotes/references render. Original transcripts/audio, entity index, major narrative files and unrelated pending changes untouched. Native browser, complete corpus and independent original-audio verification remain deferred. **Next [WCL-060](#wcl-060)**, illithids; parent WCL-012 remains open.

---

**Record-ownership rule:** This file is the only checklist and next-action pointer. [Manifest](WASTES_CLEANUP_MANIFEST.md) records *file dispositions and migrations*, not task statuses. [Changelog](WASTES_CLEANUP_CHANGELOG.md) records only meaningful dated decisions and milestones, with references to IDs here, not duplicate task detail. [Progress](WASTES_CLEANUP_PROGRESS.md) is a compatibility pointer, not a journal. [Decisions](DECISIONS.md) governs approvals; [review queue](REVIEW_QUEUE.md) and [consistency ledger](../world/CONSISTENCY_LEDGER.md) govern evidence issues. Historical B1–B289 execution detail remains in the three preserved pre-migration records.
