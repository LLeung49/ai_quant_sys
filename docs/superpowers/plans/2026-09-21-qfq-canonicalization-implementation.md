# QFQ Canonicalization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make `trade_stock_daily_qfq` the only front-adjusted business source, with QMT-native integrity audits and QMT-only turnover backfill.

**Architecture:** A new raw/QFQ audit table is separate from the legacy reconcile log. A non-affine stored pair is re-read from QMT before rebuild: exact QMT matches are warnings; changed or invalid values remain hard failures. A temporary idempotent CLI fills only NULL QFQ turnover, while all business consumers migrate to QFQ.

**Tech Stack:** Python 3.13, PyMySQL, pytest, pandas, MySQL 8, QMT ContextInfo HTTP Bridge.

**Spec:** `docs/superpowers/specs/2026-09-21-qfq-canonicalization-design.md`

## Global Constraints

- Convert QMT turnover fractions to percent with `round(rate * 100, 4)`.
- Missing, invalid, unavailable, or AkShare-fallback turnover remains NULL; never derive it from current float shares.
- QFQ is the sole business front-adjusted table; old daily receives no new writes.
- Raw reads remain only for explicit unadjusted execution facts.
- Do not use `trade_price_reconcile_log` for raw/QFQ internal audit events.
- Preserve unrelated dirty changes; do not create runtime pyc/log files in QMT roots.

## Review Focus

- QMT-native non-affine pair matching storage: warning without rebuild (Task 2).
- Non-affine pair whose current QMT source differs: hard rebuild (Task 2).
- Turnover gateway failure or absent QMT date: NULL remains (Task 3).
- Backfill retry: existing turnover is never overwritten (Task 3).
- ETF raw execution facts stay raw while adjusted analytics read QFQ (Task 6).

---

### Task 1: Create the raw/QFQ integrity audit boundary

**Files:**

- Create: `sql/2026-09-21-qfq-integrity-audit.sql`
- Create: `src/data_ingestion_qmt/qfq_integrity_audit.py`
- Create: `tests/data_ingestion/test_qfq_integrity_audit.py`

**Interfaces:** `IntegrityFinding`; `build_source_fingerprint(raw: dict, qfq: dict) -> str`; `upsert_integrity_finding(finding: IntegrityFinding) -> int`.

- [ ] **Step 1: Write failing tests**

```python
def test_fingerprint_is_stable_for_key_order_and_changes_for_price_change():
    assert build_source_fingerprint({"open": 1, "close": 2}, {"open": 1}) == build_source_fingerprint({"close": 2, "open": 1}, {"open": 1})
    assert build_source_fingerprint({"open": 1, "close": 2}, {"open": 1}) != build_source_fingerprint({"open": 1, "close": 3}, {"open": 1})

def test_upsert_preserves_first_seen(monkeypatch):
    upsert_integrity_finding(IntegrityFinding("300316.SZ", "2015-02-03", "qfq_ohlc_non_affine", "warning", "qmt_verified_exception", {"open": 26.46}, {"open": 6.701783}, "a" * 64, "qmt-v2", None, "QMT verified"))
    assert "ON DUPLICATE KEY UPDATE" in captured_sql
    assert "first_detected_at" not in captured_update_clause
```

- [ ] **Step 2: Verify red**

Run: `$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='src;src/data_ingestion_qmt'; python -m pytest --basetemp .test-tmp/qfq-audit-red tests/data_ingestion/test_qfq_integrity_audit.py -q`

Expected: module import failure.

- [ ] **Step 3: Implement DDL and UPSERT**

Create `trade_qfq_integrity_audit` with `stock_code`, `trade_date`, `check_code`, `severity`, `status`, `raw_ohlc_json`, `qfq_ohlc_json`, `source_fingerprint`, `validator_version`, first/latest/resolved timestamps, `last_error`, `note`; add unique key `(stock_code, trade_date, check_code)` and index `(status, severity, last_verified_at)`. Canonicalize JSON with sorted compact keys before SHA-256. Update latest evidence/status but never `first_detected_at`.

- [ ] **Step 4: Verify green**

