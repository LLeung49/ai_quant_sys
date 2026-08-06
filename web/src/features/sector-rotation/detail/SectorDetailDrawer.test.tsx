/** 板块详情抽屉的研究文案与关闭交互测试。 */
import { fireEvent, render, screen } from "@testing-library/react";
import { SectorDetailDrawer } from "./SectorDetailDrawer";

describe("SectorDetailDrawer", () => {
  it("展示加速走强的研究解释，并允许关闭详情", () => {
    const onClose = vi.fn();
    render(<SectorDetailDrawer sector={{ sector_name: "半导体", phase_confirmed: "accel_up", phase_age: 4, phase_confidence: 0.72, composite_rank: 1, rank_change_1d: 2, coverage_ratio: 0.96, trend_level_score: 0.4, velocity_score: 0.5, acceleration_score: 0.3, participation_score: 0.4, volume_score: 0.2 }} onClose={onClose} />);

    expect(screen.getByText("加速走强")).toBeInTheDocument();
    expect(screen.getByText(/相对强势与趋势加速同时出现/)).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: "关闭详情" }));
    expect(onClose).toHaveBeenCalledOnce();
  });
});
