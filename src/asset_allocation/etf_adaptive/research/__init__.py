"""Research orchestration built on top of the adaptive ETF backtest.

The research pipeline stages parameter screening, walk-forward validation,
baselines, performance metrics, mode attribution, two-level selection,
portfolio construction, and reproducible artifact publication.
"""

from .baselines import (
    BaselineKind,
    BaselineRun,
    run_baselines,
)
from .metrics import (
    AttributionEvent,
    ModeAttribution,
    PerformanceMetrics,
    Trade,
    attribute_by_mode,
    calculate_performance,
    max_drawdown,
    recovery_sessions,
    session_returns,
)
from .parameters import (
    ParameterCandidate,
    grid_candidates,
    stable_parameter_neighborhood,
    trend_candidates,
)
from .portfolio import (
    PairwiseRisk,
    build_equal_weight,
    build_inverse_volatility,
    correlation,
    downside_correlation,
    drawdown_overlap,
    pairwise_risk,
)
from .report import (
    ResearchArtifact,
    ResearchReportManifest,
    write_research_report,
)
from .run_research import (
    ResearchRunConfig,
    run_research,
)
from .selection import (
    CandidateMetrics,
    PortfolioMetrics,
    ProductMetrics,
    dominates,
    pareto_front,
    select_best_product,
    select_products_by_index,
)
from .walk_forward import (
    FrozenWindowSelection,
    StagedSelector,
    StagedWalkForwardRequest,
    TrainingSurfacePointLike,
    WalkForwardResult,
    WalkForwardWindow,
    build_windows,
    run_staged_walk_forward,
)

__all__ = [
    "AttributionEvent",
    "BaselineKind",
    "BaselineRun",
    "CandidateMetrics",
    "FrozenWindowSelection",
    "ModeAttribution",
    "ParameterCandidate",
    "PairwiseRisk",
    "PerformanceMetrics",
    "PortfolioMetrics",
    "ProductMetrics",
    "ResearchArtifact",
    "ResearchReportManifest",
    "ResearchRunConfig",
    "StagedSelector",
    "StagedWalkForwardRequest",
    "Trade",
    "TrainingSurfacePointLike",
    "WalkForwardResult",
    "WalkForwardWindow",
    "attribute_by_mode",
    "build_equal_weight",
    "build_inverse_volatility",
    "build_windows",
    "calculate_performance",
    "correlation",
    "dominates",
    "downside_correlation",
    "drawdown_overlap",
    "grid_candidates",
    "max_drawdown",
    "pairwise_risk",
    "pareto_front",
    "recovery_sessions",
    "run_baselines",
    "run_research",
    "run_staged_walk_forward",
    "select_best_product",
    "select_products_by_index",
    "session_returns",
    "stable_parameter_neighborhood",
    "trend_candidates",
    "write_research_report",
]
