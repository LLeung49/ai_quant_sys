# ETF Adaptive Strategy Data Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a point-in-time domestic-equity-ETF universe and dual-price market-data boundary that can safely feed the adaptive strategy backtester.

**Architecture:** Add a new `asset_allocation.etf_adaptive` package with immutable data contracts, injectable read-only providers, deterministic ETF eligibility, and a CLI audit. Reuse the repository database adapter and authoritative trading-calendar loader, but do not reuse sector-candidate selection rules.

**Tech Stack:** Python 3.11+, dataclasses, pandas, PyMySQL through `data_ingestion.db_config.execute_query`, pytest.

**Spec:** `docs/user_demand/asset-allocation-strategy/防御与宽基ETF层自适应网格+趋势策略-回测规格-v1.md`

## Global Constraints

- Upstream tables are read-only: `trade_stock_daily_raw`, `trade_stock_daily_qfq`, `trade_stock_daily_bfq`, `trade_stock_status`, and the existing corporate-action table.
- Include only ordinary mainland domestic-equity ETFs; exclude bond, money-market, commodity, cross-border/QDII, leveraged, and inverse products.
- Eligibility is point-in-time: listing age at least 252 trading sessions and trailing-20-session average amount at least CNY 10,000,000.
- Signal prices and persisted trigger levels use one adjusted coordinate; orders, lots, commission, and cash use raw prices.
- Never substitute a nearby entity bar for a missing requested trading date.
- No writes to production research tables in this plan.

---

### Task 1: Create immutable market-data and universe contracts

**Files:**
- Create: `src/asset_allocation/__init__.py`
- Create: `src/asset_allocation/etf_adaptive/__init__.py`
- Create: `src/asset_allocation/etf_adaptive/contracts.py`
- Test: `tests/asset_allocation/etf_adaptive/test_contracts.py`

**Interfaces:**
- Produces: `DualPriceBar`, `CorporateAction`, `ETFMetadata`, `ETFEligibility`, and `DataQualityIssue` dataclasses plus `DataQualityError`.
- Consumes: standard-library `date`, `Decimal`, and `Enum` only.

- [x] **Step 1: Write the failing contracts test**

```python
from datetime import date

import pytest

from asset_allocation.etf_adaptive.contracts import DualPriceBar


def test_dual_price_bar_rejects_non_positive_prices() -> None:
    with pytest.raises(ValueError, match="prices must be positive"):
        DualPriceBar(
            stock_code="510300.SH", trade_date=date(2026, 9, 1),
            signal_open=0.0, signal_high=1.0, signal_low=0.9, signal_close=1.0,
            raw_open=4.0, raw_high=4.1, raw_low=3.9, raw_close=4.0,
            amount=20_000_000.0, suspended=False, adjustment_ratio=0.25,
        )
```

- [x] **Step 2: Run the test and verify the missing module failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_contracts.py -q`

Expected: FAIL because `asset_allocation.etf_adaptive.contracts` does not exist.

- [x] **Step 3: Implement the immutable contracts**

```python
@dataclass(frozen=True)
class DualPriceBar:
    stock_code: str
    trade_date: date
    signal_open: float
    signal_high: float
    signal_low: float
    signal_close: float
    raw_open: float
    raw_high: float
    raw_low: float
    raw_close: float
    amount: float
    suspended: bool
    adjustment_ratio: float

    def __post_init__(self) -> None:
        prices = (self.signal_open, self.signal_high, self.signal_low, self.signal_close,
                  self.raw_open, self.raw_high, self.raw_low, self.raw_close)
        if any(not math.isfinite(value) or value <= 0 for value in prices):
            raise ValueError("prices must be positive finite numbers")
        if not math.isfinite(self.amount) or self.amount < 0:
            raise ValueError("amount must be a non-negative finite number")
        if not math.isfinite(self.adjustment_ratio) or self.adjustment_ratio <= 0:
            raise ValueError("adjustment_ratio must be positive")
```

Add similarly validated frozen contracts for metadata, corporate actions, eligibility decisions, and structured quality issues. Export them from `etf_adaptive.__init__`.

- [x] **Step 4: Run the contracts tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_contracts.py -q`

Expected: PASS.

- [x] **Step 5: Commit the contracts**

```powershell
git add src/asset_allocation tests/asset_allocation/etf_adaptive/test_contracts.py
git commit -m "feat: add adaptive ETF data contracts"
```

