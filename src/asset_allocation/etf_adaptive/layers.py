"""Fail-closed assignment to approved adaptive-equity sub-layers."""

from .contracts import InstrumentType, LayeredInstrument, SubLayer


def assign_sub_layer(instrument: LayeredInstrument) -> SubLayer:
    """Return the sole approved sub-layer for an instrument or reject it.

    Classification inputs are intentionally restrictive: all assets outside the
    documented equity sleeves, and every ambiguous combination, are rejected.
    Historical constituent evidence is represented by the stock contract and
    must be present before a stock can enter the blue-chip path.
    """

    if not isinstance(instrument, LayeredInstrument):
        raise ValueError("instrument must be a LayeredInstrument")

    if instrument.instrument_type is InstrumentType.STOCK:
        if (
            not instrument.is_qdii
            and instrument.style == "dividend_low_vol"
            and instrument.exposure == "domestic_dividend_low_vol"
            and instrument.is_official_dividend_low_vol_constituent
        ):
            return SubLayer.DEFENSIVE_BLUE_CHIP
        raise ValueError("instrument is outside approved layered universe")

    if instrument.instrument_type is InstrumentType.ETF:
        if not instrument.is_qdii:
            if (
                instrument.style == "dividend_low_vol"
                and instrument.exposure == "domestic_dividend_low_vol"
            ):
                return SubLayer.DEFENSIVE_DIVIDEND_ETF
            if instrument.exposure == "domestic_core":
                return SubLayer.DOMESTIC_CORE
            if instrument.exposure == "domestic_growth":
                return SubLayer.DOMESTIC_GROWTH
        elif instrument.exposure == "nasdaq_or_sp500":
            return SubLayer.OVERSEAS_MATURE
        elif instrument.exposure == "hk_offshore_china":
            return SubLayer.HONG_KONG_OFFSHORE

    raise ValueError("instrument is outside approved layered universe")


def validate_sub_layer(instrument: LayeredInstrument) -> SubLayer:
    """Validate and return the approved assignment, failing closed otherwise."""

    return assign_sub_layer(instrument)
