# Delvers — cleanup migration manifest

**Baseline:** 2026-10-26, before the first implementation slice. **Status:** Every in-scope file structurally inventoried; claim-level horizon, identity and final-state acceptance remains pending unless recorded separately. [Plan](../../../../../project/DELVERS_CAMPAIGN_CLEANUP_PLAN.md) · [Detailed baseline](../../../../../project/DELVERS_CLEANUP_BASELINE.json).

## Method and boundaries

The JSON records file hashes, headings, per-section prose counts, detected source IDs, candidate arcs, inbound Markdown links/anchors, footnote diagnostics, dependencies and proposed treatments. Episode IDs found in text are discovery leads, not verified horizons or last observations. Counts exclude headings, tables, fenced examples, complete footnote blocks, code and navigation-only lines. Inbound links cover maintained Markdown; external consumers and archives need separate checks before any move.

Each row has a proposed disposition; structural inventory does not certify factual accuracy or completed migration. Open evidence questions stay in the [campaign queue](../../../../../delvers/REVIEW_QUEUE.md) and [ledger](../../../../../delvers/world/CONSISTENCY_LEDGER.md). No aliases or identity merges are authorized by filename similarity.

## Page inventory

| Page | Purpose | Prose words | Priority | Structural findings / intended treatment |
| --- | --- | ---: | --- | --- |
| [delvers/DOCUMENTATION_PLAN.md](../../../../../delvers/DOCUMENTATION_PLAN.md) | editorial-plan | 1044 | P1 | No selected structural flag; replace obsolete active instructions; preserve dated history |
| [delvers/narrative/FIRST_JOBS.md](../../../../../delvers/narrative/FIRST_JOBS.md) | historical-study | 2628 | P2 | No selected structural flag; retain detailed historical study; compare unique scenes with primary arc |
| [delvers/narrative/README.md](../../../../../delvers/narrative/README.md) | navigation | 981 | P1 | No selected structural flag; reconcile current route and descriptions; retain canonical targets |
| [delvers/narrative/SEASON_ONE_ARC.md](../../../../../delvers/narrative/SEASON_ONE_ARC.md) | arc-narrative | 1849 | P1 | No selected structural flag; outline then consolidate with preservation and scene coverage |
| [delvers/narrative/SEASON_THREE.md](../../../../../delvers/narrative/SEASON_THREE.md) | arc-narrative | 13724 | P1 | unreferenced footnote; outline then consolidate with preservation and scene coverage |
| [delvers/narrative/SEASON_TWO.md](../../../../../delvers/narrative/SEASON_TWO.md) | arc-narrative | 9270 | P1 | No selected structural flag; outline then consolidate with preservation and scene coverage |
| [delvers/narrative/SKULL_KEEP.md](../../../../../delvers/narrative/SKULL_KEEP.md) | historical-study | 1069 | P2 | No selected structural flag; retain detailed historical study; compare unique scenes with primary arc |
| [delvers/narrative/THE_RISE_TO_BRONZE.md](../../../../../delvers/narrative/THE_RISE_TO_BRONZE.md) | historical-study | 1240 | P2 | No selected structural flag; retain detailed historical study; compare unique scenes with primary arc |
| [delvers/narrative/THE_WELLS_OF_ATOMER.md](../../../../../delvers/narrative/THE_WELLS_OF_ATOMER.md) | historical-study | 3168 | P2 | No selected structural flag; retain detailed historical study; compare unique scenes with primary arc |
| [delvers/README.md](../../../../../delvers/README.md) | navigation | 1631 | P1 | No selected structural flag; reconcile current route and descriptions; retain canonical targets |
| [delvers/REVIEW_QUEUE.md](../../../../../delvers/REVIEW_QUEUE.md) | review-register | 9096 | P1 | No selected structural flag; keep open listening issues and closed intake history distinct |
| [delvers/SOURCE_INVENTORY.md](../../../../../delvers/SOURCE_INVENTORY.md) | source-register | 750 | P2 | No selected structural flag; retain exact identities and source limits; check coverage statements |
| [delvers/world/characters/alexandre-vanderbuck-withers.md](../../../../../delvers/world/characters/alexandre-vanderbuck-withers.md) | character | 945 | P2 | episode IDs in body; emphatic action bookkeeping; unreferenced footnote; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/ambermoor.md](../../../../../delvers/world/characters/ambermoor.md) | character | 733 | P2 | episode IDs in body; research language in body; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/anthela-spiros.md](../../../../../delvers/world/characters/anthela-spiros.md) | character | 1390 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/barclay-vandergeist.md](../../../../../delvers/world/characters/barclay-vandergeist.md) | character | 739 | P2 | episode IDs in body; research language in body; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/broadside.md](../../../../../delvers/world/characters/broadside.md) | character | 469 | P2 | unreferenced footnote; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/buck-broscale-wildfire.md](../../../../../delvers/world/characters/buck-broscale-wildfire.md) | character | 887 | P2 | episode IDs in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/carrie-underworld.md](../../../../../delvers/world/characters/carrie-underworld.md) | character | 1196 | P2 | episode IDs in body; unreferenced footnote; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/cassius.md](../../../../../delvers/world/characters/cassius.md) | character | 1927 | P2 | episode IDs in body; emphatic action bookkeeping; unreferenced footnote; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/chad-brad.md](../../../../../delvers/world/characters/chad-brad.md) | character | 589 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/cheet.md](../../../../../delvers/world/characters/cheet.md) | character | 373 | P2 | research language in body; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/chuck-abnaz.md](../../../../../delvers/world/characters/chuck-abnaz.md) | character | 552 | P2 | episode IDs in body; emphatic action bookkeeping; unreferenced footnote; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/darmah-edstream.md](../../../../../delvers/world/characters/darmah-edstream.md) | character | 501 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/destroying-angel.md](../../../../../delvers/world/characters/destroying-angel.md) | character | 480 | P2 | episode IDs in body; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/dumbledwark-of-raisinbunch.md](../../../../../delvers/world/characters/dumbledwark-of-raisinbunch.md) | character | 911 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/enzo-vanderbuck-withers.md](../../../../../delvers/world/characters/enzo-vanderbuck-withers.md) | character | 462 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/evelyn-grinkeeper.md](../../../../../delvers/world/characters/evelyn-grinkeeper.md) | character | 7275 | P1 | episode IDs in body; research language in body; emphatic action bookkeeping; unreferenced footnote; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/gentleman-cavalier-traveler.md](../../../../../delvers/world/characters/gentleman-cavalier-traveler.md) | character | 572 | P2 | episode IDs in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/gleepo-ma.md](../../../../../delvers/world/characters/gleepo-ma.md) | character | 431 | P2 | episode IDs in body; research language in body; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/goggles-granny.md](../../../../../delvers/world/characters/goggles-granny.md) | character | 561 | P2 | episode IDs in body; research language in body; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/khalazar.md](../../../../../delvers/world/characters/khalazar.md) | character | 2232 | P1 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/koh-spiros.md](../../../../../delvers/world/characters/koh-spiros.md) | character | 7981 | P1 | episode IDs in body; research language in body; emphatic action bookkeeping; unreferenced footnote; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/krandal-splenderbelt.md](../../../../../delvers/world/characters/krandal-splenderbelt.md) | character | 7821 | P1 | episode IDs in body; research language in body; emphatic action bookkeeping; unreferenced footnote; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/marek-gideon.md](../../../../../delvers/world/characters/marek-gideon.md) | character | 475 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/margaret-dupayton.md](../../../../../delvers/world/characters/margaret-dupayton.md) | character | 632 | P2 | episode IDs in body; emphatic action bookkeeping; unreferenced footnote; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/marsh.md](../../../../../delvers/world/characters/marsh.md) | character | 714 | P2 | episode IDs in body; research language in body; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/masked-mage.md](../../../../../delvers/world/characters/masked-mage.md) | character | 255 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/nopa-ropa.md](../../../../../delvers/world/characters/nopa-ropa.md) | character | 542 | P2 | episode IDs in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/penelope-spiros.md](../../../../../delvers/world/characters/penelope-spiros.md) | character | 418 | P2 | episode IDs in body; research language in body; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/princess-hissia.md](../../../../../delvers/world/characters/princess-hissia.md) | character | 804 | P2 | episode IDs in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/radiant-lance.md](../../../../../delvers/world/characters/radiant-lance.md) | character | 393 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/shaolin-nym.md](../../../../../delvers/world/characters/shaolin-nym.md) | character | 321 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/shrugs-manaspoon.md](../../../../../delvers/world/characters/shrugs-manaspoon.md) | character | 535 | P2 | episode IDs in body; research language in body; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/skoogie.md](../../../../../delvers/world/characters/skoogie.md) | character | 398 | P2 | episode IDs in body; research language in body; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/the-great-daufante.md](../../../../../delvers/world/characters/the-great-daufante.md) | character | 502 | P2 | final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/characters/veggie-sticks.md](../../../../../delvers/world/characters/veggie-sticks.md) | character | 652 | P2 | episode IDs in body; emphatic action bookkeeping; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/CHARACTERS.md](../../../../../delvers/world/CHARACTERS.md) | navigation | 426 | P1 | No selected structural flag; reconcile current route and descriptions; retain canonical targets |
| [delvers/world/CHRONOLOGY.md](../../../../../delvers/world/CHRONOLOGY.md) | chronology | 2117 | P2 | No selected structural flag; retain source-keyed form; reconcile sequence and knowledge |
| [delvers/world/CONSISTENCY_LEDGER.md](../../../../../delvers/world/CONSISTENCY_LEDGER.md) | ledger | 1327 | P2 | No selected structural flag; retain issue register; distinguish resolved outcomes and open verification |
| [delvers/world/creatures/all-rat-cranium-congregation.md](../../../../../delvers/world/creatures/all-rat-cranium-congregation.md) | creature | 313 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/creatures/flameskull.md](../../../../../delvers/world/creatures/flameskull.md) | creature | 360 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/creatures/gricks.md](../../../../../delvers/world/creatures/gricks.md) | creature | 358 | P2 | episode IDs in body; emphatic action bookkeeping; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/creatures/hook-horrors.md](../../../../../delvers/world/creatures/hook-horrors.md) | creature | 407 | P2 | episode IDs in body; emphatic action bookkeeping; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/creatures/noble-hollow-roper.md](../../../../../delvers/world/creatures/noble-hollow-roper.md) | creature | 365 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/creatures/skeletal-bat-balcony.md](../../../../../delvers/world/creatures/skeletal-bat-balcony.md) | creature | 372 | P2 | episode IDs in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/CREATURES_AND_MONSTERS.md](../../../../../delvers/world/CREATURES_AND_MONSTERS.md) | navigation | 21 | P1 | No selected structural flag; reconcile current route and descriptions; retain canonical targets |
| [delvers/world/items/bag-of-hammer-holding.md](../../../../../delvers/world/items/bag-of-hammer-holding.md) | item | 225 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/chance-lantern.md](../../../../../delvers/world/items/chance-lantern.md) | item | 292 | P2 | episode IDs in body; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/deck-of-many-things.md](../../../../../delvers/world/items/deck-of-many-things.md) | item | 249 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/devotees-censer.md](../../../../../delvers/world/items/devotees-censer.md) | item | 272 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/dragon-slayer-longsword.md](../../../../../delvers/world/items/dragon-slayer-longsword.md) | item | 485 | P2 | episode IDs in body; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/dried-heart-jar.md](../../../../../delvers/world/items/dried-heart-jar.md) | item | 409 | P2 | episode IDs in body; research language in body; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/drift-globe.md](../../../../../delvers/world/items/drift-globe.md) | item | 268 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/friendship-ribbon.md](../../../../../delvers/world/items/friendship-ribbon.md) | item | 481 | P2 | episode IDs in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/goat-of-travail.md](../../../../../delvers/world/items/goat-of-travail.md) | item | 349 | P2 | episode IDs in body; unreferenced footnote; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/hereditary-drone.md](../../../../../delvers/world/items/hereditary-drone.md) | item | 481 | P1 | episode IDs in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/horn-of-blasting.md](../../../../../delvers/world/items/horn-of-blasting.md) | item | 300 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/khalazar-red-crystal.md](../../../../../delvers/world/items/khalazar-red-crystal.md) | item | 358 | P2 | episode IDs in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/khalazar-sensory-amulet.md](../../../../../delvers/world/items/khalazar-sensory-amulet.md) | item | 398 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; unreferenced footnote; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/loran-radiant-armour.md](../../../../../delvers/world/items/loran-radiant-armour.md) | item | 286 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/ring-of-protection.md](../../../../../delvers/world/items/ring-of-protection.md) | item | 262 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/runic-sword-hilt.md](../../../../../delvers/world/items/runic-sword-hilt.md) | item | 785 | P2 | episode IDs in body; emphatic action bookkeeping; unreferenced footnote; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/stolen-warlocks-tome.md](../../../../../delvers/world/items/stolen-warlocks-tome.md) | item | 227 | P2 | episode IDs in body; research language in body; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/three-urns-triangle-gate.md](../../../../../delvers/world/items/three-urns-triangle-gate.md) | item | 1111 | P1 | episode IDs in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/vestal-diamond-heart-handle.md](../../../../../delvers/world/items/vestal-diamond-heart-handle.md) | item | 282 | P2 | episode IDs in body; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/items/wand-of-secrets-and-geared-disc.md](../../../../../delvers/world/items/wand-of-secrets-and-geared-disc.md) | item | 537 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/black-basilica.md](../../../../../delvers/world/places/black-basilica.md) | place | 678 | P2 | episode IDs in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/black-slime-key-chamber.md](../../../../../delvers/world/places/black-slime-key-chamber.md) | place | 767 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/broscale-manor.md](../../../../../delvers/world/places/broscale-manor.md) | place | 504 | P2 | episode IDs in body; research language in body; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/chath-peak.md](../../../../../delvers/world/places/chath-peak.md) | place | 721 | P2 | episode IDs in body; research language in body; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/dawnless-dunes-pyramid.md](../../../../../delvers/world/places/dawnless-dunes-pyramid.md) | place | 1081 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/deep-winds-spa.md](../../../../../delvers/world/places/deep-winds-spa.md) | place | 1184 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/delvers-guild.md](../../../../../delvers/world/places/delvers-guild.md) | place | 2515 | P1 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/dungeon-guild-academy.md](../../../../../delvers/world/places/dungeon-guild-academy.md) | place | 502 | P2 | episode IDs in body; research language in body; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/farm-cave.md](../../../../../delvers/world/places/farm-cave.md) | place | 227 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/gemholm.md](../../../../../delvers/world/places/gemholm.md) | place | 1112 | P2 | episode IDs in body; research language in body; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/governors-hall.md](../../../../../delvers/world/places/governors-hall.md) | place | 593 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/grick-sinkhole.md](../../../../../delvers/world/places/grick-sinkhole.md) | place | 538 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/guild-public-reckoning-s3e10.md](../../../../../delvers/world/places/guild-public-reckoning-s3e10.md) | place | 467 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; review event classification and guild overlap; preserve slug until link plan exists |
| [delvers/world/places/hooper-estate.md](../../../../../delvers/world/places/hooper-estate.md) | place | 438 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/kuo-toa-lakeshore-village.md](../../../../../delvers/world/places/kuo-toa-lakeshore-village.md) | place | 720 | P2 | episode IDs in body; research language in body; unreferenced footnote; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/minotaur-mesa-bone-crypt.md](../../../../../delvers/world/places/minotaur-mesa-bone-crypt.md) | place | 399 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/noble-hollow.md](../../../../../delvers/world/places/noble-hollow.md) | place | 452 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/potato-grove.md](../../../../../delvers/world/places/potato-grove.md) | place | 1721 | P2 | episode IDs in body; emphatic action bookkeeping; unreferenced footnote; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/right-stair-grick-urn-complex.md](../../../../../delvers/world/places/right-stair-grick-urn-complex.md) | place | 619 | P2 | episode IDs in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/skull-keep.md](../../../../../delvers/world/places/skull-keep.md) | place | 602 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/snake-island.md](../../../../../delvers/world/places/snake-island.md) | place | 657 | P2 | episode IDs in body; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/southwestern-town-well.md](../../../../../delvers/world/places/southwestern-town-well.md) | place | 491 | P2 | No selected structural flag; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/splenderbelt-farm-delvers-tower.md](../../../../../delvers/world/places/splenderbelt-farm-delvers-tower.md) | place | 489 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/submerged-lake-ruins.md](../../../../../delvers/world/places/submerged-lake-ruins.md) | place | 717 | P2 | unreferenced footnote; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/temple-of-pelor.md](../../../../../delvers/world/places/temple-of-pelor.md) | place | 798 | P2 | episode IDs in body; unreferenced footnote; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/triangle-gate-catacombs.md](../../../../../delvers/world/places/triangle-gate-catacombs.md) | place | 1283 | P2 | episode IDs in body; research language in body; emphatic action bookkeeping; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/places/withers-estate.md](../../../../../delvers/world/places/withers-estate.md) | place | 1110 | P2 | episode IDs in body; emphatic action bookkeeping; unreferenced footnote; final status heading needs review; subject-focused chronological rewrite; verify last direct observation |
| [delvers/world/PLACES.md](../../../../../delvers/world/PLACES.md) | navigation | 272 | P1 | No selected structural flag; reconcile current route and descriptions; retain canonical targets |
| [delvers/world/README.md](../../../../../delvers/world/README.md) | navigation | 735 | P1 | No selected structural flag; reconcile current route and descriptions; retain canonical targets |
| [delvers/world/WORLD.md](../../../../../delvers/world/WORLD.md) | setting | 3392 | P2 | episode IDs in body; unreferenced footnote; subject-first setting synthesis with attributed accounts |

