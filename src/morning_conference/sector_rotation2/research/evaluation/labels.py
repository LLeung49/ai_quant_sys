"""Forward-label builders with exact market-calendar date semantics."""

from datetime import date
from typing import Mapping

from ..contracts import BenchmarkStatus, ForwardLabel, PathStatus, ReturnStatus
from .calendar import TradingCalendar
from .prices import PriceBar, PriceBarProvider


def build_close_to_close_label(
    *, calendar: TradingCalendar, provider: PriceBarProvider, signal_date: date,
    entity_type: str, entity_code: str, horizon: int, benchmark_type: str = "none",
    benchmark_code: str = "", price_basis: str = "close", source_snapshot_id: int | None = None,
    snapshot_mode: object | None = None,
) -> ForwardLabel:
    """Build T close -> T+h close outcome without fabricating intraday fields."""
    exit_date = _maturity_date(calendar, signal_date, horizon)
    if exit_date is None:
        return _label(
            signal_date, entity_type, entity_code, benchmark_type, benchmark_code, horizon, "close_to_close",
            signal_date, None, price_basis, None, None, None, None, None,
            ReturnStatus.NOT_MATURED, PathStatus.UNSUPPORTED, BenchmarkStatus.NOT_REQUESTED,
            source_snapshot_id, snapshot_mode,
        )

    bars = provider.load_bars(entity_type, entity_code, signal_date, exit_date)
    signal_bar, exit_bar = bars.get(signal_date), bars.get(exit_date)
    signal_close = _price(signal_bar, "close")
    exit_close = _price(exit_bar, "close")
    if signal_close is None:
        return _label(signal_date, entity_type, entity_code, benchmark_type, benchmark_code, horizon, "close_to_close",
                      signal_date, exit_date, price_basis, None, None, exit_close, None, None,
                      ReturnStatus.MISSING_SIGNAL_BAR, _path_status(provider, entity_type, bars, calendar, signal_date, exit_date),
                      BenchmarkStatus.NOT_REQUESTED, source_snapshot_id, snapshot_mode)
    if exit_close is None:
        return _label(signal_date, entity_type, entity_code, benchmark_type, benchmark_code, horizon, "close_to_close",
                      signal_date, exit_date, price_basis, signal_close, signal_close, None, None, None,
                      ReturnStatus.MISSING_EXIT, _path_status(provider, entity_type, bars, calendar, signal_date, exit_date),
                      BenchmarkStatus.NOT_REQUESTED, source_snapshot_id, snapshot_mode)

    forward_return = exit_close / signal_close - 1.0
    path_status, mae, mfe = _path_metrics(provider, entity_type, bars, calendar, signal_date, exit_date, signal_close)
    benchmark_return, benchmark_status = _benchmark_close_return(
        provider, benchmark_type, benchmark_code, signal_date, exit_date,
    )
    return _label(
        signal_date, entity_type, entity_code, benchmark_type, benchmark_code, horizon, "close_to_close",
        signal_date, exit_date, price_basis, signal_close, signal_close, exit_close, 0.0, forward_return,
        ReturnStatus.COMPLETE, path_status, benchmark_status, source_snapshot_id, snapshot_mode,
        benchmark_return=benchmark_return,
    )


