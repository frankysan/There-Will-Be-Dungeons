# Delvers S1E03 — source-identity mislabel audit (2026-10-24)

**Verified SRT mislabel:** Both existing S1E03-labelled SRT exports contain the **S1E04 session**, not the real S1E03 — *Raw End Of Joke Stick*. S1E03 published **2021-01-29**; S1E04 — *Where did this dungeon come from?* published **2021-02-01**, according to the [episode spreadsheet](https://docs.google.com/spreadsheets/d/11qsWzHHKI0i9yWBze6yoTtFKF9VltrfOFNTQ-g_gLlw/edit). The mislabelled session itself announces **Sunday 2021-01-31** and depicts the end of the grick battle, trapped dungeon and sword-hilt discovery.

## Flags for individual files in sources/

| Filename | Actual contents | Git blob SHA |
| --- | --- | --- |
| `Delvers S1E03. Raw End Of Joke Stick.parakeet.processed.srt` | **MISLABELED: S1E04** (shorter/ad-free copy) | `0a56deaad51f03734dabb441e31d47a843c8f8a9` |
| `Delvers S1E03. Raw End Of Joke Stick.qwen-q8.canary-ctc.nemotron.srt` | **MISLABELED: S1E04** (shorter/ad-free copy) | `ca6611fd7992660be490876926f4292f9a80298e` |
| `Delvers S1E04. Where did this dungeon come from.parakeet.processed.srt` | **Correctly labelled S1E04**, includes beginning advertisements | `182a2291c2820d6b75be3e633b0c6c94bb87d198` |
| `Delvers S1E04. Where did this dungeon come from.qwen-q8.canary-ctc.nemotron.srt` | **Correctly labelled S1E04**, includes beginning advertisements | `858eaa0f05f713971803dd4fc1dfdbf3d7eaf102` |

Session overlap: Parakeet pairs share **82.9%**, Qwen pairs **93.1%**, of the smaller export's unique seven-word sequences. Their content, intro date and ending substantiate the same-session identity. This is not an audio fingerprint. Additional ads shift timestamps, so the recorded times in the corrected dossier apply to the **S1E03-filename ad-free S1E04 transcript**, not to the advertised S1E04 source.

## Audio identity still to verify

The inventoried local MP3s `local/Delvers S1E03. Raw End Of Joke Stick.mp3` and `local/Delvers S1E04. Where did this dungeon come from.mp3` could not be opened with the permitted workspace binary reader. They must be flagged **IDENTITY SUSPECT / NOT VERIFIED**, not confirmed duplicates. Compare duration, tags and fingerprint against the original published S1E03 recording before replacing, deleting or renaming anything.

## Documentation crosswalk

- [S1E03 dossier](../delvers/episodes/S1E03.md) and [S1E03 comparison](DELVERS_S1E03_ASR_COMPARISON_2026-10-24.md): **warning/redirects, not completed S1E03 research**.
- [S1E04 dossier](../delvers/episodes/S1E04.md): preserves the previously misattributed grick/dungeon analysis with the corrected identity.
- [S1E04 comparison](DELVERS_S1E04_ASR_COMPARISON_2026-10-24.md): preserves **1,615 / 21,105 = 7.65%** disagreement for the two **mislabeled S1E03-named exports**. No exact whole-export metric is claimed for the two correctly named S1E04 sources.
- Source inventory and Delvers review queue must flag original S1E03 as **missing/unresearched**, and set the next verification priority to recovering its genuine January 29 recording. Kyle's S1E04 recap may describe events of S1E03 but is not direct S1E03 transcript evidence.

**Pending link correction:** Two concurrently created **untracked** pages, `delvers/world/CREATURES_AND_MONSTERS.md` and `delvers/world/creatures/gricks.md`, still reference the mislabeled S1E03 dossier in their footnotes. Guarded workspace replacement denied editing them, so their attribution needs correction to **S1E04** by an editor who can modify those untracked files. Their main subject matter is unchanged; do not mistake this outstanding issue for verified S1E03 research.

**Preservation:** No original audio or SRT file is to be edited by this documentation correction. A source-directory sidecar was attempted but denied by workspace write permissions; this audit and source inventory are the durable mislabel notices.
