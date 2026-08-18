from datetime import date, timedelta

from morning_conference.sector_rotation2.research.etf_core.execution_evidence import (
    load_etf_execution_evidence,
)


TARGET = date(2026, 8, 18)


def _rows(*, amount: float, latest_close: float = 100.0) -> list[dict[str, object]]:
    return [
        {
            "trade_date": TARGET - timedelta(days=offset),
            "close_price": latest_close if offset == 0 else 100.0,
            "amount": amount,
        }
        for offset in range(20)
    ]


def test_execution_evidence_reads_true_and_false_values_from_price_history() -> None:
    liquid = load_etf_execution_evidence(
        "512480.SH", TARGET, query=lambda *_: _rows(amount=20_000_000, latest_close=105.0),
    )
    illiquid_extended = load_etf_execution_evidence(
        "159995.SZ", TARGET, query=lambda *_: _rows(amount=1_000_000, latest_close=120.0),
    )

    assert liquid is not None
    assert liquid["liquid"] is True
    assert liquid["extended"] is False
    assert illiquid_extended is not None
    assert illiquid_extended["liquid"] is False
    assert illiquid_extended["extended"] is True


def test_execution_evidence_is_missing_without_complete_same_date_history() -> None:
    assert load_etf_execution_evidence("512480.SH", TARGET, query=lambda *_: []) is None
    assert load_etf_execution_evidence(
        "512480.SH", TARGET, query=lambda *_: _rows(amount=20_000_000)[1:],
    ) is None
