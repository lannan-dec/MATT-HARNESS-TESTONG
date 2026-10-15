# NEXT-STEPS

Rewritten at every `harness-close`. Assume the next session knows nothing that is not written here. Read this after `docs/memory/MEMORY.md` and `docs/ARCHITECTURE.md`. Plans in `docs/plans/` are dated snapshots of intent; this file is the current state. If they disagree, this file is right.

## What is true now (measured 2026-10-15)

- Bootstrap is complete once PR #1 merges: `gates` was green on it (run 38675808237) and the coverage floors are set to 100.0% line and 100.0% branch. Proof: `gh pr view 1`, `cat coverage_baseline.json`.
- Repository: https://github.com/lannan-dec/MATT-HARNESS-TESTONG, public. `main` is protected and requires the `gates` check. Proof: `gh api repos/lannan-dec/MATT-HARNESS-TESTONG/branches/main/protection`.
- Lint: 0 errors, 0 warnings. Proof: `python scripts/harness_lint.py`.
- Application code is the placeholder `src/greet.py` with 2 tests. Proof: `uv run --with pytest --with pytest-cov pytest -q`.

## Step 0: re-verify before acting on anything above

1. `python scripts/harness_lint.py`
2. `git status --short && git log --oneline -3`
3. `python scripts/harness_lint.py --doctor`

## Open threads

- Merge PR #1 when `gates` is green on the baseline commit; then plan the first real feature and replace `src/greet.py`.

## Traps, in the order they will bite

1. Pytest exits 5 with no tests and `gates` fails; the proof change supplies the first test.
2. Hooks must stay executable (`chmod +x .githooks/*`) or git silently skips them; a fresh clone also needs `git config core.hooksPath .githooks`.
3. Vendor skill links are symlinks on macOS; `.gitignore` entries for them must not end in a slash.
4. GitHub started no `gates` run for the first pushes of a new branch until the workflow was registered (a run on any branch, here via a probe); after that, pushes and PRs triggered it normally. If `gh pr checks` stays empty after a minute, close and reopen the PR.
5. Cursor has no transcript export, so `save_transcript.py` copies nothing for this host; note it in each session log.

## Kickoff text (paste into the next session)

> Read NEXT-STEPS.md in full, then AGENTS.md, then docs/memory/MEMORY.md, then docs/ARCHITECTURE.md. Run harness-open. Then: merge PR #1 if still open, then plan the first real feature.
