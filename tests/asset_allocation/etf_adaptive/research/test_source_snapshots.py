"""Offline tests for auditable AkShare source snapshots."""

from __future__ import annotations

from datetime import date, datetime

import pytest

from asset_allocation.etf_adaptive.research.source_snapshots import (
    AkShareSnapshotClient,
)








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