## Acceptance tracking

All baseline rows start **inventoried**. Record subsequent archives, changes, validation and acceptance in the pilot checkpoint below and dated follow-up reports; do not overwrite the pre-edit measurements. Pages without a completed checkpoint remain pending.

### First implementation checkpoint

**2026-10-26: first implementation slice structurally validated.** [Chapter maps and coverage review](../../../../../project/DELVERS_NARRATIVE_CHAPTER_MAPS.md) · [Pre-edit originals and reading copies](../../delvers-campaign-cleanup/README.md) · [Validation evidence](../../../../../project/DELVERS_CLEANUP_VALIDATION.json).

| Files / work | State and result |
| --- | --- |
| All 107 baseline files | **Inventoried**: structural findings, measurements and proposed dispositions recorded; claim-level horizons and final states remain pending |
| Campaign README, documentation plan, review queue, source inventory | **Validated**: current completion framing reconciled; historical intake checkpoints and source limits retained |
| Narrative portal | **Validated**: three primary arcs in reading order; four earlier studies explicitly historical, unchanged at existing paths |
| World portal | **Validated**: complete directory of existing subject paths; stale episode-status descriptions replaced by navigation |
| Shared documentation architecture | **Validated**: obsolete active Delvers intake paragraph replaced; unrelated guidance retained |
| Season One narrative | **Validated pilot**: archived, rewritten and checked against dossier evidence maps and all four older studies; original chapter anchors retained |
| Season Two and Three narratives | **Outlined**: proposed maps cover their archive IDs, with scene-level comparison still required; prose unchanged |
| World subject pages | **Inventoried only**: no biography, place, item, creature or setting rewrite performed |

