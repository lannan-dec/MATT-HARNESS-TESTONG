# NEXT-STEPS

Rewritten at every `harness-close`. Assume the next session knows nothing that is not written here. Read this after `docs/memory/MEMORY.md` and `docs/ARCHITECTURE.md`. Plans in `docs/plans/` are dated snapshots of intent; this file is the current state. If they disagree, this file is right.

## What is true now (measured 2026-10-15)

- Bootstrap steps 0 to 8 are done; step 9 is mid-flight: the proof change (`src/greet.py`, 2 tests, 100% line and branch coverage locally) is committed on `bootstrap` but the PR and green `gates` are not yet confirmed. Proof: `docs/sessions/session_2610151315.md`, `gh pr list`.
- Repository: https://github.com/lannan-dec/MATT-HARNESS-TESTONG, public. `main` is protected and requires the `gates` check. Proof: `gh api repos/lannan-dec/MATT-HARNESS-TESTONG/branches/main/protection`.
- Check whether `bootstrap` has been pushed and has a PR; `origin/main` holds only the empty root commit until it merges. Proof: `git log --oneline origin/main..bootstrap`, `gh pr list`.
- Lint: 0 errors, 1 warning (third-party `bmad-spec` SKILL.md over the 15 KB cap). Proof: `python scripts/harness_lint.py`.
- `coverage_baseline.json` floors are still null; set them with `python scripts/harness_lint.py --ratchet --update-baseline` after CI is green. Proof: `cat coverage_baseline.json`.

## Step 0: re-verify before acting on anything above

1. `python scripts/harness_lint.py`
2. `git status --short && git log --oneline -3`
3. `python scripts/harness_lint.py --doctor`

## Open threads

- Bootstrap step 9: run `harness-open`, `harness-plan feature <small thing>`, make the change with a test, `harness-close`, commit with `Surface:`, `Tests:`, `Review:`, push the branch, open a PR, wait for `gates` green, then `python scripts/harness_lint.py --ratchet --update-baseline` and commit `coverage_baseline.json`.
- The push of `bootstrap` carries tooling only; the proof change must be a separate kind (`one-kind`) or carry a `KIND-OK:` reason.

## Traps, in the order they will bite

1. Pytest exits 5 with no tests and `gates` fails; the proof change supplies the first test.
2. Hooks must stay executable (`chmod +x .githooks/*`) or git silently skips them; a fresh clone also needs `git config core.hooksPath .githooks`.
3. Vendor skill links are symlinks on macOS; `.gitignore` entries for them must not end in a slash.
4. Cursor has no transcript export, so `save_transcript.py` copies nothing for this host; note it in each session log.

## Kickoff text (paste into the next session)

> Read NEXT-STEPS.md in full, then AGENTS.md, then docs/memory/MEMORY.md, then docs/ARCHITECTURE.md. Run harness-open. Then: finish bootstrap step 9: confirm the PR's `gates` is green, set the coverage baseline, merge.