### Task 2: Implement deterministic domestic-equity ETF classification and eligibility

**Files:**
- Create: `src/asset_allocation/etf_adaptive/universe.py`
- Test: `tests/asset_allocation/etf_adaptive/test_universe.py`

**Interfaces:**
- Consumes: `ETFMetadata`, daily amount/date sequences.
- Produces: `classify_etf(metadata: ETFMetadata) -> str | None` and `evaluate_eligibility(metadata, bars, as_of_date) -> ETFEligibility`.

- [x] **Step 1: Write failing classification and point-in-time tests**

```python
def test_cross_border_and_bond_funds_are_excluded() -> None:
    assert classify_etf(_metadata("513100.SH", "纳指ETF")) is None
    assert classify_etf(_metadata("511010.SH", "国债ETF")) is None
    assert classify_etf(_metadata("510300.SH", "沪深300ETF")) == "core_broad"


def test_eligibility_uses_only_bars_available_on_as_of_date() -> None:
    bars = _amount_bars(253, 12_000_000.0) + [_bar(date(2026, 9, 2), 0.0)]
    result = evaluate_eligibility(_metadata("510300.SH", "沪深300ETF"), bars, date(2026, 9, 1))
    assert result.eligible is True
    assert result.history_sessions == 253
    assert result.avg_amount_20 == 12_000_000.0
```

- [x] **Step 2: Run the universe tests and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_universe.py -q`

Expected: FAIL because `classify_etf` and `evaluate_eligibility` are absent.

- [x] **Step 3: Implement explicit classification and eligibility rules**

```python
EXCLUDED_NAME_TOKENS = ("债", "货币", "现金", "黄金", "白银", "原油", "商品", "纳指", "标普", "恒生", "跨境", "QDII", "反向", "杠杆")


def evaluate_eligibility(metadata: ETFMetadata, bars: Sequence[DualPriceBar], as_of_date: date) -> ETFEligibility:
    observed = sorted((bar for bar in bars if bar.trade_date <= as_of_date), key=lambda bar: bar.trade_date)
    category = classify_etf(metadata)
    reasons: list[str] = []
    if category is None:
        reasons.append("not_domestic_equity_etf")
    if len(observed) < 252:
        reasons.append("listing_history_lt_252")
    avg_amount = mean(bar.amount for bar in observed[-20:]) if len(observed) >= 20 else None
    if avg_amount is None or avg_amount < 10_000_000:
        reasons.append("avg_amount_20_lt_10000000")
    latest_ok = bool(observed and observed[-1].trade_date == as_of_date and not observed[-1].suspended)
    if not latest_ok:
        reasons.append("latest_bar_untradable")
    return ETFEligibility(not reasons, tuple(reasons), category, len(observed), avg_amount)
```

Use code prefixes only to identify exchange-listed funds; use metadata fields (`fund_type`, `tracking_index_code`, `tracking_index_name`, `is_cross_border`, `is_leveraged`) as authoritative exclusions. Name tokens are a fail-closed fallback and must add a provenance reason.

- [x] **Step 4: Run the universe tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_universe.py -q`

Expected: PASS.

- [x] **Step 5: Commit the universe provider**

```powershell
git add src/asset_allocation/etf_adaptive/universe.py tests/asset_allocation/etf_adaptive/test_universe.py
git commit -m "feat: build point-in-time ETF universe"
```

### Task 3: Load aligned raw and adjusted bars without date substitution

**Files:**
- Create: `src/asset_allocation/etf_adaptive/market_data.py`
- Test: `tests/asset_allocation/etf_adaptive/test_market_data.py`

**Interfaces:**
- Produces: `AdaptiveMarketDataProvider.load_bars(stock_code, start_date, end_date) -> tuple[DualPriceBar, ...]`, `load_metadata(as_of_date)`, and `load_actions(stock_code, start_date, end_date)`.
- Consumes: injected `query(sql, params)` callable; `trade_stock_daily_raw`, `trade_stock_daily_qfq`, `trade_stock_status`, and corporate-action rows.

- [x] **Step 1: Write failing alignment and conversion tests**

