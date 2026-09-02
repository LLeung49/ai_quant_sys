"""Read-only, strictly aligned ETF market-data access."""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal, InvalidOperation
import math
from typing import Callable, Mapping, Sequence

from .contracts import (
    CorporateAction,
    CorporateActionType,
    DataQualityError,
    DataQualityIssue,
    DualPriceBar,
    ETFMetadata,
)


Query = Callable[[str, tuple[object, ...]], Sequence[Mapping[str, object]]]

RAW_BARS_SQL = """
SELECT stock_code, trade_date, open_price, high_price, low_price, close_price,
       amount, pre_close, suspend_flag
FROM trade_stock_daily_raw
WHERE stock_code = %s AND trade_date BETWEEN %s AND %s
ORDER BY trade_date
"""

QFQ_BARS_SQL = """
SELECT stock_code, trade_date, open_price, high_price, low_price, close_price,
       adjustment_asof
FROM trade_stock_daily_qfq
WHERE stock_code = %s AND trade_date BETWEEN %s AND %s
ORDER BY trade_date
"""

LATEST_ACTION_SQL = """
SELECT MAX(ex_date) AS latest_action_date
FROM trade_corporate_action
WHERE stock_code = %s AND event_status = 'effective' AND data_source = 'xtquant'
"""

METADATA_SQL = """
SELECT stock_code, stock_name AS fund_name, listing_date
FROM trade_stock_status
WHERE listing_date <= %s
ORDER BY stock_code
"""

ACTIONS_SQL = """
SELECT stock_code, ex_date, cash_dividend_per_share,
       stock_bonus_per_share, stock_gift_per_share,
       rights_issue_per_share, rights_issue_price
FROM trade_corporate_action
WHERE stock_code = %s AND ex_date BETWEEN %s AND %s
  AND event_status = 'effective' AND data_source = 'xtquant'
ORDER BY ex_date
"""


def _positive_finite(value: object, field_name: str) -> float:
    if isinstance(value, bool):
        raise ValueError(f"invalid {field_name}")
    try:
        result = float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"invalid {field_name}") from exc
    if not math.isfinite(result) or result <= 0:
        raise ValueError(f"invalid {field_name}")
    return result


def _non_negative_finite(value: object, field_name: str) -> float:
    if isinstance(value, bool):
        raise ValueError(f"invalid {field_name}")
    try:
        result = float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"invalid {field_name}") from exc
    if not math.isfinite(result) or result < 0:
        raise ValueError(f"invalid {field_name}")
    return result


def _as_date(value: object, field_name: str) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError as exc:
            raise ValueError(f"invalid {field_name}") from exc
    raise ValueError(f"invalid {field_name}")


def _as_bool(value: object, field_name: str) -> bool:
    if value is True or value == 1:
        return True
    if value is False or value == 0:
        return False
    raise ValueError(f"invalid {field_name}")


def _as_optional_text(value: object) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _as_non_negative_decimal(value: object, field_name: str) -> Decimal:
    if value is None:
        return Decimal(0)
    if isinstance(value, bool):
        raise ValueError(f"invalid {field_name}")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"invalid {field_name}") from exc
    if not result.is_finite() or result < 0:
        raise ValueError(f"invalid {field_name}")
    return result


def _validate_range(start_date: date, end_date: date) -> None:
    if not isinstance(start_date, date) or isinstance(start_date, datetime):
        raise ValueError("start_date must be a date")
    if not isinstance(end_date, date) or isinstance(end_date, datetime):
        raise ValueError("end_date must be a date")
    if start_date > end_date:
        raise ValueError("start_date must not be after end_date")


def _validate_code(stock_code: str) -> str:
    if not isinstance(stock_code, str) or not stock_code.strip():
        raise ValueError("stock_code must be a non-empty string")
    return stock_code.strip().upper()


def to_signal_price(raw_price: float, adjustment_ratio: float) -> float:
    """Convert an execution-coordinate price into the signal coordinate."""

    raw = _positive_finite(raw_price, "raw_price")
    ratio = _positive_finite(adjustment_ratio, "adjustment_ratio")
    return raw * ratio


def to_raw_distance(signal_distance: float, adjustment_ratio: float) -> float:
    """Convert a non-negative signal distance into the raw coordinate."""

    distance = _non_negative_finite(signal_distance, "signal_distance")
    ratio = _positive_finite(adjustment_ratio, "adjustment_ratio")
    return distance / ratio