The archived originals cover all eight pre-existing files rewritten or reframed in this slice, with exact-byte SHA-256 verification and rebased reading copies. Baseline JSON measurements remain frozen. No source SRT/MP3 was edited, no new listening or independent ASR review performed, and no commit or push made.

### Season One reading weight

Counts use the baseline Unicode-word method, excluding headings, complete footnotes and navigation. The introduction and unnumbered ending are outside the chapter range.

| Chapter | Before | Pilot |
| --- | ---: | ---: |
| 1 | 132 | 375 |
| 2 | 152 | 398 |
| 3 | 184 | 396 |
| 4 | 161 | 394 |
| 5 | 167 | 412 |
| 6 | 198 | 407 |
| 7 | 333 | 418 |
| 8 | 238 | 392 |
| Main prose including introduction/ending | 1,849 | 3,443 |

All eight pilot chapters fall within 350–450 words without adding unsupported scenes. Added space restores the grick escape/second entry, personal motives, reciprocal rescues and institutional context. This supports the planning reference for this arc; the denser later arcs still need their own compression review.

### Verification and remaining scope

Focused Markdownlint and scoped whitespace checks pass for the changed maintained Markdown. The validation JSON records relative-file/fragment checks, inbound fragment checks, pilot footnote completeness and archive hashes. Checks exclude fenced examples and do not certify remote URLs, factual accuracy or a rendered-site preview. Archived reading copies retain historical text and are not modernized to satisfy current prose rules.