Run: `$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='src;src/data_ingestion_qmt'; python -m pytest --basetemp .test-tmp/qfq-audit-green tests/data_ingestion/test_qfq_integrity_audit.py -q`

Expected: PASS.

- [ ] **Step 5: Commit**

Run: `git add sql/2026-09-21-qfq-integrity-audit.sql src/data_ingestion_qmt/qfq_integrity_audit.py tests/data_ingestion/test_qfq_integrity_audit.py; git commit -m "feat: record qfq integrity findings"`

### Task 2: Verify QMT-native non-affine rows before rebuilding

**Files:**

- Modify: `src/data_ingestion_qmt/price_projection_integrity.py`
- Modify: `src/data_ingestion_qmt/8-原始行情与复权数据采集_qmt_bridge.py`
- Create: `tests/test_qfq_projection_qmt_verification.py`

**Interfaces:** `classify_projection_issues(issues, stored_raw_rows, stored_qfq_rows, qmt_raw_rows, qmt_qfq_rows) -> ProjectionDecision`; `ProjectionDecision.hard_issues`; `ProjectionDecision.verified_exceptions`.

- [ ] **Step 1: Write failing tests**

```python
def test_matching_qmt_non_affine_pair_is_warning_not_rebuild():
    decision = classify_projection_issues([RawQfqIssue("300316.SZ", "2015-02-03", "qfq_ohlc_affine_mismatch")], [RAW_300316], [QFQ_300316], [RAW_300316], [QFQ_300316])
    assert decision.hard_issues == []
    assert decision.verified_exceptions[0].status == "qmt_verified_exception"

def test_changed_qmt_pair_is_hard_repair_case():
    decision = classify_projection_issues([RawQfqIssue("300316.SZ", "2015-02-03", "qfq_ohlc_affine_mismatch")], [RAW_300316], [QFQ_300316], [RAW_300316], [{**QFQ_300316, "close_price": 6.7}])
    assert decision.hard_issues[0].reason == "qmt_storage_mismatch"
```

- [ ] **Step 2: Verify red**

Run: `$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='src;src/data_ingestion_qmt'; python -m pytest --basetemp .test-tmp/qfq-verify-red tests/test_qfq_projection_qmt_verification.py -q`

Expected: `classify_projection_issues` unavailable.

- [ ] **Step 3: Implement source verification**

Keep missing-date, non-finite, invalid OHLC, negative volume/amount, QMT failure, and source/storage difference as hard errors. For `qfq_ohlc_affine_mismatch`, request QMT `none` and `front` only for affected dates. If both match stored rows at database precision and hard checks pass, UPSERT `warning/qmt_verified_exception`; otherwise UPSERT `error/repair_pending` and full-rebuild. Record `repaired` on success and `failed` with the exception on failure. Keep full-market audit.

- [ ] **Step 4: Verify green**

Run: `$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='src;src/data_ingestion_qmt'; python -m pytest --basetemp .test-tmp/qfq-verify-green tests/test_qfq_projection_qmt_verification.py tests/test_price_projection_store.py tests/test_price_projection_store_qmt_bridge.py -q`

Expected: PASS.

- [ ] **Step 5: Commit**

Run: `git add src/data_ingestion_qmt/price_projection_integrity.py 'src/data_ingestion_qmt/8-原始行情与复权数据采集_qmt_bridge.py' tests/test_qfq_projection_qmt_verification.py; git commit -m "fix: verify qmt qfq exceptions before rebuild"`

### Task 3: Add resumable QFQ turnover backfill

**Files:**

- Create: `src/data_ingestion_qmt/10-QFQ换手率全量回填_qmt.py`
- Create: `tests/test_qfq_turnover_backfill.py`
- Modify: `docs/run_daily_once_qmt.txt`

**Interfaces:** `TurnoverWindow(stock_code, start_date, end_date, missing_dates)` and `backfill_window(window, gateway, dry_run) -> BackfillResult`.

- [ ] **Step 1: Write failing tests**

