# Fate 4 — transcript appearance, features and capabilities audit

**Recorded:** 2026-10-25. **Status:** Findings saved at the owner's request
before the usage limit. Source research is substantial but final appearance
register integration and validation remain pending.

**Source revision:** `frankysan/There-Will-Be-Dungeons-Transcripts`,
commit `aabee4ffbdba2ff981522294c9dc0e62bfb0553d`.
[Current appearance register](../project/ILLUSTRATION_REFERENCES.md#wastes-fate-4) ·
[Earlier style trial](ILLUSTRATION_STYLE_STUDY_2026-10-25.md) ·
[Search manifest and review checkpoint](FATE_4_TRANSCRIPT_AUDIT_2026-10-25.json).

## Scope, method and limits

Screened **200 available primary Parakeet exports** whose names begin
`The Wastes` or `Bonus `, including later-season and retrospective
material. The search produced **528 raw cue candidates across 67 files**.
These are search candidates, not 528 genuine vehicle references:
phonetic variants also match phrases such as "feet for" and "feat for."

The initial screen covered Wastes S1E000–E066, both supplied E013.5
Parakeet copies, and available March–September 2019 bonuses; it was then
extended to all available Wastes and bonus Parakeet exports at this
revision. Inverse, Delvers and unrelated one-shots were not imported into
the Wastes continuity. Wastes-numbered standalone material was screened
without treating it as a main-party event.

The query searched Fate/Faith/Feet/Fete/Fat/Fayt/Fake/Fade plus
Four/4/For, RV, motorhome, monster truck, Winnebago and "vehicle of destiny,"
including adjacent-cue joins. Additional visual-term searches were applied
around candidate contexts. Sources were parsed completely for searching;
**semantic reading was of selected timestamped passages**, not every
word of all 200 recordings. The manifest records the actual windows
inspected, raw candidates and source Git blob identities.

Twelve Qwen Q8 exports were retrieved, including E006. Targeted passages
were compared directly in E001, E006, E010, E027, E028, E057, E065 and
E066. Other fetched Qwen files are not thereby fully reviewed.
**No audio or original design images were checked.** Agreement between
ASR versions supports a reading but does not certify the spoken words.

The workspace text reader/search could not expose the SRT corpus
(search scanned zero source files). Bounded binary reading succeeded,
but larger requested chunks were denied. Connected GitHub file reads
then supplied the transcripts at the exact workspace HEAD above.
Fetched blob identities matched the pinned source inventory.

## Appearance at introduction — essential illustration corrections

The principal description is **E006, approximately 02:15:48–02:19:10**,
supported by both Parakeet and Qwen.

| Feature | Transcript-supported finding | Locator |
| --- | --- | --- |
| Basic silhouette | Modified RV on enormous monster-truck wheels; strongly raised vehicle. | E006 P3037–3050 / Q3635–3655; E007 approximately 01:17:52–01:18:22 also calls it very tall. |
| Distinctive front | A **metal dragon-skull-like front feature**, explicitly not an actual dragon. | E006 P3040–3042 / Q3637–3641, approximately 02:15:54–02:16:07. |
| Outside movement | Metal railing along the exterior, allowing people to hold on and move around outside during combat. | E006 P3051–3055 / Q3656–3660, approximately 02:16:30–02:16:42. |
| Roof equipment | **Solar panels on top**. Exact number, layout and electrical function are not specified in the reviewed passage. | E006 P3062 / Q3666, approximately 02:16:51. |
| Combat handholds | Hang/grab bars on the roof and side for fighting and clinging to the exterior. | E006 P3085–3088 / Q3690–3696, approximately 02:17:49–02:18:00. |
| Roof access | Roof access in the unveiling; a usable hatch is explicit in later combat. | E006 P3085; E010 P1104–1106, approximately 00:45:57–00:46:10. |
| Rear access | A little ladder on the back; roof climbing via ladder is played in E007. | E006 P3119 / Q3730, approximately 02:19:04; E007 P145, approximately 00:07:01. |
| Back opening | Back door and rear window used/discussed after its return. | E026 P745–748, approximately 00:44:53–00:45:07; rear-door exit also E027 P2408–2412. |

**The two trial images omit essential established features, especially the
dragon-skull front and solar panels.** They test rendering only. The
first-pass instruction forbidding skulls must not be reused in a
source-faithful Fate 4 brief. Exterior combat handholds must be deliberate
features, rather than an ordinary decorative roof rail.

E010 approximately **01:07:23–01:07:35** explicitly gives a **ten-foot
width** (P1723–1728; Q2017–2023), so that measurement is now supported in
played dialogue as well as the prior design-register note. The
**thirty-foot length** remains inherited design-document information;
a confirming spoken length was not located in the reviewed passages.

## Interior, storage and domestic equipment

These are described in E006 approximately **02:17:31–02:19:05** in both
exports, unless otherwise indicated.

| Feature | Finding and boundary |
| --- | --- |
| Front seating | Driver's seat, **no ordinary shotgun/passenger seat**: weapons occupy that space. E010 approximately 01:46:48–01:46:56 reiterates a bucket of guns instead of a passenger seat. |
| Gear lever | Skull-shaped gearshift, removable for use as a stabbing spike. Do not confuse it with the much larger dragon-skull front feature. |
| Weapons | Glove compartment filled with guns and ammunition; further space for weapons, tools and scrap. These are stored weapons, not evidence of an installed turret. |
| Quick-access storage | Large interior wall magnet for javelins and similar equipment. |
| Communications | CB radio at the front and another at the back, allowing front/rear occupants to communicate "trucker style." Do not turn this into a mounted PA system. |
| Water | Thirty-gallon storage tank, described as supporting up to 28 days; retain as stated game-world provision, not a verified real-world consumption calculation. |
| Food | About a month's food-storage capacity. The actual departure supplies include potatoes, chew worms, smoked meats and pickled beets. Inventory changes during travel. |
| Sleeping | Four sleeping places, using a convertible sofa bed and additional mattresses pulled out across the floor. |
| Cooking | Hot plate. The reviewed unveiling does not establish a fitted full kitchen, oven or refrigerator. |
| Sanitation | Toilet/bathroom explicitly confirmed; passenger reluctance to use it does not remove it. |
| Furnishings | Sofa near a window (E010 approximately 00:44:45–00:45:10; E011 approximately 00:41:21–00:42:21). Cupboards are used during later scenes. |
| Workbench | Interior workbench beside/near the door: Stanley restrains Nash to it in E029 approximately 00:10:35–00:10:58; later references reinforce its use. |
| Cooler | Vorel rummages in a cooler in E028 approximately 01:36:06–01:36:20. This locates one in the vehicle then, without proving it was a permanently fitted refrigerator. |
| Later dining area | E065 approximately 00:56:14–00:56:50 describes seats around an RV-style table; Rorf bends/breaks the table and overloads the seating. |

Key E006 cue ranges: driver/storage/gear lever **P3079–3084 /
Q3682–3689**; radios/magnet **P3089–3095 / Q3697–3703**;
water/food **P3096–3101 / Q3704–3710**;
sleeping/cooking **P3102–3106 / Q3711–3716**;
toilet **P3108–3116 / Q3717–3727**.

Jimster supplies a **compass and binoculars** at departure (E006
approximately 02:30:50–02:31:10); Hope places the compass on the dash
around 02:34:44. These are supplied portable tools, not built-in instruments.

## Capabilities and limitations

| Capability or limit | Evidence and interpretation |
| --- | --- |
| Normal travel | E006 approximately 02:33:22–02:34:42 states 60 mph normal/top travel speed, with pushing up to about 80 mph possible. These are session travel rules. |
| Fuel | Same passage gives a 30-gallon fuel tank and about 20 miles per gallon. E006 approximately 02:31:18–02:31:35 separately mentions a filled reserve gas tank. Exact reserve capacity is not established here. |
| Overheating | Above 60 mph, hourly overheating checks; after more than 16 hours of driving, further hourly checks. The spoken downtime formula is muddled in both ASR versions (2d10 / 12 hours / at least six hours); **leave the exact formula unresolved**. |
| Actual failure | E007 approximately 01:17:20–01:20:58: engine pops, black smoke blocks visibility, then the RV stops and a front-end explosion sends shrapnel into the cab. It is disabled, not permanently destroyed at this point. |
| Horn | E007 approximately 00:28:41–00:28:58 explicitly confirms a horn. A later production discussion refers to sourcing its honking sound. |
| Roof use | Characters observe, fight and climb from the roof/hatch and exterior handholds; this does not make all later patched roof areas load-bearing. |
| Rest while traveling | E006 approximately 02:39:51–02:40:39 permits resting passengers while the driver/lookout remain active, with rotation possible. |
| PA system | E010 approximately 00:26:41–00:26:59 explicitly says there is **no PA system on Fate 4**. Stanley's carried megaphone is separate personal equipment. |
| Traction | E065 approximately 00:57:45–00:58:20: monster tires still slip/sink in wet sand. Do not portray them as guaranteeing all-terrain mobility. |
| Materials | E059 approximately 02:27:27–02:27:43: Nash says Fate 4 contains steel. This is a character observation, not proof of universal steel construction or armor. |
| Weight | E064 approximately 02:31:55–02:32:08 gives an **average camper-trailer weight** during a carrying-capacity discussion. It is not a measured Fate 4 curb weight. |

Solar panels do **not** establish solar propulsion, unlimited range,
a silent engine or a specified battery system. No transcript-grounded
mounted gun, turret, rocket launcher, armor rating or exact engine model
was established in this pass.

## Appearance and condition changes to retain

| Phase | Supported state | Important boundary |
| --- | --- | --- |
| Earlier origin, revealed later | E067 approximately 00:14:59–00:17:31 presents Hope reliving an early Jimster memory: the unmodified RV has **ordinary tires**, is musty/greasy and in disrepair, with no Hope modifications. Jimster demonstrates a cassette player. | Retrospective memory sequence, **not restoration after E066**. Continued cassette-player fit at the E006 unveiling remains unconfirmed. |
| E001 workshop | Approximately 00:17:09–00:18:45: a "small, crappy" RV on huge wheels; Hope installs the last monster wheel. Both exports support it. | E006 later calls it a big RV. Preserve both descriptions; do not invent an intervening body enlargement. |
| E005 unfinished project | Approximately 02:09:48–02:10:30: RV still being worked on and not yet named in the dialogue. | Distinguish workshop appearance from E006 public unveiling/maiden departure. |
| E006 unveiling | Full equipment description and stocking for travel. | Introduction-state baseline, with no invented paint scheme. |
| E007 breakdown | Smoke, front-engine explosion and immobilization. | Temporary disablement; E010 approximately 00:08:33–00:08:36 explicitly confirms repair. |
| E010 capture / E017 abandonment | E010 approximately 01:47:29–01:47:48: a tire is punctured by a spear-like weapon and the vehicle becomes unstable. E017 approximately 02:43:41–02:44:03 still describes damaged tires. | E011 retrieves a largely intact RV in the parking lot, but that is not proof it is fully roadworthy. The party leaves in a separate station wagon. |
| E026 recovered and repaired | Approximately 00:24:20–00:25:10: Bertrand explains repairs and bringing it back. Approximately 00:43:46–00:44:53: skull shines in sun; earlier damage appears repaired and engine starts immediately. | This is the actual repaired return, not an E017 offscreen restoration. |
| E027 blast | Approximately 02:22:00–02:27:49: explosion overturns RV; it is temporarily magically reduced for righting and returns to normal size. Large upper-left/driver-side roof area, including windshield area, is torn open. | Dialogue corrects a diameter estimate while the RV is reduced; do not fix a precise hole diameter from this passage. The resize is an external spell, not a vehicle feature. |
| E028 hide repair | Approximately 01:42:05–01:44:42: Vorel and Bok Bok make a **quilt of raptor skin/scales**, sewn with fine stripped-bone thread; Hope fastens it over the opening with nails. | Cover only: **anyone standing on it falls through**. It is not rebuilt metal roof or load-bearing armor. |
| E028 additional damage | Approximately 01:48:48–01:49:25: Stanley fires Eldritch Blast past Tedna into the wall behind him, causing a new blast opening; later dialogue notes the just-repaired hole. | Do not conflate this later wall damage with the large roof opening. |
| E057 / E059 | E057 calls Fate 4 intact and leaves it in the royal truckery; E059 approximately 01:54:47–01:55:04 says it has been fixed up, and the party selects it again. | Detailed repairs, replacement roof fittings and new equipment are not inventoried. Do not assume every earlier hole or solar panel has an individually verified repair. |
| E065 storm | Approximately 00:56:14–00:58:20: Rorf damages the dining table/seating; driver's seat is loose and wobbly; vehicle becomes stuck in wet sand. | Scene-specific interior/condition state. |
| E066 destruction | Approximately 00:18:21–00:19:08: the tyrannosaur crushes it, wheels fly off and body collapses into metal wreckage. Approximately 00:30:36–00:31:03: later explosion and fire. | Separate crushing from the subsequent fiery explosion. The original RV is destroyed. |
| E066 salvage | Approximately 00:39:04–00:42:15: **two bent axles**, sturdy custom monster tires and a recovered seat are used with dinosaur bones and rope for a completed bone-and-metal rickshaw. | A different salvage construction, called **Fang Fate Five** in both ASR versions; not a rebuilt, powered Fate 4. Exact display spelling still provisional. |

## Misleading leads and excluded features

**E057 has a material existing-summary error.** The dossier currently
describes departure in a royal monster truck. Both source exports instead
show an initial discussion of a monster truck, then an actual **interceptor**
selection. At approximately **00:47:38–00:50:20**, the chosen interceptor
is old/rust-brown, has chained tires and prominent front engine/exhaust
hardware; the party drives past Fate 4, which stays behind. **Those paint,
chain and engine details belong to the interceptor, not Fate 4.**
Correct the dossier and any directly affected summary in a bounded follow-up.

**April 2020 bonus, approximately 00:20:57–00:21:35:** a cast member imagines
owning a real-life Fate 4-like van, with lettering, window shutters and a
mounted gun. This is a hypothetical real-world vehicle, **not a newly
established Fate 4 gun mount or paint scheme**.

**April 2019 bonus:** the nautical/Waterworld version is hypothetical.
**September 2019 bonus, approximately 00:10:07–00:11:27:** a prospective
next vehicle/motorcycle and "Kismet" are future discussion; distinguish
that unbuilt powered successor from E066's actually completed salvage
rickshaw. The naming explanation says destroyed Fate vehicles advance
the number.

**September 2020 bonus, approximately 00:10:52–00:11:22:** recalls Vorel
declaring himself Lizard King on the vehicle; it does not establish
painted "Lizard King" signage.

**May 2020 bonus, approximately 00:24:58–00:25:47:** discusses sourcing
horn and engine sound effects, including a Mad Max game sound. This is
production provenance, not a canonical engine make or a newly reviewed
audio passage.

Later hits include reminiscence, spelling/phonetic false positives and
S2/S3 references that still need contextual triage. The manifest retains
them. No claim of exhaustive recovery from every ASR miss is made.

## Revised illustration requirements

For an E006-era exterior, preserve:

- RV body on conspicuously oversized, raised monster-truck wheels.
- **Fabricated metal dragon-skull front** as a defining recognition feature.
- **Roof solar panels**, **rear ladder**, **roof access/hatch** and
  deliberate **roof/side combat grab rails**.
- A side entrance and, where the relevant later state is used, the
  supported back opening; exact handedness/layout still needs confirmation.
- An era-appropriate roof: intact at unveiling, then torn and later
  visibly patched with non-load-bearing raptor hide when applicable.

For an interior, preserve the driver's seat and **weapon-filled space in
place of a normal front passenger seat**, removable skull gear lever,
glovebox weapons/ammunition, wall magnet, front/rear radios, water tank,
sofa-bed/floor mattresses, hot plate, toilet, workbench and storage.
Attach later items to their located phase rather than silently placing
every feature in the unveiling.

Keep the trial's ivory/sage/coral paint, cab-over body, exact window
arrangement, decorative fittings and precise suspension layout
**provisional artistic choices**. This audit did not verify a canonical
body paint color or exact original make/model. Existing style previews
must not be selected as continuity references without revision.

## Resume checkpoint and remaining work

**Completed:** current source inventory/ref identified; 200 primary
exports fetched/parsed/screened; candidate catalog saved; selected passages
read; several high-value descriptions checked in Qwen; findings recorded
here with chronology and rejected-lead boundaries. No source SRT/media
was edited. No new image was generated for this audit.

**Immediate next actions:**

1. Integrate these findings into the appearance register, preserving the
   old 0.2 record before any major rewrite and retaining its trial
   decisions as historical artistic choices. Keep existing A01 stable.
2. Add distinct damage/repair states and the retrospective origin state;
   distinguish a salvage rickshaw from the destroyed powered RV.
3. Correct E057's monster-truck/interceptor summary, using the compared
   00:47:38–00:50:20 passages. Do not re-research the entire episode.
4. Triage retained later-season/bonus candidates and unreviewed Qwen
   passages only where they can add a visual feature or resolve a conflict.
5. Directly inspect the source design images when access is available.
   Resolve dimensions/layout/paint without promoting the trial to canon.
6. Validate only the new report/manifest and changed reference sections.
   Canonical Markdownlint is still unavailable in this environment;
   no automated lint pass is claimed.

The current appearance register and earlier style-trial report still
describe the pre-audit state until item 1 is performed. Resume from this
checkpoint rather than refetching all 200 primary exports or claiming
that documentation integration has already happened.
