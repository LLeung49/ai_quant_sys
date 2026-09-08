"""Fail-closed daily shadow orchestration for the adaptive ETF strategy.

The shadow runner is the production-side counterpart to the historical
backtest engine. It reuses the same indicator, regime, grid, trend,
risk, and execution semantics but wraps them in an idempotent, immutable
daily contract:

* only the active ``FrozenSelection`` is consulted;
* inputs are bounded by data freshness and the trading calendar;
* every state transition and order advice carries the four immutable
  identities required by the spec (``as_of_date``, ``execution_eligible_date``,
  ``model_version``, ``config_hash``);
* the same inputs always produce the same ``ShadowRunSummary``;
* nothing here imports ``xtquant``, broker clients, or any order-placement
  API. The runner emits advice only.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta
from decimal import Decimal
from hashlib import sha256
from typing import Iterable, Mapping, Protocol, Sequence

from .backtest_provider import AdaptiveBacktestDataProvider
from .config import AdaptiveConfig, CostConfig
from .contracts import (
    DualPriceBar,
    ETFEligibility,
    ExecutionAvailability,
    InstrumentType,
    SubLayer,
    asset_layer_for,
)
from .engine import process_close
from .frozen_selection import FrozenTarget
from .indicators import IndicatorSnapshot, compute_indicators
from .shadow_store import (
    AdviceRecord,
    HealthCheck,
    InMemoryShadowStore,
    ShadowRunIdentity,
    ShadowRunRecord,
    ShadowStore,
    StateRecord,
    build_run_record,
)
from .state import (
    Decision,
    OrderIntent,
    Regime,
    StrategyState,
)


def default_shadow_store() -> ShadowStore:
    """Create the durable store used by the command-line entry point."""
    from .mysql_shadow_store import MySQLShadowStore
    return MySQLShadowStore()


def default_shadow_provider() -> _ProviderLike:
    """Create the repository's read-only dual-price market-data provider."""
    from data_ingestion.db_config import execute_query
    from morning_conference.sector_rotation2.research.evaluation.prices import (
        load_authoritative_market_calendar,
    )
    from .market_data import AdaptiveMarketDataProvider
    return AdaptiveMarketDataProvider(
        query=execute_query,
        calendar_loader=lambda start, end: load_authoritative_market_calendar(
            start, end, execute_query,
        ),
    )


MARKET_CLOSE_LOCAL: time = time(15, 0)
SAFE_PROCESSING_CUTOFF: time = time(17, 0)
DATA_FRESHNESS_LOOKBACK_DAYS: int = 550


class DataFreshnessError(RuntimeError):
    """Raised when the bar coverage for the requested date is missing or stale."""


class ConfigMismatchError(RuntimeError):
    """Raised when a frozen config_hash disagrees with the loaded state."""


class PriorStateMissingError(RuntimeError):
    """Raised when prior state is required but absent for an activated target."""


class NonTradingDateError(RuntimeError):
    """Raised when the requested ``as_of_date`` is not on the trading calendar."""


class CutoffNotReachedError(RuntimeError):
    """Raised when the call is made before the safe processing cutoff."""


class ShadowRunnerImportGuard:
    """Static guard listing modules the shadow runner must never import."""


_FORBIDDEN_IMPORT_PREFIXES: tuple[str, ...] = (
    "xtquant",
    "xtdata",
    "broker",
    "order_api",
    "trade_client",
)


def _assert_no_forbidden_imports(imported: Iterable[str]) -> None:
    seen = set(imported)
    for prefix in _FORBIDDEN_IMPORT_PREFIXES:
        if any(name == prefix or name.startswith(prefix + ".") for name in seen):
            raise RuntimeError(
                f"shadow runner must not import {prefix!r} (forbidden per spec)"
            )


