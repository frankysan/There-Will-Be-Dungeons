# Delvers — source inventory

**Rechecked 2026-10-24.** The Delvers archive has **37 episode IDs** across three seasons, but now **77 SRT exports** and **38 inventoried local MP3 files** because the genuine S1E03 replacement was added alongside rather than overwriting the mislabelled older copies. File availability does not guarantee recording identity, MP3/SRT clock equality, model configuration or audio-verified accuracy.

| Season | Available archive IDs | Entries | SRT exports | Local MP3s |
| --- | --- | --- | --- | --- |
| 1 | S1E01–S1E12 | 12 | **27** | **13** |
| 2 | S2E00–S2E12 | 13 | 26 | 13 |
| 3 | S3E01–S3E12 | 12 | 24 | 12 |
| **Total** | **Three seasons** | **37** | **77** | **38** |

## Identity and evidence limits

- **2026-10-24 IDENTITY RECOVERY:** The two **uncorrected** S1E03 SRTs remain **MISLABELED S1E04**; the correctly named S1E04 pair is another copy with ads. The genuine S1E03 is now represented by **three distinct `(corrected)` exports, P/Q4/Q8**, with a separately named local MP3. [Updated audit](../../../../../reports/DELVERS_S1E03_SOURCE_IDENTITY_2026-10-24.md). Use **only corrected exports for S1E03**; older SRTs remain evidence for S1E04. All MP3 identities and seek offsets remain unlistened.
- IDs and title spelling below preserve the existing normalized source filenames. See the [archive numbering policy](../../../../../project/EPISODE_NUMBERING.md). Original publisher labels/dates were not reconciled in the initial preparation; **S1E03 (2021-01-29) and S1E04 (2021-02-01) have now been matched to the publication spreadsheet** as part of the identity audit. Keep spoken recording dates separate from publication dates.
- **S2E00 — Cassius at the Guild** is an existing archive entry **now classified by reading both complete SRT exports** as a **narrated in-universe Cassius/Carrie academy interlude, not a player session or out-of-game recap**. Intro places it during the **S1E10 kuo-toa All-Bronze mission**, and outro advertises **next week's S1E12 finale**. **Preserve E00** despite this earlier fictional chronology. [Dossier](../../../../../delvers/episodes/S2E00.md) · [report](../../../../../reports/DELVERS_S2E00_ASR_COMPARISON_2026-10-25.md).
- **P** means the filename label `parakeet.processed`; **Q** means `qwen-q8.canary-ctc.nemotron`. These are filename-derived pipeline labels, not independently verified run metadata or proof that the two exports came from identical audio bytes.
- Each audio match is `local/<archive basename>.mp3`. Audio is ignored/local-only and is not supplied by the repository links. Matching basenames and nonzero sizes establish availability, not encoding integrity, listening verification or exact ASR-input provenance.
- **S1E01–S1E12 have completed ASR-provisional Season One research** as of 2026-10-25. **S1E12 — End Friends** is the explicit season finale and owner-confirmed first-arc endpoint; the archived [S2E00 — Cassius at the Guild](../../../../../delvers/episodes/S2E00.md) has now been **classified as an in-universe cutaway before S1E12**, with **[S2E01 — Very Snakey](../../../../../delvers/episodes/S2E01.md) now researched as the played Season Two premiere** (after two missing Snake Island weeks, source-first [report](../../../../../reports/DELVERS_S2E01_ASR_COMPARISON_2026-10-25.md)); **[S2E02 — Why Palor When you Can Pay Later](../../../../../delvers/episodes/S2E02.md) is now documented** as the played Wight Wedding, [comparison](../../../../../reports/DELVERS_S2E02_ASR_COMPARISON_2026-10-25.md); **S2E03 — Pokey Stick Junior now documented** ([dossier](../../../../../delvers/episodes/S2E03.md), [ASR comparison](../../../../../reports/DELVERS_S2E03_ASR_COMPARISON_2026-10-25.md)); **next S2E04 — Cover The Faces of Maces**. The [genuine S1E03 dossier](../../../../../delvers/episodes/S1E03.md) and [P/Q4/Q8 comparison](../../../../../reports/DELVERS_S1E03_ASR_COMPARISON_2026-10-24.md) use **corrected sources only** (P–Q8 **7.39%**, P–Q4 **7.53%** disagreement). The older S1E04 analysis retains the 7.65% score for mislabelled S1E03-named *copies of S1E04*. No MP3 heard.

