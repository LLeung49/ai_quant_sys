/** 板块 K 线 React 容器的零尺寸保护、更新释放和局部失败降级测试。 */
import { act, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import type { SectorKlineResponse } from "./sectorKlineApi";

const runtimeMocks = vi.hoisted(() => ({ createSectorKlineRuntime: vi.fn() }));
vi.mock("./klinechartRuntime", () => ({ createSectorKlineRuntime: runtimeMocks.createSectorKlineRuntime }));

import { SectorKlineChart } from "./SectorKlineChart";

const bars: SectorKlineResponse["bars"] = [
  { trade_date: "2026-08-04", timestamp: 1785772800000, open: 10, high: 11, low: 9, close: 10.5, volume: 1000, amount: 2000 },
];

describe("SectorKlineChart", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("零尺寸容器不初始化，获得有效尺寸后仅创建一次图表", async () => {
    let width = 0;
    let height = 0;
    let observerCallback: ResizeObserverCallback = () => undefined;
    const runtime = { resize: vi.fn(), setVisibleCount: vi.fn(), dispose: vi.fn() };
    runtimeMocks.createSectorKlineRuntime.mockResolvedValue(runtime);
    vi.spyOn(HTMLElement.prototype, "clientWidth", "get").mockImplementation(() => width);
    vi.spyOn(HTMLElement.prototype, "clientHeight", "get").mockImplementation(() => height);
    vi.stubGlobal("ResizeObserver", class {
      constructor(callback: ResizeObserverCallback) { observerCallback = callback; }
      observe() { /* 测试通过回调手动模拟布局完成。 */ }
      disconnect() { /* 卸载释放由运行时 dispose 断言覆盖。 */ }
    });

    const { unmount } = render(<SectorKlineChart bars={bars} mode="compact" visibleCount={120} ariaLabel="半导体 K 线" />);
    expect(runtimeMocks.createSectorKlineRuntime).not.toHaveBeenCalled();
    width = 960;
    height = 420;
    act(() => observerCallback([], {} as ResizeObserver));
    await waitFor(() => expect(runtimeMocks.createSectorKlineRuntime).toHaveBeenCalledOnce());
    act(() => observerCallback([], {} as ResizeObserver));
    expect(runtimeMocks.createSectorKlineRuntime).toHaveBeenCalledOnce();

    unmount();
    expect(runtime.dispose).toHaveBeenCalledOnce();
  });

  it("数据或模式变化前释放旧实例，并把运行时拒绝降级为局部提示", async () => {
    let observerCallback: ResizeObserverCallback = () => undefined;
    const firstRuntime = { resize: vi.fn(), setVisibleCount: vi.fn(), dispose: vi.fn() };
    runtimeMocks.createSectorKlineRuntime.mockResolvedValueOnce(firstRuntime).mockRejectedValueOnce(new Error("初始化失败"));
    vi.spyOn(HTMLElement.prototype, "clientWidth", "get").mockReturnValue(960);
    vi.spyOn(HTMLElement.prototype, "clientHeight", "get").mockReturnValue(420);
    vi.stubGlobal("ResizeObserver", class {
      constructor(callback: ResizeObserverCallback) { observerCallback = callback; }
      observe() { /* 初次 effect 会主动尝试初始化。 */ }
      disconnect() { /* 无需额外行为。 */ }
    });

    const { rerender } = render(<SectorKlineChart bars={bars} mode="compact" visibleCount={120} ariaLabel="半导体 K 线" />);
    await waitFor(() => expect(runtimeMocks.createSectorKlineRuntime).toHaveBeenCalledOnce());
    rerender(<SectorKlineChart bars={[...bars]} mode="expanded" visibleCount={60} ariaLabel="半导体 K 线" />);

    await waitFor(() => expect(firstRuntime.dispose).toHaveBeenCalledOnce());
    await waitFor(() => expect(screen.getByRole("alert")).toHaveTextContent("行情图初始化失败，请重试"));
    act(() => observerCallback([], {} as ResizeObserver));
    expect(runtimeMocks.createSectorKlineRuntime).toHaveBeenCalledTimes(2);
  });
});
