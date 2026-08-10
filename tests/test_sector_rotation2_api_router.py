"""板块轮动可视化 HTTP API 的契约测试。"""

from __future__ import annotations

from datetime import date
from decimal import Decimal

import pytest
from fastapi.testclient import TestClient
from pymysql import MySQLError


def test_sector_kline_returns_validated_numeric_bars(monkeypatch) -> None:
    """输入：有效 Decimal K 线；输出：严格的数值 bar 与稳定元数据。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(SectorRotationRepository, "load_sector_kline", lambda *_: [{
        "trade_date": date(2026, 8, 6),
        "open": Decimal("10"), "high": Decimal("11"),
        "low": Decimal("9"), "close": Decimal("10.5"),
        "volume": Decimal("1000"), "amount": Decimal("2000"),
    }])

    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/sector-kline",
        params={"sector_name": " 半导体 ", "level": "2", "end_date": "2026-08-06"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert set(payload) == {
        "sector_name", "sector_level", "requested_end_date", "actual_end_date",
        "price_basis", "bars", "meta",
    }
    assert payload["sector_name"] == "半导体"
    assert payload["actual_end_date"] == "2026-08-06"
    assert payload["price_basis"] == "equal_weight_composite_index"
    assert set(payload["bars"][0]) == {
        "trade_date", "timestamp", "open", "high", "low", "close", "volume", "amount",
    }
    assert payload["bars"][0]["timestamp"] == 1785945600000
    assert isinstance(payload["bars"][0]["close"], float)
    assert payload["meta"] == {
        "field_version": "v1",
        "source": "trade_sector_daily",
        "bar_count": 1,
        "skipped_bar_count": 0,
        "warmup_target": 100,
    }


@pytest.mark.parametrize(
    ("params", "break_name"),
    [
        ({"sector_name": "   ", "level": "2", "end_date": "2026-08-06"}, "空白行业名称进入仓储"),
        ({"sector_name": "A" * 65, "level": "2", "end_date": "2026-08-06"}, "超长行业名称进入仓储"),
        ({"sector_name": "半导体", "level": "3", "end_date": "2026-08-06"}, "超出范围层级进入仓储"),
        ({"sector_name": "半导体", "level": "x", "end_date": "2026-08-06"}, "非整数层级进入仓储"),
        ({"sector_name": "半导体", "level": "2", "end_date": "2026-99-99"}, "非法日期进入仓储"),
    ],
)
def test_sector_kline_rejects_invalid_parameters_before_repository(monkeypatch, params, break_name: str) -> None:
    """输入：非法 K 线查询参数；输出：端点专用 422，且不查询仓储。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(
        SectorRotationRepository,
        "load_sector_kline",
        lambda *_: pytest.fail(break_name),
    )

    response = TestClient(create_app()).get("/api/v1/sector-rotation/sector-kline", params=params)

    assert response.status_code == 422
    assert response.json()["error"]["code"] == "INVALID_PARAMETER"
    assert response.json()["error"]["request_id"] == response.headers["x-request-id"]


