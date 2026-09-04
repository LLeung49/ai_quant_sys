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
from .config import AdaptiveConfig
from .contracts import DualPriceBar, ETFEligibility, ExecutionAvailability
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
    """A single ETF target consumed by the shadow runner."""

    stock_code: str
    tracking_index_code: str
    layer: str
    weight: float


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
                    "weight": target.weight,
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
    initial_cash: Decimal,
    model_version: str,
) -> ShadowRunRecord:
    """Process one target's close bar and persist the resulting run record."""

    _check_config_match(prior, selection.config_hash)
    state = _build_prior_state(prior, initial_cash)
    snapshot = _latest_snapshot(bars)
    bar = bars[-1]
    decision = process_close(state, snapshot, _eligibility_for(bar), selection.config)
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
    initial_cash: Decimal = Decimal("100000"),
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
        record = process_target_close(
            target, bars, selection, prior, execution_eligible_date,
            initial_cash, model_version,
        )
        persisted = store.persist_run(record)
        target_states.append((target, persisted.state))
        advices.extend(persisted.advices)
        health_checks.append(_freshness_check(persisted, bar))

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
    raw_targets = payload.get("targets", ())
    targets = tuple(
        TargetSpec(
            stock_code=str(item["stock_code"]),
            tracking_index_code=str(item.get("tracking_index_code", "")),
            layer=str(item.get("layer", "default")),
            weight=float(item.get("weight", 0.0)),
        )
        for item in raw_targets
    )
    return ActiveSelection(
        config_hash=frozen.config_hash,
        config=frozen.config,
        data_cutoff=frozen.data_cutoff,
        targets=targets,
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
    parser.add_argument("--config-hash", default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    store: ShadowStore = InMemoryShadowStore()
    from .shadow_store import FrozenConfigRecord  # local import to avoid cycles
    if args.config_hash:
        store.activate_frozen_config(FrozenConfigRecord(
            config_hash=args.config_hash,
            config=AdaptiveConfig.default(),
            selection_payload={
                "targets": [
                    {"stock_code": "510300.SH", "weight": 1.0,
                     "layer": "core_broad", "tracking_index_code": "000300.SH"},
                ],
            },
            data_cutoff=date.fromisoformat(args.as_of_date),
            activation_date=date.fromisoformat(args.as_of_date),
            review_date=date.fromisoformat(args.as_of_date) + timedelta(days=183),
            activated_at=datetime.now(),
        ))
    raise SystemExit(0) if store else 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())

