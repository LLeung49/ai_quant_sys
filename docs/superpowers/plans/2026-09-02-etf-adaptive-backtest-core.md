# ETF Adaptive Strategy Backtest Core Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a deterministic daily-bar portfolio simulator implementing the approved GRID/TREND strategy, costs, risk controls, and T+1 execution.

**Architecture:** Implement pure decision engines around immutable state and order-intent contracts, followed by a separate execution simulator. A coordinating engine processes one close at a time in strict priority order and persists enough state for exact replay; Backtrader is not used because its default broker does not express the approved dual-price, delayed-order, minimum-commission, and state-transition semantics cleanly.

**Tech Stack:** Python 3.11+, dataclasses, Enum, numpy, pandas, TA-Lib where already installed, pytest.

**Spec:** `docs/user_demand/asset-allocation-strategy/防御与宽基ETF层自适应网格+趋势策略-回测规格-v1.md`

## Global Constraints

- Requires the contracts and provider from `2026-09-02-etf-adaptive-data-foundation.md`.
- Signals use T-close data and orders execute no earlier than T+1.
- State thresholds are ADX > 25 for TREND, ADX < 20 for GRID, and hysteresis in between.
- Orders are long-only, cash-only, 100-share lots; `max_grid_per_day = 1` and the maximum trend adds per day is one.
- Commission is `max(notional * 0.0001, 5)` per side; baseline slippage is 3 bp with 0/1/5/10 bp scenarios.
- GRID/TREND stops and the 10% hard stop never move down within a cycle.
- Insufficient cash, lot size, eligibility, or stop-risk budget means no order.

---

### Task 1: Define frozen configurations, state, and order contracts

**Files:**
- Create: `src/asset_allocation/etf_adaptive/config.py`
- Create: `src/asset_allocation/etf_adaptive/state.py`
- Test: `tests/asset_allocation/etf_adaptive/test_strategy_contracts.py`

**Interfaces:**
- Produces: `AdaptiveConfig`, `GridConfig`, `TrendConfig`, `CostConfig`, `StrategyState`, `TrendUnit`, `OrderIntent`, `OrderReason`, `Side`, `Regime`, `Decision`, `Fill`, `ExecutionResult`, `BacktestRequest`, `BacktestEvent`, `DailyNav`, `BacktestResult`, and canonical `config_hash()`.
- Consumes: `DualPriceBar` from the data-foundation plan.

- [ ] **Step 1: Write failing validation and hash tests**

```python
def test_config_hash_is_stable_and_rejects_unsafe_limits() -> None:
    left = AdaptiveConfig.default()
    right = AdaptiveConfig.default()
    assert left.config_hash() == right.config_hash()
    with pytest.raises(ValueError, match="max_grid_per_day must equal 1"):
        replace(left, grid=replace(left.grid, max_grid_per_day=2))
```

- [ ] **Step 2: Run the strategy-contract tests and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_strategy_contracts.py -q`

Expected: FAIL because configuration and state contracts are absent.

- [ ] **Step 3: Implement typed configuration and canonical hashing**

```python
@dataclass(frozen=True)
class GridConfig:
    step_pct: float
    unit_pct: float
    initial_model: str
    fixed_initial_pct: float | None
    max_grid_per_day: int = 1
    atr_stop_multiple: float = 3.0
    cooldown_sessions: int = 5


@dataclass(frozen=True)
class StrategyState:
    regime: Regime | None = None
    pending_grid: bool = False
    grid_anchor: float | None = None
    cycle_entry_price: float | None = None
    grid_stop_price: float | None = None
    trend_stop_price: float | None = None
    highest_close: float | None = None
    units: tuple[TrendUnit, ...] = ()
    cooldown_remaining: int = 0
    position_shares: int = 0
    cash: Decimal = Decimal("0")
```

Serialize enums, decimals, dates, tuples, and mappings into sorted canonical JSON before SHA-256 hashing.

- [ ] **Step 4: Run strategy-contract tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_strategy_contracts.py -q`

Expected: PASS.

- [ ] **Step 5: Commit the strategy contracts**

```powershell
git add src/asset_allocation/etf_adaptive/config.py src/asset_allocation/etf_adaptive/state.py tests/asset_allocation/etf_adaptive/test_strategy_contracts.py
git commit -m "feat: define adaptive strategy state contracts"
```

### Task 2: Implement indicators and ADX hysteresis

**Files:**
- Create: `src/asset_allocation/etf_adaptive/indicators.py`
- Create: `src/asset_allocation/etf_adaptive/regime.py`
- Test: `tests/asset_allocation/etf_adaptive/test_indicators.py`
- Test: `tests/asset_allocation/etf_adaptive/test_regime.py`

