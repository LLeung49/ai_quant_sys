from datetime import date
from decimal import Decimal

from morning_conference.sector_rotation2.api.kline import normalize_sector_kline_rows


def valid_row(trade_date_value: str, **overrides: object) -> dict[str, object]:
    """构造一条有效候选行，并允许测试覆盖单个字段。"""
    row: dict[str, object] = {
        "trade_date": date.fromisoformat(trade_date_value),
        "open": 10.0,
        "high": 11.0,
        "low": 9.0,
        "close": 10.5,
        "volume": 1000.0,
        "amount": 2000.0,
    }
    row.update(overrides)
    return row


def test_normalize_sector_kline_rows_converts_decimal_and_shanghai_midnight() -> None:
    rows = [{
        "trade_date": date(2026, 8, 6),
        "open": Decimal("10.00"),
        "high": Decimal("11.00"),
        "low": Decimal("9.50"),
        "close": Decimal("10.50"),
        "volume": Decimal("1000"),
        "amount": Decimal("2000"),
    }]

    bars, skipped = normalize_sector_kline_rows(rows, date(2026, 8, 6))

    assert skipped == 0
    assert bars == [{
        "trade_date": "2026-08-06",
        "timestamp": 1785945600000,
        "open": 10.0,
        "high": 11.0,
        "low": 9.5,
        "close": 10.5,
        "volume": 1000.0,
        "amount": 2000.0,
    }]


def test_normalize_sector_kline_rows_skips_future_duplicate_nan_and_invalid_ohlc() -> None:
    rows = [
        valid_row("2026-08-04"),
        valid_row("2026-08-04"),
        valid_row("2026-08-05"),
        valid_row("2026-08-03", close=float("nan")),
        valid_row("2026-08-02", high=9.0, close=10.0),
    ]

    bars, skipped = normalize_sector_kline_rows(rows, date(2026, 8, 4))

    assert [bar["trade_date"] for bar in bars] == ["2026-08-04"]
    assert skipped == 4


def test_normalize_sector_kline_rows_skips_negative_volume_and_sorts_dates() -> None:
    rows = [
        valid_row("2026-08-04", volume=-1.0),
        valid_row("2026-08-03"),
        valid_row("2026-08-01", amount=-1.0),
        valid_row("2026-08-02", low=11.0),
        valid_row("2026-08-04"),
    ]

    bars, skipped = normalize_sector_kline_rows(rows, date(2026, 8, 4))

    assert [bar["trade_date"] for bar in bars] == ["2026-08-03", "2026-08-04"]
    assert skipped == 3
