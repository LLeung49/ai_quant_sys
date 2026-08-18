from morning_conference.sector_rotation2.research.orchestrator.run_daily import build_parser


def test_runner_accepts_live_and_backfill_modes() -> None:
    parser = build_parser()
    live = parser.parse_args(["--as-of-date", "2026-08-18", "--level", "1"])
    backfill = parser.parse_args(["--backfill-start", "2026-08-10", "--backfill-end", "2026-08-18", "--level", "2"])
    assert live.as_of_date == "2026-08-18"
    assert backfill.backfill_end == "2026-08-18"
