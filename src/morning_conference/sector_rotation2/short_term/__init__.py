"""sector_rotation2 短期异动研究层（v2_short_term）。

定位：提供与 v1 完全解耦的 1~2 个交易日异动参考信号，不参与 v1 主评分、
阶段、Lifecycle 与排名；所有计算、存储、API 与前端展示均独立。

本包按模块文档《sector_rotation2_short_term_v2_plan.md》实现，仅在用户
明确接入数据库并运行 ``run_daily.py`` 后才会产生短期快照。本期不进行
任何回测或有效性评估。

CLI 入口::

    python -m morning_conference.sector_rotation2.short_term.run_daily --help

编程式入口::

    from morning_conference.sector_rotation2.short_term import run_short_term_for
    run_short_term_for(as_of_date="2026-08-08", sector_level=2)
"""
from __future__ import annotations

from .config import DEFAULT_SHORT_TERM_CONFIG, ModelConfigShortTerm, short_term_config_hash
from .features import build_short_term_features, calculate_stock_short_term_features
from .labels import SHORT_TERM_LABEL_PRIORITY, classify_short_term_labels, label_dataframe
from .scoring import score_short_term_panel


# run_daily 的符号通过 PEP 562 ``__getattr__`` 延迟加载，避免在
# ``python -m ...short_term.run_daily`` 时触发 RuntimeWarning。
_LAZY_ATTRS = {
    "run_short_term_for": "morning_conference.sector_rotation2.short_term.run_daily",
    "ShortTermRunResult": "morning_conference.sector_rotation2.short_term.run_daily",
}


def __getattr__(name: str):
    if name in _LAZY_ATTRS:
        import importlib
        module = importlib.import_module(_LAZY_ATTRS[name])
        value = getattr(module, name)
        globals()[name] = value  # 缓存，避免下次再走 importlib。
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return sorted(list(globals().keys()) + list(_LAZY_ATTRS.keys()))


__all__ = [
    "DEFAULT_SHORT_TERM_CONFIG",
    "ModelConfigShortTerm",
    "SHORT_TERM_LABEL_PRIORITY",
    "ShortTermRunResult",
    "build_short_term_features",
    "calculate_stock_short_term_features",
    "classify_short_term_labels",
    "label_dataframe",
    "run_short_term_for",
    "score_short_term_panel",
    "short_term_config_hash",
]