class AdaptiveMarketDataProvider:
    """Load market facts without substituting dates or entities."""

    def __init__(self, query: Query, *, ratio_tolerance: float = 1e-6) -> None:
        if not callable(query):
            raise ValueError("query must be callable")
        if (
            isinstance(ratio_tolerance, bool)
            or not isinstance(ratio_tolerance, (int, float))
            or not math.isfinite(ratio_tolerance)
            or ratio_tolerance < 0
        ):
            raise ValueError("ratio_tolerance must be a non-negative finite number")
        self._query = query
        self._ratio_tolerance = float(ratio_tolerance)
        self.last_quality_issues: tuple[DataQualityIssue, ...] = ()

    def _fail(
        self,
        code: str,
        stock_code: str,
        message: str,
        trade_date: date | None = None,
    ) -> None:
        issue = DataQualityIssue(code, stock_code, trade_date, message)
        self.last_quality_issues = (issue,)
        raise DataQualityError(message, self.last_quality_issues)

    def _index_rows(
        self,
        rows: Sequence[Mapping[str, object]],
        *,
        coordinate: str,
        stock_code: str,
        start_date: date,
        end_date: date,
    ) -> dict[date, Mapping[str, object]]:
        indexed: dict[date, Mapping[str, object]] = {}
        for row in rows:
            try:
                row_code = _validate_code(row.get("stock_code"))  # type: ignore[arg-type]
            except ValueError:
                self._fail(
                    f"invalid_{coordinate}_stock_code",
                    stock_code,
                    f"invalid {coordinate} stock_code",
                )
            try:
                day = _as_date(row.get("trade_date"), "trade_date")
            except ValueError:
                self._fail(
                    f"invalid_{coordinate}_trade_date",
                    stock_code,
                    f"invalid {coordinate} trade_date",
                )
            if row_code != stock_code:
                self._fail(
                    f"{coordinate}_stock_code_mismatch",
                    stock_code,
                    f"{coordinate} stock_code mismatch",
                    day,
                )
            if day < start_date or day > end_date:
                self._fail(
                    f"{coordinate}_trade_date_outside_range",
                    stock_code,
                    f"{coordinate} trade_date outside requested range",
                    day,
                )
            if day in indexed:
                self._fail(
                    f"duplicate_{coordinate}_trade_date",
                    stock_code,
                    f"duplicate {coordinate} trade_date",
                    day,
                )
            indexed[day] = row
        return indexed

    def load_bars(
        self, stock_code: str, start_date: date, end_date: date
    ) -> tuple[DualPriceBar, ...]:
        """Return raw/qfq bars joined by the exact requested trade date."""

        code = _validate_code(stock_code)
        _validate_range(start_date, end_date)
        self.last_quality_issues = ()
        params = (code, start_date, end_date)
        raw_rows = self._query(RAW_BARS_SQL, params)
        qfq_rows = self._query(QFQ_BARS_SQL, params)
        latest_rows = self._query(LATEST_ACTION_SQL, (code,))
        raw = self._index_rows(
            raw_rows,
            coordinate="raw",
            stock_code=code,
            start_date=start_date,
            end_date=end_date,
        )
        qfq = self._index_rows(
            qfq_rows,
            coordinate="qfq",
            stock_code=code,
            start_date=start_date,
            end_date=end_date,
        )
        if raw.keys() != qfq.keys():
            self._fail(
                "raw_qfq_date_mismatch",
                code,
                "raw/qfq date mismatch",
            )

        latest_action_date: date | None = None
        if latest_rows:
            latest_value = latest_rows[0].get("latest_action_date")
            if latest_value is not None:
                try:
                    latest_action_date = _as_date(
                        latest_value, "latest_action_date"
                    )
                except ValueError:
                    self._fail(
                        "invalid_latest_action_date",
                        code,
                        "invalid latest corporate-action date",
                    )

        bars: list[DualPriceBar] = []
        issues: list[DataQualityIssue] = []
        prior_raw_close: float | None = None
        adjustment_versions: set[date | None] = set()
        for day in sorted(raw):
            raw_row = raw[day]
            qfq_row = qfq[day]
            try:
                raw_prices = {
                    name: _positive_finite(raw_row.get(f"{name}_price"), f"raw {name}_price")
                    for name in ("open", "high", "low", "close")
                }
                signal_prices = {
                    name: _positive_finite(qfq_row.get(f"{name}_price"), f"qfq {name}_price")
                    for name in ("open", "high", "low", "close")
                }
                amount = _non_negative_finite(raw_row.get("amount"), "raw amount")
                suspended = _as_bool(raw_row.get("suspend_flag"), "suspend_flag")
            except ValueError as exc:
                self._fail("invalid_bar_value", code, str(exc), day)

            for label, prices in (("raw", raw_prices), ("qfq", signal_prices)):
                if (
                    prices["high"] < max(prices["open"], prices["close"])
                    or prices["low"] > min(prices["open"], prices["close"])
                    or prices["low"] > prices["high"]
                ):
                    self._fail(
                        f"invalid_{label}_ohlc",
                        code,
                        f"invalid {label} OHLC",
                        day,
                    )

            ratio = signal_prices["close"] / raw_prices["close"]
            if not math.isfinite(ratio) or ratio <= 0:
                self._fail("invalid_adjustment_ratio", code, "invalid adjustment ratio", day)
            for name in ("open", "high", "low"):
                candidate = signal_prices[name] / raw_prices[name]
                if not math.isclose(
                    candidate,
                    ratio,
                    rel_tol=self._ratio_tolerance,
                    abs_tol=0.0,
                ):
                    self._fail(
                        "inconsistent_raw_qfq_ohlc_ratio",
                        code,
                        "inconsistent raw/qfq OHLC ratio",
                        day,
                    )

            pre_close_value = raw_row.get("pre_close")
            if pre_close_value is None:
                issues.append(
                    DataQualityIssue(
                        "missing_pre_close", code, day, "raw pre_close is missing"
                    )
                )
            else:
                try:
                    pre_close = _positive_finite(pre_close_value, "pre_close")
                except ValueError:
                    issues.append(
                        DataQualityIssue(
                            "invalid_pre_close", code, day, "raw pre_close is invalid"
                        )
                    )
                else:
                    if prior_raw_close is not None and not math.isclose(
                        pre_close,
                        prior_raw_close,
                        rel_tol=self._ratio_tolerance,
                        abs_tol=self._ratio_tolerance,
                    ):
                        issues.append(
                            DataQualityIssue(
                                "inconsistent_pre_close",
                                code,
                                day,
                                "raw pre_close does not match the prior loaded close",
                            )
                        )

            adjustment_value = qfq_row.get("adjustment_asof")
            if adjustment_value is None:
                adjustment_asof = None
                issues.append(
                    DataQualityIssue(
                        "missing_adjustment_asof",
                        code,
                        day,
                        "qfq adjustment_asof is missing",
                    )
                )
            else:
                try:
                    adjustment_asof = _as_date(
                        adjustment_value, "adjustment_asof"
                    )
                except ValueError:
                    adjustment_asof = None
                    issues.append(
                        DataQualityIssue(
                            "invalid_adjustment_asof",
                            code,
                            day,
                            "qfq adjustment_asof is invalid",
                        )
                    )
                else:
                    if (
                        latest_action_date is not None
                        and adjustment_asof < latest_action_date
                    ):
                        issues.append(
                            DataQualityIssue(
                                "stale_adjustment_asof",
                                code,
                                day,
                                "qfq adjustment_asof predates the latest effective corporate action",
                            )
                        )
            adjustment_versions.add(adjustment_asof)
            prior_raw_close = raw_prices["close"]
            bars.append(
                DualPriceBar(
                    stock_code=code,
                    trade_date=day,
                    signal_open=signal_prices["open"],
                    signal_high=signal_prices["high"],
                    signal_low=signal_prices["low"],
                    signal_close=signal_prices["close"],
                    raw_open=raw_prices["open"],
                    raw_high=raw_prices["high"],
                    raw_low=raw_prices["low"],
                    raw_close=raw_prices["close"],
                    amount=amount,
                    suspended=suspended,
                    adjustment_ratio=ratio,
                )
            )

        if len(adjustment_versions) > 1:
            issues.append(
                DataQualityIssue(
                    "inconsistent_adjustment_asof",
                    code,
                    None,
                    "qfq rows contain inconsistent adjustment_asof versions",
                )
            )
        self.last_quality_issues = tuple(issues)
        return tuple(bars)

    def load_metadata(self, as_of_date: date) -> tuple[ETFMetadata, ...]:
        """Load current ETF metadata limited by listing date."""

        _validate_range(as_of_date, as_of_date)
        self.last_quality_issues = ()
        rows = self._query(METADATA_SQL, (as_of_date,))
        metadata: list[ETFMetadata] = []
        observed_codes: set[str] = set()
        for row in rows:
            try:
                code = _validate_code(row.get("stock_code"))  # type: ignore[arg-type]
            except ValueError:
                self._fail(
                    "invalid_metadata_stock_code",
                    "<unknown>",
                    "invalid metadata stock_code",
                )
            if code in observed_codes:
                self._fail(
                    "duplicate_metadata_stock_code",
                    code,
                    "duplicate metadata stock_code",
                )
            observed_codes.add(code)
            try:
                listing_date = _as_date(row.get("listing_date"), "listing_date")
            except ValueError:
                self._fail("invalid_listing_date", code, "invalid metadata listing_date")
            if listing_date > as_of_date:
                self._fail(
                    "metadata_listing_date_after_as_of_date",
                    code,
                    "metadata listing_date after as_of_date",
                    listing_date,
                )
            fund_name = _as_optional_text(row.get("fund_name"))
            if fund_name is None:
                self._fail("missing_fund_name", code, "metadata fund_name is missing")
            try:
                is_cross_border = _as_bool(
                    row.get("is_cross_border", False), "is_cross_border"
                )
                is_leveraged = _as_bool(
                    row.get("is_leveraged", False), "is_leveraged"
                )
            except ValueError as exc:
                self._fail("invalid_metadata_flag", code, str(exc))
            metadata.append(
                ETFMetadata(
                    stock_code=code,
                    fund_name=fund_name,
                    listing_date=listing_date,
                    fund_type=_as_optional_text(row.get("fund_type")),
                    tracking_index_code=_as_optional_text(
                        row.get("tracking_index_code")
                    ),
                    tracking_index_name=_as_optional_text(
                        row.get("tracking_index_name")
                    ),
                    is_cross_border=is_cross_border,
                    is_leveraged=is_leveraged,
                )
            )
        return tuple(metadata)

    def load_actions(
        self, stock_code: str, start_date: date, end_date: date
    ) -> tuple[CorporateAction, ...]:
        """Convert effective source events into executable action contracts."""

        code = _validate_code(stock_code)
        _validate_range(start_date, end_date)
        self.last_quality_issues = ()
        rows = self._query(ACTIONS_SQL, (code, start_date, end_date))
        actions: list[CorporateAction] = []
        observed_dates: set[date] = set()
        for row in rows:
            try:
                row_code = _validate_code(row.get("stock_code"))  # type: ignore[arg-type]
            except ValueError:
                self._fail(
                    "invalid_corporate_action_stock_code",
                    code,
                    "invalid corporate action stock_code",
                )
            try:
                effective_date = _as_date(row.get("ex_date"), "ex_date")
            except ValueError:
                self._fail("invalid_corporate_action_date", code, "invalid corporate action date")
            if row_code != code:
                self._fail(
                    "corporate_action_stock_code_mismatch",
                    code,
                    "corporate action stock_code mismatch",
                    effective_date,
                )
            if effective_date < start_date or effective_date > end_date:
                self._fail(
                    "corporate_action_date_outside_range",
                    code,
                    "corporate action date outside requested range",
                    effective_date,
                )
            if effective_date in observed_dates:
                self._fail(
                    "duplicate_corporate_action_date",
                    code,
                    "duplicate corporate action date",
                    effective_date,
                )
            observed_dates.add(effective_date)
            try:
                cash = _as_non_negative_decimal(
                    row.get("cash_dividend_per_share"),
                    "cash_dividend_per_share",
                )
                bonus = _as_non_negative_decimal(
                    row.get("stock_bonus_per_share"),
                    "stock_bonus_per_share",
                )
                gift = _as_non_negative_decimal(
                    row.get("stock_gift_per_share"),
                    "stock_gift_per_share",
                )
                rights = _as_non_negative_decimal(
                    row.get("rights_issue_per_share"),
                    "rights_issue_per_share",
                )
            except ValueError as exc:
                self._fail("invalid_corporate_action_value", code, str(exc), effective_date)
            if rights > 0:
                self._fail(
                    "unsupported_rights_issue",
                    code,
                    "unsupported rights issue",
                    effective_date,
                )
            if cash > 0:
                actions.append(
                    CorporateAction(
                        code,
                        effective_date,
                        CorporateActionType.CASH_DIVIDEND,
                        cash,
                        Decimal(1),
                    )
                )
            share_multiplier = Decimal(1) + bonus + gift
            if share_multiplier > 1:
                actions.append(
                    CorporateAction(
                        code,
                        effective_date,
                        CorporateActionType.SHARE_SPLIT,
                        None,
                        share_multiplier,
                    )
                )
        return tuple(actions)
