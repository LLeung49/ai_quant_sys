/** 板块详情抽屉、真实行情卡和原生 Portal 放大窗口的组合回归测试。 */
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";

const apiMocks = vi.hoisted(() => ({ fetchSectorKline: vi.fn() }));

vi.mock("../kline/sectorKlineApi", async (importOriginal) => {
  const actual = await importOriginal<typeof import("../kline/sectorKlineApi")>();
  return { ...actual, fetchSectorKline: apiMocks.fetchSectorKline };
});
vi.mock("../kline/LazySectorKlineChart", () => ({
  LazySectorKlineChart: ({ mode, visibleCount }: { mode: string; visibleCount: number }) => <div data-testid="real-kline-chart">{mode}:{visibleCount}</div>,
}));

import { SectorDetailDrawer, buildKlineModalSelectionIdentity } from "./SectorDetailDrawer";

const sector = { sector_name: "半导体", phase_confirmed: "accel_up", phase_age: 4, phase_confidence: 0.72, composite_rank: 1, rank_change_1d: 2, coverage_ratio: 0.96, trend_level_score: 0.4, velocity_score: 0.5, acceleration_score: 0.3, participation_score: 0.4, volume_score: 0.2 };
const response = {
  sector_name: "半导体", sector_level: 2 as const, requested_end_date: "2026-08-06", actual_end_date: "2026-08-06", price_basis: "equal_weight_composite_index" as const,
  bars: [{ trade_date: "2026-08-06", timestamp: 1785945600000, open: 10, high: 12, low: 9, close: 11, volume: 100, amount: 1_000 }],
  meta: { field_version: "v1" as const, source: "trade_sector_daily" as const, bar_count: 1, skipped_bar_count: 0, warmup_target: 100 as const },
};

/** 使用关闭重试的独立 QueryClient 渲染真实抽屉组合，隔离网络层。 */
function renderDrawer(asOfDate = "2026-08-06") {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  const onClose = vi.fn();
  return { ...render(<QueryClientProvider client={client}><SectorDetailDrawer sector={sector} level={2} asOfDate={asOfDate} isLatestDate onClose={onClose} /></QueryClientProvider>), onClose };
}

describe("SectorDetailDrawer K 线组合", () => {
  it("真实卡片将同一份缓存响应交给 Portal 弹窗，不新增第二次行情请求", async () => {
    apiMocks.fetchSectorKline.mockResolvedValue(response);
    renderDrawer();

    const expandButton = await screen.findByRole("button", { name: "放大查看半导体行情" });
    await waitFor(() => expect(apiMocks.fetchSectorKline).toHaveBeenCalledTimes(1));
    fireEvent.click(expandButton);

    const dialog = await screen.findByRole("dialog", { name: "半导体放大行情图" });
    expect(dialog.parentElement).toBe(document.body);
    expect(dialog).toHaveAttribute("open");
    expect(screen.getByText("收盘指数")).toBeInTheDocument();
    expect(screen.getByText("11")).toBeInTheDocument();
    expect(apiMocks.fetchSectorKline).toHaveBeenCalledTimes(1);
  });

  it("选择身份改变时同步判定旧 modal 不可渲染，避免旧行情在新抽屉闪现", () => {
    expect(buildKlineModalSelectionIdentity("半导体", 2, "2026-08-06")).toBe("半导体|2|2026-08-06");
    expect(buildKlineModalSelectionIdentity("半导体", 2, "2026-08-06")).not.toBe(buildKlineModalSelectionIdentity("电子", 2, "2026-08-06"));
  });

  it("第一次 Escape 的原生 cancel 关闭弹窗并恢复放大按钮焦点，第二次才关闭抽屉", async () => {
    apiMocks.fetchSectorKline.mockResolvedValue(response);
    const { onClose } = renderDrawer();

    const expandButton = await screen.findByRole("button", { name: "放大查看半导体行情" });
    fireEvent.click(expandButton);
    const dialog = await screen.findByRole("dialog", { name: "半导体放大行情图" });
    fireEvent(dialog, new Event("cancel", { bubbles: false, cancelable: true }));

    await waitFor(() => expect(screen.queryByRole("dialog")).not.toBeInTheDocument());
    expect(screen.getByRole("complementary", { name: "半导体 详情" })).toBeInTheDocument();
    expect(expandButton).toHaveFocus();
    fireEvent.keyDown(window, { key: "Escape" });
    expect(onClose).toHaveBeenCalledOnce();
  });
});