**Interfaces:**
- Produces: `IndicatorSnapshot`, `compute_indicators(bars)`, and `next_regime(previous, adx) -> Regime | None`.
- Consumes: signal-coordinate OHLC and amount; Hurst is recorded but never read by `next_regime`.

- [ ] **Step 1: Write failing warm-up, prior-channel, and hysteresis tests**

```python
@pytest.mark.parametrize(
    ("previous", "adx", "expected"),
    [(None, 22.0, None), (None, 19.0, Regime.GRID), (None, 26.0, Regime.TREND),
     (Regime.GRID, 23.0, Regime.GRID), (Regime.TREND, 23.0, Regime.TREND)],
)
def test_adx_hysteresis(previous, adx, expected) -> None:
    assert next_regime(previous, adx) == expected


def test_donchian_channels_exclude_current_bar() -> None:
    snapshot = compute_indicators(_bars_with_last_day_breakout())[-1]
    assert snapshot.close > snapshot.prior_high_20
```

- [ ] **Step 2: Run indicator/regime tests and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_indicators.py tests/asset_allocation/etf_adaptive/test_regime.py -q`

Expected: FAIL because the indicator and regime modules are absent.

- [ ] **Step 3: Implement deterministic calculations**

```python
def next_regime(previous: Regime | None, adx: float) -> Regime | None:
    if adx > 25:
        return Regime.TREND
    if adx < 20:
        return Regime.GRID
    return previous
```

Use MACD (12, 26, 9), ADX14, ATR20, MA20, population-standard-deviation Bollinger bands, prior 20-day high, prior 10-day low, amount ratio against the prior 20 sessions, 252-session price percentile, and a research-only Hurst value. Return `None` snapshots until all required inputs are warm.

- [ ] **Step 4: Run indicator/regime tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_indicators.py tests/asset_allocation/etf_adaptive/test_regime.py -q`

Expected: PASS.

- [ ] **Step 5: Commit indicators and regime logic**

```powershell
git add src/asset_allocation/etf_adaptive/indicators.py src/asset_allocation/etf_adaptive/regime.py tests/asset_allocation/etf_adaptive/test_indicators.py tests/asset_allocation/etf_adaptive/test_regime.py
git commit -m "feat: calculate adaptive ETF market regime"
```

### Task 3: Implement GRID decisions and monotone risk state

**Files:**
- Create: `src/asset_allocation/etf_adaptive/grid.py`
- Test: `tests/asset_allocation/etf_adaptive/test_grid.py`

**Interfaces:**
- Produces: `initial_grid_target_pct(snapshot, config)`, `evaluate_grid_close(state, snapshot, eligible) -> Decision`, and `apply_grid_fill(state, fill) -> StrategyState`.
- Consumes: `StrategyState`, `IndicatorSnapshot`, `GridConfig`, and `OrderIntent`.

- [ ] **Step 1: Write failing initialization, anchor, lower-band, and gap tests**

```python
def test_grid_anchor_moves_only_after_fill_and_gap_creates_one_order() -> None:
    state = _grid_state(anchor=1.00, position_pct=0.50)
    decision = evaluate_grid_close(state, _snapshot(close=0.94, lower=0.90), eligible=True)
    assert len(decision.orders) == 1
    assert decision.state.grid_anchor == 1.00
    filled = apply_grid_fill(decision.state, _fill(signal_price=0.94))
    assert filled.grid_anchor == 0.94


def test_grid_does_not_buy_below_lower_band_but_can_sell() -> None:
    assert evaluate_grid_close(_grid_state(anchor=1.00), _snapshot(close=0.89, lower=0.90), True).orders == ()
    assert evaluate_grid_close(_grid_state(anchor=0.80), _snapshot(close=0.89, lower=0.90), True).orders[0].side is Side.SELL
```

- [ ] **Step 2: Run GRID tests and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_grid.py -q`

Expected: FAIL because GRID functions are absent.

- [ ] **Step 3: Implement approved GRID semantics**

```python
def next_grid_stop(previous: float | None, highest_close: float, atr20: float) -> float:
    candidate = highest_close - 3.0 * atr20
    return candidate if previous is None else max(previous, candidate)


def initial_grid_target_pct(snapshot: IndicatorSnapshot, config: GridConfig) -> float:
    if config.initial_model == "bollinger_position":
        location = min(1.0, max(-1.0, (snapshot.close - snapshot.ma20) / (2.0 * snapshot.std20)))
        return 0.50 - 0.20 * location
    if config.initial_model == "price_percentile_252":
        return 0.70 - 0.10 * min(4, int(snapshot.price_percentile_252 * 5))
    assert config.fixed_initial_pct is not None
    return config.fixed_initial_pct
```

Generate at most one order, clamp target exposure to [0, 1], require a full 100-share lot, initialize a new cycle only after its fill, and preserve a risk-reducing sell even when eligibility has failed.

- [ ] **Step 4: Run GRID tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_grid.py -q`

