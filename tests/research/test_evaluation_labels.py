from datetime import date

import pytest

from morning_conference.sector_rotation2.research.contracts import BenchmarkStatus, PathStatus, ReturnStatus
from morning_conference.sector_rotation2.research.evaluation.calendar import TradingCalendar
from morning_conference.sector_rotation2.research.evaluation.labels import build_close_to_close_label, build_tradable_label
from morning_conference.sector_rotation2.research.evaluation.prices import InMemoryPriceBarProvider, PriceBar


T0, T1, T2, T3, T4, T5 = (date(2026, 1, day) for day in range(5, 11))


@pytest.fixture
def calendar() -> TradingCalendar:
    return TradingCalendar([T0, T1, T2, T3, T4, T5])


def provider(*, entity_bars: dict[date, PriceBar], benchmark_bars: dict[date, PriceBar] | None = None,
             entity_type: str = "stock", open_entities: set[str] | None = None, ohlc_entities: set[str] | None = None) -> InMemoryPriceBarProvider:
    bars = {(entity_type, "000001.SZ"): entity_bars}
    if benchmark_bars is not None:
        bars[("benchmark", "000300.SH")] = benchmark_bars
    return InMemoryPriceBarProvider(
        bars,
        open_entities={"stock", "benchmark"} if open_entities is None else open_entities,
        ohlc_entities={"stock", "benchmark"} if ohlc_entities is None else ohlc_entities,
    )


def bar(day: date, close: float, *, open: float | None = None, high: float | None = None, low: float | None = None) -> PriceBar:
    return PriceBar(day, close=close, open=open, high=high, low=low)


def test_tradable_horizon_does_not_shift_over_suspension(calendar: TradingCalendar) -> None:
    prices = provider(entity_bars={T0: bar(T0, 10), T2: bar(T2, 12, open=11)})
    label = build_tradable_label(calendar=calendar, provider=prices, signal_date=T0, entity_type="stock", entity_code="000001.SZ", horizon=2)
    assert label.entry_date == T1
    assert label.exit_date == T2
    assert label.return_status is ReturnStatus.UNEXECUTABLE_ENTRY
    assert label.forward_return is None


def test_horizon_one_means_next_open_to_next_close(calendar: TradingCalendar) -> None:
    prices = provider(entity_bars={T0: bar(T0, 10), T1: bar(T1, 12, open=11, high=13, low=10)})
    label = build_tradable_label(calendar=calendar, provider=prices, signal_date=T0, entity_type="stock", entity_code="000001.SZ", horizon=1)
    assert label.entry_date == T1
    assert label.exit_date == T1
    assert label.forward_return == pytest.approx(12 / 11 - 1)


def test_delayed_shadow_after_open_enters_at_following_trade_day_open(calendar: TradingCalendar) -> None:
    prices = provider(entity_bars={
        T0: bar(T0, 10),
        T2: bar(T2, 12, open=11, high=13, low=10),
        T3: bar(T3, 13, open=12, high=14, low=11),
    })

    label = build_tradable_label(
        calendar=calendar, provider=prices, signal_date=T0, entity_type="stock", entity_code="000001.SZ",
        horizon=2, entry_date_override=T2,
    )

    assert label.entry_date == T2
    assert label.exit_date == T3
    assert label.forward_return == pytest.approx(13 / 11 - 1)


def test_backfill_retains_t_plus_one_entry_without_availability_metadata(calendar: TradingCalendar) -> None:
    prices = provider(entity_bars={T0: bar(T0, 10), T1: bar(T1, 12, open=11, high=13, low=10)})

    label = build_tradable_label(
        calendar=calendar, provider=prices, signal_date=T0, entity_type="stock", entity_code="000001.SZ", horizon=1,
    )

    assert label.entry_date == T1


