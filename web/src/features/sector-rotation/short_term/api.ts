/** v2_short_term 短期异动页面的类型校验 API 客户端。 */
import { z } from "zod";

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL ?? "http://127.0.0.1:8000";

const responseMetaSchema = z.object({
  run_status: z.literal("succeeded"),
  field_version: z.literal("v2_short_term"),
  source_max_trade_date: z.string().nullable(),
  eligible_sector_count: z.number().int().nullable(),
  skipped_sector_count: z.number().int().nullable(),
  pulse_up_count: z.number().int().nullable(),
  volume_spike_count: z.number().int().nullable(),
  limit_cluster_count: z.number().int().nullable(),
  limit_panic_count: z.number().int().nullable(),
  pulse_up_sectors: z.array(z.string()).nullable().optional(),
  volume_spike_sectors: z.array(z.string()).nullable().optional(),
  limit_cluster_sectors: z.array(z.string()).nullable().optional(),
  limit_panic_sectors: z.array(z.string()).nullable().optional(),
});
export type ShortTermResponseMeta = z.infer<typeof responseMetaSchema>;

/** 短期异动快照行的字段约定（passthrough 以容忍后端新增字段）。 */
export const shortTermSectorSchema = z
  .object({
    sector_name: z.string(),
    score_eligible: z.union([z.boolean(), z.literal(0), z.literal(1)]).transform(Boolean),
    ret_1: z.number().nullable().optional(),
    ret_2: z.number().nullable().optional(),
    rs_1: z.number().nullable().optional(),
    rs_2: z.number().nullable().optional(),
    rs5_accel_1d: z.number().nullable().optional(),
    ma5_slope: z.number().nullable().optional(),
    rvol_1_20: z.number().nullable().optional(),
    share_impulse_1d: z.number().nullable().optional(),
    amount_share_today: z.number().nullable().optional(),
    breadth_up: z.number().nullable().optional(),
    breadth_above_ma5: z.number().nullable().optional(),
    breadth_new_high_5: z.number().nullable().optional(),
    breadth_strong_1d: z.number().nullable().optional(),
    breadth_rvol_1d: z.number().nullable().optional(),
    limit_up_ratio: z.number().nullable().optional(),
    limit_down_ratio: z.number().nullable().optional(),
    streak_pos_ret: z.number().int().nullable().optional(),
    streak_high_breadth: z.number().int().nullable().optional(),
    streak_top_limit_up: z.number().int().nullable().optional(),
    pulse_score: z.number().nullable().optional(),
    volume_spike_score: z.number().nullable().optional(),
    breadth_spike_score: z.number().nullable().optional(),
    limit_score: z.number().nullable().optional(),
    momentum_shift_score: z.number().nullable().optional(),
    short_term_composite: z.number().nullable().optional(),
    short_term_composite_rank: z.number().int().nullable().optional(),
    short_term_labels: z.string().nullable().optional(),
    short_term_intensity: z.enum(["intense", "moderate", "mild", "none", ""]).nullable().optional(),
  })
  .passthrough();
export type ShortTermSector = z.infer<typeof shortTermSectorSchema>;

const snapshotSchema = z.object({
  as_of_date: z.string(),
  sector_level: z.number().int(),
  model_version: z.string(),
  meta: responseMetaSchema,
  sectors: z.array(shortTermSectorSchema),
});
export type ShortTermSnapshotResponse = z.infer<typeof snapshotSchema>;

const historySchema = z.object({
  sector_level: z.number().int(),
  model_version: z.string(),
  meta: responseMetaSchema,
  points: z.array(shortTermSectorSchema),
});
export type ShortTermHistoryResponse = z.infer<typeof historySchema>;

const leadersSchema = z.object({
  as_of_date: z.string(),
  sector_level: z.number().int(),
  model_version: z.string(),
  meta: responseMetaSchema,
  leaders: z.array(shortTermSectorSchema),
});
export type ShortTermLeadersResponse = z.infer<typeof leadersSchema>;

export const availableDatesSchema = z.object({
  sector_level: z.number().int(),
  model_version: z.string(),
  dates: z.array(z.string()),
});
export type AvailableDates = z.infer<typeof availableDatesSchema>;

const errorSchema = z.object({
  error: z.object({
    code: z.string(),
    message: z.string(),
    details: z.unknown().nullable(),
    request_id: z.string(),
  }),
});

