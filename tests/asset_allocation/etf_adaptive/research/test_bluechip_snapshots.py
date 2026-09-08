from datetime import date, datetime

import pytest

from asset_allocation.etf_adaptive.research.bluechip_snapshots import (
    capture_constituent_snapshot,
)


def test_capture_constituent_snapshot_requires_dated_weighted_members() -> None:
    class Client:
        def index_constituents(self, index_code: str, as_of_date: date):
            assert (index_code, as_of_date) == ("H30269.CSI", date(2024, 1, 2))
            return {
                "as_of_date": "2024-01-02",
                "constituents": [
                    {"stock_code": "600900.SH", "weight": 0.6},
                    {"stock_code": "601088.SH", "weight": 0.4},
                ],
            }

    basket = capture_constituent_snapshot(
        "H30269.CSI",
        date(2024, 1, 2),
        Client(),
        clock=lambda: datetime(2024, 1, 3, 9, 30),
    )

    assert [member.stock_code for member in basket.members] == ["600900.SH", "601088.SH"]
    assert all(member.source_hash == basket.members[0].source_hash for member in basket.members)


def test_capture_constituent_snapshot_rejects_missing_as_of_or_weight() -> None:
    class MissingDateClient:
        def index_constituents(self, _index_code: str, _as_of_date: date):
            return {"constituents": [{"stock_code": "600900.SH", "weight": 1.0}]}

    class MissingWeightClient:
        def index_constituents(self, _index_code: str, _as_of_date: date):
            return {"as_of_date": "2024-01-02", "constituents": [{"stock_code": "600900.SH"}]}

    with pytest.raises(ValueError, match="as_of_date"):
        capture_constituent_snapshot("H30269.CSI", date(2024, 1, 2), MissingDateClient())
    with pytest.raises(ValueError, match="weight"):
        capture_constituent_snapshot("H30269.CSI", date(2024, 1, 2), MissingWeightClient())
