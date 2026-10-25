# Dusthill illustration research — bounded source audit (2026-10-25)

**Subject:** `WASTES-DUSTHILL` / The Wastes / settlement. **Primary result:** [integrated Dusthill appearance record](../project/ILLUSTRATION_DUSTHILL_REFERENCE.md), v0.1; two relevant scene states, **no town illustration generated**. **Source workspace at start:** repository branch `main`, HEAD `181342d2540927c2411e37e1115df480eff3c51f`, Git worktree initially clean. All source readings and previous visual claims distinguished by role. No audio verification.

## Aim, access and method

The requested entity is **Dusthill** (ASR `Dust Hill`), not the separate research subject [Jimster's garage](../project/ILLUSTRATION_JIMSTERS_GARAGE_REFERENCE.md). No episode cutoff specified. Followed the [research skill](../.agents/skills/twbd-illustration-research/SKILL.md) and [subject template](../project/ILLUSTRATION_SUBJECT_TEMPLATE.md). Looked at [Dusthill world page](../world/places/dusthill.md), E001/E005/E006 dossiers, garage reference, art index, image provenance and existing revision queue. Public wiki search returned an opening passage attributed to Beau that broadly agrees with the two ASR versions. It is **not** independent audio validation or an era-matched settlement plan.

**Exact text windows inspected:**

- `sources/The Wastes S1E001. The Campaign Begins!.parakeet.processed.srt`: opening ~00:04:42–00:08:26, plus exploratory cues ~00:09–00:14; **two-ASR comparison** for town's location, structures, cave farms, central well, old infrastructure and pictograms.
- `sources/The Wastes S1E001. The Campaign Begins!.qwen-q8+canary-ctc.raw.srt`: the same GM introduction ~00:04:44–00:08:27, including the pictograms passage; main material descriptions agree. Both exports may inherit acoustically incorrect phrases; no listening.
- `sources/The Wastes S1E005. Goblincide.parakeet.processed.srt`: directly read ~01:06:48–01:08:48 (tent, clearing, fire pit, first sight of attack), ~02:03–02:08 (Jimster's report, dark-farm refuge), ~02:13–02:20 (aftermath and returning civilians), with a keyword skim of further neighboring cues.
- `episodes/E006.md`: inherited earlier navigation notes for working water valve, Shun'ti's meeting and Fate 4 departure; **this run did not directly reopen the E006 raw scene**.
- `project/ILLUSTRATION_JIMSTERS_GARAGE_REFERENCE.md`: inherited time-specific garage description and E067 subjective-memory treatment, not a fresh E067 transcript reading.
- `project/IMAGE_ASSETS.md`: previous documented inspection of `Map_BeyondTheDeadfingers_resized.webp`, no direct new map-pixel inspection.
- Fan wiki home-page opening text obtained by public search (source text attributed to Beau; secondary publication).

**Search coverage and limits:** Searched the workspace `sources/` for `Dusthill` and `Dust Hill`; one broad search screened **179 files / 33,796,270 bytes before truncating**, a separate search **174 files / 31,678,000 bytes before truncating**. This is **not** all Wastes episodes or even necessarily all matching sources; `sources/` also has Delvers and other model exports. Searched `episodes/` and `project/`, each query truncated, then selected relevant early episodes deliberately. Directory-wide further scanning and later Dusthill references are an open next phase. Screens of E000/E059 source SRTs were **not** newly read (their dossier/world material was). Exact audio times are cue-clock estimates from ASR, not independently established sound clocks.

**Image inspection:** Listed `illustrations/wastes/` containing the selected `fate-4-e006-unveiling-jimsters-garage.png`. Queried binary metadata: PNG 2,132,655 bytes, SHA-256 `0a502a8813a125ff9d3083dde643ddd7a2347a8f7684d8ab704e3fbf4de09b43`. **Did not reconstruct/review its pixels**: a multi-chunk retrieval attempt hit a tool-call-count limit. `sources/images/` directory listing was denied; the regional map is known through the prior `IMAGE_ASSETS.md` audit, not direct review here. The selected PNG's existence does **not** confirm its depicted details.

## High-confidence visual facts within ASR-text limitations

| ID | Source/event | Established for depiction | Limit |
| --- | --- | --- | --- |
| S01 | E001 GM ~00:05:17–00:05:54 | Deeply sheltered **red-rock alcove**, unusually hidden **winding entrance**, huge red rocks making natural rampart, defended gate and high positions | No compass direction, exact heights, engineered full wall, street plan |
| S02 | E001 GM ~00:06:31–00:07:14 | Mud huts; a few wooden/metal barns as halls/storage; rear cave farms with animals, wheat/potatoes/beans and irrigation | Not open surface fields as primary farm; number/location of barns unspecified |
| S03 | E001 GM ~00:07:14–00:08:13 | Mechanical salvage garage; central well/outlet operated by **valve**, ancient pump beneath; village-rock pictograms | No visible surface dragon engine or proven rope-and-bucket well appearance |
| S04 | E005 GM ~01:07:50–01:08:02 | **Clearing/fire pit beside Hillmaster's tent**, gathering point | Relationship to central water outlet still unknown |
| S05 | E005 Jimster ~02:05:03–02:05:23 | Goblins over defenses; civilians barricaded in rear farm; garage secured with trucks retained | In-character testimony; not total attack map |
| S06 | E005 GM ~02:19 | People return from cave farm refuge; inspect corpses, damage and homes | Exact house damage, arson or total lost structures not given |
| S07 | E006 dossier | Meeting/casualty report and water **confirmed running at surface**, Fate 4 departure | Already curated and ASR-provisional; not newly listened or primary re-audited |
| S09 | Garage subject reference | Cliff-excavated garage, open town frontage and outer vehicle doors | Spatial reconciliation not measured |

**Chronology:** `WASTES-DUSTHILL-A01` is the opening settlement; `WASTES-DUSTHILL-A02` is E005 raid/E006 recovery and departure. Their common terrain and built character are distinguished from temporary damage and occupants. Earlier E001 water service may fail but physical drying/repair of street infrastructure cannot be inferred. Later E059 return of captives **occurs in Tietkalla**, not proven rejuvenation of Dusthill. No complete post-E006 settlement state yet described.

## End-of-campaign JSON cross-reference

Inventoried the exact `sources/json/` directory: **14 files**, including **seven** Wastes-specific files examined here — `nash-maggard.json`, `hope-akmenos.json`, `vorel.json`, `stanley-billings.json`, numbered Hope and Vorel exports, and `19247178--Squirts.json`. Actual one-line JSON was read and parsed programmatically, inspecting `data.name`, `data.id` and campaign-specific `data.notes` fields while excluding stock rules text and account data. The two namesake numbered files share the same character-sheet IDs as Hope/Vorel's named exports, so **not independent source witnesses**. Other numbered exports in this mixed directory were inventoried by filename but **not parsed and not assumed to be Wastes**.

- Hope `data.notes.otherNotes`: player-written claim of ~1.5 years living in Dusthill before play — useful character-background lead, **not building evidence**, source time `campaign_end`.
- Vorel `data.notes.allies`/`organizations`: shopkeeper family `Boxto, Rintolieal and La La`, Hillguard label and `Jimster` under a 'Dead' grouping. The latter could refer to **a later time**; do not turn it into an E005 or E059 death. Compare against an independently dated episode before resolving.
- Stanley `data.notes.enemies`/`otherNotes`: **Softhead betrayal accusation**, **Wilma/Aaron**, a **Scoutmaster** and Elhandar-bound data core. Candidate orthography and associations, not proof of an unobserved betrayal or exact early transfer.
- Nash and Squirts: no direct visual description of the village found in the specifically checked names/notes; a negative targeted scan is not whole-sheet/whole-campaign absence.

Final-sheet facts are neither contemporaneous Dusthill maps nor evidence of depicted early clothing or installed equipment. The related character-sheet notes are recorded as leads only in the integrated reference.

## Rejected assumptions and possible traps

- **Generic desert town image**: similarity alone does not verify an official Dusthill image; web image search surfaced unrelated town cartography and was **not adopted**.
- **A visible river or conventional village well**: the surface *valve outlet* and underground supply are the evidenced mechanics.
- **Continuous masonry wall or grand straight gateway**: natural giant red-rock protection is key; E005 'jumping over wall' is not a measured architectural material description.
- **Farms outside the settlement**: the described 'dark farms' lie in caves at the rear.
- **Blanket burned-out town**: E005 damage/casualties do not confirm fire, exact ruined buildings or overall destruction.
- **E059 rescue re-populates/restores Dusthill**: the return happens in Tietkalla; physical Dusthill status unshown.
- **Later archival map as E005 player handout**: map's era unknown.
- **Hope/Vorel duplicate JSON exports**: same underlying character-sheet IDs, not corroboration.
- **Final sheet's `Jimster` dead annotation**: not an E005/E006 condition; no contradiction with E059 unless a dated later narrative says so.

## Existing-image decision

Selected `WASTES-FATE4-ILL-001` is a **garage interior E006 scene**. This town-wide audit primarily adds details not necessarily visible from within that facility. No specific existing image region was confirmed inaccurate; image remains **provisionally unchanged**, not newly visually approved. Earlier vehicle style trials remain superseded under [IRV-0001](../project/ILLUSTRATION_REVISION_QUEUE.md#irv-0001--fate-4-early-style-previews-lack-defining-unveiling-features). **No new IRV flag** added without an evidenced in-frame problem; re-open pixels before claiming a full visual-impact pass.

## Follow-up: newly located village layout map (2026-10-25)

The user pointed to `local/images-wiki/maps/Dusthill.webp` (formerly `DVJ4V1JVwAErBl-.webp`), relocated from the earlier image inventory into a private `local/images-wiki/maps/` directory. This binary was **directly read and its actual pixels examined**: 166,822 bytes, SHA-256 `141731587b065a5271a6814c2d1cfd264f8b8a0a86b3fdbe41219266ef7bc5ce`. Hand-drawn on hex-grid paper, marked `DUSTHILL`, with a rough `pop - 200-300 estimated` note. Labels distinguish `Gathering Circle` from `well`, identify school, Hillmaster hut, food stores, barn, barracks, trading post, dark farms in two right-side areas and garage beside a `rock door`. Several labels (shop name, top buildings) are difficult to decipher. This is a **source image** with unknown authorship, revision date, use in campaign and scale — more geographically specific than the opening GM narration, but not independently authenticated as an E001 plan. Pixel-derived building order and compass direction must not be treated as precise coordinates.

The [active Dusthill reference](../project/ILLUSTRATION_DUSTHILL_REFERENCE.md#newly-inspected-dusthill-plan-2026-10-25) now records the map evidence and contrasts it with the generated E001 panorama selected by the owner. [IRV-0002](../project/ILLUSTRATION_REVISION_QUEUE.md#irv-0002--e001-dusthill-aerial-versus-newly-found-map) flags the **potential** layout mismatch for research/review; no proven contradiction, generation or publication. The earlier map absence in this report is superseded only for this **specific directly inspected map**. Owner provenance note (2026-10-25): the owner recalls that the map likely comes from the GM but cannot confirm this. This is a plausible attribution lead, not independently verified. No audio or exact map provenance has been verified. **Next:** establish the map's provenance/era, then reconcile site arrangement against scene descriptions and re-evaluate the selected opening-town image.

## Rename and wider map-provenance update (2026-10-25)

The owner renamed the full privately held map folder to descriptive location filenames and now considers **all six maps likely GM-originated**. This is `owner-recollection / probable-GM-origin / unverified` for **each** map, not an authenticated creator credit or a reusable-image license. The current `local/images-wiki/maps/` inventory contains `Dusthill.webp`, `Dusthill Caverns.webp`, `Slavetown.webp`, `The Teet and Trashburg.webp`, `Beyond the Deadfingers.webp`, and `Beyond the Deadfingers - Annotated.webp`. These exact files were enumerated and their present binary sizes and SHA-256 values checked; the [image provenance catalog](../project/IMAGE_ASSETS.md#current-private-map-collection--renamed-2026-10-25) records the old-to-new names and file hashes. Previous filename mappings for the other five rest on matching unique archived file sizes and names, not a second hash read of their old paths.

The earlier inspected `DVJ4V1JVwAErBl-.webp` is now **`Dusthill.webp`**, with **identical SHA-256** `141731587b065a5271a6814c2d1cfd264f8b8a0a86b3fdbe41219266ef7bc5ce`. Separately, **`Dusthill Caverns.webp`** (earlier `DVJ4cN3VAAAkrng.webp`, 101,972 bytes; SHA-256 `13eca8a7c34d72daaf07e60394c9cc8fb4ba64cf7f257a2ff03b27bce82ce268`) was **actually visually inspected**. It depicts a separate underground diagram featuring two `pit` regions and a bridge, sketched connecting paths, built features and other marks; difficult handwritten annotations were not treated as canonical names. Distinguish it from the **surface** village schematic and do not place its geometry into an E001 aerial street view. The other four map files received **metadata checks only** in this update, not new pixel reviews.

The [Dusthill illustration reference](../project/ILLUSTRATION_DUSTHILL_REFERENCE.md) was incremented to v0.2 and its layout/source notes adjusted. The E001 aerial `IRV-0002` remains a **provisional new-context review**; no new image generation, selection change, map publication or `/world` image embed occurred. Source stage remains **post-rename reference maintenance**, and provenance/era checks remain the next substantive research question.

## Resumable checkpoint

- **Source ref:** `main@181342d2540927c2411e37e1115df480eff3c51f` at start; no original SRT/media edits.
- **Completed:** Identity, initial text search and high-density opening/raid windows, same-campaign sheet-note leads, initial state descriptions, register integration, metadata-level existing image triage.
- **Files written:** [Dusthill active reference](../project/ILLUSTRATION_DUSTHILL_REFERENCE.md), this audit, [appearance index](../project/ILLUSTRATION_REFERENCES.md).
- **First incomplete phase:** Full campaign-episode expansion/search manifest; visual pixel review and additional independent-ASR/audio verification thereafter.
- **Next bounded step:** **Reopen the selected E006 garage PNG pixels and check its visible rock/workshop environment**, then (if a mismatch is genuinely visible) create/deduplicate an `IRV-####` item. Further pass: source inventory/time-window scan of remaining Wastes mentions, especially possible later physical returns.
- **Validation state:** Creation and complete readback of both new Markdown files and the modified index **passed** (stable IDs and headings present); final Git status was inspected, with three Dusthill-related changes and other unrelated Delvers edits appearing in the live worktree after the initially clean status. Those unrelated files were untouched by this task. Dedicated Markdown lint/unit checks **not run** (the available bounded check tool is InfinityDB-specific). No original SRT/media was edited; no commit or push.
