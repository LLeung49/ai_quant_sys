/** 短期异动模块的单元测试。*/

import { fireEvent, render, screen, waitFor, within } from "@testing-library/react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

const mockSnapshot = vi.hoisted(() => ({
  sectors: [
    { sector_name: "半导体", score_eligible: true, short_term_composite: 0.82, short_term_composite_rank: 1, short_term_labels: "pulse_up,volume_spike", short_term_intensity: "intense" },
    { sector_name: "银行", score_eligible: true, short_term_composite: 0.21, short_term_composite_rank: 2, short_term_labels: "limit_cluster", short_term_intensity: "mild" },
    { sector_name: "教育", score_eligible: false, short_term_composite: null, short_term_composite_rank: null, short_term_labels: "", short_term_intensity: "none" },
  ],
  meta: { run_status: "succeeded", field_version: "v2_short_term", source_max_trade_date: "2026-08-11", eligible_sector_count: 30, skipped_sector_count: 5, pulse_up_count: 3, volume_spike_count: 2, limit_cluster_count: 1, limit_panic_count: 0 },
}));

const mockV1Snapshot = vi.hoisted(() => ({
  sectors: [
    { sector_name: "半导体", score_eligible: true, phase_confirmed: "accel_up", phase_age: 4, phase_confidence: 0.72, composite_rank: 1, rank_change_1d: 2, coverage_ratio: 0.96, trend_level_score: 0.4, velocity_score: 0.5, acceleration_score: 0.3, participation_score: 0.4, volume_score: 0.2, lifecycle_state: "trending" },
    { sector_name: "银行", score_eligible: true, phase_confirmed: "neutral", phase_age: null, phase_confidence: 0.4, composite_rank: 10, rank_change_1d: -1, coverage_ratio: 0.9, trend_level_score: -0.1, velocity_score: 0.0, acceleration_score: 0.0, participation_score: 0.3, volume_score: -0.1, lifecycle_state: "neutral" },
  ],
}));

vi.mock("./api", () => ({
  fetchShortTermAvailableDates: vi.fn().mockResolvedValue({ sector_level: 2, model_version: "v2_short_term", dates: ["2026-08-11", "2026-08-10"] }),
  fetchShortTermSnapshot: vi.fn().mockImplementation(() => Promise.resolve(mockSnapshot)),
  SHORT_TERM_LABEL_WHITELIST: ["pulse_up", "pulse_down", "volume_spike", "limit_cluster", "limit_panic", "extreme_up", "extreme_down", "short_rebound_candidate", "short_breakdown_candidate"],
}));

vi.mock("../api", async () => {
  const actual = await vi.importActual("../api");
  return {
    ...actual,
    fetchAvailableDates: vi.fn().mockResolvedValue(["2026-08-11", "2026-08-10"]),
    fetchSnapshot: vi.fn().mockResolvedValue(mockV1Snapshot),
  };
});

import { ShortTermAnomalyModule } from "./ShortTermAnomalyModule";

function renderWithQueryClient(ui: React.ReactElement) {
  const queryClient = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  return render(<QueryClientProvider client={queryClient}>{ui}</QueryClientProvider>);
}

