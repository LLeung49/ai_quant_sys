/** 短期异动模块的单元测试。 */
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
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

vi.mock("./api", () => ({
  fetchShortTermAvailableDates: vi.fn().mockResolvedValue({ sector_level: 2, model_version: "v2_short_term", dates: ["2026-08-11", "2026-08-10"] }),
  fetchShortTermSnapshot: vi.fn().mockImplementation(() => Promise.resolve(mockSnapshot)),
  SHORT_TERM_LABEL_WHITELIST: ["pulse_up", "pulse_down", "volume_spike", "limit_cluster", "limit_panic", "extreme_up", "extreme_down", "short_rebound_candidate", "short_breakdown_candidate"],
}));

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

  it("以 2x2 网格展示 KPI 并渲染异动榜", async () => {
    renderWithQueryClient(<ShortTermAnomalyModule level={2} asOfDate="2026-08-11" availableDates={["2026-08-11"]} />);

    expect(await screen.findByLabelText("短期异动 KPI")).toBeInTheDocument();
    const kpi = screen.getByLabelText("短期异动 KPI");
    expect(kpi).toHaveAttribute("data-layout", "grid");
    await waitFor(() => expect(screen.getByText("3")).toBeInTheDocument());

    await waitFor(() => expect(screen.getByRole("button", { name: "查看 半导体 详情" })).toBeInTheDocument());
    expect(screen.getByRole("button", { name: "查看 银行 详情" })).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "查看 教育 详情" })).not.toBeInTheDocument();
  });

  it("标签筛选仅保留命中标签的板块", async () => {
    renderWithQueryClient(<ShortTermAnomalyModule level={2} asOfDate="2026-08-11" availableDates={["2026-08-11"]} />);

    await waitFor(() => expect(screen.getByRole("button", { name: "查看 半导体 详情" })).toBeInTheDocument());

    const select = screen.getByLabelText("短期异动标签") as HTMLSelectElement;
    fireEvent.change(select, { target: { value: "limit_cluster" } });
    await waitFor(() => expect(screen.queryByRole("button", { name: "查看 半导体 详情" })).not.toBeInTheDocument());
    expect(screen.getByRole("button", { name: "查看 银行 详情" })).toBeInTheDocument();
  });

  it("点击异动项调用 onSectorSelect 并打开详情抽屉", async () => {
    const handler = vi.fn();
    renderWithQueryClient(<ShortTermAnomalyModule level={2} asOfDate="2026-08-11" availableDates={["2026-08-11"]} onSectorSelect={handler} />);

    const btn = await screen.findByRole("button", { name: "查看 半导体 详情" });
    fireEvent.click(btn);
    expect(handler).toHaveBeenCalledWith("半导体");
    expect(await screen.findByRole("dialog", { name: "半导体 短期异动详情" })).toBeInTheDocument();
  });
});
