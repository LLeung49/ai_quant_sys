"""板块轮动可视化 API 应用工厂。"""

from __future__ import annotations

import logging
from uuid import uuid4

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pymysql import MySQLError

from .router import router
from ..short_term.api import short_term_router
from .macd_router import macd_router
from .research_router import research_router


LOGGER = logging.getLogger(__name__)


def create_app() -> FastAPI:
    """创建只读板块轮动 API 应用。

    输入：无。
    输出：已注册健康检查和板块轮动路由的 FastAPI 应用实例。
    """
    app = FastAPI(title="AI Quant 板块轮动 API", version="v1", description="仅提供已成功运行的板块轮动研究快照。")
    # 本地 Vite 开发服务器与 API 端口不同，需显式允许浏览器预检请求；不使用通配符，
    # 以便未来部署时由反向代理或配置项收敛到正式站点域名。
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
        # 本机开发时 Vite 会在端口占用后切换端口；只放行 localhost/127.0.0.1，
        # 避免开发端口变化导致页面读取失败，同时不向任意外部域开放 API。
        allow_origin_regex=r"^http://(?:localhost|127\.0\.0\.1):\d+$",
        allow_credentials=False,
        allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"],
        allow_headers=["Accept", "Content-Type", "X-Request-ID"],
    )

    @app.middleware("http")
    async def attach_request_id(request: Request, call_next):
        """为每个 HTTP 请求分配或透传追踪标识。

        输入：HTTP 请求和后续处理器。
        输出：带 ``X-Request-ID`` 响应头的 HTTP 响应，用于跨接口日志定位。
        """
        request.state.request_id = request.headers.get("X-Request-ID", str(uuid4()))
        response = await call_next(request)
        response.headers["X-Request-ID"] = request.state.request_id
        return response

    @app.exception_handler(HTTPException)
    async def handle_http_exception(request: Request, exc: HTTPException) -> JSONResponse:
        """将业务 HTTP 异常转换为统一错误信封。

        输入：原始请求和路由抛出的 ``HTTPException``。
        输出：含 ``code``、``message``、``details`` 与 ``request_id`` 的 JSON 错误响应。
        """
        detail = exc.detail if isinstance(exc.detail, dict) else {"message": str(exc.detail)}
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": {
                "code": detail.get("code", "HTTP_ERROR"),
                "message": detail.get("message", "请求处理失败"),
                "details": detail.get("details"),
                "request_id": request.state.request_id,
            }},
        )

    @app.exception_handler(RequestValidationError)
    async def handle_validation_error(request: Request, exc: RequestValidationError) -> JSONResponse:
        """将请求参数校验异常转换为统一错误信封。

        输入：原始请求和 FastAPI 参数校验异常。
        输出：状态码 422 的统一错误 JSON，并在 ``details`` 中保留字段定位信息。
        """
        # 仅板块 K 线端点将 FastAPI 框架级校验统一映射为产品契约 INVALID_PARAMETER，
        # 其余既有端点必须保留 REQUEST_VALIDATION_ERROR，避免破坏已发布的错误码。
        code = "INVALID_PARAMETER" if request.url.path.endswith("/sector-kline") else "REQUEST_VALIDATION_ERROR"
        return JSONResponse(
            status_code=422,
            content={"error": {
                "code": code,
                "message": "请求参数不合法",
                "details": exc.errors(),
                "request_id": request.state.request_id,
            }},
        )

    @app.exception_handler(MySQLError)
    async def handle_database_error(request: Request, exc: MySQLError) -> JSONResponse:
        """屏蔽数据库异常细节并返回可定位的稳定错误码。

        输入：查询或建立连接时由 PyMySQL 抛出的数据库异常。
        输出：状态码 503 的统一错误信封；完整异常仅进入服务端日志，响应不包含账号、
        地址或 SQL 等敏感信息。
        """
        LOGGER.exception("板块轮动 API 数据库访问失败，request_id=%s", request.state.request_id, exc_info=exc)
        return JSONResponse(
            status_code=503,
            content={"error": {
                "code": "DATABASE_UNAVAILABLE",
                "message": "板块轮动数据服务暂时不可用",
                "details": None,
                "request_id": request.state.request_id,
            }},
        )

    @app.exception_handler(Exception)
    async def handle_unexpected_error(request: Request, exc: Exception) -> JSONResponse:
        """将未预料异常收敛为不泄漏实现细节的统一错误信封。

        输入：未被更具体异常处理器识别的运行时异常。
        输出：状态码 500、稳定错误码和请求追踪标识；异常堆栈仅记录在服务端日志。
        """
        LOGGER.exception("板块轮动 API 未处理异常，request_id=%s", request.state.request_id, exc_info=exc)
        # 仅板块 K 线端点使用设计约定的 INTERNAL_ERROR；既有端点保持原错误码。
        code = "INTERNAL_ERROR" if request.url.path.endswith("/sector-kline") else "INTERNAL_SERVER_ERROR"
        return JSONResponse(
            status_code=500,
            content={"error": {
                "code": code,
                "message": "板块轮动服务处理请求失败",
                "details": None,
                "request_id": request.state.request_id,
            }},
            # 未预期异常会在 BaseHTTPMiddleware 的 call_next 中重新抛出，
            # 因而不会回到请求标识中间件补写响应头，需在此处显式透传。
            headers={"X-Request-ID": request.state.request_id},
        )

    @app.get("/healthz", tags=["系统"], summary="健康检查")
    def healthz() -> dict[str, str]:
        """返回服务健康状态。

        输入：无。
        输出：固定的服务可用状态字典。
        """
        return {"status": "ok"}

    app.include_router(router)
    app.include_router(short_term_router)
    app.include_router(macd_router)
    app.include_router(research_router)
    return app
