"""v2_short_term 的只读 HTTP API 层。

提供短期异动快照、历史轨迹与异动榜三个端点；不修改 v1 任何路由或快照。
"""
from __future__ import annotations

from .router import router as short_term_router

__all__ = ["short_term_router"]

