import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { fetchResearchSummary } from "./api";
import { TodaysOpportunities } from "./TodaysOpportunities";

vi.mock("./api", () => ({
  fetchResearchSummary: vi.fn(async (_date: string, _level: number, mode: string) => ({
    as_of_date: "2026-08-20", sector_level: 2, snapshot_mode: mode, research_status: "shadow",
    summary: { core_etf_ready: 1, trend_candidates: 2, repair_candidates: 3, reduce_or_avoid: 0 }, source_versions: [],
  })),
}));

describe("TodaysOpportunities", () => {
  it("requests the delayed summary in the selected primary mode", async () => {
    const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
    render(<QueryClientProvider client={client}><TodaysOpportunities asOfDate="2026-08-20" snapshotMode="delayed_shadow" /></QueryClientProvider>);
    await screen.findByText("研究机会摘要");
    expect(vi.mocked(fetchResearchSummary)).toHaveBeenCalledWith("2026-08-20", 2, "delayed_shadow");
  });
});