The premiere's original publisher title **TWBD Delvers S1E1: How Much Is Potato** and **January 11, 2021 publication date** were checked against the [publisher page](https://shows.acast.com/there-will-be-dungeons/episodes/6501086309d52c00124340d9) on 2026-10-24. The premiere publisher check is separate from the subsequent **S1E03/S1E04 spreadsheet identity correction** above; other original publisher metadata has not been comprehensively verified. Recording date and the ASR-rendered opening year remain separate, unresolved fields.

## Episode sources

Each row denotes a historical episode ID, **not unique file copies**. For S1E03, the two original SRTs remain wrong-episode duplicates; a **separate three-export corrected input set and MP3 filename** is now present. None of the MP3 content has been listened to or synchronized. Titles themselves may reveal later-season names; no story outcomes are inferred from them.

### Season 1

| Archive ID | Archive title | Parakeet | Qwen pipeline |
| --- | --- | --- | --- |
| S1E01 | How Much Is Potato | [P](../../../../../sources/Delvers%20S1E01.%20How%20Much%20Is%20Potato.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S1E01.%20How%20Much%20Is%20Potato.qwen-q8.canary-ctc.nemotron.srt) |
| S1E02 | Agreeable Meatball | [P](../../../../../sources/Delvers%20S1E02.%20Agreeable%20Meatball.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S1E02.%20Agreeable%20Meatball.qwen-q8.canary-ctc.nemotron.srt) |
| **S1E03 — RECOVERED** | Raw End Of Joke Stick | [P — genuine corrected](../../../../../sources/Delvers%20S1E03.%20Raw%20End%20Of%20Joke%20Stick%20%28corrected%29.parakeet.processed.srt) | [Q4](../../../../../sources/Delvers%20S1E03.%20Raw%20End%20Of%20Joke%20Stick%20%28corrected%29.qwen-q4.canary-ctc.nemotron.srt) · [Q8](../../../../../sources/Delvers%20S1E03.%20Raw%20End%20Of%20Joke%20Stick%20%28corrected%29.qwen-q8.canary-ctc.nemotron.srt) |
| S1E04 | Where did this dungeon come from? (plus **two mislabeled older S1E03-named sources**, see audit) | [P — actual S1E04 with ads](../../../../../sources/Delvers%20S1E04.%20Where%20did%20this%20dungeon%20come%20from.parakeet.processed.srt) | [Q — actual S1E04 with ads](../../../../../sources/Delvers%20S1E04.%20Where%20did%20this%20dungeon%20come%20from.qwen-q8.canary-ctc.nemotron.srt) |
| S1E05 | Maximum Montage | [P](../../../../../sources/Delvers%20S1E05.%20Maximum%20Montage.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S1E05.%20Maximum%20Montage.qwen-q8.canary-ctc.nemotron.srt) |
| S1E06 | The Tower | [P](../../../../../sources/Delvers%20S1E06.%20The%20Tower.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S1E06.%20The%20Tower.qwen-q8.canary-ctc.nemotron.srt) |
| S1E07 | The Well Might Be Bugged | [P](../../../../../sources/Delvers%20S1E07.%20The%20Well%20Might%20Be%20Bugged.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S1E07.%20The%20Well%20Might%20Be%20Bugged.qwen-q8.canary-ctc.nemotron.srt) |
| S1E08 | Need any help down there | [P](../../../../../sources/Delvers%20S1E08.%20Need%20any%20help%20down%20there.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S1E08.%20Need%20any%20help%20down%20there.qwen-q8.canary-ctc.nemotron.srt) |
| S1E09 | Once a Month Goat | [P](../../../../../sources/Delvers%20S1E09.%20Once%20a%20Month%20Goat.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S1E09.%20Once%20a%20Month%20Goat.qwen-q8.canary-ctc.nemotron.srt) |
| S1E10 | Fish Wizards! | [P](../../../../../sources/Delvers%20S1E10.%20Fish%20Wizards%21.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S1E10.%20Fish%20Wizards%21.qwen-q8.canary-ctc.nemotron.srt) |
| S1E11 | No More Fish | [P](../../../../../sources/Delvers%20S1E11.%20No%20More%20Fish.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S1E11.%20No%20More%20Fish.qwen-q8.canary-ctc.nemotron.srt) |
| S1E12 | End Friends | [P](../../../../../sources/Delvers%20S1E12.%20End%20Friends.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S1E12.%20End%20Friends.qwen-q8.canary-ctc.nemotron.srt) |

