/** 统一工作台在确定性接口夹具下的关键用户路径集成测试。 */
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { afterEach, vi } from "vitest";

const mockedResponses = vi.hoisted(() => ({
  replayData: [] as Record<string, unknown>[],
  history: { data: [] as Array<{ as_of_date: string; sector_name: string; velocity_score: number; acceleration_score: number }> | undefined, isLoading: false, isError: false },
  snapshotStatus: "ready" as "ready" | "loading" | "error",
  loadedSnapshotDate: "2026-08-11",
}));

const defaultReplayData = [
  { as_of_date: "2026-08-03", sector_name: "半导体", score_eligible: true, velocity_score: -0.2, acceleration_score: 0.5, volume_score: 0.2, participation_score: 0.3, phase_confirmed: "reversal_confirmed", phase_confidence: 0.7, composite_rank: 3, composite_score: 0.66, rank_change_1d: 4, rank_change_5d: 12, coverage_ratio: 0.94 },
  { as_of_date: "2026-08-04", sector_name: "教育", score_eligible: true, velocity_score: 0.6, acceleration_score: 0.8, volume_score: 0.4, participation_score: 0.5, phase_confirmed: "accel_up", phase_confidence: 0.9, composite_rank: 1, composite_score: 0.88, rank_change_1d: 9, rank_change_5d: 21, coverage_ratio: 0.97, phase_changed: 1 },
  { as_of_date: "2026-08-08", sector_name: "半导体", score_eligible: true, velocity_score: 0.1, acceleration_score: -0.2, volume_score: 0.3, participation_score: 0.4, phase_confirmed: "bottoming_candidate", phase_confidence: 0.8, composite_rank: 2, composite_score: 0.7, rank_change_1d: 1, coverage_ratio: 0.95, lifecycle_state: "repair" },
  { as_of_date: "2026-08-10", sector_name: "半导体", score_eligible: true, velocity_score: 0.2, acceleration_score: 0.1, volume_score: 0.3, participation_score: 0.5, phase_confirmed: "reversal_confirmed", phase_confidence: 0.8, composite_rank: 1, composite_score: 0.75, rank_change_1d: 2, coverage_ratio: 0.95, lifecycle_state: "repair" },
  { as_of_date: "2026-08-11", sector_name: "半导体", score_eligible: true, velocity_score: 0.7, acceleration_score: 0.6, volume_score: 0.5, participation_score: 0.6, phase_confirmed: "accel_up", phase_confidence: 0.9, composite_rank: 1, composite_score: 0.9, rank_change_1d: 4, coverage_ratio: 0.98, lifecycle_state: "trending" },
];

mockedResponses.replayData = defaultReplayData;

const isLifecyclePill = (label: string) => (_: string, node: Element | null): boolean =>
  Boolean(node?.classList.contains("lifecycle-pill") && node.textContent?.startsWith(label));

vi.mock("./useRotationData", () => ({
  useRotationData: (_level: 1 | 2, _modelVersion: string, selectedDate?: string) => ({
    loadedSnapshotDate: selectedDate === "2026-08-11" ? "2026-08-10" : selectedDate ?? mockedResponses.loadedSnapshotDate,
    latestDate: selectedDate ?? "2026-08-11",
    dates: { data: ["2026-08-11", "2026-08-10", "2026-08-04", "2026-08-03"], isLoading: false, isError: false },
    snapshot: {
      data: mockedResponses.snapshotStatus === "ready" ? {
        as_of_date: selectedDate === "2026-08-11" ? "2026-08-10" : selectedDate ?? mockedResponses.loadedSnapshotDate,
        sector_level: 2,
        model_version: "v1",
        meta: { run_status: "succeeded", field_version: "v1", source_max_trade_date: "2026-08-11" },
        sectors: [
          { as_of_date: "2026-08-04", sector_name: "半导体", score_eligible: true, velocity_score: 0.6, acceleration_score: 0.8, volume_score: 0.4, participation_score: 0.5, phase_confirmed: "decel_up", phase_confidence: 0.9, composite_rank: 1, composite_score: 0.88, rank_change_1d: 9, rank_change_5d: 21, coverage_ratio: 0.97, phase_changed: 1, lifecycle_state: "crowded", lifecycle_changed: true },
          { as_of_date: "2026-08-04", sector_name: "银行", score_eligible: true, velocity_score: 0.4, acceleration_score: 0.2, volume_score: 0.4, participation_score: 0.5, phase_confirmed: "decel_up", phase_confidence: 0.9, composite_rank: 2, composite_score: 0.78, rank_change_1d: 4, rank_change_5d: 10, coverage_ratio: 0.97, phase_changed: 0, lifecycle_state: "exit", lifecycle_changed: false },
          { as_of_date: "2026-08-04", sector_name: "教育", score_eligible: true, velocity_score: 0.2, acceleration_score: 0.6, volume_score: 0.4, participation_score: 0.5, phase_confirmed: "accel_up", phase_confidence: 0.9, composite_rank: 3, composite_score: 0.68, rank_change_1d: 1, rank_change_5d: 5, coverage_ratio: 0.97, phase_changed: 1, lifecycle_state: "trending", lifecycle_changed: true },
        ],
      } : undefined,
      isLoading: mockedResponses.snapshotStatus === "loading",
      isError: mockedResponses.snapshotStatus === "error",
    },
  }),
}));

