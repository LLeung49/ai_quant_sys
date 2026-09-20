# Sector K-line Chart Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在板块详情抽屉中交付以工作台当前日期为截止日的 K 线、MA/BOLL、成交量和 MACD 三联图，并提供可放大的专业行情弹窗。

**Architecture:** 后端新增一个只读行情端点，从 `trade_sector_daily` 参数化读取最近 350 根日线，并在独立边界模块中完成数值、OHLC 关系和 Asia/Shanghai 时间戳校验。前端使用精确锁定的 KLineChart Core 10.0.0，通过 Zod、TanStack Query、动态 import 和一个可测试的运行时适配层共享缩略图与弹窗数据；弹窗使用原生 `<dialog>` 与 Portal，避免引入额外焦点管理依赖。

**Tech Stack:** Python 3.13、FastAPI、Pydantic、PyMySQL、pytest、React 19、TypeScript 5.7、TanStack Query 5、Zod 3、KLineChart Core 10.0.0、Vitest、Testing Library、原生 `<dialog>`。

## Global Constraints

- 精确安装 `klinecharts@10.0.0`，使用 `package-lock.json` 固定版本，不使用 CDN、KLineChart Pro 或浮动版本。
- 继续保留 ECharts 负责象限图和行业轨迹；本功能不得改造或替换现有 ECharts 组件。
- 只读 `trade_sector_daily`，不得新增或修改数据库表、字段和 DDL，不得在 API 请求时聚合成分股。
- 查询必须包含 `sector_name + sector_level + trade_date <= end_date`，最多返回最近 350 根有效候选日线。
- 所有响应日线必须满足 `trade_date <= requested_end_date`，历史回放不得读取未来数据。
- MA 固定为 5/10/20/60，BOLL 固定为 20/2，VOL 均线固定为 5/10，MACD 固定为 12/26/9 且柱值为 `2 × (DIF - DEA)`。
- A 股颜色固定为红涨绿跌；MA5 金、MA10 蓝、MA20 紫、MA60 粉、BOLL 上下轨青色虚线、DIF 金、DEA 蓝。
- 缩略图默认显示 120 日且禁止缩放和拖动；弹窗支持 60/120/250 日、滚轮缩放、拖动和平移。
- API 使用现有统一错误信封和 `X-Request-ID`；行情局部失败不得导致详情抽屉或整个页面白屏。
- 所有新增 Python/TypeScript 文件头、公开函数、方法和关键分支使用中文注释；方法注释必须明确参数、返回值和异常，遵循现有 Java 风格可读性要求。
- 不直接依赖 `sector_rotation` Python 模块；若确需复用算法，复制到 `sector_rotation2` 并在中文注释中写明来源和新增差异。
- 设计基线为 `src/morning_conference/sector_rotation2/doc/2026-08-07-sector-kline-chart-design.md`。

---

## File Structure

### 后端

- Create `src/morning_conference/sector_rotation2/api/kline.py`：纯行情边界校验、Decimal 转换、交易日解析和 Asia/Shanghai 毫秒时间戳。
- Modify `src/morning_conference/sector_rotation2/api/repository.py`：新增有界、参数化的板块行情查询。
- Modify `src/morning_conference/sector_rotation2/api/schemas.py`：新增 K 线 bar、meta 和成功响应模型。
- Modify `src/morning_conference/sector_rotation2/api/router.py`：新增 `/sector-kline` 路由和稳定参数错误。
- Modify `src/morning_conference/sector_rotation2/api/app.py`：仅为该端点统一映射框架级 422 到 `INVALID_PARAMETER`，其他端点保持原契约。
- Create `tests/test_sector_rotation2_kline.py`：纯边界函数测试。
- Modify `tests/test_sector_rotation2_api_repository.py`：SQL 边界与参数化测试。
- Modify `tests/test_sector_rotation2_api_router.py`：200/404/422/503、未来数据和 Decimal 契约测试。

### 前端

- Modify `web/package.json`、`web/package-lock.json`：精确加入 KLineChart Core 10.0.0。
- Modify `web/src/features/sector-rotation/api.ts`：让统一请求函数接收可选 `AbortSignal`。
- Create `web/src/features/sector-rotation/kline/sectorKlineApi.ts`：Zod 行情契约、类型和请求函数。
- Create `web/src/features/sector-rotation/kline/useSectorKline.ts`：TanStack Query 键、启用条件、取消和缓存策略。
- Create `web/src/features/sector-rotation/kline/sectorKlineConfig.ts`：窗口、指标参数、颜色和 pane 高度常量。
- Create `web/src/features/sector-rotation/kline/indicatorParity.ts`：固定序列的系统 MACD 参考算法与 KLineChart 结果适配。
- Create `web/src/features/sector-rotation/kline/klinechartRuntime.ts`：KLineChart 动态加载、初始化、数据装载、指标创建、窗口和销毁。
- Create `web/src/features/sector-rotation/kline/SectorKlineChart.tsx`：容器可见性、ResizeObserver 和局部初始化错误。
- Create `web/src/features/sector-rotation/kline/LazySectorKlineChart.tsx`：React.lazy 与 Suspense 边界。
- Create `web/src/features/sector-rotation/kline/KlineErrorBoundary.tsx`：局部渲染错误边界。
- Create `web/src/features/sector-rotation/kline/SectorKlineCard.tsx`：抽屉行情卡、窗口按钮、加载/空态/坏数据提示和放大入口。
- Create `web/src/features/sector-rotation/kline/SectorKlineModal.tsx`：Portal、原生 dialog、指标摘要、范围控制和关闭交互。
- Modify `web/src/features/sector-rotation/detail/SectorDetailDrawer.tsx`：接收日期/层级并编排行情卡与弹窗状态。
- Modify `web/src/features/sector-rotation/SectorRotationPage.tsx`：把唯一的 `displayDate` 和当前层级传给抽屉。
- Modify `web/src/styles/globals.css`：行情卡、三联图、弹窗、响应式和 reduced-motion 样式。
- Create/modify corresponding `*.test.ts` and `*.test.tsx` files listed in each task.

### 文档

- Modify `src/morning_conference/sector_rotation2/doc/sector_rotation2_visualization_api.md`：接口字段、错误码、数据质量和示例。
- Modify `web/README.md`：依赖许可证、启动、使用、Review 和排障步骤。

---

### Task 1: 行情边界清洗与时间戳

**Files:**
- Create: `src/morning_conference/sector_rotation2/api/kline.py`
- Create: `tests/test_sector_rotation2_kline.py`

