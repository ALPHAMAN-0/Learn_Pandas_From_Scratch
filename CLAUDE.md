## Build / test / lint
- None found. No package.json/pyproject.toml/requirements.txt, no test runner, no lint config observed at REPO_ROOT.
- README.md documents only environment setup:
  - `python3 -m venv .venv`
  - `source .venv/bin/activate` (macOS/Linux)
  - `pip install pandas`
  - `python -c "import pandas as pd; print(pd.__version__)"` (verify install)

## Rules
- None observed with direct evidence (no CONTRIBUTING file, no CI config read — out of scope for this pass).

## Read first
- README.md — project overview, learning path, setup
- PANDAS_LEETCODE_PRACTICE.md — practice problem notes
- Introduction/Red CSV and DataFrame/main.py — simplest example of the repo's script pattern

Architecture: see ARCHITECTURE.md — read before structural changes
