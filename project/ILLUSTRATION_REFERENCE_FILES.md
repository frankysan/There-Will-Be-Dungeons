# Illustration reference files

## Naming and manifest ownership

Every PNG in `illustrations/references/` uses this exact pattern:

```text
<campaign>_<entity>_<episode>_<role>_v<NN>.png
wastes_nash-maggard_e001_side-left_v01.png
```

Use lowercase ASCII letters and digits, with hyphens between words inside a
field. Underscores separate the five fields. Campaign and entity identify the
tracked subject across all views and sheet pages. Episode is `e001`, `e002`,
etc., or season-qualified `s1e01` for a campaign that uses seasons. Versions
are two digits, starting at `v01`; retain existing revision numbers when
renaming. Production dates, approval status, image dimensions and color
profile belong in the manifest.

Current roles are `face`, `front`, `back`, `side-left`, `side-right`,
`side-paired`, `sheet-four-view`, and numbered sheet pages such as
`sheet-01-turnaround`, `sheet-01-front-back`, `sheet-02-sides`,
`sheet-02-face` and `sheet-03-face`. A left/right role always names the
character's **anatomical side**, independently of panel position or facing
direction. The cleanup preserves existing side identifications; it does not
perform a new visual laterality audit.

Maintain **one manifest per campaign + entity + episode**, using:

```text
<campaign>_<entity>_<episode>_manifest.json
wastes_nash-maggard_e001_manifest.json
```

Update that manifest for every view, page, revision, normalization operation
and approval decision at the same episode. Add revisions to its `assets`
array; do not create manifests per image, view, export operation or version.
Campaign, entity and episode fields must match the filename. Per the owner's
2026-10-26 instruction, **normalize E000 reference registrations to E001**;
retain original E000 labels in provenance. This is a reference registration
convention; historical episode citations and research reports retain their
source chronology.

## Current manifests

| Campaign / entity / episode | Manifest | PNGs |
| --- | --- | --- |
| Wastes / Hope Akmenos / E001 | [Manifest](../illustrations/references/wastes_hope-akmenos_e001_manifest.json) | 7 |
| Wastes / Nash Maggard / E001 | [Manifest](../illustrations/references/wastes_nash-maggard_e001_manifest.json) | 7 |
| Wastes / Stanley Billings / E001 | [Manifest](../illustrations/references/wastes_stanley-billings_e001_manifest.json) | 7 |
| Wastes / Vorel / E001 | [Manifest](../illustrations/references/wastes_vorel_e001_manifest.json) | 5 |

## Manifest data and provenance

`schema_version: 1` describes the consolidated inventory. Each manifest has
campaign, entity, stable entity/state/sheet IDs, episode, episode aliases,
`assets`, `provenance`, normalization details and notes.

- **`assets` is the current file inventory.** Each entry records filename,
  role, version, SHA-256, byte count, dimensions, bit depth, color mode,
  embedded ICC profile metadata (or `null`), and original filename aliases.
  All listed files must exist and every reference PNG must be listed once.
- **`provenance` preserves the complete prior manifest record data.** Each
  record retains its original manifest filename and SHA-256. Original upload
  filenames, source hashes, transformations, laterality corrections and
  approval decisions remain verbatim inside `record`. These historical
  records can mention absent files, session-only exports, old E000 labels,
  or registration steps that have since occurred; they are not a second
  inventory of current repository files.
- **Registration and owner approval remain separate.** The naming migration
  verifies existing bytes and metadata. It does not grant or revoke approval,
  reconcile every historical status paragraph, or restore missing artwork.
  New decisions must identify the exact filename/hash and their scope in
  this same entity/episode manifest and the design-sheet ledger.

The 2026-10-26 migration renamed **26 PNGs without changing any bytes** and
consolidated **seven manifests into four**. Nash's earlier E000 record now
lives in the same E001 manifest as his side, back and final sheet records.
The old normalized Nash face reference is an alias for the registered
`sheet-02-face` page: their SHA-256 is identical. Other absent source files
are retained as historical references rather than redirected to different
artwork. Repository paths to renamed files were updated in maintained
documents and reports; original upload/session filenames remain historical.

**Existing metadata gap:** Vorel's face v02 PNG has no embedded ICC profile,
despite its original filename containing `sRGB`. Its manifest records
`icc_profile: null`. This cleanup preserves the PNG unchanged and does not
certify its color profile or technical approval.

## Validation

Run from the repository root:

```powershell
python tools/validate_illustration_references.py
```

Or run `npm run check:illustrations`. Validation checks strict filenames,
matching campaign/entity/episode fields, one manifest per pair of entity
and episode within each campaign, complete and unique PNG registration,
file existence, SHA-256, byte counts, PNG chunk CRCs, dimensions, bit depth,
color mode and actual embedded ICC bytes. Historical provenance is not
interpreted as active file registration. This inventory check does not
grant visual approval or replace the illustration production gates.
