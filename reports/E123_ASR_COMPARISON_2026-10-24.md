# E123 — complete-export ASR comparison, 2026-10-24

**The Wastes · corrected S1E123 · No Floating Forks · played session**, with GM maintenance/quest review and a separate post-show fan tribute. Original listing **TWBD 125**, catalogue **2 November 2020** in the retained owner-spreadsheet snapshot; recording day unverified. [Dossier](../episodes/E123.md) · [Parakeet][p] · [Qwen-labelled][q]. **Text-only ASR evidence; no listening, ASR rerun, source rewrite or runtime/hardware benchmark.**

## Access, inventory and identity

The direct checkout began **clean on `main`, HEAD `5e6624159344724ccc724ce7e2e7460b87cb1e9d`** (E122 commit). The connected workspace's repository-prefixed status returned **the same branch/HEAD and zero visible changes**. GitHub successfully read the numbering policy at that **explicit commit**. Local sources and ignored audio/snapshot were used for episode evidence; no remote revision substituted for local bytes. Only the following **two E123 exports** were found in the `sources/` episode-prefix inventory; no additional raw/third-model export located there. Model/pipeline labels are **inferred from filenames**, not verified historical run settings.

| Exact basename under `sources/` | Bytes | Cues | Normalized tokens | First cue start | Final cue end |
| --- | ---: | ---: | ---: | --- | --- |
| `The Wastes S1E123. No Floating Forks.parakeet.processed.srt` | 257,461 | 2,621 | 23,679 | 00:00:06.560 | 02:49:20.370 |
| `The Wastes S1E123. No Floating Forks.qwen-q8.canary-ctc.nemotron.srt` | 345,571 | 4,264 | 23,915 | 00:00:06.400 | 02:49:20.040 |

SHA-256:

```text
Parakeet fb5a8c36e63da24722c0d776ccdc35cae142bdf2d615d6a1977b1fdeb23abf94
Qwen     26a9e129c7464b4c7c7ff31b52d75e03f2230d648e2a2383a351be948fcf22a6
MP3      6e2e967a53a0092f96cb9da27d7a9b015b9f17ba1bab4aad52bba69913e10db0
```

Matching-named audio association: **`local/The Wastes S1E123. No Floating Forks.mp3`**, **162,659,905 bytes**, ffprobe **10,137.895500 seconds (02:48:57.896)**. Parakeet/Qwen endpoints extend **22.475 / 22.145 seconds beyond this duration**. Cause, clock relationship and historical recognition-input identity remain unverified. **No constant offset, missing audio or invented speech is inferred**. Audio was not played/uploaded and no private raw material was added to tracked documentation.

Both exports parse without nonpositive durations. Primary has **zero adjacent cue overlaps**; Qwen has **one 1-millisecond overlap**, cues **604–605** near **00:21:40.999**. This is structural timing evidence, not word-alignment or acoustic completeness validation.

## Method and complete-export measurement

Ran existing `tools/prepare_episode.py` with **E123**, the verified exact pair and fresh output **`local/episode-analysis/E123`**, default ten-minute windows. `build_transcripts.parse_srt` removes speaker decorations and joins cue content. Shared `asr_metrics` normalization lowercases, deletes straight/curly apostrophes, splits on non-Unicode-letter/digit characters and produces ordered word tokens. The existing unbounded bit-vector calculation computes **exact unit-cost ordered word Levenshtein over both complete sequences**.

**1,951 edits / 23,679 primary Parakeet tokens = 8.2393682165632% inter-ASR text disagreement (8.24% rounded).** Reference/direction **Parakeet → Qwen**. Qwen has **236 more normalized tokens**. **Not WER, measured accuracy, confirmed omissions or hallucinations.** The metric includes **intro, maintenance, recap, GM dashboard, play, outro and the sung tribute**; no separate dialogue-only or song-only distance was computed.

Separate time-aware alignment yields **1,547 candidate groups**: **687 conflicting recognition, 802 possible omission, 58 uncertain segmentation**. Those are **heuristic review labels**, not the edit-distance operations or verified error counts. Several apparent omission pairs are text present in both exports at **different cue times**, including Stanley's other-body remark around **01:48:14/01:48:23** and the GM's unwell-appearance remark around **02:01:14/02:01:24**. Cue intervals are not word timings.

## Editorial reading scope

**All 17 primary ten-minute windows, all 2,621 cues, were read**, from opening through final **02:49:20** tribute credits. Typed sections distinguish maintenance/GM quest review from played events, then separate the **~02:45:55 scene fade**, post-scene outro and **~02:48:26 onward Omnom song**. The tribute was not treated as new lore or copied as lyrics.

Qwen was **completely parsed** for the measurement and **selectively read** at **00:01:12–00:02:30, 00:13–00:16, 00:21:42–00:30:36, 00:31–00:38:24, 01:09:30–01:17:36, 01:20:12–01:22:30, 01:39:36–01:52:12, 01:59:24–02:01:18, 02:29:30–02:35, 02:39:30–02:46 and 02:48 through final tribute**. Other secondary windows were **not read throughout**. This is **full primary interpretation plus selected secondary review**, not exhaustive dual-export editorial coverage or acoustic verification. Local checkpoint retains exact ranges and hashes.

