/** 板块轮动只读 API 的类型校验客户端。 */
import { z } from "zod";
import { MAX_TRAJECTORY_SECTORS } from "./history/constants";

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL ?? "http://127.0.0.1:8000";

/** 所有成功响应共用的运行审计和字段语义版本。 */
const responseMetaSchema = z.object({
  run_status: z.literal("succeeded"),
  field_version: z.literal("v1"),
  source_max_trade_date: z.string().nullable(),
  eligible_sector_count: z.number().int().nullable(),
  skipped_sector_count: z.number().int().nullable(),
  market_regime: z.string().nullable(),
  regime_multiplier: z.number().nullable(),
});

const availableDatesSchema = z.object({
  sector_level: z.number().int(),
  model_version: z.string(),
  dates: z.array(z.string()),
  meta: responseMetaSchema,
});

const snapshotSchema = z.object({
  as_of_date: z.string(),
  sector_level: z.number().int(),
  model_version: z.string(),
  meta: responseMetaSchema,
  sectors: z.array(z.record(z.string(), z.unknown())),
});
const historySchema = z.object({ sector_level: z.number().int(), model_version: z.string(), meta: responseMetaSchema, points: z.array(z.record(z.string(), z.unknown())) });

const errorSchema = z.object({
  error: z.object({
    code: z.string(),
    message: z.string(),
    details: z.unknown().nullable(),
    request_id: z.string(),
  }),
});

/** 前端用于根据稳定错误码显示状态页的 API 异常。 */
export class SectorRotationApiError extends Error {
  /** 输入：服务端稳定错误码、中文消息、追踪 ID 和可选安全详情；输出：标准 Error 子类。 */
  constructor(
    readonly code: string,
    message: string,
    readonly requestId: string,
    readonly details: unknown,
  ) {
    super(message);
    this.name = "SectorRotationApiError";
  }
}

/**
 * 发送读取请求并处理统一错误信封。
 *
 * 输入：相对 API 路径与查询参数。
 * 输出：未经业务转换的成功 JSON；失败时抛出 ``SectorRotationApiError``。
 */
/**
 * 发送只读请求并处理统一错误信封。
 *
 * 输入：相对 API 路径、查询参数，以及由 TanStack Query 提供的可选取消信号。
 * 输出：未经业务转换的成功 JSON；失败时抛出 ``SectorRotationApiError``。
 * 异常：网络异常原样抛出；非成功 HTTP 响应转换为统一的 API 异常。
 */
export async function requestJson(
  path: string,
  query: Record<string, string | number> | URLSearchParams,
  signal?: AbortSignal,
): Promise<unknown> {
  const params = query instanceof URLSearchParams ? query : new URLSearchParams(Object.entries(query).map(([key, value]) => [key, String(value)]));
  const response = await fetch(`${apiBaseUrl}${path}?${params.toString()}`, { headers: { Accept: "application/json" }, signal });
  const body: unknown = await response.json();
  if (!response.ok) {
    const parsed = errorSchema.safeParse(body);
    if (parsed.success) {
      throw new SectorRotationApiError(parsed.data.error.code, parsed.data.error.message, parsed.data.error.request_id, parsed.data.error.details);
    }
    throw new SectorRotationApiError("UNEXPECTED_API_ERROR", "服务返回了无法识别的错误响应", response.headers.get("x-request-id") ?? "unknown", null);
  }
  return body;
}

/**
 * 读取存在成功快照的可选日期。
 *
 * 输入：行业层级和模型版本。
 * 输出：日期倒序字符串列表；响应不符合契约时抛出 Zod 错误。
 */
export async function fetchAvailableDates(level: number, modelVersion: string): Promise<string[]> {
  return availableDatesSchema.parse(await requestJson("/api/v1/sector-rotation/available-dates", { level, model_version: modelVersion })).dates;
}

/**
 * 读取指定日期的完整板块截面。
 *
 * 输入：交易日、行业层级与模型版本。
 * 输出：经过运行时校验的快照响应对象。
 */
export async function fetchSnapshot(asOfDate: string, level: number, modelVersion: string) {
  return snapshotSchema.parse(await requestJson("/api/v1/sector-rotation/snapshot", { as_of_date: asOfDate, level, model_version: modelVersion }));
}

/**
 * 读取最多五个行业的已存储轨迹坐标。
 *
 * 输入：行业名称、日期范围、行业层级和模型版本。
 * 输出：按日期排序的历史点；超过五个行业时在请求前拒绝。
 */
export async function fetchSectorHistory(sectorNames: string[], startDate: string, endDate: string, level: number, modelVersion: string) {
  if (sectorNames.length < 1 || sectorNames.length > MAX_TRAJECTORY_SECTORS) throw new Error("轨迹最多选择 5 个行业，且至少选择 1 个行业");
  const query = new URLSearchParams({ start_date: startDate, end_date: endDate, level: String(level), model_version: modelVersion });
  sectorNames.forEach((sectorName) => query.append("sector_name", sectorName));
  return historySchema.parse(await requestJson("/api/v1/sector-rotation/sector-history", query)).points;
}

/**
 * 读取指定区间的全市场已存储回放点。
 *
 * 输入：起止交易日、行业层级和模型版本。
 * 输出：按服务端顺序返回的全行业历史快照点；播放期间不重复请求。
 */
export async function fetchReplay(startDate: string, endDate: string, level: number, modelVersion: string) {
  return historySchema.parse(await requestJson("/api/v1/sector-rotation/replay", { start_date: startDate, end_date: endDate, level, model_version: modelVersion })).points;
}
