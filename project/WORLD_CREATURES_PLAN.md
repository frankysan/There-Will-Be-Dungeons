# Planning a creatures and monsters category

**Status:** Initial scope and candidate inventory; no creature canon or new
subject pages are established by this plan.

## Purpose and scope

Add a reader-facing **Creatures and monsters** category to The Wastes world
reference. Prioritize:

1. Creatures or kinds of beings that appear to be original to this campaign.
2. Familiar D&D creatures with clearly evidenced, consequential campaign
   differences.
3. Individual creatures whose unusual abilities, origin, transformation, or
   role in the setting warrants a cross-reference even when their identity
   already has a character page.

Do not turn this into a catalog of every ordinary D&D encounter. A creature
does not qualify as a variant just because an episode uses it, gives it a
different name, or leaves its abilities unexplained.

## Proposed structure

- `world/CREATURES_AND_MONSTERS.md`: concise category index, grouped by
  campaign-original beings, materially adapted creatures, and notable
  individual cases.
- `world/creatures/`: detailed pages only for creature kinds or subjects that
  need more than an index entry.
- Existing character pages remain the canonical biographies for named,
  person-like NPCs. The new index should link to them rather than duplicate
  their histories. An individual can appear in more than one index when the
  category is useful to readers.
- Keep setting-wide systems and uncertain cosmology in `world/WORLD.md`;
  keep hostile-role navigation in `world/ANTAGONISTS.md`.

The category should be added to the [world portal](../world/README.md) only
when its index has a useful, source-supported starter set.

## Editorial and comparison rules

- Label a case as **campaign-original**, **campaign-modified**, **individual
  variation**, or **baseline status unknown**. Do not infer a species-wide
  trait from a single creature.
- For a D&D comparison, identify the specific official edition and creature
  entry being used as the baseline. Keep published baseline mechanics,
  table-specific rulings, observed campaign behavior, and character testimony
  distinct. If the comparison cannot be sourced, describe the campaign
  evidence without claiming a deviation.
- For campaign-original beings, explain what makes the concept distinctive
  from the recorded evidence; do not invent a D&D counterpart.
- Cite the episode dossier at each material claim. Mark ASR-only names and
  mechanics provisional; a second ASR is not audio verification.
- Do not add stat blocks, inferred alignments, ecological claims, or
  game-mechanical abilities that are not supported by sources.
- Preserve character/creature distinctions: a named sentient being is not
  reduced to a monster entry, and a creature category is not a claim that the
  subject is hostile.

## Initial candidates to assess

| Candidate | Existing canonical page or evidence | Why it merits review | Boundary or open question |
|---|---|---|---|
| The Earth-desert black dragon | [Profile](../world/characters/imprisoned-black-dragon.md) · [E121](../episodes/E121.md) · [E122](../episodes/E122.md) | Its demonstrated interaction with Diontalus's spectral form, restorative blue mist, natural heart, and spectral mother give it unusually specific campaign lore. | The dragon's history and genealogy are partly testimony; its exact name remains provisional. Compare against a cited baseline before calling any ability a D&D deviation. |
| Squirts's return | [Profile](../world/characters/squirts.md) · [E111](../episodes/E111.md) · [E125](../episodes/E125.md) | An observed death followed by a later bodily return through an infernal medical process is a notable campaign-specific creature lifecycle. | Keep Squirts's character page canonical. Brent's account of the soul and alterations is not independently verified; do not generalize this process to kobolds. |
| Henatar/Henitar Grape (?) | [Profile](../world/characters/henitar-grape.md) · [E125](../episodes/E125.md) · [E126](../episodes/E126.md) | His three-headed presentation and unusual magical equipment make him a useful test of whether a named NPC's creature traits belong in this category. | The current evidence establishes an individual description, not a species or stat-block variant. Name spellings and any final disposition remain unresolved. |
| Nash in black-dragon form | [Nash](../world/characters/nash-maggard.md) · [E126](../episodes/E126.md) | His played transformation provides a current example for distinguishing a familiar creature form from campaign-specific traits. | Do not create a dragon-form page or claim modified dragon mechanics without evidence beyond the transformation itself. |
| General Carthax | [Profile](../world/characters/general-carthax.md) · [E111](../episodes/E111.md) | His demonic identity and capture through Elhandari empathy/anti-aggression devices may help distinguish creature traits from campaign-specific treatment. | The device's effect is not proof that Carthax's underlying demon nature differs from a D&D baseline. |

These are research leads, not a commitment to publish five entries. Begin with
the cases that have the clearest evidence of campaign-specific biology, powers,
or lifecycle; keep ordinary encounters and unsupported extrapolations out.

## Implementation sequence

1. Review the cited dossiers and existing profiles, and add exact timestamps
   and evidence tiers for candidate claims.
2. Choose a small starter set. Resolve whether each item belongs as a link to
   an existing character, a new creature-kind page, or no entry.
3. For each claimed D&D difference, identify and check the official baseline;
   otherwise retain **baseline status unknown**.
4. Create the concise category index and only the necessary pages under
   `world/creatures/`; follow the [world reference template](WORLD_REFERENCE_PAGE_TEMPLATE.md).
5. Add the category to the [world portal](../world/README.md), reconcile its
   spoiler horizon with the maintained reference pages, and validate new
   relative links.

**Coordination note:** The portal currently states a researched horizon of
E125, while an E126 dossier and related working-tree edits are present.
Reconcile and update the horizon as part of a future category publication;
this initial planning pass does not modify those in-progress files.