```python
def test_backfill_updates_only_null_rows():
    result = backfill_window(TurnoverWindow("600519.SH", "20260915", "20260918", {"20260915", "20260918"}), FakeGateway({"600519.SH": {"20260915": 0.0011, "20260918": 0.002}}), dry_run=False)
    assert result.matched == 2
    assert captured_values == [(0.11, "600519.SH", "2026-09-15"), (0.2, "600519.SH", "2026-09-18")]
    assert "AND turnover_rate IS NULL" in captured_sql

def test_dry_run_and_missing_qmt_date_do_not_write():
    result = backfill_window(TurnoverWindow("600519.SH", "20260915", "20260918", {"20260915", "20260918"}), FakeGateway({"600519.SH": {"20260915": 0.0011}}), dry_run=True)
    assert result.written == 0
    assert result.missing_dates == {"20260918"}
```

- [ ] **Step 2: Verify red**

Run: `$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='src;src/data_ingestion_qmt'; python -m pytest --basetemp .test-tmp/qfq-turnover-red tests/test_qfq_turnover_backfill.py -q`

Expected: script/module unavailable.

- [ ] **Step 3: Implement QMT-only idempotent updates**

Use grouped SQL to get NULL turnover windows without loading all QFQ rows. Request QMT in batches of five. Normalize dates, intersect QMT rates with requested NULL dates, and use `UPDATE trade_stock_daily_qfq SET turnover_rate=%s WHERE stock_code=%s AND trade_date=%s AND turnover_rate IS NULL`. Add `--dry-run`, `--limit-codes`, `--start-date`, `--end-date`, `--batch-size`; continue after one gateway failure and report it without fallback.

- [ ] **Step 4: Verify green and dry run**

Run: `$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='src;src/data_ingestion_qmt'; python -m pytest --basetemp .test-tmp/qfq-turnover-green tests/test_qfq_turnover_backfill.py tests/data_ingestion/test_qmt_data_gateway.py -q; python 'src/data_ingestion_qmt/10-QFQ换手率全量回填_qmt.py' --dry-run --limit-codes 5`

Expected: tests PASS and dry run reports zero writes.

- [ ] **Step 5: Commit**

Run: `git add 'src/data_ingestion_qmt/10-QFQ换手率全量回填_qmt.py' tests/test_qfq_turnover_backfill.py docs/run_daily_once_qmt.txt; git commit -m "feat: add qfq turnover backfill"`

### Task 4: Retire QMT old-table writers

**Files:**

- Modify: `src/morning_conference_qmt/sector_rotation/1-run_init_qmt_bridge.py`
- Modify: `src/morning_conference_qmt/sector_rotation/2-run_data_daily_qmt_bridge.py`
- Delete: `src/data_ingestion_qmt/1-行情数据采集_qmt_bridge.py`, `src/data_ingestion_qmt/9-前复权对账与定向重刷.py`, `src/morning_conference_qmt/sector_rotation/stock_kline_loader_qmt_bridge.py`
- Modify: `docs/README_qmt.txt`, `docs/run_daily_once_qmt.txt`, `tests/test_qmt_module_mirror.py`

**Interfaces:** QMT initialization imports classification sync plus QFQ sector index builder only; daily sector work assumes task 8 already populated QFQ.

- [ ] **Step 1: Write failing entrypoint tests**

```python
def test_qmt_init_has_no_legacy_kline_loader():
    source = INIT_PATH.read_text(encoding="utf-8")
    assert "stock_kline_loader_qmt_bridge" not in source
    assert "--skip-kline" not in source

def test_qmt_old_daily_writers_do_not_exist():
    assert not (QMT_INGESTION / "1-行情数据采集_qmt_bridge.py").exists()
    assert not (QMT_INGESTION / "9-前复权对账与定向重刷.py").exists()
```

- [ ] **Step 2: Verify red**

Run: `$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='src;src/data_ingestion_qmt'; python -m pytest --basetemp .test-tmp/qfq-retire-red tests/test_qmt_module_mirror.py -q`

Expected: old files/imports are still present.

- [ ] **Step 3: Retire paths and docs**

Remove only listed QMT writers, imports, arguments and legacy wording. State task 8 is required before sector index rebuild. Do not change the QFQ sector builder.