vi.mock("./useCalendarAvailability", () => ({
  useCalendarAvailability: () => ({
    data: {
      sector_level: 2,
      model_version: "v1",
      trade_dates: ["2026-08-10", "2026-08-11"],
      snapshot_dates: ["2026-08-10"],
      latest_snapshot_date: "2026-08-10",
    },
    isError: false,
  }),
}));

vi.mock("./useReplayData", () => ({
  useReplayData: () => ({
    data: mockedResponses.replayData,
    isLoading: false,
    isError: false,
  }),
}));

vi.mock("./useHistoryData", () => ({
  useHistoryData: () => mockedResponses.history,
}));

vi.mock("./detail/SectorDetailDrawer", () => ({
  SectorDetailDrawer: ({ asOfDate, level, isLatestDate }: { asOfDate: string; level: number; isLatestDate: boolean }) => <div data-testid="drawer-date">{asOfDate}|{level}|{String(isLatestDate)}</div>,
}));

vi.mock("./chart/LazyQuadrantChart", () => ({
  LazyQuadrantChart: ({ sectors, trail, onSelect }: { sectors: { sector_name: string }[]; trail: unknown[]; onSelect: (name: string) => void }) => <div data-testid="quadrant"><span>当前图表：{sectors.map((sector) => sector.sector_name).join("、")}</span><span>尾迹点：{trail.length}</span><button type="button" onClick={() => onSelect(sectors[0].sector_name)}>图中选择 {sectors[0].sector_name}</button></div>,
}));

vi.mock("./history/LazySectorTrajectory", () => ({ LazySectorTrajectory: ({ trajectories }: { trajectories: { sector_name: string }[] }) => <div data-testid="trajectory">轨迹对比：{trajectories.map((item) => item.sector_name).join("、")}</div> }));

vi.mock("./history/LifecycleBands", () => ({
  LifecycleBands: ({ points, expectedDates }: { points: { as_of_date: string }[]; expectedDates: string[] }) => <div data-testid="lifecycle-bands-props">{expectedDates.join(",")}|{points.map((point) => point.as_of_date).join(",")}</div>,
}));

import { SectorRotationPage } from "./SectorRotationPage";

