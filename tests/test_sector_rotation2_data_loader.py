from __future__ import annotations

import pandas as pd

from morning_conference.sector_rotation2.data_loader import (
    build_market_benchmark,
    validate_sector_frame,
)


def valid_frame() -> pd.DataFrame:
    return pd.DataFrame(
        {"close": [100.0, 110.0], "amount": [10.0, 20.0]},
        index=pd.to_datetime(["2026-01-01", "2026-01-02"]),
    )


def test_validate_sector_frame_rejects_duplicate_dates_and_negative_amount():
    frame = pd.DataFrame(
        {"close": [100.0, 101.0], "amount": [10.0, -1.0]},
        index=pd.to_datetime(["2026-01-02", "2026-01-02"]),
    )

    result = validate_sector_frame(frame)

    assert result.valid is False
    assert {"duplicate_trade_date", "negative_amount"} <= set(result.reasons)


def test_build_market_benchmark_uses_only_eligible_sector_frames():
    invalid = valid_frame().assign(amount=[10.0, -1.0])

    benchmark = build_market_benchmark({"A": valid_frame(), "B": invalid})

    assert benchmark["eligible_sector_count"].iloc[-1] == 1
    assert benchmark["amount"].tolist() == [10.0, 20.0]
