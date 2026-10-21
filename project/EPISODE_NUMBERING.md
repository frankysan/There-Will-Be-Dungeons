# Episode numbering and archive-filename crosswalk

**Status:** Owner-provided numbering/reference convention, reviewed **2026-10-21**. **Source:** the archive owner's exported spreadsheet **`There Will Be Dungeons episodes.xlsx`** (`Sheet2`, **240 data entries**, columns **A–I**). The **original Google Drive file** remains the owner's source of truth; the exported snapshot was supplied for this review. The source document itself is **not copied to this repository**.

## Rule: corrected IDs are canonical *within this archive*

- **Column A, `Name`**, records a publisher/original listing label, often a podcast number. This is useful for finding a historical title and reconciling RSS archives, but must **not** determine repository paths when it differs from the owner's corrected numbering.
- **Column I, `Column 1`**, provides the owner's **normalized archive basename** with campaign, season, corrected episode number and title. **Use this value** to reconcile archived `sources/` SRT filenames, episode dossiers and future `transcripts/` filenames. Prefixing/extension as appropriate does not change the corrected ID.
- **Column H, `Episode`**, contains some spreadsheet calculations that render as **`#NAME?`** when this particular exported XLSX is imported for analysis. It is **not a dependable primary episode-ID source in this review**. Do not replace explicit Column I values with those computed errors.
- Columns **B/E** supply date-like strings/serials, **C/D** optional title/description text, **F/G** campaign/season categorization. These are *spreadsheet metadata*, not independently verified publication/recording dates or audio quotations; some other formula-driven columns also render as `#NAME?`.
- Episodes in other campaigns and bonus shows are **not** Wastes Season 1 episodes. Preserve their original names and corrected category separately rather than allocating them ordinary `E###` identifiers.
- **Supplemental `S1E013.5`** is an intentional intermediate identifier, *not* evidence of an original podcast episode formally numbered 13.5. Its in-world scene chronology is a separate editorial dimension, documented in [E013.5](../episodes/E013.5.md).

## Representative crosswalk: Wastes S1 before the first offset

These correspond **one-to-one through original 54** (and, for E000, the original `There Will Be Dungeons: 00` listing):

| Original/source label | Corrected repository ID | Archive basename / note |
|---|---|---|
| `There Will Be Dungeons: 00` | **E000** | `The Wastes S1E000. Introductions` |
| `TWBD 01: The Campaign Begins!` | **E001** | `The Wastes S1E001. The Campaign Begins!` |
| `TWBD 02: Spiders` | **E002** | `The Wastes S1E002. Spiders` |
| `TWBD 03: Soft Head Returns` | **E003** | `The Wastes S1E003. Soft Head Returns` |
| `TWBD 04: The Oil Demon` | **E004** | `The Wastes S1E004. The Oil Demon` |
| `TWBD 05: Goblincide` | **E005** | `The Wastes S1E005. Goblincide` |
| `TWBD 06: Start your engines!` | **E006** | `The Wastes S1E006. Start your engines!` |
| `TWBD 07: Bok Bok Keeping It Fresh` | **E007** | `The Wastes S1E007. Bok Bok Keeping It Fresh` |
| `TWBD 08: Stupid Gnomes!` | **E008** | `The Wastes S1E008. Stupid Gnomes!` |
| `TWBD 09: Surfacing` | **E009** | `The Wastes S1E009. Surfacing` |
| `TWBD 10: Shackles` | **E010** | `The Wastes S1E010. Shackles` |
| `TWBD 11: Kick me as hard as you can` | **E011** | `The Wastes S1E011. Kick me as hard as you can` |
| `TWBD 12: Work Hours` | **E012** | `The Wastes S1E012. Work Hours` |
| `TWBD 13: Old One Eye` | **E013** | `The Wastes S1E013. Old One Eye` |
| `TWBD: Supplemental` | **E013.5** | `The Wastes S1E013.5 Supplemental` (unnumbered originally) |
| `TWBD 14: That's Magic` | **E014** | `The Wastes S1E014. That's Magic` |
| `TWBD 15: The Darkness` | **E015** | `The Wastes S1E015. The Darkness` |
| `TWBD 16: Dragon Mother` | **E016** | `The Wastes S1E016. Dragon Mother` |
| `TWBD 17: Fire in the hole!` | **E017** | `The Wastes S1E017. Fire in the hole!` (future dossier) |
| `TWBD 18: Into the storm` | **E018** | `The Wastes S1E018. Into the storm` (future dossier) |

