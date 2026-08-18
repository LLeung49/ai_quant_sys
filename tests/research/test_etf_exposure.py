import pytest

from morning_conference.sector_rotation2.research.etf_core.exposure import (
    aggregate_constituents,
    normalize_stock_code,
)


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("600000", "600000"),
        ("600000.SH", "600000"),
        ("SH600000", "600000"),
        ("000001.SZ", "000001"),
        ("sz.000001", "000001"),
        (" 300750 ", "300750"),
    ],
)
def test_normalize_stock_code_accepts_six_digit_market_variants(raw, expected):
    assert normalize_stock_code(raw) == expected


def test_aggregate_constituents_supports_code_alias_and_sums_duplicates():
    rows = [
        {"stock_code": "600000.SH", "weight": 0.12},
        {"code": "600000", "weight": 0.08},
        {"stock_code": "000001.SZ", "weight": 0.20},
    ]

    assert aggregate_constituents(rows) == {
        "600000": pytest.approx(0.20),
        "000001": pytest.approx(0.20),
    }


def test_aggregate_constituents_rejects_missing_code_or_weight():
    with pytest.raises(ValueError, match="stock code"):
        aggregate_constituents([{"weight": 0.1}])
    with pytest.raises(ValueError, match="weight"):
        aggregate_constituents([{"stock_code": "600000"}])
