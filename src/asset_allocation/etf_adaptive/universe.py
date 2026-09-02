"""Deterministic point-in-time ETF classification and eligibility rules."""

from __future__ import annotations

from datetime import date
import re
from statistics import mean
from typing import Sequence

from .contracts import DualPriceBar, ETFEligibility, ETFMetadata


_EXCHANGE_ETF_CODE = re.compile(r"^(?:5\d{5}\.SH|15\d{4}\.SZ)$", re.IGNORECASE)

_METADATA_EXCLUSION_TOKENS = (
    "债券",
    "货币",
    "现金",
    "黄金",
    "白银",
    "原油",
    "商品",
    "跨境",
    "境外",
    "QDII",
    "反向",
    "杠杆",
)
_INDEX_CODE_EXCLUSION_TOKENS = (
    "NDX",
    "NASDAQ",
    "SPX",
    "S&P",
    "HSI",
    "HSTECH",
)
_NAME_EXCLUSION_TOKENS = _METADATA_EXCLUSION_TOKENS + (
    "债",
    "纳指",
    "纳斯达克",
    "标普",
    "恒生",
    "日经",
)

_INDEX_CODE_GROUPS = {
    "000016.SH": "core_broad",
    "000300.SH": "core_broad",
    "000906.SH": "core_broad",
    "932000.CSI": "core_broad",
    "000905.SH": "small_mid_broad",
    "000852.SH": "small_mid_broad",
    "399006.SZ": "growth_broad",
    "000688.SH": "growth_broad",
    "000922.SH": "defensive",
}

_FALLBACK_GROUP_TOKENS = (
    (
        "defensive",
        ("红利低波", "低波红利", "红利", "低波", "价值", "质量", "高股息"),
    ),
    (
        "core_broad",
        (
            "沪深300",
            "CSI300",
            "CSI 300",
            "中证A500",
            "中证800",
            "上证50",
            "深证100",
            "全市场",
            "全指",
            "核心宽基",
        ),
    ),
    ("small_mid_broad", ("中证500", "中证1000", "中证2000", "国证2000", "中小盘")),
    ("growth_broad", ("创业板", "科创50", "科创100", "成长")),
)


def _contains_token(value: str | None, tokens: tuple[str, ...]) -> bool:
    if value is None:
        return False
    normalized = value.casefold()
    return any(token.casefold() in normalized for token in tokens)


def _classification(metadata: ETFMetadata) -> tuple[str | None, str]:
    if not _EXCHANGE_ETF_CODE.fullmatch(metadata.stock_code.strip()):
        return None, "metadata"
    if metadata.is_cross_border or metadata.is_leveraged:
        return None, "metadata"
    if _contains_token(metadata.fund_type, _METADATA_EXCLUSION_TOKENS):
        return None, "metadata"
    if _contains_token(metadata.tracking_index_code, _INDEX_CODE_EXCLUSION_TOKENS):
        return None, "metadata"
    if _contains_token(metadata.tracking_index_name, _NAME_EXCLUSION_TOKENS):
        return None, "metadata"
    if _contains_token(metadata.fund_name, _NAME_EXCLUSION_TOKENS):
        return None, "metadata"

    index_code = (metadata.tracking_index_code or "").strip().upper()
    if index_code in _INDEX_CODE_GROUPS:
        return _INDEX_CODE_GROUPS[index_code], "metadata"

    fallback_text = " ".join(
        value for value in (metadata.tracking_index_name, metadata.fund_name) if value
    )
    normalized = fallback_text.casefold()
    for group, tokens in _FALLBACK_GROUP_TOKENS:
        if any(token.casefold() in normalized for token in tokens):
            return group, "name_fallback"
    return None, "metadata"


def classify_etf(metadata: ETFMetadata) -> str | None:
    """Return the deterministic supported exposure group, failing closed."""

    return _classification(metadata)[0]


def evaluate_eligibility(
    metadata: ETFMetadata,
    bars: Sequence[DualPriceBar],
    as_of_date: date,
) -> ETFEligibility:
    """Evaluate classification, history, liquidity, and tradability as of a date."""

    observed = sorted(
        (bar for bar in bars if bar.trade_date <= as_of_date),
        key=lambda bar: bar.trade_date,
    )
    category, provenance = _classification(metadata)
    reasons: list[str] = []
    if category is None:
        reasons.append("not_domestic_equity_etf")
    if len(observed) < 252:
        reasons.append("listing_history_lt_252")

    average_amount = (
        mean(bar.amount for bar in observed[-20:]) if len(observed) >= 20 else None
    )
    if average_amount is None or average_amount < 10_000_000:
        reasons.append("avg_amount_20_lt_10000000")

    latest_is_tradable = bool(
        observed
        and observed[-1].trade_date == as_of_date
        and not observed[-1].suspended
    )
    if not latest_is_tradable:
        reasons.append("latest_bar_untradable")

    return ETFEligibility(
        eligible=not reasons,
        rejection_reasons=tuple(reasons),
        exposure_group=category,
        history_session_count=len(observed),
        average_amount_20d=average_amount,
        classification_provenance=provenance,
    )
