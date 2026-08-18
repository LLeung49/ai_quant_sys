"""Provider-independent ETF constituent normalization and aggregation."""

from __future__ import annotations

import math
import re
from collections.abc import Iterable, Mapping


_CODE_PATTERN = re.compile(
    r"^(?:(?:SH|SZ|BJ)\.?)?(\d{6})(?:\.(?:SH|SZ|BJ))?$",
    re.IGNORECASE,
)


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
