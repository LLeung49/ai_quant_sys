from pathlib import Path


REPORT = Path(__file__).parents[2] / "docs/user_demand/qmt_switch/qmt_bridge_validation_report.md"


def test_validation_report_covers_all_consumers():
    report = REPORT.read_text(encoding="utf-8")
    for name in ("三投影行情", "传统行情", "财务", "Morning K线", "行业分类", "ETF篮子"):
        assert name in report
