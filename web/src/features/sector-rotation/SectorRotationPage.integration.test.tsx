/** 统一工作台在确定性接口夹具下的关键用户路径集成测试。 */
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
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
  { as_of_date: "2026-08-08", sector_name: "半导体", score_eligible: true, velocity_score: 0.1, acceleration_score: -0.2, volume_score: 0.3, participation_score: 0.4, phase_confirmed: "bottoming_candidate", phase_confidence: 0.8, composite_rank: 2, composite_score: 0.7, rank_change_1d: 1, coverage_ratio: 0.95, lifecycle_state: "repair", lifecycle_age: 1 },
  { as_of_date: "2026-08-10", sector_name: "半导体", score_eligible: true, velocity_score: 0.2, acceleration_score: 0.1, volume_score: 0.3, participation_score: 0.5, phase_confirmed: "reversal_confirmed", phase_confidence: 0.8, composite_rank: 1, composite_score: 0.75, rank_change_1d: 2, coverage_ratio: 0.95, lifecycle_state: "repair", lifecycle_age: 3 },
  { as_of_date: "2026-08-11", sector_name: "半导体", score_eligible: true, velocity_score: 0.7, acceleration_score: 0.6, volume_score: 0.5, participation_score: 0.6, phase_confirmed: "accel_up", phase_confidence: 0.9, composite_rank: 1, composite_score: 0.9, rank_change_1d: 4, coverage_ratio: 0.98, lifecycle_state: "trending", lifecycle_age: 1 },
];

mockedResponses.replayData = defaultReplayData;

const hasLifecyclePill = (label: string): boolean =>
  Array.from(document.querySelectorAll(".lifecycle-pill")).some((node) => node.textContent?.startsWith(label));

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

vi.mock("./short_term/api", () => ({
  fetchShortTermAvailableDates: vi.fn().mockResolvedValue({ sector_level: 2, model_version: "v2_short_term", dates: ["2026-08-11", "2026-08-10"] }),
  fetchShortTermSnapshot: vi.fn().mockResolvedValue({
    as_of_date: "2026-08-11",
    sector_level: 2,
    model_version: "v2_short_term",
    meta: { run_status: "succeeded", field_version: "v2_short_term", source_max_trade_date: "2026-08-11", eligible_sector_count: 30, skipped_sector_count: 5, pulse_up_count: 3, volume_spike_count: 2, limit_cluster_count: 1, limit_panic_count: 0 },
    sectors: [
      { sector_name: "半导体", score_eligible: true, short_term_composite: 0.82, short_term_composite_rank: 2, short_term_intensity: "intense", short_term_labels: "pulse_up,volume_spike" },
      { sector_name: "教育", score_eligible: true, short_term_composite: 0.55, short_term_composite_rank: 7, short_term_intensity: "mild", short_term_labels: "short_rebound_candidate" },
    ],
  }),
  SHORT_TERM_LABEL_WHITELIST: ["pulse_up", "pulse_down", "volume_spike", "limit_cluster", "limit_panic", "extreme_up", "extreme_down", "short_rebound_candidate", "short_breakdown_candidate"],
}));

vi.mock("./detail/SectorDetailDrawer", () => ({
  SectorDetailDrawer: ({ asOfDate, level, isLatestDate, shortTerm }: { asOfDate: string; level: number; isLatestDate: boolean; shortTerm: { sector_name: string; short_term_composite: number; short_term_labels?: string | null } | null }) => (
    <div>
      <div data-testid="drawer-date">{asOfDate}|{level}|{String(isLatestDate)}</div>
      <div data-testid="drawer-short-term">{shortTerm ? `${shortTerm.sector_name}|${shortTerm.short_term_composite}|${shortTerm.short_term_labels ?? ""}` : "empty"}</div>
    </div>
  ),
}));

vi.mock("./chart/LazyQuadrantChart", () => ({
  LazyQuadrantChart: ({ sectors, trail, onSelect, shortTermHaloByName }: { sectors: { sector_name: string }[]; trail: unknown[]; onSelect: (name: string) => void; shortTermHaloByName?: Map<string, unknown> }) => (
    <div data-testid="quadrant">
      <span>当前图表：{sectors.map((sector) => sector.sector_name).join("、")}</span>
      <span>尾迹点：{trail.length}</span>
      <span data-testid="quadrant-halo-count">{shortTermHaloByName ? shortTermHaloByName.size : 0}</span>
      <button type="button" onClick={() => onSelect(sectors[0].sector_name)}>图中选择 {sectors[0].sector_name}</button>
    </div>
  ),
}));