@pytest.mark.parametrize(
    "rows",
    [
        [],
        [{
            "trade_date": date(2026, 8, 6),
            "open": Decimal("10"), "high": Decimal("9"),
            "low": Decimal("8"), "close": Decimal("10"),
            "volume": Decimal("1000"), "amount": Decimal("2000"),
        }],
    ],
)
def test_sector_kline_returns_not_found_for_empty_or_unusable_rows(monkeypatch, rows) -> None:
    """输入：空结果或全部无效候选行；输出：统一 K 线未找到错误。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(SectorRotationRepository, "load_sector_kline", lambda *_: rows)

    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/sector-kline",
        params={"sector_name": "半导体", "level": "2", "end_date": "2026-08-06"},
    )

    assert response.status_code == 404
    assert response.json()["error"]["code"] == "SECTOR_KLINE_NOT_FOUND"
    assert response.json()["error"]["request_id"] == response.headers["x-request-id"]


def test_sector_kline_excludes_future_rows_and_counts_them_as_skipped(monkeypatch) -> None:
    """输入：仓储误返回未来数据；输出：响应不泄露未来 bar 且统计跳过行。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(SectorRotationRepository, "load_sector_kline", lambda *_: [
        {
            "trade_date": date(2026, 8, 6),
            "open": Decimal("10"), "high": Decimal("11"), "low": Decimal("9"),
            "close": Decimal("10"), "volume": Decimal("1000"), "amount": Decimal("2000"),
        },
        {
            "trade_date": date(2026, 8, 7),
            "open": Decimal("11"), "high": Decimal("12"), "low": Decimal("10"),
            "close": Decimal("11"), "volume": Decimal("1100"), "amount": Decimal("2200"),
        },
    ])

    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/sector-kline",
        params={"sector_name": "半导体", "level": "2", "end_date": "2026-08-06"},
    )

    assert response.status_code == 200
    assert response.json()["actual_end_date"] == "2026-08-06"
    assert response.json()["meta"]["skipped_bar_count"] == 1
    assert [bar["trade_date"] for bar in response.json()["bars"]] == ["2026-08-06"]


def test_sector_kline_maps_database_and_unexpected_failures_to_endpoint_contract(monkeypatch) -> None:
    """输入：K 线仓储的数据库与未知异常；输出：专用安全错误码和请求标识。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    def raise_database_error(*_args):
        raise MySQLError("password=secret; SELECT * FROM trade_sector_daily")

    monkeypatch.setattr(SectorRotationRepository, "load_sector_kline", raise_database_error)
    database_response = TestClient(create_app(), raise_server_exceptions=False).get(
        "/api/v1/sector-rotation/sector-kline",
        params={"sector_name": "半导体", "level": "2", "end_date": "2026-08-06"},
    )

    assert database_response.status_code == 503
    assert database_response.json()["error"]["code"] == "DATABASE_UNAVAILABLE"
    assert "secret" not in database_response.text
    assert database_response.json()["error"]["request_id"] == database_response.headers["x-request-id"]

    monkeypatch.setattr(SectorRotationRepository, "load_sector_kline", lambda *_: (_ for _ in ()).throw(RuntimeError("internal secret")))
    unexpected_response = TestClient(create_app(), raise_server_exceptions=False).get(
        "/api/v1/sector-rotation/sector-kline",
        params={"sector_name": "半导体", "level": "2", "end_date": "2026-08-06"},
    )

    assert unexpected_response.status_code == 500
    assert unexpected_response.json()["error"]["code"] == "INTERNAL_ERROR"
    assert "secret" not in unexpected_response.text
    assert unexpected_response.json()["error"]["request_id"] == unexpected_response.headers["x-request-id"]


def test_non_kline_validation_and_unexpected_errors_keep_existing_codes(monkeypatch) -> None:
    """输入：既有端点的框架校验和未知异常；输出：原有错误码不被 K 线规则影响。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    validation_response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/snapshot",
        params={"as_of_date": "2026-08-06", "level": "3", "model_version": "v1"},
    )
    monkeypatch.setattr(SectorRotationRepository, "list_available_dates", lambda *_: (_ for _ in ()).throw(RuntimeError("internal secret")))
    unexpected_response = TestClient(create_app(), raise_server_exceptions=False).get(
        "/api/v1/sector-rotation/available-dates",
        params={"level": "2", "model_version": "v1"},
    )

    assert validation_response.status_code == 422
    assert validation_response.json()["error"]["code"] == "REQUEST_VALIDATION_ERROR"
    assert unexpected_response.status_code == 500
    assert unexpected_response.json()["error"]["code"] == "INTERNAL_SERVER_ERROR"


