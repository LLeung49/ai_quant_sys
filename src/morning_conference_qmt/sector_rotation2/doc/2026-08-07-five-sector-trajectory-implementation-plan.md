# 五行业轨迹对比实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将行业轨迹对比上限从三个统一提升到五个，并保证前端、API、仓储、配色、提示和文档使用同一边界。

**Architecture:** Python 侧由仓储模块导出 `MAX_HISTORY_SECTORS = 5`，路由和仓储共同使用该常量；TypeScript 侧由历史模块导出 `MAX_TRAJECTORY_SECTORS = 5` 与五种稳定颜色，API 客户端、页面状态、控件和图表配置共同消费。第六个行业在浏览器请求前与服务端查询前均被拒绝。

**Tech Stack:** Python 3.13、FastAPI、PyMySQL、pytest、React 19、TypeScript、ECharts 6、Vitest。

## Global Constraints

- 不修改 MySQL 表结构，不执行 DDL，不重新计算任何指标或阶段。
- 历史接口只读取 `status='succeeded'` 的持久化快照，继续使用参数化 SQL。
- 新增或修改的代码注释使用中文；方法说明明确输入、输出和边界。
- 最多五个行业；第六个行业不得替换已有选择，也不得进入数据库查询。
- 五条轨迹颜色必须稳定且彼此可区分，5/20/60 日切换不得改变颜色顺序。

---

### Task 1: 后端五行业查询契约

**Files:**
- Modify: `src/morning_conference/sector_rotation2/api/repository.py`
- Modify: `src/morning_conference/sector_rotation2/api/router.py`
- Test: `tests/test_sector_rotation2_api_repository.py`
- Test: `tests/test_sector_rotation2_api_router.py`

**Interfaces:**
- Produces: `MAX_HISTORY_SECTORS: Final[int] = 5`。
- Consumes: `SectorRotationRepository.load_sector_history(sector_names, start_date, end_date, sector_level, model_version)`。

- [x] **Step 1: Write failing tests for five accepted and six rejected sectors**

```python
def test_load_sector_history_accepts_five_sectors(monkeypatch):
    monkeypatch.setattr("morning_conference.sector_rotation2.api.repository.execute_query", lambda *_: [])
    result = SectorRotationRepository().load_sector_history(["A", "B", "C", "D", "E"], "2026-07-01", "2026-08-06", 2, "v1")
    assert result == []

def test_load_sector_history_rejects_more_than_five_sectors():
    with pytest.raises(ValueError, match="最多只能查询 5 个行业"):
        SectorRotationRepository().load_sector_history(["A", "B", "C", "D", "E", "F"], "2026-07-01", "2026-08-06", 2, "v1")
```

- [x] **Step 2: Run the focused tests and confirm RED**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/test_sector_rotation2_api_repository.py tests/test_sector_rotation2_api_router.py -q`

Expected: five-sector request fails under the current three-sector limit.

- [x] **Step 3: Implement the shared Python boundary**

```python
from typing import Any, Final

MAX_HISTORY_SECTORS: Final[int] = 5

if not 1 <= len(sector_names) <= MAX_HISTORY_SECTORS:
    raise ValueError(f"最多只能查询 {MAX_HISTORY_SECTORS} 个行业，且至少选择 1 个行业")
```

Import the constant in `router.py` and set `Query(min_length=1, max_length=MAX_HISTORY_SECTORS, description="行业名称，可重复传入最多五个")`.

- [x] **Step 4: Run focused Python tests and confirm GREEN**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/test_sector_rotation2_api_repository.py tests/test_sector_rotation2_api_router.py -q`

Expected: all API repository and router tests pass.

### Task 2: 前端五轨迹选择与稳定配色

