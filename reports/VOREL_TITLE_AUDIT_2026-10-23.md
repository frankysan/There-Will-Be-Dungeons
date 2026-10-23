# Vorel title-register audit — 2026-10-23

**Scope:** Targeted transcript search for titles missing from [Vorel's character-page register](../world/characters/vorel.md#titles-and-epithets--source-indexed-register). Local checkout, starting HEAD `b25b64a`, initially clean. This is a **title search and selected-passage comparison**, not a full-episode dossier, listening review or validation of every exploit implied by a title.

## Findings and editorial treatment

The original register had no entries for the extended self-introductions in **S1E040, S1E060 and S1E117**, or the later-season titles repeated in **The Wastes Round Up**. The character page now records those names individually, including titles absent from the final recap: **Terror of the Sands, Destroyer of Bean Juice, Owner of Charlemagne's, Leader of a Goblin Army, Soon to Be King of the Lizards, Promised Mate of Typalla**, and the uncertain **Victor of Slavetown / Destroyer of the Mines** readings.

Earlier evidence also changes the register's starting points:

- **Lizard King:** Bok Bok's address in **E006 ~00:45–00:46** precedes Vorel's **E026 ~00:54** statement that he will declare himself king, his direct answer to a title inquiry in **E028 ~02:11**, and the already-recorded E036 declaration. Preserve these different kinds of use.
- **King of the Deserts:** Bertrand greets Vorel this way in **E026 ~02:42:30–02:42:45**; Vorel accepts it as a fine title.
- **Hero of the Waste(s):** Vorel proposes the collective **Heroes of the Wastes** at the end of **E026**, and uses the singular personal style in **E040**. The group label does not make every companion endorse it immediately.
- **Hill Guard of Dusthill:** E001 provides the group recruitment context; the longer personal style is explicit in the E060 recital. The naming of an institution at an earlier cue is not itself Vorel receiving a title.
- **Keeper of Groxl:** Named by Vorel in **E077 ~03:18**, before the E117 list. Preserve the ASR aliases `grojil` / `Grogil` while using the established Eye of Groxl identity.
- **M-sports titles:** E086 has Lohar's advertising use of **M-sports Fighting Champion**. E087 has the referee's announcement and trophy wording **Sigil M-sports Champion / Big Time Smackaroo** (last phrase ASR-provisional). E117's **Gold Medalist of Smackems** is a further self-recital style, not a verbatim replacement for that trophy wording.
- **Greatest of the Time Vorels:** The longer boast is already explicit in **S2E02 ~01:53:30**, before S2E03–S2E04 and later abbreviated lists.
- **Entomber of the Maggot Lord:** **S2E12 ~01:31:10–01:31:45** contains Kyle constructing the title, with cast assistance; **S3E03** contains the complete self-recital. Do not conceal the earlier fragmented construction or present its ASR as an exact quotation.
- **The Patient:** Self-added in **S3E13 ~01:38:25**, repeated around **01:51:56**; the ASR has `patients` / `patience`, while the roundup gives the clearer title form.
- **Friend:** Stanley explicitly offers this title in **S3E18 ~02:09:25–02:09:40**, and Vorel accepts/extends it as **Friend Till the End of His Days**. It is not merely a retrospective addition in the roundup.

The page keeps **later-season title evidence separate from its narrative coverage through E106**. E117 and the roundup are evidence of titles being recited at those points; neither justifies backdating adoption to the underlying exploit. The roundup itself is **out-of-game retrospective material**, despite its `S3E019` archive filename.

## Search method and limits

The local `sources/` inventory contained **501 SRT exports**. The relevant search scope was **341 Wastes-labelled exports plus 76 bonus-labelled exports (417 files)**. Other campaigns were not treated as Vorel's continuity. The Wastes inventory includes supplemental/alternate copies and additional ASR variants; file counts are not counts of independent recordings.

Searches joined complete cue text in recording order, removing parenthesized speaker decorations only in a temporary search view so phrases split across cues could match. Searches covered title/epithet language, introductions, king/fang/champion references, naming variants and distinctive fragments from the final recital. The original SRTs were read without edits. Contextual comparisons used the paired **`.parakeet.processed.srt`** and **`.qwen-q8.canary-ctc.nemotron.srt`** exports listed below. These are filename labels, not verified model-run metadata.

The reviewed source windows establish **earliest located naming**, not guaranteed first occurrence across every possible ASR spelling. Generic matches such as `hill guard`, `patient`, `entombed` and `champion` were checked in context rather than automatically assigned to Vorel. Searches are not full-recording reading or audio verification. Agreement between two exports does not prove exact spoken words, speaker identity or orthography.

## Wording that remains unresolved

| Source | Preserved readings and decision |
| --- | --- |
| S1E040 ~01:34:56; S1E060 ~02:12:25 | **Bloody Cage / Rusty Cage:** retain both named variants; do not silently harmonize the arena name. |
| S1E040 ~01:36:58–01:37:06 | **Slayer of Tylander:** Parakeet splits `slayer` into a separate speaker cue and has `Thailand`; Qwen keeps `Slayer of Tylander` together. Attribution follows the ongoing Vorel speech, pending audio. |
| S1E040 ~01:36:58–01:37:06 | **Victor of Slavetown / Destroyer of the Mines** are candidates: Parakeet `Victor or slave town destroyer of the mines`; Qwen `Victor of Flame. Down, destroyer of the minds`. Do not certify the reconstructed nouns. |
| S1E040 ~02:03; S1E060 ~02:12:29 | E040 has `awesomeist of sapphire` / `acidist of sapphire`; the clearer **Arsonist of the Sapphire** recital is in E060. E040 is a candidate earlier use, not verified exact wording. |
| S1E040 / S1E060 / S1E117 | **Tylander / Thylander / tailander**, **Blunk / blunt / blancoliver / Blank Oliver**, and **Typala / Taipala** remain traceable recognition variants. Later **Destroyer of Thylander and His Beast(s)** extends earlier wording; it does not erase **Slayer of Tylander**. |
| S1E060 ~02:12:36; S1E117 ~02:07:46 | **Boon of Fuxi:** E060 `boon of fushi` / `Boone of Fushi`; E117 Qwen merges it as `Hunafushi`. Fuxi is the established reference spelling, not a transcription correction to the originals. |
| S1E087 ~02:10:34 | Trophy **Big Time Smackaroo / Smackeru**, distinct from E117 **Gold Medalist of Smackems / smack ems**. Preserve the different named forms until listening clarifies them. |
| S1E117 ~02:08:29; roundup ~01:16:30 | **Conqueror of the Locked Air Vacuum Pirates / Airlock Vacuum Pirates**: E117 exports both give `locked air`; the roundup has `airlok` / `Airlock`. Exact phrase and segmentation need audio. |
| S1E124 ~00:28:31 | **Butcher of the Barosaurus / barrow saurus** and **Deceiver of the Cheater Diontalus / Cheetah, Dian Talos**: reference labels remain provisional, not verified creature spelling or exact epithet. |
| S3E09 ~00:06:15; roundup ~01:16:52 | **Entomber / Intumere / Intumbr**: retain the recognition conflict; S2E12 supplies the earlier title-construction context. |
| S3E08 ~02:24:37; roundup ~01:16:58 | **Savior of the Universe** is explicit during play and in S3E09. The roundup's Parakeet `survivor or savior` is ambiguous; do not promote Survivor of the Universe as a separately confirmed title. |
| Roundup ~01:17:04–01:17:11 | **The Shieldless Dasher:** both exports run the words together without a clear secure boundary between titles. Preserve the phrase and flag segmentation rather than assert two distinct titles. |

These are bounded listening tasks at the listed windows. **No audio was checked**, and no full-export disagreement metric was calculated for this title search.

## Attribution checks and exclusions

- **God Killer** in S3E09 belongs to **Groxl**; he calls Vorel **Slayer of the God Killer**. E061's God Killer discussion likewise does not give that unqualified title to Vorel.
- **Defender of Earth** in E106 is the **Principal's** self-description. Vorel's own located use is S3E11; the E106 match must not backdate it.
- **Lord of the Goblin Tribes** in E026 is Vorel's proposed future title for **Bok Bok**, not Vorel.
- **Proud mount of Metal Mandy** in E040 ~01:21:45 is Vorel's boast within the **Craigfar** disguise exchange. It is retained here as temporary persona wording, rather than treated as a lasting Vorel honor.
- **Kicker of One's Own Penis**, **Licker of Slow Peters/Froghemoths**, **Rider of the Time Barf** and **Current Carrier of Peeled Vegetables in My Pants** at E117 ~02:15:40–02:16:25 are joking title suggestions for **Nash**, not additional Vorel titles.
- **Keeper of the Showtime** at the end of E117 is host/show banter; it is not Vorel's title. Nearby finder/title jokes were not automatically assigned to him.
- **Mawstorm** and **Fang Fate Five** name other subjects. **Creator of the Fate Five** does describe Vorel and is therefore included.
- Existing **clan pledge**, **Door Authority accusation**, uncertain **song lyric** and **Rex** entries remain with their original qualifications; none was converted into a universal office.

## Source windows and export inventory

Times are recording-clock offsets in the named exports. Each link identifies the exact local source filename; cue ranges refer to that export. Windows are selected title passages, not claims of whole-episode review.

| Source | Selected windows | Parakeet export and cue ranges | Qwen export and cue ranges |
| --- | --- | --- | --- |
| S1E001 | 01:14:00–01:15:40 | [SRT](../sources/The%20Wastes%20S1E001.%20The%20Campaign%20Begins%21.parakeet.processed.srt) 1920–1954 | [SRT](../sources/The%20Wastes%20S1E001.%20The%20Campaign%20Begins%21.qwen-q8.canary-ctc.nemotron.srt) 2348–2392 |
| S1E006 | 00:44:40–00:46:30 | [SRT](../sources/The%20Wastes%20S1E006.%20Start%20your%20engines%21.parakeet.processed.srt) 1045–1077 | [SRT](../sources/The%20Wastes%20S1E006.%20Start%20your%20engines%21.qwen-q8.canary-ctc.nemotron.srt) 1289–1328 |
| S1E007 | 00:55:30–00:56:30 | [SRT](../sources/The%20Wastes%20S1E007.%20Bok%20Bok%20Keeping%20It%20Fresh.parakeet.processed.srt) 1337–1362 | [SRT](../sources/The%20Wastes%20S1E007.%20Bok%20Bok%20Keeping%20It%20Fresh.qwen-q8.canary-ctc.nemotron.srt) 1593–1623 |
| S1E026 | 00:18:30–00:19:10; 00:53:55–00:54:35; 02:42:20–02:43:05; 03:02:00–03:04:50 | [SRT](../sources/The%20Wastes%20S1E026.%20The%20Hunt.parakeet.processed.srt) 332–344; 897–904; 2667–2677; 2958–3005 | [SRT](../sources/The%20Wastes%20S1E026.%20The%20Hunt.qwen-q8.canary-ctc.nemotron.srt) 513–534; 1417–1429; 4341–4357; 4778–4852 |
| S1E028 | 02:10:30–02:11:30 | [SRT](../sources/The%20Wastes%20S1E028.%20It%27s%20A%20Cat%20Person%21.parakeet.processed.srt) 2215–2230 | [SRT](../sources/The%20Wastes%20S1E028.%20It%27s%20A%20Cat%20Person%21.qwen-q8.canary-ctc.nemotron.srt) 3749–3778 |
| S1E040 | 01:21:30–01:22:15; 01:34:20–01:35:25; 01:36:45–01:37:20; 01:42:50–01:43:30; 02:02:40–02:03:30; 02:04:40–02:05:30; 02:24:55–02:25:35 | [SRT](../sources/The%20Wastes%20S1E040.%20The%20Tale%20of%20The%20Two%20Phillips.parakeet.processed.srt) 1360–1371; 1562–1576; 1599–1608; 1694–1704; 2042–2058; 2085–2097; 2412–2424 | [SRT](../sources/The%20Wastes%20S1E040.%20The%20Tale%20of%20The%20Two%20Phillips.qwen-q8.canary-ctc.nemotron.srt) 2253–2271; 2602–2624; 2658–2674; 2812–2827; 3392–3421; 3468–3492; 4073–4098 |
| S1E060 | 02:11:40–02:13:15 | [SRT](../sources/The%20Wastes%20S1E060.%20What%27s%20for%20dinner.parakeet.processed.srt) 1935–1951 | [SRT](../sources/The%20Wastes%20S1E060.%20What%27s%20for%20dinner.qwen-q8.canary-ctc.nemotron.srt) 2913–2935 |
| S1E077 | 03:17:40–03:18:35 | [SRT](../sources/The%20Wastes%20S1E077.%20The%20Wall%20Nash.parakeet.processed.srt) 2898–2907 | [SRT](../sources/The%20Wastes%20S1E077.%20The%20Wall%20Nash.qwen-q8.canary-ctc.nemotron.srt) 4841–4859 |
| S1E086 | 02:40:20–02:40:50 | [SRT](../sources/The%20Wastes%20S1E086.%20Don%27t%20be%20such%20a%20Berk.parakeet.processed.srt) 2572–2579 | [SRT](../sources/The%20Wastes%20S1E086.%20Don%27t%20be%20such%20a%20Berk.qwen-q8.canary-ctc.nemotron.srt) 4369–4380 |
| S1E087 | 02:09:35–02:10:55 | [SRT](../sources/The%20Wastes%20S1E087.%20We%20have%20a%20winner.parakeet.processed.srt) 2117–2138 | [SRT](../sources/The%20Wastes%20S1E087.%20We%20have%20a%20winner.qwen-q8.canary-ctc.nemotron.srt) 3369–3400 |
| S1E117 | 02:06:50–02:09:35; 02:15:30–02:16:25 | [SRT](../sources/The%20Wastes%20S1E117.%20The%20Fireside%20Stories.parakeet.processed.srt) 1753–1784; 1846–1862 | [SRT](../sources/The%20Wastes%20S1E117.%20The%20Fireside%20Stories.qwen-q8.canary-ctc.nemotron.srt) 2810–2860; 2966–2997 |
| S1E124 | 00:27:50–00:28:50 | [SRT](../sources/The%20Wastes%20S1E124.%20Bow%20To%20The%20Fish%20Bird.parakeet.processed.srt) 426–439 | [SRT](../sources/The%20Wastes%20S1E124.%20Bow%20To%20The%20Fish%20Bird.qwen-q8.canary-ctc.nemotron.srt) 659–683 |
| S2E01 | 00:42:30–00:42:55 | [SRT](../sources/The%20Wastes%20S2E01.%20Nash%20We%27ll%20Get%20One%20From%20Space..parakeet.processed.srt) 632–639 | [SRT](../sources/The%20Wastes%20S2E01.%20Nash%20We%27ll%20Get%20One%20From%20Space..qwen-q8.canary-ctc.nemotron.srt) 968–977 |
| S2E02 | 01:53:15–01:53:50 | [SRT](../sources/The%20Wastes%20S2E02.%20This%20Is%20Space%2C%20It%27s%20Very%20Very%20Big%21.parakeet.processed.srt) 1677–1685 | [SRT](../sources/The%20Wastes%20S2E02.%20This%20Is%20Space%2C%20It%27s%20Very%20Very%20Big%21.qwen-q8.canary-ctc.nemotron.srt) 2646–2658 |
| S2E03 | 00:19:45–00:20:15 | [SRT](../sources/The%20Wastes%20S2E03.%20Enemy%20Mine.parakeet.processed.srt) 308–316 | [SRT](../sources/The%20Wastes%20S2E03.%20Enemy%20Mine.qwen-q8.canary-ctc.nemotron.srt) 487–500 |
| S2E12 | 01:31:00–01:32:20 | [SRT](../sources/The%20Wastes%20S2E12.%20Dust%20to%20Dust.parakeet.processed.srt) 1355–1371 | [SRT](../sources/The%20Wastes%20S2E12.%20Dust%20to%20Dust.qwen-q8.canary-ctc.nemotron.srt) 2402–2433 |
| S3E03 | 02:11:15–02:12:00 | [SRT](../sources/The%20Wastes%20S3E03.%20Hammer%20Giggle.parakeet.processed.srt) 2083–2091 | [SRT](../sources/The%20Wastes%20S3E03.%20Hammer%20Giggle.qwen-q8.canary-ctc.nemotron.srt) 3541–3552 |
| S3E08 | 02:24:30–02:25:15 | [SRT](../sources/The%20Wastes%20S3E08.%20Electric%20Lizard.parakeet.processed.srt) 2351–2364 | [SRT](../sources/The%20Wastes%20S3E08.%20Electric%20Lizard.qwen-q8.canary-ctc.nemotron.srt) 4011–4035 |
| S3E09 | 00:05:35–00:07:15 | [SRT](../sources/The%20Wastes%20S3E09.%20Tank%20Boy.parakeet.processed.srt) 67–85 | [SRT](../sources/The%20Wastes%20S3E09.%20Tank%20Boy.qwen-q8.canary-ctc.nemotron.srt) 94–125 |
| S3E11 | 02:23:35–02:24:25 | [SRT](../sources/The%20Wastes%20S3E11.%20Two%20Wrongs.parakeet.processed.srt) 1853–1861 | [SRT](../sources/The%20Wastes%20S3E11.%20Two%20Wrongs.qwen-q8.canary-ctc.nemotron.srt) 3042–3053 |
| S3E13 | 01:38:00–01:38:55; 01:51:45–01:52:20 | [SRT](../sources/The%20Wastes%20S3E13.%20You%20stole%20my%20heart.parakeet.processed.srt) 1465–1474; 1661–1670 | [SRT](../sources/The%20Wastes%20S3E13.%20You%20stole%20my%20heart.qwen-q8.canary-ctc.nemotron.srt) 2413–2433; 2765–2780 |
| S3E18 | 02:09:05–02:09:50 | [SRT](../sources/The%20Wastes%20S3E18.%20Chrome%2C%20Chrome%20on%20The%20Range.parakeet.processed.srt) 1976–1984 | [SRT](../sources/The%20Wastes%20S3E18.%20Chrome%2C%20Chrome%20on%20The%20Range.qwen-q8.canary-ctc.nemotron.srt) 3163–3174 |
| S3E019 | 01:14:50–01:17:50 | [SRT](../sources/The%20Wastes%20S3E019.%20The%20Wastes%20Round%20Up.parakeet.processed.srt) 1489–1542 | [SRT](../sources/The%20Wastes%20S3E019.%20The%20Wastes%20Round%20Up.qwen-q8.canary-ctc.nemotron.srt) 2475–2553 |
