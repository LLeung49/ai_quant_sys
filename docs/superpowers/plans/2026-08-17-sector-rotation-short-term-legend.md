# 行业轮动短期异动图例澄清 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 让象限图图例准确说明：颜色表示方向，形状的透明度、大小与发光表示强度，并明确脉冲三角的尖锐度规则。

**Architecture:** 仅调整 `SectorRotationPage` 的图例展示与提示文案。短期异动的标签、强度分级及 `quadrantOption` 形状渲染保持不变；页面测试约束新语义。

**Tech Stack:** React、TypeScript、Vitest、Testing Library。

## Global Constraints

- 不改变 `short_term_intensity` 计算、API 契约或 ECharts 图形编码。
- 方向色仍为涨红、跌绿、量能、反弹、破位五类。
- 强度图例不得将橙、黄、绿解释为主象限图形的颜色规则。

---

### Task 1: 修正短期强度图例文案与示意

**Files:**

- Modify: `web/src/features/sector-rotation/SectorRotationPage.tsx:228-255`
- Modify: `web/src/features/sector-rotation/SectorRotationPage.test.tsx`

**Interfaces:**

- Consumes: `SHORT_TERM_LABEL_DIRECTION_COLOR` 与现有 `.quadrant-anomaly-legend__item` 样式。
- Produces: 保持组件 props 不变的图例 DOM；方向组保留五种颜色，强度组呈现 `强：实 / 中：半透明 / 轻：淡`。

- [ ] **Step 1: 写出失败测试**

新增快照模式渲染用例，mock 可用快照与短期 hook，并断言：

```tsx
expect(screen.getByText("强：实")).toBeInTheDocument();
expect(screen.getByText("中：半透明")).toBeInTheDocument();
expect(screen.getByText("轻：淡")).toBeInTheDocument();
expect(screen.getByText(/脉冲三角越尖越强/)).toBeInTheDocument();
expect(screen.queryByText("强异动")).not.toBeInTheDocument();
```

- [ ] **Step 2: 运行测试并确认失败**

运行 `npm run test -- --run src/features/sector-rotation/SectorRotationPage.test.tsx`；预期因页面仍渲染“强异动 / 中等异动 / 轻度异动”而失败。

- [ ] **Step 3: 最小实现**

将强度组 entries 替换为：

```tsx
{ key: "intense", label: "强：实", swatch: "rgba(220, 232, 248, 1)" }
{ key: "moderate", label: "中：半透明", swatch: "rgba(220, 232, 248, 0.68)" }
{ key: "mild", label: "轻：淡", swatch: "rgba(220, 232, 248, 0.38)" }
```

将提示改为 `颜色按方向区分；强度由形状透明度、大小与发光递减表示，脉冲三角越尖越强。`。

- [ ] **Step 4: 运行测试并确认通过**

运行 `npm run test -- --run src/features/sector-rotation/SectorRotationPage.test.tsx`；预期 PASS。

- [ ] **Step 5: 运行图表相关回归测试**

运行 `npm run test -- --run src/features/sector-rotation/chart/shortTermHalo.test.ts src/features/sector-rotation/chart/quadrantOption.test.ts src/features/sector-rotation/SectorRotationPage.test.tsx`；预期全部 PASS。

- [ ] **Step 6: 提交**

运行 `git add web/src/features/sector-rotation/SectorRotationPage.tsx web/src/features/sector-rotation/SectorRotationPage.test.tsx`，再运行 `git commit -m "fix: clarify short-term anomaly legend"`。
