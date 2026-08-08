/** 板块行情缩略卡的本地状态、窗口切换和放大入口测试。 */
import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { SectorRotationApiError } from "../api";

const klineMocks = vi.hoisted(() => ({
  useSectorKline: vi.fn(),
}));

vi.mock("./useSectorKline", () => ({ useSectorKline: klineMocks.useSectorKline }));
vi.mock("./LazySectorKlineChart", () => ({
  LazySectorKlineChart: ({ visibleCount }: { visibleCount: number }) => <div data-testid="kline-chart">缩略图窗口：{visibleCount}</div>,
}));

import { SectorKlineCard } from "./SectorKlineCard";

const response = {
  sector_name: "半导体",
  sector_level: 2 as const,
  requested_end_date: "2026-08-06",
  actual_end_date: "2026-08-06",
  price_basis: "equal_weight_composite_index" as const,
  bars: [{ trade_date: "2026-08-06", timestamp: 1785945600000, open: 10, high: 12, low: 9, close: 11, volume: 100, amount: 1_000 }],
  meta: { field_version: "v1" as const, source: "trade_sector_daily" as const, bar_count: 1, skipped_bar_count: 0, warmup_target: 100 as const },
};

/** 使用可控 Hook 返回值渲染缩略卡，隔离 HTTP 与 KLineChart 的无关实现。 */
function renderCard(queryResult: Record<string, unknown>, props: Partial<React.ComponentProps<typeof SectorKlineCard>> = {}) {
  klineMocks.useSectorKline.mockReturnValue(queryResult);
  const onVisibleCountChange = vi.fn();
  const onExpand = vi.fn();
  const view = render(<SectorKlineCard sectorName="半导体" level={2} asOfDate="2026-08-06" isLatestDate visibleCount={120} onVisibleCountChange={onVisibleCountChange} onExpand={onExpand} {...props} />);
  return { ...view, onVisibleCountChange, onExpand };
}

describe("SectorKlineCard", () => {
  it("显示工作台截止日、价格口径、窗口按钮和放大入口", () => {
    const { onExpand } = renderCard({ data: response, isLoading: false, isError: false });

    expect(screen.getByText("板块行情")).toBeInTheDocument();
    expect(screen.getByText((_content, element) => (
      element?.tagName === "P" && element.textContent === "截至 2026-08-06 · 等权合成指数"
    ))).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "显示最近 120 个交易日" })).toHaveAttribute("aria-pressed", "true");
    fireEvent.click(screen.getByRole("button", { name: "放大查看半导体行情" }));
    expect(onExpand).toHaveBeenCalledOnce();
  });

  it("切换可见窗口只更新本地窗口状态，行情查询上下文保持不变", () => {
    const { onVisibleCountChange, rerender } = renderCard({ data: response, isLoading: false, isError: false });

    fireEvent.click(screen.getByRole("button", { name: "显示最近 60 个交易日" }));
    expect(onVisibleCountChange).toHaveBeenCalledWith(60);
    // 模拟抽屉接收窗口回调后的受控重渲染，覆盖真实交互中的第二次 Hook 执行。
    rerender(<SectorKlineCard sectorName="半导体" level={2} asOfDate="2026-08-06" isLatestDate visibleCount={60} onVisibleCountChange={onVisibleCountChange} onExpand={vi.fn()} />);
    // 内部 setState 与受控 props 重渲染均可能再次执行 Hook；关键是请求上下文不含 visibleCount，Query Key 不会变化。
    const expectedQueryContext = { sectorName: "半导体", level: 2, endDate: "2026-08-06", enabled: true, isLatestDate: true };
    expect(klineMocks.useSectorKline.mock.calls.length).toBeGreaterThanOrEqual(2);
    for (const [params] of klineMocks.useSectorKline.mock.calls) {
      expect(params).toEqual(expectedQueryContext);
      expect(params).not.toHaveProperty("visibleCount");
    }
    expect(screen.getByTestId("kline-chart")).toHaveTextContent("缩略图窗口：60");
  });

  it("在加载、无数据、普通错误和数据质量不足时保持局部稳定状态", () => {
    const { rerender } = renderCard({ data: undefined, isLoading: true, isError: false });
    expect(screen.getByLabelText("正在加载板块行情")).toBeInTheDocument();

    klineMocks.useSectorKline.mockReturnValue({ data: undefined, isLoading: false, isError: true, error: new SectorRotationApiError("SECTOR_KLINE_NOT_FOUND", "未找到", "req-404", null) });
    rerender(<SectorKlineCard sectorName="半导体" level={2} asOfDate="2026-08-06" isLatestDate visibleCount={120} onVisibleCountChange={vi.fn()} onExpand={vi.fn()} />);
    expect(screen.getByText("该板块在指定日期前暂无有效行情")).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "放大查看半导体行情" })).not.toBeInTheDocument();

    const refetch = vi.fn();
    klineMocks.useSectorKline.mockReturnValue({ data: undefined, isLoading: false, isError: true, error: new SectorRotationApiError("INTERNAL_ERROR", "服务异常", "req-500", null), refetch });
    rerender(<SectorKlineCard sectorName="半导体" level={2} asOfDate="2026-08-06" isLatestDate visibleCount={120} onVisibleCountChange={vi.fn()} onExpand={vi.fn()} />);
    expect(screen.getByText("请求编号：req-500")).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: "重试板块行情" }));
    expect(refetch).toHaveBeenCalledOnce();

    klineMocks.useSectorKline.mockReturnValue({ data: { ...response, meta: { ...response.meta, skipped_bar_count: 2, bar_count: 1 } }, isLoading: false, isError: false });
    rerender(<SectorKlineCard sectorName="半导体" level={2} asOfDate="2026-08-06" isLatestDate visibleCount={120} onVisibleCountChange={vi.fn()} onExpand={vi.fn()} />);
    expect(screen.getByText("有 2 个交易日行情异常已跳过")).toBeInTheDocument();
    expect(screen.getByText("长期指标仍在形成")).toBeInTheDocument();
  });
});
