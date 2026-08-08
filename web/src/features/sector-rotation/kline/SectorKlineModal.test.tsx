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
  LazySectorKlineChart: ({ mode, visibleCount }: { mode: string; visibleCount: number }) => (
    <div data-testid="expanded-kline-chart">{mode}:{visibleCount}</div>
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
  it("放大图填满 grid 分配的可用轨道，不引入会造成裁剪的桌面最小高度", () => {
    const expandedChartRule = globalStyles.match(/\.sector-kline-chart--expanded\s*\{[^}]*\}/)?.[0] ?? "";
    expect(expandedChartRule).toContain("height: 100%");
    expect(expandedChartRule).toContain("min-height: 0");
    expect(expandedChartRule).not.toContain("clamp(300px");
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
