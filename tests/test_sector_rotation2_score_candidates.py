from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from morning_conference.sector_rotation2.score_candidates import CANDIDATE_NAMES, build_candidate_scores


def test_build_candidate_scores_uses_frozen_h1_h2_h3_formulas():
    snapshots = pd.DataFrame(
        {
            "as_of_date": ["2026-01-05"],
            "sector_name": ["A"],
            "trend_level_score": [0.8],
            "velocity_score": [0.4],
            "acceleration_score": [0.2],
            "participation_score": [0.6],
        }
    )

    result = build_candidate_scores(snapshots)

    assert CANDIDATE_NAMES == ("h1_acceleration", "h2_trend_pruned", "h3_trend_reversed")
    assert result.loc[0, "h1_acceleration"] == pytest.approx(0.2)
    assert result.loc[0, "h2_trend_pruned"] == pytest.approx(0.4)
    assert result.loc[0, "h3_trend_reversed"] == pytest.approx(-0.34)


def test_build_candidate_scores_renormalizes_only_available_frozen_weights():
    snapshots = pd.DataFrame(
        {
            "as_of_date": ["2026-01-05", "2026-01-05"],
            "sector_name": ["A", "B"],
            "trend_level_score": [np.nan, np.nan],
            "velocity_score": [np.nan, np.nan],
            "acceleration_score": [0.2, np.nan],
            "participation_score": [0.6, np.nan],
        }
    )

    result = build_candidate_scores(snapshots)

    assert result.loc[0, "h2_trend_pruned"] == pytest.approx(0.4)
    assert result.loc[0, "h3_trend_reversed"] == pytest.approx(0.4)
    assert pd.isna(result.loc[1, "h1_acceleration"])
    assert pd.isna(result.loc[1, "h2_trend_pruned"])
    assert pd.isna(result.loc[1, "h3_trend_reversed"])


def test_build_candidate_scores_rejects_missing_frozen_component_column():
    snapshots = pd.DataFrame(
        {
            "as_of_date": ["2026-01-05"],
            "sector_name": ["A"],
            "trend_level_score": [0.8],
            "velocity_score": [0.4],
            "acceleration_score": [0.2],
        }
    )

    with pytest.raises(ValueError, match="participation_score"):
        build_candidate_scores(snapshots)