**Interfaces:**
- Consumes: 仓储层原始 `list[dict[str, Any]]` 和已解析的 `datetime.date requested_end_date`。
- Produces: `normalize_sector_kline_rows(rows, requested_end_date) -> tuple[list[dict[str, Any]], int]`；返回严格升序有效 bars 和跳过行数。
- Produces: `trade_date_to_shanghai_timestamp(trade_date) -> int`；返回交易日上海零点 Unix 毫秒。

- [ ] **Step 1: 写失败测试，锁定 Decimal、时区和坏行行为**

```python
from datetime import date
from decimal import Decimal

from morning_conference.sector_rotation2.api.kline import normalize_sector_kline_rows


def valid_row(trade_date_value: str, **overrides: object) -> dict[str, object]:
    """构造一条有效候选行，并允许测试覆盖单个字段。"""
    row: dict[str, object] = {
        "trade_date": date.fromisoformat(trade_date_value),
        "open": 10.0, "high": 11.0, "low": 9.0, "close": 10.5,
        "volume": 1000.0, "amount": 2000.0,
    }
    row.update(overrides)
    return row


def test_normalize_sector_kline_rows_converts_decimal_and_shanghai_midnight() -> None:
    rows = [{
        "trade_date": date(2026, 8, 6),
        "open": Decimal("10.00"), "high": Decimal("11.00"),
        "low": Decimal("9.50"), "close": Decimal("10.50"),
        "volume": Decimal("1000"), "amount": Decimal("2000"),
    }]

    bars, skipped = normalize_sector_kline_rows(rows, date(2026, 8, 6))

    assert skipped == 0
    assert bars == [{
        "trade_date": "2026-08-06", "timestamp": 1785945600000,
        "open": 10.0, "high": 11.0, "low": 9.5, "close": 10.5,
        "volume": 1000.0, "amount": 2000.0,
    }]


def test_normalize_sector_kline_rows_skips_future_duplicate_nan_and_invalid_ohlc() -> None:
    # 同一天第二条、未来日、NaN 和 high < close 均不得进入前端。
    rows = [valid_row("2026-08-04"), valid_row("2026-08-04"),
            valid_row("2026-08-05"), valid_row("2026-08-03", close=float("nan")),
            valid_row("2026-08-02", high=9.0, close=10.0)]

    bars, skipped = normalize_sector_kline_rows(rows, date(2026, 8, 4))

    assert [bar["trade_date"] for bar in bars] == ["2026-08-04"]
    assert skipped == 4
```

- [ ] **Step 2: 运行测试并确认失败原因是模块尚不存在**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/test_sector_rotation2_kline.py -q`

Expected: FAIL with `ModuleNotFoundError: morning_conference.sector_rotation2.api.kline`。

- [ ] **Step 3: 实现最小纯边界模块**

```python
"""板块日 K 线 API 的纯数据边界校验。"""
from __future__ import annotations

from datetime import date, datetime, time
from math import isfinite
from typing import Any
from zoneinfo import ZoneInfo

SHANGHAI_TIMEZONE = ZoneInfo("Asia/Shanghai")


def trade_date_to_shanghai_timestamp(trade_date: date) -> int:
    """将交易日转换为上海时区零点毫秒时间戳。

    参数:
        trade_date: 已解析且不含时间部分的交易日期。
    返回:
        对应 ``00:00:00 Asia/Shanghai`` 的 Unix 毫秒。
    """
    return int(datetime.combine(trade_date, time.min, SHANGHAI_TIMEZONE).timestamp() * 1000)


def normalize_sector_kline_rows(
    rows: list[dict[str, Any]], requested_end_date: date
) -> tuple[list[dict[str, Any]], int]:
    """清洗仓储返回的板块行情行。

    参数:
        rows: 可含 date/string、Decimal、None 或非法浮点数的数据库字典行。
        requested_end_date: 用户请求的截止日期，任何未来行都必须排除。
    返回:
        第一项为日期唯一且严格升序的有效行情；第二项为被排除的原始行数。
    """
```

实现中统一 `float()` 转换数值，使用 `isfinite()`、正数/非负数和 OHLC 关系校验；按交易日排序后保留第一条唯一日期，并把每个非法或重复原始行计入 `skipped`。不得使用 `NaN -> 0` 或自动修正 high/low。

- [ ] **Step 4: 运行纯边界测试**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/test_sector_rotation2_kline.py -q`

Expected: PASS，且至少覆盖有效 Decimal、上海时间戳、未来日、重复日、NaN、负量和 OHLC 关系异常。

- [ ] **Step 5: 提交 Task 1**

```powershell
git add src/morning_conference/sector_rotation2/api/kline.py tests/test_sector_rotation2_kline.py
git commit -m "feat: validate sector kline data boundary"
```

### Task 2: 最近 350 根行情参数化查询

**Files:**
- Modify: `src/morning_conference/sector_rotation2/api/repository.py`
- Modify: `tests/test_sector_rotation2_api_repository.py`

**Interfaces:**
- Consumes: `sector_name: str`、`sector_level: int`、`end_date: str`。
- Produces: `SectorRotationRepository.load_sector_kline(...) -> list[dict[str, Any]]`，返回数据库最近 350 条候选行并按日期升序。

- [ ] **Step 1: 写失败的仓储契约测试**

```python
def test_load_sector_kline_is_parameterized_bounded_and_ascending(monkeypatch) -> None:
    captured: dict[str, object] = {}

    def fake_execute_query(sql, params):
        captured["sql"], captured["params"] = sql, params
        return []

    monkeypatch.setattr("morning_conference.sector_rotation2.api.repository.execute_query", fake_execute_query)
    result = SectorRotationRepository().load_sector_kline("半导体' OR 1=1", 2, "2026-08-06")

    assert result == []
    assert "trade_date <= %s" in captured["sql"]
    assert "ORDER BY trade_date DESC" in captured["sql"]
    assert "LIMIT %s" in captured["sql"]
    assert str(captured["sql"]).rstrip().endswith("ORDER BY trade_date ASC")
    assert captured["params"] == ("半导体' OR 1=1", 2, "2026-08-06", 350)
    assert "OR 1=1" not in captured["sql"]
```

同时增加非法层级测试，断言 3 级行业在执行 SQL 前抛出 `ValueError`。

- [ ] **Step 2: 运行单个仓储测试并确认失败**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/test_sector_rotation2_api_repository.py::test_load_sector_kline_is_parameterized_bounded_and_ascending -q`

Expected: FAIL with `AttributeError: load_sector_kline`。

- [ ] **Step 3: 实现双层排序的有界 SQL**

```python
KLINE_BAR_LIMIT: Final[int] = 350

