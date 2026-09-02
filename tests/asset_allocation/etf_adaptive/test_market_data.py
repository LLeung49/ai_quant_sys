from __future__ import annotations

from datetime import date
from decimal import Decimal
from typing import Any

import pytest

from asset_allocation.etf_adaptive.contracts import (
    CorporateActionType,
    DataQualityError,
)
from asset_allocation.etf_adaptive.market_data import (
    AdaptiveMarketDataProvider,
    to_raw_distance,
    to_signal_price,
)


START = date(2026, 8, 31)
END = date(2026, 9, 1)
CODE = "510300.SH"


def _raw_row(day: date = END, **overrides: object) -> dict[str, object]:
    row: dict[str, object] = {
        "stock_code": CODE,
        "trade_date": day,
        "open_price": Decimal("4.00"),
        "high_price": Decimal("4.40"),
        "low_price": Decimal("3.60"),
        "close_price": Decimal("4.08"),
        "amount": Decimal("20000000.00"),
        "pre_close": Decimal("4.00"),
        "suspend_flag": 0,
    }
    row.update(overrides)
    return row


def _qfq_row(day: date = END, **overrides: object) -> dict[str, object]:
    row: dict[str, object] = {
        "stock_code": CODE,
        "trade_date": day,
        "open_price": Decimal("1.00"),
        "high_price": Decimal("1.10"),
        "low_price": Decimal("0.90"),
        "close_price": Decimal("1.02"),
        "adjustment_asof": date(2026, 8, 15),
    }
    row.update(overrides)
    return row


class QueryFixture:
    def __init__(
        self,
        *,
        raw: list[dict[str, object]] | None = None,
        qfq: list[dict[str, object]] | None = None,
        latest_action: date | None = date(2026, 8, 15),
        metadata: list[dict[str, object]] | None = None,
        actions: list[dict[str, object]] | None = None,
    ) -> None:
        self.raw = [_raw_row()] if raw is None else raw
        self.qfq = [_qfq_row()] if qfq is None else qfq
        self.latest_action = latest_action
        self.metadata = [] if metadata is None else metadata
        self.actions = [] if actions is None else actions
        self.calls: list[tuple[str, tuple[object, ...]]] = []

    def __call__(self, sql: str, params: tuple[object, ...]) -> list[dict[str, Any]]:
        self.calls.append((sql, params))
        if "trade_stock_daily_raw" in sql:
            return self.raw
        if "trade_stock_daily_qfq" in sql:
            return self.qfq
        if "MAX(ex_date)" in sql:
            return [{"latest_action_date": self.latest_action}]
        if "trade_stock_status" in sql:
            return self.metadata
        if "trade_corporate_action" in sql:
            return self.actions
        raise AssertionError(f"unexpected query: {sql}")


def test_provider_loads_one_row_per_coordinate_and_uses_same_day_ratio() -> None:
    query = QueryFixture()
    provider = AdaptiveMarketDataProvider(query=query)

    bars = provider.load_bars(CODE, START, END)

    assert len(bars) == 1
    bar = bars[0]
    assert bar.stock_code == CODE
    assert bar.trade_date == END
    assert bar.signal_close == pytest.approx(1.02)
    assert bar.raw_close == pytest.approx(4.08)
    assert bar.amount == pytest.approx(20_000_000.0)
    assert bar.suspended is False
    assert bar.adjustment_ratio == pytest.approx(0.25)
    assert provider.last_quality_issues == ()
    assert len(query.calls) == 3
    assert "FROM trade_stock_daily_raw" in query.calls[0][0]
    assert "FROM trade_stock_daily_qfq" in query.calls[1][0]
    assert "MAX(ex_date)" in query.calls[2][0]
    assert query.calls[0][1] == (CODE, START, END)
    assert query.calls[1][1] == (CODE, START, END)
    assert query.calls[2][1] == (CODE,)


def test_signal_coordinate_round_trip_uses_same_day_ratio() -> None:
    assert to_signal_price(4.08, 0.25) == pytest.approx(1.02)
    assert to_raw_distance(0.05, 0.25) == pytest.approx(0.20)


def test_provider_rejects_dates_missing_from_either_price_coordinate() -> None:
    provider = AdaptiveMarketDataProvider(query=QueryFixture(qfq=[]))

    with pytest.raises(DataQualityError, match="raw/qfq date mismatch"):
        provider.load_bars(CODE, START, END)

    assert [issue.code for issue in provider.last_quality_issues] == [
        "raw_qfq_date_mismatch"
    ]


@pytest.mark.parametrize("table", ["raw", "qfq"])
def test_provider_rejects_duplicate_dates_before_alignment(table: str) -> None:
    rows = [_raw_row(), _raw_row()] if table == "raw" else [_qfq_row(), _qfq_row()]
    query = QueryFixture(**{table: rows})

    with pytest.raises(DataQualityError, match=f"duplicate {table} trade_date"):
        AdaptiveMarketDataProvider(query=query).load_bars(CODE, START, END)


