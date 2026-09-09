from dataclasses import replace
from datetime import date
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.backtest_provider import AdaptiveBacktestDataProvider
from asset_allocation.etf_adaptive.config import AdaptiveConfig
from asset_allocation.etf_adaptive.contracts import (
    CorporateAction,
    CorporateActionType,
    DualPriceBar,
    ETFEligibility,
    ExecutionAvailability,
)
from asset_allocation.etf_adaptive.engine import AdaptiveBacktestEngine
from asset_allocation.etf_adaptive import engine as engine_module
from asset_allocation.etf_adaptive.execution import ExecutionSimulator
from asset_allocation.etf_adaptive.state import (
    BacktestRequest,
    Decision,
    OrderIntent,
    OrderReason,
    Side,
)


CODE = "510300.SH"
START = date(2026, 9, 1)
END = date(2026, 9, 3)


def _bars() -> tuple[DualPriceBar, ...]:
    return tuple(
        DualPriceBar(
            CODE,
            date(2026, 9, day),
            1.0,
            1.1,
            0.9,
            1.0,
            4.0,
            4.4,
            3.6,
            4.0,
            20_000_000.0,
            False,
            0.25,
            4.0,
            ExecutionAvailability(False, False, "exchange"),
        )
        for day in range(1, 4)
    )


def _actions() -> tuple[CorporateAction, ...]:
    return (
        CorporateAction(
            CODE,
            date(2026, 9, 2),
            CorporateActionType.SHARE_SPLIT,
            None,
            Decimal("1.1"),
        ),
    )


def _eligibility(
    bars: tuple[DualPriceBar, ...] | None = None,
) -> dict[date, ETFEligibility]:
    eligible = ETFEligibility(True, (), "broad", 252, 20_000_000.0)
    return {bar.trade_date: eligible for bar in bars or _bars()}


def _request() -> BacktestRequest:
    return BacktestRequest(CODE, Decimal("1000"), start_date=START, end_date=END)


class InMemoryBacktestProvider:
    def __init__(
        self,
        bars: tuple[DualPriceBar, ...],
        actions: tuple[CorporateAction, ...],
        eligibility: dict[date, ETFEligibility],
    ) -> None:
        self.bars = bars
        self.actions = actions
        self.eligibility = eligibility
        self.calls: list[str] = []
        self.range_requests: list[tuple[str, str, date, date]] = []
        self.eligibility_requests: list[tuple[str, tuple[DualPriceBar, ...]]] = []

    def load_bars(
        self, stock_code: str, start_date: date, end_date: date,
    ) -> tuple[DualPriceBar, ...]:
        self.calls.append("bars")
        self.range_requests.append(("bars", stock_code, start_date, end_date))
        return self.bars

    def load_actions(
        self, stock_code: str, start_date: date, end_date: date,
    ) -> tuple[CorporateAction, ...]:
        self.calls.append("actions")
        self.range_requests.append(("actions", stock_code, start_date, end_date))
        return self.actions

    def load_eligibility(
        self, stock_code: str, bars: tuple[DualPriceBar, ...],
    ) -> dict[date, ETFEligibility]:
        self.calls.append("eligibility")
        self.eligibility_requests.append((stock_code, bars))
        return self.eligibility


def _engine(
    provider: AdaptiveBacktestDataProvider | None = None,
) -> AdaptiveBacktestEngine:
    config = AdaptiveConfig.default()
    return AdaptiveBacktestEngine(
        config,
        ExecutionSimulator(config.cost, config.trend),
        provider,
    )


def test_run_loads_pit_inputs_from_provider() -> None:
    bars = _bars()
    provider = InMemoryBacktestProvider(bars, _actions(), _eligibility(bars))

    result = _engine(provider).run(_request())

    assert provider.calls == ["bars", "actions", "eligibility"]
    assert provider.range_requests == [
        ("bars", CODE, START, END),
        ("actions", CODE, START, END),
    ]
    assert provider.eligibility_requests == [(CODE, bars)]
    assert provider.eligibility_requests[0][1] is bars
    assert any(event.kind == "corporate_action" for event in result.events)