A manual pilot readback checked the introduction, all eight chapters, ending and source notes against the reviewed dossiers/studies. Sensitive boundaries retained include promised versus delivered deed, offered versus accepted Snake Island job, senior guild knowledge versus party knowledge, testimony versus fact, both rescued First Sons, living prisoners and the swallowed cultist.

The 19 baseline pages flagged for unreferenced notes and other structural findings remain review leads, not automatic fixes or proof of missing facts. Later subject batches must establish actual horizons and last observations, compare possible overlap/aliases and verify final states. The next bounded narrative pass is Season Two's full coverage checklist and consolidation; the world pilot set remains Koh, the guild, the urns and one short place/creature article.

### Second implementation checkpoint — Season Two

**2026-10-26: Season Two consolidated and structurally validated.** [Coverage and acceptance report](../../../../../reports/DELVERS_SEASON_TWO_CONSOLIDATION_2026-10-26.md) · [Preserved originals](../../delvers-season-two-consolidation/README.md) · [Validation](../../../../../project/DELVERS_SEASON_TWO_VALIDATION.json).

The second arc now has eight connected chapters in the existing file and under the existing title. All 21 former substantive sections have explicit dispositions and legacy compatibility anchors. The 9,270-word pre-edit body becomes 3,435 words including its opening. Chapters 1–6 contain 382–415 words, and chapters 7–8 contain 502/504; their fuller treatment preserves the successful rescue, changed personal lives and unresolved catastrophe. No strict length ceiling displaced supported events.

Six pre-edit working copies are archived with exact original hashes and rebased reading copies. The new report accounts for condensed tactics, purchases, reference details and provenance, which remain reachable in the old narrative and dossiers. Corrected presentation includes deed timing, the larva observation and the order of Maynard's report. Source disputes, the jade count, red-shard custody and retrospective dragon victory remain qualified rather than silently resolved.

