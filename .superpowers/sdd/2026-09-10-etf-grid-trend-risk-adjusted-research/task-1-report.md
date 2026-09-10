# Task 1 report: risk-adjusted research decisions

## Delivered

- Added `research.decision` with `ResearchConclusion`, `ResearchEvidence`,
  `DecisionSummary`, and a pure fail-closed `evaluate_research_decision`.
- Re-exported the decision contract from `research.__init__`.
- Added focused tests for pass, defensive parameter optimization, invalid data,
  non-finite and boolean numerics, incomplete evidence, and structural-change
  conclusions.

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

Output: `7 passed, 1 warning in 0.08s`. The warning is an existing inability
to write `.pytest_cache` in this worktree; it does not affect test execution.

## Commit

`5e6c2b98f61a8841b31c7eb02f6230738e92b913` — `feat: add risk-adjusted
research decisions`.

## Concerns

No strategy, broker, execution, GRID, or TREND logic changed. Decision
thresholds are explicit and intentionally conservative; execution evidence is
validated for finite, non-negative cost/turnover and exposure constrained to
the [0, 1] range, since this contract has no portfolio-value-normalized cost
limit from which to derive an additional ceiling.
