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
class ExecutionAvailability:
    buy_locked: bool
    sell_locked: bool
    provenance: str

    def __post_init__(self) -> None:
        _require_bool(self.buy_locked, "buy_locked")
        _require_bool(self.sell_locked, "sell_locked")
        _require_non_empty_text(self.provenance, "provenance")


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
    raw_pre_close: float = 1.0
    execution_availability: ExecutionAvailability = ExecutionAvailability(
        True, True, "unavailable"
    )
    adjustment_offset: float = 0.0

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
        _validate_finite_float(
            self.raw_pre_close, "raw_pre_close", allow_zero=False
        )
        _validate_finite_float(self.amount, "amount", allow_zero=True)
        _validate_finite_float(
            self.adjustment_ratio, "adjustment_ratio", allow_zero=False
        )
        if not isinstance(self.adjustment_offset, float) or not math.isfinite(
            self.adjustment_offset
        ):
            raise ValueError("adjustment_offset must be a finite float")
        if not isinstance(self.execution_availability, ExecutionAvailability):
            raise ValueError("execution_availability must be an ExecutionAvailability")


@dataclass(frozen=True)
class ETFMetadata:
    stock_code: str
    fund_name: str
    listing_date: date
    fund_type: str | None = None
    tracking_index_code: str | None = None
    tracking_index_name: str | None = None
    is_domestic_equity: bool | None = None
    is_cross_border: bool = False
    is_leveraged: bool = False

    def __post_init__(self) -> None:
        _require_non_empty_text(self.stock_code, "stock_code")
        _require_non_empty_text(self.fund_name, "fund_name")
        _require_date(self.listing_date, "listing_date")
        _validate_optional_text(self.fund_type, "fund_type")
        _validate_optional_text(self.tracking_index_code, "tracking_index_code")
        _validate_optional_text(self.tracking_index_name, "tracking_index_name")
        if self.is_domestic_equity is not None:
            _require_bool(self.is_domestic_equity, "is_domestic_equity")
        _require_bool(self.is_cross_border, "is_cross_border")
        _require_bool(self.is_leveraged, "is_leveraged")


class InstrumentType(str, Enum):
    """Tradable identity types supported by the layered universe."""

    ETF = "etf"
    STOCK = "stock"


class AssetLayer(str, Enum):
    """Top-level sleeves whose budgets remain account-allocation inputs."""

    DEFENSIVE = "defensive"
    BROAD_BETA = "broad_beta"


class SubLayer(str, Enum):
    """The complete approved adaptive-equity sub-layer allowlist."""

    DEFENSIVE_DIVIDEND_ETF = "defensive_dividend_etf"
    DEFENSIVE_BLUE_CHIP = "defensive_blue_chip"
    DOMESTIC_CORE = "broad_domestic_core"
    DOMESTIC_GROWTH = "broad_domestic_growth"
    OVERSEAS_MATURE = "broad_overseas_mature"
    HONG_KONG_OFFSHORE = "broad_hk_offshore"


_SUB_LAYER_ASSET_LAYERS = {
    SubLayer.DEFENSIVE_DIVIDEND_ETF: AssetLayer.DEFENSIVE,
    SubLayer.DEFENSIVE_BLUE_CHIP: AssetLayer.DEFENSIVE,
    SubLayer.DOMESTIC_CORE: AssetLayer.BROAD_BETA,
    SubLayer.DOMESTIC_GROWTH: AssetLayer.BROAD_BETA,
    SubLayer.OVERSEAS_MATURE: AssetLayer.BROAD_BETA,
    SubLayer.HONG_KONG_OFFSHORE: AssetLayer.BROAD_BETA,
}


def asset_layer_for(sub_layer: SubLayer) -> AssetLayer:
    """Return the immutable parent layer for an approved sub-layer."""

    if not isinstance(sub_layer, SubLayer):
        raise ValueError("sub_layer must be a SubLayer")
    return _SUB_LAYER_ASSET_LAYERS[sub_layer]


@dataclass(frozen=True)
class LayeredInstrument:
    """A point-in-time candidate awaiting fail-closed sub-layer assignment."""

    stock_code: str
    as_of_date: date
    instrument_type: InstrumentType
    style: str | None
    exposure: str | None
    is_qdii: bool
    is_official_dividend_low_vol_constituent: bool = False

    def __post_init__(self) -> None:
        _require_non_empty_text(self.stock_code, "stock_code")
        _require_date(self.as_of_date, "as_of_date")
        if not isinstance(self.instrument_type, InstrumentType):
            raise ValueError("instrument_type must be an InstrumentType")
        _validate_optional_text(self.style, "style")
        _validate_optional_text(self.exposure, "exposure")
        _require_bool(self.is_qdii, "is_qdii")
        _require_bool(
            self.is_official_dividend_low_vol_constituent,
            "is_official_dividend_low_vol_constituent",
        )

    @property
    def asset_layer(self) -> AssetLayer:
        """Resolve the parent layer only after approved assignment."""

        from .layers import assign_sub_layer

        return asset_layer_for(assign_sub_layer(self))


@dataclass(frozen=True)
class SubLayerBudget:
    """An existing account budget delegated to one approved sub-layer."""

    sub_layer: SubLayer
    budget: Decimal

    def __post_init__(self) -> None:
        if not isinstance(self.sub_layer, SubLayer):
            raise ValueError("sub_layer must be a SubLayer")
        _validate_positive_decimal(self.budget, "budget")

    @property
    def asset_layer(self) -> AssetLayer:
        return asset_layer_for(self.sub_layer)


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

    @property
    def event_id(self) -> str:
        return f"{self.stock_code}:{self.effective_date.isoformat()}:{self.action_type.value}"

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
