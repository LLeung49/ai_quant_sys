from datetime import date

from data_ingestion.repair_market_volume_units import (
    VolumeRepairCandidate,
    build_repair_plan,
    iter_months,
    month_window,
)


def candidate(*, volume: int, stock_code: str = "600000.SH") -> VolumeRepairCandidate:
    return VolumeRepairCandidate(
        table_name="trade_stock_daily_qfq",
        stock_code=stock_code,
        trade_date=date(2026, 8, 12),
        volume=volume,
        amount=1_000_000,
        close_price=10,
    )


def test_build_repair_plan_contains_only_share_unit_rows():
    plan = build_repair_plan([
        candidate(volume=100_000),
        candidate(volume=1_000, stock_code="600001.SH"),
    ])

    assert plan.row_counts == {"trade_stock_daily_qfq": 1}
    assert plan.candidates[0].normalized_volume == 1_000


def test_build_repair_plan_reports_affected_date_bounds():
    plan = build_repair_plan([
        candidate(volume=100_000),
        VolumeRepairCandidate(
            table_name="trade_stock_daily_qfq",
            stock_code="600002.SH",
            trade_date=date(2026, 8, 13),
            volume=200_000,
            amount=2_000_000,
            close_price=10,
        ),
    ])

    assert plan.start_date == date(2026, 8, 12)
    assert plan.end_date == date(2026, 8, 13)


def test_month_window_returns_half_open_calendar_month():
    assert month_window("2026-08") == (date(2026, 8, 1), date(2026, 9, 1))
    assert month_window("2026-12") == (date(2026, 12, 1), date(2027, 1, 1))


def test_iter_months_includes_both_endpoints():
    assert list(iter_months("2026-07", "2026-09")) == ["2026-07", "2026-08", "2026-09"]
