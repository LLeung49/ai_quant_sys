import { z } from "zod";

const candidateSchema = z.object({
  id: z.number().int(),
  entity_code: z.string(), entity_name: z.string().optional(), sector_name: z.string().nullable().optional(), strategy_type: z.string(),
  candidate_status: z.string(), candidate_score: z.number().nullable().optional(), rank_in_sector: z.number().nullable().optional(),
  research_status: z.string(), validation_status: z.string(), execution_status: z.string(), model_version: z.string(),
  config_hash: z.string(), snapshot_mode: z.string(), feature_json: z.record(z.unknown()).or(z.array(z.unknown())),
  reasons_json: z.array(z.unknown()), risk_flags_json: z.array(z.unknown()),
  data_available_at: z.string().nullable().optional(), run_at: z.string().nullable().optional(),
  execution_eligible_at: z.string().nullable().optional(), availability_basis: z.string().nullable().optional(),
  daily_bar_entry_date: z.string().nullable().optional(), daily_bar_entry_reason: z.string().nullable().optional(),
  is_data_quality_blocked: z.boolean().optional(),
}).passthrough();
export type ResearchCandidate = z.infer<typeof candidateSchema>;

const response = z.object({ as_of_date: z.string(), sector_level: z.number(), snapshot_mode: z.string(), candidates: z.array(candidateSchema) });
const summary = z.object({ as_of_date: z.string(), sector_level: z.number(), snapshot_mode: z.string(), research_status: z.string(), summary: z.record(z.number()), source_versions: z.array(z.object({ strategy_type: z.string(), model_version: z.string(), config_hash: z.string() })).default([]) });
const latestDate = z.object({ as_of_date: z.string().nullable(), sector_level: z.number(), snapshot_mode: z.string() });

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL ?? "http://127.0.0.1:8000";
async function get(path: string, params: Record<string, string | number>) {
  const result = await fetch(`${apiBaseUrl}${path}?${new URLSearchParams(Object.entries(params).map(([k, v]) => [k, String(v)]))}`);
  if (!result.ok) throw new Error("研究驾驶舱数据暂不可用");
  return result.json();
}
async function mutate(path: string, method: string, body: unknown) {
  const result = await fetch(`${apiBaseUrl}${path}`, { method, headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(body) });
  if (!result.ok) throw new Error("研究记录保存失败");
  return result.status === 204 ? null : result.json();
}
export function addToWatchlist(snapshotId: number, note = "") { return mutate("/api/v1/sector-rotation/research/watchlist", "POST", { snapshot_id: snapshotId, note }); }
export function updateWatchlist(snapshotId: number, watchStatus: "watch" | "paused" | "done") { return mutate(`/api/v1/sector-rotation/research/watchlist/${snapshotId}`, "PATCH", { snapshot_id: snapshotId, watch_status: watchStatus }); }
export function removeFromWatchlist(snapshotId: number) { return mutate(`/api/v1/sector-rotation/research/watchlist/${snapshotId}?user_id=default`, "DELETE", {}); }
export function recordDecision(snapshotId: number, decision: "WATCH" | "ENTER" | "SKIP" | "EXIT", note = "") { return mutate("/api/v1/sector-rotation/research/decisions", "POST", { snapshot_id: snapshotId, decision, note }); }
export function fetchResearchSummary(asOfDate: string, level = 2, snapshotMode = "live_shadow") {
  return get("/api/v1/sector-rotation/research/today-summary", { as_of_date: asOfDate, level, snapshot_mode: snapshotMode }).then((value) => summary.parse(value));
}
export function fetchLatestResearchDate(level = 2, snapshotMode = "live_shadow") { return get("/api/v1/sector-rotation/research/latest-date", { level, snapshot_mode: snapshotMode }).then((value) => latestDate.parse(value)); }
export function fetchResearchCandidates(asOfDate: string, level = 2, snapshotMode = "live_shadow", strategyType?: string, sectorName?: string) {
  const path = strategyType === "etf_core" ? "/api/v1/sector-rotation/research/etf-candidates" : strategyType === "sector_opportunity" ? "/api/v1/sector-rotation/research/opportunities" : "/api/v1/sector-rotation/research/stock-candidates";
  return get(path, { as_of_date: asOfDate, level, snapshot_mode: snapshotMode, ...(strategyType && !["etf_core", "sector_opportunity"].includes(strategyType) ? { strategy_type: strategyType } : {}), ...(sectorName ? { sector_name: sectorName } : {}) }).then((value) => response.parse({ ...(value as object), candidates: "candidates" in (value as object) ? (value as { candidates: unknown[] }).candidates : (value as { opportunities: unknown[] }).opportunities }));
}
export function fetchWatchlist() { return get("/api/v1/sector-rotation/research/watchlist", { user_id: "default" }); }
export function fetchDecisions() { return get("/api/v1/sector-rotation/research/decisions", { user_id: "default" }); }
