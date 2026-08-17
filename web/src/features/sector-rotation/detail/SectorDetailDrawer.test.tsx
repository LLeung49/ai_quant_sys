/** 板块详情抽屉的研究文档与关闭交互测试。*/

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { vi } from "vitest";
import { SectorDetailDrawer } from "./SectorDetailDrawer";

vi.mock("../kline/SectorKlineCard", () => ({
  SectorKlineCard: ({ sectorName, level, asOfDate, onExpand }: { sectorName: string; level: number; asOfDate: string; onExpand: (data: unknown) => void }) => (
    <button data-testid="sector-kline-card" type="button" onClick={() => onExpand({})}>
      {sectorName}|{level}|{asOfDate}
    </button>
  ),
}));
vi.mock("../kline/SectorKlineModal", () => ({
  SectorKlineModal: () => <div role="dialog" aria-label="半导体放大行情图" />,
}));

// 拦截 fetchShortTermHistory,避免真实网络请求。
const fetchShortTermHistoryMock = vi.fn();
vi.mock("../short_term/api", async () => {
  const actual = await vi.importActual("../short_term/api");
  return {
    ...actual,
    fetchShortTermHistory: (...args: unknown[]) => fetchShortTermHistoryMock(...args),
  };
});

function makeWrapper() {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  return function Wrapper({ children }: { children: React.ReactNode }) {
    return <QueryClientProvider client={client}>{children}</QueryClientProvider>;
  };
}

const baseSector = {
  sector_name: "半导体",
  phase_confirmed: "accel_up",
  phase_age: 4,
  phase_confidence: 0.72,
  composite_rank: 1,
  rank_change_1d: 2,
  coverage_ratio: 0.96,
  trend_level_score: 0.4,
  velocity_score: 0.5,
  acceleration_score: 0.3,
  participation_score: 0.4,
  volume_score: 0.2,
};

