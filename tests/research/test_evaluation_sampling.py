from datetime import date

import pandas as pd

from morning_conference.sector_rotation2.research.evaluation.sampling import sample_signal_frame


def test_event_mode_deduplicates_macd_cross_but_snapshot_keeps_observations() -> None:
    frame = pd.DataFrame({
        "signal_event_id": ["cross", "cross", "cross"], "gc_offset": [0, 1, 2],
        "signal_date": [date(2026, 1, 5), date(2026, 1, 6), date(2026, 1, 7)],
    })
    assert len(sample_signal_frame(frame, "snapshot")) == 3
    events = sample_signal_frame(frame, "event")
    assert len(events) == 1
    assert events.iloc[0]["signal_date"] == date(2026, 1, 5)
