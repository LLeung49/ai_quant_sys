"""External ETF source adapters for research-only mapping workflows."""
from __future__ import annotations

from collections.abc import Callable

import pandas as pd


def normalize_etf_code(code: str) -> str:
    """Normalize a Shanghai or Shenzhen listed ETF code to project format."""
    value = str(code).strip().upper()
    if value.endswith((".SH", ".SZ")):
        return value
    if value.startswith(("50", "51", "56", "58")):
        return f"{value}.SH"
    if value.startswith(("15", "16", "18")):
        return f"{value}.SZ"
    raise ValueError(f"unsupported ETF code: {code}")


def fetch_etf_holdings(
    etf_codes: list[str],
    holdings_fetcher: Callable[[str], pd.DataFrame],
    fetched_at: pd.Timestamp,
    max_attempts: int = 2,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Fetch requested ETF holdings and preserve failures as explicit evidence."""
    evidence: list[pd.DataFrame] = []
    failures: list[dict[str, object]] = []
    for etf_code in etf_codes:
        error: Exception | None = None
        for attempt in range(1, max_attempts + 1):
            try:
                frame = holdings_fetcher(etf_code.split(".")[0]).copy()
                frame["etf_code"] = etf_code
                frame["fetched_at"] = fetched_at
                evidence.append(frame)
                error = None
                break
            except Exception as exc:  # source errors become research evidence
                error = exc
        if error is not None:
            failures.append({
                "etf_code": etf_code,
                "fetched_at": fetched_at,
                "failure_reason": f"{type(error).__name__}: {error}",
                "attempt_count": max_attempts,
            })
    return (
        pd.concat(evidence, ignore_index=True) if evidence else pd.DataFrame(),
        pd.DataFrame(failures, columns=["etf_code", "fetched_at", "failure_reason", "attempt_count"]),
    )