def build_tradable_label(
    *, calendar: TradingCalendar, provider: PriceBarProvider, signal_date: date,
    entity_type: str, entity_code: str, horizon: int, benchmark_type: str = "none",
    benchmark_code: str = "", price_basis: str = "qfq", source_snapshot_id: int | None = None,
    snapshot_mode: object | None = None, entry_date_override: date | None = None,
) -> ForwardLabel:
    """Build a daily-bar tradable outcome; date positions never use entity bars.

    The default remains the historical close-signal/T+1-open convention.  A
    delayed operational snapshot may provide its already-resolved daily-bar
    entry date; its holding window begins at that open, rather than pretending
    it could have filled at the earlier T+1 open.
    """
    try:
        entry_date = entry_date_override or _maturity_date(calendar, signal_date, 1)
        exit_date = (
            _maturity_date(calendar, entry_date, horizon - 1)
            if entry_date_override is not None and entry_date is not None
            else _maturity_date(calendar, signal_date, horizon)
        )
    except ValueError:
        entry_date, exit_date = None, None
    if entry_date is None or exit_date is None:
        return _label(signal_date, entity_type, entity_code, benchmark_type, benchmark_code, horizon, "tradable",
                      entry_date, exit_date, price_basis, None, None, None, None, None,
                      ReturnStatus.NOT_MATURED, PathStatus.UNSUPPORTED, BenchmarkStatus.NOT_REQUESTED,
                      source_snapshot_id, snapshot_mode)
    if not provider.supports_open(entity_type):
        return _label(signal_date, entity_type, entity_code, benchmark_type, benchmark_code, horizon, "tradable",
                      entry_date, exit_date, price_basis, None, None, None, None, None,
                      ReturnStatus.UNSUPPORTED_PRICE_WINDOW, PathStatus.UNSUPPORTED, BenchmarkStatus.NOT_REQUESTED,
                      source_snapshot_id, snapshot_mode)

    bars = provider.load_bars(entity_type, entity_code, signal_date, exit_date)
    signal_close = _price(bars.get(signal_date), "close")
    entry_open = _price(bars.get(entry_date), "open")
    exit_close = _price(bars.get(exit_date), "close")
    path_status = _path_status(provider, entity_type, bars, calendar, entry_date, exit_date)
    if signal_close is None:
        return _label(signal_date, entity_type, entity_code, benchmark_type, benchmark_code, horizon, "tradable",
                      entry_date, exit_date, price_basis, None, entry_open, exit_close, None, None,
                      ReturnStatus.MISSING_SIGNAL_BAR, path_status, BenchmarkStatus.NOT_REQUESTED, source_snapshot_id, snapshot_mode)
    if entry_open is None:
        return _label(signal_date, entity_type, entity_code, benchmark_type, benchmark_code, horizon, "tradable",
                      entry_date, exit_date, price_basis, signal_close, None, exit_close, None, None,
                      ReturnStatus.UNEXECUTABLE_ENTRY, path_status, BenchmarkStatus.NOT_REQUESTED, source_snapshot_id, snapshot_mode)
    if exit_close is None:
        return _label(signal_date, entity_type, entity_code, benchmark_type, benchmark_code, horizon, "tradable",
                      entry_date, exit_date, price_basis, signal_close, entry_open, None, entry_open / signal_close - 1.0, None,
                      ReturnStatus.MISSING_EXIT, path_status, BenchmarkStatus.NOT_REQUESTED, source_snapshot_id, snapshot_mode)

    forward_return = exit_close / entry_open - 1.0
    path_status, mae, mfe = _path_metrics(provider, entity_type, bars, calendar, entry_date, exit_date, entry_open)
    benchmark_return, benchmark_status = _benchmark_tradable_return(
        provider, benchmark_type, benchmark_code, entry_date, exit_date,
    )
    return _label(
        signal_date, entity_type, entity_code, benchmark_type, benchmark_code, horizon, "tradable",
        entry_date, exit_date, price_basis, signal_close, entry_open, exit_close, entry_open / signal_close - 1.0,
        forward_return, ReturnStatus.COMPLETE, path_status, benchmark_status, source_snapshot_id, snapshot_mode,
        mae=mae, mfe=mfe, benchmark_return=benchmark_return,
    )


def build_delayed_unavailable_label(
    *, signal_date: date, entity_type: str, entity_code: str, horizon: int,
    source_snapshot_id: int | None, snapshot_mode: object | None,
) -> ForwardLabel:
    """Mark delayed non-tradable inputs as explicitly unevaluable on daily bars."""
    return _label(
        signal_date, entity_type, entity_code, "none", "", horizon, "close_to_close",
        None, None, "delayed_shadow_requires_tradable_open", None, None, None, None, None,
        ReturnStatus.UNSUPPORTED_PRICE_WINDOW, PathStatus.UNSUPPORTED, BenchmarkStatus.NOT_REQUESTED,
        source_snapshot_id, snapshot_mode,
    )


def build_delayed_not_matured_label(
    *, signal_date: date, entity_type: str, entity_code: str, horizon: int,
    label_type: str, source_snapshot_id: int | None, snapshot_mode: object | None,
) -> ForwardLabel:
    """Represent a delayed label whose required session is outside calendar coverage."""
    price_basis = (
        "delayed_shadow_requires_tradable_open"
        if label_type == "close_to_close"
        else "qfq"
    )
    return _label(
        signal_date, entity_type, entity_code, "none", "", horizon, label_type,
        None, None, price_basis, None, None, None, None, None,
        ReturnStatus.NOT_MATURED, PathStatus.UNSUPPORTED, BenchmarkStatus.NOT_REQUESTED,
        source_snapshot_id, snapshot_mode,
    )


def calc_mae_mfe(bars: Mapping[date, PriceBar], dates: tuple[date, ...], entry_price: float) -> tuple[float, float] | None:
    """Calculate excursions only when every requested bar has valid high/low data."""
    lows = [_price(bars.get(day), "low") for day in dates]
    highs = [_price(bars.get(day), "high") for day in dates]
    if any(value is None for value in lows) or any(value is None for value in highs):
        return None
    return min(float(value) / entry_price - 1.0 for value in lows), max(float(value) / entry_price - 1.0 for value in highs)


def _maturity_date(calendar: TradingCalendar, signal_date: date, horizon: int) -> date | None:
    try:
        return calendar.shift(signal_date, horizon)
    except IndexError:
        return None