## Substantive disagreements and editorial traps

| Window | Text evidence / risk | Safe interpretation and next check |
| --- | --- | --- |
| ~00:01–00:03 | Baby-arm feat, grenade/mask sheet edits and unread mushroom list | Maintenance wording, not a new limb/spell or complete item handout. Verify restrictions; no added Nash incantation. |
| ~00:13–00:16 | Both describe **swallowing then deliberate expulsion** | E122 cliffhanger actually resolved. First candy was spat out, second swallowed; no demonstrated curse or transformation. |
| ~00:23–00:29 | **rubistic triangle sphere / Rubistic Tranglosphere**, Soulbroker names, **`celeblie prime` / `Silently Prime`** | Preserve working names/uncertainty; do not fabricate a new canonical entity. The contract clock is explicitly approximate and general planar time ratio unconfirmed. |
| ~00:30–00:38 | Custodian **Tomsilar Bear / Tom Silar Bear**, female **Elenueva / Ellen Nueva**; mage council **cadulet / Cadgulet** | Self-repeated male name remains unverified orthography. Council attribution is tentative NPC identification; no proven mass possession. |
| ~00:32:45 | Parakeet refers to a dead **beersaurus**, Qwen **brachiosaurus** | Context is verification of **Chester**, not a newly encountered dinosaur. Keep original readings traceable. |
| ~01:09–01:17 | **“I could be king of space,” “king of the sun,”** and companion encouragement | Record wording as aspirations/jokes, not office, conquest or a new solar damage ability. **Ruby** names a proposed device, not a built artifact. |
| ~01:44–01:46 | Hope's Hand-removal death statement and blood-cost ring offer closely shared | Character report and unperformed proposal; no tested removal, father summoning or new demonstrated ring power. Distinguish from E116's depicted return. |
| ~01:48:40–01:50:40 | Initial broken response: Parakeet **`when he died`**, Qwen **`when Emily died`**; live participants report **lag and request replay** | Restated passage concerns **her family**. No new “Emily” character/death and no double-counted confession. Diarization splits Hope across labels 3/5; neither label independently fixes identity. |
| ~02:00:37–02:01 | Parakeet **`question yeah what oh that's`**; Qwen **`what happened to our stats?`**, both follow with **“they remain”** and Strength/Dexterity figures | Completed long rest **does not restore the drained abilities**. Stanley Strength **7**, Dexterity **17**; neither a new injury nor a cure. |
| ~02:06:18–02:06:40 | Parakeet waking fragment **`i'm going to go Angela`**, Qwen **`Nash I'm gonna go Angelashi`**, with offset flags | Context is Stanley's *Message* prank waking Nash. Do not infer Angelashi is physically present, transformed or relocated. |
| ~02:31:36 | Nobieri's prayer: Parakeet **`he christa mad hinder`**, Qwen **`Ye Christa Melaya, Irendo Ber`** | Both name an **Infernal mending prayer**, finger repaired **without HP restoration**. It is Nobieri's casting, not Nash's rhyme or a certified divine name. |
| ~02:32–02:34 | Mushroom directions and small-number investigation permission | Delivery/permission performed; larger collection and investigation outcomes unplayed. Vorel's off-location interjection is explicitly excluded. |
| ~02:39–02:45:55 | GM briefly says Diontalus then corrects to **Emenil**; both end at lake approach | Spoken GM name slip, **not possession reveal**. Refugees stay; personal leader warning and divine answer remain pending. |
| ~02:48:26–02:49:20 | Large differences in sung Omnom tribute and credits | Separate listener contribution, not a played resurrection, reliable quote or title grant. Audio and credits require checking; lyrics not reproduced. |

## Follow-through and remaining work

Core dossier/report, model log and research queue distinguish **Candy actually swallowed/expelled; long rest completed with persistent drain; Harbor reached and mushrooms delivered; refugees stay; lake communion only approached**. Material continuity, narrative, profiles, device/vehicle references and Vorel/Nash registers follow those boundaries. **No audio, SRT edits or remote writes.**

Priority listening is the **mechanics/dashboard, proper names/Prime phrase, private reconciliation and lag replay, persistent drain, mending prayer and final lake cutoff**, after establishing the **~22-second local-copy endpoint mismatch**. **E124 — Bow To The Fish Bird** is verified present in both exports but **not interpreted here**; its title cannot fill E123's absent divine answer.

**Validation:** Read back **30 changed Markdown files** and checked **2,192 link references**, with **no missing local targets**. `git diff --check` passes. `npm run lint:markdown` checks **343 maintained files** and fails on the **same 10 pre-existing violations** as the 340-file baseline. Comparison against initial `HEAD` with the installed library/config finds **zero introduced violations**; the new dossier, report and vehicle page are lint-clean. Both original SRT hashes and the matching-named local MP3 hash remain unchanged; Git shows **no source/media edits**. Work is **local and uncommitted**, with no push or remote write.

[p]: ../sources/The%20Wastes%20S1E123.%20No%20Floating%20Forks.parakeet.processed.srt
[q]: ../sources/The%20Wastes%20S1E123.%20No%20Floating%20Forks.qwen-q8.canary-ctc.nemotron.srt
