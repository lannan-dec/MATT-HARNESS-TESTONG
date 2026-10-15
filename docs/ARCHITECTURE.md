# Architecture map

last_reviewed: 2026-10-15

The one living map of this repository: components, flows, boundaries and invariants. Read it before touching unfamiliar code; update it in the same change that moves structure (`harness-close` step 3). It describes this repository only. Each invariant cites the defect or decision that bought it. Factual claims carry a `verify:` line so the lint fails on the commit that makes them false.

## What this repository is

A trial repository for the agentic development harness: it holds the harness itself and no application code yet. It is for the person testing how coding agents from several vendors behave under the harness.

## Layout

| Path | Holds | Owner doc or skill |
|---|---|---|
| `AGENTS.md` | the constitution (Part A) and repository facts (Part B) | `AGENTS.md` |
| `scripts/` | lint, push guard and transcript saver | `AGENTS.md` section 6 |
| `.githooks/`, `.github/` | git hooks and the CI gate | `AGENTS.md` section 2 |
| `.agents/skills/` | installed, pinned skills | `skills-lock.json` |
| `docs/` | map, ADRs, memory, plans, session records | `AGENTS.md` section 3 |

## Flows

1. Change loop: `harness-open` -> `harness-plan` -> implement -> `harness-close` -> commit -> push on a branch -> pull request with `gates` green. Files: `.agents/skills/`, `scripts/harness_lint.py`.

## Boundaries and invariants

- **Enforcement lives in git and CI.** Hooks and the `gates` workflow run the lint, not any vendor hook. Bought by: the harness adoption decision (docs/adr/0001-adopt-harness.md).
  <!-- verify: exists AGENTS.md -->
  <!-- verify: exists docs/adr/README.md -->
  <!-- verify: exists docs/memory/MEMORY.md -->
  <!-- verify: exists docs/sessions/README.md -->
  <!-- verify: exists scripts/harness_lint.py -->
  <!-- verify: exists scripts/save_transcript.py -->
  <!-- verify: exists .githooks/pre-commit -->
  <!-- verify: exists .githooks/pre-push -->
  <!-- verify: exists .github/workflows/harness-gates.yml -->

## Deliberately not built yet

- Application code: add when the first real feature is planned.
