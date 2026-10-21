"""Provider-independent validation for daily market rows.

The functions in this module form the last boundary before persistence.  A
provider may omit a row, but it may never represent a missing or suspended row
by writing zero prices.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
import math
from typing import Mapping, Sequence


PRICE_FIELDS = ("open_price", "high_price", "low_price", "close_price")
REQUIRED_MODES = ("none", "front", "back")
STORAGE_PRICE_QUANTUM = Decimal("0.000001")


@dataclass(frozen=True)
class ValidationIssue:
    code: str
    message: str
    stock_code: str = ""
    trade_date: str = ""
    field: str | None = None
    mode: str | None = None
    severity: str = "error"


@dataclass(frozen=True)
class ValidationResult:
    is_valid: bool
    issues: tuple[ValidationIssue, ...] = ()
    quarantined: bool = False


@dataclass(frozen=True)
class BatchValidationResult:
    is_valid: bool
    issues: tuple[ValidationIssue, ...] = ()


def _identity(row: Mapping[str, object]) -> tuple[str, str]:
    return str(row.get("stock_code", "")), str(row.get("trade_date", ""))[:10]


def _number(value: object) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError):
        return None
    return number if math.isfinite(number) else None


def validate_market_row(
    row: Mapping[str, object], *, allow_negative_price: bool = False
) -> ValidationResult:
    """Validate one normalized row without changing or repairing its values."""
    stock_code, trade_date = _identity(row)
    issues: list[ValidationIssue] = []
    prices: dict[str, float] = {}
    negative_fields: list[str] = []

    for field in PRICE_FIELDS:
        number = _number(row.get(field))
        if number is None:
            issues.append(ValidationIssue(
                "non_finite_price", f"{field} must be finite", stock_code,
                trade_date, field,
            ))
            continue
        prices[field] = number
        if number == 0:
            issues.append(ValidationIssue(
                "zero_price", f"{field} must not be zero", stock_code,
                trade_date, field,
            ))
        elif Decimal(str(number)).quantize(
            STORAGE_PRICE_QUANTUM, rounding=ROUND_HALF_UP
        ) == 0:
            issues.append(ValidationIssue(
                "zero_price_after_storage_rounding",
                f"{field} would be stored as zero",
                stock_code,
                trade_date,
                field,
            ))
        elif number < 0:
            if allow_negative_price:
                negative_fields.append(field)
            else:
                issues.append(ValidationIssue(
                    "negative_price", f"{field} must be positive", stock_code,
                    trade_date, field,
                ))

    for field in ("volume", "amount"):
        number = _number(row.get(field))
        if number is None:
            issues.append(ValidationIssue(
                "non_finite_trading_value", f"{field} must be finite",
                stock_code, trade_date, field,
            ))
        elif number < 0:
            issues.append(ValidationIssue(
                "negative_trading_value", f"{field} must be non-negative",
                stock_code, trade_date, field,
            ))

    if len(prices) == len(PRICE_FIELDS) and not any(
        issue.code in {"zero_price", "negative_price"} for issue in issues
    ):
        low = prices["low_price"]
        high = prices["high_price"]
        if low > high or low > min(prices["open_price"], prices["close_price"]):
            issues.append(ValidationIssue(
                "invalid_ohlc", "low_price exceeds another OHLC value",
                stock_code, trade_date, "low_price",
            ))
        if high < max(prices["open_price"], prices["close_price"]):
            issues.append(ValidationIssue(
                "invalid_ohlc", "high_price is below another OHLC value",
                stock_code, trade_date, "high_price",
            ))

    quarantined = bool(negative_fields)
    if quarantined:
        issues.append(ValidationIssue(
            "negative_adjusted_price",
            "adjusted prices cross or remain below zero; preserve with research quarantine",
            stock_code,
            trade_date,
            ",".join(negative_fields),
            severity="warning",
        ))
    is_valid = not any(issue.severity == "error" for issue in issues)
    return ValidationResult(is_valid, tuple(issues), quarantined)


def validate_projection_batch(
    rows_by_mode: Mapping[str, Sequence[Mapping[str, object]]],
) -> BatchValidationResult:
    """Validate all modes and their shared dates, volumes, and amounts."""
    issues: list[ValidationIssue] = []
    indexed: dict[str, dict[tuple[str, str], Mapping[str, object]]] = {}

    for mode in REQUIRED_MODES:
        rows = rows_by_mode.get(mode)
        if rows is None:
            issues.append(ValidationIssue(
                "missing_projection_mode", f"missing projection mode: {mode}", mode=mode
            ))
            continue
        mode_rows: dict[tuple[str, str], Mapping[str, object]] = {}
        for row in rows:
            result = validate_market_row(row, allow_negative_price=(mode == "front"))
            issues.extend(
                ValidationIssue(
                    issue.code, issue.message, issue.stock_code, issue.trade_date,
                    issue.field, mode, issue.severity,
                )
                for issue in result.issues
            )
            key = _identity(row)
            if key in mode_rows:
                issues.append(ValidationIssue(
                    "duplicate_projection_row", "duplicate stock/date in projection",
                    key[0], key[1], mode=mode,
                ))
            mode_rows[key] = row
        indexed[mode] = mode_rows

    if len(indexed) == len(REQUIRED_MODES):
        reference_keys = set(indexed["none"])
        for mode in ("front", "back"):
            if set(indexed[mode]) != reference_keys:
                issues.append(ValidationIssue(
                    "projection_date_mismatch",
                    f"{mode} stock/date coverage differs from raw",
                    mode=mode,
                ))
        for key in reference_keys.intersection(*(set(indexed[m]) for m in ("front", "back"))):
            raw = indexed["none"][key]
            for mode in ("front", "back"):
                projected = indexed[mode][key]
                if any(
                    _number(raw.get(field)) != _number(projected.get(field))
                    for field in ("volume", "amount")
                ):
                    issues.append(ValidationIssue(
                        "projection_volume_amount_mismatch",
                        f"{mode} volume/amount differs from raw",
                        key[0], key[1], mode=mode,
                    ))

    return BatchValidationResult(
        not any(issue.severity == "error" for issue in issues), tuple(issues)
    )