@dataclass(frozen=True)
class TargetSpec:
    """A single funded layered target consumed by the advice-only runner.

    The defaults preserve report-only construction by older callers.  A target
    loaded for execution is parsed fail-closed by :func:`_build_active_selection`
    and therefore always supplies the explicit layered fields.
    """

    stock_code: str
    tracking_index_code: str
    layer: str
    weight: Decimal | float
    sub_layer: SubLayer | None = None
    sub_layer_budget: Decimal | None = None
    instrument_type: InstrumentType = InstrumentType.ETF


@dataclass(frozen=True)
class ETFCostBoundary:
    """Existing ETF commission/slippage configuration, kept unchanged."""

    cost: CostConfig


@dataclass(frozen=True)
class ChinaAStockCostBoundary:
    """Date-versioned mainland A-share execution cost schedule.

    Advice does not execute orders.  This boundary makes the stock schedule
    explicit for downstream fill modelling instead of allowing an ETF cost
    configuration to be silently reused.
    """

    effective_date: date
    commission_rate: Decimal
    minimum_commission: Decimal
    stamp_duty_sell_rate: Decimal
    transfer_fee_rate: Decimal


def cost_boundary_for(
    target: TargetSpec, trade_date: date, config: AdaptiveConfig,
) -> ETFCostBoundary | ChinaAStockCostBoundary:
    """Select the instrument-specific, date-valid cost boundary for advice."""

    if target.instrument_type is InstrumentType.ETF:
        return ETFCostBoundary(config.cost)
    if target.instrument_type is InstrumentType.STOCK:
        # China A-share stamp duty has been 0.05% on sells since 2023-08-28;
        # the exchange transfer fee is 0.001% on both sides from 2022-04-29.
        # Earlier dates use the prior statutory schedules rather than today's.
        if trade_date >= date(2023, 8, 28):
            stamp_duty = Decimal("0.0005")
        elif trade_date >= date(2008, 9, 19):
            stamp_duty = Decimal("0.001")
        else:
            stamp_duty = Decimal("0.003")
        transfer_fee = Decimal("0.00001") if trade_date >= date(2022, 4, 29) else Decimal("0.00002")
        return ChinaAStockCostBoundary(
            effective_date=trade_date,
            commission_rate=Decimal("0.0003"),
            minimum_commission=Decimal("5"),
            stamp_duty_sell_rate=stamp_duty,
            transfer_fee_rate=transfer_fee,
        )
    raise ValueError(f"unsupported instrument type for {target.stock_code!r}")


def execution_cost_config_for(
    target: TargetSpec, trade_date: date, config: AdaptiveConfig,
) -> CostConfig:
    """Translate the target-specific boundary into the simulator's cost contract."""

    boundary = cost_boundary_for(target, trade_date, config)
    if isinstance(boundary, ETFCostBoundary):
        return boundary.cost
    return CostConfig(
        commission_rate=float(boundary.commission_rate),
        minimum_commission=float(boundary.minimum_commission),
        slippage_bps=config.cost.slippage_bps,
        sell_tax_rate=float(boundary.stamp_duty_sell_rate),
        transfer_fee_rate=float(boundary.transfer_fee_rate),
    )


@dataclass(frozen=True)
class ActiveSelection:
    """Lightweight view of the active frozen selection."""

    config_hash: str
    config: AdaptiveConfig
    data_cutoff: date
    targets: tuple[TargetSpec, ...]


