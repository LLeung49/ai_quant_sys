"""Deterministic point-in-time ETF classification and eligibility rules."""

from __future__ import annotations

from datetime import date
import re
from statistics import mean
from typing import Sequence

from .contracts import DualPriceBar, ETFEligibility, ETFMetadata


_EXCHANGE_ETF_CODE = re.compile(
    r"^(?:(?:510|511|512|513|515|516|517|518|560|561|562|563|588|589)"
    r"\d{3}\.SH|159\d{3}\.SZ)$",
    re.IGNORECASE,
)

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
    "港股",
    "香港",
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
    "000010.SH": "core_broad",
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

_DOMESTIC_EQUITY_FUND_TYPE_TOKENS = (
    "domestic equity etf",
    "股票型ETF",
    "股票指数ETF",
    "指数股票型",
)

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

    if not _contains_token(
        metadata.fund_type, _DOMESTIC_EQUITY_FUND_TYPE_TOKENS
    ):
        return None, "metadata"

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

    point_in_time = sorted(
        (bar for bar in bars if bar.trade_date <= as_of_date),
        key=lambda bar: (
            bar.trade_date,
            bar.stock_code,
            bar.amount,
            bar.suspended,
            bar.signal_open,
            bar.signal_high,
            bar.signal_low,
            bar.signal_close,
            bar.raw_open,
            bar.raw_high,
            bar.raw_low,
            bar.raw_close,
            bar.adjustment_ratio,
        ),
    )
    expected_code = metadata.stock_code.strip().upper()
    has_foreign_bar = any(
        bar.stock_code.strip().upper() != expected_code for bar in point_in_time
    )
    has_pre_listing_bar = any(
        bar.stock_code.strip().upper() == expected_code
        and bar.trade_date < metadata.listing_date
        for bar in point_in_time
    )
    matching = [
        bar
        for bar in point_in_time
        if bar.stock_code.strip().upper() == expected_code
        and bar.trade_date >= metadata.listing_date
    ]
    observed_by_date: dict[date, DualPriceBar] = {}
    has_duplicate_date = False
    for bar in matching:
        if bar.trade_date in observed_by_date:
            has_duplicate_date = True
            continue
        observed_by_date[bar.trade_date] = bar
    observed = list(observed_by_date.values())

    category, provenance = _classification(metadata)
    reasons: list[str] = []
    if category is None:
        reasons.append("not_domestic_equity_etf")
    if metadata.listing_date > as_of_date:
        reasons.append("listing_date_after_as_of_date")
    if has_pre_listing_bar:
        reasons.append("bar_date_before_listing_date")
    if has_foreign_bar:
        reasons.append("bar_stock_code_mismatch")
    if has_duplicate_date:
        reasons.append("duplicate_trade_date")
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