Current dispositions supersede the first checkpoint's earlier outlined status for Season Two:

| Work | Current state |
| --- | --- |
| Season One | Validated pilot retained unchanged |
| Season Two | Validated consolidation; 12 dossier scene maps/cutoffs and all 21 former narrative sections reviewed |
| Season Three | Outline only; full coverage checklist and consolidation next |
| World subjects | Structural inventory only; no subject rewrite in this slice |
| Campaign/narrative portals and chapter maps | Updated to reflect the two completed consolidations |

The 215 protected-file hashes cover world Markdown, episode dossiers, Season One/Three, earlier detailed studies and Delvers SRTs. This task edits no source media and performs no audio or new ASR review. No commit or push was performed by this task. Whole-campaign factual acceptance and a rendered-site preview are not claimed.

### Third implementation checkpoint — Season Three

**2026-10-26: Season Three consolidated and structurally validated.** [Coverage report](../../../../../reports/DELVERS_SEASON_THREE_CONSOLIDATION_2026-10-26.md) · [Paragraph ledger](../../../../../project/DELVERS_SEASON_THREE_COVERAGE.json) · [Preserved originals](../../delvers-season-three-consolidation/README.md) · [Validation](../../../../../project/DELVERS_SEASON_THREE_VALIDATION.json).

All 95 former prose paragraphs have recorded dispositions. The 13,724-word body becomes 3,802 words, including a 51-word introduction and 147-word one-year epilogue. Nine main chapters contain 367, 382, 397, 381, 387, 382, 413, 415 and 480 words. Gate entry and preparation now precede a separate finale, retaining both evacuations, the joint final blow, reciprocal healing and the minotaurs' chosen rest. The original title/path and horizon-note key remain; the formerly unreferenced horizon note is now attached to the opening.

Six current working copies were preserved with original hashes and rebased reading copies. The 215 protected-file hashes cover world Markdown, all Delvers episode dossiers, Season One/Two, earlier studies and Delvers SRTs. No world article, earlier narrative, episode dossier or source media was rewritten in this slice. No audio/new ASR review, original handout inspection, naming resolution or issue closure is claimed. No commit or push was performed by this task.

Current dispositions supersede the earlier outlined status for Season Three:

| Work | Current state |
| --- | --- |
| All three primary narratives | Preserved, consolidated and structurally validated in bounded checkpoints |
| Season Three finale/epilogue | Actual defeat, rescues and completed year retained; invitation remains future and letter unopened |
| World subjects | Structural inventory only; domain-specific pilots next |
| Claim-level source verification | Existing dossier limits remain; unresolved listening/source-identity questions stay open |

Proceed with Koh, the guild, the three urns and one short place/creature pilot before broader world rollout. Functional chronology, ledger and specialist registers retain their evidence functions. Full world acceptance and a rendered-site preview remain pending.

### Fourth implementation checkpoint — World pilots

**2026-10-26: Four world pilots migrated and structurally validated.** [Subject/coverage report](../../../../../reports/DELVERS_WORLD_PILOTS_2026-10-26.md) · [Section ledger](../../../../../project/DELVERS_WORLD_PILOT_COVERAGE.json) · [Pre-edit archive](../../delvers-world-pilots/README.md) · [Validation](../../../../../project/DELVERS_WORLD_PILOT_VALIDATION.json).

| Subject | Current disposition | Main prose before → after |
| --- | --- | ---: |
| Koh | Character-focused Introduction, three chronological arcs, abilities/limits and Current status; separate commentary in notes | 7,981 → 965 |
| Delvers guild | Institutional history under existing place path; practical leadership versus legal uncertainty distinguished | 2,515 → 799 |
| Three urns | Collective artifact account; observed/claimed contents, custody, actual uses and untracked empty vessels | 1,111 → 468 |
| Skeletal bat | Individual creature appearance, pursuit and solo defeat; no species-wide or rider identification | 372 → 199 |

Koh's substantive arcs contain 220, 256 and 270 words. All four ordinary subject pages end in Current status and retain source horizons in notes. All 73 former heading/subsection anchors map to a new section or source note; exact historical recaps and tables remain archived. No slugs, canonical identities or source files were changed.

Eight original working copies and rebased reading copies are preserved. One inherited September bonus link in Koh's reading copy is transparently corrected in the archive manifest; its exact original bytes remain unchanged. A total of 213 protected-file hashes covers other world Markdown, all episode dossiers, all narrative files, Delvers SRTs and the frozen initial baseline. No new audio, SRT interpretation, private-source review, naming decision or source-question closure occurred. No commit or push was performed by this task.

The character/institution/artifact/creature pilots meet their bounded domain contracts; this supersedes their earlier inventoried-only status. Other subject pages remain pending. Next migrate Evelyn and Krandal, then connected family/mentor and guild subjects in small batches. Resolve event/place and reasoning-creature taxonomy only after examining each subject and inbound-link consequences. Full world acceptance and a rendered-site preview are not claimed.

### Fifth implementation checkpoint — Evelyn and Krandal

**2026-10-26: Two core biographies migrated and structurally validated.** [Character report](../../../../../reports/DELVERS_EVELYN_KRANDAL_2026-10-26.md) · [Section ledger](../../../../../project/DELVERS_EVELYN_KRANDAL_COVERAGE.json) · [Pre-edit archive](../../delvers-evelyn-krandal/README.md) · [Validation](../../../../../project/DELVERS_EVELYN_KRANDAL_VALIDATION.json).

| Subject | Current disposition | Main prose before → after |
| --- | --- | ---: |
| Evelyn | Introduction, three character arcs, abilities/bonds and Current status; private knowledge, inconsistent mercy and final invitation distinguished | 7,275 → 938 |
| Krandal | Introduction, three character arcs, abilities/care and Current status; doubt, neglected obligations, actual repair and surviving cleric/farmer retained | 7,821 → 966 |

