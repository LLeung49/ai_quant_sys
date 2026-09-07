# Task 4 implementation report — Freeze sub-layer budgets and run daily targets

## Scope completed

- Replaced layer-level 2–4 target validation and the universal 50% target cap
  with exact `Decimal` weight validation inside each funded sub-layer.
- Frozen targets now retain the approved sub-layer, parent layer, account-currency
  sub-layer budget, instrument type, target weight, and manifest config hash.
  Activation persists the normalized target records for daily consumers.
- Ambiguous legacy target manifests (those lacking sub-layer identity, budget, or
  instrument type) fail closed. Configured sub-layers with no targets also fail.
- Daily shadow initializes new target state with
  `sub_layer_budget * target_weight`; it no longer accepts or applies a shared
  `initial_cash` budget.
- Kept ETF costs on the current configured boundary. Stock targets dispatch to a
  separate China A-share boundary with date-versioned stamp-duty and transfer-fee
  fields; the advice-only runner records the selected cost model and never places
  an order.

## Changed files

- `src/asset_allocation/etf_adaptive/frozen_selection.py`
- `src/asset_allocation/etf_adaptive/run_shadow_daily.py`
- `tests/asset_allocation/etf_adaptive/test_frozen_selection.py`
- `tests/asset_allocation/etf_adaptive/test_run_shadow_daily.py`

## Verification

Passed:

```powershell
$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_frozen_selection.py tests/asset_allocation/etf_adaptive/test_run_shadow_daily.py tests/asset_allocation/etf_adaptive/test_shadow_report.py tests/asset_allocation/etf_adaptive/test_shadow_store.py tests/asset_allocation/etf_adaptive/test_mysql_shadow_store.py tests/asset_allocation/etf_adaptive/test_verify_shadow.py -q -p no:cacheprovider
```

Result: `59 passed in 0.18s`.

`git diff --check` passed.

The package-wide command collected the suite and produced `342 passed`, one
expected legacy-manifest failure, and four unrelated fixture setup errors. The
legacy report fixture omits required sub-layer/budget/instrument fields and is
therefore now rejected fail-closed; updating that Task 5 integration fixture is
outside Task 4. The four setup errors are `WinError 5` while pytest attempts to
scan `C:\Users\HUAWEI\AppData\Local\Temp\pytest-of-HUAWEI`, before those test
bodies run.

## Commit

`feat: fund adaptive shadow targets by sub-layer` (Task 4-only local commit)
