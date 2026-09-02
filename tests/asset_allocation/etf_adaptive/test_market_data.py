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
    METADATA_SQL,
    AdaptiveMarketDataProvider,
    to_raw_distance,
    to_raw_price,
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
        if "trade_stock_status" in sql:
            return self.metadata
        if "trade_corporate_action" in sql:
            return self.actions
        raise AssertionError(f"unexpected query: {sql}")

    def provider(self, **overrides: object) -> AdaptiveMarketDataProvider:
        calendar_loader = lambda _start, _end: tuple(
            sorted(
                {
                    day
                    for row in self.raw
                    if isinstance((day := row.get("trade_date")), date)
                }
            )
        )
        provenance_loader = lambda code, as_of_date: {
            "stock_code": code,
            "as_of_date": as_of_date,
            "latest_action_date": self.latest_action,
            "complete": True,
            "source": "authoritative-test-snapshot",
        }
        options: dict[str, object] = {
            "calendar_loader": calendar_loader,
            "adjustment_provenance_loader": provenance_loader,
        }
        options.update(overrides)
        return AdaptiveMarketDataProvider(query=self, **options)  # type: ignore[arg-type]


def test_provider_loads_one_row_per_coordinate_and_uses_same_day_ratio() -> None:
    query = QueryFixture()
    provider = query.provider()

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
    assert [issue.code for issue in provider.last_quality_issues] == [
        "unverified_pre_close"
    ]
    assert provider.last_quality_issues[0].trade_date == END
    assert len(query.calls) == 2
    assert "FROM trade_stock_daily_raw" in query.calls[0][0]
    assert "FROM trade_stock_daily_qfq" in query.calls[1][0]
    assert query.calls[0][1] == (CODE, START, END)
    assert query.calls[1][1] == (CODE, START, END)


def test_signal_coordinate_round_trip_uses_same_day_ratio() -> None:
    assert to_signal_price(4.08, 0.25) == pytest.approx(1.02)
    assert to_raw_distance(0.05, 0.25) == pytest.approx(0.20)


def test_signal_and_raw_price_conversion_is_a_round_trip() -> None:
    assert to_signal_price(4.08, 0.25) == pytest.approx(1.02)
    assert to_raw_price(1.02, 0.25) == pytest.approx(4.08)


def test_raw_price_conversion_rejects_underflow_to_zero() -> None:
    with pytest.raises(ValueError, match="result must be positive"):
        to_raw_price(5e-324, 1e308)


@pytest.mark.parametrize(
    ("conversion", "left", "right"),
    [
        (to_signal_price, 1e308, 1e308),
        (to_raw_distance, 1e308, 1e-308),
    ],
)
def test_coordinate_conversions_reject_non_finite_results(
    conversion: object, left: float, right: float
) -> None:
    with pytest.raises(ValueError, match="result must be finite"):
        conversion(left, right)  # type: ignore[operator]


def test_provider_rejects_dates_missing_from_either_price_coordinate() -> None:
    provider = QueryFixture(qfq=[]).provider()

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
        query.provider().load_bars(CODE, START, END)


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
        query.provider().load_bars(CODE, START, END)


def test_provider_wraps_malformed_source_identity_as_data_quality_error() -> None:
    query = QueryFixture(raw=[_raw_row(stock_code=None)])

    with pytest.raises(DataQualityError, match="invalid raw stock_code"):
        query.provider().load_bars(CODE, START, END)


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
        query.provider().load_bars(CODE, START, END)


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
        query.provider().load_bars(CODE, START, END)


def test_provider_rejects_unknown_suspend_flag_instead_of_assuming_tradable() -> None:
    query = QueryFixture(raw=[_raw_row(suspend_flag=None)])

    with pytest.raises(DataQualityError, match="invalid suspend_flag"):
        query.provider().load_bars(CODE, START, END)


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
            adjustment_asof=date(2026, 8, 15),
        ),
        _qfq_row(adjustment_asof=date(2026, 8, 15)),
    ]
    provider = QueryFixture(
        raw=raw, qfq=qfq, latest_action=date(2026, 8, 15)
    ).provider()

    bars = provider.load_bars(CODE, START, END)

    assert len(bars) == 2
    assert [issue.code for issue in provider.last_quality_issues] == [
        "missing_pre_close",
        "inconsistent_pre_close",
    ]
    assert [issue.trade_date for issue in provider.last_quality_issues] == [
        START,
        END,
    ]


