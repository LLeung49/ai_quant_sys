/** 板块 K 线 React 容器的零尺寸保护、更新释放和局部失败降级测试。 */
import { StrictMode } from "react";
import { act, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import type { SectorKlineResponse } from "./sectorKlineApi";

const runtimeMocks = vi.hoisted(() => ({ createSectorKlineRuntime: vi.fn() }));
vi.mock("./klinechartRuntime", () => ({ createSectorKlineRuntime: runtimeMocks.createSectorKlineRuntime }));

import { SectorKlineChart } from "./SectorKlineChart";

const bars: SectorKlineResponse["bars"] = [
  { trade_date: "2026-08-04", timestamp: 1785772800000, open: 10, high: 11, low: 9, close: 10.5, volume: 1000, amount: 2000 },
];

/** 创建可由测试手动完成的 Promise，用于稳定复现异步初始化与 props 切换竞态。 */
function createDeferred<T>() {
  let resolve!: (value: T) => void;
  let reject!: (reason?: unknown) => void;
  const promise = new Promise<T>((onResolve, onReject) => {
    resolve = onResolve;
    reject = onReject;
  });
  return { promise, resolve, reject };
}

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

  it("旧异步初始化尚未完成时切换模式，最终仍会初始化最新输入并释放迟到实例", async () => {
    const firstAttempt = createDeferred<{ resize: () => void; setVisibleCount: () => void; dispose: () => void }>();
    const secondAttempt = createDeferred<{ resize: () => void; setVisibleCount: () => void; dispose: () => void }>();
    const staleRuntime = { resize: vi.fn(), setVisibleCount: vi.fn(), dispose: vi.fn() };
    const latestRuntime = { resize: vi.fn(), setVisibleCount: vi.fn(), dispose: vi.fn() };
    runtimeMocks.createSectorKlineRuntime.mockReturnValueOnce(firstAttempt.promise).mockReturnValueOnce(secondAttempt.promise);
    vi.spyOn(HTMLElement.prototype, "clientWidth", "get").mockReturnValue(960);
    vi.spyOn(HTMLElement.prototype, "clientHeight", "get").mockReturnValue(420);
    vi.stubGlobal("ResizeObserver", class {
      constructor(_callback: ResizeObserverCallback) { /* 首次 effect 会主动尝试初始化。 */ }
      observe() { /* 无需额外布局回调。 */ }
      disconnect() { /* effect cleanup 覆盖断开流程。 */ }
    });

    const { rerender } = render(<SectorKlineChart bars={bars} mode="compact" visibleCount={120} ariaLabel="半导体 K 线" />);
    await waitFor(() => expect(runtimeMocks.createSectorKlineRuntime).toHaveBeenCalledOnce());
    rerender(<SectorKlineChart bars={[...bars]} mode="expanded" visibleCount={60} ariaLabel="半导体 K 线" />);
    await waitFor(() => expect(runtimeMocks.createSectorKlineRuntime).toHaveBeenNthCalledWith(2, expect.objectContaining({ mode: "expanded", visibleCount: 60 })));

    await act(async () => { secondAttempt.resolve(latestRuntime); });
    await act(async () => { firstAttempt.resolve(staleRuntime); });
    await waitFor(() => expect(staleRuntime.dispose).toHaveBeenCalledOnce());
    expect(latestRuntime.setVisibleCount).toHaveBeenCalledWith(60);
  });

  it("StrictMode 双执行 effect 时，第二个生命周期仍能创建图表并释放首个迟到实例", async () => {
    const firstAttempt = createDeferred<{ resize: () => void; setVisibleCount: () => void; dispose: () => void }>();
    const secondAttempt = createDeferred<{ resize: () => void; setVisibleCount: () => void; dispose: () => void }>();
    const staleRuntime = { resize: vi.fn(), setVisibleCount: vi.fn(), dispose: vi.fn() };
    const currentRuntime = { resize: vi.fn(), setVisibleCount: vi.fn(), dispose: vi.fn() };
    runtimeMocks.createSectorKlineRuntime.mockReturnValueOnce(firstAttempt.promise).mockReturnValueOnce(secondAttempt.promise);
    vi.spyOn(HTMLElement.prototype, "clientWidth", "get").mockReturnValue(960);
    vi.spyOn(HTMLElement.prototype, "clientHeight", "get").mockReturnValue(420);
    vi.stubGlobal("ResizeObserver", class {
      constructor(_callback: ResizeObserverCallback) { /* effect 会主动初始化。 */ }
      observe() { /* 无需额外布局回调。 */ }
      disconnect() { /* StrictMode cleanup 覆盖断开流程。 */ }
    });

    render(<StrictMode><SectorKlineChart bars={bars} mode="compact" visibleCount={120} ariaLabel="半导体 K 线" /></StrictMode>);
    await waitFor(() => expect(runtimeMocks.createSectorKlineRuntime).toHaveBeenCalledTimes(2));
    await act(async () => { secondAttempt.resolve(currentRuntime); });
    await act(async () => { firstAttempt.resolve(staleRuntime); });

    await waitFor(() => expect(staleRuntime.dispose).toHaveBeenCalledOnce());
    expect(currentRuntime.setVisibleCount).toHaveBeenCalledWith(120);
  });

  it("初始化失败后保留容器，并在 bars 或模式变更时清错并重新初始化", async () => {
    const recoveredRuntime = { resize: vi.fn(), setVisibleCount: vi.fn(), dispose: vi.fn() };
    runtimeMocks.createSectorKlineRuntime.mockRejectedValueOnce(new Error("临时失败")).mockResolvedValueOnce(recoveredRuntime);
    vi.spyOn(HTMLElement.prototype, "clientWidth", "get").mockReturnValue(960);
    vi.spyOn(HTMLElement.prototype, "clientHeight", "get").mockReturnValue(420);
    vi.stubGlobal("ResizeObserver", class {
      constructor(_callback: ResizeObserverCallback) { /* 初次 effect 会主动尝试初始化。 */ }
      observe() { /* 无需额外布局回调。 */ }
      disconnect() { /* 无需额外行为。 */ }
    });

    const { rerender } = render(<SectorKlineChart bars={bars} mode="compact" visibleCount={120} ariaLabel="半导体 K 线" />);
    await waitFor(() => expect(screen.getByRole("alert")).toHaveTextContent("行情图初始化失败，请重试"));
    expect(screen.getByRole("img", { name: "半导体 K 线" })).toBeInTheDocument();
    rerender(<SectorKlineChart bars={[...bars]} mode="expanded" visibleCount={60} ariaLabel="半导体 K 线" />);

    await waitFor(() => expect(runtimeMocks.createSectorKlineRuntime).toHaveBeenCalledTimes(2));
    await waitFor(() => expect(screen.queryByRole("alert")).not.toBeInTheDocument());
    expect(recoveredRuntime.setVisibleCount).toHaveBeenCalledWith(60);
  });
});
