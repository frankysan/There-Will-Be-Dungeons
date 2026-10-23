# World reference reorganization — 2026-10-23

**Project:** *There Will Be Dungeons Transcripts*, The Wastes only. **Research horizon:** E118 (E107–E109 is a historical prequel long before E001); bonus episodes remain cast/GM commentary. **Editorial operation:** No source SRT or episode dossier edits and no independent listening. This report documents the follow-up consolidation of `world/` after the first set of subject-category indexes and profiles was introduced.

## Results

- `world/README.md` is the compact encyclopedia portal, with seven subject categories.
- `world/CHARACTERS.md` is a character directory rather than an E054 table followed by E### appendices. Major missing supporting/ambiguous persons gained pages: **Nobieri, Tobacho Fleur, the hooded Voice, Steerious Business, Blood Skunk Hendrickson and Dr. Spider**.
- `world/PLACES.md` is a location directory and arc-by-arc route synopsis. Four missing significant destinations gained primary pages: **White Tower, Solar Mines/Blood Canyons, Kaiser Casino and Leopold experimental facility**.
- `world/WORLD.md` now presents stable setting systems—Earth/Scorching, politics, technology, planar theology and epistemic limits—rather than repeating all arc events.
- `world/CHRONOLOGY.md` remains the **one intentionally detailed episode-ordered timeline**; a navigational note clarifies that it tracks time-of-knowledge rather than serving as another thematic profile.
- Category indexes `ANTAGONISTS.md`, `FACTIONS_AND_POWERS.md`, `HISTORICAL_EVENTS.md` and the root project/world entry points now link to major new subjects.
- `project/WORLD_REFERENCE_PAGE_TEMPLATE.md` codifies source tier, spoiler cutoff, profile headings, archival procedure and directory/category ownership. Back-navigation was added to the 10 new person/place and six existing artifact profiles, plus three historical studies.

## Before/after size of three active indexes

| Index | Old reference text | New subject-centered text | Approximate reduction |
| --- | ---: | ---: | ---: |
| `world/CHARACTERS.md` | 30,232 characters | 7,517 | 75% |
| `world/PLACES.md` | 30,856 characters | 6,878 | 78% |
| `world/WORLD.md` | 35,749 characters | 9,527 | 73% |

The reductions **do not delete historical research**. The three original E118-era working versions were copied before rewriting to [the 2026-10-22 archive](../research/legacy/2026-10-22/README.md) with all relative Markdown links rebased. Earlier full append-only archives and Git history are also retained. These are **frozen sources**, not alternate current-world indexes.

## Evidence and chronology constraints retained

- The reported E048 death of Angelashi and direct E054 rescue are different evidence cutoffs.
- E081's on-screen sacrifice/death declaration and E082's return are both documented.
- Hope's E101 departure divides Arc Four and Arc Five **within one episode**.
- The Eye of Groxl remains one owner-confirmed item despite ASR variants; the Eye of the Voice, living Hand, detached Fist gauntlet, CHIDS portable portal and Traversal Drive remain distinct.
- A speaker's alleged historical explanation, uncertain private letter, retrospective bonus remark or proposed future course must not become a witnessed event.
- `Inverse`, E043 and the pre-Dusthill Dunebreaker story must not be silently interleaved with the main Wastes chronology.

## Validation performed and limits

A bounded workspace-based link audit examined **35** newly added, changed and archived documents over five batches, totaling **1,246 checked local link references**. References were compared to fresh repository directory inventories. This found one pre-existing outdated archived link to `narrative/YEAR_TWO.md`, now corrected to `narrative/ARC_THREE.md`. Six `transcripts/` references and the episode-analysis skill link initially fell outside the inventory scope; their directories were separately inspected and files confirmed present. The three freshly rebased long snapshots each passed their 398 combined local-link checks.

A separate bounded **Markdown structure preflight on 32 changed, maintained Markdown files** found no heading-level, heading-spacing, multiple-blank-line, tab/trailing-space or table-spacing problems. These are **structural checks, not full markdownlint, tests, audio verification or CI**. The connected workspace exposes read/replace/create/git-status tools but no canonical shell/check runner for this repository; **no full documentation test suite was run and no commit was requested**. This audit does not certify external links, Markdown fragment anchors, facts inferred from ASR or every pre-existing legacy file.

## Next maintenance

1. Future episode analyses should update the appropriate **subject page and dossier**, not append a full episode synopsis to every top-level index.
2. **Follow-up completed, 2026-10-23:** The four long protagonist profiles were frozen and rewritten as subject-focused biographies, Diontalus received a separate page, and Vorel's titles moved to a source-indexed register. See [profile consolidation report](PROTAGONIST_PROFILE_CONSOLIDATION_2026-10-23.md). Future maintenance should prevent renewed episode-by-episode accretion.
3. When check execution is available, run repository Markdown lint and any documentation tests; fix issues before treating this as fully validated.
4. Keep `world/entities.json` explicitly a **seed**, not an automatically authoritative catalog synchronized with all E118 lore.

[World portal](../world/README.md) · [Template](../project/WORLD_REFERENCE_PAGE_TEMPLATE.md) · [Architecture](../project/DOCUMENTATION_ARCHITECTURE.md) · [Review queue](../project/REVIEW_QUEUE.md).