def test_provider_action_is_applied_to_inventory_before_pending_fill(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    bars = _bars()
    split = replace(_actions()[0], effective_date=END)
    provider = InMemoryBacktestProvider(bars, (split,), _eligibility(bars))
    buy = OrderIntent(
        START,
        Side.BUY,
        OrderReason.GRID_INITIALIZE,
        0.05,
        (),
        500.0,
        0.0,
        "establish held inventory",
    )
    sell = OrderIntent(
        date(2026, 9, 2),
        Side.SELL,
        OrderReason.HARD_STOP,
        0.05,
        (),
        0.0,
        0.0,
        "sell all split-adjusted inventory",
    )
    close_count = 0

    def decide(state, *_):
        nonlocal close_count
        orders = ((buy,), (sell,), ())[close_count]
        close_count += 1
        return Decision(state, orders)

    monkeypatch.setattr(
        "asset_allocation.etf_adaptive.indicators.compute_indicators",
        lambda values: (object(),) * len(values),
    )
    monkeypatch.setattr(engine_module, "process_close", decide)

    result = _engine(provider).run(_request())

    fills = [event for event in result.events if event.kind == "fill"]
    assert fills[-1].payload == (
        ("reason", "hard_stop"), ("side", "sell"), ("shares", "110"),
        ("raw_price", "3.9988"), ("commission", "5.00"),
    )
    assert result.nav[-1].cash == Decimal("1029.748")
    assert result.nav[-1].market_value == Decimal("0.0")


def test_provider_run_matches_explicit_test_seam() -> None:
    bars = _bars()
    actions = _actions()
    eligibility = _eligibility(bars)
    provider = InMemoryBacktestProvider(bars, actions, eligibility)

    provider_result = _engine(provider).run(_request())
    explicit_result = _engine().run_with_data(
        _request(), bars, eligibility, actions,
    )

    assert provider_result == explicit_result


@pytest.mark.parametrize(
    ("bars", "message"),
    (
        ((_bars()[0], replace(_bars()[1], stock_code="510500.SH"), _bars()[2]), "stock code"),
        ((_bars()[0], _bars()[2], _bars()[1]), "ordered unique sessions"),
        ((_bars()[0], _bars()[1], _bars()[1]), "ordered unique sessions"),
        ((_bars()[1], _bars()[2]), "bar coverage"),
        ((_bars()[0], _bars()[1]), "bar coverage"),
    ),
)
def test_run_with_data_rejects_invalid_bar_identity_and_coverage(
    bars: tuple[DualPriceBar, ...], message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        _engine().run_with_data(_request(), bars, _eligibility(bars), ())


@pytest.mark.parametrize(
    "action",
    (
        replace(_actions()[0], stock_code="510500.SH"),
        replace(_actions()[0], effective_date=date(2026, 8, 31)),
        replace(_actions()[0], effective_date=date(2026, 9, 4)),
    ),
)
def test_run_with_data_rejects_action_outside_request_identity_or_range(
    action: CorporateAction,
) -> None:
    with pytest.raises(ValueError, match="corporate action"):
        _engine().run_with_data(_request(), _bars(), _eligibility(), (action,))


def test_run_with_data_requires_eligibility_for_every_bar() -> None:
    eligibility = _eligibility()
    del eligibility[date(2026, 9, 2)]

    with pytest.raises(ValueError, match="eligibility coverage"):
        _engine().run_with_data(_request(), _bars(), eligibility, ())


def test_run_requires_an_injected_provider() -> None:
    with pytest.raises(ValueError, match="provider"):
        _engine().run(_request())


def test_run_with_data_rejects_non_date_request_boundaries() -> None:
    request = replace(_request(), start_date="2026-09-01")  # type: ignore[arg-type]

    with pytest.raises(ValueError, match="start_date must be a date"):
        _engine().run_with_data(request, _bars(), _eligibility(), ())