def load_sector_kline(
    self, sector_name: str, sector_level: int, end_date: str
) -> list[dict[str, Any]]:
    """读取指定截止日前最近 350 根板块合成日线。

    参数:
        sector_name: 完整行业名称，不做模糊匹配。
        sector_level: 申万行业层级，只允许 1 或 2。
        end_date: ISO 截止日期；查询不得返回该日之后数据。
    返回:
        按交易日升序的 OHLCV/成交额候选行；不在仓储层修复坏数据。
    """
    self._validate_level(sector_level)
    sql = """
        SELECT trade_date, open, high, low, close, volume, amount
        FROM (
            SELECT trade_date,
                   open_idx AS open, high_idx AS high, low_idx AS low,
                   close_idx AS close, total_volume AS volume, total_amount AS amount
            FROM trade_sector_daily
            WHERE sector_name = %s AND sector_level = %s AND trade_date <= %s
            ORDER BY trade_date DESC
            LIMIT %s
        ) AS recent_bars
        ORDER BY trade_date ASC
    """
    return list(execute_query(sql, (sector_name, sector_level, end_date, KLINE_BAR_LIMIT)))
```

- [ ] **Step 4: 运行完整仓储测试**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/test_sector_rotation2_api_repository.py -q`

Expected: PASS，现有快照/轨迹/回放查询契约不回归。

- [ ] **Step 5: 提交 Task 2**

```powershell
git add src/morning_conference/sector_rotation2/api/repository.py tests/test_sector_rotation2_api_repository.py
git commit -m "feat: query bounded sector kline history"
```

### Task 3: K 线 HTTP 成功与错误契约

**Files:**
- Modify: `src/morning_conference/sector_rotation2/api/schemas.py`
- Modify: `src/morning_conference/sector_rotation2/api/router.py`
- Modify: `src/morning_conference/sector_rotation2/api/app.py`
- Modify: `tests/test_sector_rotation2_api_router.py`

**Interfaces:**
- Consumes: `GET /api/v1/sector-rotation/sector-kline?sector_name=...&level=2&end_date=YYYY-MM-DD`。
- Produces: `SectorKlineResponse`，字段严格为设计规格中的 `sector_name/sector_level/requested_end_date/actual_end_date/price_basis/bars/meta`。
- Produces errors: 422 `INVALID_PARAMETER`、404 `SECTOR_KLINE_NOT_FOUND`、503 `DATABASE_UNAVAILABLE`、500 `INTERNAL_ERROR`。

- [ ] **Step 1: 写 200、404、422 和未来数据测试**

```python
def test_sector_kline_returns_validated_numeric_bars(monkeypatch) -> None:
    monkeypatch.setattr(SectorRotationRepository, "load_sector_kline", lambda *_: [{
        "trade_date": date(2026, 8, 6),
        "open": Decimal("10"), "high": Decimal("11"),
        "low": Decimal("9"), "close": Decimal("10.5"),
        "volume": Decimal("1000"), "amount": Decimal("2000"),
    }])
    response = TestClient(create_app()).get("/api/v1/sector-rotation/sector-kline", params={
        "sector_name": "半导体", "level": "2", "end_date": "2026-08-06",
    })

    assert response.status_code == 200
    assert response.json()["actual_end_date"] == "2026-08-06"
    assert response.json()["bars"][0]["timestamp"] == 1785945600000
    assert isinstance(response.json()["bars"][0]["close"], float)
    assert response.json()["meta"] == {
        "field_version": "v1", "source": "trade_sector_daily",
        "bar_count": 1, "skipped_bar_count": 0, "warmup_target": 100,
    }
```

补充以下明确断言：

- 仓储空结果和“全部候选行被清洗”都返回 404 `SECTOR_KLINE_NOT_FOUND`。
- 空白行业、65 字符行业、`level=3`、`level=x`、非法日期均返回 422 `INVALID_PARAMETER`，且不访问仓储。
- 仓储即使错误返回未来日，成功响应也不含未来 bar，`skipped_bar_count` 增加。
- MySQL 异常继续由应用层转换为 503，响应不泄漏 SQL/密码。

- [ ] **Step 2: 运行路由新增测试并确认 404 或属性缺失**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/test_sector_rotation2_api_router.py -q -k sector_kline`

Expected: FAIL，因为路由和响应模型尚不存在。

- [ ] **Step 3: 定义强类型响应模型**

```python
class SectorKlineBar(BaseModel):
    """单根经过校验的板块合成日 K 线。"""
    trade_date: str
    timestamp: int
    open: float
    high: float
    low: float
    close: float
    volume: float
    amount: float


class SectorKlineMeta(BaseModel):
    field_version: Literal["v1"] = "v1"
    source: Literal["trade_sector_daily"] = "trade_sector_daily"
    bar_count: int
    skipped_bar_count: int
    warmup_target: int = 100


class SectorKlineResponse(BaseModel):
    sector_name: str
    sector_level: int
    requested_end_date: str
    actual_end_date: str
    price_basis: Literal["equal_weight_composite_index"] = "equal_weight_composite_index"
    bars: list[SectorKlineBar]
    meta: SectorKlineMeta
```

- [ ] **Step 4: 实现端点专用参数解析和成功响应**

在 `router.py` 中新增 `_invalid_parameter(message)` 和 `_parse_sector_kline_request(...)`。`level` 继续声明为整数并保留 OpenAPI 类型，FastAPI 负责类型和 1/2 范围校验；辅助函数执行行业名 strip、空白检查和 `date.fromisoformat(end_date)`。框架级异常由下一段的端点专用错误映射统一转换。

```python
@router.get("/sector-kline", response_model=SectorKlineResponse, summary="读取板块合成日 K 线")
def get_sector_kline(
    sector_name: str = Query(min_length=1, max_length=64),
    level: int = Query(ge=1, le=2, description="申万行业层级，只允许 1 或 2"),
    end_date: str = Query(description="行情截止日，格式 YYYY-MM-DD"),
) -> SectorKlineResponse:
    clean_name, parsed_level, parsed_end_date = _parse_sector_kline_request(
        sector_name, level, end_date
    )
    rows = SectorRotationRepository().load_sector_kline(
        clean_name, parsed_level, parsed_end_date.isoformat()
    )
    bars, skipped = normalize_sector_kline_rows(rows, parsed_end_date)
    if not bars:
        raise _not_found("SECTOR_KLINE_NOT_FOUND", "未找到该板块在指定日期前的有效行情")
    return SectorKlineResponse(
        sector_name=clean_name,
        sector_level=parsed_level,
        requested_end_date=parsed_end_date.isoformat(),
        actual_end_date=bars[-1]["trade_date"],
        bars=bars,
        meta=SectorKlineMeta(bar_count=len(bars), skipped_bar_count=skipped),
    )