def test_deferred_entry_outside_calendar_is_not_matured_instead_of_raising() -> None:
    limited_calendar = TradingCalendar([T0, T1])
    prices = provider(entity_bars={T0: bar(T0, 10), T1: bar(T1, 11, open=10)})

    label = build_tradable_label(
        calendar=limited_calendar, provider=prices, signal_date=T0, entity_type="stock", entity_code="000001.SZ",
        horizon=1, entry_date_override=T2,
    )

    assert label.return_status is ReturnStatus.NOT_MATURED


def test_horizon_five_exits_market_t_plus_five(calendar: TradingCalendar) -> None:
    prices = provider(entity_bars={T0: bar(T0, 10), T1: bar(T1, 11, open=10), T5: bar(T5, 15, open=14)})
    label = build_tradable_label(calendar=calendar, provider=prices, signal_date=T0, entity_type="stock", entity_code="000001.SZ", horizon=5)
    assert label.exit_date == calendar.shift(T0, 5)


def test_sector_without_open_rejects_tradable_label(calendar: TradingCalendar) -> None:
    prices = provider(entity_type="sector_l2", entity_bars={T0: bar(T0, 10), T1: bar(T1, 11) }, open_entities=set(), ohlc_entities=set())
    label = build_tradable_label(calendar=calendar, provider=prices, signal_date=T0, entity_type="sector_l2", entity_code="000001.SZ", horizon=1)
    assert label.return_status is ReturnStatus.UNSUPPORTED_PRICE_WINDOW


def test_sector_without_ohlc_has_no_mae_mfe(calendar: TradingCalendar) -> None:
    prices = provider(entity_type="sector_l2", entity_bars={T0: bar(T0, 10), T1: bar(T1, 11)}, open_entities=set(), ohlc_entities=set())
    label = build_close_to_close_label(calendar=calendar, provider=prices, signal_date=T0, entity_type="sector_l2", entity_code="000001.SZ", horizon=1)
    assert label.forward_return == pytest.approx(0.1)
    assert label.path_status is PathStatus.UNSUPPORTED
    assert label.mae is None
    assert label.mfe is None


def test_missing_intermediate_ohlc_marks_path_incomplete_but_keeps_endpoint_return(calendar: TradingCalendar) -> None:
    prices = provider(entity_bars={T0: bar(T0, 10), T1: bar(T1, 11, open=10, high=12, low=9), T3: bar(T3, 13, open=12, high=14, low=11)})
    label = build_tradable_label(calendar=calendar, provider=prices, signal_date=T0, entity_type="stock", entity_code="000001.SZ", horizon=3)
    assert label.return_status is ReturnStatus.COMPLETE
    assert label.path_status is PathStatus.INCOMPLETE
    assert label.mae is None
    assert label.mfe is None


def test_tradable_excess_requires_benchmark_open_on_same_entry_date(calendar: TradingCalendar) -> None:
    prices = provider(entity_bars={T0: bar(T0, 10), T1: bar(T1, 12, open=11, high=13, low=10)}, benchmark_bars={T0: bar(T0, 100), T1: bar(T1, 101)})
    label = build_tradable_label(calendar=calendar, provider=prices, signal_date=T0, entity_type="stock", entity_code="000001.SZ", horizon=1, benchmark_type="benchmark", benchmark_code="000300.SH")
    assert label.forward_return is not None
    assert label.benchmark_status is BenchmarkStatus.MISSING_ENTRY
    assert label.benchmark_return is None
    assert label.excess_return is None
    assert label.excess_is_complete is False


def test_close_to_close_excess_uses_same_signal_and_exit_dates(calendar: TradingCalendar) -> None:
    prices = provider(entity_bars={T0: bar(T0, 10), T2: bar(T2, 12)}, benchmark_bars={T0: bar(T0, 100), T2: bar(T2, 110)})
    label = build_close_to_close_label(calendar=calendar, provider=prices, signal_date=T0, entity_type="stock", entity_code="000001.SZ", horizon=2, benchmark_type="benchmark", benchmark_code="000300.SH")
    assert label.benchmark_status is BenchmarkStatus.COMPLETE
    assert label.benchmark_return == pytest.approx(0.1)
    assert label.excess_return == pytest.approx(0.1)