describe("SectorDetailDrawer", () => {
  beforeEach(() => {
    fetchShortTermHistoryMock.mockReset();
    fetchShortTermHistoryMock.mockResolvedValue({
      sector_level: 2,
      model_version: "v2_short_term",
      meta: {
        run_status: "succeeded",
        field_version: "v2_short_term",
        source_max_trade_date: "2026-08-10",
        eligible_sector_count: 30,
        skipped_sector_count: 0,
        pulse_up_count: 0,
        volume_spike_count: 0,
        limit_cluster_count: 0,
        limit_panic_count: 0,
      },
      points: [],
    });
  });

  it("展示 Lifecycle 研究解释,并允许关闭详情", async () => {
    const onClose = vi.fn();
    render(<SectorDetailDrawer sector={baseSector} level={2} asOfDate="2026-08-04" isLatestDate={false} onClose={onClose} />, { wrapper: makeWrapper() });
    await waitFor(() => expect(screen.getByTestId("sector-kline-card")).toBeInTheDocument());
    expect(screen.getByRole("heading", { level: 3, name: "加速走强 · 未知状态" })).toBeInTheDocument();
    expect(screen.getByTestId("sector-kline-card")).toHaveTextContent("半导体|2|2026-08-04");
    fireEvent.click(screen.getByRole("button", { name: "关闭详情" }));
    expect(onClose).toHaveBeenCalledOnce();
  });

  it("第一次 Escape 只关闭行情弹窗,第二次才关闭详情抽屉", async () => {
    const onClose = vi.fn();
    render(<SectorDetailDrawer sector={baseSector} level={2} asOfDate="2026-08-04" isLatestDate={false} onClose={onClose} />, { wrapper: makeWrapper() });
    await waitFor(() => expect(screen.getByTestId("sector-kline-card")).toBeInTheDocument());

    fireEvent.click(screen.getByTestId("sector-kline-card"));
    expect(screen.getByRole("dialog", { name: "半导体放大行情图" })).toBeInTheDocument();
    fireEvent.keyDown(window, { key: "Escape" });
    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
    expect(onClose).not.toHaveBeenCalled();
    fireEvent.keyDown(window, { key: "Escape" });
    expect(onClose).toHaveBeenCalledOnce();
  });

  it("工作台日期变化时自动关闭旧的行情弹窗", async () => {
    const onClose = vi.fn();
    const sector = { ...baseSector };
    const { rerender } = render(<SectorDetailDrawer sector={sector} level={2} asOfDate="2026-08-04" isLatestDate={false} onClose={onClose} />, { wrapper: makeWrapper() });
    await waitFor(() => expect(screen.getByTestId("sector-kline-card")).toBeInTheDocument());

    fireEvent.click(screen.getByTestId("sector-kline-card"));
    expect(screen.getByRole("dialog")).toBeInTheDocument();
    rerender(<SectorDetailDrawer sector={sector} level={2} asOfDate="2026-08-05" isLatestDate={false} onClose={onClose} />);
    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  });

  it("展示当前 Lifecycle、转移与固定声明", async () => {
    render(<SectorDetailDrawer sector={{ ...baseSector, lifecycle_state: "trending", lifecycle_reason: "phase_accel_up", lifecycle_age: 3, lifecycle_changed: true }} previousLifecycleState="repair" level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />, { wrapper: makeWrapper() });
    await waitFor(() => expect(screen.getByTestId("sector-kline-card")).toBeInTheDocument());

    expect(screen.getByRole("heading", { level: 3, name: "加速走强 · 趋势运行" })).toBeInTheDocument();
    expect(screen.getByText(/修复观察.*趋势运行/)).toBeInTheDocument();
    expect(screen.getByText("Lifecycle 为市场状态观察标签,不构成交易建议。")).toBeInTheDocument();
  });

  it("在行情信息与 K 线卡之前展示组合研究结论及 Lifecycle 指标", async () => {
    render(<SectorDetailDrawer sector={{ ...baseSector, phase_confirmed: "reversal_confirmed", lifecycle_state: "emerging", lifecycle_reason: "reversal_confirmed", lifecycle_age: 3, lifecycle_changed: true }} previousLifecycleState="repair" level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />, { wrapper: makeWrapper() });
    await waitFor(() => expect(screen.getByTestId("sector-kline-card")).toBeInTheDocument());

    const conclusion = screen.getByLabelText("组合研究结论");
    const context = screen.getByLabelText("板块行情信息");
    const klineCard = screen.getByTestId("sector-kline-card");
    expect(conclusion).toHaveTextContent("修复确认 · 初步启动");
    expect(conclusion).toHaveTextContent("可进入重点跟踪，等待排名与市场环境共同确认。");
    expect(conclusion).toHaveTextContent("确认阶段为修复确认");
    expect(conclusion).toHaveTextContent("持续天数");
    expect(conclusion).toHaveTextContent("3 日");
    expect(conclusion).toHaveTextContent("前态 → 当前态");
    expect(conclusion).toHaveTextContent("修复观察 → 初步启动");
    expect(conclusion.compareDocumentPosition(context) & Node.DOCUMENT_POSITION_FOLLOWING).toBeTruthy();
    expect(conclusion.compareDocumentPosition(klineCard) & Node.DOCUMENT_POSITION_FOLLOWING).toBeTruthy();
  });

  it("在 K 线卡之前展示当前层级和截至日的板块行情信息卡", async () => {
    render(<SectorDetailDrawer sector={{ ...baseSector, lifecycle_state: "trending" }} previousLifecycleState="repair" level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />, { wrapper: makeWrapper() });
    await waitFor(() => expect(screen.getByTestId("sector-kline-card")).toBeInTheDocument());

    const context = screen.getByLabelText("板块行情信息");
    const klineCard = screen.getByTestId("sector-kline-card");
    expect(context).toHaveTextContent("板块行情");
    expect(context).toHaveTextContent("价格口径: 申万二级行业等权合成指数日线收盘价");
    expect(context).toHaveTextContent("截至日期: 2026-08-10");
    expect(context.compareDocumentPosition(klineCard) & Node.DOCUMENT_POSITION_FOLLOWING).toBeTruthy();
    expect(screen.getByText(/修复观察.*趋势运行/)).toBeInTheDocument();
  });

  it("在前一状态缺失时明示不可用", async () => {
    render(<SectorDetailDrawer sector={{ ...baseSector, lifecycle_state: "trending" }} level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />, { wrapper: makeWrapper() });
    await waitFor(() => expect(screen.getByTestId("sector-kline-card")).toBeInTheDocument());

    expect(screen.getByText("前一状态暂不可用")).toBeInTheDocument();
  });

  it("将 Lifecycle 持续天数与今日变化的缺失值显示为数据不足", async () => {
    const baseForNull = { ...baseSector, lifecycle_state: "trending" };
    const { rerender } = render(<SectorDetailDrawer sector={{ ...baseForNull, lifecycle_age: 3, lifecycle_changed: true }} level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />, { wrapper: makeWrapper() });
    await waitFor(() => expect(screen.getByTestId("sector-kline-card")).toBeInTheDocument());

    expect(screen.getByText("持续天数").parentElement).toHaveTextContent("3 日");
    expect(screen.getByText("今日变化").parentElement).toHaveTextContent("是");

    rerender(<SectorDetailDrawer sector={{ ...baseForNull, lifecycle_age: null, lifecycle_changed: false }} level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />);
    expect(screen.getByText("持续天数").parentElement).toHaveTextContent("数据不足");
    expect(screen.getByText("今日变化").parentElement).toHaveTextContent("否");

    rerender(<SectorDetailDrawer sector={{ ...baseForNull, lifecycle_changed: undefined }} level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />);
    expect(screen.getByText("持续天数").parentElement).toHaveTextContent("数据不足");
    expect(screen.getByText("今日变化").parentElement).toHaveTextContent("数据不足");

    rerender(<SectorDetailDrawer sector={{ ...baseForNull, lifecycle_changed: null }} level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />);
    expect(screen.getByText("今日变化").parentElement).toHaveTextContent("数据不足");
  });

  it("渲染短期命中与中长期观察双列布局", async () => {
    const shortTerm = {
      sector_name: "半导体",
      score_eligible: true,
      short_term_intensity: "intense" as const,
      short_term_labels: "pulse_up,volume_spike",
      short_term_composite: 0.85,
      short_term_composite_rank: 1,
      ret_1: 0.012,
      rs_1: 0.005,
      breadth_up: 0.78,
    };
    render(<SectorDetailDrawer sector={baseSector} shortTerm={shortTerm} level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />, { wrapper: makeWrapper() });
    await waitFor(() => expect(screen.getByTestId("sector-kline-card")).toBeInTheDocument());

    expect(screen.getByText("短期命中")).toBeInTheDocument();
    expect(screen.getByText("中长期观察")).toBeInTheDocument();
    expect(screen.getByText("短期综合分")).toBeInTheDocument();
    await waitFor(() => expect(screen.getByText("短期综合分")).toBeInTheDocument());
    expect(screen.getByText("0.850")).toBeInTheDocument();
    expect(screen.getByText("强异动")).toBeInTheDocument();
    // 命中标签 chip
    expect(screen.getByText("单日脉冲上涨")).toBeInTheDocument();
    expect(screen.getByText("量能异动")).toBeInTheDocument();
    expect(screen.getByText("评分拆解")).toBeInTheDocument();
    expect(screen.getByText("数据覆盖率")).toBeInTheDocument();
    expect(screen.getByText("阶段置信度")).toBeInTheDocument();
    expect(screen.getByText("阶段持续")).toBeInTheDocument();
    expect(screen.getByText("当前阶段")).toBeInTheDocument();
    expect(screen.getByText("综合排名")).toBeInTheDocument();
  });

  it("shortTerm 为 null 时短期列显示空态卡片,不抛错", async () => {
    render(<SectorDetailDrawer sector={baseSector} shortTerm={null} level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />, { wrapper: makeWrapper() });
    await waitFor(() => expect(screen.getByTestId("sector-kline-card")).toBeInTheDocument());

    expect(screen.getByText("当日无短期评分,可在次日观察面板继续跟踪")).toBeInTheDocument();
    expect(screen.getByText("中长期观察")).toBeInTheDocument();
  });

  it("短期列的命中标签 chips 按优先级排序", async () => {
    const shortTerm = {
      sector_name: "半导体",
      score_eligible: true,
      short_term_intensity: "moderate" as const,
      short_term_labels: "volume_spike,limit_cluster,pulse_up",
      short_term_composite: 0.6,
      short_term_composite_rank: 5,
    };
    render(<SectorDetailDrawer sector={baseSector} shortTerm={shortTerm} level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />, { wrapper: makeWrapper() });
    await waitFor(() => expect(screen.getByTestId("sector-kline-card")).toBeInTheDocument());

    const chips = screen.getAllByText(/^单日脉冲上涨$|^量能异动$|^涨停集群$/);
    expect(chips.map((c) => c.textContent)).toEqual(["单日脉冲上涨", "涨停集群", "量能异动"]);
  });

  it("5 日 strip 在数据为空时显示'数据不足'占位", async () => {
    render(<SectorDetailDrawer sector={baseSector} shortTerm={null} level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />, { wrapper: makeWrapper() });
    await waitFor(() => expect(screen.getByTestId("sector-kline-card")).toBeInTheDocument());

    expect(screen.getByText("5 日连续性")).toBeInTheDocument();
    // 至少 1 个 '数据不足' aria-label
    await waitFor(() => expect(document.querySelectorAll(".short-term-strip__cell").length).toBe(5));
    expect(screen.getAllByLabelText("数据不足").length).toBeGreaterThan(0);
  });

  it("短期历史 strip 渲染 5 个 cell 并显示当日 .is-now", async () => {
    fetchShortTermHistoryMock.mockResolvedValueOnce({
      sector_level: 2,
      model_version: "v2_short_term",
      meta: {
        run_status: "succeeded",
        field_version: "v2_short_term",
        source_max_trade_date: "2026-08-10",
        eligible_sector_count: 30,
        skipped_sector_count: 0,
        pulse_up_count: 1,
        volume_spike_count: 1,
        limit_cluster_count: 0,
        limit_panic_count: 0,
      },
      points: [
        { sector_name: "半导体", as_of_date: "2026-08-10", score_eligible: true, short_term_intensity: "intense", short_term_labels: "pulse_up", short_term_composite: 0.85, ret_1: 0.012, rs_1: 0.005, rvol_1_20: 1.85 },
        { sector_name: "半导体", as_of_date: "2026-08-09", score_eligible: true, short_term_intensity: "moderate", short_term_labels: "volume_spike", short_term_composite: 0.5, ret_1: 0.005, rs_1: 0.002, rvol_1_20: 1.5 },
        { sector_name: "半导体", as_of_date: "2026-08-08", score_eligible: true, short_term_intensity: "mild", short_term_labels: "short_rebound_candidate", short_term_composite: 0.3 },
        { sector_name: "半导体", as_of_date: "2026-08-07", score_eligible: true },
        { sector_name: "半导体", as_of_date: "2026-08-06", score_eligible: true, short_term_intensity: "moderate", short_term_labels: "pulse_up" },
      ],
    });
    render(<SectorDetailDrawer sector={baseSector} shortTerm={null} level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />, { wrapper: makeWrapper() });
    await waitFor(() => expect(screen.getByTestId("sector-kline-card")).toBeInTheDocument());

    await waitFor(() => expect(document.querySelectorAll(".short-term-strip__cell").length).toBe(5));
    // 当日 cell 应有 is-now class
    const nowCells = document.querySelectorAll(".short-term-strip__cell.is-now");
    expect(nowCells.length).toBe(1);
    expect(nowCells[0]).toHaveAttribute("aria-label", expect.stringMatching(/2026-08-10/));
    // 不同强度的 cell
    await waitFor(() => expect(document.querySelectorAll(".short-term-strip__cell.is-intense").length).toBeGreaterThan(0));
    await waitFor(() => expect(document.querySelectorAll(".short-term-strip__cell.is-moderate").length).toBeGreaterThan(0));
    await waitFor(() => expect(document.querySelectorAll(".short-term-strip__cell.is-mild").length).toBeGreaterThan(0));
    await waitFor(() => expect(document.querySelectorAll(".short-term-strip__cell.is-empty").length).toBeGreaterThan(0));
  });
});