```

在 `app.py` 的 `RequestValidationError` 处理器中仅当 `request.url.path.endswith('/sector-kline')` 时使用 `INVALID_PARAMETER`，保证 FastAPI 对缺参、非法整数、越界层级和超长行业等框架级异常也遵循本端点契约；现有接口继续返回 `REQUEST_VALIDATION_ERROR`。同理，未预期异常处理器仅对该端点返回设计规定的 `INTERNAL_ERROR`，其他现有端点继续返回 `INTERNAL_SERVER_ERROR`，并增加回归测试锁定两种行为。

- [ ] **Step 5: 运行路由和 API 回归测试**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/test_sector_rotation2_api_router.py tests/test_sector_rotation2_api_repository.py tests/test_sector_rotation2_kline.py -q`

Expected: PASS，所有新增错误都含 `request_id`，现有接口错误码保持不变。

- [ ] **Step 6: 提交 Task 3**

```powershell
git add src/morning_conference/sector_rotation2/api/schemas.py src/morning_conference/sector_rotation2/api/router.py src/morning_conference/sector_rotation2/api/app.py tests/test_sector_rotation2_api_router.py
git commit -m "feat: expose sector kline read api"
```

### Task 4: 前端 K 线契约、取消和缓存

**Files:**
- Modify: `web/src/features/sector-rotation/api.ts`
- Modify: `web/src/features/sector-rotation/api.test.ts`
- Create: `web/src/features/sector-rotation/kline/sectorKlineApi.ts`
- Create: `web/src/features/sector-rotation/kline/sectorKlineApi.test.ts`
- Create: `web/src/features/sector-rotation/kline/useSectorKline.ts`
- Create: `web/src/features/sector-rotation/kline/useSectorKline.test.tsx`

**Interfaces:**
- Consumes: 后端 `SectorKlineResponse` JSON 和 TanStack Query 提供的 `AbortSignal`。
- Produces: `fetchSectorKline(sectorName, level, endDate, signal?) -> Promise<SectorKlineResponse>`。
- Produces: `useSectorKline({sectorName, level, endDate, enabled, isLatestDate})`。

- [ ] **Step 1: 写 Zod 严格数值和 URL 参数失败测试**

```typescript
it("拒绝字符串价格和不合法 OHLC", async () => {
  vi.stubGlobal("fetch", vi.fn().mockResolvedValue(new Response(JSON.stringify({
    ...validResponse,
    bars: [{ ...validResponse.bars[0], close: "10.5", high: 9 }],
  }))));

  await expect(fetchSectorKline("半导体", 2, "2026-08-06"))
    .rejects.toThrow();
});

it("编码行业、层级和工作台截止日期并透传 signal", async () => {
  const controller = new AbortController();
  const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify(validResponse)));
  vi.stubGlobal("fetch", fetchMock);

  await fetchSectorKline("半导体/设备", 2, "2026-08-06", controller.signal);

  const [url, init] = fetchMock.mock.calls[0];
  expect(new URL(String(url)).searchParams.get("sector_name")).toBe("半导体/设备");
  expect(init.signal).toBe(controller.signal);
});
```

- [ ] **Step 2: 运行 API 单测并确认失败**

Run: `npm run test -- --run src/features/sector-rotation/kline/sectorKlineApi.test.ts`

Expected: FAIL，因为模块尚不存在。

- [ ] **Step 3: 扩展统一 requestJson 并实现严格 Schema**

把 `requestJson` 改为具名导出并增加可选 `signal`，现有调用不传时行为不变：

```typescript
export async function requestJson(
  path: string,
  query: Record<string, string | number> | URLSearchParams,
  signal?: AbortSignal,
): Promise<unknown> {
  // 保留现有错误信封解析，只在 fetch init 中增加 signal。
}
```

`sectorKlineApi.ts` 使用 `z.number().finite().positive()` 校验 OHLC，使用 `finite().nonnegative()` 校验量额，并在 `superRefine` 中校验 high/low、严格升序、唯一日期和 `trade_date <= requested_end_date`。Schema 不允许字符串数值。

- [ ] **Step 4: 写 Query Key、enabled、staleTime 和取消测试**

```typescript
expect(buildSectorKlineQueryKey("半导体", 2, "2026-08-06"))
  .toEqual(["sector-rotation", "sector-kline", "半导体", 2, "2026-08-06"]);
```

通过 `QueryClientProvider` 渲染 hook，断言 `enabled=false` 不请求；`isLatestDate=true` 使用 `60_000`，历史日期使用 `Infinity`；queryFn 把上下文 `signal` 传给 `fetchSectorKline`。

- [ ] **Step 5: 实现 useSectorKline 并运行测试**

```typescript
export function useSectorKline(params: UseSectorKlineParams) {
  return useQuery({
    queryKey: buildSectorKlineQueryKey(params.sectorName, params.level, params.endDate),
    queryFn: ({ signal }) => fetchSectorKline(
      params.sectorName, params.level, params.endDate, signal
    ),
    enabled: params.enabled && Boolean(params.sectorName && params.endDate),
    staleTime: params.isLatestDate ? 60_000 : Infinity,
  });
}
```

Run: `npm run test -- --run src/features/sector-rotation/api.test.ts src/features/sector-rotation/kline/sectorKlineApi.test.ts src/features/sector-rotation/kline/useSectorKline.test.tsx`

Expected: PASS，现有快照和历史 API 客户端不回归。

- [ ] **Step 6: 提交 Task 4**

```powershell
git add web/src/features/sector-rotation/api.ts web/src/features/sector-rotation/api.test.ts web/src/features/sector-rotation/kline/sectorKlineApi.ts web/src/features/sector-rotation/kline/sectorKlineApi.test.ts web/src/features/sector-rotation/kline/useSectorKline.ts web/src/features/sector-rotation/kline/useSectorKline.test.tsx
git commit -m "feat: add sector kline web contract"
```

### Task 5: 精确依赖与 MACD 口径门槛

**Files:**
- Modify: `web/package.json`
- Modify: `web/package-lock.json`
- Create: `web/src/features/sector-rotation/kline/sectorKlineConfig.ts`
- Create: `web/src/features/sector-rotation/kline/indicatorParity.ts`
- Create: `web/src/features/sector-rotation/kline/indicatorParity.test.ts`