describe("ShortTermAnomalyModule", () => {
  beforeEach(() => {
    mockSnapshot.sectors = [
      { sector_name: "半导体", score_eligible: true, short_term_composite: 0.82, short_term_composite_rank: 1, short_term_labels: "pulse_up,volume_spike", short_term_intensity: "intense" },
      { sector_name: "银行", score_eligible: true, short_term_composite: 0.21, short_term_composite_rank: 2, short_term_labels: "limit_cluster", short_term_intensity: "mild" },
      { sector_name: "教育", score_eligible: false, short_term_composite: null, short_term_composite_rank: null, short_term_labels: "", short_term_intensity: "none" },
    ];
    mockSnapshot.meta = { run_status: "succeeded", field_version: "v2_short_term", source_max_trade_date: "2026-08-11", eligible_sector_count: 30, skipped_sector_count: 5, pulse_up_count: 3, volume_spike_count: 2, limit_cluster_count: 1, limit_panic_count: 0 };
  });

  afterEach(() => {
    vi.clearAllMocks();
  });

  it("以 2x2 网格展示 KPI", async () => {
    renderWithQueryClient(<ShortTermAnomalyModule level={2} asOfDate="2026-08-11" availableDates={["2026-08-11"]} />);

    expect(await screen.findByLabelText("短期异动 KPI")).toBeInTheDocument();
    const kpi = screen.getByLabelText("短期异动 KPI");
    expect(kpi).toHaveAttribute("data-layout", "grid");
    // pulse_up_count = 3，应渲染在 KPI 中。
    await waitFor(() => expect(screen.getByText("3")).toBeInTheDocument());
  });

  it("在 KPI 之后渲染次日研究观察候选面板", async () => {
    renderWithQueryClient(<ShortTermAnomalyModule level={2} asOfDate="2026-08-11" availableDates={["2026-08-11"]} />);

    expect(await screen.findByLabelText("次日研究观察候选")).toBeInTheDocument();

    // 半导体 pulse_up + volume_spike 应进入"强势跟进观察"卡。
    const strengthCard = await screen.findByRole("article", { name: "强势跟进观察研究观察候选" });
    // 等候选按钮出现（说明快照数据已加载）。
    expect(await within(strengthCard).findByRole("button", { name: "查看 半导体 短期异动详情" })).toBeInTheDocument();
  });

  it("标签筛选不影响候选面板，仍基于完整快照展示", async () => {
    // 准备含四类候选的快照。
    mockSnapshot.sectors = [
      { sector_name: "半导体", score_eligible: true, short_term_composite: 0.91, short_term_composite_rank: 1, short_term_labels: "pulse_up,volume_spike", short_term_intensity: "intense" },
      { sector_name: "新能源", score_eligible: true, short_term_composite: 0.7, short_term_composite_rank: 2, short_term_labels: "pulse_up,volume_spike", short_term_intensity: "moderate" },
      { sector_name: "煤炭", score_eligible: true, short_term_composite: -0.55, short_term_composite_rank: 11, short_term_labels: "pulse_down,volume_spike", short_term_intensity: "intense" },
      { sector_name: "软件", score_eligible: true, short_term_composite: 0.12, short_term_composite_rank: 12, short_term_labels: "short_rebound_candidate", short_term_intensity: "mild" },
      { sector_name: "建材", score_eligible: true, short_term_composite: -0.18, short_term_composite_rank: 13, short_term_labels: "short_breakdown_candidate", short_term_intensity: "mild" },
    ];

    renderWithQueryClient(<ShortTermAnomalyModule level={2} asOfDate="2026-08-11" availableDates={["2026-08-11"]} />);

    await screen.findByLabelText("次日研究观察候选");

    // 等候数据加载完成。
    const strengthCard = await screen.findByRole("article", { name: "强势跟进观察研究观察候选" });
    expect(await within(strengthCard).findByRole("button", { name: "查看 半导体 短期异动详情" })).toBeInTheDocument();
    expect(await within(strengthCard).findByRole("button", { name: "查看 新能源 短期异动详情" })).toBeInTheDocument();

    const panicCard = await screen.findByRole("article", { name: "恐慌修复观察研究观察候选" });
    expect(await within(panicCard).findByRole("button", { name: "查看 煤炭 短期异动详情" })).toBeInTheDocument();

    // 切换到 pulse_down 筛选，候选面板应保持不变（仍含半导体、新能源、煤炭）。
    const select = screen.getByLabelText("短期异动标签") as HTMLSelectElement;
    fireEvent.change(select, { target: { value: "pulse_down" } });

    // 等候过滤重新计算。
    await waitFor(() => {
      expect(within(strengthCard).getByRole("button", { name: "查看 半导体 短期异动详情" })).toBeInTheDocument();
    });
    expect(within(strengthCard).getByRole("button", { name: "查看 新能源 短期异动详情" })).toBeInTheDocument();
    expect(within(panicCard).getByRole("button", { name: "查看 煤炭 短期异动详情" })).toBeInTheDocument();
  });

  it("点击候选面板中的板块按钮打开统一详情抽屉并同步 onSectorSelect", async () => {
    const handler = vi.fn();
    renderWithQueryClient(
      <ShortTermAnomalyModule level={2} asOfDate="2026-08-11" availableDates={["2026-08-11"]} onSectorSelect={handler} />,
    );

    await screen.findByLabelText("次日研究观察候选");

    const candidateBtn = await screen.findByRole("button", { name: "查看 半导体 短期异动详情" });
    fireEvent.click(candidateBtn);
    expect(handler).toHaveBeenCalledWith("半导体");
    // 新版统一抽屉 aria-label 为 "{行业} 详情"
    // 新版统一详情抽屉是 <aside aria-label="{行业} 详情">,通过 aria-label 查询。
    expect(await screen.findByLabelText("半导体 详情")).toBeInTheDocument();
  });
});
