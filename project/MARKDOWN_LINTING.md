# Markdown validation

The repository uses **markdownlint-cli2** to catch Markdown structure mistakes (especially broken GitHub-flavored tables) before new lore documents are merged. This check is for editorial Markdown only; it **never edits or regenerates the source SRT**.

## Run locally

From the repository root, install **Node.js 22 or later**, then run:

```sh
npm install
npm run lint:markdown
```

To suggest automatic formatting repairs **only in a local working copy**, run `npm run lint:markdown:fix`, inspect the diff, and run the normal check again. **Do not mass-autofix source transcripts or archived research.** The normal lint command is read-only.

The [GitHub Actions workflow](../.github/workflows/markdownlint.yml) runs the same check on changes to Markdown, linter configuration and package metadata in pull requests or on pushes to `main`. It can also be manually dispatched.

## Scope and rule policy

The glob set in [`.markdownlint-cli2.yaml`](../.markdownlint-cli2.yaml) covers the repository README and maintained documents in `episodes/`, `narrative/`, `world/`, `project/`, and `reports/`. **Frozen `research/legacy/` snapshots and generated `transcripts/` files are excluded** to preserve their provenance and avoid lint fixes changing historical/automated output.

The [`.markdownlint.json`](../.markdownlint.json) configuration intentionally starts with structural correctness rules instead of demanding stylistic rewrites of the entire evidence archive:

- **MD055 / MD056 / MD058:** table outer-pipe style, equal column counts and required blank lines around tables.
- **MD001 / MD022 / MD024 / MD025:** heading order, spacing, and unique title/section structure; duplicate headings are allowed only when they appear in distinct parent sections.
- **MD009 / MD010 / MD012 / MD047:** whitespace hygiene and final newline.

This is a **focused baseline**, not a claim that every possible markdownlint style rule is enabled. **MD013 long-line limits remain disabled**, because citation-heavy prose and source-backed narratives are intentionally long, and **MD060 fixed table-cell widths are not required**. A table can still be unreadably wide even if its pipes and cell counts parse correctly; prefer a **compact chronological table with detailed notes below**, as in [Vorel's title register](../world/characters/vorel.md).

If a new rule is enabled later, first review its findings in the maintained documentation and resolve them or narrowly document an intentional exception. **Do not silence table-integrity failures** to preserve a broken table. Tests are concerned with Markdown source structure, not with the **truth of episode claims**, citation targets or visual rendering. Those need separate review.
