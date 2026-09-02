from __future__ import annotations

from datetime import date, timedelta
import json
from pathlib import Path

import pytest

import asset_allocation.etf_adaptive.run_data_audit as audit_cli
from asset_allocation.etf_adaptive.contracts import (
    DataQualityError,
    DataQualityIssue,
    DualPriceBar,
    ETFMetadata,
)
from asset_allocation.etf_adaptive.market_data import (
    LATEST_ACTION_SQL,
    METADATA_SQL,
    QFQ_BARS_SQL,
    RAW_BARS_SQL,
    AdaptiveMarketDataProvider,
)
from asset_allocation.etf_adaptive.run_data_audit import audit_universe


AS_OF_DATE = date(2026, 9, 1)


def _bar(stock_code: str, trade_date: date) -> DualPriceBar:
    return DualPriceBar(
        stock_code=stock_code,
        trade_date=trade_date,
        signal_open=1.0,
        signal_high=1.1,
        signal_low=0.9,
        signal_close=1.0,
        raw_open=4.0,
        raw_high=4.4,
        raw_low=3.6,
        raw_close=4.0,
        amount=20_000_000.0,
        suspended=False,
        adjustment_ratio=0.25,
    )


class ProviderFixture:
    def __init__(self) -> None:
        self.last_quality_issues = ()
        self._metadata = (
            ETFMetadata(
                stock_code="510300.SH",
                fund_name="CSI 300 ETF",
                listing_date=date(2012, 5, 28),
                tracking_index_code="000300.SH",
            ),
            ETFMetadata(
                stock_code="513100.SH",
                fund_name="NASDAQ ETF",
                listing_date=date(2013, 5, 15),
                tracking_index_code="NDX",
                is_cross_border=True,
            ),
        )
        first_day = AS_OF_DATE - timedelta(days=251)
        self._bars = {
            metadata.stock_code: tuple(
                _bar(metadata.stock_code, first_day + timedelta(days=offset))
                for offset in range(252)
            )
            for metadata in self._metadata
        }

    def load_metadata(self, as_of_date: date) -> tuple[ETFMetadata, ...]:
        assert as_of_date == AS_OF_DATE
        self.last_quality_issues = ()
        return self._metadata

    def load_bars(
        self, stock_code: str, start_date: date, end_date: date
    ) -> tuple[DualPriceBar, ...]:
        assert end_date == AS_OF_DATE
        self.last_quality_issues = ()
        return self._bars[stock_code]


def _provider_fixture() -> ProviderFixture:
    return ProviderFixture()


def test_audit_reports_eligible_and_rejected_counts(tmp_path: Path) -> None:
    output = tmp_path / "audit.json"

    report = audit_universe(AS_OF_DATE, _provider_fixture(), output_path=output)

    assert report.eligible_count == 1
    assert report.rejected_by_reason["not_domestic_equity_etf"] == 1
    assert json.loads(output.read_text(encoding="utf-8"))["as_of_date"] == "2026-09-01"


def test_audit_summarizes_universe_groups_and_date_coverage() -> None:
    report = audit_universe(AS_OF_DATE, _provider_fixture())

    assert report.universe_count == 2
    assert report.eligible_count == 1
    assert report.rejected_count == 1
    assert report.eligible_by_exposure_group == {"core_broad": 1}
    assert {
        code: {
            "first_trade_date": coverage.first_trade_date,
            "last_trade_date": coverage.last_trade_date,
            "session_count": coverage.session_count,
        }
        for code, coverage in report.date_coverage.items()
    } == {
        "510300.SH": {
            "first_trade_date": "2025-12-24",
            "last_trade_date": "2026-09-01",
            "session_count": 252,
        },
        "513100.SH": {
            "first_trade_date": "2025-12-24",
            "last_trade_date": "2026-09-01",
            "session_count": 252,
        },
    }


