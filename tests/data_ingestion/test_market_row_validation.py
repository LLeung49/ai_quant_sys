import math

import pytest

from data_ingestion.market_row_validation import (
    validate_market_row,
    validate_projection_batch,
)
from data_ingestion import price_projection_store as store
from data_ingestion import akshare_market_fallback as fallback


def row(**overrides):
    value = {
        "stock_code": "600519.SH",
        "trade_date": "2026-09-18",
        "open_price": 10.0,
        "high_price": 11.0,
        "low_price": 9.0,
        "close_price": 10.5,
        "volume": 100,
        "amount": 1000.0,
    }
    value.update(overrides)
    return value


@pytest.mark.parametrize("field", ["open_price", "high_price", "low_price", "close_price"])
@pytest.mark.parametrize("bad_value", [0, math.nan, math.inf, -math.inf])
def test_raw_and_hfq_reject_zero_or_non_finite_prices(field, bad_value):
    result = validate_market_row(row(**{field: bad_value}))

    assert not result.is_valid
    assert any(issue.field == field for issue in result.issues)


def test_valid_market_row_passes():
    result = validate_market_row(row())

    assert result.is_valid
    assert not result.quarantined
    assert result.issues == ()


def test_price_that_database_would_round_to_zero_is_rejected():
    result = validate_market_row(row(
        open_price=0.0000001,
        high_price=0.0000002,
        low_price=0.0000001,
        close_price=0.0000001,
    ), allow_negative_price=True)

    assert not result.is_valid
    assert {issue.code for issue in result.issues} == {
        "zero_price_after_storage_rounding"
    }


def test_negative_qfq_is_preserved_but_quarantined():
    result = validate_market_row(
        row(open_price=-2.0, high_price=-1.0, low_price=-3.0, close_price=-1.5),
        allow_negative_price=True,
    )

    assert result.is_valid
    assert result.quarantined
    assert {issue.code for issue in result.issues} == {"negative_adjusted_price"}


@pytest.mark.parametrize(
    "overrides",
    [
        {"high_price": 8.0},
        {"low_price": 10.6},
        {"volume": -1},
        {"amount": -0.01},
    ],
)
def test_invalid_ohlc_or_negative_trading_values_are_rejected(overrides):
    assert not validate_market_row(row(**overrides)).is_valid


def test_projection_batch_requires_same_dates_and_volume_amount():
    raw = row()
    qfq = row()
    hfq = row(amount=1001.0)

    result = validate_projection_batch({"none": [raw], "front": [qfq], "back": [hfq]})

    assert not result.is_valid
    assert any(issue.code == "projection_volume_amount_mismatch" for issue in result.issues)


def test_projection_batch_accepts_aligned_modes():
    result = validate_projection_batch(
        {"none": [row()], "front": [row()], "back": [row()]}
    )

    assert result.is_valid


@pytest.mark.parametrize("writer", ["single", "batch"])
def test_zero_price_never_reaches_execute_many(monkeypatch, writer):
    calls = []
    monkeypatch.setattr(store, "execute_many", lambda sql, values: calls.append(values))
    bad_rows = [row(open_price=0, high_price=0, low_price=0, close_price=0)]

    with pytest.raises(ValueError, match="zero_price"):
        if writer == "single":
            store.write_daily_rows("none", bad_rows, adjustment_asof=None)
        else:
            store.write_daily_rows_batch("none", bad_rows, adjustment_asofs={})

    assert calls == []


def test_akshare_fallback_rejects_zero_price_frame():
    pd = pytest.importorskip("pandas")
    frame = pd.DataFrame(
        [{
            "trade_date": "2026-09-18",
            "open": 0,
            "high": 0,
            "low": 0,
            "close": 0,
            "volume": 0,
            "amount": 0,
        }]
    )

    rows, failures = fallback._select_target_rows(frame, {"2026-09-18"})

    assert rows == {}
    assert "invalid market values" in failures["2026-09-18"]