The substantive arcs contain 238/256/249 words for Evelyn and 245/260/262 for Krandal. All 84 old headings have recorded dispositions and preserved targets. Six exact working-copy originals and rebased reading copies are archived. Two inherited September bonus links are corrected only in reading copies and new notes, with explicit manifest exceptions. All 215 protected-file hashes match, covering other world pages, all episode dossiers, all narrative files, Delvers SRTs and the frozen baseline.

This completes the core-PC subject batch within the report's evidence limits, superseding these two pages' inventoried-only status. No source media, earlier narrative, other subject page or historical baseline was changed. No new listening/ASR interpretation, private-source review, identity resolution or central issue closure occurred. No commit or push was performed by this task.

Next examine Margaret and the Traveler, then Nopa Ropa and Hissia, before continuing connected guild and domain batches. Other world subjects and final campaign integration remain pending; this checkpoint does not certify the whole directory.

### Sixth implementation checkpoint — Margaret and the Traveler

**2026-10-26: Two supporting biographies migrated and structurally validated.** [Character report](../../../../../reports/DELVERS_MARGARET_TRAVELER_2026-10-26.md) · [Coverage ledger](../../../../../project/DELVERS_MARGARET_TRAVELER_COVERAGE.json) · [Pre-edit archive](../../delvers-margaret-traveler/README.md) · [Validation](../../../../../project/DELVERS_MARGARET_TRAVELER_VALIDATION.json).

| Subject | Current disposition | Main prose before → after |
| --- | --- | ---: |
| Margaret | Chronological invention, cover, friendship and trusted correspondence; last direct role distinguished from later requests and unknown epilogue | 632 → 490 |
| Traveler | Introduction, Ball relationship/defense, actual departure, private curse lead and final unresolved invitation | 572 → 428 |

All 12 former headings remain reachable, with two unheaded identity/illustration blocks also accounted for. Six exact working-copy originals and equivalent rebased reading copies are archived; no reading-copy target corrections were needed. The 218 protected hashes cover 215 campaign files and three pre-existing changed paths outside this batch. The living manifest's prior working-copy changes were preserved before this append.

The earlier Margaret Ball and Traveler departure cutoffs are superseded by later dossier evidence, while their own last appearances remain distinct from the campaign's ending. No Margaret-specific finale, confirmed Wildfire sighting, fully heard confession, independently identified pamphlet distributor, freed Traveler, performed wedding or new identity is inferred. Relevant dossier mentions were searched through all 37 campaign entries, with selected passages read; no new ASR/audio or original visual-source review occurred. No source issue was closed, and no commit or push was performed by this task.

Next examine Nopa Ropa and Hissia as a linked relationship/rescue batch, followed by connected guild subjects. Remaining ordinary world pages and final campaign integration are pending; chronology and evidence registers keep their functions.

### Seventh implementation checkpoint — Nopa Ropa and Hissia

**2026-10-26: Two linked search/rescue biographies migrated and structurally validated.** [Character report](../../../../../reports/DELVERS_NOPA_HISSIA_2026-10-26.md) · [Coverage ledger](../../../../../project/DELVERS_NOPA_HISSIA_COVERAGE.json) · [Pre-edit archive](../../delvers-nopa-hissia/README.md) · [Validation](../../../../../project/DELVERS_NOPA_HISSIA_VALIDATION.json).

| Subject | Current disposition | Main prose before → after |
| --- | --- | ---: |
| Nopa Ropa | Introduction, third-arc service/pledge/rescue and Current status; actual conduct distinguished from rat projections and plans | 542 → 365 |
| Hissia | Introduction, Ball relationship claims, third-arc captivity/reunion and Current status; missing island history remains unresolved | 804 → 406 |

All nine former headings remain reachable, and six unheaded identity/history/visual blocks have dispositions. Six exact working-copy originals and equivalent reading copies are preserved without target corrections. The 221 protected hashes cover 215 campaign files and six prior batch artifacts. Existing control-file changes are preserved in the pre-edit archive; concurrent Wastes work is outside this batch.

Nopa's living reunion and Hissia's identification, nonlethal recovery, evacuation, awakening and kiss are completed events. Earlier uncertain sightings and reported captivity remain historically scoped. Snake Island consent/marriage, gift origins, royal succession, the cause of forbidden love and later residence remain unresolved. No snakefolk reinforcements, Nopa-forged censer, actual farm foreclosure or rat-generated worker revolt is inferred.

Relevant mentions were searched across all 37 campaign dossiers and selected source paragraphs read; no fresh ASR/audio, sheets or original visual-source review occurred. No source issue was closed, no dossier/media was changed, and no commit or push was performed by this task.

Next examine Cassius and Carrie as connected guild subjects, then continue remaining domain batches. Full-world acceptance and final campaign integration remain pending.

### Eighth implementation checkpoint — Cassius and Carrie

**2026-10-26: Two guild biographies migrated and structurally validated.** [Character report](../../../../../reports/DELVERS_CASSIUS_CARRIE_2026-10-26.md) · [Coverage ledger](../../../../../project/DELVERS_CASSIUS_CARRIE_COVERAGE.json) · [Pre-edit archive](../../delvers-cassius-carrie/README.md) · [Validation](../../../../../project/DELVERS_CASSIUS_CARRIE_VALIDATION.json).

| Subject | Current disposition | Main prose before → after |
| --- | --- | ---: |
| Cassius | Introduction, three character arcs and Current status; civic purpose, private commission, confinement and practical restoration distinguished | 1,927 → 648 |
| Carrie | Introduction, three character arcs and Current status; curiosity, experiment, consent, actual detector and discreet support retained | 1,198 → 581 |

