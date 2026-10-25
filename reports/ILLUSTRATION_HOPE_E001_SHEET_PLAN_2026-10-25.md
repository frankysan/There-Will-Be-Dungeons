# Hope Akmenos — E001 progressive design-sheet plan (2026-10-25)

**Request:** `$twbd-illustration-generate Wastes "Hope Akmenos" E001 design-sheet plan`  
**Branch / stage:** `DESIGN_SHEET / plan`; written planning only, **no image generated in this invocation**.  
**Subject:** `WASTES-HOPE-AKMENOS` (Oriphi “Hope” Akmenos; player Kristen); **appearance:** `WASTES-HOPE-AKMENOS-A01` (Dusthill/E001 organic baseline); **reserved sheet:** `WASTES-HOPE-AKMENOS-DS-001`.  
**State:** `BRIEF_READY` for one *provisional E001 face draft*; sheet still unapproved / initial image stage pending. Baseline subject record v0.2 and style guide v0.6 / locked style v2. No requested image asset or renderer input is being claimed.

[Integrated appearance evidence](../project/ILLUSTRATION_HOPE_AKMENOS_REFERENCE.md) · [Hope source audit](ILLUSTRATION_WASTES_HOPE_AKMENOS_AUDIT_2026-10-25.md) · [sheet ledger](../project/ILLUSTRATION_CHARACTER_DESIGN_SHEETS.md) · [canonical staged workflow](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET.md) · [reusable prompts](../.agents/skills/twbd-illustration-generate/CHARACTER_SHEET_PROMPTS.md)

## Source constraints and confidence

- **E001 confirmed in reviewed reader-draft ASR (S01–S02):** Hope is an adult **horned tiefling woman**, called Hope, visibly optimistic, mechanically skilled, building a vehicle compatible with a dragon engine in Dusthill, and plausibly in **work clothes**. No exact E001 hair, skin, eye, horn curve, jewelry or costume palette has been verified by listening.
- **Later D&D Beyond same-character snapshot (S03–S04), not opening canon:** maroon skin, purple hair, gold eyes, age 32, 5 ft 6 in and 140 lb; car-part armor and a keepsake necklace entered in the character's “Look” notes. Two JSON files duplicate the **same** character sheet; they are not independent sources. These facts guide *candidate* visual continuity, but do not prove E001 colors, exact stature or displayed equipment.
- **Independent source-family guidance:** 2014 D&D tiefling anatomy supports two horns, a long tail, pointed canine teeth and unusual eyes. The Wastes uses its own tiefling origin story; never add a generic Forgotten Realms lineage. Scott Johnson's undated drawing favors outward-swept horns, short/swept hair, goggles and workwear; Ron Tang favors horned braided hair and a tail; Casey Boyd favors pale hair. These archived art interpretations are **not owner-approved models**, and their licensing is not assumed.
- **Height:** player gives a tentative **~5 ft 6 in** in E088 (S19), consistent with the late sheet but conflicting with fan-wiki 5 ft 8 in. Use approximate 5 ft 6 in for scaling only, not as an E001 factual height statement.
- **Research not complete:** full original-dialogue sweeps E002–E037, audio verification, horn fitting chronology, E001 tail narration, necklace timing, exact costume and body colors remain open. They do **not** block a labeled provisional first E001 face study under the source-gated sheet policy.

## Proposed owner-reviewable E001 visual design (D choices, not spoken facts)

**Concept:** an **approachable, resourceful Dusthill tiefling engineer**, not a generic armored fantasy adventurer. Show her confidence and optimism through a direct lively gaze, quick almost conspiratorial smile, and practical posture.

1. **Face candidate D01:** woman in her early thirties, expressive brows, visible pointed ears, two fairly substantial **symmetrical organic horns** growing from the skull and curling outward/back in restrained ribbed arcs (Scott/Ron visual-language candidate, geometry not verified). Subtle pointed canines on smiling face. Neither horn metallic or broken.
2. **Palette candidate D02:** **deep maroon skin, purple hair, warm gold eyes**, carried over *provisionally* from the later character-sheet fields. Keep eyebrows and lips readable within the shared flat-shaded, inked graphic-novel treatment; neutral backdrop. Treat all three as a selection for owner review, not confirmed E001 colors.
3. **Hair candidate D03:** a **short/medium swept-back practical purple hairstyle**, kept clear of horns and ears, consistent with a mechanic's daily work. Prefer it as the first face concept because it is compatible with Scott's undated illustration and easily preserves silhouette across views. Long braids (Ron) and pale hair (Casey) are alternate archived interpretations, not extra features to combine into one head.
4. **Workwear candidate D04, for FRONT approval:** off-white/grey rolled-sleeve work shirt, weathered charcoal/brown utility vest or short jacket, muted dusty trousers, sturdy leather boots and reachable working pockets; subtle repaired fabric/salvaged detailing. Practical canvas/leather shapes rather than a grand late-series armor suit. Exact outfit colors/cuts, whether a small necklace and goggles appear, and belt/tools remain owner selections to lock **only when FRONT is approved**. A necklace would reference the character-entered keepsake concept but **its E001 wearing is unverified**; goggles are similarly only a Scott-image design lead.
5. **Body candidate D05:** humanlike athletic/work-capable proportions, all four natural limbs, one **long organic tail** emerging from the lower back, tapering with consistent root and cross-sectional geometry. The tail is species/archival-art supported but not yet directly described in the checked E001 scene; owner may accept its shape as art design. No asymmetric wounds or augmentation at baseline.

