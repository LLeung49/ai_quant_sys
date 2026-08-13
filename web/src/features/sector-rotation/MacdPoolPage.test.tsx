import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { render, screen, waitFor } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { MacdPoolPage } from "./MacdPoolPage";
import * as api from "./api";
function renderPage() { const client = new QueryClient({ defaultOptions: { queries: { retry: false } } }); return render(<QueryClientProvider client={client}><MacdPoolPage /></QueryClientProvider>); }
describe("MacdPoolPage", () => {
 it("renders grouped entities", async () => { vi.spyOn(api, "requestJson").mockResolvedValue({ groups: { etf: [{ entity_type: "etf", stock_code: "510300.SH", stock_name: "沪深300ETF", vol_ratio: 1.6, rsi_14: 60 }], sector_l1: [], sector_l2: [] } }); renderPage(); expect(await screen.findByText("沪深300ETF")).toBeInTheDocument(); expect(screen.getByText("ETF（1）")).toBeInTheDocument(); });
 it("renders empty state on request failure", async () => { vi.spyOn(api, "requestJson").mockRejectedValue(new Error("offline")); renderPage(); await waitFor(() => expect(screen.getByText("当前日期暂无 MACD 板块池数据")).toBeInTheDocument()); });
 it("renders the trajectory state after selecting an entity", async () => { vi.spyOn(api, "requestJson").mockImplementation(async (path) => path.includes("trajectory") ? { trajectory: { stock_code: "510300.SH", points: [{ as_of_date: "2026-08-12", er: 0.4, adx: 20 }, { as_of_date: "2026-08-13", er: 0.6, adx: 24 }] } } : path.includes("dates") ? { dates: ["2026-08-13"] } : { groups: { etf: [{ entity_type: "etf", stock_code: "510300.SH", stock_name: "沪深300ETF", kama_efficiency: 0.6, adx_14: 24 }], sector_l1: [], sector_l2: [] } }); renderPage(); const row = await screen.findByText("沪深300ETF"); row.closest("tr")?.click(); expect(await screen.findByText(/趋势强化/)).toBeInTheDocument(); });
});