All 24 former headings retain their targets and recorded dispositions. Six exact working-copy originals and equivalent reading copies are archived, without target corrections. All 224 protected hashes match: 215 campaign files plus nine prior character-batch artifacts. Existing control changes are preserved, and concurrent Wastes/root work remains outside this batch.

Cassius's latest physical scene is his S3E10 release/desk return, followed by the S3E11 rescue assignment; no formal acquittal or personal year-later outcome is supplied. Carrie's last direct interaction is S3E06 in her lab, while later sources refer to her detector. Neither receives an invented finale appearance. The S2E00 Academy cutaway retains its first-arc chronology. The shard's unshown return, interpretations of history, unverified genealogy, experimental limits and disputed accusations stay bounded in notes.

All 37 dossier files were searched for relevant mentions, with selected full paragraphs reviewed; no new SRT/audio, sheets or original visual-source inspection occurred. No evidence issue was closed, no source dossier/media changed, and no commit or push was performed by this task.

Next examine Wildfire and Alexandre Withers as linked patron/investigator subjects, then continue connected guild and remaining domain batches. Full-world acceptance and final campaign integration remain pending.

### Ninth implementation checkpoint — Wildfire and Alexandre Withers

**2026-10-26: Two linked patron/investigator biographies migrated and structurally validated.** [Character report](../../../../../reports/DELVERS_WILDFIRE_WITHERS_2026-10-26.md) · [Coverage ledger](../../../../../project/DELVERS_WILDFIRE_WITHERS_COVERAGE.json) · [Pre-edit archive](../../delvers-wildfire-withers/README.md) · [Validation](../../../../../project/DELVERS_WILDFIRE_WITHERS_VALIDATION.json).

| Subject | Current disposition | Main prose before → after |
| --- | --- | ---: |
| Wildfire | Introduction, three character arcs and Current status; brother, mentorship, assessment, patron defense, confrontation and actual survival distinguished | 887 → 529 |
| Alexandre Withers | Introduction, three character arcs and Current status; property claims, guarded knowledge, reported losses, incriminating response and rescue retained | 945 → 510 |

All 18 old heading targets remain reachable, with dispositions recorded. Withers's existing Current status heading now describes the latest rescue outcome rather than the obsolete burglary-only cutoff. Six exact working-copy originals and equivalent reading copies are archived without target corrections. All 227 protected hashes match: 215 campaign files and 12 prior character-batch artifacts. Existing control changes are preserved; concurrent Wastes/root work remains outside scope.

Both are found alive/apparently compelled and evacuated unconscious/stable through the first completed circle. No individual awakening, reunion, confession, judgment or year-later outcome is supplied. The reported theft-investigation hire and Withers's later Broscales/doors statement remain distinct. Wildfire's species is not changed by a generic captive grouping. Earlier missing/fall cutoffs remain historical, and the staged fire chronology is retained.

Relevant mentions were searched across all 37 dossiers and selected complete source paragraphs read; no new ASR/audio, sheets or original visual-source review occurred. No evidence issue was closed, no dossier/media changed, and no commit or push was performed by this task.

Next examine Anthela and Penelope as Koh's linked family subjects, then continue connected family, guild and domain batches. Full-world acceptance and final campaign integration remain pending.

### Tenth implementation checkpoint — Anathala and Penelope Spiros

**2026-10-26: Two family biographies migrated and structurally validated.** [Family report](../../../../../reports/DELVERS_SPIROS_FAMILY_2026-10-26.md) · [Coverage ledger](../../../../../project/DELVERS_SPIROS_FAMILY_COVERAGE.json) · [Pre-edit archive](../../delvers-spiros-family/README.md) · [Validation](../../../../../project/DELVERS_SPIROS_FAMILY_VALIDATION.json).

| Subject | Current disposition | Main prose before → after |
| --- | --- | ---: |
| Anathala/Anthela | Introduction, three chronological family arcs and Current status; coerced belief, recognition, bodily recovery, consent and continued fear distinguished | 1,392 → 551 |
| Penelope | Introduction, three brief family arcs and Current status; stories, mother's return, separate disclosure, dreams and epilogue retained | 418 → 323 |

All 13 former heading targets remain reachable, and four additional identity/provenance blocks have dispositions. Six exact working-copy originals and equivalent reading copies are archived without target corrections. All 232 protected hashes match: 215 campaign files, 15 prior batch artifacts and two bonus-provenance documents. Earlier archives and the frozen baseline remain unchanged.

The S3E01 naming direction is retained without renaming the canonical file/title or historic citations. Brief recognition differs from actual physical awakening; mother's knowledge differs from the daughter's later disclosure. Actual household events remain separate from rat projections, and the final family image does not relocate the household. Source-specific introduction age six supplements the old blanket age caution, without an inferred later age. Performer-approved hooves remain attributed design evidence, while discarded half-elf-Koh ideas and unused kidnapping routes are not made history or immunity.

Relevant mentions were searched across all 37 dossiers and selected complete paragraphs plus existing retrospective passages read. No new ASR/audio, sheets, original art or full campaign rereading occurred. No evidence issue was closed, no dossier/media changed, and no commit or push was performed by this task.

Next examine Broadside and Cheet as linked guild subjects, then continue guild and domain batches. Full-world acceptance and final campaign integration remain pending.

### Eleventh implementation checkpoint — Broadside and Cheet

**2026-10-26: Two linked guild biographies migrated and structurally validated.** [Character report](../../../../../reports/DELVERS_BROADSIDE_CHEET_2026-10-26.md) · [Coverage ledger](../../../../../project/DELVERS_BROADSIDE_CHEET_COVERAGE.json) · [Pre-edit archive](../../delvers-broadside-cheet/README.md) · [Validation](../../../../../project/DELVERS_BROADSIDE_CHEET_VALIDATION.json).

