"""Immutable domain contracts for point-in-time adaptive ETF data."""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from enum import Enum
import math


def _require_non_empty_text(value: str, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")


def _validate_optional_text(value: str | None, field_name: str) -> None:
    if value is not None:
        _require_non_empty_text(value, field_name)


def _validate_positive_decimal(value: Decimal, field_name: str) -> None:
    if not isinstance(value, Decimal) or not value.is_finite() or value <= 0:
        raise ValueError(f"{field_name} must be a positive finite Decimal")


@dataclass(frozen=True)
class DualPriceBar:
    stock_code: str
    trade_date: date
    signal_open: float
    signal_high: float
    signal_low: float
    signal_close: float
    raw_open: float
    raw_high: float
    raw_low: float
    raw_close: float
    amount: float
    suspended: bool
    adjustment_ratio: float

    def __post_init__(self) -> None:
        prices = (
            self.signal_open,
            self.signal_high,
            self.signal_low,
            self.signal_close,
            self.raw_open,
            self.raw_high,
            self.raw_low,
            self.raw_close,
        )
        if any(not math.isfinite(value) or value <= 0 for value in prices):
            raise ValueError("prices must be positive finite numbers")
        if not math.isfinite(self.amount) or self.amount < 0:
            raise ValueError("amount must be a non-negative finite number")
        if not math.isfinite(self.adjustment_ratio) or self.adjustment_ratio <= 0:
            raise ValueError("adjustment_ratio must be positive")


@dataclass(frozen=True)
class ETFMetadata:
    stock_code: str
    fund_name: str
    listing_date: date
    fund_type: str | None = None
    tracking_index_code: str | None = None
    tracking_index_name: str | None = None
    is_cross_border: bool = False
    is_leveraged: bool = False

    def __post_init__(self) -> None:
        _require_non_empty_text(self.stock_code, "stock_code")
        _require_non_empty_text(self.fund_name, "fund_name")
        _validate_optional_text(self.fund_type, "fund_type")
        _validate_optional_text(self.tracking_index_code, "tracking_index_code")
        _validate_optional_text(self.tracking_index_name, "tracking_index_name")


class CorporateActionType(str, Enum):
    CASH_DIVIDEND = "cash_dividend"
    SHARE_SPLIT = "share_split"


@dataclass(frozen=True)
class CorporateAction:
    stock_code: str
    effective_date: date
    action_type: CorporateActionType
    cash_per_share: Decimal | None
    share_multiplier: Decimal

    def __post_init__(self) -> None:
        _require_non_empty_text(self.stock_code, "stock_code")
        if not isinstance(self.action_type, CorporateActionType):
            raise ValueError("action_type must be a CorporateActionType")
        _validate_positive_decimal(self.share_multiplier, "share_multiplier")
        if self.action_type is CorporateActionType.CASH_DIVIDEND:
            if self.cash_per_share is None:
                raise ValueError("cash_per_share is required for cash dividends")
            _validate_positive_decimal(self.cash_per_share, "cash_per_share")
        elif self.cash_per_share is not None:
            raise ValueError("cash_per_share must be omitted for share splits")


@dataclass(frozen=True)
class ETFEligibility:
    eligible: bool
    rejection_reasons: tuple[str, ...]
    exposure_group: str | None
    history_session_count: int
    average_amount_20d: float | None

    def __post_init__(self) -> None:
        if not isinstance(self.rejection_reasons, tuple):
            raise ValueError("rejection_reasons must be a tuple")
        for reason in self.rejection_reasons:
            _require_non_empty_text(reason, "rejection_reasons entries")
        if self.eligible and self.rejection_reasons:
            raise ValueError("eligible decisions cannot have rejection reasons")
        if not self.eligible and not self.rejection_reasons:
            raise ValueError("ineligible decisions must have rejection reasons")
        _validate_optional_text(self.exposure_group, "exposure_group")
        if isinstance(self.history_session_count, bool) or self.history_session_count < 0:
            raise ValueError("history_session_count must be a non-negative integer")
        if self.average_amount_20d is not None and (
            not math.isfinite(self.average_amount_20d) or self.average_amount_20d < 0
        ):
            raise ValueError("average_amount_20d must be a non-negative finite number")


@dataclass(frozen=True)
class DataQualityIssue:
    code: str | Enum
    stock_code: str
    trade_date: date | None
    message: str

    def __post_init__(self) -> None:
        code = self.code.value if isinstance(self.code, Enum) else self.code
        _require_non_empty_text(code, "code")
        _require_non_empty_text(self.stock_code, "stock_code")
        _require_non_empty_text(self.message, "message")


class DataQualityError(ValueError):
    """Raised when one or more data-quality issues prevent processing."""

    def __init__(self, message: str, issues: tuple[DataQualityIssue, ...] = ()) -> None:
        super().__init__(message)
        if not isinstance(issues, tuple) or not all(
            isinstance(issue, DataQualityIssue) for issue in issues
        ):
            raise ValueError("issues must be a tuple of DataQualityIssue instances")
        self.issues = issues
