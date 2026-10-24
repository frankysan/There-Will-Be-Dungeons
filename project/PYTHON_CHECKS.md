# Python checks

The project's `.py` files are checked with **Ruff** for lint errors and **Pyright** for basic type errors. **Pylance** uses Pyright's type-checking engine in VS Code; CI runs the Pyright CLI. Both read the shared [pyproject.toml](../pyproject.toml).

## Set up locally

Use Python **3.11 or later**. From the repository root:

```sh
python -m venv .venv
```

Activate the environment in PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Or activate it in Bash:

```sh
source .venv/bin/activate
```

Install the pinned check tools and run the checks:

```sh
python -m pip install -r requirements-dev.txt
python -m ruff check .
python -m pyright
python -m unittest discover -s tests
```

With Node.js/npm installed and the Python environment active, `npm run check:python` runs both static checks. The individual commands are `npm run lint:python` and `npm run typecheck:python`.

## Editor checks

Install the workspace's recommended **Python**, **Pylance**, and **Ruff** extensions. In VS Code, run **Python: Select Interpreter** and choose the environment where you installed `requirements-dev.txt`.

The [workspace settings](../.vscode/settings.json) select Pylance and enable diagnostics across the workspace. The shared configuration enables **basic** type checking, targets Python **3.11**, and resolves the standalone modules in `tools/` and `experiments/`. Pylance uses the selected interpreter to resolve dependencies, so selecting the correct environment matters.

## Scope and CI

The checks cover project Python files, including `tools/`, `tests/`, and `experiments/`. Local data and environments under `local/`, `.venv/`, `node_modules/`, and Python caches are excluded. No scripts, ASR jobs, or report regeneration run during static analysis.

Ruff explicitly enables its default `E4`, `E7`, `E9`, and `F` rule groups. Import placement (`E402`) is exempted in experiment scripts and the two tests that add `tools/` to `sys.path` before importing modules. Other enabled rules still apply to those files. These are read-only lint checks; formatting is not enforced.

The [Python checks workflow](../.github/workflows/python-checks.yml) installs the pinned tools and runs Ruff and Pyright on Python/configuration changes in pull requests and pushes to `main`. It also supports manual dispatch. The existing regression-test workflows remain separate.