@pytest.mark.parametrize(
    ("table", "rows", "message"),
    [
        ("raw", [_raw_row(stock_code="510500.SH")], "raw stock_code mismatch"),
        ("qfq", [_qfq_row(stock_code="510500.SH")], "qfq stock_code mismatch"),
        ("raw", [_raw_row(date(2026, 9, 2))], "raw trade_date outside requested range"),
        ("qfq", [_qfq_row(date(2026, 9, 2))], "qfq trade_date outside requested range"),
    ],
)
def test_provider_never_substitutes_an_entity_or_date(
    table: str, rows: list[dict[str, object]], message: str
) -> None:
    query = QueryFixture(**{table: rows})

    with pytest.raises(DataQualityError, match=message):
        AdaptiveMarketDataProvider(query=query).load_bars(CODE, START, END)


def test_provider_wraps_malformed_source_identity_as_data_quality_error() -> None:
    query = QueryFixture(raw=[_raw_row(stock_code=None)])

    with pytest.raises(DataQualityError, match="invalid raw stock_code"):
        AdaptiveMarketDataProvider(query=query).load_bars(CODE, START, END)


@pytest.mark.parametrize(
    ("raw_overrides", "qfq_overrides", "message"),
    [
        ({"close_price": Decimal("0")}, {}, "invalid raw close_price"),
        ({}, {"close_price": Decimal("0")}, "invalid qfq close_price"),
        ({"high_price": Decimal("3.90")}, {}, "invalid raw OHLC"),
        ({}, {"low_price": Decimal("1.03")}, "invalid qfq OHLC"),
        ({}, {"high_price": Decimal("1.11")}, "inconsistent raw/qfq OHLC ratio"),
    ],
)
def test_provider_rejects_invalid_prices_ohlc_and_adjustment_ratios(
    raw_overrides: dict[str, object],
    qfq_overrides: dict[str, object],
    message: str,
) -> None:
    query = QueryFixture(
        raw=[_raw_row(**raw_overrides)],
        qfq=[_qfq_row(**qfq_overrides)],
    )

    with pytest.raises(DataQualityError, match=message):
        AdaptiveMarketDataProvider(query=query).load_bars(CODE, START, END)


def test_ratio_tolerance_is_relative_for_small_adjustment_factors() -> None:
    query = QueryFixture(
        raw=[
            _raw_row(
                open_price=Decimal("10000"),
                high_price=Decimal("11000"),
                low_price=Decimal("9000"),
                close_price=Decimal("10000"),
            )
        ],
        qfq=[
            _qfq_row(
                open_price=Decimal("1"),
                high_price=Decimal("1.101"),
                low_price=Decimal("0.9"),
                close_price=Decimal("1"),
            )
        ],
    )

    with pytest.raises(DataQualityError, match="inconsistent raw/qfq OHLC ratio"):
        AdaptiveMarketDataProvider(query=query).load_bars(CODE, START, END)


def test_provider_rejects_unknown_suspend_flag_instead_of_assuming_tradable() -> None:
    query = QueryFixture(raw=[_raw_row(suspend_flag=None)])

    with pytest.raises(DataQualityError, match="invalid suspend_flag"):
        AdaptiveMarketDataProvider(query=query).load_bars(CODE, START, END)


def test_provider_reports_pre_close_and_adjustment_provenance_deterministically() -> None:
    raw = [
        _raw_row(
            START,
            open_price=Decimal("3.90"),
            high_price=Decimal("4.10"),
            low_price=Decimal("3.80"),
            close_price=Decimal("4.00"),
            pre_close=None,
        ),
        _raw_row(pre_close=Decimal("3.95")),
    ]
    qfq = [
        _qfq_row(
            START,
            open_price=Decimal("0.975"),
            high_price=Decimal("1.025"),
            low_price=Decimal("0.950"),
            close_price=Decimal("1.000"),
            adjustment_asof=None,
        ),
        _qfq_row(adjustment_asof=date(2026, 8, 1)),
    ]
    provider = AdaptiveMarketDataProvider(
        query=QueryFixture(raw=raw, qfq=qfq, latest_action=date(2026, 8, 15))
    )

    bars = provider.load_bars(CODE, START, END)

    assert len(bars) == 2
    assert [issue.code for issue in provider.last_quality_issues] == [
        "missing_pre_close",
        "missing_adjustment_asof",
        "inconsistent_pre_close",
        "stale_adjustment_asof",
        "inconsistent_adjustment_asof",
    ]
    assert [issue.trade_date for issue in provider.last_quality_issues] == [
        START,
        START,
        END,
        END,
        None,
    ]


