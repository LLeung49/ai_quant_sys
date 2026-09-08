from datetime import date, datetime

import pytest

from asset_allocation.etf_adaptive.research.bluechip_snapshots import (
    BlueChipSnapshotStore,
    capture_constituent_snapshot,
)
from asset_allocation.etf_adaptive.research.bluechip_basket import BlueChipBasket, BlueChipConstituent
from asset_allocation.etf_adaptive.research.source_snapshots import SourceSnapshot


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


def test_snapshot_store_writes_source_before_its_pit_members() -> None:
    calls: list[tuple[str, tuple[object, ...]]] = []

    class Cursor:
        def execute(self, sql: str, params: tuple[object, ...]) -> None:
            calls.append((sql, params))

        def close(self) -> None:
            pass

    class Connection:
        def cursor(self) -> Cursor:
            return Cursor()

        def commit(self) -> None:
            calls.append(("commit", ()))

        def rollback(self) -> None:
            calls.append(("rollback", ()))

        def close(self) -> None:
            pass

    source = SourceSnapshot("index_provider", "index_constituents", datetime(2024, 1, 3, 9, 30), date(2024, 1, 2), {"index_code": "H30269.CSI"}, "a" * 64)
    basket = BlueChipBasket("H30269.CSI", date(2024, 1, 2), (BlueChipConstituent("600900.SH", 1.0, "a" * 64),))

    BlueChipSnapshotStore(connection_factory=Connection).persist(source, basket)

    assert "asset_allocation_etf_research_source_snapshot" in calls[0][0]
    assert "asset_allocation_etf_research_constituent_pit" in calls[1][0]
    assert calls[-1] == ("commit", ())