**Interfaces:**
- Consumes: KLineChart `getSupportedIndicators()` 的内置 MACD 模板与固定 KLineData 序列。
- Produces: `SYSTEM_MACD_NAME`，值为已验证的 `MACD` 或薄适配器名 `SYSTEM_MACD`。
- Produces: `calculateSystemMacd(closes, fast=12, slow=26, signal=9)`，仅用于测试参考和必要的薄适配器。

- [ ] **Step 1: 精确安装依赖并验证锁文件**

Run: `npm install --save-exact klinecharts@10.0.0`

Expected: `package.json` 出现 `"klinecharts": "10.0.0"`，`npm ls klinecharts` 只解析到 10.0.0。

- [ ] **Step 2: 写固定序列的 Python 口径期望测试**

在 `indicatorParity.test.ts` 固定以下 80 个非线性收盘价，断言参考函数最后三项 DIF/DEA/HIST 为已由现有 Python 口径计算的常量，而不是在测试中重复同一 TypeScript 实现：

```powershell
$env:PYTHONPATH='src'
python -c "import pandas as pd; s=pd.Series([100+i*.18+((i%7)-3)*.42 for i in range(80)]); ef=s.ewm(span=12,adjust=False).mean(); es=s.ewm(span=26,adjust=False).mean(); dif=ef-es; dea=dif.ewm(span=9,adjust=False).mean(); print(dif.tail(3).tolist()); print(dea.tail(3).tolist()); print((2*(dif-dea)).tail(3).tolist())"
```

测试常量固定为：

```typescript
const PYTHON_MACD_TAIL = {
  dif: [1.2699075437491558, 1.1991115788507614, 1.1778428134306438],
  dea: [1.2792604654824336, 1.263230688156099, 1.2461531132110082],
  hist: [-0.01870584346655546, -0.12823821861067541, -0.1366205995607288],
} as const;
```

输入序列在 TypeScript 中用 `Array.from({ length: 80 }, (_, i) => 100 + i * .18 + ((i % 7) - 3) * .42)` 生成，容差 `1e-10`。测试同时从 KLineChart 10.0.0 的 `getSupportedIndicators()` 找到 `MACD`，调用其 `calc`，比较 DIF、DEA 和柱值。

- [ ] **Step 3: 运行口径测试，执行明确决策门槛**

Run: `npm run test -- --run src/features/sector-rotation/kline/indicatorParity.test.ts`

Expected outcome A: 内置 MACD 的 DIF/DEA/HIST 全部通过，则 `SYSTEM_MACD_NAME = "MACD"`，不注册自定义指标。

Expected outcome B: DIF/DEA 一致但柱值为 `DIF - DEA`，或 EMA 初始化不同，则测试必须先失败；随后只注册 `SYSTEM_MACD`，其 `calc` 使用 `adjust=False` 递推公式和 `2 × (DIF - DEA)`，测试改为同时记录内置差异并断言适配器与 Python 常量一致。不得自行实现 MA、BOLL 或 VOL。

- [ ] **Step 4: 集中定义指标和颜色常量**

```typescript
export const KLINE_WINDOWS = [60, 120, 250] as const;
export type KlineWindow = (typeof KLINE_WINDOWS)[number];
export const DEFAULT_KLINE_WINDOW: KlineWindow = 120;
export const INDICATOR_PARAMS = {
  ma: [5, 10, 20, 60], boll: [20, 2], vol: [5, 10], macd: [12, 26, 9],
} as const;
export const KLINE_COLORS = {
  up: "#ff7285", down: "#37d6b0", ma5: "#f0b65a", ma10: "#67a9ff",
  ma20: "#9a8cff", ma60: "#ff8fc7", boll: "#35cbd6", dif: "#f0b65a", dea: "#67a9ff",
} as const;
```

- [ ] **Step 5: 运行依赖、口径和类型验证**

Run: `npm ls klinecharts`

Expected: `klinecharts@10.0.0`，无 invalid/deduped mismatch。

Run: `npm run test -- --run src/features/sector-rotation/kline/indicatorParity.test.ts`

Expected: PASS，并明确证明最终使用的 MACD 名称符合 Python 12/26/9、HIST×2 口径。

- [ ] **Step 6: 提交 Task 5**

```powershell
git add web/package.json web/package-lock.json web/src/features/sector-rotation/kline/sectorKlineConfig.ts web/src/features/sector-rotation/kline/indicatorParity.ts web/src/features/sector-rotation/kline/indicatorParity.test.ts
git commit -m "feat: lock klinecharts and verify macd parity"
```

### Task 6: KLineChart 三联图运行时与生命周期

**Files:**
- Create: `web/src/features/sector-rotation/kline/klinechartRuntime.ts`
- Create: `web/src/features/sector-rotation/kline/klinechartRuntime.test.ts`
- Create: `web/src/features/sector-rotation/kline/SectorKlineChart.tsx`
- Create: `web/src/features/sector-rotation/kline/SectorKlineChart.test.tsx`
- Create: `web/src/features/sector-rotation/kline/LazySectorKlineChart.tsx`
- Create: `web/src/features/sector-rotation/kline/KlineErrorBoundary.tsx`

**Interfaces:**
- Consumes: `SectorKlineBar[]`、`mode: "compact" | "expanded"`、`visibleCount: number` 和已具备正尺寸的 HTMLElement。
- Produces: `createSectorKlineRuntime(options) -> Promise<{ resize(): void; setVisibleCount(count): void; dispose(): void }>`。
- Produces: `<SectorKlineChart bars mode visibleCount ariaLabel />`。

- [ ] **Step 1: 写运行时失败测试，模拟 KLineChart 10 API**

```typescript
it("创建 MA/BOLL、VOL、MACD 三联图并使用本地数据加载器", async () => {
  const chart = fakeChart();
  vi.doMock("klinecharts", () => ({ init: vi.fn(() => chart), dispose: vi.fn() }));

  const runtime = await createSectorKlineRuntime({
    container, bars: fixtureBars, mode: "compact", visibleCount: 120,
  });

  expect(chart.setDataLoader).toHaveBeenCalledOnce();
  expect(chart.setSymbol).toHaveBeenCalledWith(expect.objectContaining({ ticker: "SECTOR_INDEX" }));
  expect(chart.setPeriod).toHaveBeenCalledWith({ span: 1, type: "day" });
  expect(chart.createIndicator).toHaveBeenCalledWith(
    expect.objectContaining({ name: "MA", calcParams: [5, 10, 20, 60], paneId: "candle_pane" }), true,
  );
  expect(chart.createIndicator).toHaveBeenCalledWith(expect.objectContaining({ name: "VOL", calcParams: [5, 10] }));
  expect(chart.createIndicator).toHaveBeenCalledWith(expect.objectContaining({ name: SYSTEM_MACD_NAME, calcParams: [12, 26, 9] }));
  expect(chart.setZoomEnabled).toHaveBeenCalledWith(false);
  expect(chart.setScrollEnabled).toHaveBeenCalledWith(false);
  runtime.dispose();
});
```

