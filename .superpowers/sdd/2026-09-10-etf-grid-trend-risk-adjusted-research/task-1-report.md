# Task 1 report: risk-adjusted research decisions

## Delivered

- Added `research.decision` with `ResearchConclusion`, `ResearchEvidence`,
  `DecisionSummary`, and a pure fail-closed `evaluate_research_decision`.
- Re-exported the decision contract from `research.__init__`.
- Added focused tests for pass, defensive parameter optimization, invalid data,
  non-finite and boolean numerics, incomplete evidence, and structural-change
  conclusions.
- Fix round 1: added a strict positive-integer OOS-window count and
  `cost_drag` (total cost / recorded initial OOS NAV). Cost drag is finite,
  bounded to [0, 1], and must not exceed 2% for any non-blocked conclusion.
- Fix round 2: added `initial_oos_nav`, requiring it to be finite and
  positive. The evaluator verifies `cost_drag == total_cost / initial_oos_nav`
  with `rel_tol=1e-9` and `abs_tol=1e-12` before reaching a conclusion.

## Files changed

- `src/asset_allocation/etf_adaptive/research/decision.py`
- `src/asset_allocation/etf_adaptive/research/__init__.py`
- `tests/asset_allocation/etf_adaptive/research/test_decision.py`
- `.superpowers/sdd/2026-09-10-etf-grid-trend-risk-adjusted-research/task-1-report.md`

## Verification

Command:

```powershell
$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_decision.py -q
```

Output: `13 passed, 1 warning in 0.08s`. The warning is an existing inability
to write `.pytest_cache` in this worktree; it does not affect test execution.

## Commit

`5e6c2b98f61a8841b31c7eb02f6230738e92b913` — `feat: add risk-adjusted
research decisions`.

Fix-round commit: `b119ecf6200bb269669363231723700c3741fd06` — `fix: harden
research decision evidence`.

Fix-round 2 commit: `5b97948643f46b9bb948921c7adaea57619fcaed` — `fix: verify
research cost drag`.

## Concerns

No strategy, broker, execution, GRID, or TREND logic changed. Decision
thresholds are explicit and intentionally conservative; execution evidence is
validated for finite, non-negative cost/turnover, exposure constrained to the
[0, 1] range, and cost drag capped at 2%.