- [ ] **Step 4: Verify green**

Run: `$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='src;src/data_ingestion_qmt'; python -m pytest --basetemp .test-tmp/qfq-retire-green tests/test_qmt_module_mirror.py tests/test_sector_rotation_init_start_date.py tests/test_sector_rotation_qmt_bridge.py -q`

Expected: PASS.

- [ ] **Step 5: Commit**

Run: `git add -A src/data_ingestion_qmt src/morning_conference_qmt/sector_rotation docs/README_qmt.txt docs/run_daily_once_qmt.txt tests; git commit -m "refactor: retire qmt legacy daily writers"`

### Task 5: Migrate QMT business consumers

**Files:**

- Modify: `src/data_ingestion_qmt/4-新闻事件采集.py`, `src/data_ingestion_qmt/5-研报数据采集.py`
- Modify: `src/morning_conference_qmt/sector_rotation2/macd_pool.py`, `run_macd_daily.py`, `research/etf_core/return_data.py`, `research/financial/service.py`
- Create: `tests/test_qfq_qmt_consumers.py`

**Interfaces:** Existing function signatures, query aliases, DataFrame columns and return shapes remain unchanged.

- [ ] **Step 1: Write failing SQL tests**

```python
def test_qmt_news_universe_uses_qfq(monkeypatch):
    monkeypatch.setattr(news, "execute_query", capture_query)
    news.get_all_stocks()
    assert captured_sql == "SELECT DISTINCT stock_code FROM trade_stock_daily_qfq"

def test_qmt_macd_date_uses_qfq(monkeypatch):
    monkeypatch.setattr(run_macd_daily, "execute_query", capture_query)
    run_macd_daily.latest_trade_date()
    assert "trade_stock_daily_qfq" in captured_sql
```

- [ ] **Step 2: Verify red**

Run: `$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='src;src/data_ingestion_qmt'; python -m pytest --basetemp .test-tmp/qfq-qmt-consumers-red tests/test_qfq_qmt_consumers.py -q`

Expected: SQL still uses old daily.

- [ ] **Step 3: Replace QMT business reads**

Use QFQ for universes, dates, OHLC, volume, amount, MACD, ETF return mapping and financial valuation closes. Preserve aliases and returned shapes.

- [ ] **Step 4: Verify green**

Run: `$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='src;src/data_ingestion_qmt'; python -m pytest --basetemp .test-tmp/qfq-qmt-consumers-green tests/test_qfq_qmt_consumers.py tests/test_sector_rotation_qmt_bridge.py tests/research/test_etf_return_data.py -q`

Expected: PASS.

- [ ] **Step 5: Commit**

Run: `git add src/data_ingestion_qmt src/morning_conference_qmt tests; git commit -m "refactor: use qfq in qmt consumers"`

### Task 6: Migrate non-QMT consumers and block legacy writers

**Files:**

- Modify: `src/pattern_detection/data_loader.py`, `9-形态选股雷达.py`, `10-MACD全市场扫描选股.py`
- Modify: `src/data_ingestion/4-新闻事件采集.py`, `src/data_ingestion/5-研报数据采集.py`
- Modify: `src/morning_conference/sector_rotation2/macd_pool.py`, `run_macd_daily.py`, `research/etf_core/return_data.py`, `research/financial/service.py`
- Modify: direct old-table writer scripts to raise a deprecation error before write.
- Create: `tests/test_qfq_canonical_consumers.py`

**Interfaces:** Public loaders retain their parameters and output columns. `asset_allocation/etf_adaptive/market_data.py` keeps raw reads for execution facts and QFQ reads for adjusted prices.

- [ ] **Step 1: Write failing repository contract tests**

```python
def test_business_readers_use_qfq_not_legacy_daily():
    for path in BUSINESS_READER_PATHS:
        source = path.read_text(encoding="utf-8")
        assert "FROM trade_stock_daily\n" not in source
        assert "FROM trade_stock_daily AS" not in source
        assert "trade_stock_daily_qfq" in source

def test_asset_allocation_keeps_raw_and_qfq_contracts():
    source = ASSET_MARKET_DATA.read_text(encoding="utf-8")
    assert "FROM trade_stock_daily_raw" in source
    assert "FROM trade_stock_daily_qfq" in source
```

