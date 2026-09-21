from data_ingestion_qmt.price_projection_integrity import (
    RawQfqIssue,
    classify_projection_issues,
)


RAW_300316 = {
    "stock_code": "300316.SZ",
    "trade_date": "2015-02-03",
    "open_price": 26.46,
    "high_price": 26.47,
    "low_price": 25.53,
    "close_price": 26.24,
}
QFQ_300316 = {
    "stock_code": "300316.SZ",
    "trade_date": "2015-02-03",
    "open_price": 6.701783,
    "high_price": 6.705280,
    "low_price": 6.376608,
    "close_price": 6.624860,
}


def test_matching_qmt_non_affine_pair_is_warning_not_rebuild():
    decision = classify_projection_issues(
        [RawQfqIssue("300316.SZ", "2015-02-03", "qfq_ohlc_affine_mismatch")],
        [RAW_300316],
        [QFQ_300316],
        [RAW_300316],
        [QFQ_300316],
    )

    assert decision.hard_issues == []
    assert decision.verified_exceptions[0].status == "qmt_verified_exception"


def test_changed_qmt_pair_is_hard_repair_case():
    changed_qfq = {**QFQ_300316, "close_price": 6.7}
    decision = classify_projection_issues(
        [RawQfqIssue("300316.SZ", "2015-02-03", "qfq_ohlc_affine_mismatch")],
        [RAW_300316],
        [QFQ_300316],
        [RAW_300316],
        [changed_qfq],
    )

    assert decision.hard_issues[0].reason == "qmt_storage_mismatch"
