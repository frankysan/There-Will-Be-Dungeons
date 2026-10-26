# December 2021 bonus (Bonus 2021-12): two-ASR comparison — 2026-10-26

**Archive identity:** `Bonus 2021-12 - December 2021`, out-of-game cast/GM listener Q&A; **not Wastes S2E05** and not Delvers played content. Host audibly represented in ASR saying **“December 4th”**, **not independently verified as public release/recording date**. [Dossier](../episodes/BONUS-2021-12.md).

**Provenance:** `main` workspace HEAD `132087db91cf29dea2ee5790677c02680b8534ab`, initial status contains nine visible unrelated Delvers cleanup legacy untracked entries, seven additional restricted entries, untouched. Both full-file exports fetched from GitHub at **this exact commit**; matching first local source lines verified; whole local-file byte identity not proven. Blob IDs below are Git blob IDs, not SHA-256. Source model labels inferred from filenames only.

| Export | Git blob ID | SRT cues | Last cue end | Normalized words | Text characters |
| --- | --- | ---: | --- | ---: | ---: |
| [Parakeet processed](../sources/Bonus%202021-12%20-%20December%202021.parakeet.processed.srt) | `eb71bafff14780cb1d0da181969c0d70f697e269` | **621** | **00:31:19.590** | **5,914** | **58,951** |
| [Qwen Q8 / Canary CTC / Nemotron-labelled](../sources/Bonus%202021-12%20-%20December%202021.qwen-q8.canary-ctc.nemotron.srt) | `0b250dd1ce531be9f67cb568204eb2922866a029` | **934** | **00:31:19.320** | **6,013** | **74,962** |

**Exact global unit-cost ordered word edit distance = 451 / 5,914 = 7.63% inter-ASR TEXT DISAGREEMENT (not WER or an error/accuracy rate).** Qwen has **99 more** normalized words. Method: strip cue indices/timestamps and optional `(speaker N)` labels, join speech in recording order; lowercase, remove straight/curly apostrophes joining contractions, replace non-Unicode-letter/digit with spaces, split tokens. Exact two-row DP with **±1,500**-token diagonal band; actual minimum **451 < 1,500**, so no better path could leave that band. Not a word-error rate against a human ground truth and does not measure true model omissions.

**Scope:** Entire primary export **reviewed to final host closing ~00:31:19**; complete Qwen export parsed for global numeric result and **selected independent windows** reviewed (~00:00–00:16, ~00:18–00:30). Last Qwen/Parakeet cue times nearly identical. No original audio, signal alignment, full secondary independent human-style review, or external feat rules verified. No source SRT modified.

## High-priority textual variants and listening checks

| Clock | Source disagreement or attribution |
| --- | --- |
| **~00:00–00:02** | Host gives **December 4** date; verify exact words if date is used beyond spoken attribution. Ghosts “stasis/zip file” is **Beau's explanation**; canasta is expressly comic speculation. |
| **~00:03–00:07** | Q/P agree on Beau's **Nash heart–Solar Mines–Principle** hidden design link. Scott says Nash **escaped with one other person**; companion's whereabouts unknown. *Upgraded Slow Peters* is **a question/hypothesis**, never Beau-confirmed as executed. |
| **~00:07–00:09** | Kyle initially says confusing **“Crypt Lords/Kings”**, later explicitly corrects to **Warhammer Tomb Kings**; **Khalazar** name ASR variants `Kalazar`; he denies already knowing the **Pathfinder Mummy's Mask** AP. |
| **~00:09–00:11** | Delvers **bell pants** are frogfolk cult artifacts. Qwen supports fish/frog worshipers attempting their own summons and human cultists gathering items to prevent it; these are **Kyle's unused/partly used Season One background plans**, not a newly played ritual or verified power activation. |
| **~00:11–00:14** | Jon explains ***Eldritch Blast* → *Booming Blade* → *Eldritch Blast***, links spell to **Diontalus** (ASR `Dient Tallus/Dian Talos`) and **Kittobo Prayeth** (ASR divergent). Feat label spoken **“magic adept”**, not externally validated `Magic Initiate` feat; avoid declaring legal class rules. |
| **~00:14–00:17** | **Glorious damage** token homebrew: max damage **then doubled**, chosen when rolling damage, generally **next combat**, with possible unused-party-token retention. A joke about punching dinosaurs into space is not evidence of a played event. |
| **~00:17–00:24** | Scott's early grim Nash and Jon's planned subdued Stanley are **retrospective descriptions and counterfactual redesigns**. Neither is an alternate Wastes campaign actually performed. |
| **~00:24–00:27** | Kyle offers Vorel **Principle City scholar/Tarzan-inspired English education** and evolution of verbose style; this is **creator interpretation**, not a newly played kidnapping. |
| **~00:27–00:31** | Kristen's Hope **Road Warrior** influences, Squirts alternative, potential “reckoning” and death are **ideas/speculation**. No definite future ending foretold. Jon's Hope/Stanley parallels are **interpretation**, not extra dialogue. |
| **~00:31:19** | Both exports finish at original show closing, no hidden played postscript seen in transcribed text. |

**Follow-up:** Ear-check named entities/feat, actual recording-date provenance and whether unused plot explanation has independent canonical text; preserve all creator-versus-played and Wastes-versus-Delvers boundaries. **No confirmed audio verification.**
