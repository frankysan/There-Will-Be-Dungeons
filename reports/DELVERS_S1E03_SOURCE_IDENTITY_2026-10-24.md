# Delvers S1E03 — source-identity mislabel and subsequent recovery (2026-10-24)

**RECOVERED:** The true S1E03 is now available in three additional SRT files with **`(corrected)`** filenames: Parakeet blob `f7a2823f5b2ad8e048a324c2a05d9789cbcf5506`, Qwen Q4 `bd0e0373989511d9045eec74ecc06f3325a896da`, and Qwen Q8 `da85b4f44a0d397c64670dc3fac2397e343bf34c`. They start after the crypt with the guild's Grick Sighted assignment and end amid the initial grick fight, immediately preceding S1E04. The separately named corrected MP3 is inventoried but **not accessible for listening** through the workspace. [Genuine S1E03 dossier](../delvers/episodes/S1E03.md) · [new comparison](DELVERS_S1E03_ASR_COMPARISON_2026-10-24.md). The following is **historical explanation of the still-mislabeled *uncorrected* files**, not a claim that S1E03 remains absent.

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

The inventoried *older* local MP3s `local/Delvers S1E03. Raw End Of Joke Stick.mp3` and `local/Delvers S1E04. Where did this dungeon come from.mp3` could not be opened with the permitted workspace binary reader. They must be flagged **IDENTITY SUSPECT / NOT VERIFIED**, not confirmed duplicates. Compare duration, tags and fingerprint against the original published S1E03 recording before replacing, deleting or renaming anything.

## Documentation crosswalk

- [S1E03 dossier](../delvers/episodes/S1E03.md) and [S1E03 comparison](DELVERS_S1E03_ASR_COMPARISON_2026-10-24.md): **now genuine recovered-session research** using the three `(corrected)` exports; **7.39% P–Q8 and 7.53% P–Q4**, both text-only.
- [S1E04 dossier](../delvers/episodes/S1E04.md): preserves the previously misattributed grick/dungeon analysis with the corrected identity.
- [S1E04 comparison](DELVERS_S1E04_ASR_COMPARISON_2026-10-24.md): preserves **1,615 / 21,105 = 7.65%** disagreement for the two **mislabeled S1E03-named exports**. No exact whole-export metric is claimed for the two correctly named S1E04 sources.
- Source inventory and Delvers review queue **now mark S1E03 as recovered and researched**; the original `S1E03` paths remain flagged as mislabeled **S1E04**. Kyle's S1E04 recap is corroborated by the newly obtained S1E03 scene, without converting S1E04-only outcomes into S1E03 scenes.

**Historical link-warning status:** The earlier audit noted that two then-untracked creature pages linked to a blocked S1E03 dossier. Both S1E03 and S1E04 now have their own source-first dossiers. The creature page citations should be audited **per specific scene**, not mechanically reassigned: Evelyn's first grick kill is **S1E03**; the later escape, trap corpses and return are **S1E04**.

**Preservation:** No original audio or SRT file is to be edited by this documentation correction. A source-directory sidecar was attempted but denied by workspace write permissions; this audit and source inventory are the durable mislabel notices.
