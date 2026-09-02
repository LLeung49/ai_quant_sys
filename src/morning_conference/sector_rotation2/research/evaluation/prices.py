"""Price-bar interfaces used by evaluation labels.

Providers return bars keyed by their actual market date.  Callers must never
replace a requested calendar date with a nearby entity-specific bar.
"""

from dataclasses import dataclass
from datetime import date, datetime
from typing import Any, Callable, Iterable, Mapping, Protocol


@dataclass(frozen=True)
class PriceBar:
    trade_date: date
    close: float | None
    open: float | None = None
    high: float | None = None
    low: float | None = None


class PriceBarProvider(Protocol):
    def load_bars(self, entity_type: str, entity_code: str, start_date: date, end_date: date) -> Mapping[date, PriceBar]: ...

    def supports_open(self, entity_type: str) -> bool: ...

    def supports_ohlc(self, entity_type: str) -> bool: ...


class InMemoryPriceBarProvider:
    """Deterministic provider for label tests and offline evaluation logic."""

    def __init__(self, bars: Mapping[tuple[str, str], Mapping[date, PriceBar]], *, open_entities: set[str] | None = None,
                 ohlc_entities: set[str] | None = None) -> None:
        self._bars = {key: dict(value) for key, value in bars.items()}
        self._open_entities = frozenset(open_entities or ())
        self._ohlc_entities = frozenset(ohlc_entities or ())

    def load_bars(self, entity_type: str, entity_code: str, start_date: date, end_date: date) -> Mapping[date, PriceBar]:
        return {
            day: bar for day, bar in self._bars.get((entity_type, entity_code), {}).items()
            if start_date <= day <= end_date
        }

    def supports_open(self, entity_type: str) -> bool:
        return entity_type in self._open_entities

    def supports_ohlc(self, entity_type: str) -> bool:
        return entity_type in self._ohlc_entities


class MySQLPriceBarProvider:
    """Read-only adapter for existing sector and adjusted stock/ETF price tables."""

    _CLOSE_ONLY_TYPES = frozenset({"sector", "sector_l1", "sector_l2"})
    _OHLC_TYPES = frozenset({"stock", "etf"})

    def __init__(self, query: Callable[[str, tuple[object, ...]], list[dict[str, Any]]]) -> None:
        self._query = query

    def load_bars(self, entity_type: str, entity_code: str, start_date: date, end_date: date) -> Mapping[date, PriceBar]:
        if entity_type in self._CLOSE_ONLY_TYPES:
            rows = self._query(
                "SELECT trade_date, close_idx AS close FROM trade_sector_daily "
                "WHERE sector_name=%s AND trade_date BETWEEN %s AND %s ORDER BY trade_date",
                (entity_code, start_date, end_date),
            )
        elif entity_type in self._OHLC_TYPES:
            rows = self._query(
                "SELECT trade_date, open_price AS open, high_price AS high, low_price AS low, close_price AS close "
                "FROM trade_stock_daily_qfq WHERE stock_code=%s AND trade_date BETWEEN %s AND %s ORDER BY trade_date",
                (entity_code, start_date, end_date),
            )
        else:
            raise ValueError(f"unsupported evaluation entity_type: {entity_type}")
        return {
            trade_date: PriceBar(
                trade_date=trade_date, close=_float_or_none(row.get("close")), open=_float_or_none(row.get("open")),
                high=_float_or_none(row.get("high")), low=_float_or_none(row.get("low")),
            )
            for row in rows if (trade_date := _coerce_date(row.get("trade_date"))) is not None
        }

    def supports_open(self, entity_type: str) -> bool:
        return entity_type in self._OHLC_TYPES

    def supports_ohlc(self, entity_type: str) -> bool:
        return entity_type in self._OHLC_TYPES


def load_authoritative_market_calendar(
    start_date: date, end_date: date, query: Callable[[str, tuple[object, ...]], list[dict[str, Any]]], *, sector_level: int = 1,
    schedule_loader: Callable[[date, date], Iterable[date]] | None = None,
) -> tuple[date, ...]:
    """Load an A-share session schedule, including not-yet-priced future dates.

    Completed sector bars are sufficient for a fully historical window.  When
    the requested window extends beyond them, use the exchange-schedule
    boundary rather than guessing future sessions from price availability.
    """
    rows = query(
        "SELECT DISTINCT trade_date FROM trade_sector_daily WHERE sector_level=%s "
        "AND trade_date BETWEEN %s AND %s ORDER BY trade_date",
        (sector_level, start_date, end_date),
    )
    completed_dates = tuple(day for row in rows if (day := _coerce_date(row.get("trade_date"))) is not None)
    if completed_dates and completed_dates[-1] >= end_date:
        return completed_dates

    loader = schedule_loader or load_exchange_schedule
    try:
        scheduled_dates = tuple(sorted(set(loader(start_date, end_date))))
    except Exception as exc:
        raise RuntimeError(
            "authoritative exchange schedule unavailable for required future sessions "
            f"{start_date.isoformat()}..{end_date.isoformat()}"
        ) from exc
    if not scheduled_dates:
        raise RuntimeError(
            "authoritative exchange schedule unavailable for required future sessions "
            f"{start_date.isoformat()}..{end_date.isoformat()}"
        )
    return scheduled_dates


def load_exchange_schedule(start_date: date, end_date: date) -> tuple[date, ...]:
    """Read the published mainland-exchange session schedule through AkShare.

    This intentionally lives behind a small injectable boundary so operational
    runners can use future sessions while tests stay deterministic.
    """
    import akshare as ak

    frame = ak.tool_trade_date_hist_sina()
    if "trade_date" not in frame.columns:
        raise ValueError("exchange schedule response has no trade_date column")
    dates = tuple(
        day
        for value in frame["trade_date"].tolist()
        if (day := _coerce_date(value)) is not None and start_date <= day <= end_date
    )
    return tuple(sorted(set(dates)))


def _coerce_date(value: object) -> date | None:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if value is None:
        return None
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


def _float_or_none(value: object) -> float | None:
    try:
        return None if value is None else float(value)
    except (TypeError, ValueError):
        return None
