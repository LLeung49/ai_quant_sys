"""Provider-independent ETF constituent normalization and aggregation."""

from __future__ import annotations

import math
import re
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from typing import Literal


_CODE_PATTERN = re.compile(
    r"^(?:(?:SH|SZ|BJ)\.?)?(\d{6})(?:\.(?:SH|SZ|BJ))?$",
    re.IGNORECASE,
)
_WEIGHT_TOLERANCE = 1e-9


@dataclass(frozen=True)
class ExposureResult:
    """Quality-passing ETF exposure to one SW2 membership universe."""

    etf_code: str
    exposure_weight: float
    coverage_ratio: float


@dataclass(frozen=True)
class RejectedExposure:
    """An assessed ETF that was excluded from the eligible candidate maps."""

    etf_code: str
    exposure_weight: float
    coverage_ratio: float
    failure_reason: str


@dataclass(frozen=True)
class ExposureAssessment:
    """Complete constituent assessment, retaining both eligible and rejected ETFs."""

    eligible: list[ExposureResult]
    rejected: list[RejectedExposure]


def normalize_stock_code(code: str) -> str:
    """Return a six-digit, market-neutral stock code.

    Provider feeds commonly use ``600000``, ``600000.SH``, ``SH600000`` or
    ``sz.000001``.  The market is deliberately discarded because SW2
    membership and ETF baskets are joined on the security code only.
    """

    if code is None:
        raise ValueError("stock code is required")
    raw = str(code).strip().upper().replace(" ", "")
    # Prefix feeds may contain a dot (e.g. ``SZ.000001``), while suffix feeds
    # use the conventional ``000001.SZ`` form.  The regex keeps both forms
    # strict so malformed identifiers cannot silently enter exposure sums.
    match = _CODE_PATTERN.fullmatch(raw)
    if not match:
        raise ValueError(f"invalid stock code: {code!r}")
    return match.group(1)


def aggregate_constituents(rows: Iterable[Mapping[str, object]]) -> dict[str, float]:
    """Normalize constituent rows and sum duplicate security weights.

    Both ``stock_code`` and the shorter ``code`` provider field are accepted;
    ``stock_code`` takes precedence when present.  Weights are returned as
    floats and must be finite and non-negative.
    """

    aggregated: dict[str, float] = {}
    for row in rows:
        if not isinstance(row, Mapping):
            raise ValueError("constituent row must be a mapping")
        code = row.get("stock_code")
        if code is None or str(code).strip() == "":
            code = row.get("code")
        if code is None or str(code).strip() == "":
            raise ValueError("stock code is required")
        if "weight" not in row or row.get("weight") is None:
            raise ValueError("weight is required")
        try:
            weight = float(row["weight"])
        except (TypeError, ValueError) as exc:
            raise ValueError(f"invalid weight: {row['weight']!r}") from exc
        if not math.isfinite(weight) or weight < 0:
            raise ValueError(f"invalid weight: {row['weight']!r}")
        normalized = normalize_stock_code(code)
        aggregated[normalized] = aggregated.get(normalized, 0.0) + weight
    return aggregated


def rank_sector_etfs(
    sw2_codes: Iterable[str],
    baskets: Mapping[str, Iterable[Mapping[str, object]] | Mapping[str, object]],
    min_coverage: float,
    *,
    weight_unit: Literal["decimal", "percent"],
) -> list[ExposureResult]:
    """Return the quality-passing Top3 ETFs ranked by actual SW2 exposure."""

    return assess_sector_etfs(
        sw2_codes, baskets, min_coverage, weight_unit=weight_unit,
    ).eligible


def assess_sector_etfs(
    sw2_codes: Iterable[str],
    baskets: Mapping[str, Iterable[Mapping[str, object]] | Mapping[str, object]],
    min_coverage: float,
    *,
    weight_unit: Literal["decimal", "percent"],
) -> ExposureAssessment:
    """Assess all ETF baskets so rejected coverage remains auditable downstream."""

    if not 0 <= min_coverage <= 1:
        raise ValueError("min_coverage must be between zero and one")
    if weight_unit not in {"decimal", "percent"}:
        raise ValueError(f"invalid weight unit: {weight_unit!r}")

    normalized_sw2_codes = {normalize_stock_code(code) for code in sw2_codes}
    if not normalized_sw2_codes or not baskets:
        return ExposureAssessment(eligible=[], rejected=[])

    ranked: list[ExposureResult] = []
    rejected: list[RejectedExposure] = []
    for etf_code, basket in baskets.items():
        if not basket:
            continue
        aggregated = _aggregate_basket(basket)
        if not aggregated:
            continue

        normalized_weights = _normalize_weights(aggregated, weight_unit)
        coverage_ratio = sum(normalized_weights.values())
        exposure_weight = sum(
            weight for stock_code, weight in normalized_weights.items()
            if stock_code in normalized_sw2_codes
        )
        if coverage_ratio < min_coverage:
            rejected.append(RejectedExposure(
                str(etf_code), exposure_weight, coverage_ratio, "coverage_below_minimum",
            ))
            continue
        if exposure_weight <= 0:
            rejected.append(RejectedExposure(
                str(etf_code), exposure_weight, coverage_ratio, "no_sector_exposure",
            ))
            continue

        ranked.append(
            ExposureResult(
                etf_code=str(etf_code),
                exposure_weight=exposure_weight,
                coverage_ratio=coverage_ratio,
            )
        )

    return ExposureAssessment(
        eligible=sorted(
            ranked, key=lambda item: (-item.exposure_weight, -item.coverage_ratio, item.etf_code),
        )[:3],
        rejected=sorted(
            rejected, key=lambda item: (-item.exposure_weight, -item.coverage_ratio, item.etf_code),
        ),
    )


def _aggregate_basket(
    basket: Iterable[Mapping[str, object]] | Mapping[str, object],
) -> dict[str, float]:
    if isinstance(basket, Mapping):
        return aggregate_constituents(
            {"stock_code": code, "weight": weight}
            for code, weight in basket.items()
        )
    return aggregate_constituents(basket)


def _normalize_weights(
    weights: Mapping[str, float],
    weight_unit: Literal["decimal", "percent"],
) -> dict[str, float]:
    """Convert explicitly declared provider weights to decimal weights."""

    values = tuple(weights.values())
    if weight_unit == "percent":
        scale = 100.0
    else:
        if any(weight > 1.0 for weight in values):
            raise ValueError("decimal ETF basket contains weight above one")
        scale = 1.0

    if sum(values) > scale + _WEIGHT_TOLERANCE:
        raise ValueError("ETF basket weight coverage exceeds 100%")
    return {stock_code: weight / scale for stock_code, weight in weights.items()}

