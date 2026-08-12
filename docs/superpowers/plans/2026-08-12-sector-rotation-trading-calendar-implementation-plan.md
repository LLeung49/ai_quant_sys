# 板块轮动交易日历 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 用交易月历替换快照日期下拉框，并将未生成快照的交易日作为可选择、可解释的业务状态。

**Architecture:** 后端提供上游交易日与成功快照日的权威集合；前端用独立查询和受控月历呈现。页面分离用户选中日与实际加载的最近成功快照日，避免对无快照日请求 404。

**Tech Stack:** FastAPI/PyMySQL、React/TypeScript/TanStack Query、Vitest、pytest、CSS。

## Global Constraints

- 不新增日期组件依赖。
- 前端不得用周末规则推断交易日。
- 无快照交易日不得请求 snapshot API，必须展示业务提示。
- SQL 参数化，日历查询必须有日期范围。
- 每项生产变更先有失败测试。

---

### Task 1: 日历可用性 API

**Files:**
- Modify: `src/morning_conference/sector_rotation2/api/repository.py`
- Modify: `src/morning_conference/sector_rotation2/api/schemas.py`
- Modify: `src/morning_conference/sector_rotation2/api/router.py`
- Test: `tests/test_sector_rotation2_api_repository.py`
- Test: `tests/test_sector_rotation2_api_router.py`

**Interfaces:** Produces `load_calendar_availability(level, model_version, start_date, end_date) -> tuple[list[str], list[str]]` and `GET /calendar-availability` with `trade_dates`, `snapshot_dates`, `latest_snapshot_date`.

- [ ] Write failing repository test with upstream dates `2026-08-10/11`, only `2026-08-10` successful; assert SQL parameters include level, date range, succeeded, model version.
- [ ] Write failing router test asserting the endpoint returns the two sets and latest snapshot date.
- [ ] Run `$env:PYTHONPATH='src'; python -m pytest tests/test_sector_rotation2_api_repository.py tests/test_sector_rotation2_api_router.py -q`; expect missing method/route failure.
- [ ] Implement a parameterized `trade_sector_daily` date query and a parameterized successful-run snapshot date query constrained to the same range; add `CalendarAvailabilityResponse` and route date-range validation.
- [ ] Rerun focused tests; commit `feat: expose sector rotation calendar availability`.

### Task 2: 前端 API 与月历组件

**Files:**
- Modify: `web/src/features/sector-rotation/api.ts`
- Modify: `web/src/features/sector-rotation/api.test.ts`
- Create: `web/src/features/sector-rotation/useCalendarAvailability.ts`
- Create: `web/src/features/sector-rotation/useCalendarAvailability.test.tsx`
- Create: `web/src/features/sector-rotation/filters/TradingCalendar.tsx`
- Create: `web/src/features/sector-rotation/filters/TradingCalendar.test.tsx`
- Modify: `web/src/features/sector-rotation/filters/RotationFilters.tsx`
- Modify: `web/src/features/sector-rotation/filters/RotationFilters.test.tsx`
- Modify: `web/src/styles/globals.css`
- Modify: `web/src/styles/globals.test.ts`

**Interfaces:** `fetchCalendarAvailability(level, modelVersion, startDate, endDate)` and `useCalendarAvailability(...)`; `TradingCalendar({ tradeDates, snapshotDates, selectedDate, onDateChange })`.

- [ ] Write failing API/hook tests for parsing calendar response and using displayed month bounds as query key.
- [ ] Write failing calendar test: `2026-08-10` is snapshot, `2026-08-11` is a clickable pending day whose accessible name includes “尚未生成快照”, and non-trade days are disabled.
- [ ] Run focused tests; expect missing exports/components.
- [ ] Add the Zod schema/query hook; implement 7-column month grid with previous/next month controls, ISO date buttons and `data-date-status=snapshot|pending|closed`.
- [ ] Integrate the calendar in `RotationFilters`; style snapshot, pending and closed states with existing dark theme; test CSS selectors.
- [ ] Rerun focused tests; commit `feat: add sector rotation trading calendar`.

### Task 3: 页面日期语义与提示

**Files:**
- Modify: `web/src/features/sector-rotation/SectorRotationPage.tsx`
- Modify: `web/src/features/sector-rotation/SectorRotationPage.integration.test.tsx`
- Modify: `web/src/features/sector-rotation/useRotationData.ts`
- Modify: `web/src/features/sector-rotation/useRotationData.test.tsx`

**Interfaces:** `selectedDate` remains URL/user intent. `loadedSnapshotDate` is the latest `snapshot_dates` member not later than `selectedDate`; only it is sent to `useRotationData`.

- [ ] Write failing integration test selecting `2026-08-11` with only `2026-08-10` snapshot: URL retains 8/11, user sees `2026-08-11 的板块轮动快照尚未生成`, snapshot fetch receives only 8/10.
- [ ] Run focused tests; expect selected pending dates to be unavailable or to cause incorrect fetch.
- [ ] Implement date resolution and a `role=status` notice: `当前展示 {loadedSnapshotDate} 的最近成功快照。`; keep selected pending date when refresh serializes URL.
- [ ] Rerun focused tests; commit `feat: preserve pending rotation trade dates`.

### Task 4: 完整验证

**Files:** Verify only.

- [ ] Run back-end: `$env:PYTHONPATH='src'; python -m pytest tests/test_sector_rotation2_api_repository.py tests/test_sector_rotation2_api_router.py tests/test_sector_rotation2_snapshot_store.py tests/test_sector_rotation2_run_daily.py -q`.
- [ ] Run front-end from `web/`: `npm run test -- --run; npm run lint; npm run build`.
- [ ] Smoke-test `GET /calendar-availability` against port 8000; confirm `2026-08-11` is in `trade_dates` and dates remain separately represented.
- [ ] Run `git diff --check` and report verified behavior and existing tooling warnings.