**Scope:** The table is a reference for current and immediately forthcoming work, not a substitute for **all 240 original spreadsheet rows**. Consult **the source spreadsheet's Column I** for the exact label of any other episode, including subtitles, bonuses, and season transitions.

## Important numbering shifts later in Wastes Season 1

| Publisher/original listing | Spreadsheet's corrected classification | Consequence |
|---|---|---|
| **TWBD 55: The Year One Q&A!** | **`Bonus for March 2019 The Year One Q&A!`** | Original episode 55 is a **bonus**, not `The Wastes S1E055`. It must not consume a main-story number |
| **TWBD 56: My Standards Are Very Lizard** | **`The Wastes S1E055. My Standards Are Very Lizard`** | Original regular 56 becomes corrected **E055** |
| **TWBD 57: Welcome back, George** | **`The Wastes S1E056. Welcome back, George`** | Continues the one-step correction |
| **There Will Be Dungeons 58: The Royal Truckery** | **`The Wastes S1E057. The Royal Truckery`** | Still corrected original minus one |
| **There Will Be Dungeons 77: Inverse Part 3** and **TWBD 77: Inverse Part 4** | **`Inverse S1E3. Inverse Part 3`** and **`Inverse S1E4. Inverse Part 4`** | These are **Inverse** episodes, not ordinary Wastes S1 installments. The spreadsheet assigns both an original-listing **77**, requiring a multi-field source key (name + title + campaign), not bare original number |
| **TWBD 78: Potable Portable Portal** | **`The Wastes S1E076. Potable Portable Portal`** | Original 78 becomes corrected **E076**, **two fewer**, following the excluded Q&A and Inverse numbers |
| **TWBD 79: The Wall Nash** | **`The Wastes S1E077. The Wall Nash`** | The two-step offset continues |
| **TWBD 130: Burrow** | **`The Wastes S1E128. Burrow`** | Late Wastes S1 retains the **two-step** corrected offset |

**Other separated series:** The source contains four **Inverse** parts, **Delvers** seasons 1–3, Wastes seasons 2–3, a **Star Trek one-off**, numerous monthly **Bonus** entries, and a **Wastes campaign roundup**. The source's normalized names for these entries—not the Wastes S1 shift arithmetic—determine their archive identifiers.

## Exceptions not to silently “fix”

- The original `TWBD The Wastes S3E78: Electric Lizard` maps to corrected **`The Wastes S3E08. Electric Lizard`**. This looks like a typo in original listing but is preserved verbatim as an *original label*; the spreadsheet's corrected name is the archive identifier.
- Some original bonus titles mention one month while Column I labels another (e.g. an original **May 2019** bonus normalized as **June 2019**). Retain both source strings and their dates; **do not reverse the user's existing normalization** without discussion.
- Original listing number **77** is reused for two distinct `Inverse` rows. An original number alone is **not a unique database key**.
- Corrected episode identifiers may differ between main campaigns. Never join `E015` without **campaign + season** context.

## Future import / testing contract

If adding code to ingest these sources later: **preserve the full original listing, corrected basename, campaign, season, supplemental/bonus class, source row and (where present) date as separate fields**. Do not compute corrected numbers with a blanket subtraction, infer them from `#NAME?` cells, or silently update machine transcripts. Test explicitly around **E013.5, bonus-original 55, original/Inverse 77, original 78 → corrected E076, original 130 → corrected E128, and Wastes S3E78 → S3E08**.

Related: [archive owner's event/spelling notes](OWNER_EPISODE_NOTES.md) (personal, noncanonical), [source hierarchy](EXTERNAL_REFERENCES.md), and [editorial policy](EDITORIAL_GUIDE.md).
