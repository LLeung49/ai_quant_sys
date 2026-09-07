from datetime import date
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.contracts import (
    AssetLayer,
    InstrumentType,
    LayeredInstrument,
    SubLayer,
    SubLayerBudget,
)
from asset_allocation.etf_adaptive.layers import assign_sub_layer, validate_sub_layer


AS_OF_DATE = date(2026, 9, 1)


def _instrument(**overrides: object) -> LayeredInstrument:
    values: dict[str, object] = {
        "stock_code": "510880.SH",
        "as_of_date": AS_OF_DATE,
        "instrument_type": InstrumentType.ETF,
        "style": "dividend_low_vol",
        "exposure": "domestic_dividend_low_vol",
        "is_qdii": False,
    }
    values.update(overrides)
    return LayeredInstrument(**values)  # type: ignore[arg-type]


def test_assign_sub_layer_maps_only_the_approved_etf_paths() -> None:
    assert assign_sub_layer(_instrument()) is SubLayer.DEFENSIVE_DIVIDEND_ETF
    assert assign_sub_layer(
        _instrument(style=None, exposure="domestic_core")
    ) is SubLayer.DOMESTIC_CORE
    assert assign_sub_layer(
        _instrument(style=None, exposure="domestic_growth")
    ) is SubLayer.DOMESTIC_GROWTH
    assert assign_sub_layer(
        _instrument(
            stock_code="513100.SH",
            style=None,
            exposure="nasdaq_or_sp500",
            is_qdii=True,
        )
    ) is SubLayer.OVERSEAS_MATURE
    assert assign_sub_layer(
        _instrument(
            stock_code="513130.SH",
            style=None,
            exposure="hk_offshore_china",
            is_qdii=True,
        )
    ) is SubLayer.HONG_KONG_OFFSHORE


def test_assign_sub_layer_allows_stocks_only_with_official_dividend_membership() -> None:
    approved = _instrument(
        stock_code="601088.SH",
        instrument_type=InstrumentType.STOCK,
        is_official_dividend_low_vol_constituent=True,
    )

    assert assign_sub_layer(approved) is SubLayer.DEFENSIVE_BLUE_CHIP
    assert approved.asset_layer is AssetLayer.DEFENSIVE
    assert validate_sub_layer(approved) is SubLayer.DEFENSIVE_BLUE_CHIP

    with pytest.raises(ValueError, match="outside approved layered universe"):
        assign_sub_layer(
            _instrument(
                stock_code="601088.SH",
                instrument_type=InstrumentType.STOCK,
                is_official_dividend_low_vol_constituent=False,
            )
        )


@pytest.mark.parametrize(
    "instrument",
    [
        _instrument(stock_code="518880.SH", style=None, exposure="gold"),
        _instrument(stock_code="511010.SH", style=None, exposure="debt"),
        _instrument(stock_code="511880.SH", style=None, exposure="cash"),
        _instrument(exposure="nasdaq_or_sp500", is_qdii=False),
        _instrument(exposure="domestic_core", is_qdii=True),
    ],
)
def test_assign_sub_layer_fails_closed_for_unapproved_or_misclassified_assets(
    instrument: LayeredInstrument,
) -> None:
    with pytest.raises(ValueError, match="outside approved layered universe"):
        assign_sub_layer(instrument)


def test_sub_layer_budget_requires_a_positive_decimal_for_an_approved_sub_layer() -> None:
    budget = SubLayerBudget(SubLayer.DOMESTIC_CORE, Decimal("42000"))

    assert budget.asset_layer is AssetLayer.BROAD_BETA
    assert budget.budget == Decimal("42000")

    with pytest.raises(ValueError, match="positive finite Decimal"):
        SubLayerBudget(SubLayer.DOMESTIC_CORE, Decimal("0"))
