from datetime import date

import pytest

from asset_allocation.etf_adaptive.research.bluechip_basket import BlueChipBasketRepository


def _row(**changes):
    row = {"index_code": "H30269.CSI", "as_of_date": date(2024, 1, 2), "stock_code": "600900.SH", "weight": 0.6, "source_hash": "a" * 64}
    row.update(changes)
    return row


def test_repository_resolves_source_hashed_weighted_basket() -> None:
    basket = BlueChipBasketRepository(lambda _sql, _params: (_row(), _row(stock_code="601088.SH", weight=0.4))).load("H30269.CSI", date(2024, 1, 2))
    assert basket.index_code == "H30269.CSI"
    assert {member.stock_code for member in basket.members} == {"600900.SH", "601088.SH"}


def test_repository_rejects_duplicate_member_or_invalid_weight_sum() -> None:
    duplicate = BlueChipBasketRepository(lambda _sql, _params: (_row(), _row()))
    with pytest.raises(ValueError, match="duplicate"):
        duplicate.load("H30269.CSI", date(2024, 1, 2))
    invalid = BlueChipBasketRepository(lambda _sql, _params: (_row(), _row(stock_code="601088.SH", weight=0.3)))
    with pytest.raises(ValueError, match="sum to 1"):
        invalid.load("H30269.CSI", date(2024, 1, 2))


def test_repository_rejects_empty_or_unhashed_pit_rows() -> None:
    with pytest.raises(ValueError, match="no PIT"):
        BlueChipBasketRepository(lambda _sql, _params: ()).load("H30269.CSI", date(2024, 1, 2))
    with pytest.raises(ValueError, match="source_hash"):
        BlueChipBasketRepository(lambda _sql, _params: (_row(source_hash=None),)).load("H30269.CSI", date(2024, 1, 2))
