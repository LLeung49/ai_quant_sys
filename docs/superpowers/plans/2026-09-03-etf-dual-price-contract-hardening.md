# ETF 双价格契约补强 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make ETF adaptive data contracts explicit and safe for adjusted-signal versus raw-execution conversions, and give later company-action accounting a stable event identity.

**Architecture:** Retain `DualPriceBar.signal_*` and `raw_*`. Add the sole missing inverse price converter and a derived `CorporateAction.event_id`, then correct the deferred backtest-core plan so it turns indicator-space ATR into a raw distance with the T+1 bar ratio before creating real-price orders.

**Tech Stack:** Python standard library, pytest, Markdown.

**Spec:** `docs/superpowers/specs/2026-09-03-etf-dual-price-contract-hardening-design.md`

## Global Constraints

- `signal_*` is adjusted OHLC for research returns and technical indicators only.
- `raw_*` is unadjusted OHLC for fills, lots, costs, cash, NAV, and monetary risk only.
- An ATR or other signal distance must call `to_raw_distance(distance, next_bar.adjustment_ratio)` before a raw-price calculation.
- Do not implement a ledger, engine, execution simulator, schema migration, or unsupported action type.

---

### Task 1: Add inverse-price conversion and stable action identity

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/market_data.py:152-170`
- Modify: `src/asset_allocation/etf_adaptive/contracts.py:111-130`
- Modify: `tests/asset_allocation/etf_adaptive/test_market_data.py`
- Modify: `tests/asset_allocation/etf_adaptive/test_contracts.py`

**Interfaces:**
- Consumes: `_positive_finite`, `to_signal_price`, `CorporateAction`, `CorporateActionType`.
- Produces: `to_raw_price(signal_price: float, adjustment_ratio: float) -> float` and read-only `CorporateAction.event_id: str`.
- Contract: `to_raw_price(to_signal_price(raw, ratio), ratio)` restores `raw`; `event_id` is `stock_code:YYYY-MM-DD:action_type`.

- [ ] **Step 1: Write failing tests**

```python
def test_signal_and_raw_price_conversion_is_a_round_trip() -> None:
    assert to_signal_price(4.08, 0.25) == pytest.approx(1.02)
    assert to_raw_price(1.02, 0.25) == pytest.approx(4.08)


def test_corporate_action_event_ids_are_stable_and_distinguish_types() -> None:
    cash = CorporateAction("510300.SH", date(2026, 9, 1), CorporateActionType.CASH_DIVIDEND, Decimal("0.10"), Decimal("1"))
    split = CorporateAction("510300.SH", date(2026, 9, 1), CorporateActionType.SHARE_SPLIT, None, Decimal("1.10"))
    assert cash.event_id == "510300.SH:2026-09-01:cash_dividend"
    assert split.event_id == "510300.SH:2026-09-01:share_split"
    assert cash.event_id != split.event_id
```

- [ ] **Step 2: Run the tests to verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_market_data.py tests/asset_allocation/etf_adaptive/test_contracts.py -q`

Expected: FAIL because `to_raw_price` and `event_id` are absent.

- [ ] **Step 3: Implement the smallest compatible API**

```python
def to_raw_price(signal_price: float, adjustment_ratio: float) -> float:
    signal = _positive_finite(signal_price, "signal_price")
    ratio = _positive_finite(adjustment_ratio, "adjustment_ratio")
    result = signal / ratio
    if not math.isfinite(result):
        raise ValueError("result must be finite")
    return result


@property
def event_id(self) -> str:
    return f"{self.stock_code}:{self.effective_date.isoformat()}:{self.action_type.value}"
```

Do not add a dataclass field, change action constructors, or change `ACTIONS_SQL`.