另写 expanded 测试断言 zoom/scroll 为 true、pane 高度比例不同；`getBars` 只在 `type === 'init'` 返回升序全部 bars 并调用 `callback(data, false)`，不访问网络、不订阅实时数据。

- [ ] **Step 2: 运行运行时测试并确认模块不存在**

Run: `npm run test -- --run src/features/sector-rotation/kline/klinechartRuntime.test.ts`

Expected: FAIL，因为运行时尚未创建。

- [ ] **Step 3: 实现 KLineChart 10 动态加载与指标创建**

运行时必须遵守 10.x API：使用 `setDataLoader`，不得使用已移除的 `applyNewData`。初始化顺序固定为：

```typescript
const module = await import("klinecharts");
const chart = module.init(container, {
  locale: "zh-CN",
  timezone: "Asia/Shanghai",
  styles: buildKlineStyles(mode),
});
chart.setDataLoader({ getBars: ({ type, callback }) => callback(type === "init" ? data : [], false) });
chart.setSymbol({ ticker: "SECTOR_INDEX", pricePrecision: 4, volumePrecision: 0 });
chart.setPeriod({ span: 1, type: "day" });
chart.createIndicator({ name: "MA", calcParams: [5, 10, 20, 60], paneId: "candle_pane" }, true);
chart.createIndicator({ name: "BOLL", calcParams: [20, 2], paneId: "candle_pane" }, true);
const volumePaneId = chart.createIndicator({ name: "VOL", calcParams: [5, 10] });
const macdPaneId = chart.createIndicator({ name: SYSTEM_MACD_NAME, calcParams: [12, 26, 9] });
```

`data` 必须显式映射为 KLineChart 10 的字段，其中后端 `amount` 对应图表 `turnover`：

```typescript
const data = bars.map((bar) => ({
  timestamp: bar.timestamp,
  open: bar.open, high: bar.high, low: bar.low, close: bar.close,
  volume: bar.volume,
  turnover: bar.amount,
}));
```

通过 `overrideIndicator` 隐藏 BOLL 中轨的绘制但保留值，并把 MA20 Tooltip 标题设置为 `MA20 / BOLL MID`。该配置写成纯函数并测试 figure key/颜色，不能依赖肉眼判断。

- [ ] **Step 4: 实现可见根数算法和销毁**

`setVisibleCount(count)` 使用 `chart.getSize("candle_pane", "main").width` 计算 `clamp(width / count, 1, 50)`，调用 `setBarSpace` 后 `scrollToRealTime(0)`；每次 resize 后重新套用当前 count。`dispose()` 必须幂等，并调用模块级 `dispose(chart)`。

- [ ] **Step 5: 写 React 生命周期失败测试**

测试以下顺序：容器 `clientWidth/clientHeight` 为 0 时不初始化；ResizeObserver 首次报告正尺寸后仅初始化一次；bars 或 mode 变化时先 dispose 旧实例；卸载时 dispose；运行时 reject 时显示局部 `role=alert` 而不是抛到页面顶层。

- [ ] **Step 6: 实现组件、Lazy 和局部错误边界**

`SectorKlineChart.tsx` 只负责 DOM/React 生命周期；所有三方调用都留在运行时文件。`LazySectorKlineChart.tsx` 使用 `lazy(() => import('./SectorKlineChart'))` 和高度稳定的 skeleton。`KlineErrorBoundary` 捕获渲染异常并展示“行情图初始化失败，请重试”。

- [ ] **Step 7: 运行 Task 6 测试**

Run: `npm run test -- --run src/features/sector-rotation/kline/klinechartRuntime.test.ts src/features/sector-rotation/kline/SectorKlineChart.test.tsx`

Expected: PASS；控制台测试不得出现零尺寸初始化和未处理 Promise。

- [ ] **Step 8: 提交 Task 6**

```powershell
git add web/src/features/sector-rotation/kline/klinechartRuntime.ts web/src/features/sector-rotation/kline/klinechartRuntime.test.ts web/src/features/sector-rotation/kline/SectorKlineChart.tsx web/src/features/sector-rotation/kline/SectorKlineChart.test.tsx web/src/features/sector-rotation/kline/LazySectorKlineChart.tsx web/src/features/sector-rotation/kline/KlineErrorBoundary.tsx
git commit -m "feat: render sector kline three-pane chart"
```

### Task 7: 抽屉行情卡与工作台日期联动

**Files:**
- Create: `web/src/features/sector-rotation/kline/SectorKlineCard.tsx`
- Create: `web/src/features/sector-rotation/kline/SectorKlineCard.test.tsx`
- Modify: `web/src/features/sector-rotation/detail/SectorDetailDrawer.tsx`
- Modify: `web/src/features/sector-rotation/detail/SectorDetailDrawer.test.tsx`
- Modify: `web/src/features/sector-rotation/SectorRotationPage.tsx`
- Modify: `web/src/features/sector-rotation/SectorRotationPage.test.tsx`

**Interfaces:**
- Consumes: `sectorName`、`level: 1 | 2`、`asOfDate`、`isLatestDate`、`visibleCount`、`onVisibleCountChange`、`onExpand`。
- Produces: 加载、成功、无数据、错误、坏行和预热不足状态下均稳定的抽屉行情区。
- Modifies drawer props: `SectorDetailDrawer({ sector, level, asOfDate, isLatestDate, onClose })`。

- [ ] **Step 1: 写卡片状态和不重复请求测试**

```typescript
it("显示当前截止日、窗口按钮和放大入口", async () => {
  renderCardWithQuery(validResponse);
  expect(await screen.findByText("板块行情")).toBeInTheDocument();
  expect(screen.getByText("截至 2026-08-06")).toBeInTheDocument();
  expect(screen.getByRole("button", { name: "显示最近 120 个交易日" })).toHaveAttribute("aria-pressed", "true");
  fireEvent.click(screen.getByRole("button", { name: "放大查看半导体行情" }));
  expect(onExpand).toHaveBeenCalledOnce();
});
```

