# The Wastes — N1-P3-D creature and technology canonical spelling cleanup

**Date:** 2026-10-28 (Europe/Stockholm). **Authority:** standing owner decision **D-047** authorizes bounded, unambiguous minor spelling and reader-facing canonical-name corrections without repeat approvals; **D-044** confirms **T'ietkalla** and **The Principal**. This batch does not license a new story claim, identity adjudication, arc rewrite, file rename or source-text alteration.

**Initial Git checkpoint:** repository `There Will Be Dungeons Transcripts`, branch `main`, HEAD `7f331552a7c87172a18a9b165f258f4b1c036f38`; **139 visible changes and 59 restricted omitted** at start. All concurrent Delvers changes and previous Wastes cleanup batches protected. No commit/push.

## Ordered four-file worklist, fully read before mutation

All **92/92 numbered lines** across the following four subject articles were read and the original byte SHA-256 preflighted. Exactly **nine old-name appearances across eight source lines** are active editorial wording or link labels, not source quotes or historical aliases.

| ID | Source | Lines | Original SHA-256 | Proposed changed lines and occurrences | Links | Footnote uses / definitions | Status |
| --- | --- | ---: | --- | --- | ---: | --- | --- |
| D01 | `world/creatures/pixie-hulks.md` | 24 | `4fbe023d87150a427183b4267fbc320cd05acfc146344648be170366245cad33` | 7, 11, 19: three `Tietkalla` → `T'ietkalla` | 10 | **5 uses / 4 definitions, original pre-existing counts** | queued |
| D02 | `world/creatures/sand-squid.md` | 28 | `0582b577b020a681d8111cfbcd576ca52c594c722e11b48ca270c02a864fe98f` | 17: one `Tietkalla` → `T'ietkalla` | 15 | 6 / 6 | queued |
| D03 | `world/technology/eye-of-groxl.md` | 31 | `ea1a9399b236447f40c63409c3873579070c3ebfc41a5a21118c1dbb1c6fe326` | 17: one referent-confirmed `the Principle` → `the Principal`; 25: `Tietkalla/froghemoth` → `T'ietkalla/froghemoth` | 22 | 0 / 0 | queued |
| D04 | `world/technology/gem-of-tides.md` | 9 | `d0ee3c36873b1ad134e5b1e714714f3c1cc5a1b8fbe21c78a4aa04251565f19a` | 5: one possessive `Tietkalla` → `T'ietkalla`; 7: two usages including displayed `[Tietkalla]` → `[T'ietkalla]` | 6 | 0 / 0 | queued |
| **TOTAL** | **Four existing source files** | **92** | Original hashes above | **8 source lines; 9 spelling corrections** | **53** | **11 uses / 10 definitions, original asymmetry** | **queued** |

**Preservation:** Create and verify SHA-256/byte-identical backups of the **actual working-copy originals** in `research/legacy/` before editing. Do not change links to the historical `places/tietkalla.md` slug, footnote IDs, heading order, story claims, cutoff/custody statements, Groxl ASR aliases, direct quotations or uncertainties. The pre-existing pixie-hulks 5-use/4-definition count is **not** a new defect caused by this operation; treat all original footnote tokens as immutable.

**Protocol:** 0. Save this approved-intent / D-047 applicability journal. 1. Preserve all four byte-exact originals and verify hashes. 2. Recheck hashes, perform exact guarded replacements on the eight listed lines. 3. Compare complete original vs edited bytes, exact changed line numbers and substitutions, **92/92 source lines**, **53/53 ordered Markdown URL destinations**, exact footnote token arrays/definitions and file-specific LF/CRLF. 4. Record post-edit SHA-256 and completion in journal, then one manifest and one progress checkpoint and final Git status.

**Unrun limitations:** Workspace MCP does not provide primary audio listening, Markdownlint, `git diff --check` or full link-target/fragment/backlink checking. Do not claim these passed. **No additional source file or substantive edit allowed by this batch.**

**Checkpoint 0 — PASSED:** Intent persisted before editing; all four live sources SHA-256 matched the table above. Byte-identical working originals archived and independently reread with matching size and SHA at `research/legacy/{PIXIE_HULKS,SAND_SQUID,EYE_OF_GROXL,GEM_OF_TIDES}_PRE_N1_P3_D_2026-10-28.md`. Original files had not been edited before archive verification.

## Exact executed delta and verification

| ID | Changed original numbered lines | Canonical replacements | Final source SHA-256 | Result |
| --- | --- | ---: | --- | --- |
| D01 | 7, 11, 19 | 3 | `f13425c397436367b3dd9b36fb6eaeb3297739a29fbdfc732ccbc7f31941b028` | PASS |
| D02 | 17 | 1 | `8d79bf6199ec6160ade455bed45f0e8c5647422d9c3be51ff9540dc53eff56b4` | PASS |
| D03 | 17, 25 | 2 | `9a69b05b0a835a8e044fe561cd1891cfd5fa6503d885e34a664dc9464fc376de` | PASS |
| D04 | 5, 7 | 3 | `ecd49521bc1b161cbcea4d474a596fc3383227715ba065e2a5263861ed257f87` | PASS |

**Checkpoint 1 — PASSED:** Nine individually guarded text replacements succeeded. Changed only `Tietkalla` → `T'ietkalla` and one unambiguous `the Principle` → `the Principal`. The `Eye of Groxl` retained its original ASR aliases and uncertainty wording, quoted phrases and entity distinctions.

**Checkpoint 2 — PASSED:** Binary source-vs-archived-original reread for four files: **92/92 original numbered source lines**, **8/8 specified changed lines**, **9/9 name substitutions** and no other source-line differences, **53/53 ordered Markdown URL destinations unchanged**, all original footnote tokens and their definitions unchanged, LF style in three files and CRLF in `eye-of-groxl.md` preserved. Footnote baseline is **11 references / 10 definitions** because `pixie-hulks.md` reuses a footnote; not a change introduced here. No audiovisual/source-fact validation done.

**Checkpoint 3 — CLOSED (2026-10-28):** One guarded completion entry added to `project/WASTES_CLEANUP_MANIFEST.md` (line 197) and one to `project/WASTES_CLEANUP_PROGRESS.md` (line 123); both independently read back. Final Git status: `main`, HEAD unchanged at `7f331552a7c87172a18a9b165f258f4b1c036f38`, **148 visible changes with 59 restricted entries omitted**, including separate concurrent Delvers work. This batch modified only the four named original articles, their four exact-original archives, this execution journal and the two Wastes checkpoint documents. No commit/push. **Next:** N1-P3-E minor editorial audit beginning with `world/technology/fate-six.md` and a small set of related world articles. C1, D-045 A1 and D-046 R1 substantive decisions remain gated. `git diff --check`, Markdownlint, real Markdown target/anchor/backlink checks and source audio remain unrun.