def test_load_metadata_reads_only_rows_listed_by_the_as_of_date() -> None:
    metadata_rows = [
        {
            "stock_code": CODE,
            "fund_name": "沪深300ETF",
            "listing_date": date(2012, 5, 28),
        }
    ]
    query = QueryFixture(metadata=metadata_rows)
    provider = AdaptiveMarketDataProvider(query=query)

    result = provider.load_metadata(END)

    assert len(result) == 1
    assert result[0].stock_code == CODE
    assert result[0].listing_date == date(2012, 5, 28)
    assert result[0].fund_type is None
    assert result[0].is_cross_border is False
    assert len(query.calls) == 1
    assert "FROM trade_stock_status" in query.calls[0][0]
    assert "fund_type" not in query.calls[0][0]
    assert query.calls[0][1] == (END,)


def test_load_metadata_rejects_future_and_duplicate_rows_from_adapter() -> None:
    row = {
        "stock_code": CODE,
        "fund_name": "沪深300ETF",
        "listing_date": date(2026, 9, 2),
        "is_cross_border": 0,
        "is_leveraged": 0,
    }

    with pytest.raises(DataQualityError, match="metadata listing_date after as_of_date"):
        AdaptiveMarketDataProvider(query=QueryFixture(metadata=[row])).load_metadata(END)

    row["listing_date"] = date(2012, 5, 28)
    with pytest.raises(DataQualityError, match="duplicate metadata stock_code"):
        AdaptiveMarketDataProvider(query=QueryFixture(metadata=[row, dict(row)])).load_metadata(END)


def test_load_metadata_wraps_malformed_source_identity_as_data_quality_error() -> None:
    row = {
        "stock_code": None,
        "fund_name": "沪深300ETF",
        "listing_date": date(2012, 5, 28),
    }

    with pytest.raises(DataQualityError, match="invalid metadata stock_code"):
        AdaptiveMarketDataProvider(query=QueryFixture(metadata=[row])).load_metadata(END)


def test_load_actions_converts_cash_and_share_events_without_date_substitution() -> None:
    query = QueryFixture(
        actions=[
            {
                "stock_code": CODE,
                "ex_date": END,
                "cash_dividend_per_share": Decimal("0.08"),
                "stock_bonus_per_share": Decimal("0.10"),
                "stock_gift_per_share": Decimal("0.05"),
                "rights_issue_per_share": Decimal("0"),
                "rights_issue_price": None,
            }
        ]
    )
    provider = AdaptiveMarketDataProvider(query=query)

    actions = provider.load_actions(CODE, START, END)

    assert [action.action_type for action in actions] == [
        CorporateActionType.CASH_DIVIDEND,
        CorporateActionType.SHARE_SPLIT,
    ]
    assert actions[0].cash_per_share == Decimal("0.08")
    assert actions[1].cash_per_share is None
    assert actions[1].share_multiplier == Decimal("1.15")
    assert len(query.calls) == 1
    assert "FROM trade_corporate_action" in query.calls[0][0]
    assert query.calls[0][1] == (CODE, START, END)


@pytest.mark.parametrize(
    ("overrides", "message"),
    [
        ({"stock_code": "510500.SH"}, "corporate action stock_code mismatch"),
        ({"ex_date": date(2026, 9, 2)}, "corporate action date outside requested range"),
        ({"rights_issue_per_share": Decimal("0.1")}, "unsupported rights issue"),
    ],
)
def test_load_actions_rejects_entity_date_substitution_and_unsupported_rights(
    overrides: dict[str, object], message: str
) -> None:
    row: dict[str, object] = {
        "stock_code": CODE,
        "ex_date": END,
        "cash_dividend_per_share": Decimal("0.08"),
        "stock_bonus_per_share": Decimal("0"),
        "stock_gift_per_share": Decimal("0"),
        "rights_issue_per_share": Decimal("0"),
        "rights_issue_price": None,
    }
    row.update(overrides)

    with pytest.raises(DataQualityError, match=message):
        AdaptiveMarketDataProvider(
            query=QueryFixture(actions=[row])
        ).load_actions(CODE, START, END)


def test_load_actions_wraps_malformed_source_identity_as_data_quality_error() -> None:
    row: dict[str, object] = {
        "stock_code": None,
        "ex_date": END,
        "cash_dividend_per_share": Decimal("0.08"),
        "stock_bonus_per_share": Decimal("0"),
        "stock_gift_per_share": Decimal("0"),
        "rights_issue_per_share": Decimal("0"),
        "rights_issue_price": None,
    }

    with pytest.raises(DataQualityError, match="invalid corporate action stock_code"):
        AdaptiveMarketDataProvider(
            query=QueryFixture(actions=[row])
        ).load_actions(CODE, START, END)