describe("SectorRotationPage 统一工作台", () => {
  afterEach(() => {
    // 每个用例都还原 URL，避免历史日期参数污染后续工作台初始化。
    window.history.replaceState(null, "", "/");
    mockedResponses.replayData = defaultReplayData;
    mockedResponses.history = { data: [{ as_of_date: "2026-08-04", sector_name: "教育", velocity_score: 0.6, acceleration_score: 0.8 }], isLoading: false, isError: false };
    mockedResponses.snapshotStatus = "ready";
    mockedResponses.loadedSnapshotDate = "2026-08-11";
  });

  it("keeps a pending trading date in the URL and explains the loaded fallback snapshot", async () => {
    const { unmount } = render(<SectorRotationPage />);

    fireEvent.click(await screen.findByRole("button", { name: /2026-08-11.*尚未生成快照/ }));

    expect(await screen.findByRole("status")).toHaveTextContent("2026-08-11 的板块轮动快照尚未生成，当前展示 2026-08-10 的最近成功快照。");
    await waitFor(() => expect(window.location.search).toContain("date=2026-08-11"));

    unmount();
    render(<SectorRotationPage />);
    expect(await screen.findByRole("status")).toHaveTextContent("2026-08-11 的板块轮动快照尚未生成，当前展示 2026-08-10 的最近成功快照。");
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
    expect(screen.getByText(/尾迹点：/)).toBeInTheDocument();
    expect(screen.getAllByTestId("quadrant")).toHaveLength(1);
  });

  it("回放帧没有已选行业时不使用最新快照打开抽屉", async () => {
    // 单日观察明确选择不同于最新日期的历史快照，验证不会被 2026-08-04 覆盖。
    window.history.replaceState(null, "", "/?sector=教育&date=2026-08-03");
    render(<SectorRotationPage />);

    expect(screen.getByTestId("drawer-date")).toHaveTextContent("2026-08-03|2|false");
    fireEvent.click(screen.getByRole("button", { name: /动态回放/ }));
    await waitFor(() => expect(screen.queryByTestId("drawer-date")).not.toBeInTheDocument());
  });

  it("在历史日期与回放时不向状态带传入未来点", async () => {
    window.history.replaceState(null, "", "/?sector=教育&date=2026-08-03");
    render(<SectorRotationPage />);

    expect(await screen.findByTestId("lifecycle-bands-props")).toHaveTextContent("2026-08-03|");
    fireEvent.click(screen.getByRole("button", { name: /动态回放/ }));
    expect(await screen.findByTestId("lifecycle-bands-props")).toHaveTextContent("2026-08-03|");
  });

  it("Phase、Lifecycle、搜索和今日变化共同过滤图表与排名", async () => {
    window.history.replaceState(null, "", "/?phase=decel_up&lifecycle=risk&changed=1&q=半导体");
    render(<SectorRotationPage />);

    expect(await screen.findByText("当前图表：半导体")).toBeInTheDocument();
    expect(screen.queryByText("当前图表：银行")).not.toBeInTheDocument();
    expect(screen.getByRole("button", { name: "查看 半导体 详情" })).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "查看 银行 详情" })).not.toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "查看 教育 详情" })).not.toBeInTheDocument();
  });

  it("回放到 8 月 10 日时不使用 8 月 11 日的 Lifecycle", async () => {
    window.history.replaceState(null, "", "/?sector=半导体&mode=replay&date=2026-08-10");
    render(<SectorRotationPage />);

    expect(await screen.findByLabelText("全市场回放控制")).toBeInTheDocument();
    expect(await screen.findByText(isLifecyclePill("修复观察"))).toBeInTheDocument();
    expect(screen.queryByText(isLifecyclePill("趋势运行"))).not.toBeInTheDocument();
    expect(screen.queryByText(isLifecyclePill("强势拥挤"))).not.toBeInTheDocument();
  });

  it("回放标题只显示当前帧截止日期，不显示最新快照截止日期", async () => {
    window.history.replaceState(null, "", "/?sector=半导体&mode=replay&date=2026-08-10");
    render(<SectorRotationPage />);

    const header = await screen.findByText(/ROTATION WORKBENCH/);
    expect(header).toHaveTextContent("2026-08-10");
    expect(header).not.toHaveTextContent("2026-08-11");
  });

  it.each(["loading", "error"] as const)("回放不受快照 %s 状态阻塞", async (snapshotStatus) => {
    mockedResponses.snapshotStatus = snapshotStatus;
    window.history.replaceState(null, "", "/?sector=半导体&mode=replay&date=2026-08-10");
    render(<SectorRotationPage />);

    expect(await screen.findByLabelText("全市场回放控制")).toBeInTheDocument();
    expect(screen.getByTestId("quadrant")).toBeInTheDocument();
  });

  it("回放帧为空时不回退到最新快照", async () => {
    mockedResponses.replayData = [];
    window.history.replaceState(null, "", "/?sector=半导体&mode=replay&date=2026-08-10");
    const { container } = render(<SectorRotationPage />);

    expect(await screen.findByText("回放数据暂不可用")).toBeInTheDocument();
    expect(screen.queryByTestId("quadrant")).not.toBeInTheDocument();
    expect(screen.queryByText(isLifecyclePill("强势拥挤"))).not.toBeInTheDocument();
    expect(screen.getByLabelText("今日关注行业")).toHaveTextContent("0 个有效行业");
    expect(screen.queryByTestId("drawer-date")).not.toBeInTheDocument();
    expect([...container.querySelectorAll(".summary-card strong")].slice(1).map((element) => element.textContent)).toEqual(["0", "0", "0", "0"]);
  });

  it("历史请求失败只在轨迹区局部降级", async () => {
    mockedResponses.history = { data: undefined, isLoading: false, isError: true };
    window.history.replaceState(null, "", "/?sector=半导体");
    render(<SectorRotationPage />);

    expect(await screen.findByText("历史轨迹暂不可用，当前快照保持可用。")).toBeInTheDocument();
    expect(screen.getByTestId("quadrant")).toBeInTheDocument();
    expect(screen.getByLabelText("今日关注行业")).toHaveTextContent("3 个有效行业");
    expect(screen.getByRole("button", { name: "查看 半导体 详情" })).toBeInTheDocument();
    expect(screen.getByTestId("drawer-date")).toBeInTheDocument();
  });

  it("页面不渲染交易动作或仓位乘数", () => {
    const { container } = render(<SectorRotationPage />);

    expect(container).not.toHaveTextContent("lifecycle_action");
    expect(container).not.toHaveTextContent("lifecycle_position_multiplier");
    expect(container).not.toHaveTextContent("买入");
    expect(container).not.toHaveTextContent("加仓");
    expect(container).not.toHaveTextContent("减仓");
    expect(container).not.toHaveTextContent("退出建议");
  });
});
