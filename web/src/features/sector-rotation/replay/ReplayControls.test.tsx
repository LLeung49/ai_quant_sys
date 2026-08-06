/** 回放控制器的可访问操作测试。 */
import { fireEvent, render, screen } from "@testing-library/react";
import { ReplayControls } from "./ReplayControls";

describe("ReplayControls", () => {
  it("回传播放和时间轴跳转操作", () => {
    const dispatch = vi.fn();
    render(<ReplayControls dates={["2026-08-01", "2026-08-04"]} index={0} playing={false} dispatch={dispatch} />);
    fireEvent.click(screen.getByRole("button", { name: "播放回放" }));
    fireEvent.change(screen.getByLabelText("回放日期时间轴"), { target: { value: "1" } });
    expect(dispatch).toHaveBeenNthCalledWith(1, { type: "PLAY" });
    expect(dispatch).toHaveBeenNthCalledWith(2, { type: "SEEK", index: 1 });
  });
});