**Files:**
- Create: `web/src/features/sector-rotation/history/constants.ts`
- Modify: `web/src/features/sector-rotation/api.ts`
- Modify: `web/src/features/sector-rotation/SectorRotationPage.tsx`
- Modify: `web/src/features/sector-rotation/history/TrajectoryControls.tsx`
- Modify: `web/src/features/sector-rotation/history/trajectoryOption.ts`
- Modify: `web/src/features/sector-rotation/history/SectorTrajectory.tsx`
- Test: `web/src/features/sector-rotation/api.test.ts`
- Test: `web/src/features/sector-rotation/history/TrajectoryControls.test.tsx`
- Test: `web/src/features/sector-rotation/history/trajectoryOption.test.ts`

**Interfaces:**
- Produces: `MAX_TRAJECTORY_SECTORS = 5` and `TRAJECTORY_COLORS` containing exactly five stable colors.
- Consumes: `fetchSectorHistory(sectorNames, startDate, endDate, level, modelVersion)` and `buildTrajectoryOption(trajectories)`.

- [x] **Step 1: Write failing frontend tests**

```typescript
expect(fetchSectorHistory(["A", "B", "C", "D", "E"], start, end, 2, "v1")).resolves.toEqual([]);
await expect(fetchSectorHistory(["A", "B", "C", "D", "E", "F"], start, end, 2, "v1")).rejects.toThrow("最多选择 5 个行业");
expect(buildTrajectoryOption(fiveTrajectories).series).toHaveLength(5);
expect(screen.getByText("已选择 5/5 个行业")).toBeInTheDocument();
```

- [x] **Step 2: Run focused frontend tests and confirm RED**

Run: `npm run test -- --run src/features/sector-rotation/api.test.ts src/features/sector-rotation/history/TrajectoryControls.test.tsx src/features/sector-rotation/history/trajectoryOption.test.ts`

Expected: current API precheck, page selection, control copy and chart slicing still stop at three.

- [x] **Step 3: Implement constants and replace all three-sector limits**

```typescript
export const MAX_TRAJECTORY_SECTORS = 5;
export const TRAJECTORY_COLORS = ["#37d6b0", "#67a9ff", "#f0b65a", "#ff7189", "#a98bff"] as const;
```

Use `MAX_TRAJECTORY_SECTORS` in the API precheck, `SectorRotationPage` comparison state and `TrajectoryControls`; use `TRAJECTORY_COLORS` and `.slice(0, MAX_TRAJECTORY_SECTORS)` in the chart option. When five are already selected, keep the existing five unchanged.

- [x] **Step 4: Run focused frontend tests and confirm GREEN**

Run: `npm run test -- --run src/features/sector-rotation/api.test.ts src/features/sector-rotation/history/TrajectoryControls.test.tsx src/features/sector-rotation/history/trajectoryOption.test.ts`

Expected: five-sector cases pass and six-sector cases are rejected before fetch.

### Task 3: 契约文档与全量回归

**Files:**
- Modify: `src/morning_conference/sector_rotation2/doc/sector_rotation2_visualization_api.md`
- Modify: `src/morning_conference/sector_rotation2/doc/2026-08-06-sector-rotation2-visualization-implementation-plan.md`
- Modify: `web/README.md`

**Interfaces:**
- Documents: one-to-five `sector_name` query parameters and five-color trajectory review procedure.

- [x] **Step 1: Replace three-sector wording with the approved five-sector contract**

Document that one to five sectors are accepted, the sixth is rejected, no DDL is required, and users can remove one of five before adding another.

- [x] **Step 2: Run full verification**

Run:

```powershell
$env:PYTHONPATH='src'
python -m pytest tests/test_sector_rotation2_api_repository.py tests/test_sector_rotation2_api_router.py -q
cd web
npm run lint
npm run test -- --run
npm run build
```

Expected: zero failed tests, zero TypeScript errors and a successful Vite production build; the existing ECharts chunk-size warning is non-blocking.

- [x] **Step 3: Review the final diff**

Run: `git diff --check` and search for stale limits with `rg -n "最多三个|最多 3|length >= 3|length > 3|slice\\(0, 3\\)|max_length=3" src tests web --glob '!web/node_modules/**'`.

Expected: no whitespace errors and no active three-sector limit remains in source, tests or current documentation.