class ManyRejectedProvider:
    def __init__(self) -> None:
        self.last_quality_issues = ()
        self.codes = tuple(f"510{number:03d}.SH" for number in range(900, 912))

    def load_metadata(self, as_of_date: date) -> tuple[ETFMetadata, ...]:
        self.last_quality_issues = ()
        return tuple(
            ETFMetadata(
                stock_code=code,
                fund_name="Unclassified sector ETF",
                listing_date=date(2020, 1, 1),
            )
            for code in reversed(self.codes)
        )

    def load_bars(
        self, stock_code: str, start_date: date, end_date: date
    ) -> tuple[DualPriceBar, ...]:
        self.last_quality_issues = ()
        first_day = AS_OF_DATE - timedelta(days=251)
        return tuple(
            _bar(stock_code, first_day + timedelta(days=offset))
            for offset in range(252)
        )


def test_audit_sorts_codes_and_reasons_and_caps_examples_at_ten() -> None:
    report = audit_universe(AS_OF_DATE, ManyRejectedProvider())

    assert list(report.date_coverage) == sorted(report.date_coverage)
    assert list(report.rejected_by_reason) == sorted(report.rejected_by_reason)
    assert report.rejected_by_reason == {"not_domestic_equity_etf": 12}
    assert report.examples_by_reason == {
        "not_domestic_equity_etf": tuple(
            f"510{number:03d}.SH" for number in range(900, 910)
        )
    }


class QualityIssueProvider(ProviderFixture):
    def __init__(self) -> None:
        super().__init__()
        self._metadata = (
            self._metadata[0],
            ETFMetadata(
                stock_code="510500.SH",
                fund_name="CSI 500 ETF",
                listing_date=date(2013, 3, 15),
                tracking_index_code="000905.SH",
            ),
        )

    def load_bars(
        self, stock_code: str, start_date: date, end_date: date
    ) -> tuple[DualPriceBar, ...]:
        if stock_code == "510500.SH":
            issue = DataQualityIssue(
                "raw_qfq_date_mismatch",
                stock_code,
                None,
                "raw/qfq date mismatch",
            )
            self.last_quality_issues = (issue,)
            raise DataQualityError("raw/qfq date mismatch", (issue,))

        bars = super().load_bars(stock_code, start_date, end_date)
        self.last_quality_issues = (
            DataQualityIssue(
                "stale_adjustment_asof",
                stock_code,
                date(2026, 8, 31),
                "stale adjustment version",
            ),
            DataQualityIssue(
                "stale_adjustment_asof",
                stock_code,
                AS_OF_DATE,
                "stale adjustment version",
            ),
        )
        return bars


def test_audit_counts_nonfatal_and_fatal_data_quality_issues() -> None:
    report = audit_universe(AS_OF_DATE, QualityIssueProvider())

    assert report.eligible_count == 1
    assert report.rejected_count == 1
    assert report.rejected_by_reason == {"data_quality_error": 1}
    assert report.data_quality_error_count == 3
    assert report.data_quality_by_reason == {
        "raw_qfq_date_mismatch": 1,
        "stale_adjustment_asof": 2,
    }
    assert report.raw_qfq_mismatch_count == 1
    assert report.stale_adjustment_version_count == 2
    assert report.examples_by_reason["raw_qfq_date_mismatch"] == ("510500.SH",)
    assert report.examples_by_reason["stale_adjustment_asof"] == ("510300.SH",)
    assert report.date_coverage["510500.SH"].session_count == 0


