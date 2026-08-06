/** 全市场回放视图的帧选择测试。 */
import { render, screen } from "@testing-library/react";
import { vi } from "vitest";
vi.mock("../chart/QuadrantChart", () => ({ QuadrantChart: () => <div>象限帧</div> }));
import { MarketReplay } from "./MarketReplay";

describe("MarketReplay", () => {
  it("展示首个已加载交易日和象限帧", () => {
    render(<MarketReplay points={[{ as_of_date: "2026-08-04", sector_name: "半导体", velocity_score: 0.2, acceleration_score: 0.3, volume_score: 0.1, participation_score: 0.2, phase_confirmed: "accel_up", phase_confidence: 0.7, composite_rank: 1 }]} />);
    expect(screen.getByText("2026-08-04")).toBeInTheDocument();
    expect(screen.getByText("象限帧")).toBeInTheDocument();
  });
});
