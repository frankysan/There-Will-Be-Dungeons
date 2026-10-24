# Markdown validation

The repository uses **markdownlint's core library** plus the local [Node.js runner](../scripts/lint-markdown.mjs) to catch Markdown structure mistakes (especially malformed GitHub-flavored tables). We previously used `markdownlint-cli2@0.23.3`, but its glob-processing dependency tree triggered npm audit warnings. Even cli2 0.24.0 still depends on `micromatch`, whose `braces` dependency had no patched release at the time of this change. Using the core library directly avoids that CLI-specific glob dependency tree and retains the same Markdown rules.

## Run locally

From the repository root, install **Node.js 22 or later** and run:

```sh
npm install
npm run lint:markdown
npm audit
```

## KaTeX dependency security

**October 2026:** `markdownlint@0.42.0` brings in `micromark-extension-math`, which depends on `katex@^0.16.0`. The KaTeX advisory [GHSA-238p-pmpm-9mq7](https://github.com/advisories/GHSA-238p-pmpm-9mq7) affects KaTeX versions **before 0.18.2**. Because the patched release is outside the transitive semver range, `package.json` includes a **targeted npm override** for `katex: 0.18.2`. This is a deliberate cross-minor override, **not** a downgrade of `markdownlint` as `npm audit fix --force` suggests.

After `npm install`, check `npm ls katex`, `npm run lint:markdown`, and `npm audit`. The override's compatibility with this linter and a clean dependency audit **must be verified using the installed dependency tree**, not inferred from the manifest. If a future maintained `micromark-extension-math` release permits patched KaTeX naturally, remove the override after testing.

The security advisory concerns how inherited JavaScript properties can affect KaTeX's trusted-rendering settings when prototype pollution is already present. This repository **only lints maintainer-controlled Markdown** and does not publish KaTeX-rendered HTML, which limits exposure; nonetheless, prefer a patched dependency when compatible.

If an older installation/lockfile still contains `markdownlint-cli2`, refresh dependencies with `npm install` after pulling this change. Verify the installed tree with `npm ls markdownlint markdownlint-cli2 micromatch braces`. A locally generated `package-lock.json` should be reviewed and committed separately if this project adopts lockfile-based reproducibility. Do **not** use `npm audit fix --force` to select a CLI dependency tree without reviewing its dependencies.

## Fast per-episode validation (changed files only)

Use the existing runner with **explicit maintained Markdown paths** when validating the current episode's edits, rather than linting the entire archive after every documentation pass:

```sh
npm run lint:markdown -- --files episodes/E125.md reports/E125_ASR_COMPARISON_2026-10-24.md world/CHRONOLOGY.md
```

Substitute **actual changed paths** from Git status; include each modified dossier/report/reference page as needed. The `--files` mode is **read-only**, rejects paths outside the maintained Markdown set, refuses absent/empty arguments, and does not recurse across the repository. `README.md` and Markdown inside `delvers/`, `episodes/`, `narrative/`, `world/`, `project/` and `reports/` are eligible. The `.agents/skills/` tree is **outside this maintained-documentation lint scope**. Quoting is required for individual paths containing spaces.

**Full repository lint remains** `npm run lint:markdown` (also the CI/release command); targeted success **does not** mean all repository Markdown passed. An episode whose only available access is a read/write MCP connector with no general-purpose runner must report **lint not run**, not compensate by repeatedly fetching the same content. Editorial source/cutoff checks and automatic Markdownlint are separate kinds of validation; neither is an audio quality check. [Episode-analysis skill](../.agents/skills/twbd-episode-analysis/SKILL.md).

To apply available automatic formatting fixes **only in the local working copy**, run `npm run lint:markdown:fix`, inspect the diff and run normal lint again. The regular lint command is **read-only**. Do not mass-autofix sources or historical research. `--fix` intentionally cannot be combined with `--files`.

The [GitHub Actions workflow](../.github/workflows/markdownlint.yml) runs **both** the Markdown lint command and `npm audit --audit-level=low` on Markdown and dependency changes in pull requests or pushes to `main`. It can also be manually dispatched. New dependency advisories will fail the audit step for review.

## Scope and rule policy

The runner uses **Node's native file-system APIs**, not glob libraries, to find `README.md` and maintained documentation recursively within `delvers/`, `episodes/`, `narrative/`, `world/`, `project/`, and `reports/`. Delvers coverage includes its preparation documents and future nested episode, world and narrative pages. **Frozen `research/legacy/` snapshots and generated `transcripts/` files are excluded**, as are source SRTs.

The [`.markdownlint.json`](../.markdownlint.json) configuration enables a structural baseline:

- **MD055 / MD056 / MD058:** table outer-pipe style, equal column counts and blank lines around tables.
- **MD001 / MD022 / MD024 / MD025:** heading order, spacing and unique title/section structure, with repeat headings allowed in distinct parent sections.
- **MD009 / MD010 / MD012 / MD047:** whitespace and final-newline hygiene.

**MD013 line length is deliberately disabled** for citation-heavy prose; MD060 table-column visual alignment is not required. A Markdown table can remain unwieldy even with valid pipe counts; prefer compact tables with prose underneath (as in [Vorel's title register](../world/characters/vorel.md)).

The standalone `markdownlint` package and its dependencies should still be checked using `npm audit`; this change **does not guarantee every future advisory is absent**. If a new rule or security advisory arises, review the findings and resolve or narrowly document the exception instead of hiding errors. Markdown linting checks **formatting**, not the truth of episode claims, link destinations or visual rendering.