分别模拟 `SECTOR_KLINE_NOT_FOUND`、普通 API 错误、`skipped_bar_count > 0`、`bar_count < visibleCount + 100`，断言局部文案、重试按钮和放大按钮显隐。点击 60/120/250 只更新本地窗口，不增加 fetch 次数。

- [ ] **Step 2: 运行卡片测试并确认失败**

Run: `npm run test -- --run src/features/sector-rotation/kline/SectorKlineCard.test.tsx`

Expected: FAIL，因为卡片尚不存在。

- [ ] **Step 3: 实现查询状态外壳**

卡片只调用一次 `useSectorKline`；成功后把相同 response 传给缩略图和后续弹窗。预热提示使用：

```typescript
const visibleBars = Math.min(visibleCount, data.meta.bar_count);
const warmupUsed = Math.max(0, data.meta.bar_count - visibleBars);
const warmupSufficient = warmupUsed >= data.meta.warmup_target;
```

404 显示“该板块在指定日期前暂无有效行情”且隐藏放大按钮；其他失败显示 `requestId` 和“重试”按钮，调用 query 的 `refetch()`。

- [ ] **Step 4: 写工作台传参失败测试**

在 `SectorRotationPage.test.tsx` mock 抽屉，断言单日和回放模式都传入唯一的 `displayDate`，而不是总使用最新快照日期。切换回放帧后期望 `asOfDate` 同步变化。

- [ ] **Step 5: 修改 Drawer 和 Page**

`SectorRotationPage` 调用：

```tsx
{selected && displayDate && <SectorDetailDrawer
  sector={selected}
  level={level}
  asOfDate={displayDate}
  isLatestDate={displayDate === dates.data?.[0]}
  onClose={() => setSelectedSectorName(null)}
/>}
```

抽屉在三项摘要后插入 `SectorKlineCard`。窗口状态提升到抽屉：`const [visibleCount, setVisibleCount] = useState<KlineWindow>(120)`；行业、日期或层级变化时关闭弹窗但保留默认窗口策略。

- [ ] **Step 6: 运行卡片、抽屉和页面测试**

Run: `npm run test -- --run src/features/sector-rotation/kline/SectorKlineCard.test.tsx src/features/sector-rotation/detail/SectorDetailDrawer.test.tsx src/features/sector-rotation/SectorRotationPage.test.tsx`

Expected: PASS，历史回放日期传入 K 线请求，且窗口切换不产生额外 HTTP 请求。

- [ ] **Step 7: 提交 Task 7**

```powershell
git add web/src/features/sector-rotation/kline/SectorKlineCard.tsx web/src/features/sector-rotation/kline/SectorKlineCard.test.tsx web/src/features/sector-rotation/detail/SectorDetailDrawer.tsx web/src/features/sector-rotation/detail/SectorDetailDrawer.test.tsx web/src/features/sector-rotation/SectorRotationPage.tsx web/src/features/sector-rotation/SectorRotationPage.test.tsx
git commit -m "feat: add kline card to sector drawer"
```

### Task 8: 放大 dialog、Esc 层级、样式与响应式

**Files:**
- Create: `web/src/features/sector-rotation/kline/SectorKlineModal.tsx`
- Create: `web/src/features/sector-rotation/kline/SectorKlineModal.test.tsx`
- Modify: `web/src/features/sector-rotation/detail/SectorDetailDrawer.tsx`
- Modify: `web/src/features/sector-rotation/detail/SectorDetailDrawer.test.tsx`
- Modify: `web/src/styles/globals.css`

**Interfaces:**
- Consumes: 已加载 `SectorKlineResponse`、当前窗口、板块阶段摘要和关闭回调。
- Produces: Portal 到 `document.body` 的原生模态 dialog；关闭后焦点回到放大按钮。
- Produces: 60/120/250 快捷键和 `0/1/2` 三档底部 range control；滑杆索引映射为 60/120/250，共享 `KlineWindow visibleCount`，不产生任意中间窗口值。

- [ ] **Step 1: 写原生 dialog 和关闭层级失败测试**

```typescript
it("第一次 Escape 只关闭行情弹窗，第二次才关闭抽屉", async () => {
  render(<SectorDetailDrawer {...props} onClose={onDrawerClose} />);
  fireEvent.click(await screen.findByRole("button", { name: "放大查看半导体行情" }));
  expect(screen.getByRole("dialog", { name: "半导体 放大行情图" })).toBeInTheDocument();

  fireEvent.keyDown(window, { key: "Escape" });
  expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  expect(onDrawerClose).not.toHaveBeenCalled();

  fireEvent.keyDown(window, { key: "Escape" });
  expect(onDrawerClose).toHaveBeenCalledOnce();
});
```

增加遮罩关闭、右上角关闭、行业/日期变化自动关闭、关闭后焦点恢复和 Modal/compact 共用 response 不新增 fetch 的测试。测试 setup 仅为 jsdom 补充 `HTMLDialogElement.showModal/close`，生产代码使用浏览器原生实现。

- [ ] **Step 2: 运行 modal 测试并确认失败**

Run: `npm run test -- --run src/features/sector-rotation/kline/SectorKlineModal.test.tsx src/features/sector-rotation/detail/SectorDetailDrawer.test.tsx`

Expected: FAIL，因为 Modal 和 Esc 层级尚未实现。

- [ ] **Step 3: 实现 Portal + 原生 dialog**

```tsx
return createPortal(
  <dialog ref={dialogRef} className="sector-kline-dialog"
    aria-label={`${sectorName} 放大行情图`}
    onCancel={(event) => { event.preventDefault(); onClose(); }}
    onClick={(event) => { if (event.target === event.currentTarget) onClose(); }}>
    <div className="sector-kline-modal">...</div>
  </dialog>,
  document.body,
);
```

挂载时调用 `showModal()`，卸载前若仍 open 则 `close()`。使用原生 modal 的背景 inert 与焦点约束，不引入第三方 focus-trap；显式保存 opener ref，关闭后 `.focus()`。

- [ ] **Step 4: 重构抽屉 Esc 处理为单一所有者**

抽屉 window keydown 逻辑必须读取 `isKlineModalOpen`：

```typescript
if (event.key !== "Escape") return;
if (isKlineModalOpen) {
  setKlineModalOpen(false);
  return;
}
onClose();
```

Modal 的 `onCancel` 只处理原生 cancel，不再额外注册第二个 window Escape listener，避免一次按键同时关闭两层。

- [ ] **Step 5: 添加精确布局和 z-index 样式**

CSS 必须包含以下可验证约束：

