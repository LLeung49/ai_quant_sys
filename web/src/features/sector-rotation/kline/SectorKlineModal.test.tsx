/** 板块 K 线放大行情弹窗的原生 dialog、焦点恢复和快捷窗口交互测试。 */
import { fireEvent, render, screen } from "@testing-library/react";
import { createRef } from "react";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it, vi } from "vitest";
import type { SectorKlineResponse } from "./sectorKlineApi";

// 测试工作目录固定为 web；以该目录解析可避开 Vitest 的非 file import.meta.url 限制。
const globalStyles = readFileSync(resolve(process.cwd(), "src/styles/globals.css"), "utf8");

vi.mock("./LazySectorKlineChart", () => ({
  LazySectorKlineChart: ({ mode, visibleCount, waves }: { mode: string; visibleCount: number; waves?: unknown[] }) => (
    <div data-testid="expanded-kline-chart" data-wave-count={waves?.length ?? 0}>{mode}:{visibleCount}</div>
  ),
}));

import { SectorKlineModal } from "./SectorKlineModal";

const response: SectorKlineResponse = {
  sector_name: "半导体",
  sector_level: 2,
  requested_end_date: "2026-08-06",
  actual_end_date: "2026-08-06",
  price_basis: "equal_weight_composite_index",
  bars: [{ trade_date: "2026-08-06", timestamp: 1785945600000, open: 10, high: 12, low: 9, close: 11, volume: 100, amount: 1_000 }],
  meta: { field_version: "v1", source: "trade_sector_daily", bar_count: 1, skipped_bar_count: 0, warmup_target: 100 },
};

describe("SectorKlineModal", () => {
  it("展示波段起止日期、无排名前缀的股票和当前成分映射口径", () => {
    const wave = {
      base_date: "2026-08-04", start_date: "2026-08-05", end_date: "2026-08-06",
      start_timestamp: 1785859200000, end_timestamp: 1785945600000,
      start_low: 9, end_high: 12, trading_days: 2, sector_change_pct: 9,
      is_confirmed: true,
      leaders: [
        { rank: 1, stock_code: "000001.SZ", stock_name: "甲", change_pct: 60 },
        { rank: 2, stock_code: "000002.SZ", stock_name: "乙", change_pct: 50 },
        { rank: 3, stock_code: "000003.SZ", stock_name: "丙", change_pct: 40 },
      ],
    };
    render(<SectorKlineModal data={{ ...response, waves: [wave], membership_asof_mode: "current_mapping" }} visibleCount={120} onVisibleCountChange={vi.fn()} openerRef={createRef()} onClose={vi.fn()} />);
    expect(screen.getByTestId("expanded-kline-chart")).toHaveAttribute("data-wave-count", "1");
    expect(screen.getByText(/2026-08-05.*2026-08-06/)).toBeInTheDocument();
    expect(screen.getByText("甲")).toHaveClass("sector-wave-list__leader-name");
    expect(screen.getByText("+60.00%")).toHaveClass("sector-wave-list__leader-change");
    expect(screen.getByText("乙")).toBeInTheDocument();
    expect(screen.getByText("丙")).toBeInTheDocument();
    expect(screen.queryByText(/龙[123一二三]/)).not.toBeInTheDocument();
    expect(screen.getByText(/当前成分股映射/)).toBeInTheDocument();
  });
  it("放大图保持更高的绘图高度，弹窗内容和波段列表使用同一滚动区域", () => {
    const dialogRule = globalStyles.match(/\.sector-kline-dialog\s*\{[^}]*\}/)?.[0] ?? "";
    const modalRule = globalStyles.match(/\.sector-kline-modal\s*\{[^}]*\}/)?.[0] ?? "";
    const chartWrapRule = globalStyles.match(/\.sector-kline-modal__chart-wrap\s*\{[^}]*\}/)?.[0] ?? "";
    const expandedShellRule = globalStyles.match(/\.sector-kline-chart-shell--expanded\s*\{[^}]*\}/)?.[0] ?? "";
    const expandedChartRule = globalStyles.match(/\.sector-kline-chart--expanded\s*\{[^}]*\}/)?.[0] ?? "";
    const waveListRule = globalStyles.match(/\.sector-wave-list\s*\{[^}]*\}/)?.[0] ?? "";
    expect(dialogRule).toContain("height: 94dvh");
    expect(modalRule).toContain("overflow-y: auto");
    expect(modalRule).toContain("grid-template-rows: auto auto auto auto");
    expect(chartWrapRule).toContain("height: auto");
    expect(chartWrapRule).toContain("min-height: 0");
    expect(chartWrapRule).toContain("box-sizing: border-box");
    expect(expandedShellRule).toContain("height: clamp(700px");
    expect(expandedShellRule).toContain("flex: 0 0 auto");
    expect(expandedChartRule).toContain("height: 100%");
    expect(expandedChartRule).toContain("min-height: 0");
    expect(waveListRule).toContain("max-height: none");
    expect(waveListRule).toContain("overflow: visible");
    expect(globalStyles).toContain("height: max(580px, calc(100dvh - 180px))");
  });

  it("通过 body Portal 显示原生 dialog，并在关闭后恢复打开按钮焦点", () => {
    const onClose = vi.fn();
    const openerRef = createRef<HTMLButtonElement>();
    render(<><button ref={openerRef} type="button">放大查看半导体行情</button><SectorKlineModal data={response} visibleCount={120} onVisibleCountChange={vi.fn()} openerRef={openerRef} onClose={onClose} /></>);

    const dialog = screen.getByRole("dialog", { name: "半导体放大行情图" });
    expect(dialog.parentElement).toBe(document.body);
    expect(dialog).toHaveClass("sector-kline-dialog");
    expect(screen.getByTestId("expanded-kline-chart")).toHaveTextContent("expanded:120");
    fireEvent.click(screen.getByRole("button", { name: "关闭半导体放大行情" }));

    expect(onClose).toHaveBeenCalledOnce();
    expect(openerRef.current).toHaveFocus();
  });

  it("遮罩、原生 cancel 和 60/120/250 档位都按对外契约工作", () => {
    const onClose = vi.fn();
    const onVisibleCountChange = vi.fn();
    const openerRef = createRef<HTMLButtonElement>();
    render(<><button ref={openerRef} type="button">放大查看半导体行情</button><SectorKlineModal data={response} visibleCount={120} onVisibleCountChange={onVisibleCountChange} openerRef={openerRef} onClose={onClose} /></>);

    const dialog = screen.getByRole("dialog", { name: "半导体放大行情图" });
    fireEvent.click(screen.getByRole("button", { name: "显示最近 250 个交易日" }));
    expect(onVisibleCountChange).toHaveBeenCalledWith(250);
    fireEvent.click(dialog);
    expect(onClose).toHaveBeenCalledOnce();
    // Testing Library 没有 fireEvent.cancel；直接派发原生 cancel 事件以覆盖浏览器 Escape 关闭路径。
    const cancelEvent = new Event("cancel", { bubbles: false, cancelable: true });
    fireEvent(dialog, cancelEvent);
    expect(cancelEvent.defaultPrevented).toBe(true);
    expect(onClose).toHaveBeenCalledTimes(2);
  });
});
