from datetime import date

import pandas as pd

from morning_conference.sector_rotation2.research.evaluation.adapters import MacdSignalAdapter, ShortTermSignalAdapter
from morning_conference.sector_rotation2.research.evaluation.calendar import TradingCalendar


def test_short_term_spec_declares_rank_semantics() -> None:
    adapter = ShortTermSignalAdapter()
    assert adapter.spec.supports_rank_metrics is True
    assert adapter.spec.cross_section_cols == ("signal_date", "sector_level")
    assert adapter.spec.score_col == "signal_score"


def test_macd_normalization_preserves_event_provenance() -> None:
    calendar = TradingCalendar([date(2026, 1, 5), date(2026, 1, 6), date(2026, 1, 7)])
    adapter = MacdSignalAdapter(calendar)
    frame = pd.DataFrame({
        "signal_date": [date(2026, 1, 5), date(2026, 1, 6), date(2026, 1, 7)],
        "entity_code": ["512480.SH"] * 3, "gc_offset": [0, 1, 2],
        "upstream_model_version": ["etf_core_v1"] * 3, "upstream_config_hash": ["cfg"] * 3,
        "upstream_run_id": ["run"] * 3,
    })
    normalized = adapter.normalize(frame)
    assert adapter.spec.supports_rank_metrics is False
    assert adapter.spec.score_col is None
    assert normalized["event_date"].tolist() == [date(2026, 1, 5)] * 3
    assert normalized["signal_event_id"].nunique() == 1
    assert normalized["condition_key"].unique().tolist() == ["macd_metrics_available"]