@pytest.mark.parametrize(
    ("provider", "expected_exit_code"),
    [(ProviderFixture(), 0), (QualityIssueProvider(), 2)],
)
def test_main_maps_data_quality_to_exit_code_and_writes_requested_json(
    provider: ProviderFixture,
    expected_exit_code: int,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output = tmp_path / f"audit-{expected_exit_code}.json"
    monkeypatch.setattr(audit_cli, "default_provider", lambda: provider)

    exit_code = audit_cli.main(
        ["--as-of-date", "2026-09-01", "--output-json", str(output)]
    )

    stdout = capsys.readouterr().out.strip()
    assert exit_code == expected_exit_code
    assert stdout == output.read_text(encoding="utf-8")
    assert json.loads(stdout)["data_quality_error_count"] == (
        0 if expected_exit_code == 0 else 3
    )


class MetadataErrorProvider:
    def __init__(self) -> None:
        self.last_quality_issues: tuple[DataQualityIssue, ...] = ()

    def load_metadata(self, as_of_date: date) -> tuple[ETFMetadata, ...]:
        issue = DataQualityIssue(
            "duplicate_metadata_stock_code",
            "510300.SH",
            None,
            "duplicate metadata stock_code",
        )
        self.last_quality_issues = (issue,)
        raise DataQualityError("duplicate metadata stock_code", (issue,))

    def load_bars(
        self, stock_code: str, start_date: date, end_date: date
    ) -> tuple[DualPriceBar, ...]:
        raise AssertionError("bars must not be loaded after metadata failure")


def test_audit_reports_metadata_quality_failure_without_loading_bars() -> None:
    report = audit_universe(AS_OF_DATE, MetadataErrorProvider())

    assert report.universe_count == 0
    assert report.eligible_count == 0
    assert report.rejected_count == 0
    assert report.data_quality_error_count == 1
    assert report.data_quality_by_reason == {"duplicate_metadata_stock_code": 1}
    assert report.examples_by_reason == {
        "duplicate_metadata_stock_code": ("510300.SH",)
    }


class UnclassifiedQualityErrorProvider:
    def __init__(self) -> None:
        self.last_quality_issues: tuple[DataQualityIssue, ...] = ()

    def load_metadata(self, as_of_date: date) -> tuple[ETFMetadata, ...]:
        raise DataQualityError("metadata source rejected the request")

    def load_bars(
        self, stock_code: str, start_date: date, end_date: date
    ) -> tuple[DualPriceBar, ...]:
        raise AssertionError("bars must not be loaded after metadata failure")


def test_audit_fails_closed_for_an_unclassified_quality_error() -> None:
    report = audit_universe(AS_OF_DATE, UnclassifiedQualityErrorProvider())

    assert report.data_quality_error_count == 1
    assert report.data_quality_by_reason == {"unclassified_data_quality_error": 1}


def test_default_provider_uses_authoritative_calendar_to_detect_shared_gap(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    missing = AS_OF_DATE - timedelta(days=1)

    def query(sql: str, params: tuple[object, ...]) -> tuple[dict[str, object], ...]:
        if sql == RAW_BARS_SQL:
            return (
                {
                    "stock_code": "510300.SH",
                    "trade_date": AS_OF_DATE,
                    "open_price": 4.0,
                    "high_price": 4.4,
                    "low_price": 3.6,
                    "close_price": 4.0,
                    "amount": 20_000_000.0,
                    "pre_close": 4.0,
                    "suspend_flag": False,
                },
            )
        if sql == QFQ_BARS_SQL:
            return (
                {
                    "stock_code": "510300.SH",
                    "trade_date": AS_OF_DATE,
                    "open_price": 1.0,
                    "high_price": 1.1,
                    "low_price": 0.9,
                    "close_price": 1.0,
                    "adjustment_asof": None,
                },
            )
        if sql == LATEST_ACTION_SQL:
            return ({"latest_action_date": None},)
        raise AssertionError(f"unexpected query: {sql!r}, {params!r}")

    monkeypatch.setattr(audit_cli, "execute_query", query)
    monkeypatch.setattr(
        audit_cli,
        "load_authoritative_market_calendar",
        lambda start, end, calendar_query: (start, end),
        raising=False,
    )

    provider = audit_cli.default_provider()
    with pytest.raises(DataQualityError) as raised:
        provider.load_bars("510300.SH", missing, AS_OF_DATE)

    assert raised.value.issues[0].code == "missing_market_session"


class FutureBarProvider(ProviderFixture):
    def load_bars(
        self, stock_code: str, start_date: date, end_date: date
    ) -> tuple[DualPriceBar, ...]:
        return super().load_bars(stock_code, start_date, end_date) + (
            _bar(stock_code, AS_OF_DATE + timedelta(days=1)),
        )


def test_audit_rejects_future_bars_and_excludes_them_from_coverage() -> None:
    report = audit_universe(AS_OF_DATE, FutureBarProvider())

    assert report.eligible_count == 0
    assert report.rejected_by_reason == {
        "bar_date_after_as_of_date": 2,
        "not_domestic_equity_etf": 1,
    }
    assert report.data_quality_error_count == 2
    assert report.data_quality_by_reason == {"bar_date_after_as_of_date": 2}
    assert report.date_coverage["510300.SH"].last_trade_date == "2026-09-01"
    assert report.date_coverage["510300.SH"].session_count == 252


def _adaptive_provider_with_no_actions() -> AdaptiveMarketDataProvider:
    first_day = AS_OF_DATE - timedelta(days=251)
    days = tuple(first_day + timedelta(days=offset) for offset in range(252))

    def query(sql: str, params: tuple[object, ...]) -> tuple[dict[str, object], ...]:
        if sql == METADATA_SQL:
            return (
                {
                    "stock_code": "510300.SH",
                    "fund_name": "CSI 300 ETF",
                    "listing_date": first_day,
                },
            )
        if sql == RAW_BARS_SQL:
            return tuple(
                {
                    "stock_code": "510300.SH",
                    "trade_date": day,
                    "open_price": 4.0,
                    "high_price": 4.4,
                    "low_price": 3.6,
                    "close_price": 4.0,
                    "amount": 20_000_000.0,
                    "pre_close": 4.0,
                    "suspend_flag": False,
                }
                for day in days
            )
        if sql == QFQ_BARS_SQL:
            return tuple(
                {
                    "stock_code": "510300.SH",
                    "trade_date": day,
                    "open_price": 1.0,
                    "high_price": 1.1,
                    "low_price": 0.9,
                    "close_price": 1.0,
                    "adjustment_asof": None,
                }
                for day in days
            )
        if sql == LATEST_ACTION_SQL:
            return ({"latest_action_date": None},)
        raise AssertionError(f"unexpected query: {sql!r}, {params!r}")

    class PointInTimeMetadataFixture(AdaptiveMarketDataProvider):
        def load_metadata(self, as_of_date: date) -> tuple[ETFMetadata, ...]:
            assert as_of_date == AS_OF_DATE
            self.last_quality_issues = ()
            return (
                ETFMetadata(
                    stock_code="510300.SH",
                    fund_name="CSI 300 ETF",
                    listing_date=first_day,
                    tracking_index_code="000300.SH",
                ),
            )

    return PointInTimeMetadataFixture(query=query)


def test_audit_accepts_null_adjustment_provenance_when_no_action_exists(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    provider = _adaptive_provider_with_no_actions()
    output = tmp_path / "audit.json"
    monkeypatch.setattr(audit_cli, "default_provider", lambda: provider)

    exit_code = audit_cli.main(
        ["--as-of-date", "2026-09-01", "--output-json", str(output)]
    )

    assert provider.last_quality_issues[0].code == "unverified_pre_close"
    assert exit_code == 0
    assert json.loads(output.read_text(encoding="utf-8"))["data_quality_error_count"] == 0


def test_audit_reports_current_metadata_source_limitations_without_loading_bars() -> None:
    calls: list[str] = []

    def query(sql: str, _params: tuple[object, ...]) -> tuple[dict[str, object], ...]:
        calls.append(sql)
        if sql == METADATA_SQL:
            return (
                {
                    "stock_code": "510300.SH",
                    "fund_name": "CSI 300 ETF",
                    "listing_date": date(2012, 5, 28),
                },
            )
        raise AssertionError("bar data must not be loaded from unversioned metadata")

    report = audit_universe(
        AS_OF_DATE, AdaptiveMarketDataProvider(query=query)
    )

    assert calls == [METADATA_SQL]
    assert report.universe_count == 0
    assert report.eligible_count == 0
    assert report.data_quality_by_reason == {
        "classification_provenance_unavailable": 1,
        "point_in_time_metadata_unavailable": 1,
    }
