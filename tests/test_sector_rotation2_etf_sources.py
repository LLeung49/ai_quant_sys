from __future__ import annotations

import pandas as pd
import pytest

from morning_conference.sector_rotation2.etf_sources import fetch_etf_holdings, fetch_etf_universe, normalize_etf_code


def test_normalize_etf_code_adds_exchange_suffix_and_rejects_unknown_prefix():
    assert normalize_etf_code("510300") == "510300.SH"
    assert normalize_etf_code("159915.SZ") == "159915.SZ"

    with pytest.raises(ValueError, match="unsupported ETF code"):
        normalize_etf_code("000001")


def test_fetch_etf_holdings_records_failed_request_without_evidence_rows():
    def rate_limited(_: str) -> pd.DataFrame:
        raise RuntimeError("rate limited")

    evidence, failures = fetch_etf_holdings(
        ["510300.SH"], rate_limited, pd.Timestamp("2026-08-11"), max_attempts=1
    )

    assert evidence.empty
    assert failures.to_dict("records") == [{
        "etf_code": "510300.SH",
        "fetched_at": pd.Timestamp("2026-08-11"),
        "failure_reason": "RuntimeError: rate limited",
        "attempt_count": 1,
    }]


def test_fetch_etf_universe_normalizes_akshare_snapshot():
    result = fetch_etf_universe(
        lambda: pd.DataFrame({"代码": ["510300"], "名称": ["沪深300ETF"]}),
        pd.Timestamp("2026-08-11"),
    )

    assert result.loc[0, "etf_code"] == "510300.SH"
    assert result.loc[0, "source"] == "akshare.fund_etf_spot_em"