/** 短期异动 API 错误，统一抛出供上层捕获。 */
export class ShortTermApiError extends Error {
  constructor(
    readonly code: string,
    message: string,
    readonly requestId: string,
    readonly details: unknown,
  ) {
    super(message);
    this.name = "ShortTermApiError";
  }
}

/**
 * 发送只读请求并处理统一错误信封。
 *
 * 输入：相对 API 路径、查询参数和可选取消信号。
 * 输出：未经业务转换的成功 JSON；失败抛出 ShortTermApiError。
 */
export async function requestJson(
  path: string,
  query: Record<string, string | number> | URLSearchParams,
  signal?: AbortSignal,
): Promise<unknown> {
  const params =
    query instanceof URLSearchParams
      ? query
      : new URLSearchParams(Object.entries(query).map(([key, value]) => [key, String(value)]));
  const response = await fetch(`${apiBaseUrl}${path}?${params.toString()}`, {
    headers: { Accept: "application/json" },
    signal,
  });
  const body: unknown = await response.json();
  if (!response.ok) {
    const parsed = errorSchema.safeParse(body);
    if (parsed.success) {
      throw new ShortTermApiError(
        parsed.data.error.code,
        parsed.data.error.message,
        parsed.data.error.request_id,
        parsed.data.error.details,
      );
    }
    throw new ShortTermApiError(
      "UNEXPECTED_API_ERROR",
      "服务返回了无法识别的错误响应",
      response.headers.get("x-request-id") ?? "unknown",
      null,
    );
  }
  return body;
}

/** 读取单日短期异动全板块快照。 */
export async function fetchShortTermAvailableDates(
  level: number,
  modelVersion = "v2_short_term",
): Promise<AvailableDates> {
  return availableDatesSchema.parse(
    await requestJson("/api/v1/sector-rotation/short-term/available-dates", {
      level,
      model_version: modelVersion,
    }),
  );
}

export async function fetchShortTermSnapshot(
  asOfDate: string,
  level: number,
  modelVersion = "v2_short_term",
): Promise<ShortTermSnapshotResponse> {
  return snapshotSchema.parse(
    await requestJson("/api/v1/sector-rotation/short-term/snapshot", {
      as_of_date: asOfDate,
      level,
      model_version: modelVersion,
    }),
  );
}

/** 读取最多 5 个板块的短期异动历史轨迹。 */
export async function fetchShortTermHistory(
  sectorNames: string[],
  startDate: string,
  endDate: string,
  level: number,
  modelVersion = "v2_short_term",
): Promise<ShortTermHistoryResponse> {
  if (sectorNames.length < 1 || sectorNames.length > 5) {
    throw new Error("轨迹最多选择 5 个行业，且至少选择 1 个行业");
  }
  const query = new URLSearchParams({
    start_date: startDate,
    end_date: endDate,
    level: String(level),
    model_version: modelVersion,
  });
  sectorNames.forEach((name) => query.append("sector_names", name));
  return historySchema.parse(await requestJson("/api/v1/sector-rotation/short-term/history", query));
}

/**
 * 读取当日异动榜：可按标签与最低强度过滤。
 *
 * 输入：交易日、层级、模型版本、可选标签白名单、最低强度。
 * 输出：按 ``short_term_composite_rank`` 升序的异动板块列表。
 */
export async function fetchShortTermLeaders(
  asOfDate: string,
  level: number,
  options: { labels?: string[]; minIntensity?: "intense" | "moderate" | "mild" } = {},
  modelVersion = "v2_short_term",
): Promise<ShortTermLeadersResponse> {
  const query = new URLSearchParams({
    as_of_date: asOfDate,
    level: String(level),
    model_version: modelVersion,
  });
  options.labels?.forEach((label) => query.append("labels", label));
  if (options.minIntensity) query.set("min_intensity", options.minIntensity);
  return leadersSchema.parse(await requestJson("/api/v1/sector-rotation/short-term/leaders", query));
}

/** 后端稳定错误码白名单，用于参数校验。 */
export const SHORT_TERM_LABEL_WHITELIST = [
  "pulse_up",
  "pulse_down",
  "volume_spike",
  "limit_cluster",
  "limit_panic",
  "extreme_up",
  "extreme_down",
  "short_rebound_candidate",
  "short_breakdown_candidate",
] as const;
export type ShortTermLabel = (typeof SHORT_TERM_LABEL_WHITELIST)[number];