def test_provider_rejects_adjustment_version_after_historical_end_date() -> None:
    provider = QueryFixture(
            qfq=[_qfq_row(adjustment_asof=date(2026, 9, 2))],
            latest_action=END,
        ).provider()

    with pytest.raises(DataQualityError, match="after requested end_date") as raised:
        provider.load_bars(CODE, START, END)

    assert [issue.code for issue in raised.value.issues] == [
        "future_adjustment_asof"
    ]


def test_provider_rejects_action_query_returning_event_after_end_date() -> None:
    provider = QueryFixture(latest_action=date(2026, 9, 2)).provider()

    with pytest.raises(DataQualityError, match="after requested end_date") as raised:
        provider.load_bars(CODE, START, END)

    assert [issue.code for issue in raised.value.issues] == [
        "future_latest_action_date"
    ]


def test_provider_rejects_adjustment_version_unequal_to_bounded_action() -> None:
    provider = QueryFixture(
            qfq=[_qfq_row(adjustment_asof=date(2026, 8, 1))],
            latest_action=date(2026, 8, 15),
        ).provider()

    with pytest.raises(DataQualityError, match="does not match") as raised:
        provider.load_bars(CODE, START, END)

    assert [issue.code for issue in raised.value.issues] == [
        "adjustment_asof_mismatch"
    ]


def test_provider_accepts_null_adjustment_provenance_when_no_action_exists() -> None:
    provider = QueryFixture(
            qfq=[_qfq_row(adjustment_asof=None)],
            latest_action=None,
        ).provider()

    bars = provider.load_bars(CODE, START, END)

    assert len(bars) == 1
    assert [issue.code for issue in provider.last_quality_issues] == [
        "unverified_pre_close"
    ]


def test_null_adjustment_pair_is_not_proof_without_authoritative_source() -> None:
    provider = AdaptiveMarketDataProvider(
        query=QueryFixture(
            qfq=[_qfq_row(adjustment_asof=None)], latest_action=None
        ),
        calendar_loader=lambda _start, _end: (END,),
    )

    with pytest.raises(
        DataQualityError, match="adjustment provenance unavailable"
    ) as raised:
        provider.load_bars(CODE, START, END)

    assert raised.value.issues[0].code == "adjustment_provenance_unavailable"


def test_injected_authoritative_source_can_establish_no_action_state() -> None:
    provider = AdaptiveMarketDataProvider(
        query=QueryFixture(
            qfq=[_qfq_row(adjustment_asof=None)], latest_action=None
        ),
        calendar_loader=lambda _start, _end: (END,),
        adjustment_provenance_loader=lambda code, as_of_date: {
            "stock_code": code,
            "as_of_date": as_of_date,
            "latest_action_date": None,
            "complete": True,
            "source": "authoritative-test-snapshot",
        },
    )

    bars = provider.load_bars(CODE, START, END)

    assert len(bars) == 1


def test_provider_requires_calendar_for_bar_loading() -> None:
    provider = AdaptiveMarketDataProvider(query=QueryFixture())

    with pytest.raises(DataQualityError, match="market calendar unavailable") as raised:
        provider.load_bars(CODE, START, END)

    assert raised.value.issues[0].code == "market_calendar_unavailable"


def test_provider_rejects_aligned_rows_absent_from_authoritative_calendar() -> None:
    provider = AdaptiveMarketDataProvider(
        query=QueryFixture(),
        calendar_loader=lambda _start, _end: (),
        adjustment_provenance_loader=lambda code, as_of_date: {
            "stock_code": code,
            "as_of_date": as_of_date,
            "latest_action_date": date(2026, 8, 15),
            "complete": True,
            "source": "authoritative-test-snapshot",
        },
    )

    with pytest.raises(DataQualityError, match="not in authoritative calendar") as raised:
        provider.load_bars(CODE, START, END)

    assert raised.value.issues[0].code == "unexpected_market_session"