- [ ] **Step 4: Run focused regression tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_market_data.py tests/asset_allocation/etf_adaptive/test_contracts.py -q`

Expected: PASS.

- [ ] **Step 5: Commit**

```powershell
git add src/asset_allocation/etf_adaptive/market_data.py src/asset_allocation/etf_adaptive/contracts.py tests/asset_allocation/etf_adaptive/test_market_data.py tests/asset_allocation/etf_adaptive/test_contracts.py
git commit -m "feat: harden ETF dual-price contracts"
```

### Task 2: Correct the deferred backtest-core ATR bridge

**Files:**
- Modify: `docs/superpowers/plans/2026-09-02-etf-adaptive-backtest-core.md:233-270`
- Modify: `docs/superpowers/plans/2026-09-02-etf-adaptive-backtest-core.md:285-333`

**Interfaces:**
- Consumes: `IndicatorSnapshot.atr20` in signal coordinate, T+1 `DualPriceBar.adjustment_ratio`, `to_raw_distance`, `to_raw_price`, and `CorporateAction.event_id`.
- Produces: exact future implementation instructions requiring conversion before raw order sizing, raw stop price construction, and action de-duplication.

- [ ] **Step 1: Replace the raw-ATR test example**

```python
def test_unit_size_converts_signal_atr_using_next_execution_ratio() -> None:
    signal_atr20 = 0.05
    raw_atr20 = to_raw_distance(signal_atr20, adjustment_ratio=0.25)
    assert raw_atr20 == pytest.approx(0.20)
    assert calculate_unit_shares(120_000, 0.005, raw_atr20, stop_n=2.0) == 1_500
```

State immediately below it that signal ATR `0.05` must never directly enter a raw-price order calculation.

- [ ] **Step 2: Replace the ambiguous sizing example**

```python
def calculate_unit_shares(budget: float, risk_per_unit: float, raw_atr20: float, stop_n: float) -> int:
    stop_distance = stop_n * raw_atr20
    return 0 if stop_distance <= 0 else max(0, int((budget * risk_per_unit / stop_distance) // 100) * 100)

raw_atr20 = to_raw_distance(signal_atr20, next_bar.adjustment_ratio)
shares = calculate_unit_shares(budget, risk_per_unit, raw_atr20, stop_n)
```

Require complete signal price thresholds to use `to_raw_price`; signal-only comparisons remain in the signal coordinate.

- [ ] **Step 3: Specify action de-duplication**

```python
if action.event_id not in applied_action_ids:
    applied_action_ids.add(action.event_id)
```

Specify cash dividends and share multipliers are applied exactly once, preserving exact Decimal and explicit fractional-entitlement policy; do not silently round or discard it.

- [ ] **Step 4: Validate the clarification**

Run: `rg -n "signal_atr20|raw_atr20|to_raw_distance|to_raw_price|event_id" docs/superpowers/plans/2026-09-02-etf-adaptive-backtest-core.md`

Expected: all indicator ATR values are signal-coordinate until explicitly converted, and action application names `event_id`.

- [ ] **Step 5: Commit**

```powershell
git add -f docs/superpowers/plans/2026-09-02-etf-adaptive-backtest-core.md
git commit -m "docs: clarify ETF raw ATR execution bridge"
```

### Task 3: Verify no scope expansion

**Files:**
- Verify: `src/asset_allocation/etf_adaptive/contracts.py`
- Verify: `src/asset_allocation/etf_adaptive/market_data.py`
- Verify: `tests/asset_allocation/etf_adaptive/test_contracts.py`
- Verify: `tests/asset_allocation/etf_adaptive/test_market_data.py`

- [ ] **Step 1: Run the complete ETF data-foundation suite**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_contracts.py tests/asset_allocation/etf_adaptive/test_market_data.py tests/asset_allocation/etf_adaptive/test_universe.py tests/asset_allocation/etf_adaptive/test_run_data_audit.py -q`

Expected: PASS.

- [ ] **Step 2: Run final diff checks**

Run: `git diff --check; git status --short`

Expected: no whitespace errors; no new database, execution, portfolio, or engine module.
