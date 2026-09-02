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


def _require_date(value: date, field_name: str) -> None:
    if not isinstance(value, date):
        raise ValueError(f"{field_name} must be a date")


def _require_bool(value: bool, field_name: str) -> None:
    if not isinstance(value, bool):
        raise ValueError(f"{field_name} must be a bool")


def _validate_finite_float(
    value: float, field_name: str, *, allow_zero: bool
) -> None:
    if not isinstance(value, float) or not math.isfinite(value) or (
        value < 0 if allow_zero else value <= 0
    ):
        qualifier = "non-negative" if allow_zero else "positive"
        raise ValueError(f"{field_name} must be a {qualifier} finite number")


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
        _require_non_empty_text(self.stock_code, "stock_code")
        _require_date(self.trade_date, "trade_date")
        _require_bool(self.suspended, "suspended")
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
        if any(
            not isinstance(value, float) or not math.isfinite(value) or value <= 0
            for value in prices
        ):
            raise ValueError("prices must be positive finite numbers")
        _validate_finite_float(self.amount, "amount", allow_zero=True)
        _validate_finite_float(
            self.adjustment_ratio, "adjustment_ratio", allow_zero=False
        )


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
        _require_date(self.listing_date, "listing_date")
        _validate_optional_text(self.fund_type, "fund_type")
        _validate_optional_text(self.tracking_index_code, "tracking_index_code")
        _validate_optional_text(self.tracking_index_name, "tracking_index_name")
        _require_bool(self.is_cross_border, "is_cross_border")
        _require_bool(self.is_leveraged, "is_leveraged")


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
        _require_date(self.effective_date, "effective_date")
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
    classification_provenance: str = "metadata"

    def __post_init__(self) -> None:
        _require_bool(self.eligible, "eligible")
        if not isinstance(self.rejection_reasons, tuple):
            raise ValueError("rejection_reasons must be a tuple")
        for reason in self.rejection_reasons:
            _require_non_empty_text(reason, "rejection_reasons entries")
        if self.eligible and self.rejection_reasons:
            raise ValueError("eligible decisions cannot have rejection reasons")
        if not self.eligible and not self.rejection_reasons:
            raise ValueError("ineligible decisions must have rejection reasons")
        _validate_optional_text(self.exposure_group, "exposure_group")
        if self.eligible and self.exposure_group is None:
            raise ValueError("eligible decisions require an exposure_group")
        if not isinstance(self.classification_provenance, str) or (
            self.classification_provenance
            not in {"metadata", "name_fallback"}
        ):
            raise ValueError(
                "classification_provenance must be metadata or name_fallback"
            )
        if not isinstance(self.history_session_count, int) or isinstance(
            self.history_session_count, bool
        ) or self.history_session_count < 0:
            raise ValueError("history_session_count must be a non-negative integer")
        if self.average_amount_20d is not None:
            _validate_finite_float(
                self.average_amount_20d, "average_amount_20d", allow_zero=True
            )
        if self.eligible:
            if self.history_session_count < 252:
                raise ValueError("eligible decisions require at least 252 history sessions")
            if self.average_amount_20d is None or self.average_amount_20d < 10_000_000:
                raise ValueError(
                    "eligible decisions require a 20-session average amount of at least 10000000"
                )


@dataclass(frozen=True)
class DataQualityIssue:
    code: str | Enum
    stock_code: str
    trade_date: date | None
    message: str

    def __post_init__(self) -> None:
        if isinstance(self.code, Enum):
            code = self.code.value
            if not isinstance(code, str):
                raise ValueError("code enums must have string values")
        else:
            code = self.code
        _require_non_empty_text(code, "code")
        _require_non_empty_text(self.stock_code, "stock_code")
        if self.trade_date is not None:
            _require_date(self.trade_date, "trade_date")
        _require_non_empty_text(self.message, "message")


class DataQualityError(ValueError):
    """Raised when one or more data-quality issues prevent processing."""

    def __init__(self, message: str, issues: tuple[DataQualityIssue, ...] = ()) -> None:
        super().__init__(message)
        _require_non_empty_text(message, "message")
        if not isinstance(issues, tuple) or not all(
            isinstance(issue, DataQualityIssue) for issue in issues
        ):
            raise ValueError("issues must be a tuple of DataQualityIssue instances")
        self.issues = issues
