"""Old wide imports are evidence, not authority over dated revisions."""

from data_ingestion.financial_recovery.native_stage_reconcile import compare_old_row


def _row(profit):
    return {"revenue": 100., "net_profit": profit, "total_assets": 200.,
            "total_equity": 80., "operating_cashflow": 5.}


def test_reconcile_distinguishes_historical_and_unmatched_versions():
    old = dict(_row(10.), operating_cash_flow=5.)
    assert compare_old_row(old, [_row(10.), _row(11.)]) == "historical_match"
    assert compare_old_row(old, [_row(11.), _row(10.)]) == "latest_match"
    assert compare_old_row(old, [_row(12.)]) == "no_value_match"
    assert compare_old_row(old, []) == "no_candidate"
