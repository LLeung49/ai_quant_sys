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
