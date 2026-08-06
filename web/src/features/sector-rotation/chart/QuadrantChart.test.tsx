/** ECharts 象限图组件的生命周期测试。 */
import { act, render } from "@testing-library/react";
import { vi } from "vitest";

const setOption = vi.fn();
const dispose = vi.fn();
vi.mock("./echarts", () => ({ echarts: { init: vi.fn(() => ({ setOption, dispose, resize: vi.fn(), on: vi.fn() })) } }));

import { echarts } from "./echarts";
import { QuadrantChart } from "./QuadrantChart";

describe("QuadrantChart", () => {
  it("容器获得有效尺寸后才初始化图表，并在卸载时释放实例", () => {
    let width = 0;
    let height = 0;
    let observerCallback: ResizeObserverCallback = () => undefined;
    vi.spyOn(HTMLElement.prototype, "clientWidth", "get").mockImplementation(() => width);
    vi.spyOn(HTMLElement.prototype, "clientHeight", "get").mockImplementation(() => height);
    vi.stubGlobal("ResizeObserver", class {
      constructor(callback: ResizeObserverCallback) { observerCallback = callback; }
      observe() { /* 测试只需手动触发尺寸回调。 */ }
      disconnect() { /* 组件卸载行为由 ECharts dispose 断言覆盖。 */ }
    });

    const { unmount } = render(<QuadrantChart sectors={[{ sector_name: "半导体", velocity_score: 0.4, acceleration_score: 0.2, volume_score: 0.3, participation_score: 0.5, phase_confirmed: "accel_up", phase_confidence: 0.8, composite_rank: 1 }]} />);

    expect(echarts.init).not.toHaveBeenCalled();
    width = 900;
    height = 560;
    act(() => observerCallback([], {} as ResizeObserver));
    expect(echarts.init).toHaveBeenCalledOnce();
    expect(setOption).toHaveBeenCalledOnce();
    unmount();
    expect(dispose).toHaveBeenCalledOnce();
  });
});
