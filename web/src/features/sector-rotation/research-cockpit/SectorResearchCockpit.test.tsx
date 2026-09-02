import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { fetchResearchCandidates } from "./api";
import { SectorResearchCockpit } from "./SectorResearchCockpit";

vi.mock("./api", () => ({
  addToWatchlist: vi.fn(), recordDecision: vi.fn(),
  fetchResearchCandidates: vi.fn(async (_date: string, _level: number, mode: string, strategyType: string) => ({
    as_of_date: "2026-08-20", sector_level: 2, snapshot_mode: mode,
    candidates: strategyType === "etf_core" ? [{
      id: 1, entity_code: "510300.SH", entity_name: "沪深300ETF", sector_name: "指数", strategy_type: "etf_core", candidate_status: "ready", candidate_score: 0.8,
      rank_in_sector: 1, research_status: "shadow", validation_status: "not_evaluated", execution_status: "manual_only", model_version: "v1", config_hash: "hash", snapshot_mode: mode, feature_json: {}, reasons_json: [], risk_flags_json: [],
      data_available_at: "2026-08-20T18:00:00", run_at: "2026-08-21T09:10:00", execution_eligible_at: "2026-08-21T09:30:00", daily_bar_entry_date: "2026-08-21", availability_basis: "market_close_1800",
    }] : [],
  })),
}));

function renderCockpit(mode: "live_shadow" | "delayed_shadow" | "backfill" = "live_shadow") {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  return render(<QueryClientProvider client={client}><SectorResearchCockpit asOfDate="2026-08-20" snapshotMode={mode} /></QueryClientProvider>);
}

describe("SectorResearchCockpit", () => {
  it("shows a security name, code, and complete timing contract", async () => {
    renderCockpit();
    expect(await screen.findByText("沪深300ETF")).toBeInTheDocument();
    expect(screen.getByText("510300.SH")).toBeInTheDocument();
    expect(screen.getByText("数据就绪：2026-08-20 18:00")).toBeInTheDocument();
    expect(screen.getByText("最早日线入场：2026-08-21 开盘")).toBeInTheDocument();
  });

  it("does not report an unscored ETF as data-quality blocked", async () => {
    vi.mocked(fetchResearchCandidates).mockImplementation(async (_date, _level, mode, strategyType) => ({
      as_of_date: "2026-08-20", sector_level: 2, snapshot_mode: mode ?? "delayed_shadow",
      candidates: strategyType === "etf_core" ? [{
        id: 3, entity_code: "510300.SH", entity_name: "沪深300ETF", strategy_type: "etf_core", candidate_status: "ready", candidate_score: null,
        research_status: "shadow", validation_status: "not_evaluated", execution_status: "manual_only", model_version: "v1", config_hash: "hash", snapshot_mode: "delayed_shadow", feature_json: {}, reasons_json: [], risk_flags_json: [], is_data_quality_blocked: false,
        data_available_at: "2026-08-20T18:00:00", run_at: "2026-08-21T09:10:00", execution_eligible_at: "2026-08-21T09:30:00", daily_bar_entry_date: "2026-08-21", availability_basis: "market_close_1800",
      }] : [],
    }));
    renderCockpit("delayed_shadow");
    expect(await screen.findByText("未评分")).toBeInTheDocument();
    expect(screen.queryByText("数据质量阻断")).not.toBeInTheDocument();
  });

  it("keeps a complete timing contract when daily entry projection is unavailable", async () => {
    vi.mocked(fetchResearchCandidates).mockImplementation(async (_date, _level, mode, strategyType) => ({
      as_of_date: "2026-08-28", sector_level: 2, snapshot_mode: mode ?? "delayed_shadow",
      candidates: strategyType === "etf_core" ? [{
        id: 4, entity_code: "510300.SH", entity_name: "沪深300ETF", strategy_type: "etf_core", candidate_status: "ready", candidate_score: null,
        research_status: "shadow", validation_status: "not_evaluated", execution_status: "manual_only", model_version: "v1", config_hash: "hash", snapshot_mode: "delayed_shadow", feature_json: {}, reasons_json: [], risk_flags_json: [], is_data_quality_blocked: false,
        data_available_at: "2026-08-28T18:00:00", run_at: "2026-08-30T11:30:00", execution_eligible_at: "2026-08-31T09:30:00", daily_bar_entry_date: null, daily_bar_entry_reason: "trading_calendar_unavailable", availability_basis: "market_close_1800",
      }] : [],
    }));
    renderCockpit("delayed_shadow");
    expect(await screen.findByText("可执行时间：2026-08-31 09:30")).toBeInTheDocument();
    expect(screen.getByText("日线入场日待交易日历确认")).toBeInTheDocument();
    expect(screen.queryByText(/时间契约不完整/)).not.toBeInTheDocument();
  });

  it("uses the delayed mode for all candidate requests", async () => {
    renderCockpit("delayed_shadow");
    await screen.findByText("沪深300ETF");
    expect(vi.mocked(fetchResearchCandidates)).toHaveBeenCalledWith("2026-08-20", 2, "delayed_shadow", "etf_core", undefined);
  });

  it("separates post-open operational availability from the following daily-bar entry", async () => {
    vi.mocked(fetchResearchCandidates).mockImplementation(async (_date, _level, mode, strategyType) => ({
      as_of_date: "2026-08-20", sector_level: 2, snapshot_mode: mode ?? "delayed_shadow",
      candidates: strategyType === "etf_core" ? [{
        id: 2, entity_code: "510300.SH", strategy_type: "etf_core", candidate_status: "ready", candidate_score: 0.8, research_status: "shadow", validation_status: "not_evaluated", execution_status: "manual_only", model_version: "v1", config_hash: "hash", snapshot_mode: "delayed_shadow", feature_json: {}, reasons_json: [], risk_flags_json: [],
        data_available_at: "2026-08-20T18:00:00", run_at: "2026-08-21T10:00:00", execution_eligible_at: "2026-08-21T10:00:00", daily_bar_entry_date: "2026-08-22", availability_basis: "market_close_1800",
      }] : [],
    }));
    renderCockpit("delayed_shadow");
    expect(await screen.findByText("可执行时间：2026-08-21 10:00")).toBeInTheDocument();
    expect(screen.getByText("最早日线入场：2026-08-22 开盘")).toBeInTheDocument();
  });
});
