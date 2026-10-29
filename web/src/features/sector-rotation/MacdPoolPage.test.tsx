import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { MacdPoolPage } from "./MacdPoolPage";
import * as api from "./api";

// ECharts 在 jsdom 下无法使用 canvas，这里只验证 React 树，不依赖图表绘制。
vi.mock("./MacdPoolChart", () => ({
  MacdPoolChart: ({ points, trajectory, stateLabel, selectedCode }: { points: unknown[]; trajectory?: { points: { er: number | null; adx: number | null }[] } | null; stateLabel?: string; selectedCode?: string | null }) => (
    <div data-testid="macd-chart" data-selected={selectedCode ?? ""} data-points={points.length} data-state={stateLabel ?? ""}>
      {trajectory ? <span data-testid="macd-chart-state">{stateLabel}</span> : null}
    </div>
  ),
}));

function renderPage() {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  return render(<QueryClientProvider client={client}><MacdPoolPage /></QueryClientProvider>);
}

function mockApi(responses: Record<string, unknown>) {
  vi.spyOn(api, "requestJson").mockImplementation(async (path: string) => {
    if (path.includes("etf-kline")) return responses.etfKline;
    if (path.includes("sector-kline")) return responses.sectorKline;
    if (path.includes("/snapshot")) return responses.snapshot;
    if (path.includes("macd-pool-dates")) return responses.dates;
    if (path.includes("macd-pool-trajectory")) return responses.trajectory;
    if (path.includes("macd-pool")) return responses.pool;
    throw new Error(`unexpected api call: ${path}`);
  });
}

