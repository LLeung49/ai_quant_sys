"""Canonical daily-market volume contract.

All persisted daily market volume is measured in lots (100 shares).  The
amount/price/volume relation makes a historical shares-vs-lots mix detectable
without relying on incomplete source provenance.
"""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Literal


VolumeUnit = Literal["lot", "share", "unknown"]
LOT_RATIO_MIN = Decimal("50")
LOT_RATIO_MAX = Decimal("150")
SHARE_RATIO_MIN = Decimal("0.5")
SHARE_RATIO_MAX = Decimal("2")
SHARES_PER_LOT = 100


@dataclass(frozen=True)
class VolumeAssessment:
    unit: VolumeUnit
    normalized_volume: int | None
    ratio: Decimal | None


def _ratio(amount: object, close_price: object, volume: object) -> Decimal | None:
    try:
        amount_value = Decimal(str(amount))
        close_value = Decimal(str(close_price))
        volume_value = int(volume)
    except (InvalidOperation, TypeError, ValueError):
        return None
    if amount_value <= 0 or close_value <= 0 or volume_value <= 0:
        return None
    return amount_value / (close_value * Decimal(volume_value))


def assess_volume(amount: object, close_price: object, volume: object) -> VolumeAssessment:
    """Classify a market row and return its canonical lot volume if known."""
    ratio = _ratio(amount, close_price, volume)
    if ratio is None:
        return VolumeAssessment("unknown", None, None)
    volume_value = int(volume)
    if LOT_RATIO_MIN <= ratio <= LOT_RATIO_MAX:
        return VolumeAssessment("lot", volume_value, ratio)
    if SHARE_RATIO_MIN <= ratio <= SHARE_RATIO_MAX:
        normalized = int(
            (Decimal(volume_value) / SHARES_PER_LOT).quantize(
                Decimal("1"), rounding=ROUND_HALF_UP
            )
        )
        return VolumeAssessment("share", normalized, ratio)
    return VolumeAssessment("unknown", None, ratio)


def normalize_to_lot(amount: object, close_price: object, volume: object) -> int:
    """Return canonical lot volume or fail closed for an ambiguous row."""
    assessment = assess_volume(amount, close_price, volume)
    if assessment.normalized_volume is None:
        raise ValueError("cannot classify volume unit")
    return assessment.normalized_volume
