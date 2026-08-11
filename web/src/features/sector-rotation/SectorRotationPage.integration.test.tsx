/** 统一工作台在确定性接口夹具下的关键用户路径集成测试。 */
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { afterEach, vi } from "vitest";

vi.mock("./useRotationData", () => ({
  useRotationData: (_level: 1 | 2, _modelVersion: string, selectedDate?: string) => ({
    // mock 也按真实 Hook 的优先级返回历史单日所选日期，防止测试错误地始终拿最新日。
    latestDate: selectedDate ?? "2026-08-04",
    dates: { data: ["2026-08-04", "2026-08-03"], isLoading: false, isError: false },
    snapshot: {
      data: {
        as_of_date: selectedDate ?? "2026-08-04",
        sector_level: 2,
        model_version: "v1",
        meta: { run_status: "succeeded", field_version: "v1", source_max_trade_date: "2026-08-04" },
        sectors: [
          { as_of_date: "2026-08-04", sector_name: "半导体", score_eligible: true, velocity_score: 0.6, acceleration_score: 0.8, volume_score: 0.4, participation_score: 0.5, phase_confirmed: "decel_up", phase_confidence: 0.9, composite_rank: 1, composite_score: 0.88, rank_change_1d: 9, rank_change_5d: 21, coverage_ratio: 0.97, phase_changed: 1, lifecycle_state: "crowded", lifecycle_changed: true },
          { as_of_date: "2026-08-04", sector_name: "银行", score_eligible: true, velocity_score: 0.4, acceleration_score: 0.2, volume_score: 0.4, participation_score: 0.5, phase_confirmed: "decel_up", phase_confidence: 0.9, composite_rank: 2, composite_score: 0.78, rank_change_1d: 4, rank_change_5d: 10, coverage_ratio: 0.97, phase_changed: 0, lifecycle_state: "exit", lifecycle_changed: false },
          { as_of_date: "2026-08-04", sector_name: "教育", score_eligible: true, velocity_score: 0.2, acceleration_score: 0.6, volume_score: 0.4, participation_score: 0.5, phase_confirmed: "accel_up", phase_confidence: 0.9, composite_rank: 3, composite_score: 0.68, rank_change_1d: 1, rank_change_5d: 5, coverage_ratio: 0.97, phase_changed: 1, lifecycle_state: "trending", lifecycle_changed: true },
        ],
      },
      isLoading: false,
      isError: false,
    },
  }),
}));

vi.mock("./useReplayData", () => ({
  useReplayData: () => ({
    data: [
      { as_of_date: "2026-08-03", sector_name: "半导体", score_eligible: true, velocity_score: -0.2, acceleration_score: 0.5, volume_score: 0.2, participation_score: 0.3, phase_confirmed: "reversal_confirmed", phase_confidence: 0.7, composite_rank: 3, composite_score: 0.66, rank_change_1d: 4, rank_change_5d: 12, coverage_ratio: 0.94 },
      { as_of_date: "2026-08-04", sector_name: "教育", score_eligible: true, velocity_score: 0.6, acceleration_score: 0.8, volume_score: 0.4, participation_score: 0.5, phase_confirmed: "accel_up", phase_confidence: 0.9, composite_rank: 1, composite_score: 0.88, rank_change_1d: 9, rank_change_5d: 21, coverage_ratio: 0.97, phase_changed: 1 },
    ],
    isLoading: false,
    isError: false,
  }),
}));

vi.mock("./useHistoryData", () => ({
  useHistoryData: () => ({ data: [{ as_of_date: "2026-08-04", sector_name: "教育", velocity_score: 0.6, acceleration_score: 0.8 }], isLoading: false, isError: false }),
}));

vi.mock("./detail/SectorDetailDrawer", () => ({
  SectorDetailDrawer: ({ asOfDate, level, isLatestDate }: { asOfDate: string; level: number; isLatestDate: boolean }) => <div data-testid="drawer-date">{asOfDate}|{level}|{String(isLatestDate)}</div>,
}));

vi.mock("./chart/LazyQuadrantChart", () => ({
  LazyQuadrantChart: ({ sectors, trail, onSelect }: { sectors: { sector_name: string }[]; trail: unknown[]; onSelect: (name: string) => void }) => <div data-testid="quadrant"><span>当前图表：{sectors.map((sector) => sector.sector_name).join("、")}</span><span>尾迹点：{trail.length}</span><button type="button" onClick={() => onSelect(sectors[0].sector_name)}>图中选择 {sectors[0].sector_name}</button></div>,
}));

vi.mock("./history/LazySectorTrajectory", () => ({ LazySectorTrajectory: ({ trajectories }: { trajectories: { sector_name: string }[] }) => <div data-testid="trajectory">轨迹对比：{trajectories.map((item) => item.sector_name).join("、")}</div> }));

import { SectorRotationPage } from "./SectorRotationPage";

describe("SectorRotationPage 统一工作台", () => {
  afterEach(() => {
    // 每个用例都还原 URL，避免历史日期参数污染后续工作台初始化。
    window.history.replaceState(null, "", "/");
  });

  it("只保留一个主象限，并让回放帧、选择尾迹和轨迹分析同步", async () => {
    render(<SectorRotationPage />);

    expect(screen.getAllByTestId("quadrant")).toHaveLength(1);
    expect(screen.getByText("当前图表：半导体、银行、教育")).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: "图中选择 半导体" }));
    expect(await screen.findByText("轨迹对比：半导体")).toBeInTheDocument();

    fireEvent.click(screen.getByRole("button", { name: /动态回放/ }));
    expect(await screen.findByLabelText("全市场回放控制")).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: "上一帧" }));

    await waitFor(() => expect(screen.getByText("当前图表：半导体")).toBeInTheDocument());
    expect(screen.getByText("尾迹点：1")).toBeInTheDocument();
    expect(screen.getAllByTestId("quadrant")).toHaveLength(1);
  });

  it("向已打开抽屉传递历史单日日期，并在回放帧切换时同步更新", async () => {
    // 单日观察明确选择不同于最新日期的历史快照，验证不会被 2026-08-04 覆盖。
    window.history.replaceState(null, "", "/?sector=教育&date=2026-08-03");
    render(<SectorRotationPage />);

    expect(screen.getByTestId("drawer-date")).toHaveTextContent("2026-08-03|2|false");
    fireEvent.click(screen.getByRole("button", { name: /动态回放/ }));
    await waitFor(() => expect(screen.getByTestId("drawer-date")).toHaveTextContent("2026-08-03|2|false"));
    fireEvent.click(await screen.findByRole("button", { name: "下一帧" }));
    await waitFor(() => expect(screen.getByTestId("drawer-date")).toHaveTextContent("2026-08-04|2|true"));
  });

  it("Phase、Lifecycle、搜索和今日变化共同过滤图表与排名", async () => {
    window.history.replaceState(null, "", "/?phase=decel_up&lifecycle=risk&changed=1&q=半导体");
    render(<SectorRotationPage />);

    expect(await screen.findByText("当前图表：半导体")).toBeInTheDocument();
    expect(screen.queryByText("当前图表：银行")).not.toBeInTheDocument();
  });
});