describe("MacdPoolPage", () => {
 it("opens a market drawer for an ETF and closes it", async () => {
    mockApi({
      dates: { dates: ["2026-08-13"] },
      pool: { groups: { etf: [{ entity_type: "etf", stock_code: "510300.SH", stock_name: "沪深300ETF" }], sector_l1: [], sector_l2: [] } },
      trajectory: { trajectory: { stock_code: "510300.SH", points: [] } },
      etfKline: { stock_code: "510300.SH", actual_end_date: "2026-08-13", bars: [{ trade_date: "2026-08-13", timestamp: 1786540800000, open: 4, high: 4.2, low: 3.9, close: 4.1, volume: 1000, amount: 4100 }], meta: { bar_count: 1, skipped_bar_count: 0, warmup_target: 100 } },
    });
    renderPage();
    fireEvent.click(await screen.findByRole("button", { name: /沪深300ETF/ }));
    expect(await screen.findByRole("complementary", { name: "沪深300ETF 详情" })).toBeInTheDocument();
    expect(screen.getByText("ETF 行情")).toBeInTheDocument();
    expect(screen.getByText(/前复权/)).toBeInTheDocument();
    expect(await screen.findByRole("button", { name: "显示最近 60 个交易日" })).toBeInTheDocument();
    expect(screen.queryByText("组合研究结论")).not.toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: "关闭详情" }));
    expect(screen.queryByRole("complementary", { name: "沪深300ETF 详情" })).not.toBeInTheDocument();
 });

 it("opens the existing rotation drawer for a sector", async () => {
    mockApi({
      dates: { dates: ["2026-08-13"] },
      pool: { groups: { etf: [], sector_l1: [], sector_l2: [{ entity_type: "sector_l2", stock_code: "半导体", stock_name: "半导体" }] } },
      trajectory: { trajectory: { stock_code: "半导体", points: [] } },
      snapshot: { as_of_date: "2026-08-13", sector_level: 2, model_version: "v1", meta: { run_status: "succeeded", field_version: "v1", source_max_trade_date: "2026-08-13", eligible_sector_count: 1, skipped_sector_count: 0, market_regime: null, regime_multiplier: null }, sectors: [{ sector_name: "半导体", score_eligible: true, lifecycle_state: null, lifecycle_reason: null, lifecycle_changed: null, lifecycle_age: null, phase_confirmed: "neutral", phase_confidence: null, composite_rank: 1, rank_change_1d: null, trend_level_score: null, velocity_score: null, acceleration_score: null, participation_score: null, volume_score: null }] },
    });
    renderPage();
    fireEvent.click(await screen.findByRole("button", { name: /半导体/ }));
    expect(await screen.findByRole("complementary", { name: "半导体 详情" })).toBeInTheDocument();
    expect(await screen.findByText("组合研究结论")).toBeInTheDocument();
 });

 it("keeps a first-level sector drawer available when its rotation snapshot is absent", async () => {
    mockApi({
      dates: { dates: ["2026-08-13"] },
      pool: { groups: { etf: [], sector_l1: [{ entity_type: "sector_l1", stock_code: "电子", stock_name: "电子" }], sector_l2: [] } },
      trajectory: { trajectory: { stock_code: "电子", points: [] } },
    });
    renderPage();
    fireEvent.click(await screen.findByRole("button", { name: /电子/ }));
    expect(await screen.findByRole("complementary", { name: "电子 详情" })).toBeInTheDocument();
    expect(screen.getByText("板块行情")).toBeInTheDocument();
    await waitFor(() => expect(api.requestJson).toHaveBeenCalledWith(
      "/api/v1/sector-rotation/sector-kline",
      { sector_name: "电子", level: 1, end_date: "2026-08-13" },
      expect.anything(),
    ));
 });
 it("filters ETF points whose names are missing or still equal to the code", async () => {
    mockApi({
      dates: { dates: ["2026-08-13"] },
      pool: { groups: { etf: [
        { entity_type: "etf", stock_code: "511010.SH", stock_name: null, kama_efficiency: 0.6, adx_14: 24 },
        { entity_type: "etf", stock_code: "511020.SH", stock_name: "511020.SH", kama_efficiency: 0.5, adx_14: 22 },
        { entity_type: "etf", stock_code: "511030.SH", stock_name: "511030", kama_efficiency: 0.5, adx_14: 22 },
        { entity_type: "etf", stock_code: "510300.SH", stock_name: "沪深300ETF", kama_efficiency: 0.7, adx_14: 26 },
      ], sector_l1: [], sector_l2: [] } },
      trajectory: { trajectory: { stock_code: "510300.SH", points: [] } },
    });
    renderPage();
    await waitFor(() => expect(screen.getByTestId("macd-chart")).toHaveAttribute("data-points", "1"));
    expect(screen.getByRole("button", { name: /沪深300ETF/ })).toBeInTheDocument();
    expect(screen.queryByRole("button", { name: /511010|511020|511030/ })).not.toBeInTheDocument();
 });

 it("renders grouped entities", async () => {
    mockApi({
      dates: { dates: ["2026-08-13"] },
      pool: { groups: { etf: [{ entity_type: "etf", stock_code: "510300.SH", stock_name: "沪深300ETF", vol_ratio: 1.6, rsi_14: 60 }], sector_l1: [], sector_l2: [] } },
      trajectory: { trajectory: { stock_code: "510300.SH", points: [] } },
    });
    renderPage();
    await waitFor(() => expect(screen.getByRole("button", { name: /沪深300ETF/ })).toBeInTheDocument());
    const header = screen.getByText((_, el) => el?.tagName === "SPAN" && (el.textContent ?? "").replace(/\s+/g, "") === "1个命中");
    expect(header).toBeInTheDocument();
 });

 it("renders empty state on request failure", async () => {
    vi.spyOn(api, "requestJson").mockImplementation(async (path: string) => {
      if (path.includes("macd-pool-dates")) return { dates: ["2026-08-13"] };
      throw new Error("offline");
    });
    renderPage();
    await waitFor(() => expect(screen.getByText("该日期暂无 MACD 板块池数据")).toBeInTheDocument());
 });

 it("renders the trajectory state after selecting an entity", async () => {
    mockApi({
      dates: { dates: ["2026-08-13"] },
      pool: { groups: { etf: [{ entity_type: "etf", stock_code: "510300.SH", stock_name: "沪深300ETF", kama_efficiency: 0.6, adx_14: 24 }], sector_l1: [], sector_l2: [] } },
      trajectory: { trajectory: { stock_code: "510300.SH", points: [{ as_of_date: "2026-08-12", er: 0.4, adx: 20 }, { as_of_date: "2026-08-13", er: 0.6, adx: 24 }] } },
    });
    renderPage();
    const row = await screen.findByRole("button", { name: /沪深300ETF/ });
    fireEvent.click(row);
    expect(await screen.findByTestId("macd-chart-state")).toHaveTextContent(/趋势强化/);
 });
});
