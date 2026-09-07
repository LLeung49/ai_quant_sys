from __future__ import annotations

from datetime import date

import pytest

from asset_allocation.etf_adaptive.constituents import (
    HistoricalConstituentProvider,
    InMemoryHistoricalConstituentRepository,
    InMemoryInstrumentMetadataRepository,
)
from asset_allocation.etf_adaptive.contracts import (
    DataQualityError,
    DualPriceBar,
    ExecutionAvailability,
    InstrumentType,
)
from asset_allocation.etf_adaptive.market_data import LayeredMarketDataProvider


AS_OF = date(2025, 6, 1)


def _membership(**overrides: object) -> dict[str, object]:
    row: dict[str, object] = {
        "index_code": "H30269",
        "stock_code": "601088.SH",
        "effective_start": date(2025, 1, 1),
        "effective_end": date(2025, 6, 30),
    }
    row.update(overrides)
    return row


def _metadata(**overrides: object) -> dict[str, object]:
    row: dict[str, object] = {
        "stock_code": "601088.SH",
        "effective_start": date(2025, 1, 1),
        "effective_end": date(2025, 6, 30),
        "listing_date": date(2008, 1, 1),
        "instrument_type": "stock",
        "style": "dividend_low_vol",
        "exposure": "domestic_dividend_low_vol",
        "is_qdii": False,
        "sub_layer": "defensive_blue_chip",
    }
    row.update(overrides)
    return row


def _bar(code: str) -> DualPriceBar:
    return DualPriceBar(
        stock_code=code,
        trade_date=AS_OF,
        signal_open=1.0,
        signal_high=1.1,
        signal_low=0.9,
        signal_close=1.0,
        raw_open=4.0,
        raw_high=4.4,
        raw_low=3.6,
        raw_close=4.0,
        raw_pre_close=4.0,
        amount=20_000_000.0,
        suspended=False,
        adjustment_ratio=0.25,
        execution_availability=ExecutionAvailability(False, False, "exchange"),
    )


class FakePriceProvider:
    def load_bars(
        self, stock_code: str, start_date: date, end_date: date
    ) -> tuple[DualPriceBar, ...]:
        assert start_date == end_date == AS_OF
        return (_bar(stock_code),)


def _layered_provider(
    *,
    memberships: tuple[dict[str, object], ...] = (_membership(),),
    metadata: tuple[dict[str, object], ...] = (_metadata(),),
    provenance_complete: bool = True,
) -> LayeredMarketDataProvider:
    return LayeredMarketDataProvider(
        constituents=HistoricalConstituentProvider(
            InMemoryHistoricalConstituentRepository(memberships)
        ),
        metadata=InMemoryInstrumentMetadataRepository(metadata),
        prices=FakePriceProvider(),
        price_provenance=lambda code, as_of: {
            "stock_code": code,
            "as_of_date": as_of,
            "source": "authoritative-test-snapshot",
            "complete": provenance_complete,
        },
    )


def test_historical_constituents_select_only_the_effective_members() -> None:
    provider = HistoricalConstituentProvider(
        InMemoryHistoricalConstituentRepository(
            (
                _membership(),
                _membership(
                    stock_code="600000.SH",
                    effective_start=date(2025, 7, 1),
                    effective_end=date(2025, 12, 31),
                ),
            )
        )
    )

    assert provider.members(AS_OF, "H30269") == ("601088.SH",)


def test_historical_constituents_fail_closed_for_a_missing_effective_range() -> None:
    provider = HistoricalConstituentProvider(
        InMemoryHistoricalConstituentRepository((_membership(effective_start=None),))
    )

    with pytest.raises(DataQualityError) as raised:
        provider.members(AS_OF, "H30269")

    assert raised.value.issues[0].code == "missing_constituent_effective_range"


def test_layered_provider_loads_dated_stock_and_explicitly_classified_qdii() -> None:
    qdii_metadata = _metadata(
        stock_code="513100.SH",
        listing_date=date(2013, 5, 1),
        instrument_type="etf",
        style=None,
        exposure="nasdaq_or_sp500",
        is_qdii=True,
        sub_layer="broad_overseas_mature",
    )
    provider = _layered_provider(metadata=(_metadata(), qdii_metadata))

    instruments = provider.load_instruments(AS_OF)

    assert [(item.stock_code, item.instrument_type) for item in instruments] == [
        ("513100.SH", InstrumentType.ETF),
        ("601088.SH", InstrumentType.STOCK),
    ]


@pytest.mark.parametrize("metadata", [_metadata(listing_date=None), _metadata(sub_layer=None)])
def test_layered_provider_fails_closed_for_incomplete_metadata(
    metadata: dict[str, object],
) -> None:
    with pytest.raises(DataQualityError) as raised:
        _layered_provider(metadata=(metadata,)).load_instruments(AS_OF)

    assert raised.value.issues[0].code in {
        "missing_listing_date",
        "missing_instrument_classification",
    }


def test_layered_provider_fails_closed_without_trusted_price_provenance() -> None:
    with pytest.raises(DataQualityError) as raised:
        _layered_provider(provenance_complete=False).load_instruments(AS_OF)

    assert raised.value.issues[0].code == "price_provenance_unavailable"
