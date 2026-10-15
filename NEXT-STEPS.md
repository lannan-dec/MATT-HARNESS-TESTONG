# NEXT-STEPS

Rewritten at every `harness-close`. Assume the next session knows nothing that is not written here. Read this after `docs/memory/MEMORY.md` and `docs/ARCHITECTURE.md`. Plans in `docs/plans/` are dated snapshots of intent; this file is the current state. If they disagree, this file is right.

## What is true now (measured 2026-10-15)

- Bootstrap is in progress (step 3 done: Part B and placeholders filled); skills and enforcement are not yet installed. Proof: `python scripts/harness_lint.py`.

## Step 0: re-verify before acting on anything above

1. `python scripts/harness_lint.py`
2. `git status --short && git log --oneline -3`
3. `python scripts/harness_lint.py --doctor`

## Open threads

- Bootstrap: steps 4 to 9 of BOOTSTRAP.md remain; the next session needs to know which step passed last (see the newest session log).

## Traps, in the order they will bite

1. Arming `core.hooksPath` before the skills exist makes every commit fail; finish steps 4 and 5 first.

## Kickoff text (paste into the next session)

> Read NEXT-STEPS.md in full, then AGENTS.md, then docs/memory/MEMORY.md, then docs/ARCHITECTURE.md. Run harness-open. Then: continue the bootstrap from the first step whose check has not passed.
