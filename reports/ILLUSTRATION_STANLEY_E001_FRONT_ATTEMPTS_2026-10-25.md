# Stanley Billings — E001 front-view attempts (2026-10-25)

**Subject:** `WASTES-STANLEY-BILLINGS`. **Appearance:** `WASTES-STANLEY-BILLINGS-A01` (E001). **Sheet:** `WASTES-STANLEY-BILLINGS-DS-001`. **Current phase:** `FRONT_DRAFTING`; **no accepted front anchor**.

## Preflight and approved dependency

- The owner's exact normalized face reference was placed at `illustrations/references/Stanley_Billings_E001_Face_v1_1024_sRGB.png` and read through the workspace binary tool: **1,305,953 bytes**, SHA-256 `3c315ea76096eb4253ba8504a0209e48fe00fc3dfab3d691d8d22e97630d1e4d`; **1024 × 1024 RGB PNG** with embedded ICC chunk. Independently matched session copy has a **588-byte “sRGB built-in”** ICC profile and visibly preserves the owner's accepted early Stanley bust. Owner instructed “Proceed” after normalized export; record `FACE_APPROVED` in the distinct [face acceptance report](ILLUSTRATION_STANLEY_E001_FACE_ANCHOR_2026-10-25.md).
- Intended next **single-stage** image: **one** head-to-boots, strictly front-facing, neutral full-body standing figure of the *same* brown-haired, tan-skinned, brown-eyed, moustached/goateed adult half-elf. Continue the **brown high-collared coat**, muted dark vest, open off-white shirt, visibly functional coat pockets, practical dark trousers and boots; optional **one sheathed rapier** at a consistent chosen hip. Clothing construction, hip-side placement and other full-body design specifics remain owner-reviewable choices.
- This is an E001 **design-sheet front anchor**, not an instruction to produce a text-labeled multi-view sheet. Keep all source citations and notes outside the pixels; no side/back figures, portrait inset, equipment panels, color charts, typography, future artifacts, flamboyant scarves or unsupported loadout.
- The current renderer interface inferred a design-sheet composite despite instructions in the active stage and commentary. It did **not** offer a verified mechanism to inject the accepted normalized face file as an explicit per-call reference. The accepted face was inspected by the assistant, but **pixels passed to renderer = not verified**. Thus these attempts cannot establish identity continuity.

## Rejected generation attempts

| Attempt | Image generation ID | Session output (not a repo asset) | Measured technical attributes | Specific rejection |
| --- | --- | --- | --- | --- |
| F01 | `1fb9d8c7-a1d9-4031-bc62-69147091922e` | `/mnt/data/wide_character_design_sheet_illustration_on_a_parc.png` | **1536 × 1024** RGB PNG, **2,858,244 bytes**, SHA-256 `3c77554acef86b2a8639ed9fa5f70ec5d6f5c43f5c7818d348b3f0ff6c71154a`; **no ICC** | Full **front/side/back plus portrait/expression/equipment montage**, embedded text/labels, multiple accessory details and decorative sheet layout. Violates one-front-view gate, square size, profile requirements and one-stage generation. Not accepted. |
| F02 | `c5d5f29c-74dc-4ad9-9933-8de2ad42d893` | `/mnt/data/overall_a_clean_character_design_sheet_illustrati.png` | **1024 × 1536** RGB PNG, **2,841,057 bytes**, SHA-256 `f50f578dcf47f6ef19e3e8039b9a1d2095aac0ae6d759c3c1045a0b5b8a73c56`; **no ICC** | Again a **labeled entire character turnaround sheet** with face/profile/back, expression and equipment panels. Invented extra pendant/book/pouches/scarf. Violates phase scope, provenance and square/sRGB technical contract. Not accepted. |

Both are **rejected/noncompliant experiments**, not approval candidates. They must **not** replace the owner-approved face or become front/side/back anchors by cropping/reformatting: the small montage figures and facial variants are not demonstrated faithful to the original approved face, and a crop would not repair unsupported additions. No images were uploaded to the project repository during this phase; do not add `IRV` flags for unselected drafts.

**Renderer's actual prompt:** unavailable to inspect with certainty; reported generation `prompt` metadata is empty, so do not pretend the project style block was actually transmitted verbatim. Requested square-size parameter was not honored. Future tool use must support the explicit *single front* stage and preferably accept the verified approved face PNG itself as visual conditioning. Then verify the resulting **1024 × 1024, sRGB PNG** and visual continuity, obtain owner acceptance, store in `illustrations/references/`, and compare repo readback checksum before `FRONT_APPROVED`.

## Checkpoint

**`FACE_APPROVED` remains valid and unchanged.** `FRONT_DRAFTING` is the only active stage; `FRONT_APPROVED`, `SIDE_APPROVED`, `BACK_APPROVED` and final `OWNER_APPROVED` are **false/not reached**. Do not automatically advance to profile or assembly. Next executable request should be a strict `$twbd-illustration-generate Wastes "Stanley Billings" E001 design-sheet front` **with an image-generation interface that respects one-view constraints**. Preserve the two historical rendered failures solely for traceability; no source or art approval has been changed by their incidental features.

**Checks:** image dimensions, PNG format, file size, SHA and absent ICC inspected locally for both session files. Project text report written and read back via workspace tools. TWBD lint/tests not available through the current remote workspace interface; **not run**.
