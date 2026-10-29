/** 使用真实图表验证可见窗口内的 MACD 纵轴缩放，Canvas 由测试环境提供。 */
import { afterEach, describe, expect, it, vi } from "vitest";
import * as klinecharts from "klinecharts";
import { createSectorKlineRuntime, type SectorKlineRuntime } from "./klinechartRuntime";
import { SYSTEM_MACD_NAME } from "./indicatorParity";

// 只记录初始化返回的真实实例；指标计算、窗格布局和纵轴计算均执行原库逻辑。
vi.mock("klinecharts", async (importOriginal) => {
  const actual = await importOriginal<typeof import("klinecharts")>();
  return { ...actual, init: vi.fn(actual.init) };
});

describe("MACD 可见窗口纵轴", () => {
  let runtime: SectorKlineRuntime | undefined;
  let host: HTMLDivElement | undefined;

  afterEach(() => {
    runtime?.dispose();
    host?.remove();
    vi.restoreAllMocks();
    vi.unstubAllGlobals();
  });

  async function createChart(mode: "compact" | "expanded", closes: number[]) {
    vi.stubGlobal("ResizeObserver", class {
      observe() {}
      unobserve() {}
      disconnect() {}
    });
    host = document.createElement("div");
    // jsdom 不计算布局，图表内部创建的 100% 容器也需要有效尺寸。
    vi.spyOn(HTMLElement.prototype, "clientWidth", "get").mockReturnValue(960);
    vi.spyOn(HTMLElement.prototype, "clientHeight", "get").mockReturnValue(740);
    document.body.append(host);
    const initSpy = vi.mocked(klinecharts.init);
    initSpy.mockClear();
    const bars = closes.map((close, index) => {
      return { trade_date: "2026-08-04", timestamp: 1700000000000 + index * 86400000,
        open: close, high: close, low: close, close, volume: 1000, amount: 10000 };
    });
    runtime = await createSectorKlineRuntime({ container: host, bars, mode, visibleCount: 60 });
    const chart = initSpy.mock.results[0]!.value as klinecharts.Chart;
    await vi.waitFor(() => {
      expect(chart.getIndicators({ name: SYSTEM_MACD_NAME })[0]?.result).toHaveLength(closes.length);
    });
    const indicator = chart.getIndicators({ name: SYSTEM_MACD_NAME })[0]!;
    return chart.getYAxes({ paneId: indicator.paneId })[0]!;
  }

  it.each(["compact", "expanded"] as const)("%s 模式不让历史极值压扁近期小幅波动，并随窗口重新缩放", async (mode) => {
    // 早期大幅波动，近期只有几分钱的变化；近期 EMA 已充分消化历史冲击。
    const closes = Array.from({ length: 360 }, (_, index) =>
      index < 40 ? 100 + (index % 2) * 200 : 10 + Math.sin(index / 5) * 0.03);
    const axis = await createChart(mode, closes);
    await vi.waitFor(() => {
      expect(axis.getRange().range).toBeGreaterThan(0);
      expect(axis.getRange().range).toBeLessThan(0.2);
    });

    runtime!.setVisibleCount(360);
    await vi.waitFor(() => expect(axis.getRange().range).toBeGreaterThan(10));
    runtime!.setVisibleCount(60);
    await vi.waitFor(() => expect(axis.getRange().range).toBeLessThan(0.2));
    expect(axis.getRange().from).toBeLessThanOrEqual(0);
    expect(axis.getRange().to).toBeGreaterThanOrEqual(0);
  });

  it("完全横盘时仍有有限且可用的纵轴范围", async () => {
    const axis = await createChart("compact", Array(120).fill(10));
    await vi.waitFor(() => {
      const range = axis.getRange();
      expect(range.from).toBeLessThan(0);
      expect(range.to).toBeGreaterThan(0);
      expect(range.range).toBeGreaterThan(0);
      expect(range.range).toBeLessThan(0.01);
    });
  });
});