@dataclass(frozen=True)
class ShadowRunSummary:
    """Aggregated output of one shadow run for every active target."""

    as_of_date: date
    model_version: str
    config_hash: str
    execution_eligible_date: date
    run_id: str
    target_states: tuple[tuple[TargetSpec, StateRecord], ...]
    advices: tuple[AdviceRecord, ...]
    health_checks: tuple[HealthCheck, ...]

    def canonical_json(self) -> str:
        """Deterministic byte-equivalent serialization for replay checks."""

        body = {
            "as_of_date": self.as_of_date.isoformat(),
            "model_version": self.model_version,
            "config_hash": self.config_hash,
            "execution_eligible_date": self.execution_eligible_date.isoformat(),
            "run_id": self.run_id,
            "target_states": [
                {
                    "stock_code": target.stock_code,
                    "tracking_index_code": target.tracking_index_code,
                    "layer": target.layer,
                    "sub_layer": target.sub_layer.value if target.sub_layer else None,
                    "sub_layer_budget": (
                        str(target.sub_layer_budget) if target.sub_layer_budget is not None else None
                    ),
                    "instrument_type": target.instrument_type.value,
                    "weight": str(target.weight),
                    "state": {
                        "as_of_date": state.as_of_date.isoformat(),
                        "config_hash": state.config_hash,
                        "cash": str(state.cash),
                        "position_shares": state.position_shares,
                        "regime": state.regime,
                    },
                }
                for target, state in self.target_states
            ],
            "advices": sorted(
                (
                    {
                        "stock_code": advice.stock_code,
                        "as_of_date": advice.as_of_date.isoformat(),
                        "execution_eligible_date": advice.execution_eligible_date.isoformat(),
                        "signal_date": advice.signal_date.isoformat(),
                        "side": advice.order.side.value,
                        "reason": advice.order.reason.value,
                        "target_budget": advice.order.target_budget,
                        "risk_per_unit": advice.order.risk_per_unit,
                    }
                    for advice in self.advices
                ),
                key=lambda item: (item["stock_code"], item["signal_date"], item["reason"]),
            ),
        }
        import json as _json
        return _json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def derive_run_id(as_of_date: date, model_version: str, config_hash: str, targets: Sequence[TargetSpec]) -> str:
    """Deterministic SHA-256-based UUID-like identifier for one shadow run."""

    payload = (
        as_of_date.isoformat(),
        model_version,
        config_hash,
        ",".join(sorted(target.stock_code for target in targets)),
    )
    digest = sha256("|".join(payload).encode("utf-8")).hexdigest()
    return digest


def require_after_market_data_cutoff(as_of_date: date, now: datetime) -> None:
    """Refuse to run before the safe post-close processing cutoff."""

    if now.date() < as_of_date:
        raise CutoffNotReachedError(
            f"shadow runner called for {as_of_date.isoformat()} before the date itself "
            f"(now={now.isoformat()})"
        )
    if now.date() == as_of_date and now.time() < SAFE_PROCESSING_CUTOFF:
        raise CutoffNotReachedError(
            f"shadow runner must wait until {SAFE_PROCESSING_CUTOFF.isoformat()} "
            f"local time; now={now.isoformat()}"
        )


def next_trading_session(as_of_date: date, trading_dates: Sequence[date]) -> date:
    """Return the first trading date strictly after ``as_of_date``."""

    sorted_dates = sorted(set(trading_dates))
    if as_of_date not in sorted_dates:
        raise NonTradingDateError(
            f"{as_of_date.isoformat()} is not a trading date"
        )
    for candidate in sorted_dates:
        if candidate > as_of_date:
            return candidate
    raise NonTradingDateError(
        f"no trading date after {as_of_date.isoformat()} in the supplied calendar"
    )


def require_fresh_bar(stock_code: str, bars: Sequence[DualPriceBar], as_of_date: date) -> DualPriceBar:
    """Fail closed when no fresh bar is available for ``as_of_date``."""

    if not bars:
        raise DataFreshnessError(
            f"{stock_code} has no bars through {as_of_date.isoformat()}"
        )
    latest = bars[-1]
    if latest.trade_date != as_of_date:
        raise DataFreshnessError(
            f"{stock_code} missing {as_of_date.isoformat()} bar; latest available "
            f"is {latest.trade_date.isoformat()}"
        )
    return latest


def _eligibility_for(bar: DualPriceBar) -> ETFEligibility:
    return ETFEligibility(
        eligible=not bar.suspended,
        rejection_reasons=() if not bar.suspended else ("suspended",),
        exposure_group="shadow",
        history_session_count=300,
        average_amount_20d=float(bar.amount),
    )


