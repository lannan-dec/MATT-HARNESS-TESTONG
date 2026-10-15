# Plan (feature): proof-greet
Status: done 2026-10-15. Departures: none from the design; the commit carries a KIND-OK because the bootstrap branch (tooling) must ship with a product test for `gates` to pass on a protected `main`.

Acceptance criteria: `greet("World")` returns `"Hello, World!"`, and an empty or blank name raises `ValueError`. Verified by `tests/test_greet.py` passing under the repository's test command and by `gates` going green on the pull request with a Cobertura `coverage.xml` produced.
Surface: src/greet.py, tests/test_greet.py, pytest.ini, coverage_baseline.json (floors set after CI is green), docs/ARCHITECTURE.md, NEXT-STEPS.md, docs/sessions/session_2610151315.md
Design: one pure function, stdlib only. `pytest.ini` sets `pythonpath = src` so `uv run pytest` and `python -m pytest` both import it; the alternative (a package with `__init__.py`) is more files for no gain. No dependency, no abstraction added.
Test plan: unit `greet` happy path and the blank-name failure; e2e n/a: no user-facing journey exists, this change only exercises the harness loop.
Architecture map delta: yes (Layout gains `src/` and `tests/`, and the "not built yet" line goes). ADR: no (no durable decision; it is a throwaway proof change).
Cross-repo impact: none
Open questions: should the proof function stay once the real stack arrives? Recommended: yes until replaced, it carries the coverage floor.
BACKLOG: the third-party `bmad-spec` SKILL.md is over the 15 KB cap (WARN); not ours to split.