def test_snapshot_returns_not_found_when_no_successful_snapshot(monkeypatch) -> None:
    """输入：不存在成功快照的日期；输出：404 和可读错误码。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(SectorRotationRepository, "load_snapshot", lambda *_: [])
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/snapshot",
        params={"as_of_date": "2026-08-04", "level": 2, "model_version": "v1"},
    )

    assert response.status_code == 404
    assert response.headers["x-request-id"]
    assert response.json() == {
        "error": {
            "code": "SNAPSHOT_NOT_FOUND",
            "message": "未找到已成功运行的板块快照",
            "details": None,
            "request_id": response.headers["x-request-id"],
        }
    }


def test_snapshot_rejects_unsupported_sector_level() -> None:
    """输入：三级行业参数；输出：422，不应执行数据查询。"""
    from morning_conference.sector_rotation2.api.app import create_app

    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/snapshot",
        params={"as_of_date": "2026-08-04", "level": 3, "model_version": "v1"},
    )

    assert response.status_code == 422
    assert response.json()["error"]["code"] == "REQUEST_VALIDATION_ERROR"
    assert response.json()["error"]["request_id"] == response.headers["x-request-id"]


def test_available_dates_returns_successful_run_dates(monkeypatch) -> None:
    """输入：行业层级和模型版本；输出：前端可选的成功运行日期。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(SectorRotationRepository, "list_available_dates", lambda *_: ["2026-08-04", "2026-08-03"])
    response = TestClient(create_app()).get("/api/v1/sector-rotation/available-dates", params={"level": 2, "model_version": "v1"})

    assert response.status_code == 200
    assert response.json() == {
        "sector_level": 2,
        "model_version": "v1",
        "dates": ["2026-08-04", "2026-08-03"],
        "meta": {
            "run_status": "succeeded",
            "field_version": "v1",
            "source_max_trade_date": None,
            "eligible_sector_count": None,
            "skipped_sector_count": None,
            "market_regime": None,
            "regime_multiplier": None,
        },
    }


def test_snapshot_serializes_mysql_decimal_metrics_as_json_numbers(monkeypatch) -> None:
    """输入：含 MySQL Decimal 指标的快照行；输出：前端可直接运算的 JSON number。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(
        SectorRotationRepository,
        "load_snapshot",
        lambda *_: [{"sector_name": "教育", "composite_score": Decimal("0.73129092"), "velocity_score": Decimal("0.95")}],
    )
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/snapshot",
        params={"as_of_date": "2026-08-04", "level": 2, "model_version": "v1"},
    )

    assert response.status_code == 200
    assert response.json()["sectors"][0]["composite_score"] == 0.73129092
    assert isinstance(response.json()["sectors"][0]["composite_score"], float)


def test_snapshot_returns_stable_run_metadata_without_leaking_internal_columns(monkeypatch) -> None:
    """输入：含运行审计字段的快照；输出：统一 meta，行业记录不暴露内部辅助字段。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(
        SectorRotationRepository,
        "load_snapshot",
        lambda *_: [{
            "sector_name": "半导体",
            "market_regime": "high_volatility",
            "regime_multiplier": Decimal("0.85"),
            "_source_max_trade_date": "2026-08-04",
            "_eligible_sector_count": 113,
            "_skipped_sector_count": 0,
        }],
    )
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/snapshot",
        params={"as_of_date": "2026-08-04", "level": 2, "model_version": "v1"},
    )

    assert response.status_code == 200
    assert response.json()["meta"] == {
        "run_status": "succeeded",
        "field_version": "v1",
        "source_max_trade_date": "2026-08-04",
        "eligible_sector_count": 113,
        "skipped_sector_count": 0,
        "market_regime": "high_volatility",
        "regime_multiplier": 0.85,
    }
    assert all(not key.startswith("_") for key in response.json()["sectors"][0])


def test_sector_history_returns_standard_not_found_when_no_stored_points(monkeypatch) -> None:
    """输入：没有存储点的历史区间；输出：统一的 404 错误信封。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(SectorRotationRepository, "load_sector_history", lambda *_: [])
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/sector-history",
        params=[("sector_name", "半导体"), ("start_date", "2026-07-01"), ("end_date", "2026-08-04")],
    )

    assert response.status_code == 404
    assert response.json()["error"]["code"] == "HISTORY_NOT_FOUND"


def test_sector_history_accepts_five_sector_names(monkeypatch) -> None:
    """输入：五个行业名称；输出：通过 HTTP 参数校验并一次传入仓储层。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    captured: dict[str, object] = {}

    def fake_history(_self, sector_names, *_args):
        captured["sector_names"] = sector_names
        return [{"as_of_date": "2026-08-06", "sector_name": sector_names[0]}]

    monkeypatch.setattr(SectorRotationRepository, "load_sector_history", fake_history)
    sectors = ["半导体", "通信设备", "软件开发", "证券", "贵金属"]
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/sector-history",
        params=[*(('sector_name', name) for name in sectors), ("start_date", "2026-07-01"), ("end_date", "2026-08-06")],
    )

    assert response.status_code == 200
    assert captured["sector_names"] == sectors