```python
def test_provider_rejects_dates_missing_from_either_price_coordinate() -> None:
    provider = AdaptiveMarketDataProvider(query=_query_with_qfq_gap())
    with pytest.raises(DataQualityError, match="raw/qfq date mismatch"):
        provider.load_bars("510300.SH", date(2026, 8, 1), date(2026, 9, 1))


def test_signal_coordinate_round_trip_uses_same_day_ratio() -> None:
    bar = _dual_bar(signal_close=1.0, raw_close=4.0, adjustment_ratio=0.25)
    assert to_signal_price(4.08, bar.adjustment_ratio) == pytest.approx(1.02)
    assert to_raw_distance(0.05, bar.adjustment_ratio) == pytest.approx(0.20)
```

- [x] **Step 2: Run the market-data tests and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_market_data.py -q`

Expected: FAIL because the provider and conversion functions are absent.

- [x] **Step 3: Implement one-query-per-table loading and strict joins**

```python
def to_signal_price(raw_price: float, adjustment_ratio: float) -> float:
    return raw_price * adjustment_ratio


def to_raw_distance(signal_distance: float, adjustment_ratio: float) -> float:
    return signal_distance / adjustment_ratio


def _align_rows(raw_rows: Sequence[Mapping[str, object]], qfq_rows: Sequence[Mapping[str, object]]) -> tuple[DualPriceBar, ...]:
    raw = {_as_date(row["trade_date"]): row for row in raw_rows}
    qfq = {_as_date(row["trade_date"]): row for row in qfq_rows}
    if raw.keys() != qfq.keys():
        raise DataQualityError("raw/qfq date mismatch")
    return tuple(_make_dual_bar(raw[day], qfq[day]) for day in sorted(raw))
```

Calculate the same-day adjustment ratio from valid raw and adjusted closes; require the OHLC ratios to agree within a configured numeric tolerance. Carry `suspend_flag`, `pre_close`, `amount`, and `adjustment_asof` provenance into the returned bar/quality metadata.

- [x] **Step 4: Run focused and existing projection tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_market_data.py tests/test_price_projection_store.py tests/test_price_corporate_actions.py -q`

Expected: PASS.

- [x] **Step 5: Commit the market-data provider**

```powershell
git add src/asset_allocation/etf_adaptive/market_data.py tests/asset_allocation/etf_adaptive/test_market_data.py
git commit -m "feat: add dual-price ETF market data provider"
```

### Task 4: Add a read-only universe/data audit CLI

**Files:**
- Create: `src/asset_allocation/etf_adaptive/run_data_audit.py`
- Test: `tests/asset_allocation/etf_adaptive/test_run_data_audit.py`

**Interfaces:**
- Produces: `audit_universe(as_of_date, provider) -> AuditReport` and CLI arguments `--as-of-date`, `--output-json`.
- Consumes: Tasks 1-3 providers; writes only the explicitly requested local JSON report.

- [x] **Step 1: Write the failing audit test**

```python
def test_audit_reports_eligible_and_rejected_counts(tmp_path: Path) -> None:
    output = tmp_path / "audit.json"
    report = audit_universe(date(2026, 9, 1), _provider_fixture(), output_path=output)
    assert report.eligible_count == 1
    assert report.rejected_by_reason["not_domestic_equity_etf"] == 1
    assert json.loads(output.read_text(encoding="utf-8"))["as_of_date"] == "2026-09-01"
```

- [x] **Step 2: Run the audit test and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_run_data_audit.py -q`

Expected: FAIL because `audit_universe` is absent.

- [x] **Step 3: Implement deterministic JSON output and fail-closed exit codes**

```python
def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    report = audit_universe(date.fromisoformat(args.as_of_date), default_provider(), Path(args.output_json))
    print(json.dumps(asdict(report), ensure_ascii=False, sort_keys=True))
    return 0 if report.data_quality_error_count == 0 else 2
```

Sort all codes and reason keys before serialization. Include date coverage, raw/qfq mismatch counts, stale adjustment versions, eligible counts by exposure group, rejection counts, and examples capped at ten codes per reason.

- [x] **Step 4: Run the complete data-foundation test slice**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_contracts.py tests/asset_allocation/etf_adaptive/test_universe.py tests/asset_allocation/etf_adaptive/test_market_data.py tests/asset_allocation/etf_adaptive/test_run_data_audit.py -q`

Expected: PASS.

- [x] **Step 5: Commit the audit CLI**

```powershell
git add src/asset_allocation/etf_adaptive/run_data_audit.py tests/asset_allocation/etf_adaptive/test_run_data_audit.py
git commit -m "feat: audit adaptive ETF research data"
```