| Subject | Current disposition | Main prose before → after |
| --- | --- | ---: |
| Broadside | Introduction, three relevant arc sections and Current status; mercy, trust, continued work and sound-related fear retained | 469 → 424 |
| Cheet | Introduction, first-arc choices/judgment, brief reported reassignment and Current status; curiosity and influence remain bounded | 373 → 324 |

All nine former heading targets remain reachable, including native current-status headings now updated beyond the old first-arc cutoffs. Six exact working-copy originals and equivalent reading copies are archived without target corrections. All 235 protected hashes match: 215 campaign files, 18 prior batch artifacts and two April bonus-provenance documents. Existing working-copy control/family changes and concurrent Wastes work are preserved.

Broadside's last direct scene is S3E01 helping move furniture after hiding from the sound; Cheet's direct custody ends in S1E12, followed by Broadside's S2E06 report of Academy clerical duty and later discipline references. Neither receives an invented finale outcome. Sword return is retrospective with no fixed transfer time; physical mercy is not an independently proved psychic cure. Truth-circle testimony, guild findings, curiosity and actual free will are not collapsed into one certainty.

The first arcs carry most personal change; later brief observations/reports are not padded. Broadside's 202-word first arc was reviewed for recap and retained for its distinct mercy, redemption and trust developments. Relevant mentions were searched across all 37 dossiers, with selected complete paragraphs, existing ledger entries and the April bonus passage read. No fresh ASR/audio, sheets or original art review occurred. No evidence issue was closed, no dossier/media changed, and no commit or push was performed by this task.

Next examine Marek Gideon and Noble Hollow as a linked character/place batch, then continue connected guild and domain batches. Full-world acceptance and final campaign integration remain pending.

### Twelfth implementation checkpoint — Marek Gideon and Noble Hollow

**2026-10-26: One character and one place migrated and structurally validated.** [Subject report](../../../../../reports/DELVERS_MAREK_NOBLE_HOLLOW_2026-10-26.md) · [Coverage ledger](../../../../../project/DELVERS_MAREK_NOBLE_HOLLOW_COVERAGE.json) · [Pre-edit archive](../../delvers-marek-noble-hollow/README.md) · [Validation](../../../../../project/DELVERS_MAREK_NOBLE_HOLLOW_VALIDATION.json).

| Subject | Current disposition | Main prose before → after |
| --- | --- | ---: |
| Marek | Introduction, first-arc conduct/testimony and Current status; actual defeat and proposed trial remain distinct | 475 → 307 |
| Noble Hollow | Introduction, three landscape/use phases and Current status; collapse, actual crypt access and fertile land retained | 452 → 424 |

All ten former heading targets remain reachable. Six exact working-copy originals and equivalent reading copies are archived without target corrections. All 238 protected hashes match: 215 campaign files, 21 previous batch artifacts and two November provenance documents. Earlier archives, the frozen baseline and already modified prior artifacts are preserved; concurrent outside work remains out of scope.

Marek's later report/removal references provide no completed trial, sentence or new personal scene. Noble Hollow's old collapse is actually used as a route to the bone crypt in S3E10, and its cursed land actually regains fertility after Khalazar's defeat. That renewal does not establish a restored clearing/tree, sealed cavern, destroyed piercers or title to the entire tract. The place article explains these changes without duplicating the full encounter.

Relevant mentions were searched across all 37 campaign dossiers; selected complete source paragraphs, three related place articles and existing retrospective context were read. No new ASR/audio, original maps/handouts, sheets or art were reviewed. No evidence issue was closed, no dossier/media changed, and no commit or push was performed by this task.

Next examine Enzo Withers and Skull Keep as a linked character/place batch, then continue connected subject and domain work. Full-world acceptance and final campaign integration remain pending.

### Thirteenth implementation checkpoint — Enzo Withers and Skull Keep

**2026-10-26: One character and one place migrated and structurally validated.** [Subject report](../../../../../reports/DELVERS_ENZO_SKULL_KEEP_2026-10-26.md) · [Coverage ledger](../../../../../project/DELVERS_ENZO_SKULL_KEEP_COVERAGE.json) · [Pre-edit archive](../../delvers-enzo-skull-keep/README.md) · [Validation](../../../../../project/DELVERS_ENZO_SKULL_KEEP_VALIDATION.json).

| Subject | Current disposition | Main prose before → after |
| --- | --- | ---: |
| Enzo | Introduction, direct encounter/release wish, later-record context and Current status; claims and observed reflection remain distinct | 462 → 406 |
| Skull Keep | Introduction, household/condition changes, later investigation, geography synthesis and Current status | 602 → 427 |

All 12 former heading targets remain reachable. Six exact working-copy originals and equivalent reading copies are archived without target corrections. All 241 protected hashes match: 215 campaign files, 24 previous batch artifacts and two April provenance documents. Existing Marek/Noble Hollow working-copy control changes and earlier archives are preserved; concurrent outside work remains out of scope.

Both last direct observations remain in S1E06. Later portrait/plaque/tunneling testimony and physical arrival in the named desert do not supply another Enzo meeting or resolve his consciousness. The lake vision and rat-generated tower scene are not physical revisits. The observed upper room is distinct from the unvisited basement/alchemy lab; lake drainage does not merge the two lakes or survey every passage. No title resolution, rebuilt estate or complete family tree is invented.

Relevant mentions were searched across all 37 campaign dossiers; selected full source paragraphs, the existing flameskull article and April bonus passages were read. No new ASR/audio, original maps/handouts, sheets or art were reviewed. No evidence issue was closed, no dossier/media changed, and no commit or push was performed by this task.

Next examine Withers Estate and Broscale Manor as linked place accounts, then continue connected subject/domain work. Full-world acceptance and final campaign integration remain pending.
