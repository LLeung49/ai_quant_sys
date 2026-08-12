# 板块轮动工作台信息层级优化 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将市场指标、行业 Lifecycle 筛选和日期交互归入正确的信息层级，并提升排行榜与抽屉可读性。

**Architecture:** 保持现有页面状态与数据请求；把 Lifecycle 筛选控制从 `MarketSummary` 移到象限工作台，日历保留独立受控组件但以弹层挂载。视觉修改仅使用现有 React、lucide 和 CSS。

**Tech Stack:** React/TypeScript、Vitest/Testing Library、CSS。

## Global Constraints

- 不引入新依赖，不改变后端接口和 Lifecycle 判定规则。
- 无 Lifecycle 的历史快照仍禁用 Lifecycle 观察重点，不能伪造结果。
- 日期弹层不改变筛选区高度，待生成日期的回退快照行为不变。
- 每项生产改动先有失败测试。

---

### Task 1: 触发式交易日历

**Files:**
- Modify: `web/src/features/sector-rotation/filters/TradingCalendar.tsx`
- Modify: `web/src/features/sector-rotation/filters/TradingCalendar.test.tsx`
- Modify: `web/src/features/sector-rotation/filters/RotationFilters.tsx`
- Modify: `web/src/features/sector-rotation/filters/RotationFilters.test.tsx`
- Modify: `web/src/styles/globals.css`
- Modify: `web/src/styles/globals.test.ts`

- [ ] 写失败测试：默认没有 `交易日历` grid；点击日期按钮后出现 grid 且触发按钮 `aria-expanded=true`；再次点击、Escape、外部 pointer down 后关闭。
- [ ] 运行 `npm run test -- --run src/features/sector-rotation/filters/TradingCalendar.test.tsx src/features/sector-rotation/filters/RotationFilters.test.tsx src/styles/globals.test.ts`，确认缺失弹层行为而失败。
- [ ] 实现日期触发按钮、`isOpen` 状态、文档级 Escape/外部点击监听；月历使用绝对定位 `trading-calendar-popover`，选择有效交易日后关闭。
- [ ] 添加弹层定位、z-index、边框和紧凑按钮 CSS；为 popover 和触发状态增加 CSS 契约测试。
- [ ] 运行聚焦测试通过并提交 `feat: collapse rotation trading calendar`。

### Task 2: 工作台观察重点与市场总览瘦身

**Files:**
- Modify: `web/src/features/sector-rotation/summary/MarketSummary.tsx`
- Modify: `web/src/features/sector-rotation/summary/MarketSummary.test.tsx`
- Modify: `web/src/features/sector-rotation/SectorRotationPage.tsx`
- Modify: `web/src/features/sector-rotation/SectorRotationPage.integration.test.tsx`
- Modify: `web/src/styles/globals.css`

- [ ] 写失败测试：MarketSummary 不再渲染趋势/修复/风险/今日变化按钮；象限图标题区渲染 `观察重点` 分段控件；点击“今日 Lifecycle 变化”只留下 `lifecycle_changed=true` 行业并设置 `aria-pressed`。
- [ ] 运行 `npm run test -- --run src/features/sector-rotation/summary/MarketSummary.test.tsx src/features/sector-rotation/SectorRotationPage.integration.test.tsx`，确认失败。
- [ ] 将 MarketSummary 改为只接收 `marketRegime`；在页面图表标题区加入五个观察重点按钮，并把当前 `lifecycleFilter`/`changedOnly` 状态接线到该控件。无 Lifecycle 时禁用四个非“全部”重点并显示简短说明。
- [ ] 为观察重点控件添加响应式 CSS，保证与单日观察/动态回放并列，且过滤只影响象限和排行榜。
- [ ] 运行聚焦测试通过并提交 `feat: move lifecycle focus into workbench`。

### Task 3: 排行榜与 Lifecycle 短标签

**Files:**
- Modify: `web/src/features/sector-rotation/ranking/SectorRanking.tsx`
- Modify: `web/src/features/sector-rotation/ranking/SectorRanking.test.tsx`
- Modify: `web/src/styles/globals.css`
- Modify: `web/src/styles/globals.test.ts`

- [ ] 写失败测试：Lifecycle 显示 `背离｜第 1 日｜今日切换`，未切换时不含“今日切换”；排名变化元素同时含上/下箭头和数值。
- [ ] 运行 `npm run test -- --run src/features/sector-rotation/ranking/SectorRanking.test.tsx src/styles/globals.test.ts`，确认失败。
- [ ] 提取 Lifecycle 短标签格式化函数，使用独立文本片段而非连续含义混杂的标签；将排名列网格末列设为足够固定宽度并禁止变化值折叠。
- [ ] 添加 CSS 契约测试确保桌面排行网格的变化列宽度和 `white-space: nowrap`。
- [ ] 运行聚焦测试通过并提交 `fix: clarify lifecycle ranking labels`。

### Task 4: 抽屉行情信息卡

**Files:**
- Modify: `web/src/features/sector-rotation/detail/SectorDetailDrawer.tsx`
- Modify: `web/src/features/sector-rotation/detail/SectorDetailDrawer.test.tsx`
- Modify: `web/src/styles/globals.css`
- Modify: `web/src/styles/globals.test.ts`

- [ ] 写失败测试：抽屉在 K 线卡前渲染 `板块行情` 信息卡，包含价格口径和截至日期；保留上一状态到当前状态的 Lifecycle 说明。
- [ ] 运行 `npm run test -- --run src/features/sector-rotation/detail/SectorDetailDrawer.test.tsx src/styles/globals.test.ts`，确认失败。
- [ ] 实现带标题、口径、截止日的 `detail-market-context` 卡，使用现有 `asOfDate`/`level` 语义；不触发额外数据请求。
- [ ] 添加统一深色表面、边框、圆角和三层排版 CSS 契约。
- [ ] 运行聚焦测试通过并提交 `feat: refine sector detail market context`。

### Task 5: 回归验证与交付

**Files:** Verify only.

- [ ] 从 `web/` 运行 `npm run test -- --run; npm run lint; npm run build`。
- [ ] 检查 `git diff --check`，手动确认日历默认收起、观察重点位于象限区、市场总览仅有市场环境卡。
- [ ] 报告测试结果及已知 Vite ECharts chunk-size 提示。
