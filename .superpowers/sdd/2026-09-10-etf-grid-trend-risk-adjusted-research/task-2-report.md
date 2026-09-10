# Task 2 report: stable exit parameter regions

## Delivered

- Added only the approved GRID exit axes: ATR stop multiple `(2.0, 3.0,
  4.0)` and cooldown sessions `(0, 3, 5, 10)`.
- Added only the approved TREND exit/filter axes: stop-N `(1.5, 2.0, 2.5,
  3.0)` and MACD-bullish requirement `(False, True)`.
- Added `expand_candidate_axis(base_candidate, axis=...)`, which varies one
  approved new axis and retains every other grid, trend, cost, and family
  setting from the training-selected base candidate. Task 3 can use this
  bounded API instead of replaying a new/old Cartesian product.
- Corrected stable-neighborhood matching so numeric immediate neighbors must
  have every other axis unchanged. MACD categorical stability requires both
  observed values to pass.

## Scope

Changed only:

- `src/asset_allocation/etf_adaptive/research/parameters.py`
- `tests/asset_allocation/etf_adaptive/research/test_parameters.py`
- this report

No GRID or TREND execution logic, broker integration, or automated trading
behavior changed.

## Test-driven evidence

The initial focused test run failed during collection because the approved
axis constants were absent from `research.parameters`, confirming the new
contract did not already exist. The implementation was then added minimally
to satisfy the tests.

## Verification

Command:

```powershell
$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_parameters.py tests/asset_allocation/etf_adaptive/test_contracts.py -q
```

Output: `31 passed, 1 warning in 15.79s`.

The warning is the existing inability to write `.pytest_cache` in this
worktree; it does not affect test execution.

## Commit

Pending: `feat: screen stable exit parameter regions`.

## Fix round 1/5

- Restored baseline `grid_candidates()` and `trend_candidates()` to 220 and
  144 candidates respectively, with the default approved exit/filter values.
  The approved value tuples remain available only through
  `expand_candidate_axis` for staged expansion.
- Extended `stable_parameter_neighborhood` with an optional `candidates`
  sequence or config-hash index. Callers can therefore evaluate the exact
  expanded surface rather than depending on the baseline catalog.
- Made neighbor comparison remove only the asserted axis from the complete
  `AdaptiveConfig` payload. Any unrelated GRID, TREND, or cost-field change
  now prevents the candidate from being a neighbor.
- Added regressions for baseline sizes, all four single-axis expansions, a
  stable three-point expanded surface, and unrelated GRID/TREND mismatch
  rejection.

Verification:

```powershell
$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_parameters.py tests/asset_allocation/etf_adaptive/test_contracts.py -q
```

Output: `37 passed, 1 warning in 0.64s`. The warning is the existing
worktree pytest-cache permission denial.

Fix-round commit pending.
