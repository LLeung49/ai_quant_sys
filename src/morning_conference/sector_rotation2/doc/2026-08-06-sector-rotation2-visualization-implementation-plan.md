# Sector Rotation 2 Visualization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Build a no-login, read-only sector-rotation web module with a daily quadrant, sector trajectories and all-market replay.

**Architecture:** Python FastAPI exposes only successful versioned snapshots. A separate React/TypeScript/Vite application reads those APIs through TanStack Query and renders ECharts; the browser never accesses MySQL.

**Tech Stack:** Python 3.13, FastAPI, Pydantic, pytest; React, TypeScript, Vite, ECharts, TanStack Query, Tailwind CSS, shadcn/ui, Vitest.

## Global Constraints

- Chinese comments and Java-style input/output documentation are mandatory for new Python functions and nontrivial frontend logic.
- Read only `sector_rotation_sector_daily_snapshot` and `sector_rotation_run_log`; no DDL or changes to calculation code.
- API returns only `status='succeeded'` snapshots, uses parameterized SQL and JSON `null` for absent values.
- Default level is 2; only levels 1 and 2 are accepted. History comparison has a strict five-sector limit.
- UI copy uses research observations and risk prompts, never trading directives or return promises.

### Task 1: API repository and HTTP contract

**Files:** create `src/morning_conference/sector_rotation2/api/{__init__,schemas,repository,router,app}.py`; modify `pyproject.toml`; test `tests/test_sector_rotation2_api_repository.py` and `tests/test_sector_rotation2_api_router.py`.

**Produces:** `create_app() -> FastAPI`, with `GET /healthz`, `/api/v1/sector-rotation/available-dates`, `/snapshot`, `/sector-history`, and `/replay`.

- [ ] Write failing repository tests that mock `execute_query`; assert valid levels, bound date ranges, parameterized SQL, successful-run filter, null preservation and five-sector limit.
- [ ] Run `python -m pytest tests/test_sector_rotation2_api_repository.py -q`; verify it fails because no API exists.
- [ ] Implement typed Pydantic DTOs and repositories. Snapshot metadata includes date, level, model version, regime, multiplier, source freshness and eligible count.
- [ ] Write failing FastAPI TestClient tests for 200, 404 absent data and 422 invalid parameters.
- [ ] Implement router, dependency injection, safe exception mapping, limited CORS and Chinese OpenAPI descriptions; add pinned `fastapi` and `uvicorn[standard]` dependencies.
- [ ] Run both API tests; commit `feat: add sector rotation read api`.

### Task 2: API field dictionary and semantics

**Files:** modify API schemas/repository; create `src/morning_conference/sector_rotation2/doc/sector_rotation2_visualization_api.md`; extend repository tests.

**Produces:** stable response documentation mapping every output property to a source column, Chinese label, user interpretation and null behavior.

- [ ] Test successful snapshot metadata, ineligible sectors, null freshness and historical gaps.
- [ ] Assemble metadata from matching succeeded runs; return ordered stored dates only and never recompute scores/phases.
- [ ] Document fields, phase labels, score-as-relative-value caveat and API errors; run tests and commit `docs: define sector rotation visualization api`.

### Task 3: Web scaffold and visual system

**Files:** create `web/{package.json,vite.config.ts,tsconfig.json,index.html,.env.example,README.md}`, `web/src/{main.tsx,app/App.tsx,app/queryClient.ts,styles/globals.css,test/setup.ts}`, and app-shell tests.

**Produces:** a runnable independent dark-mode React application; `VITE_API_BASE_URL` is its only backend setting.

- [ ] Scaffold with React/TS/Vite, ECharts, TanStack Query, Tailwind, shadcn/ui, Vitest and Testing Library.
- [ ] Write failing shell test for product title, loading skeleton, non-advice footer and keyboard landmark.
- [ ] Implement deep blue-gray tokens, semantic phase colors, reduced-motion CSS and responsive breakpoints; run tests and commit `feat: scaffold sector rotation web app`.

### Task 4: Typed client, filters and market summary

**Files:** create `web/src/features/sector-rotation/{api,types,labels,useSectorRotationQuery}.ts` and `filters/RotationFilters.tsx`, `summary/MarketSummary.tsx` plus tests.

**Produces:** URL-backed `date`, `level`, `modelVersion`, `phase`, `q` state and cached typed snapshot query.

- [ ] Test default latest date/level 2, URL updates, phase/search filtering and distinct unavailable/empty states.
- [ ] Implement fetch DTO validation, query keys/cancellation, label mapping and summary cards for regime, freshness, coverage and counts.
- [ ] Run focused tests; commit `feat: add sector rotation filters and summary`.

### Task 5: Daily quadrant and ranking

**Files:** create `chart/{quadrantOption,QuadrantChart}.tsx`, `ranking/SectorRanking.tsx` and tests; modify `App.tsx`.

**Produces:** fixed `[-1,1]` velocity/acceleration axes, phase colors, volume-sized bubbles, confidence opacity, participation border and shared selection state.

- [ ] Test fixed axes, quadrant labels, phase colors, missing coordinates exclusion, radius clamps and tooltip wording.
- [ ] Implement pure ECharts option builder plus mount/resize/dispose component.
- [ ] Test chart/list selection synchronization and ineligible-sector behavior; implement responsive ranking composition.
- [ ] Run tests; commit `feat: add sector rotation quadrant view`.

### Task 6: Detail drawer and explanation

**Files:** create `detail/{SectorDetailDrawer,ScoreBreakdown,Interpretation}.tsx` plus tests.