- [ ] **Step 2: Verify red**

Run: `$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='src;src/data_ingestion_qmt'; python -m pytest --basetemp .test-tmp/qfq-all-consumers-red tests/test_qfq_canonical_consumers.py -q`

Expected: remaining legacy business SQL is listed.

- [ ] **Step 3: Migrate and lock writes**

Replace front-adjusted business reads for dates, universe, OHLC, volume and amount with QFQ. Keep asset allocation raw SQL. Make direct old-table writers raise a clear deprecation error before any QMT/DB write, and remove them from daily guides.

- [ ] **Step 4: Verify green and scan**

Run: `$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='src;src/data_ingestion_qmt'; python -m pytest --basetemp .test-tmp/qfq-all-consumers-green tests/test_qfq_canonical_consumers.py tests/test_sector_rotation2_run_daily.py tests/research/test_etf_return_data.py -q; rg -n "FROM trade_stock_daily(\\s| AS)|INSERT INTO trade_stock_daily|UPDATE trade_stock_daily" src --glob "*.py"`

Expected: tests PASS; scan has no runnable business old-table SQL.

- [ ] **Step 5: Commit**

Run: `git add src/pattern_detection src/data_ingestion src/morning_conference tests; git commit -m "refactor: make qfq canonical price source"`

### Task 7: Controlled cutover and final evidence

**Files:**

- Modify: `docs/run_daily_once_qmt.txt`
- Create: `docs/user_demand/qmt_switch/QFQ_切换验收记录.md`

- [ ] **Step 1: Write preflight failure test**

```python
def test_qfq_preflight_has_no_qmt_old_writer_or_guide_reference():
    assert not QMT_OLD_WRITER.exists()
    assert "1-行情数据采集_qmt_bridge.py" not in RUN_GUIDE.read_text(encoding="utf-8")
```

- [ ] **Step 2: Verify red before cleanup**

Run: `$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='src;src/data_ingestion_qmt'; python -m pytest --basetemp .test-tmp/qfq-preflight-red tests/test_qfq_canonical_consumers.py -q`

Expected: fails until Task 4 cleanup is complete.

- [ ] **Step 3: Apply DDL and run reviewed backfill**

Run DDL through the existing database migration procedure. Then run `python 'src/data_ingestion_qmt/10-QFQ换手率全量回填_qmt.py' --dry-run --limit-codes 20`, review output, then run `python 'src/data_ingestion_qmt/10-QFQ换手率全量回填_qmt.py' --batch-size 5`. Record before/after NULL counts, QMT failures, unmatched dates and audit statuses in the acceptance record.

- [ ] **Step 4: Run final regression**

Run: `$env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONPATH='src;src/data_ingestion_qmt'; python -m pytest --basetemp .test-tmp/qfq-final tests/test_qmt_module_mirror.py tests/data_ingestion/test_qmt_data_gateway.py tests/data_ingestion/test_qfq_integrity_audit.py tests/test_qfq_projection_qmt_verification.py tests/test_qfq_turnover_backfill.py tests/test_qfq_canonical_consumers.py -q`

Expected: PASS. Separately record project-wide pytest collection `PermissionError` paths if historical report/temp folders remain inaccessible.

- [ ] **Step 5: Commit evidence**

Run: `git add docs/run_daily_once_qmt.txt docs/user_demand/qmt_switch/QFQ_切换验收记录.md tests; git commit -m "docs: record qfq cutover verification"`

## Self-Review

- Tasks 1–2 implement audit persistence plus QMT verification/rebuild boundaries.
- Task 3 provides the NULL-only QMT turnover backfill.
- Tasks 4–6 retire writers and migrate both QMT and non-QMT consumers while protecting explicit raw semantics.
- Task 7 records controlled database execution and verification.
- Every review-focus case has a named test, all interfaces appear before use, and no TBD/TODO placeholders remain.