def _calendar_window(calendar: TradingCalendar, start_date: date, end_date: date) -> tuple[date, ...]:
    offset = 0
    dates: list[date] = []
    while True:
        current = calendar.shift(start_date, offset)
        dates.append(current)
        if current == end_date:
            return tuple(dates)
        offset += 1


def _price(bar: PriceBar | None, field: str) -> float | None:
    value = getattr(bar, field, None) if bar is not None else None
    return float(value) if value is not None and float(value) > 0 else None


def _path_status(provider: PriceBarProvider, entity_type: str, bars: Mapping[date, PriceBar], calendar: TradingCalendar,
                 start_date: date, end_date: date) -> PathStatus:
    if not provider.supports_ohlc(entity_type):
        return PathStatus.UNSUPPORTED
    dates = _calendar_window(calendar, start_date, end_date)
    return PathStatus.COMPLETE if calc_mae_mfe(bars, dates, 1.0) is not None else PathStatus.INCOMPLETE


def _path_metrics(provider: PriceBarProvider, entity_type: str, bars: Mapping[date, PriceBar], calendar: TradingCalendar,
                  start_date: date, end_date: date, entry_price: float) -> tuple[PathStatus, float | None, float | None]:
    status = _path_status(provider, entity_type, bars, calendar, start_date, end_date)
    if status is not PathStatus.COMPLETE:
        return status, None, None
    mae_mfe = calc_mae_mfe(bars, _calendar_window(calendar, start_date, end_date), entry_price)
    assert mae_mfe is not None
    return status, mae_mfe[0], mae_mfe[1]


def _benchmark_close_return(provider: PriceBarProvider, benchmark_type: str, benchmark_code: str,
                            entry_date: date, exit_date: date) -> tuple[float | None, BenchmarkStatus]:
    if benchmark_type == "none" or not benchmark_code:
        return None, BenchmarkStatus.NOT_REQUESTED
    bars = provider.load_bars(benchmark_type, benchmark_code, entry_date, exit_date)
    entry, exit_price = _price(bars.get(entry_date), "close"), _price(bars.get(exit_date), "close")
    if entry is None:
        return None, BenchmarkStatus.MISSING_ENTRY
    if exit_price is None:
        return None, BenchmarkStatus.MISSING_EXIT
    return exit_price / entry - 1.0, BenchmarkStatus.COMPLETE


def _benchmark_tradable_return(provider: PriceBarProvider, benchmark_type: str, benchmark_code: str,
                               entry_date: date, exit_date: date) -> tuple[float | None, BenchmarkStatus]:
    if benchmark_type == "none" or not benchmark_code:
        return None, BenchmarkStatus.NOT_REQUESTED
    if not provider.supports_open(benchmark_type):
        return None, BenchmarkStatus.UNSUPPORTED_WINDOW
    bars = provider.load_bars(benchmark_type, benchmark_code, entry_date, exit_date)
    entry, exit_price = _price(bars.get(entry_date), "open"), _price(bars.get(exit_date), "close")
    if entry is None:
        return None, BenchmarkStatus.MISSING_ENTRY
    if exit_price is None:
        return None, BenchmarkStatus.MISSING_EXIT
    return exit_price / entry - 1.0, BenchmarkStatus.COMPLETE


def _label(signal_date: date, entity_type: str, entity_code: str, benchmark_type: str, benchmark_code: str,
           horizon: int, label_type: str, entry_date: date | None, exit_date: date | None, price_basis: str,
           signal_close: float | None, entry_price: float | None, exit_price: float | None, entry_gap: float | None,
           forward_return: float | None, return_status: ReturnStatus, path_status: PathStatus,
           benchmark_status: BenchmarkStatus, source_snapshot_id: int | None, snapshot_mode: object | None,
           *, mae: float | None = None, mfe: float | None = None, benchmark_return: float | None = None) -> ForwardLabel:
    complete = return_status is ReturnStatus.COMPLETE
    excess_complete = complete and benchmark_status is BenchmarkStatus.COMPLETE
    return ForwardLabel(
        signal_date=signal_date, entity_type=entity_type, entity_code=entity_code,
        benchmark_type=benchmark_type, benchmark_code=benchmark_code, horizon=horizon, label_type=label_type,
        entry_date=entry_date, exit_date=exit_date, price_basis=price_basis, signal_close=signal_close,
        entry_price=entry_price, exit_price=exit_price, entry_gap=entry_gap, forward_return=forward_return,
        benchmark_return=benchmark_return, excess_return=(forward_return - benchmark_return) if excess_complete else None,
        mae=mae, mfe=mfe, return_status=return_status, path_status=path_status,
        benchmark_status=benchmark_status, is_complete=complete, excess_is_complete=excess_complete,
        source_snapshot_id=source_snapshot_id, snapshot_mode=snapshot_mode,
    )
