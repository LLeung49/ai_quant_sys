# ETF Per-Instrument Validation Implementation Plan

> For agentic workers: REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax.

**Goal:** Run cost-net rolling GRID/TREND versus buy-and-hold validation for a fixed ETF manifest and give every ETF an independent result.

**Architecture:** A research module builds training surfaces from the existing engine, freezes one configuration per OOS window, and returns serializable evidence. A read-only provider factory and CLI reuse existing DB adapters, produce JSON/Markdown, and never compute cross-ETF weights.

**Tech Stack:** Python, pytest, existing asset_allocation.etf_adaptive engine and MySQL read-only query adapter.

**Spec:** docs/superpowers/specs/2026-09-08-etf-per-instrument-validation-design.md

## Global Constraints

- Fixed representative ETF list only: no return-based universe/weight selection, layer portfolio, blue-chip PIT requirement, or broker orders.
- Reuse existing engine, costs, candidates, calendar, and B&H baseline.
- Training selection cannot inspect validation results; missing data returns data_rejected without date/entity substitution.
- passed means annualized OOS excess return > 0, drawdown excess <= 0.02, and a strict majority of non-lagging OOS windows.

---

### Task 1: Manifest and validation result contracts

**Files:** Create src/asset_allocation/etf_adaptive/research/instrument_validation.py and tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py; modify src/asset_allocation/etf_adaptive/research/__init__.py.

**Interfaces:** Produce ValidationTarget, FIXED_VALIDATION_TARGETS, ValidationStatus, InstrumentValidationResult, and evaluate_validation_gate for Tasks 2–3.

- [ ] Step 1: Write failing test asserting the fixed manifest is exactly: 515450.SH, 515080.SH, 510300.SH, 563360.SH, 159915.SZ, 588000.SH, 513100.SH, 513500.SH, 513130.SH, 513330.SH; assert gate passes only when annual excess is positive, drawdown excess <= .02, and 2 of 3 windows are non-lagging.
- [ ] Step 2: Run $env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py -q --basetemp=.pytest-instrument-contracts. Expected: FAIL because module does not exist.
- [ ] Step 3: Implement immutable target/window/result dataclasses with IDs, as-of date, config hash, returns, drawdowns and rejection reason. Define ValidationStatus values passed, failed, data_rejected and the gate formula annual_excess > 0 and drawdown_excess <= .02 and non_lagging_windows > total_windows / 2.
- [ ] Step 4: Re-run Step 2; expected PASS. Commit message: feat: define per-ETF validation contracts.

### Task 2: Train-only parameter surfaces and frozen OOS paths

**Files:** Modify src/asset_allocation/etf_adaptive/research/instrument_validation.py and its test file.

**Interfaces:** Consume AdaptiveBacktestDataProvider, grid_candidates, trend_candidates, stable_parameter_neighborhood, build_windows, run_baselines. Produce run_instrument_validation(target, provider, start_date, as_of_date, initial_cash).

- [ ] Step 1: Write failing tests with an in-memory provider: every result window has training_end < validation_start and a config hash; provider missing a validation session returns data_rejected.
- [ ] Step 2: Run $env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py -q --basetemp=.pytest-instrument-execution. Expected: FAIL because runner does not exist.
- [ ] Step 3: For each 504/126/126 window, split the 504 training sessions into four 126-session score segments. Run every GRID-only and TREND-only candidate per segment with B&H from run_baselines. Positive means candidate return minus B&H return >= 0. Select stable candidates at min_positive_window_share=.75 using GRID axes step_pct/unit_pct/fixed_initial_pct and TREND axes risk_per_unit/add_n/max_units/amount_ratio_min. Combine chosen configurations, then run FULL_ADAPTIVE and BUY_AND_HOLD on the following validation dates. Convert coverage/DataQuality errors to data_rejected; return failed/no_stable_training_parameters for empty family selection.
- [ ] Step 4: Add parametrized tests proving each of: non-positive annual excess, drawdown excess .021, and one of three non-lagging windows fails independently. Run the Step 2 command plus tests/asset_allocation/etf_adaptive/research/test_execution_evidence.py; expected PASS.
- [ ] Step 5: Commit message: feat: run per-ETF rolling validation.

### Task 3: Production provider and report CLI

**Files:** Create src/asset_allocation/etf_adaptive/research/validation_provider.py, tests/asset_allocation/etf_adaptive/research/test_validation_provider.py, src/asset_allocation/etf_adaptive/run_instrument_validation.py, and tests/asset_allocation/etf_adaptive/test_run_instrument_validation.py.

**Interfaces:** Produce default_validation_provider() and main(argv) -> int.

- [ ] Step 1: Write failing test that provider provenance query receives a stock code and bounded cutoff; write CLI test that monkeypatches a provider, runs start date/as-of date/output directory, and gets exactly ten JSON result rows.
- [ ] Step 2: Run $env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_validation_provider.py tests/asset_allocation/etf_adaptive/test_run_instrument_validation.py -q --basetemp=.pytest-validation-cli. Expected: FAIL because provider and CLI do not exist.
- [ ] Step 3: Use execute_query, load_authoritative_market_calendar, and AdaptiveMarketDataProvider. Provenance must query the latest effective xtquant corporate action with stock_code=%s and ex_date <= %s; reject invalid/duplicate results; return the requested cutoff, source trade_corporate_action:xtquant, complete true, and latest action date. CLI requires start date, as-of date, output dir; iterates manifest order; writes UTF-8 JSON and Markdown, lists only passed codes beneath 影子运行候选, and writes no weights. Return 0 for at least one pass, 2 for no pass, 3 if all data rejected.
- [ ] Step 4: Run $env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_run_instrument_validation.py tests/asset_allocation/etf_adaptive/research -q --basetemp=.pytest-validation-cli, then run $env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive -q --basetemp=.pytest-per-etf-validation-full. Expected: both PASS.
- [ ] Step 5: Commit message: feat: report per-ETF validation results.

## Plan Self-Review

- Task 1 fixes the non-optimized universe and independent gate; Task 2 provides training-only selection and OOS evidence; Task 3 provides fail-closed real data access and reproducible reports.
- No task builds a layer portfolio, blue-chip PIT ingestion, broker order, or return-selected ETF workflow.