**Exclude from E001:** E033 rocket launcher; E037–E039 trauma, **mechanical anatomical LEFT arm/leg/horn** and wrist rocket; queen's crown and regalia after E054; E088 mirror-return body/scars/clothing; E101 **RIGHT Hand of the Voice**; end-game weaponry, equipment and machine augmentations. Do not use fan art with a later-era mechanical **right arm** as anatomical evidence.

## Progressive stage gates

| Stage | Intended output | Main continuity/approval check |
| --- | --- | --- |
| **FACE** (next) | Exactly **one** centered neutral-background head-and-shoulders portrait; no text, multi-views, weapons or sheet inset | Owner selects or corrects skin/hair/eye colors, horn size/root/curl, hairstyle/ear shape and likeness. Register accepted exact image after 1024-square PNG/sRGB check. |
| **FRONT** | Exactly **one** neutral head-to-boot frontal full figure, built from **actual FACE pixels as an attached visual input**, not merely text | Lock anatomy/proportions, organic hands/legs, tail visibility, one coherent practical outfit, pockets, boots, optional pendant/goggles/tools and exact accessory placements. |
| **PAIRED SIDES** | **Two strict 90° full-body anatomical projections** of *the same approved FRONT image*: **left panel Hope's LEFT** (she faces viewer-right →); **right panel Hope's RIGHT** (she faces viewer-left ←) | Both horns same physical root/curve across cameras; hair, ears, possible necklace, tail root/length and any asymmetry stay on the same anatomical sides, not mirror-copy geometry. Owner supplies approved front PNG as a direct image attachment to an image-edit request when necessary, following Stanley pilot. |
| **BACK** | Exactly **one** true orthographic rear view, preferably reference-conditioned from approved front and sides | Same horn bases, head/hair proportions, natural tail root and direction, seams, vest/jacket, boot heels and all selected utility gear. No invented backpack/weapons. |
| **ASSEMBLE** | Deterministic composite of exact approved anchor pixels, typically two **text-free** pages: comparable-scale front/both sides/back + full-resolution accepted face and approved tiny details | Never regenerate the figure to make a sheet. Review each assembled page independently; normalize/export/visually inspect/check SHA-256/ICC, then register in repository. Final `OWNER_APPROVED` needs owner's **separate composite-page approval** and repository readback. |

**Render invariants:** one 1024 × 1024 (1:1) PNG, *actual* embedded sRGB or verified conversion, immutable full style-lock v2 from generation SKILL.md §3B, bold variable-weight ink, adult-animation-influenced graphic novel, cel-shaded muted earth tones, no photorealism, lettering, watermarks or gratuitous props. Render one stage and one candidate at a time. Keep source findings, exclusions and source-license notes outside the image. Existing-project Hope PNGs: none found in `illustrations/references/` at plan stage; only archived undated external artwork with unresolved redistribution rights.

## Later appearance states — separate sheets/variants

This **E001/A01** sheet is a stable early anchor only. In **A03** her **anatomical left** arm and leg become mechanical (and a left metallic horn is later attested). **A05 (E088 resurrection in Sigil)** is a **new organic body**, with restored biological arm/leg, no integrated gun/metal prostheses but **old scars retained**; the original corpse remains behind. The status of the horn and exact scarring still need focused later-era verification. A05 arrives without clothing, then receives borrowed tunic/trousers and later distinct black/gold clothing. **A06 (E101)** replaces her **anatomical right hand** with the Hand of the Voice. Neither A05 nor A06 may be silently merged into E001.

## Result / next action

**Plan ready, not visual approval.** No image-generation call, image export or registration attempted. Documentation/readback verification applies only to this written report; artwork QA is **NOT RUN**. Preserve the existing dirty working-tree edits from other project activities.

**Next stage:** `$twbd-illustration-generate Wastes "Hope Akmenos" E001 design-sheet face`, using the provisional D01–D03 choices for a single portrait, then ask for explicit review before advancing.
