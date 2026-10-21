import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { fetchLatestResearchDate, fetchResearchCandidates, fetchResearchSummary } from "../features/sector-rotation/research-cockpit/api";
import { App } from "./App";

vi.mock("../features/sector-rotation/research-cockpit/api", () => ({
  fetchLatestResearchDate: vi.fn(async (_level: number, mode?: string) => ({ as_of_date: "2026-08-20", sector_level: 2, snapshot_mode: mode ?? "backfill" })),
  fetchResearchSummary: vi.fn(async (_date: string, _level: number, mode: string) => ({ as_of_date: "2026-08-20", sector_level: 2, snapshot_mode: mode, research_status: "shadow", summary: {}, source_versions: [] })),
  fetchResearchCandidates: vi.fn(async (_date: string, _level: number, mode: string) => ({ as_of_date: "2026-08-20", sector_level: 2, snapshot_mode: mode, candidates: [] })),
  fetchWatchlist: vi.fn(async () => ({ items: [] })), fetchDecisions: vi.fn(async () => ({ decisions: [] })),
  addToWatchlist: vi.fn(), recordDecision: vi.fn(), updateWatchlist: vi.fn(), removeFromWatchlist: vi.fn(),
}));

describe("App", () => {
  it("shows the sector rotation title and loading state", () => {
    render(<App />);
    expect(screen.getByRole("heading", { name: "板块轮动" })).toBeInTheDocument();
  });

  it("opens the latest available mode and propagates it to research queries", async () => {
    render(<App />);
    fireEvent.click(screen.getAllByRole("tab")[2]);
    const modeSelect = await screen.findByRole("combobox");
    await waitFor(() => expect(vi.mocked(fetchLatestResearchDate)).toHaveBeenCalledWith(2));
    await waitFor(() => expect(vi.mocked(fetchLatestResearchDate)).toHaveBeenCalledWith(2, "backfill"));
    await waitFor(() => expect(vi.mocked(fetchResearchSummary)).toHaveBeenCalledWith("2026-08-20", 2, "backfill"));
    await waitFor(() => expect(vi.mocked(fetchResearchCandidates)).toHaveBeenCalledWith("2026-08-20", 2, "backfill", "etf_core", undefined));
    expect(modeSelect).toHaveValue("backfill");
    fireEvent.change(modeSelect, { target: { value: "delayed_shadow" } });
    await waitFor(() => expect(vi.mocked(fetchLatestResearchDate)).toHaveBeenCalledWith(2, "delayed_shadow"));
  });
});