def test_sector_history_rejects_six_sector_names_before_repository(monkeypatch) -> None:
    """输入：六个行业名称；输出：422 且不访问仓储层。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(SectorRotationRepository, "load_sector_history", lambda *_: pytest.fail("六行业请求不应进入仓储层"))
    sectors = ["A", "B", "C", "D", "E", "F"]
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/sector-history",
        params=[*(('sector_name', name) for name in sectors), ("start_date", "2026-07-01"), ("end_date", "2026-08-06")],
    )

    assert response.status_code == 422
    assert response.json()["error"]["code"] == "REQUEST_VALIDATION_ERROR"


@pytest.mark.parametrize("origin", ["http://localhost:5173", "http://127.0.0.1:5174"])
def test_api_allows_local_vite_origin_for_browser_requests(origin: str) -> None:
    """输入：本机任意 Vite 开发端口的 CORS 预检；输出：允许该源读取只读 API。"""
    from morning_conference.sector_rotation2.api.app import create_app

    response = TestClient(create_app()).options(
        "/api/v1/sector-rotation/snapshot",
        headers={"Origin": origin, "Access-Control-Request-Method": "GET"},
    )

    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == origin


def test_database_failure_returns_stable_safe_error(monkeypatch) -> None:
    """输入：数据库连接异常；输出：503 稳定错误码，不向浏览器泄漏连接详情。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    def fail_query(*_args) -> list[str]:
        raise MySQLError("password=secret; connection refused")

    monkeypatch.setattr(SectorRotationRepository, "list_available_dates", fail_query)
    response = TestClient(create_app(), raise_server_exceptions=False).get(
        "/api/v1/sector-rotation/available-dates",
        params={"level": 2, "model_version": "v1"},
    )

    assert response.status_code == 503
    assert response.json()["error"]["code"] == "DATABASE_UNAVAILABLE"
    assert "secret" not in response.text
    assert response.json()["error"]["request_id"] == response.headers["x-request-id"]


def test_replay_rejects_reversed_date_range_with_stable_error(monkeypatch) -> None:
    """输入：开始日晚于结束日；输出：422 稳定业务错误，且不访问仓储层。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    monkeypatch.setattr(SectorRotationRepository, "load_replay", lambda *_: pytest.fail("非法区间不应执行查询"))
    response = TestClient(create_app()).get(
        "/api/v1/sector-rotation/replay",
        params={"start_date": "2026-08-05", "end_date": "2026-08-04", "level": 2, "model_version": "v1"},
    )

    assert response.status_code == 422
    assert response.json()["error"]["code"] == "INVALID_DATE_RANGE"


def test_unexpected_failure_still_returns_uniform_error_envelope(monkeypatch) -> None:
    """输入：未预料的服务端异常；输出：500 统一错误信封且不泄漏内部详情。"""
    from morning_conference.sector_rotation2.api.app import create_app
    from morning_conference.sector_rotation2.api.repository import SectorRotationRepository

    def fail_query(*_args) -> list[str]:
        raise RuntimeError("internal secret detail")

    monkeypatch.setattr(SectorRotationRepository, "list_available_dates", fail_query)
    response = TestClient(create_app(), raise_server_exceptions=False).get(
        "/api/v1/sector-rotation/available-dates",
        params={"level": 2, "model_version": "v1"},
    )

    assert response.status_code == 500
    assert response.json()["error"]["code"] == "INTERNAL_SERVER_ERROR"
    assert "secret" not in response.text
