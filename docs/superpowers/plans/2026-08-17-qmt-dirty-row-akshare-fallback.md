# QMT Dirty-Row AkShare Fallback Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace only QMT daily rows with invalid core OHLCV values using validated AkShare data from the same date and adjustment mode.

**Architecture:** Add an isolated AkShare fallback module for provider selection, code and adjustment conversion, date matching, and numeric validation. The collector retains QMT batch retrieval and existing UPSERTs, merging fallback values only where QMT rows are invalid.

**Tech Stack:** Python 3.13, AkShare, pandas, pytest, QMT xtdata, existing MySQL storage layer.

## Global Constraints

- Process only QMT rows returned with invalid `open/high/low/close/volume/amount`; QMT empty responses remain failures.
- Never overwrite a valid QMT row or an unrequested date.
- Map modes exactly: `none -> ""`, `front -> "qfq"`, `back -> "hfq"`.
- Call Eastmoney `stock_zh_a_hist` first; use Sina `stock_zh_a_daily` after exception, empty response, or incomplete valid target dates.
- Write only target dates whose six required values are finite and numeric.
- An unresolved date marks its stock failed while preserving writes of other valid rows.

## File Structure

- `src/data_ingestion/akshare_market_fallback.py`: validates and returns exact-date AkShare OHLCV fallback rows.
- `src/data_ingestion/8-原始行情与复权数据采集.py`: identifies invalid QMT rows, asks the fallback module, merges valid replacements, and records unresolved rows.
- `tests/test_akshare_market_fallback.py`: provider and validation behavior.
- `tests/test_price_projection_store.py`: collector merge and unresolved-row behavior.

## Tasks

### Task 1: Add a validated AkShare fallback module

**Files:** Create `src/data_ingestion/akshare_market_fallback.py`; create `tests/test_akshare_market_fallback.py`.

**Interfaces:** Produce `fetch_valid_rows(stock_code: str, dividend_type: str, target_dates: set[str]) -> tuple[dict[str, dict], dict[str, str]]`. The first mapping contains only `{date: {open, high, low, close, volume, amount}}`; the second maps every unresolved requested date to an error message.

- [ ] Write a failing test that mocks `ak.stock_zh_a_hist`, requests `{"2026-08-14", "2026-08-15"}` in `front` mode, and asserts it receives symbol `600519`, adjustment `qfq`, returns only a valid target row, and reports an invalid target row.
- [ ] Run `$env:PYTHONPATH='src'; python -m pytest tests/test_akshare_market_fallback.py::test_fetch_valid_rows_uses_eastmoney_qfq_and_returns_only_requested_valid_dates -q`; expect failure because the module does not yet exist.
- [ ] Implement `MODE_ADJUST = {"none": "", "front": "qfq", "back": "hfq"}`, Eastmoney Chinese-column normalization, `YYYY-MM-DD` normalization, finite numeric conversion, and exact-date filtering.
- [ ] Re-run the focused test; expect pass.
- [ ] Commit only the module and test with message `feat: add validated AkShare market fallback`.

### Task 2: Add Sina as the partial-result fallback

**Files:** Modify `src/data_ingestion/akshare_market_fallback.py`; modify `tests/test_akshare_market_fallback.py`.

**Interfaces:** Keep `fetch_valid_rows`; make it merge missing target dates from Sina. `_sina_symbol("000001.SZ")` must return `"sz000001"`; `.SH` must use `sh`.

- [ ] Write a failing test where Eastmoney supplies valid `2026-08-14` only, Sina supplies `2026-08-15`, and an `back` request asserts Sina receives `sz000001` and `hfq`.
- [ ] Run `$env:PYTHONPATH='src'; python -m pytest tests/test_akshare_market_fallback.py::test_fetch_valid_rows_falls_back_to_sina_when_eastmoney_cannot_supply_every_target -q`; expect failure because no Sina request occurs.
- [ ] Implement `_sina_symbol`, Sina field normalization, per-provider exception capture, and merge only dates still unresolved after Eastmoney.
- [ ] Run `$env:PYTHONPATH='src'; python -m pytest tests/test_akshare_market_fallback.py -q`; expect pass.
- [ ] Commit only Task 2 files with message `feat: fall back to Sina for missing AkShare rows`.

