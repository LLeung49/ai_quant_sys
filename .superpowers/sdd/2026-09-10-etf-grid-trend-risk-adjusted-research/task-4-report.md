# Task 4 Report: Risk-Adjusted ETF Validation Artifacts

## Delivered

- Replaced the legacy report summary with canonical, fail-closed blocks for:
  - `decision` (conclusion and blockers)
  - complete strategy / buy-and-hold metrics and metric differences
  - `oos_distribution`
  - execution, invested/cash sessions, exposure, turnover, costs, and cost drag
  - data cutoff, window config hashes, and Task 3 training-surface summaries
- The writer consumes only fields recorded by `InstrumentValidationResult` and
  `ValidationWindowResult`; it does not execute a strategy, broker, or provider.
- Missing or invalid evidence produces `do_not_trade`, explicit blockers, and
  null comparison/execution/OOS blocks rather than synthetic zero values.
- Replaced malformed Markdown with a UTF-8 Chinese decision report containing
  a recommendation, comparison table, OOS distribution, execution evidence,
  provenance, and event attribution.
- Expanded charts to recorded price/fills, equity, drawdown, and exposure
  panels while retaining staging-directory atomic publication.

## TDD evidence

1. Added the valid-recorded-evidence and absent-evidence report tests first.
   The initial focused run failed before implementation: existing charts could
   not handle the recorded data fixture and `comparison` did not exist.
2. Added regression tests for absent recorded exposure and an OOS window count
   that disagrees with the recorded windows. Both failed as expected because
   the legacy decision remained `passed` with an unsupported execution or OOS
   evidence block.
3. Added the fail-closed evidence, exposure, and OOS-count validation, then
   re-ran the focused suite.

## Verification

```text
$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_validation_report.py -q --basetemp 'D:\aiQuant\ai_quant_sys\.pytest-task4-report' -p no:cacheprovider
4 passed in 5.45s
```

The explicit `--basetemp` and elevated test execution were necessary because
the shared Windows pytest temporary directory was not readable in the sandbox.

## Scope check

Only `validation_report.py` and its focused tests changed. No engine or broker
code was modified.
