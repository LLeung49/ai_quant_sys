import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { render, screen, waitFor } from "@testing-library/react";
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
    if (path.includes("macd-pool-dates")) return responses.dates;
    if (path.includes("macd-pool-trajectory")) return responses.trajectory;
    if (path.includes("macd-pool")) return responses.pool;
    throw new Error(`unexpected api call: ${path}`);
  });
}

describe("MacdPoolPage", () => {
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
    row.click();
    expect(await screen.findByTestId("macd-chart-state")).toHaveTextContent(/趋势强化/);
 });
});