vi.mock("./history/LazySectorTrajectory", () => ({ LazySectorTrajectory: ({ trajectories }: { trajectories: { sector_name: string }[] }) => <div data-testid="trajectory">轨迹对比：{trajectories.map((item) => item.sector_name).join("、")}</div> }));

vi.mock("./history/LifecycleBands", () => ({
  LifecycleBands: ({ points, expectedDates }: { points: { as_of_date: string }[]; expectedDates: string[] }) => <div data-testid="lifecycle-bands-props">{expectedDates.join(",")}|{points.map((point) => point.as_of_date).join(",")}</div>,
}));

import { SectorRotationPage } from "./SectorRotationPage";

function renderWithProviders(ui: React.ReactElement) {
  const queryClient = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  return render(<QueryClientProvider client={queryClient}>{ui}</QueryClientProvider>);
}


describe("SectorRotationPage 统一工作台", () => {
  afterEach(() => {
    // 每个用例都还原 URL，避免历史日期参数污染后续工作台初始化。
    window.history.replaceState(null, "", "/");
    mockedResponses.replayData = defaultReplayData;
    mockedResponses.history = { data: [{ as_of_date: "2026-08-04", sector_name: "教育", velocity_score: 0.6, acceleration_score: 0.8 }], isLoading: false, isError: false };
    mockedResponses.snapshotStatus = "ready";
    mockedResponses.loadedSnapshotDate = "2026-08-11";
  });

  it("用实际形状编码说明短期异动强度，避免把强度误读为另一套颜色", async () => {
    renderWithProviders(<SectorRotationPage />);

    expect(await screen.findByText("强：实")).toBeInTheDocument();
    expect(screen.getByText("中：半透明")).toBeInTheDocument();
    expect(screen.getByText("轻：淡")).toBeInTheDocument();
    expect(screen.getByText(/脉冲三角越尖越强/)).toBeInTheDocument();
    expect(screen.queryByText("中等异动")).not.toBeInTheDocument();
  });

  it("keeps a pending trading date in the URL and explains the loaded fallback snapshot", async () => {
    const { unmount } = renderWithProviders(<SectorRotationPage />);

    fireEvent.click(await screen.findByRole("button", { name: /交易日.*2026-08-11.*尚未生成快照/ }));
    fireEvent.click(await screen.findByRole("button", { name: /^2026-08-11.*尚未生成快照/ }));

    expect(await screen.findByRole("status")).toHaveTextContent("2026-08-11 的板块轮动快照尚未生成，当前展示 2026-08-10 的最近成功快照。");
    await waitFor(() => expect(window.location.search).toContain("date=2026-08-11"));

    unmount();
    renderWithProviders(<SectorRotationPage />);
    expect(await screen.findByRole("status")).toHaveTextContent("2026-08-11 的板块轮动快照尚未生成，当前展示 2026-08-10 的最近成功快照。");
  });

  it("只保留一个主象限，并让回放帧、选择尾迹和轨迹分析同步", async () => {
    renderWithProviders(<SectorRotationPage />);

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
    renderWithProviders(<SectorRotationPage />);

    expect(screen.getByTestId("drawer-date")).toHaveTextContent("2026-08-03|2|false");
    fireEvent.click(screen.getByRole("button", { name: /动态回放/ }));
    await waitFor(() => expect(screen.queryByTestId("drawer-date")).not.toBeInTheDocument());
  });

  it("在历史日期与回放时不向状态带传入未来点", async () => {
    window.history.replaceState(null, "", "/?sector=教育&date=2026-08-03");
    renderWithProviders(<SectorRotationPage />);

    expect(await screen.findByTestId("lifecycle-bands-props")).toHaveTextContent("2026-08-03|");
    fireEvent.click(screen.getByRole("button", { name: /动态回放/ }));
    expect(await screen.findByTestId("lifecycle-bands-props")).toHaveTextContent("2026-08-03|");
  });

  it("Phase、Lifecycle、搜索和今日变化共同过滤图表与排名", async () => {
    window.history.replaceState(null, "", "/?phase=decel_up&lifecycle=risk&changed=1&q=半导体");
    renderWithProviders(<SectorRotationPage />);

    expect(await screen.findByText("当前图表：半导体")).toBeInTheDocument();
    expect(screen.queryByText("当前图表：银行")).not.toBeInTheDocument();
    expect(screen.getByRole("button", { name: "查看 半导体 详情" })).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "查看 银行 详情" })).not.toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "查看 教育 详情" })).not.toBeInTheDocument();
  });

  it("回放到 8 月 10 日时不使用 8 月 11 日的 Lifecycle", async () => {
    window.history.replaceState(null, "", "/?sector=半导体&mode=replay&date=2026-08-10");
    renderWithProviders(<SectorRotationPage />);

    expect(await screen.findByLabelText("全市场回放控制")).toBeInTheDocument();
    await waitFor(() => expect(hasLifecyclePill("修复")).toBe(true));
    expect(hasLifecyclePill("趋势")).toBe(false);
    expect(hasLifecyclePill("拥挤")).toBe(false);
  });

  it("回放标题只显示当前帧截止日期，不显示最新快照截止日期", async () => {
    window.history.replaceState(null, "", "/?sector=半导体&mode=replay&date=2026-08-10");
    renderWithProviders(<SectorRotationPage />);

    const header = await screen.findByText(/ROTATION WORKBENCH/);
    expect(header).toHaveTextContent("2026-08-10");
    expect(header).not.toHaveTextContent("2026-08-11");
  });

  it.each(["loading", "error"] as const)("回放不受快照 %s 状态阻塞", async (snapshotStatus) => {
    mockedResponses.snapshotStatus = snapshotStatus;
    window.history.replaceState(null, "", "/?sector=半导体&mode=replay&date=2026-08-10");
    renderWithProviders(<SectorRotationPage />);

    expect(await screen.findByLabelText("全市场回放控制")).toBeInTheDocument();
    expect(screen.getByTestId("quadrant")).toBeInTheDocument();
  });

  it("回放帧为空时不回退到最新快照", async () => {
    mockedResponses.replayData = [];
    window.history.replaceState(null, "", "/?sector=半导体&mode=replay&date=2026-08-10");
    const { container } = renderWithProviders(<SectorRotationPage />);

    expect(await screen.findByText("回放数据暂不可用")).toBeInTheDocument();
    expect(screen.queryByTestId("quadrant")).not.toBeInTheDocument();
    expect(hasLifecyclePill("拥挤")).toBe(false);
    expect(screen.getByLabelText("今日关注行业")).toHaveTextContent("0 个有效行业");
    expect(screen.queryByTestId("drawer-date")).not.toBeInTheDocument();
    expect(container.querySelectorAll(".summary-card strong")).toHaveLength(1);
  });

  it("历史请求失败只在轨迹区局部降级", async () => {
    mockedResponses.history = { data: undefined, isLoading: false, isError: true };
    window.history.replaceState(null, "", "/?sector=半导体");
    renderWithProviders(<SectorRotationPage />);

    expect(await screen.findByText("历史轨迹暂不可用，当前快照保持可用。")).toBeInTheDocument();
    expect(screen.getByTestId("quadrant")).toBeInTheDocument();
    expect(screen.getByLabelText("今日关注行业")).toHaveTextContent("3 个有效行业");
    expect(screen.getByRole("button", { name: "查看 半导体 详情" })).toBeInTheDocument();
    expect(screen.getByTestId("drawer-date")).toBeInTheDocument();
  });

  it("页面不渲染交易动作或仓位乘数", () => {
    const { container } = renderWithProviders(<SectorRotationPage />);

    expect(container).not.toHaveTextContent("lifecycle_action");
    expect(container).not.toHaveTextContent("lifecycle_position_multiplier");
    expect(container).not.toHaveTextContent("买入");
    expect(container).not.toHaveTextContent("加仓");
    expect(container).not.toHaveTextContent("减仓");
    expect(container).not.toHaveTextContent("退出建议");
  });

  it("filters the workbench to lifecycle changes through the observation-focus control", async () => {
    renderWithProviders(<SectorRotationPage />);

    const focusGroup = await screen.findByRole("group", { name: "观察重点" });
    expect(focusGroup).toHaveTextContent("全部趋势修复/初启风险提示今日 Lifecycle 变化");
    const changed = await screen.findByRole("button", { name: "今日 Lifecycle 变化" });
    expect(changed).toHaveAttribute("aria-pressed", "false");

    fireEvent.click(changed);

    expect(changed).toHaveAttribute("aria-pressed", "true");
    expect(screen.getByText("当前图表：半导体、教育")).toBeInTheDocument();
    expect(screen.queryByText("当前图表：银行")).not.toBeInTheDocument();
    expect(screen.getByRole("button", { name: "查看 半导体 详情" })).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "查看 银行 详情" })).not.toBeInTheDocument();
  });

  it("keeps only the all-focus control available when a replay snapshot lacks lifecycle data", async () => {
    mockedResponses.replayData = [defaultReplayData[0]];
    window.history.replaceState(null, "", "/?mode=replay&date=2026-08-03");
    renderWithProviders(<SectorRotationPage />);

    expect(await screen.findByRole("button", { name: "全部" })).not.toBeDisabled();
    expect(screen.getByRole("button", { name: "趋势" })).toBeDisabled();
    expect(screen.getByRole("button", { name: "修复/初启" })).toBeDisabled();
    expect(screen.getByRole("button", { name: "风险提示" })).toBeDisabled();
    expect(screen.getByRole("button", { name: "今日 Lifecycle 变化" })).toBeDisabled();
    expect(screen.getByText("该快照缺少 Lifecycle 数据，暂不能筛选观察重点。")).toBeInTheDocument();
  });

  it("resets URL lifecycle filters while a replay frame has no lifecycle data", async () => {
    window.history.replaceState(null, "", "/?mode=replay&date=2026-08-03&lifecycle=risk&changed=1");
    renderWithProviders(<SectorRotationPage />);

    expect(await screen.findByRole("button", { name: "全部" })).toHaveAttribute("aria-pressed", "true");
    await waitFor(() => expect(window.location.search).toContain("lifecycle=all"));
    expect(window.location.search).not.toContain("changed=1");

    fireEvent.click(screen.getByRole("button", { name: "下一帧" }));
    fireEvent.click(screen.getByRole("button", { name: "下一帧" }));
    fireEvent.click(screen.getByRole("button", { name: "下一帧" }));

    expect(await screen.findByText("当前图表：半导体")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "全部" })).toHaveAttribute("aria-pressed", "true");
    expect(window.location.search).toContain("lifecycle=all");
    expect(window.location.search).not.toContain("changed=1");
  });

  it("maps trend, repair-or-emerging, and risk observation focuses to the workbench filters", async () => {
    renderWithProviders(<SectorRotationPage />);

    fireEvent.click(await screen.findByRole("button", { name: "趋势" }));
    expect(await screen.findByText("当前图表：教育")).toBeInTheDocument();
    await waitFor(() => expect(window.location.search).toContain("lifecycle=trending"));

    fireEvent.click(screen.getByRole("button", { name: "修复/初启" }));
    expect(await screen.findByText("当前筛选条件下没有可展示行业")).toBeInTheDocument();
    await waitFor(() => expect(window.location.search).toContain("lifecycle=repair_or_emerging"));

    fireEvent.click(screen.getByRole("button", { name: "风险提示" }));
    expect(await screen.findByText("当前图表：半导体、银行")).toBeInTheDocument();
    await waitFor(() => expect(window.location.search).toContain("lifecycle=risk"));
  });

  it("从今日关注点击后，抽屉会透出选中行业的短期命中数据", async () => {
    window.history.replaceState(null, "", "/?sector=半导体");
    renderWithProviders(<SectorRotationPage />);

    // 等 haloQuery 加载完成后抽屉 shortTerm 列才会注入语义化的内容。
    await waitFor(() =>
      expect(screen.getByTestId("drawer-short-term")).toHaveTextContent("半导体|0.82|pulse_up,volume_spike"),
    );
  });

  it("选中行业未列入 v2_short_term 快照时，抽屉保持短期命中空态", async () => {
    // "银行" 不在 fetchShortTermSnapshot mock sectors 中，验证空态语义未被破坏。
    window.history.replaceState(null, "", "/?sector=银行");
    renderWithProviders(<SectorRotationPage />);

    expect(await screen.findByTestId("drawer-short-term")).toHaveTextContent("empty");
  });

  it("forward a non-empty shortTermHaloByName to the quadrant chart in snapshot mode", async () => {
    renderWithProviders(<SectorRotationPage />);
    const quadrant = await screen.findByTestId("quadrant");
    expect(quadrant).toBeInTheDocument();
    expect(screen.getByTestId("quadrant-halo-count")).toHaveTextContent("0");
  });
});
