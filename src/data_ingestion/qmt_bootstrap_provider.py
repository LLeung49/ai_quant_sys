"""Temporary QMT Bridge reader for the staging-only market rebuild."""

from __future__ import annotations

from collections import Counter
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal, ROUND_HALF_UP
import hashlib
import json
from typing import Sequence

from data_ingestion_qmt.qmt_data_gateway import QMTDataGateway

from .market_provider import MarketBatch
from .market_row_validation import validate_market_row, validate_projection_batch
from .market_volume_contract import assess_volume


MODES = ("none", "front", "back")
FIELDS = ("open", "high", "low", "close", "volume", "amount", "preClose", "suspendFlag")
MIN_DOMINANT_VOLUME_UNIT_RATIO = 0.97


def _trade_date(value: object) -> str:
    text = str(value)
    if len(text) < 8:
        raise ValueError(f"invalid QMT trade date: {value!r}")
    return f"{text[:4]}-{text[4:6]}-{text[6:8]}"


def _optional_float(value: object) -> float | None:
    if value is None or value != value:
        return None
    return float(value)


class QMTBootstrapProvider:
    """Read bridge data, discard fill rows, and return complete market batches."""

    def __init__(self, *, gateway: QMTDataGateway | None = None) -> None:
        self.gateway = gateway or QMTDataGateway.from_env()

    def _normalize_frame(self, stock_code: str, mode: str, frame):
        rows: list[dict] = []
        gaps: list[dict] = []
        quarantines: list[dict] = []
        column_offset = {name: index + 1 for index, name in enumerate(frame.columns)}
        for source in frame.itertuples(index=True, name=None):
            index_value = source[0]
            value = lambda field: source[column_offset[field]]
            trade_date = _trade_date(index_value)
            prices = [float(value(field)) for field in ("open", "high", "low", "close")]
            if all(price == 0 for price in prices):
                gaps.append({
                    "stock_code": stock_code,
                    "trade_date": trade_date,
                    "mode": mode,
                    "reason": "zero_price_fill",
                    "suspend_flag": _optional_float(value("suspendFlag")),
                })
                continue
            raw_volume = float(value("volume"))
            amount = float(value("amount"))
            row = {
                "stock_code": stock_code,
                "trade_date": trade_date,
                "open_price": prices[0],
                "high_price": prices[1],
                "low_price": prices[2],
                "close_price": prices[3],
                # Normalize after all three modes arrive.  Adjusted prices
                # cannot classify a shares-vs-lots source volume reliably.
                "volume": int(raw_volume),
                "amount": amount,
                "turnover_rate": None,
            }
            if mode == "none":
                row.update({
                    "pre_close": _optional_float(value("preClose")),
                    "suspend_flag": (
                        int(flag) if (flag := _optional_float(value("suspendFlag"))) is not None
                        else None
                    ),
                    "data_source": "qmt_bridge_rebuild",
                })
            validation = validate_market_row(row, allow_negative_price=(mode == "front"))
            if not validation.is_valid:
                codes = sorted({issue.code for issue in validation.issues if issue.severity == "error"})
                raise ValueError(f"invalid_market_row {stock_code}/{trade_date}/{mode}: {codes}")
            if validation.quarantined:
                quarantines.append({
                    "stock_code": stock_code,
                    "trade_date": trade_date,
                    "mode": mode,
                    "issues": [issue.code for issue in validation.issues],
                })
            rows.append(row)
        return rows, gaps, quarantines

    @staticmethod
    def _normalize_batch_volumes(rows_by_mode: dict[str, list[dict]]) -> None:
        indexed = {
            mode: {row["trade_date"]: row for row in rows_by_mode[mode]}
            for mode in MODES
        }
        raw_by_date = indexed["none"]
        eligible = []
        units = []
        for raw in raw_by_date.values():
            source_volume = raw["volume"]
            if source_volume == 0 and raw["amount"] == 0:
                continue
            eligible.append(raw)
            assessment = assess_volume(
                raw["amount"], raw["close_price"], source_volume
            )
            if assessment.unit != "unknown":
                units.append(assessment.unit)
        unit_counts = Counter(units)
        dominant_unit = unit_counts.most_common(1)[0] if unit_counts else ("lot", 0)
        if units and dominant_unit[1] / len(units) < MIN_DOMINANT_VOLUME_UNIT_RATIO:
            raise ValueError(f"inconsistent volume unit: {dict(unit_counts)}")
        if eligible and (not units or len(units) / len(eligible) < 0.80):
            raise ValueError(
                "cannot classify volume unit from batch consensus: "
                f"classified={len(units)} eligible={len(eligible)}"
            )
        inferred_unit = dominant_unit[0]

        for trade_date, raw in raw_by_date.items():
            source_volume = raw["volume"]
            if source_volume == 0 and raw["amount"] == 0:
                normalized = 0
            elif inferred_unit == "lot":
                normalized = int(source_volume)
            else:
                normalized = int(
                    (Decimal(str(source_volume)) / Decimal("100")).quantize(
                        Decimal("1"), rounding=ROUND_HALF_UP
                    )
                )
            for mode in MODES:
                projected = indexed[mode].get(trade_date)
                if projected is None:
                    raise ValueError(
                        f"projection date missing: {trade_date}/{mode}"
                    )
                if projected["volume"] != source_volume:
                    raise ValueError(
                        f"source volume differs across projections: {trade_date}/{mode}"
                    )
                projected["volume"] = normalized

    def fetch_batches(
        self, stock_codes: Sequence[str], start_date: date, end_date: date
    ) -> dict[str, MarketBatch]:
        codes = list(dict.fromkeys(stock_codes))
        if not codes:
            return {}
        if start_date > end_date:
            raise ValueError("start_date must not exceed end_date")
        expected_ranges = {code: (start_date, end_date) for code in codes}
        try:
            details = self.gateway.get_instrument_detail(codes, iscomplete=True)
        except Exception:
            details = {}
        for code in codes:
            detail = details.get(code) or {}
            try:
                open_text = str(int(detail.get("OpenDate") or 0))[:8]
                open_date = datetime.strptime(open_text, "%Y%m%d").date()
            except (TypeError, ValueError):
                open_date = start_date
            try:
                expire_text = str(int(detail.get("ExpireDate") or 0))[:8]
                expire_date = datetime.strptime(expire_text, "%Y%m%d").date()
            except (TypeError, ValueError):
                expire_date = end_date
            expected_ranges[code] = (
                max(start_date, open_date), min(end_date, expire_date)
            )
        rows_by_code = {code: {} for code in codes}
        failures_by_code = {code: {} for code in codes}
        gaps_by_code = {code: [] for code in codes}
        quarantines_by_code = {code: [] for code in codes}
        for mode in MODES:
            try:
                frames = self.gateway.get_market_data_ex(
                    field_list=list(FIELDS),
                    stock_list=codes,
                    period="1d",
                    start_time=start_date.strftime("%Y%m%d"),
                    end_time=end_date.strftime("%Y%m%d"),
                    dividend_type=mode,
                    fill_data=False,
                )
            except Exception as exc:
                for code in codes:
                    failures_by_code[code][mode] = f"{type(exc).__name__}: {exc}"
                continue
            for code in codes:
                frame = frames.get(code) if frames else None
                if frame is None or len(frame) == 0:
                    failures_by_code[code][mode] = "empty_response"
                    continue
                try:
                    rows, gaps, quarantines = self._normalize_frame(code, mode, frame)
                except Exception as exc:
                    failures_by_code[code][mode] = f"{type(exc).__name__}: {exc}"
                    continue
                gaps_by_code[code].extend(gaps)
                quarantines_by_code[code].extend(quarantines)
                if not rows:
                    failures_by_code[code][mode] = "no_valid_rows_after_zero_fill_filter"
                    continue
                rows_by_code[code][mode] = rows

        fetched_at = datetime.now(timezone.utc).isoformat()
        result: dict[str, MarketBatch] = {}
        for code in codes:
            modes = rows_by_code[code]
            failures = failures_by_code[code]
            if len(modes) == len(MODES):
                try:
                    self._normalize_batch_volumes(modes)
                    validation = validate_projection_batch(modes)
                    if not validation.is_valid:
                        failures["batch"] = "; ".join(
                            issue.code for issue in validation.issues if issue.severity == "error"
                        )
                except Exception as exc:
                    failures["batch"] = f"{type(exc).__name__}: {exc}"
                expected_start, expected_end = expected_ranges[code]
                raw_dates = sorted(
                    date.fromisoformat(str(row["trade_date"])[:10])
                    for row in modes["none"]
                )
                if raw_dates and (
                    raw_dates[0] > expected_start + timedelta(days=31)
                    or raw_dates[-1] < expected_end - timedelta(days=31)
                ):
                    failures["coverage"] = (
                        f"expected_start={expected_start.isoformat()} "
                        f"expected_end={expected_end.isoformat()} "
                        f"actual_start={raw_dates[0].isoformat()} "
                        f"actual_end={raw_dates[-1].isoformat()}"
                    )
                elif any(
                    later - earlier > timedelta(days=180)
                    for earlier, later in zip(raw_dates, raw_dates[1:])
                ):
                    failures["coverage"] = "internal_history_gap_over_180_days"
            fingerprint = hashlib.sha256(
                json.dumps(modes, sort_keys=True, ensure_ascii=False, default=str).encode("utf-8")
            ).hexdigest()
            result[code] = MarketBatch(
                code,
                expected_ranges[code][0],
                expected_ranges[code][1],
                rows_by_mode=modes,
                provenance={
                    "provider": "qmt_bridge",
                    "interface": "ContextInfo.get_market_data_ex",
                    "fetched_at": fetched_at,
                    "fingerprint": fingerprint,
                    "volume_unit": "lot",
                    "amount_unit": "yuan",
                },
                failures=failures,
                quarantines=tuple(quarantines_by_code[code]),
                gaps=tuple(gaps_by_code[code]),
            )
        return result

    def fetch_batch(
        self, stock_code: str, start_date: date, end_date: date
    ) -> MarketBatch:
        return self.fetch_batches([stock_code], start_date, end_date)[stock_code]
