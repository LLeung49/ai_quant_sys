"""Fixed-universe contracts for independent ETF strategy validation."""

from dataclasses import dataclass
from enum import Enum

from ..contracts import SubLayer


class ValidationStatus(str, Enum):
    PASSED = "passed"
    FAILED = "failed"
    DATA_REJECTED = "data_rejected"


@dataclass(frozen=True)
class ValidationTarget:
    exposure_id: str
    stock_code: str
    sub_layer: SubLayer

    def __post_init__(self) -> None:
        if not isinstance(self.exposure_id, str) or not self.exposure_id.strip():
            raise ValueError("exposure_id must be a non-empty string")
        if not isinstance(self.stock_code, str) or not self.stock_code.strip():
            raise ValueError("stock_code must be a non-empty string")
        if not isinstance(self.sub_layer, SubLayer):
            raise ValueError("sub_layer must be a SubLayer")


FIXED_VALIDATION_TARGETS = (
    ValidationTarget("sp_china_low_vol_dividend", "515450.SH", SubLayer.DEFENSIVE_DIVIDEND_ETF),
    ValidationTarget("csi_dividend", "515080.SH", SubLayer.DEFENSIVE_DIVIDEND_ETF),
    ValidationTarget("csi_300", "510300.SH", SubLayer.DOMESTIC_CORE),
    ValidationTarget("csi_a500", "563360.SH", SubLayer.DOMESTIC_CORE),
    ValidationTarget("chinext", "159915.SZ", SubLayer.DOMESTIC_GROWTH),
    ValidationTarget("star_50", "588000.SH", SubLayer.DOMESTIC_GROWTH),
    ValidationTarget("nasdaq_100", "513100.SH", SubLayer.OVERSEAS_MATURE),
    ValidationTarget("sp_500", "513500.SH", SubLayer.OVERSEAS_MATURE),
    ValidationTarget("hang_seng_tech", "513130.SH", SubLayer.HONG_KONG_OFFSHORE),
    ValidationTarget("hang_seng_internet_technology", "513330.SH", SubLayer.HONG_KONG_OFFSHORE),
)


def evaluate_validation_gate(*, annual_excess: float, drawdown_excess: float, non_lagging_windows: int, total_windows: int) -> ValidationStatus:
    if total_windows <= 0:
        raise ValueError("total_windows must be positive")
    return ValidationStatus.PASSED if (annual_excess > 0.0 and drawdown_excess <= 0.02 and non_lagging_windows > total_windows / 2) else ValidationStatus.FAILED