### Season 2

| Archive ID | Archive title | Parakeet | Qwen pipeline |
| --- | --- | --- | --- |
| S2E00 | Cassius at the Guild | [P](../../../../../sources/Delvers%20S2E00.%20Cassius%20at%20the%20Guild.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S2E00.%20Cassius%20at%20the%20Guild.qwen-q8.canary-ctc.nemotron.srt) |
| S2E01 | Very Snakey | [P](../../../../../sources/Delvers%20S2E01.%20Very%20Snakey.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S2E01.%20Very%20Snakey.qwen-q8.canary-ctc.nemotron.srt) |
| S2E02 | Why Palor When you Can Pay Later | [P](../../../../../sources/Delvers%20S2E02.%20Why%20Palor%20When%20you%20Can%20Pay%20Later.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S2E02.%20Why%20Palor%20When%20you%20Can%20Pay%20Later.qwen-q8.canary-ctc.nemotron.srt) |
| S2E03 | Pokey Stick Junior | [P](../../../../../sources/Delvers%20S2E03.%20Pokey%20Stick%20Junior.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S2E03.%20Pokey%20Stick%20Junior.qwen-q8.canary-ctc.nemotron.srt) |
| S2E04 | Cover The Faces of Maces | [P](../../../../../sources/Delvers%20S2E04.%20Cover%20The%20Faces%20of%20Maces.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S2E04.%20Cover%20The%20Faces%20of%20Maces.qwen-q8.canary-ctc.nemotron.srt) |
| S2E05 | Shut up, Fruit Loops! | [P](../../../../../sources/Delvers%20S2E05.%20Shut%20up%2C%20Fruit%20Loops%21.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S2E05.%20Shut%20up%2C%20Fruit%20Loops%21.qwen-q8.canary-ctc.nemotron.srt) |
| S2E06 | Frog Man Cometh | [P](../../../../../sources/Delvers%20S2E06.%20Frog%20Man%20Cometh.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S2E06.%20Frog%20Man%20Cometh.qwen-q8.canary-ctc.nemotron.srt) |
| S2E07 | The Devils Eggs | [P](../../../../../sources/Delvers%20S2E07.%20The%20Devils%20Eggs.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S2E07.%20The%20Devils%20Eggs.qwen-q8.canary-ctc.nemotron.srt) |
| S2E08 | Golden Potato Sword | [P](../../../../../sources/Delvers%20S2E08.%20Golden%20Potato%20Sword.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S2E08.%20Golden%20Potato%20Sword.qwen-q8.canary-ctc.nemotron.srt) |
| S2E09 | Potatopia | [P](../../../../../sources/Delvers%20S2E09.%20Potatopia.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S2E09.%20Potatopia.qwen-q8.canary-ctc.nemotron.srt) |
| S2E10 | Carrie On | [P](../../../../../sources/Delvers%20S2E10.%20Carrie%20On.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S2E10.%20Carrie%20On.qwen-q8.canary-ctc.nemotron.srt) |
| S2E11 | New High Score | [P](../../../../../sources/Delvers%20S2E11.%20New%20High%20Score.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S2E11.%20New%20High%20Score.qwen-q8.canary-ctc.nemotron.srt) |
| S2E12 | The Bell of The Ball | [P](../../../../../sources/Delvers%20S2E12.%20The%20Bell%20of%20The%20Ball.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S2E12.%20The%20Bell%20of%20The%20Ball.qwen-q8.canary-ctc.nemotron.srt) |

### Season 3