Expected: PASS.

- [ ] **Step 5: Commit GRID logic**

```powershell
git add src/asset_allocation/etf_adaptive/grid.py tests/asset_allocation/etf_adaptive/test_grid.py
git commit -m "feat: implement adaptive grid decisions"
```

### Task 4: Implement TREND entry, sizing, pyramiding, and exit

**Files:**
- Create: `src/asset_allocation/etf_adaptive/trend.py`
- Test: `tests/asset_allocation/etf_adaptive/test_trend.py`

**Interfaces:**
- Produces: `trend_entry_allowed`, `calculate_unit_shares`, `evaluate_trend_close`, and `apply_trend_fill`.
- Consumes: frozen config/state/snapshot contracts.

- [ ] **Step 1: Write failing risk-size and exit-priority tests**

```python
def test_unit_size_converts_signal_atr_using_next_execution_ratio() -> None:
    signal_atr20 = 0.05
    raw_atr20 = to_raw_distance(signal_atr20, adjustment_ratio=0.25)
    assert raw_atr20 == pytest.approx(0.20)
    assert calculate_unit_shares(120_000, 0.005, raw_atr20, stop_n=2.0) == 1_500


def test_trend_exit_wins_over_add_signal() -> None:
    decision = evaluate_trend_close(_trend_state(), _snapshot(stop_hit=True, add_hit=True), eligible=True)
    assert decision.orders == (_full_exit(OrderReason.TREND_STOP),)
```

Signal ATR `0.05` must never directly enter a raw-price order calculation; `IndicatorSnapshot.atr20` remains in signal coordinates until converted at T+1 using that execution bar's adjustment ratio.

