"""Tests for trend universe loader."""

from datetime import date, timedelta

import pytest

from morning_conference.sector_rotation2.research.stock_alpha.common import (
    TREND_FOLLOW_PLAYBOOK,
    load_sector_close_series,
    load_sector_membership,
    load_stock_close_series,
    load_stock_universe,
)
from morning_conference.sector_rotation2.research.stock_alpha.config import TrendAlphaConfig


def _config() -> TrendAlphaConfig:
    return TrendAlphaConfig()


def _recent_date(days_ago: int) -> date:
    """Return a date ``days_ago`` calendar days before 2026-08-17."""

    return date(2026, 8, 17) - timedelta(days=days_ago)


def _status_rows() -> list[dict]:
    return [
        {"stock_code": "600000", "listing_date": date(2024, 1, 2), "is_suspended": False,
         "is_tradable": True, "sector_1": "Bank", "sector_2": "State Bank"},
        # Listed only 30 days ago: should be filtered out by the listing_age gate.
        {"stock_code": "000001", "listing_date": _recent_date(30), "is_suspended": False,
         "is_tradable": True, "sector_1": "Bank", "sector_2": "Joint Bank"},
        {"stock_code": "300750", "listing_date": date(2018, 6, 1), "is_suspended": True,
         "is_tradable": True, "sector_1": "Tech", "sector_2": "EV Battery"},
        {"stock_code": "688001", "listing_date": date(2019, 7, 22), "is_suspended": False,
         "is_tradable": False, "sector_1": "Tech", "sector_2": "Chip"},
        {"stock_code": "601318", "listing_date": date(2007, 2, 1), "is_suspended": False,
         "is_tradable": True, "sector_1": "Insurance", "sector_2": "Insurance"},
    ]


def _stub_query(sql: str, params: tuple) -> list[dict]:
    normalized = " ".join(sql.split())
    if "AS sector_name" in normalized:
        field = "sector_1" if "sector_1" in normalized else "sector_2"
        return [{"stock_code": code, "sector_name": row[field]} for row in _status_rows()
                for code in [row["stock_code"]]]
    if "FROM trade_stock_status" in normalized and "GROUP BY" not in normalized:
        return _status_rows()
    return []


def test_trend_follow_playbook_constant() -> None:
    assert TREND_FOLLOW_PLAYBOOK == "trend_follow"


def test_load_sector_membership_groups_stocks_by_sector() -> None:
    grouped = load_sector_membership({"Bank", "Tech"}, sector_level=1, as_of_date=date(2026, 8, 17), query=_stub_query)
    assert set(grouped) == {"Bank", "Tech"}
    assert "600000" in grouped["Bank"]
    assert "300750" in grouped["Tech"]


def test_load_stock_universe_drops_stocks_below_min_listing_age() -> None:
    rows = load_stock_universe(
        as_of_date=date(2026, 8, 17),
        sector_names={"Bank"},
        sector_level=1,
        config=_config(),
        query=_stub_query,
    )
    codes = {row.stock_code for row in rows}
    # 000001 listed 30 days ago: too recently for the 120-day gate.
    assert "000001" not in codes
    assert "600000" in codes


def test_load_stock_universe_drops_suspended_stocks() -> None:
    rows = load_stock_universe(
        as_of_date=date(2026, 8, 17),
        sector_names={"Tech"},
        sector_level=1,
        config=_config(),
        query=_stub_query,
    )
    codes = {row.stock_code for row in rows}
    assert "300750" not in codes
    assert "688001" not in codes


def test_load_stock_universe_does_not_drop_stocks_when_price_history_is_missing() -> None:
    """Price history is now deferred to feature computation, not universe gating."""

    cfg = TrendAlphaConfig(min_price_history=60)
    rows = load_stock_universe(
        as_of_date=date(2026, 8, 17),
        sector_names={"Bank"},
        sector_level=1,
        config=cfg,
        query=_stub_query,
    )
    codes = {row.stock_code for row in rows}
    assert "000001" not in codes  # listing_age gate still applies
    assert "600000" in codes


