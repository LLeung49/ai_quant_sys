/** 多行业轨迹对比控制测试。 */
import { fireEvent, render, screen } from "@testing-library/react";
import { TrajectoryControls } from "./TrajectoryControls";

describe("TrajectoryControls", () => {
  it("展示五个行业、稳定色标和已满提示，并允许移除其中一个", () => {
    const onRemove = vi.fn();
    render(<TrajectoryControls sectorNames={["教育", "软件开发", "贵金属", "证券", "半导体"]} onRemove={onRemove} />);
    expect(screen.getAllByRole("button")).toHaveLength(5);
    expect(screen.getByText("已选择 5/5 个行业")).toBeInTheDocument();
    expect(screen.getByLabelText("移除 半导体").querySelector("i")).toHaveStyle({ background: "#a98bff" });
    fireEvent.click(screen.getByRole("button", { name: "移除 软件开发" }));
    expect(onRemove).toHaveBeenCalledWith("软件开发");
  });
});