def test_provider_detects_session_missing_from_both_price_coordinates() -> None:
    missing = date(2026, 8, 31)
    start = date(2026, 8, 30)
    raw = [_raw_row(start), _raw_row(END)]
    qfq = [_qfq_row(start), _qfq_row(END)]

    def calendar_loader(requested_start: date, requested_end: date) -> tuple[date, ...]:
        assert (requested_start, requested_end) == (start, END)
        return (start, missing, END)

    provider = QueryFixture(raw=raw, qfq=qfq).provider(
        calendar_loader=calendar_loader
    )

    with pytest.raises(DataQualityError, match="expected market session is missing") as raised:
        provider.load_bars(CODE, start, END)

    assert raised.value.issues[0].code == "missing_market_session"
    assert raised.value.issues[0].trade_date == missing


def test_provider_accepts_expected_suspended_session_with_aligned_rows() -> None:
    raw = [_raw_row(START, suspend_flag=1), _raw_row(END)]
    qfq = [_qfq_row(START), _qfq_row(END)]
    provider = QueryFixture(raw=raw, qfq=qfq).provider(
        calendar_loader=lambda _start, _end: (START, END)
    )

    bars = provider.load_bars(CODE, START, END)

    assert [bar.suspended for bar in bars] == [True, False]


def test_provider_reports_unavailable_market_calendar_as_quality_error() -> None:
    def unavailable(_start: date, _end: date) -> tuple[date, ...]:
        raise RuntimeError("calendar unavailable")

    provider = QueryFixture().provider(calendar_loader=unavailable)

    with pytest.raises(DataQualityError, match="market calendar unavailable") as raised:
        provider.load_bars(CODE, START, END)

    assert raised.value.issues[0].code == "market_calendar_unavailable"


def test_first_bar_pre_close_is_unverified_even_when_later_bar_confirms() -> None:
    raw = [
        _raw_row(
            START,
            open_price=Decimal("3.90"),
            high_price=Decimal("4.10"),
            low_price=Decimal("3.80"),
            close_price=Decimal("4.00"),
            pre_close=Decimal("3.90"),
        ),
        _raw_row(pre_close=Decimal("4.00")),
    ]
    qfq = [
        _qfq_row(
            START,
            open_price=Decimal("0.975"),
            high_price=Decimal("1.025"),
            low_price=Decimal("0.950"),
            close_price=Decimal("1.000"),
        ),
        _qfq_row(),
    ]
    provider = QueryFixture(raw=raw, qfq=qfq).provider()

    provider.load_bars(CODE, START, END)

    assert [issue.code for issue in provider.last_quality_issues] == [
        "unverified_pre_close"
    ]
    assert provider.last_quality_issues[0].trade_date == START


def test_current_metadata_source_fails_closed_with_provenance_issues() -> None:
    metadata_rows = [
        {
            "stock_code": CODE,
            "fund_name": "沪深300ETF",
            "listing_date": date(2012, 5, 28),
        }
    ]
    query = QueryFixture(metadata=metadata_rows)
    provider = AdaptiveMarketDataProvider(query=query)

    with pytest.raises(DataQualityError, match="point-in-time ETF metadata unavailable") as raised:
        provider.load_metadata(END)

    assert [issue.code for issue in raised.value.issues] == [
        "point_in_time_metadata_unavailable",
        "classification_provenance_unavailable",
    ]
    assert len(query.calls) == 1
    assert "FROM trade_stock_status" in query.calls[0][0]
    assert "listing_date IS NULL" in METADATA_SQL
    assert "LEFT(stock_code, 3)" in METADATA_SQL
    assert query.calls[0][1] == (END,)


def test_current_metadata_source_reports_unknown_listing_date() -> None:
    row = {"stock_code": CODE, "fund_name": "CSI 300 ETF", "listing_date": None}
    provider = AdaptiveMarketDataProvider(query=QueryFixture(metadata=[row]))

    with pytest.raises(DataQualityError) as raised:
        provider.load_metadata(END)

    assert "unknown_listing_date" in [
        issue.code for issue in raised.value.issues
    ]