- [ ] **Step 2: Run TREND tests and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_trend.py -q`

Expected: FAIL because TREND functions are absent.

- [ ] **Step 3: Implement entry, units, adds, and exits**

```python
def calculate_unit_shares(budget: float, risk_per_unit: float, raw_atr20: float, stop_n: float) -> int:
    stop_distance = stop_n * raw_atr20
    return 0 if stop_distance <= 0 else max(0, int((budget * risk_per_unit / stop_distance) // 100) * 100)

raw_atr20 = to_raw_distance(signal_atr20, next_bar.adjustment_ratio)
shares = calculate_unit_shares(budget, risk_per_unit, raw_atr20, stop_n)


def trend_entry_allowed(snapshot: IndicatorSnapshot, config: TrendConfig) -> bool:
    base = snapshot.adx > 25 and snapshot.close > snapshot.prior_high_20
    macd_ok = not config.require_macd_bullish or snapshot.dif > snapshot.dea
    amount_ok = config.amount_ratio_min is None or snapshot.amount_ratio >= config.amount_ratio_min
    return base and macd_ok and amount_ok
```

Complete signal price thresholds must use `to_raw_price`; signal-only comparisons remain in the signal coordinate.

Store each unit's actual fill, signal-coordinate fill, signal-day ATR, shares, and next-add reference. Implement one-add-per-day, aggregate stop-risk cap `budget * risk_per_unit * max_units`, monotone stops, prior-10-low exit, and exact MACD dead-cross exit.

- [ ] **Step 4: Run TREND tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_trend.py -q`

Expected: PASS.

- [ ] **Step 5: Commit TREND logic**

```powershell
git add src/asset_allocation/etf_adaptive/trend.py tests/asset_allocation/etf_adaptive/test_trend.py
git commit -m "feat: implement ATR trend campaign"
```

### Task 5: Implement execution costs, fills, and corporate-action rebasing

**Files:**
- Create: `src/asset_allocation/etf_adaptive/execution.py`
- Test: `tests/asset_allocation/etf_adaptive/test_execution.py`

**Interfaces:**
- Produces: `ExecutionSimulator.execute(intents, next_bar, state) -> ExecutionResult` and `rebase_signal_state(state, old_ratio, new_ratio)`.
- Consumes: raw next-open data, signal/raw adjustment ratio, corporate actions, commission/slippage config.

- [ ] **Step 1: Write failing cost, lot, failed-fill, and rebasing tests**

```python
def test_minimum_commission_and_three_bp_slippage() -> None:
    fill = _simulator(slippage_bps=3).buy(_intent(shares=1000), _bar(raw_open=10.0))
    assert fill.price == pytest.approx(10.003)
    assert fill.commission == Decimal("5.00")


def test_signal_levels_rebase_without_changing_raw_cost_basis() -> None:
    state = _state(grid_anchor=1.0, raw_cost=4.0)
    rebased = rebase_signal_state(state, old_ratio=0.25, new_ratio=0.20)
    assert rebased.grid_anchor == pytest.approx(0.8)
    assert rebased.raw_average_cost == 4.0
```

- [ ] **Step 2: Run execution tests and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_execution.py -q`

Expected: FAIL because execution simulation is absent.

- [ ] **Step 3: Implement conservative execution**

```python
def commission(notional: Decimal, rate: Decimal = Decimal("0.0001"), minimum: Decimal = Decimal("5")) -> Decimal:
    return max(notional * rate, minimum).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def slipped_open(raw_open: float, side: Side, bps: float) -> float:
    multiplier = 1 + bps / 10_000 if side is Side.BUY else 1 - bps / 10_000
    return raw_open * multiplier
```

Reject fills for suspension, zero amount, exchange-limit lock, insufficient cash/shares, and pre-fill risk failure. De-duplicate corporate actions by event ID:

```python
if action.event_id not in applied_action_ids:
    applied_action_ids.add(action.event_id)
```

Apply cash dividends and share multipliers exactly once, preserving exact `Decimal` arithmetic and an explicit fractional-entitlement policy; do not silently round or discard fractional entitlements. This plan specifies the contract only; no action-processing engine is implemented here.

- [ ] **Step 4: Run execution plus data-coordinate tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_execution.py tests/asset_allocation/etf_adaptive/test_market_data.py -q`

Expected: PASS.

- [ ] **Step 5: Commit execution simulation**

```powershell
git add src/asset_allocation/etf_adaptive/execution.py tests/asset_allocation/etf_adaptive/test_execution.py
git commit -m "feat: simulate executable ETF orders"
```

### Task 6: Integrate the daily engine and approved mode transitions

**Files:**
- Create: `src/asset_allocation/etf_adaptive/engine.py`
- Test: `tests/asset_allocation/etf_adaptive/test_engine.py`
- Test: `tests/asset_allocation/etf_adaptive/test_engine_scenarios.py`

**Interfaces:**
- Produces: `AdaptiveBacktestEngine.run(request: BacktestRequest) -> BacktestResult` and `process_close(state, snapshot, eligibility) -> Decision`.
- Consumes: all previous backtest-core modules and data-foundation providers.

- [ ] **Step 1: Write failing end-to-end transition tests**

```python
def test_grid_to_trend_reuses_inventory_but_trims_to_risk_unit() -> None:
    result = _run_scenario("grid_to_bullish_trend")
    transition = result.events.by_reason(OrderReason.GRID_TO_TREND_REBALANCE)
    assert transition.sell_then_buy_round_trip is False
    assert transition.ending_shares == result.events.first_trend_unit_shares


def test_trend_to_grid_waits_for_exit_fill_before_initializing() -> None:
    result = _run_scenario("trend_to_grid")
    assert result.events.grid_initialization.signal_date > result.events.trend_exit.fill_date
```

- [ ] **Step 2: Run engine scenarios and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_engine.py tests/asset_allocation/etf_adaptive/test_engine_scenarios.py -q`

Expected: FAIL because the coordinating engine is absent.

- [ ] **Step 3: Implement strict event sequencing**

```python
def process_close(state: StrategyState, snapshot: IndicatorSnapshot, eligibility: ETFEligibility, config: AdaptiveConfig) -> Decision:
    stop_decision = evaluate_global_stop(state, snapshot, config)
    if stop_decision.orders:
        return stop_decision
    requested_regime = next_regime(state.regime, snapshot.adx)
    if state.regime is Regime.TREND and state.position_shares and requested_regime is Regime.GRID:
        state = replace(state, pending_grid=True)
        return evaluate_trend_close(state, snapshot, eligibility.eligible, allow_add=False)
    if state.regime is Regime.GRID and requested_regime is Regime.TREND:
        return transition_grid_to_trend(state, snapshot, eligibility, config)
    return evaluate_active_mode(state, snapshot, eligibility, config)
```

Process pending T+1 orders before the next close, maintain a daily NAV/event ledger, initialize GRID only after the prior TREND exit has filled, and preserve cycle hard-stop identity through GRID-to-TREND takeover.

- [ ] **Step 4: Run all backtest-core tests and static checks**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_strategy_contracts.py tests/asset_allocation/etf_adaptive/test_indicators.py tests/asset_allocation/etf_adaptive/test_regime.py tests/asset_allocation/etf_adaptive/test_grid.py tests/asset_allocation/etf_adaptive/test_trend.py tests/asset_allocation/etf_adaptive/test_execution.py tests/asset_allocation/etf_adaptive/test_engine.py tests/asset_allocation/etf_adaptive/test_engine_scenarios.py -q`

Expected: PASS.

Run: `git diff --check`

Expected: exit 0.

- [ ] **Step 5: Commit the deterministic engine**

```powershell
git add src/asset_allocation/etf_adaptive/engine.py tests/asset_allocation/etf_adaptive/test_engine.py tests/asset_allocation/etf_adaptive/test_engine_scenarios.py
git commit -m "feat: integrate adaptive ETF backtest engine"
```