def test_load_stock_universe_only_includes_requested_sectors() -> None:
    rows = load_stock_universe(
        as_of_date=date(2026, 8, 17),
        sector_names={"Bank"},
        sector_level=1,
        config=_config(),
        query=_stub_query,
    )
    sector_names = {row.sector_name for row in rows}
    assert sector_names == {"Bank"}


def test_load_stock_universe_emits_current_mapping_quality() -> None:
    rows = load_stock_universe(
        as_of_date=date(2026, 8, 17),
        sector_names={"Insurance"},
        sector_level=1,
        config=_config(),
        query=_stub_query,
    )
    assert rows and rows[0].mapping_quality == "current_mapping"


def test_load_stock_universe_records_eligibility_unknown_when_metadata_missing() -> None:
    def _query(sql: str, params: tuple) -> list[dict]:
        normalized = " ".join(sql.split())
        if "AS sector_name" in normalized:
            return [{"stock_code": "999999", "sector_name": "Bank"}]
        if "FROM trade_stock_status" in normalized and "GROUP BY" not in normalized:
            return [{"stock_code": "999999", "sector_1": "Bank"}]
        return []

    rows = load_stock_universe(
        as_of_date=date(2026, 8, 17),
        sector_names={"Bank"},
        sector_level=1,
        config=_config(),
        query=_query,
    )
    assert rows and rows[0].stock_code == "999999"
    assert "listing_date" in rows[0].eligibility_unknown
    assert "is_suspended" in rows[0].eligibility_unknown
    assert "is_tradable" in rows[0].eligibility_unknown


def test_load_stock_universe_returns_empty_when_no_sector_matches() -> None:
    rows = load_stock_universe(
        as_of_date=date(2026, 8, 17),
        sector_names={"Unseen"},
        sector_level=1,
        config=_config(),
        query=_stub_query,
    )
    assert rows == []


def test_load_stock_close_series_returns_qfq_prices() -> None:
    def _query(sql: str, params: tuple) -> list[dict]:
        return [
            {"stock_code": "600000", "trade_date": date(2026, 8, 16), "close": 10.0, "volume": 100, "amount": 1000.0},
            {"stock_code": "600000", "trade_date": date(2026, 8, 17), "close": 11.0, "volume": 110, "amount": 1100.0},
        ]

    series = load_stock_close_series(["600000"], as_of_date=date(2026, 8, 17), query=_query)
    assert series == {"600000": {date(2026, 8, 16): 10.0, date(2026, 8, 17): 11.0}}


def test_load_stock_close_series_batches_large_input() -> None:
    calls: list[int] = []

    def _query(sql: str, params: tuple) -> list[dict]:
        normalized = " ".join(sql.split())
        in_match = normalized.split("IN (", 1)[1]
        codes_section = in_match.split(")")[0]
        n = len([c for c in codes_section.split(",") if c.strip()])
        calls.append(n)
        return []

    codes = [f"{i:06d}" for i in range(250)]
    load_stock_close_series(codes, date(2026, 8, 17), query=_query, batch_size=100)
    assert calls == [100, 100, 50]


def test_load_stock_close_series_accepts_bounded_history() -> None:
    captured = {}
    def _query(sql: str, params: tuple) -> list[dict]:
        captured['sql'] = sql
        captured['params'] = params
        return []
    load_stock_close_series(['600000'], date(2026, 8, 17), query=_query,
                            start_date=date(2025, 8, 17))
    assert 'trade_date BETWEEN %s AND %s' in captured['sql']
    assert captured['params'] == (date(2025, 8, 17), date(2026, 8, 17), '600000')


def test_load_sector_close_series_returns_close_index() -> None:
    def _query(sql: str, params: tuple) -> list[dict]:
        return [
            {"sector_name": "Bank", "trade_date": date(2026, 8, 17), "close": 1000.0},
        ]

    series = load_sector_close_series(["Bank"], sector_level=1, as_of_date=date(2026, 8, 17), query=_query)
    assert series == {"Bank": {date(2026, 8, 17): 1000.0}}


def test_config_validates_alpha_weights_sum_to_one() -> None:
    with pytest.raises(ValueError, match="alpha_weights must sum to 1.0"):
        TrendAlphaConfig(alpha_weights=(0.6, 0.3, 0.2))
