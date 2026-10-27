# Repository agent instructions

These instructions apply to work throughout **There Will Be Dungeons Transcripts**, including the skills under `.agents/skills/`. Read the relevant skill and project-specific editorial rules in addition to this file.

## Repository access and deliverable priority

**Use the first viable method in this exact order for reading, editing and delivering repository work:**

1. **Local file access** — Directly inspect and edit the current local checkout/filesystem when it is accessible and appropriate. Prefer targeted reads, local Git status/diffs and safe working-tree changes. Include local-only/ignored source archives where permitted; do not assume they are available remotely.
2. **MCP access** — If direct local access is unavailable or insufficient, use a connected workspace/project MCP service to search, read and make guarded edits to the correct local repository. Discover its supported actions and identify its actual workspace and revision. For this repository, a workspace may be exposed as `There Will Be Dungeons Transcripts/`.
3. **GitHub access** — If the first two routes cannot do the required work, use the GitHub repository connection/API, preferably a pinned branch or commit. Use GitHub for authoritative remote history/PR operations whenever those are the actual task; do not pretend a remote tree includes local-only or uncommitted files. The GitHub-specific connector falls under this third tier, even if it is technically an MCP integration.
4. **Git patches** — If an authorized live edit cannot be made using the preceding routes, provide a minimal, reviewable Git patch against an identified revision, with exact paths and application instructions. Do not describe an unapplied patch as a repository change.
5. **Zipped file bundles** — Use a ZIP containing replacement files only when the other four options are unsuitable, unavailable or explicitly requested. Include a manifest identifying paths, baseline and scope; avoid overwriting unrelated files and never package private audio/media or secrets without authorization.

**This is an ordered preference, not an instruction to try all five methods or duplicate every read.** Before selecting a route, check whether it can handle the operation and supplies the right repository revision. If a higher-priority route is stale, read-only, denied, lacks the necessary data or would endanger existing work, use the next capable route and note the reason. For tasks inherently involving GitHub PRs, remote refs or permissions, use the connected GitHub service for that action rather than manufacturing a local substitute.

**Safety and provenance:** Check the checkout's branch, HEAD and working-tree status when possible. Never silently mix local, MCP and GitHub revisions or overwrite unrelated user changes. Use bounded source reads and guarded, unique-context edits; keep original recordings, source ASR, private maps and archived research intact. Treat successfully persisted edits, proposed patches and file bundles as distinct outcomes. Do not commit, push, merge or publish unless requested/authorized; never infer success or passing tests without checking.

See [transcription workflow](project/WORKFLOW.md), [editorial guide](project/EDITORIAL_GUIDE.md) and the applicable `.agents/skills/<skill>/SKILL.md` for task-specific procedures.
