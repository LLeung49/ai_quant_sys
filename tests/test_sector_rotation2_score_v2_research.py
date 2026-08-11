from __future__ import annotations

import pandas as pd


def _snapshots() -> pd.DataFrame:
    dates = pd.date_range("2024-01-02", periods=4, freq="B")
    rows = []
    for date in dates:
        for rank in range(10):
            rows.append({
                "as_of_date": date,
                "sector_name": f"sector_{rank}",
                "trend_level_score": 0.0,
                "velocity_score": 0.0,
                "acceleration_score": float(rank),
                "participation_score": float(rank),
            })
    return pd.DataFrame(rows)


def _labels() -> pd.DataFrame:
    dates = pd.date_range("2024-01-02", periods=4, freq="B")
    return pd.DataFrame([
        {
            "as_of_date": date,
            "target_date": date + pd.Timedelta(days=1),
            "sector_name": f"sector_{rank}",
            "horizon": 1,
            "excess_return": rank / 100.0,
        }
        for date in dates
        for rank in range(10)
    ])


def test_run_nested_research_writes_auditable_nested_outputs(tmp_path, monkeypatch):
    from morning_conference.sector_rotation2 import run_score_v2_research

    snapshots = _snapshots()
    labels = _labels()
    monkeypatch.setattr(run_score_v2_research, "execute_query", lambda *_: snapshots.to_dict("records"))
    monkeypatch.setattr(run_score_v2_research, "build_forward_return_labels", lambda *_args, **_kwargs: labels)
    outer_windows = [{
        "train_start": pd.Timestamp("2024-01-02"),
        "train_end": pd.Timestamp("2024-01-03"),
        "validation_start": pd.Timestamp("2024-01-04"),
        "validation_end": pd.Timestamp("2024-01-05"),
    }]
    result = run_score_v2_research.run_nested_research(
        level=2,
        start_date="2024-01-02",
        end_date="2024-01-05",
        model_version="v1",
        output_dir=tmp_path,
        horizons=(1,),
        outer_windows=outer_windows,
        inner_window_factory=lambda _dates: [{
            "train_start": pd.Timestamp("2024-01-02"),
            "train_end": pd.Timestamp("2024-01-02"),
            "validation_start": pd.Timestamp("2024-01-03"),
            "validation_end": pd.Timestamp("2024-01-03"),
        }],
    )

    assert result["selection"].iloc[0]["candidate"] == "h1_acceleration"
    assert result["outer"].iloc[0]["sample_count"] == 20
    assert (tmp_path / "sector_rotation2_v2_nested_selection_2024-01-05.csv").exists()
    assert (tmp_path / "sector_rotation2_v2_nested_outer_2024-01-05.csv").exists()
    report = (tmp_path / "sector_rotation2_v2_nested_report_2024-01-05.md").read_text(encoding="utf-8")
    assert "nested_historical_validation" in report
    assert "not a final OOS" in report
