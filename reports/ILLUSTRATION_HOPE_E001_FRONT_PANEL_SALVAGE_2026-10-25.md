# Hope Akmenos — E001 front panel-removal salvage (2026-10-25)

**User direction:** “I think we can keep the first result, but crop out the unwanted detail panels.”  
**Scope:** `WASTES-HOPE-AKMENOS-A01`, E001 Dusthill, `WASTES-HOPE-AKMENOS-DS-001`.  
**Outcome:** `FRONT_CANDIDATE_AWAITING_OWNER_REVIEW`. A new, **non-generative source-preserving** panel-free composite was prepared and validated locally; **not yet owner-approved, not repository-registered**. Historical `FRONT_METHOD_BLOCKED` still applies to uncontrolled repetitive generative attempts, not to this deliberate compositing solution. **Approved face anchor remains unchanged.**

## Selection and rejected alternative results

The selected exact source is **the first FRONT attempt F01**, generation ID `cd5dd474-2a91-44cf-abba-d0b912e25dd4`, actual image `/mnt/data/a_clean_character_concept_turnaround_style_illustr.png`, **1254 × 1254** RGB PNG, **2,649,270 bytes**, SHA-256 `0bfbecb5a0ea8f4bd8224820c519604d2b9ed9195703a524073e471a5228bb60`. It contains a center figure surrounded by intrusive side detail panels; no source ICC tag. The owner specifically preferred retaining this first figure, not using F02 or starting a different costume.

Before controlled compositing, the image-edit renderer returned two **standalone redesigned outputs** that superficially resemble F01 but do not preserve the original figure's precise pixels:
- `3207633b-e89f-44ce-8d0a-2cfb7020a260`, `/mnt/data/a_clean_centered_character_concept_illustration_o.png`, 1254-square RGB PNG, 2,357,117 bytes, SHA-256 `09daa25860dfa18a157d9206c698d954bf9008844f6812af9dc271b9d23c9c87`; untagged.
- `256e9aa0-6c14-4683-91b8-e409ee506a83`, `/mnt/data/a_clean_character_illustration_on_a_plain_parchme.png`, 1254-square RGB PNG, 2,502,924 bytes, SHA-256 `9372179b107876249a410fa7a97d02f5a1f80c3e5b395835034992f7bc0261db`; untagged.

**Neither regenerated candidate is promoted or registered:** the user's requested salvage favors *unchanged central-figure pixels*. The actual renderer prompt/reference lineage was not verified.

## Deterministic panel removal

- Source image: **F01 only**; input full-square RGB pixels retained for central character. The surrounding left and right panel areas were replaced by a neutral synthetic paper-like background, sampled/statistically matched to original blank-background colors. The source figure is isolated with a hand-tuned, soft-edged, **row-dependent extraction region** to protect its left arm/boots and the rightward curling tail while excluding all independent face, rear-view, horn, tool and boot inset illustrations.
- **No generative modification** to the selected central character. Full 1254-square image with recomposed background was proportionally downscaled with LANCZOS; no forced crop, no figure cut, no stretch. The source original is unchanged.
- The 1024-square output was visually inspected as a **single head-to-boots figure**, both ram horns intact, boots/feet visible, left and right arms/hands, brass goggles, purple hair, deep-maroon face, necklace, practical vest, tool belt, trousers, gloves/bracers, and full arrow/spade-tipped tail visible. No surrounding inset panels, labels or borders remain. Some soft paper/background variation remains and is not character content.
- A representative **unmasked central-image pixel comparison** with direct Lanczos-resized F01 returned 100% identical RGB values across the sampled central interior areas (e.g. `(490,190)-(600,850)` and `(450,250)-(690,950)` after 1024 resizing), confirming the central design is source-derived rather than rerendered.
- Exact new deliverable: `/mnt/data/Hope_Akmenos_E001_Front_v1_PanelsRemoved_1024_sRGB.png`, RGB PNG **1024 × 1024**, **1,244,152 bytes**, SHA-256 `8c19629c99f5111bc56735473d9024d31a6a289f4cd6961b4d428bad48a960e1`. Embedded verified **588-byte ICC “sRGB built-in”**. The original had no color profile; **RGB interpreted as sRGB** to assign ICC, not colorimetrically measured.
- **Remaining compliance caveat:** The *source-selected* standing pose is slightly three-quarter/angled and Hope has her right arm/hand on her hip. This is **not a strictly neutral orthographic front**. Because the user explicitly requested preservation of that first figure, present this as an intentional *candidate exception* for review, never quietly recategorize it as a true orthographic model. If approved, the side/back stages still require actual owner-selected source conditioning and structural reconciliation.

## Approval and registry gate

- `FACE_APPROVED`: unchanged; exact `illustrations/references/Hope_Akmenos_E001_Face_v1_1024_sRGB.png` hash `1ef34cf6f619757df4e51e0f12a151965f1ed3381506af1b1c06c65667d3c91d`.
- `FRONT_CANDIDATE_AWAITING_OWNER_REVIEW`: image available in session; **do not claim** `FRONT_APPROVED` before the owner sees and accepts this *exact crop/composite* and its intentional nonorthographic pose.
- On acceptance, ensure same bytes transferred under new versioned `illustrations/references/` path, repo-read SHA-256, dimensions, embedded sRGB profile and image content; if transfer cannot be verified, record `FRONT_REGISTRATION_PENDING`. Only then `FRONT_APPROVED`.
- No code changed and no unrelated work touched. Local PNG decode/dimensions/ICC/SHA and image inspection **PASS**; repo registration and TWBD test suite **NOT RUN**.

[Earlier FRONT attempt audit](ILLUSTRATION_HOPE_E001_FRONT_ATTEMPTS_2026-10-25.md) · [Accepted face](ILLUSTRATION_HOPE_E001_FACE_ACCEPTANCE_2026-10-25.md) · [Workflow](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET.md)