| Archive ID | Archive title | Parakeet | Qwen pipeline |
| --- | --- | --- | --- |
| S3E01 | Maximize The Yield | [P](../../../../../sources/Delvers%20S3E01.%20Maximize%20The%20Yield.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S3E01.%20Maximize%20The%20Yield.qwen-q8.canary-ctc.nemotron.srt) |
| S3E02 | Call your Mummy | [P](../../../../../sources/Delvers%20S3E02.%20Call%20your%20Mummy.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S3E02.%20Call%20your%20Mummy.qwen-q8.canary-ctc.nemotron.srt) |
| S3E03 | Thank You For The Deposit | [P](../../../../../sources/Delvers%20S3E03.%20Thank%20You%20For%20The%20Deposit.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S3E03.%20Thank%20You%20For%20The%20Deposit.qwen-q8.canary-ctc.nemotron.srt) |
| S3E04 | Take a photographical, it'll last longer. | [P](../../../../../sources/Delvers%20S3E04.%20Take%20a%20photographical%2C%20it%27ll%20last%20longer..parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S3E04.%20Take%20a%20photographical%2C%20it%27ll%20last%20longer..qwen-q8.canary-ctc.nemotron.srt) |
| S3E05 | Dungeon Goes Poof | [P](../../../../../sources/Delvers%20S3E05.%20Dungeon%20Goes%20Poof.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S3E05.%20Dungeon%20Goes%20Poof.qwen-q8.canary-ctc.nemotron.srt) |
| S3E06 | A naked man can be slippery | [P](../../../../../sources/Delvers%20S3E06.%20A%20naked%20man%20can%20be%20slippery.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S3E06.%20A%20naked%20man%20can%20be%20slippery.qwen-q8.canary-ctc.nemotron.srt) |
| S3E07 | A Shirt Full of Mayo | [P](../../../../../sources/Delvers%20S3E07.%20A%20Shirt%20Full%20of%20Mayo.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S3E07.%20A%20Shirt%20Full%20of%20Mayo.qwen-q8.canary-ctc.nemotron.srt) |
| S3E08 | I Smell a Rat Ball | [P](../../../../../sources/Delvers%20S3E08.%20I%20Smell%20a%20Rat%20Ball.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S3E08.%20I%20Smell%20a%20Rat%20Ball.qwen-q8.canary-ctc.nemotron.srt) |
| S3E09 | I Am The Natural One | [P](../../../../../sources/Delvers%20S3E09.%20I%20Am%20The%20Natural%20One.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S3E09.%20I%20Am%20The%20Natural%20One.qwen-q8.canary-ctc.nemotron.srt) |
| S3E10 | Sad in a boney kind of way | [P](../../../../../sources/Delvers%20S3E10.%20Sad%20in%20a%20boney%20kind%20of%20way.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S3E10.%20Sad%20in%20a%20boney%20kind%20of%20way.qwen-q8.canary-ctc.nemotron.srt) |
| S3E11 | There's a Bat in The Balcony | [P](../../../../../sources/Delvers%20S3E11.%20There%27s%20a%20Bat%20in%20The%20Balcony.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S3E11.%20There%27s%20a%20Bat%20in%20The%20Balcony.qwen-q8.canary-ctc.nemotron.srt) |
| S3E12 | KOA is not A-OK | [P](../../../../../sources/Delvers%20S3E12.%20KOA%20is%20not%20A-OK.parakeet.processed.srt) | [Q](../../../../../sources/Delvers%20S3E12.%20KOA%20is%20not%20A-OK.qwen-q8.canary-ctc.nemotron.srt) |

## How this inventory was checked

Direct filesystem discovery matched `sources/Delvers *.parakeet.processed.srt` and each exact-basename Qwen companion, then checked for the corresponding direct-root `local/Delvers *.mp3`. This original intake counted **74** Delvers SRTs and **37** matching MP3 basenames at that checkpoint. A further **three corrected S1E03 SRTs and one separately named corrected S1E03 MP3** were subsequently discovered (now **77** and **38**). The corrected exports were content-verified through GitHub, but their MP3 was not opened; this later source recovery supersedes the initial completeness claim.

The local checkout was on `main` at `76cb96b` with existing uncommitted E120 documentation work. This inventory describes that local state; it does not assert synchronization with GitHub or an MCP workspace. Original SRTs and audio were not edited. Recheck availability and source identity when each entry is analyzed.

## Supporting material

The existing [Discord spelling and provenance register](../../../../../reports/DISCORD_SPELLING_2026-10-21.md) assigns **Source D2, Kyle's cast-posted Dungeon Guild Guide**, to Delvers. Its prior review records written names and institutions, page locators and a private-download hash. This preparation reuses that register; it does not claim a new PDF inspection or redistribute the handout.

The register also contains a Delvers-attributed **Khalezaar** spelling lead and archived character-sheet preview leads. Their identity, episode association and historical state still need checking. A handout, preview or planning document cannot establish that a character appeared, an event occurred or a rule was used in play.

[Campaign index](../../../../../delvers/README.md) · [Documentation plan](../../../../../delvers/DOCUMENTATION_PLAN.md) · [Delvers review queue](../../../../../delvers/REVIEW_QUEUE.md)
