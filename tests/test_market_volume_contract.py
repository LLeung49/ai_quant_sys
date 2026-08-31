import pytest

from data_ingestion.market_volume_contract import assess_volume, normalize_to_lot


def test_assess_volume_classifies_lot_from_amount_price_relation():
    result = assess_volume(amount=1_000_000, close_price=10, volume=1_000)

    assert result.unit == "lot"
    assert result.normalized_volume == 1_000


def test_normalize_to_lot_converts_share_values():
    assert normalize_to_lot(amount=1_000_000, close_price=10, volume=100_000) == 1_000


def test_normalize_to_lot_rounds_non_multiple_share_values_to_nearest_lot():
    assert normalize_to_lot(amount=1_000_500, close_price=10, volume=100_050) == 1_001


def test_normalize_to_lot_rejects_unclassifiable_values():
    with pytest.raises(ValueError, match="cannot classify volume unit"):
        normalize_to_lot(amount=1_000_000, close_price=10, volume=37_000)