def test_current_metadata_source_rejects_non_etf_candidate_rows() -> None:
    row = {
        "stock_code": "600000.SH",
        "fund_name": "Pudong Development Bank",
        "listing_date": date(1999, 11, 10),
    }
    provider = AdaptiveMarketDataProvider(query=QueryFixture(metadata=[row]))

    with pytest.raises(DataQualityError) as raised:
        provider.load_metadata(END)

    assert "metadata_non_etf_candidate" in [
        issue.code for issue in raised.value.issues
    ]


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
                "share_reform_flag": 0,
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
    assert "share_reform_flag" in query.calls[0][0]
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
        "share_reform_flag": 0,
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
        "share_reform_flag": 0,
    }

    with pytest.raises(DataQualityError, match="invalid corporate action stock_code"):
        AdaptiveMarketDataProvider(
            query=QueryFixture(actions=[row])
        ).load_actions(CODE, START, END)


def test_load_actions_rejects_missing_share_reform_provenance() -> None:
    row: dict[str, object] = {
        "stock_code": CODE,
        "ex_date": END,
        "cash_dividend_per_share": Decimal("0.08"),
        "stock_bonus_per_share": Decimal("0"),
        "stock_gift_per_share": Decimal("0"),
        "rights_issue_per_share": Decimal("0"),
        "rights_issue_price": None,
    }
    provider = AdaptiveMarketDataProvider(query=QueryFixture(actions=[row]))

    with pytest.raises(
        DataQualityError,
        match="missing corporate action value: share_reform_flag",
    ) as raised:
        provider.load_actions(CODE, START, END)

    assert [issue.code for issue in raised.value.issues] == [
        "invalid_corporate_action_value"
    ]
    assert provider.last_quality_issues == raised.value.issues


@pytest.mark.parametrize(
    "missing_field",
    [
        "cash_dividend_per_share",
        "stock_bonus_per_share",
        "stock_gift_per_share",
        "rights_issue_per_share",
    ],
)
def test_load_actions_rejects_missing_action_rates(missing_field: str) -> None:
    row: dict[str, object] = {
        "stock_code": CODE,
        "ex_date": END,
        "cash_dividend_per_share": Decimal("0.08"),
        "stock_bonus_per_share": Decimal("0"),
        "stock_gift_per_share": Decimal("0"),
        "rights_issue_per_share": Decimal("0"),
        "rights_issue_price": None,
        "share_reform_flag": 0,
    }
    row[missing_field] = None

    with pytest.raises(DataQualityError, match="missing corporate action value"):
        AdaptiveMarketDataProvider(
            query=QueryFixture(actions=[row])
        ).load_actions(CODE, START, END)


@pytest.mark.parametrize(
    ("overrides", "message"),
    [
        ({"rights_issue_price": Decimal("2.50")}, "unsupported rights issue"),
        ({"rights_issue_price": "bad"}, "invalid rights_issue_price"),
        ({"share_reform_flag": 1}, "unsupported corporate action payload"),
    ],
)
def test_load_actions_rejects_unmodelled_payload_fields(
    overrides: dict[str, object], message: str
) -> None:
    row: dict[str, object] = {
        "stock_code": CODE,
        "ex_date": END,
        "cash_dividend_per_share": Decimal("0"),
        "stock_bonus_per_share": Decimal("0"),
        "stock_gift_per_share": Decimal("0"),
        "rights_issue_per_share": Decimal("0"),
        "rights_issue_price": None,
        "share_reform_flag": 0,
    }
    row.update(overrides)

    with pytest.raises(DataQualityError, match=message):
        AdaptiveMarketDataProvider(
            query=QueryFixture(actions=[row])
        ).load_actions(CODE, START, END)


def test_load_actions_rejects_all_zero_unmodelled_action_row() -> None:
    row: dict[str, object] = {
        "stock_code": CODE,
        "ex_date": END,
        "cash_dividend_per_share": Decimal("0"),
        "stock_bonus_per_share": Decimal("0"),
        "stock_gift_per_share": Decimal("0"),
        "rights_issue_per_share": Decimal("0"),
        "rights_issue_price": None,
        "share_reform_flag": 0,
    }

    with pytest.raises(DataQualityError, match="unmodelled corporate action"):
        AdaptiveMarketDataProvider(
            query=QueryFixture(actions=[row])
        ).load_actions(CODE, START, END)
