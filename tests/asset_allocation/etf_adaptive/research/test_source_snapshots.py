"""Offline tests for auditable MiniQMT and AkShare source snapshots."""

from __future__ import annotations

from datetime import date, datetime

import pytest

from asset_allocation.etf_adaptive.research.source_snapshots import (
    AkShareSnapshotClient,
    MiniQmtSnapshotClient,
)


class _MiniQmtClient:
    def get_instrument_detail(self, code: str, *, iscomplete: bool) -> dict[str, object]:
        assert code == "513100.SH"
        assert iscomplete is True
        return {
            "InstrumentID": "513100",
            "ExchangeID": "SH",
            "InstrumentName": "纳斯达克100ETF",
            "OpenDate": "20130515",
        }

    def get_instrument_type(self, code: str) -> str:
        assert code == "513100.SH"
        return "ETF"

    def get_trading_calendar(self, market: str, start: str, end: str) -> tuple[str, ...]:
        assert (market, start, end) == ("SH", "20240102", "20240103")
        return ("20240102", "20240103")


def test_miniqmt_instrument_snapshot_preserves_verified_etf_identity() -> None:
    snapshot = MiniQmtSnapshotClient(
        _MiniQmtClient(),
        clock=lambda: datetime(2024, 6, 30, 15, 0),
    ).instrument("513100.SH", date(2024, 6, 30))

    assert snapshot.source_name == "miniqmt"
    assert snapshot.source_kind == "instrument"
    assert snapshot.as_of_date == date(2024, 6, 30)
    assert snapshot.payload["code"] == "513100.SH"
    assert snapshot.payload["instrument_type"] == "ETF"
    assert snapshot.payload["detail"]["InstrumentID"] == "513100"
    assert len(snapshot.source_hash) == 64


def test_miniqmt_calendar_rejects_malformed_session() -> None:
    class MalformedCalendarClient(_MiniQmtClient):
        def get_trading_calendar(self, market: str, start: str, end: str) -> tuple[str, ...]:
            return ("20240102", "not-a-date")

    client = MiniQmtSnapshotClient(MalformedCalendarClient())

    with pytest.raises(ValueError, match="invalid MiniQMT calendar"):
        client.calendar("SH", date(2024, 1, 2), date(2024, 1, 3))


def test_akshare_overview_extracts_tracking_benchmark_and_fees() -> None:
    class AkShareClient:
        def fund_overview_em(self, *, symbol: str) -> dict[str, object]:
            assert symbol == "513100"
            return {
                "基金简称": "国泰纳斯达克100ETF",
                "跟踪标的": "纳斯达克100指数",
                "管理费率": "0.60%",
                "托管费率": "0.20%",
            }

    snapshot = AkShareSnapshotClient(AkShareClient()).fund_overview(
        "513100.SH", datetime(2024, 6, 30, 15, 0)
    )

    assert snapshot.source_name == "akshare"
    assert snapshot.source_kind == "fund_overview"
    assert snapshot.payload == {
        "code": "513100",
        "fund_name": "国泰纳斯达克100ETF",
        "tracking_benchmark": "纳斯达克100指数",
        "management_fee": 0.006,
        "custody_fee": 0.002,
    }


def test_miniqmt_instrument_rejects_unavailable_provider_response() -> None:
    class UnavailableMiniQmtClient:
        def get_instrument_detail(self, _code: str, *, iscomplete: bool) -> None:
            assert iscomplete is True
            return None

        def get_instrument_type(self, _code: str) -> str:
            return "ETF"

    client = MiniQmtSnapshotClient(UnavailableMiniQmtClient())

    with pytest.raises(ValueError, match="MiniQMT instrument unavailable"):
        client.instrument("513100.SH", date(2024, 6, 30))
