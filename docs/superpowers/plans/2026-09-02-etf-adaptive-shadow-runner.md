# ETF Adaptive Strategy Shadow Runner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Run the frozen adaptive ETF strategy after each close, persist exact state, and emit auditable T+1 order advice without any brokerage order capability.

**Architecture:** Add immutable frozen-config records and transactional daily state/signal tables, then wrap the same indicator, strategy, risk, and execution semantics used by historical backtests. The runner fails closed on stale data, duplicate dates, missing prior state, or config mismatch and publishes machine-readable plus human-readable reports.

**Tech Stack:** Python 3.11+, MySQL 8, dataclasses, argparse, pytest.

**Spec:** `docs/user_demand/asset-allocation-strategy/防御与宽基ETF层自适应网格+趋势策略-回测规格-v1.md`

## Global Constraints

- Requires the data-foundation, backtest-core, and research-report plans.
- The runner may persist shadow state and advice but must not import QMT trading/order APIs or expose an order-placement interface.
- One frozen selection/config is active for a six-month review cycle; daily execution never optimizes parameters.
- Every state transition and order advice must carry as-of date, execution-eligible date, model version, config hash, and prior-state identity.
- Re-running the same date/config is idempotent and produces byte-equivalent advice.
- At least 60 trading sessions of shadow evidence are required before a separate live-trading design.

---

### Task 1: Add shadow persistence schema and repository

**Files:**
- Create: `sql/20260902_create_etf_adaptive_shadow_tables.sql`
- Create: `src/asset_allocation/etf_adaptive/shadow_store.py`
- Test: `tests/asset_allocation/etf_adaptive/test_shadow_store.py`

**Interfaces:**
- Produces: `ShadowStore.ensure_schema()`, `load_frozen_config`, `load_latest_state`, `persist_run(run)`, and immutable identities `(as_of_date, stock_code, model_version, config_hash)`.
- Consumes: JSON-safe strategy state and frozen research selection.

- [ ] **Step 1: Write failing repository contract tests**

```python
def test_persist_run_is_idempotent_and_never_replaces_different_config() -> None:
    store = InMemoryShadowStore()
    run = _shadow_run(config_hash="cfg-a")
    store.persist_run(run)
    store.persist_run(run)
    assert store.run_count == 1
    with pytest.raises(ConfigConflictError):
        store.persist_run(replace(run, config_hash="cfg-b"))
```

- [ ] **Step 2: Run shadow-store tests and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_shadow_store.py -q`

Expected: FAIL because the schema and repository are absent.

- [ ] **Step 3: Implement append-only config/run identities and atomic state writes**

```sql
CREATE TABLE IF NOT EXISTS asset_allocation_etf_adaptive_run (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    as_of_date DATE NOT NULL,
    model_version VARCHAR(64) NOT NULL,
    config_hash CHAR(64) NOT NULL,
    run_id CHAR(36) NOT NULL,
    status VARCHAR(32) NOT NULL,
    error_json JSON NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uk_adaptive_run (as_of_date, model_version, config_hash)
);
```

Add separate frozen-config, per-symbol state, order-advice, fill-observation, and health-check tables. Use a single database transaction for one daily run so partial state/advice cannot be visible.

- [ ] **Step 4: Run store tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_shadow_store.py -q`

Expected: PASS.

- [ ] **Step 5: Commit schema and store**

```powershell
git add sql/20260902_create_etf_adaptive_shadow_tables.sql src/asset_allocation/etf_adaptive/shadow_store.py tests/asset_allocation/etf_adaptive/test_shadow_store.py
git commit -m "feat: persist adaptive ETF shadow state"
```

### Task 2: Freeze approved research selections for daily use

**Files:**
- Create: `src/asset_allocation/etf_adaptive/frozen_selection.py`
- Test: `tests/asset_allocation/etf_adaptive/test_frozen_selection.py`

**Interfaces:**
- Produces: `FrozenSelection.from_research_manifest(path)`, `validate_activation(selection, today)`, and `activate_selection(store, selection)`.
- Consumes: research `manifest.json`, selected ETFs, layer weights, config hashes, and review dates.

- [ ] **Step 1: Write failing mutation and activation-date tests**

```python
def test_frozen_selection_rejects_manifest_hash_mismatch() -> None:
    with pytest.raises(ValueError, match="manifest config hash mismatch"):
        FrozenSelection.from_payload(_payload(config_hash="wrong"))


def test_activation_cannot_begin_before_research_data_cutoff() -> None:
    with pytest.raises(ValueError, match="activation date must follow data cutoff"):
        validate_activation(_selection(cutoff=date(2026, 9, 1), active_from=date(2026, 9, 1)), date(2026, 9, 1))
```

- [ ] **Step 2: Run frozen-selection tests and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_frozen_selection.py -q`

Expected: FAIL because frozen-selection handling is absent.

- [ ] **Step 3: Implement canonical loading and activation guards**

```python
@dataclass(frozen=True)
class FrozenSelection:
    model_version: str
    config_hash: str
    data_cutoff: date
    active_from: date
    review_after: date
    targets: tuple[FrozenTarget, ...]

    def canonical_payload(self) -> dict[str, object]:
        return {"model_version": self.model_version, "data_cutoff": self.data_cutoff.isoformat(),
                "active_from": self.active_from.isoformat(), "review_after": self.review_after.isoformat(),
                "targets": [target.canonical_payload() for target in self.targets]}
```

Recompute the hash from canonical content, require unique ETF codes, layer weights summing to one per layer, no single target above 50%, and active/review dates matching the six-month policy.

- [ ] **Step 4: Run frozen-selection tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_frozen_selection.py -q`

Expected: PASS.

- [ ] **Step 5: Commit frozen-selection handling**

