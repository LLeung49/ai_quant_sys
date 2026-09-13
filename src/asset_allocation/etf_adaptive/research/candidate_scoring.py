"""Deterministic ranking of training evidence inside an approved plateau."""

from dataclasses import dataclass
from typing import Mapping, Sequence

from .parameters import conservative_config_key


@dataclass(frozen=True)
class TrainingCandidateScore:
    """Equal-subperiod excess metrics; no validation observations are inputs.

    ``positive_subperiod_share`` retains the stability rule's non-lagging
    convention (strategy return >= B&H return). Cost drag is total strategy
    cost divided by the sum of starting training NAVs; exposure is the share
    of recorded training sessions with an invested position. Family and axes
    distinguish repeated configurations across sequential screening stages.
    """

    config_hash: str
    config: Mapping[str, object]
    positive_subperiod_share: float
    sortino_excess: float
    sharpe_excess: float
    drawdown_improvement: float
    cvar5_improvement: float
    cost_drag: float
    exposure_ratio: float
    stable: bool
    rejection_reason: str | None
    family: str = "full"
    screened_axes: tuple[str, ...] = ()


def select_stable_representative(
    scores: Sequence[TrainingCandidateScore],
) -> TrainingCandidateScore | None:
    """Apply the stability gate before lexicographic training-only ranking."""
    stable = (score for score in scores if score.stable)
    return min(stable, key=lambda score: (
        -score.positive_subperiod_share,
        -score.sortino_excess,
        -score.sharpe_excess,
        score.cost_drag,
        conservative_config_key(score.config),
        score.config_hash,
    ), default=None)