```css
.sector-kline-card { width: 100%; margin-top: 18px; }
.sector-kline-chart--compact { width: 100%; height: 340px; min-height: 340px; }
.sector-kline-dialog { width: min(92vw, 1440px); height: 88vh; padding: 0; border: 0; background: transparent; color: var(--text); }
.sector-kline-dialog::backdrop { background: rgba(2, 8, 15, .78); backdrop-filter: blur(8px); }
.sector-kline-modal { width: 100%; height: 100%; overflow: hidden; border: 1px solid var(--line-strong); border-radius: 18px; background: #081525; }
.sector-kline-chart--expanded { width: 100%; height: min(68vh, 760px); min-height: 520px; }
```

dialog 作为 top layer 不受抽屉 `z-index: 50` 遮挡；不要再用普通 fixed div 模拟 modal。`@media (max-width: 640px)` 使用 `100vw × 100dvh`、无圆角、紧凑 header；`prefers-reduced-motion` 沿用全局规则。

- [ ] **Step 6: 运行 Task 8 测试与 TypeScript 检查**

Run: `npm run test -- --run src/features/sector-rotation/kline/SectorKlineModal.test.tsx src/features/sector-rotation/detail/SectorDetailDrawer.test.tsx`

Expected: PASS，Esc、遮罩、焦点恢复和共享请求通过。

Run: `npm run lint`

Expected: TypeScript 0 errors。

- [ ] **Step 7: 提交 Task 8**

```powershell
git add web/src/features/sector-rotation/kline/SectorKlineModal.tsx web/src/features/sector-rotation/kline/SectorKlineModal.test.tsx web/src/features/sector-rotation/detail/SectorDetailDrawer.tsx web/src/features/sector-rotation/detail/SectorDetailDrawer.test.tsx web/src/styles/globals.css web/src/test/setup.ts
git commit -m "feat: add expanded sector kline dialog"
```

### Task 9: 契约文档、全量回归与人工验收

**Files:**
- Modify: `src/morning_conference/sector_rotation2/doc/sector_rotation2_visualization_api.md`
- Modify: `web/README.md`
- Verify: all files from Tasks 1-8

**Interfaces:**
- Consumes: 已完成的 API、前端和测试命令。
- Produces: 可由用户逐步启动、使用、排障和 Review 的最终说明；不产生数据库迁移。

- [ ] **Step 1: 更新 API 文档**

增加 `/sector-kline` 的请求参数、200 示例、字段语义、350 根/100 根预热、上海时间戳、实际截止日、数据清洗规则和四个稳定错误码。明确 `amount -> KLineChart turnover`、`trade_sector_daily` 只读、无需 DDL。

- [ ] **Step 2: 更新 README 启动和 Review 流程**

README 增加：

- `klinecharts@10.0.0`、Apache-2.0 和官方链接。
- API 启动后直接验证 `/sector-kline?sector_name=半导体&level=2&end_date=2026-08-06`。
- 在单日观察和动态回放分别打开抽屉，核对 K 线截止日。
- 核对 60/120/250、放大、滚轮、拖动、range、Tooltip、红涨绿跌、指标颜色。
- 核对无数据、坏行、预热不足、API 失败和 `request_id`。
- 明确本功能没有 DDL，启动前只需已有 `trade_sector_daily` 行情。

- [ ] **Step 3: 运行后端完整相关回归**

Run: `$env:PYTHONPATH='src'; python -m pytest tests -q -k sector_rotation2 --basetemp 'D:\aiQuant\ai_quant_sys\.pytest-tmp-sector-kline-final'`

Expected: 0 failed；输出中的 passed 数量必须记录在最终交付说明中。

- [ ] **Step 4: 运行前端全量测试、lint 和生产构建**

Run: `npm run test -- --run`

Expected: 0 failed。

Run: `npm run lint`

Expected: TypeScript 0 errors。

Run: `npm run build`

Expected: exit 0，Vite 生成生产产物；若出现 chunk size 警告，确认 KLineChart 位于动态 chunk 而非首屏主 chunk，并在交付说明中记录。

- [ ] **Step 5: 启动真实服务并完成浏览器验收**

后端：

```powershell
cd D:\aiQuant\ai_quant_sys
$env:PYTHONPATH='src'
uvicorn morning_conference.sector_rotation2.api.app:create_app --factory --host 127.0.0.1 --port 8000
```

前端：

```powershell
cd D:\aiQuant\ai_quant_sys\web
npm run dev
```

浏览器验收记录以下证据：

1. 抽屉三联图容器约 340px、宽度与抽屉一致，不出现零尺寸控制台警告。
2. 2026-08-06 单日观察与历史回放日期分别核对，图上最后一根不晚于工作台日期。
3. 数据库抽取一个交易日，对比 OHLCV/成交额与 Tooltip。
4. 60/120/250 切换不产生额外 `/sector-kline` 请求。
5. 第一次 Esc 只关闭放大 dialog，第二次关闭抽屉；关闭后焦点回到放大按钮。
6. 窄屏 dialog 接近全屏，header、图表和关闭按钮均可用。
7. API 失败仅替换行情卡，评分拆解和详情其他区域仍可读。

- [ ] **Step 6: 检查差异与无数据库变更**

Run: `git diff --check`

Expected: 无行尾空格或冲突标记。

Run: `git diff --name-only | rg "sql|schema|ddl"`

Expected: 无输出；若命中仅因文档路径包含关键词，逐项确认没有数据库脚本变更。

- [ ] **Step 7: 提交文档与最终验收结果**

```powershell
git add src/morning_conference/sector_rotation2/doc/sector_rotation2_visualization_api.md web/README.md
git commit -m "docs: add sector kline usage and review guide"
```

最终交付说明必须列出：提交列表、后端测试 passed 数、前端测试 passed 数、lint/build 结果、真实 API 示例、无需 DDL、已知限制（仅日线、最多 350 根、非实时）。

---

## Recommended Review Checkpoints

1. **Task 1-3 后端 Gate：** 先 Review 查询不越界、坏行不修复、时间戳和统一错误契约，再允许前端接入。
2. **Task 4-5 契约与指标 Gate：** 确认 Zod 不接收字符串数值，MACD 与 Python HIST×2 结果一致，再允许绘图。
3. **Task 6-7 缩略图 Gate：** 确认 KLineChart 10 API、动态加载、dispose、当前工作台日期和局部失败。
4. **Task 8 交互 Gate：** 确认原生 dialog、Esc 层级、焦点和移动端布局。
5. **Task 9 Release Gate：** 全量测试、lint、build 和真实数据浏览器验收全部有新鲜证据后才宣布完成。