def _indicator_snapshot(bar: DualPriceBar, snapshot: IndicatorSnapshot | None) -> IndicatorSnapshot:
    if snapshot is not None:
        return snapshot
    return IndicatorSnapshot(
        close=float(bar.signal_close),
        prior_high_20=float(bar.signal_close),
        prior_low_10=float(bar.signal_close),
        ma20=float(bar.signal_close),
        std20=0.0,
        atr20=None,
        signal_date=bar.trade_date,
    )


def _build_prior_state(prior: tuple[ShadowRunRecord, StateRecord] | None, cash: Decimal) -> StrategyState:
    if prior is None:
        return StrategyState(cash=cash, position_shares=0)
    return prior[1].state


def _check_config_match(
    prior: tuple[ShadowRunRecord, StateRecord] | None, expected_hash: str,
) -> None:
    if prior is None:
        return
    if prior[1].config_hash != expected_hash:
        raise ConfigMismatchError(
            "prior state config_hash "
            f"{prior[1].config_hash!r} differs from active config_hash {expected_hash!r}"
        )


def process_target_close(
    target: TargetSpec,
    bars: Sequence[DualPriceBar],
    selection: ActiveSelection,
    prior: tuple[ShadowRunRecord, StateRecord] | None,
    execution_eligible_date: date,
    strategy_budget: Decimal,
    model_version: str,
) -> ShadowRunRecord:
    """Process one target's close bar and persist the resulting run record."""

    _check_config_match(prior, selection.config_hash)
    state = _build_prior_state(prior, strategy_budget)
    snapshot = _latest_snapshot(bars)
    bar = bars[-1]
    target_config = replace(selection.config, cost=execution_cost_config_for(
        target, bar.trade_date, selection.config,
    ))
    decision = process_close(state, snapshot, _eligibility_for(bar), target_config)
    state = decision.state
    identity = ShadowRunIdentity(
        as_of_date=bar.trade_date,
        model_version=model_version,
        stock_code=target.stock_code,
    )
    record = build_run_record(
        run_id="",
        identity=identity,
        config_hash=selection.config_hash,
        execution_eligible_date=execution_eligible_date,
        state=state,
        orders=decision.orders,
    )
    run_id = derive_run_id(
        bar.trade_date, model_version, selection.config_hash, (target,),
    )
    return replace(record, run_id=run_id)


def replace(record: ShadowRunRecord, **fields) -> ShadowRunRecord:
    """Small ``dataclasses.replace`` wrapper that keeps imports tight."""

    from dataclasses import replace as _replace
    return _replace(record, **fields)


def _latest_snapshot(bars: Sequence[DualPriceBar]) -> IndicatorSnapshot:
    snapshots = compute_indicators(bars)
    for snapshot in reversed(snapshots):
        if snapshot is not None:
            return snapshot
    last = bars[-1]
    return _indicator_snapshot(last, None)


@dataclass(frozen=True)
class _ProviderLike(Protocol):
    def load_calendar(self, around: date) -> Sequence[date]: ...

    def load_bars(self, stock_code: str, start_date: date, end_date: date) -> Sequence[DualPriceBar]: ...