### Task 3: Merge exact fallback rows into QMT batch collection

**Files:** Modify `src/data_ingestion/8-原始行情与复权数据采集.py` around `_rows_from_dataframe` and `download_and_save_batch`; modify `tests/test_price_projection_store.py`.

**Interfaces:** Import `fetch_valid_rows`. Add `_split_qmt_rows(stock_code, dataframe, dividend_type) -> tuple[list[dict], set[str]]` and `_rows_from_fallback(stock_code, rows_by_date, dividend_type) -> list[dict]`. Keep `_rows_from_dataframe` as a compatibility wrapper if existing tests call it.

- [ ] Write a failing batch test with one valid QMT row on `2026-07-28`, one invalid QMT row on `2026-07-29`, and mocked `fetch_valid_rows` returning a valid `2026-07-29` row. Assert all three modes write two rows; assert the valid QMT close remains unchanged and the invalid date uses the fallback value.
- [ ] Run `$env:PYTHONPATH='src'; python -m pytest tests/test_price_projection_store.py::test_batch_replaces_only_qmt_invalid_row_with_akshare_row -q`; expect failure because invalid QMT rows are currently logged and skipped.
- [ ] Implement splitting of valid QMT rows and dirty dates. For each code/mode call the fallback only when dirty dates exist. Convert returned fallback rows to the storage schema; raw fallback rows must set `pre_close=None` and `suspend_flag=None`, adjusted rows must set `turnover_rate=None`.
- [ ] Re-run the focused batch test; expect pass.
- [ ] Commit collector and test only with message `feat: repair QMT dirty rows with AkShare`.

### Task 4: Preserve good rows when fallback remains incomplete

**Files:** Modify `tests/test_price_projection_store.py`; modify `tests/test_akshare_market_fallback.py` if a provider-error assertion is needed.

**Interfaces:** `download_and_save_batch` must keep returning `(counts, failed_codes)`. Counts include only rows sent to UPSERT; `failed_codes` includes a code whose any mode has an unresolved dirty date.

- [ ] Write a failing test where QMT contains one valid and one invalid date and mocked fallback returns `{}` plus `{"2026-07-29": "Sina response missing target date"}`. Assert only `2026-07-28` is written, every mode counts one row, and failures equal `["600519.SH"]`.
- [ ] Run `$env:PYTHONPATH='src'; python -m pytest tests/test_price_projection_store.py::test_batch_marks_stock_failed_when_akshare_cannot_fill_qmt_dirty_date -q`; expect failure until the collector records fallback errors.
- [ ] Add `[行情回退失败]` progress output containing stock, mode, unresolved dates, and reason; mark only that stock failed while retaining valid rows for all modes and stocks.
- [ ] Run `$env:PYTHONPATH='src'; python -m pytest tests/test_akshare_market_fallback.py tests/test_price_projection_store.py -q`; expect pass.
- [ ] Commit Task 4 tests and collector changes with message `test: cover unresolved QMT dirty-row fallback`.

### Task 5: Verify the completed behavior

**Files:** Verify all Task 1-4 files.

- [ ] Run `$env:PYTHONPATH='src'; python -m pytest tests/test_akshare_market_fallback.py tests/test_price_projection_store.py tests/test_dual_track_workflow.py -q`; expect full pass.
- [ ] Run `git diff --check HEAD~4..HEAD`; expect no whitespace errors.
- [ ] Run `git diff --stat HEAD~4..HEAD`; verify implementation changes are limited to the fallback module, collector, and listed tests.
- [ ] Commit any verification-only correction with message `chore: verify AkShare dirty-row fallback`.
