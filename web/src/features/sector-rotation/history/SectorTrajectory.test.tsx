/** 历史轨迹 ECharts 组件生命周期测试。 */
import { act, render } from "@testing-library/react";
import { vi } from "vitest";
const setOption = vi.fn(); const dispose = vi.fn();
vi.mock("../chart/echarts", () => ({ echarts: { init: vi.fn(() => ({ setOption, dispose, resize: vi.fn() })) } }));
import { SectorTrajectory } from "./SectorTrajectory";

describe("SectorTrajectory", () => {
  it("挂载历史轨迹并在卸载时释放图表", () => {
    let width = 0; let height = 0; let callback: ResizeObserverCallback = () => undefined;
    vi.spyOn(HTMLElement.prototype, "clientWidth", "get").mockImplementation(() => width);
    vi.spyOn(HTMLElement.prototype, "clientHeight", "get").mockImplementation(() => height);
    vi.stubGlobal("ResizeObserver", class {
      constructor(next: ResizeObserverCallback) { callback = next; }
      observe() { /* 由测试手动触发。 */ }
      disconnect() { /* 卸载结果由 dispose 断言覆盖。 */ }
    });
    const { unmount } = render(<SectorTrajectory trajectories={[{ sector_name: "半导体", points: [{ as_of_date: "2026-08-04", velocity_score: 0.2, acceleration_score: 0.3 }] }]} />);
    expect(setOption).not.toHaveBeenCalled();
    width = 900; height = 440;
    act(() => callback([], {} as ResizeObserver));
    expect(setOption).toHaveBeenCalledOnce(); unmount(); expect(dispose).toHaveBeenCalledOnce();
  });
});