def run_shadow_date(
    as_of_date: date,
    now: datetime,
    store: ShadowStore,
    provider: _ProviderLike,
    *,
    model_version: str = "shadow-v1",
) -> ShadowRunSummary:
    """Run the daily shadow orchestrator for ``as_of_date`` and persist results."""

    require_after_market_data_cutoff(as_of_date, now)
    frozen = store.load_active_frozen_config(as_of_date)
    if frozen is None:
        raise PriorStateMissingError(
            f"no active frozen selection on {as_of_date.isoformat()}"
        )
    selection = _build_active_selection(frozen)
    calendar = list(provider.load_calendar(as_of_date))
    execution_eligible_date = next_trading_session(as_of_date, calendar)

    target_states: list[tuple[TargetSpec, StateRecord]] = []
    advices: list[AdviceRecord] = []
    health_checks: list[HealthCheck] = []
    lookback_start = selection.data_cutoff - timedelta(days=DATA_FRESHNESS_LOOKBACK_DAYS)
    for target in selection.targets:
        bars = list(provider.load_bars(target.stock_code, lookback_start, as_of_date))
        bar = require_fresh_bar(target.stock_code, bars, as_of_date)
        prior = store.load_latest_state(target.stock_code, selection.config_hash)
        strategy_budget = target.sub_layer_budget * _as_decimal_weight(target.weight)
        record = process_target_close(
            target, bars, selection, prior, execution_eligible_date,
            strategy_budget, model_version,
        )
        cost_boundary = cost_boundary_for(target, as_of_date, selection.config)
        record = replace(
            record,
            health_checks=(_cost_boundary_check(record, target, cost_boundary),),
        )
        persisted = store.persist_run(record)
        target_states.append((target, persisted.state))
        advices.extend(persisted.advices)
        health_checks.append(_freshness_check(persisted, bar))
        health_checks.extend(persisted.health_checks)

    run_id = derive_run_id(
        as_of_date, model_version, selection.config_hash,
        [target for target, _ in target_states],
    )
    return ShadowRunSummary(
        as_of_date=as_of_date,
        model_version=model_version,
        config_hash=selection.config_hash,
        execution_eligible_date=execution_eligible_date,
        run_id=run_id,
        target_states=tuple(target_states),
        advices=tuple(advices),
        health_checks=tuple(health_checks),
    )


def _build_active_selection(frozen) -> ActiveSelection:
    payload = frozen.selection_payload or {}
    _require_passing_layer_benchmarks(payload)
    raw_targets = payload.get("targets", ())
    if not isinstance(raw_targets, Sequence) or isinstance(raw_targets, (str, bytes)):
        raise ValueError("frozen selection targets must be a sequence")
    targets: list[TargetSpec] = []
    for item in raw_targets:
        if not isinstance(item, Mapping):
            raise ValueError("frozen selection target must be a mapping")
        required = {
            "stock_code", "sub_layer", "sub_layer_budget", "instrument_type", "weight", "config_hash",
        }
        missing = required.difference(item)
        if missing:
            raise ValueError(
                "legacy frozen target is ambiguous; missing " + ", ".join(sorted(missing))
            )
        if str(item["config_hash"]) != frozen.config_hash:
            raise ValueError("frozen target config_hash must equal the active frozen config_hash")
        try:
            sub_layer = SubLayer(str(item["sub_layer"]))
            instrument_type = InstrumentType(str(item["instrument_type"]))
            budget = Decimal(str(item["sub_layer_budget"]))
            weight = Decimal(str(item["weight"]))
        except (ValueError, ArithmeticError) as exc:
            raise ValueError(f"invalid frozen target payload: {exc}") from exc
        if not budget.is_finite() or budget <= 0 or not weight.is_finite() or weight <= 0:
            raise ValueError("frozen target budget and weight must be positive finite decimals")
        expected_layer = asset_layer_for(sub_layer).value
        if str(item.get("layer", expected_layer)) != expected_layer:
            raise ValueError("frozen target layer must match its approved sub_layer")
        targets.append(TargetSpec(
            stock_code=str(item["stock_code"]),
            tracking_index_code=str(item.get("tracking_index_code", "")),
            layer=expected_layer,
            weight=weight,
            sub_layer=sub_layer,
            sub_layer_budget=budget,
            instrument_type=instrument_type,
        ))
    _validate_active_targets(targets)
    return ActiveSelection(
        config_hash=frozen.config_hash,
        config=frozen.config,
        data_cutoff=frozen.data_cutoff,
        targets=tuple(targets),
    )