**Produces:** focus-managed selected-sector detail, deterministic research-safe interpretation and null/coverage disclosure.

- [ ] Test accelerating, decelerating, repair, missing-data and high-volatility wording; prohibit trading verbs.
- [ ] Implement stage/age/confidence/rank/coverage breakdown and collapsible methodology; test keyboard focus return.
- [ ] Run tests; commit `feat: add sector rotation detail explanation`.

### Task 7: Historical trajectories

**Files:** create `history/{trajectoryOption,SectorTrajectory,TrajectoryControls}.tsx` plus tests; modify query hooks and drawer.

**Produces:** 5/20/60 trading-day trajectory with up to five sectors and gaps rendered as breaks.

- [ ] Test date order, latest highlight, three-series limit, window state and gap segmentation.
- [ ] Implement history query, URL state, trajectory chart, legend and phase-transition list; run tests and commit `feat: add sector rotation trajectories`.

### Task 8: Market replay

**Files:** create `replay/{replayState,ReplayControls,MarketReplay}.tsx` plus tests; modify quadrant option.

**Produces:** deterministic playback reducer and accessible controls; frames are preloaded, so playback makes no new requests.

- [ ] Test reducer bounds, seek, speed, pause-on-completion and selection retention.
- [ ] Implement range retrieval, play/pause/step/slider controls and reduced-motion default; run tests and commit `feat: add sector rotation market replay`.

### Task 9: Full regression, real-data validation and handoff

**Files:** create frontend E2E fixture/test; add design spec to the branch; link from existing validation guide without modifying its user-authored content.

- [ ] Test latest date, level switch, filter, selection, drawer, trajectory and replay using deterministic API fixtures with a historical gap.
- [ ] Write Chinese startup/review guide covering API/frontend commands, data freshness, model version, empty/error/partial coverage states and real level-2 validation.
- [ ] Run `python -m pytest tests/test_sector_rotation2_*.py -q`, `npm run lint`, `npm run test -- --run`, and `npm run build`; commit `docs: complete sector rotation visualization handoff`.

## Coverage self-review

Tasks 1-6 deliver the V1-A static product. Tasks 7-8 deliver the confirmed immediate follow-up dynamic product. Task 9 verifies the complete user path. The plan adds no database table because the current daily snapshot and run log already contain all required fields.

---

## Approved Workbench Consolidation Addendum

### Task 10: Unified frame state and URL contract

**Files:** create `web/src/features/sector-rotation/workbench/{frameState,urlState}.ts`; modify `SectorRotationPage.tsx`; add focused tests.

**Produces:** one `displayDate` and `displaySectors` source used by summary, chart, ranking and detail; URL-backed date, level, mode, phase, query and selected sector.

- [x] Write failing reducer tests proving replay frame changes all consumers and exiting replay restores the prior snapshot date.
- [x] Write failing URL tests for parse/serialize and invalid-value fallback.
- [x] Implement pure state helpers and connect them to the page without adding requests during playback.
- [x] Run focused tests and verify latest replay frame equals the same-date snapshot view model.

### Task 11: Intelligent labels and attention reasons

**Files:** create `chart/attentionPriority.ts`; modify `quadrantOption.ts`, `QuadrantChart.tsx`, `labels.ts`; add tests.

**Produces:** `rankAttention(sectors, selectedName, density) -> AttentionDecision[]`, with stable reasons and label visibility.

- [x] Test selected, top rank, phase change, rank jump, acceleration extreme, weakening and reversal reasons independently.
- [x] Test deterministic priority order, density limits and forced search/selection labels.
- [x] Implement reason chips in Tooltip and ECharts overlap avoidance.
- [x] Add compact/focus/all density control and run chart tests.

### Task 12: Integrated replay controls and selected-sector trail

**Files:** modify `replay/{replayState,ReplayControls}.ts(x)`, `SectorRotationPage.tsx`, `quadrantOption.ts`; remove standalone `MarketReplay` composition; add tests.

**Produces:** one chart panel switching snapshot/replay mode, with play/pause/step/speed/seek and a 10-session selected-sector trail.

- [x] Extend reducer tests for speed, completion pause, mode entry and seek boundaries.
- [x] Test `buildSectorTrail(points, sector, currentDate, 10)` for ordering and missing-coordinate breaks.
- [x] Render replay controls inside the main chart panel and feed its frame to summary/ranking/detail.
- [x] Verify playback uses preloaded points and no standalone second quadrant remains.

### Task 13: Three-sector trajectory analysis

**Files:** create `history/TrajectoryControls.tsx`, `history/historyGaps.ts`; modify history hook/chart/page; add tests.

**Produces:** up to three selected sectors, 5/20/60-session windows, latest-node emphasis, phase transitions and explicit gap disclosure.

- [x] Test add/remove/five-sector limit and deterministic colors.
- [x] Test missing successful dates become line breaks and visible gap summaries.
- [x] Implement comparison controls and grouped history query.
- [x] Run focused history tests.

### Task 14: Contract completion and end-to-end handoff

**Files:** modify API schemas/repository/router and API docs; add frontend integration fixture/test and update `web/README.md`.

**Produces:** response metadata containing freshness/status/field version, distinct stable errors, and a documented end-to-end review path.

- [x] Test metadata and error codes at the API boundary.
- [x] Implement minimal metadata without recomputing stored scores.
- [x] Add deterministic browser-level fixture test for snapshot, replay, label reason, trail and comparison.
- [x] Run Python tests, frontend tests, lint and production build.