```powershell
git add src/asset_allocation/etf_adaptive/frozen_selection.py tests/asset_allocation/etf_adaptive/test_frozen_selection.py
git commit -m "feat: freeze adaptive ETF production selections"
```

### Task 3: Implement fail-closed daily shadow orchestration

**Files:**
- Create: `src/asset_allocation/etf_adaptive/run_shadow_daily.py`
- Test: `tests/asset_allocation/etf_adaptive/test_run_shadow_daily.py`

**Interfaces:**
- Produces: `run_shadow_date(as_of_date, now, store, provider) -> ShadowRunSummary` and CLI `--as-of-date`, `--today`, `--model-version`, `--config-hash`.
- Consumes: the exact backtest close-processing function, authoritative calendar, active frozen selection, prior state, and fresh T bars.

- [ ] **Step 1: Write failing freshness, replay, and no-broker-import tests**

```python
def test_shadow_runner_fails_closed_when_target_bar_is_stale() -> None:
    with pytest.raises(DataFreshnessError, match="510300.SH missing 2026-09-01 bar"):
        run_shadow_date(date(2026, 9, 1), _after_close(), _store(), _provider_missing_target())


def test_shadow_runner_replay_is_byte_equivalent() -> None:
    first = run_shadow_date(TARGET, _after_close(), _store(), _provider())
    second = run_shadow_date(TARGET, _after_close(), _store(), _provider())
    assert first.canonical_json() == second.canonical_json()
```

- [ ] **Step 2: Run shadow-runner tests and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_run_shadow_daily.py -q`

Expected: FAIL because daily shadow orchestration is absent.

- [ ] **Step 3: Implement calendar-aware close processing**

```python
def run_shadow_date(as_of_date: date, now: datetime, store: ShadowStore, provider: AdaptiveMarketDataProvider) -> ShadowRunSummary:
    selection = store.load_active_selection(as_of_date)
    require_after_market_data_cutoff(as_of_date, now)
    execution_date = next_trading_session(as_of_date, provider.load_calendar(as_of_date))
    states = []
    for target in selection.targets:
        bars = provider.load_bars(target.stock_code, selection.data_cutoff - timedelta(days=550), as_of_date)
        require_fresh_bar(target.stock_code, bars, as_of_date)
        states.append(process_target_close(target, bars, store.load_latest_state(target.stock_code), execution_date))
    return store.persist_run(build_shadow_run(selection, as_of_date, execution_date, states))
```

Reject future/historical mode confusion, missing previous state after activation, stale/duplicate bars, adjustment-ratio discontinuities without an action, config mismatches, and non-trading dates. Do not import `xtquant`, broker clients, or any order API.

- [ ] **Step 4: Run shadow-runner and backtest scenario tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_run_shadow_daily.py tests/asset_allocation/etf_adaptive/test_engine_scenarios.py -q`

Expected: PASS.

- [ ] **Step 5: Commit the daily runner**

```powershell
git add src/asset_allocation/etf_adaptive/run_shadow_daily.py tests/asset_allocation/etf_adaptive/test_run_shadow_daily.py
git commit -m "feat: run adaptive ETF shadow signals daily"
```

### Task 4: Add daily reports and 60-session readiness verification

**Files:**
- Create: `src/asset_allocation/etf_adaptive/shadow_report.py`
- Create: `src/asset_allocation/etf_adaptive/verify_shadow.py`
- Test: `tests/asset_allocation/etf_adaptive/test_shadow_report.py`
- Test: `tests/asset_allocation/etf_adaptive/test_verify_shadow.py`

**Interfaces:**
- Produces: `render_daily_report(run)`, `verify_shadow_period(start_date, end_date, store) -> ShadowReadiness`, and CLI exit 0 only when all gates pass.
- Consumes: persisted runs, advice, observed next-open fills, health checks, and frozen configuration.

- [ ] **Step 1: Write failing traceability and readiness tests**

```python
def test_daily_report_contains_state_risk_and_order_trace() -> None:
    report = render_daily_report(_run_with_buy_advice())
    assert "GRID" in report
    assert "grid_anchor" in report
    assert "execution_eligible_date" in report
    assert "config_hash" in report


def test_readiness_requires_sixty_complete_sessions_and_reproducible_signals() -> None:
    result = verify_shadow_period(START, END, _store_with_sessions(59))
    assert result.ready is False
    assert "complete_sessions_lt_60" in result.failures
```

- [ ] **Step 2: Run report/readiness tests and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_shadow_report.py tests/asset_allocation/etf_adaptive/test_verify_shadow.py -q`

Expected: FAIL because reports and readiness verification are absent.

- [ ] **Step 3: Implement Chinese daily report and explicit readiness gates**

```python
READINESS_GATES = (
    "complete_sessions_gte_60",
    "signal_reproducibility_eq_1",
    "state_continuity_eq_1",
    "future_data_violations_eq_0",
    "unexplained_config_changes_eq_0",
    "observed_slippage_within_5bp_scenario",
)
```

Render one summary plus per-target state, indicators, anchors, stops, position/cash, blocked reasons, and T+1 advice. Verification must report every failed gate, never collapse failures into one boolean, and must not label readiness as permission to auto-trade.

- [ ] **Step 4: Run all adaptive-strategy tests and repository checks**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive -q`

Expected: PASS.

Run: `git diff --check`

Expected: exit 0.

- [ ] **Step 5: Commit shadow reports and verifier**

```powershell
git add src/asset_allocation/etf_adaptive/shadow_report.py src/asset_allocation/etf_adaptive/verify_shadow.py tests/asset_allocation/etf_adaptive/test_shadow_report.py tests/asset_allocation/etf_adaptive/test_verify_shadow.py
git commit -m "feat: verify adaptive ETF shadow readiness"
```