def _require_passing_layer_benchmarks(payload: Mapping[str, object]) -> None:
    """Reject new research payloads that record a failed layer-level gate.

    Historic frozen records did not carry layer research evidence and remain
    readable for audit/replay.  Any new record which includes the field must
    be complete and passing before it can generate advice.
    """

    raw = payload.get("layer_benchmarks")
    if raw is None:
        return
    if not isinstance(raw, Mapping):
        raise ValueError("layer benchmark evidence must be a mapping")
    expected = {"defensive", "broad_beta"}
    if set(raw) != expected:
        raise ValueError("layer benchmark evidence must cover defensive and broad_beta")
    for layer in expected:
        result = raw[layer]
        if not isinstance(result, Mapping) or result.get("passed") is not True:
            raise ValueError(f"layer benchmark did not pass: {layer}")


def _as_decimal_weight(weight: Decimal | float) -> Decimal:
    value = Decimal(str(weight))
    if not value.is_finite() or value <= 0:
        raise ValueError("target weight must be a positive finite decimal")
    return value


def _validate_active_targets(targets: Sequence[TargetSpec]) -> None:
    grouped: dict[SubLayer, list[TargetSpec]] = {}
    for target in targets:
        if target.sub_layer is None or target.sub_layer_budget is None:
            raise ValueError("frozen target is missing required sub-layer funding")
        grouped.setdefault(target.sub_layer, []).append(target)
    if not grouped:
        raise ValueError("active frozen selection has no funded targets")
    for sub_layer, members in grouped.items():
        if len({member.sub_layer_budget for member in members}) != 1:
            raise ValueError(f"sub-layer {sub_layer.value!r} has inconsistent target budgets")
        if sum((_as_decimal_weight(member.weight) for member in members), Decimal("0")) != Decimal("1"):
            raise ValueError(f"sub-layer {sub_layer.value!r} target weights must sum exactly to 1")


def _cost_boundary_check(
    record: ShadowRunRecord,
    target: TargetSpec,
    boundary: ETFCostBoundary | ChinaAStockCostBoundary,
) -> HealthCheck:
    detail: dict[str, object] = {"instrument_type": target.instrument_type.value}
    if isinstance(boundary, ETFCostBoundary):
        detail["cost_model"] = "etf_config"
        detail["commission_rate"] = boundary.cost.commission_rate
    else:
        detail.update({
            "cost_model": "china_a_stock",
            "commission_rate": str(boundary.commission_rate),
            "stamp_duty_sell_rate": str(boundary.stamp_duty_sell_rate),
            "transfer_fee_rate": str(boundary.transfer_fee_rate),
        })
    return HealthCheck(
        run_id=record.run_id,
        check_name="instrument_cost_boundary",
        passed=True,
        detail=detail,
    )


def _freshness_check(record: ShadowRunRecord, bar: DualPriceBar) -> HealthCheck:
    fresh = bar.trade_date == record.identity.as_of_date
    return HealthCheck(
        run_id=record.run_id,
        check_name="data_freshness",
        passed=fresh,
        detail={
            "stock_code": record.identity.stock_code,
            "as_of_date": record.identity.as_of_date.isoformat(),
            "bar_trade_date": bar.trade_date.isoformat(),
        },
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run one adaptive ETF shadow session and persist to the shadow store",
    )
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--today", required=True, help="ISO datetime treated as wall-clock now")
    parser.add_argument("--model-version", default="shadow-v1")
    return parser


def main(
    argv: list[str] | None = None,
    *,
    store_factory=None,
    provider_factory=None,
) -> int:
    args = build_parser().parse_args(argv)
    try:
        store_factory = store_factory or default_shadow_store
        provider_factory = provider_factory or default_shadow_provider
        summary = run_shadow_date(
            date.fromisoformat(args.as_of_date),
            datetime.fromisoformat(args.today),
            store_factory(), provider_factory(), model_version=args.model_version,
        )
    except (ValueError, RuntimeError) as exc:
        import sys
        print(str(exc), file=sys.stderr)
        return 2
    print(summary.canonical_json())
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())

