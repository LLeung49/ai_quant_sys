/** 板块合成日 K 线的 HTTP 契约、运行时校验和只读请求客户端。 */
import { z } from "zod";
import { requestJson } from "../api";

/** ISO 日线日期的最小格式约束，排序和截止日约束在完整响应中校验。 */
const tradeDateSchema = z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "交易日必须采用 YYYY-MM-DD 格式");

/** 单根 K 线必须使用有限 JSON 数值，拒绝字符串数值以避免图表计算出现隐式类型转换。 */
const sectorKlineBarSchema = z.object({
  trade_date: tradeDateSchema,
  timestamp: z.number().finite().int().positive(),
  open: z.number().finite().positive(),
  high: z.number().finite().positive(),
  low: z.number().finite().positive(),
  close: z.number().finite().positive(),
  volume: z.number().finite().nonnegative(),
  amount: z.number().finite().nonnegative(),
}).superRefine((bar, context) => {
  if (bar.low > bar.open || bar.low > bar.close) {
    context.addIssue({ code: z.ZodIssueCode.custom, message: "最低价不能高于开盘价或收盘价" });
  }
  if (bar.high < bar.open || bar.high < bar.close || bar.high < bar.low) {
    context.addIssue({ code: z.ZodIssueCode.custom, message: "最高价必须不低于开盘价、收盘价和最低价" });
  }
});

/** 后端元数据说明返回条数、跳过条数和指标预热目标。 */
const sectorKlineMetaSchema = z.object({
  field_version: z.literal("v1"),
  source: z.literal("trade_sector_daily"),
  bar_count: z.number().int().nonnegative(),
  skipped_bar_count: z.number().int().nonnegative(),
  warmup_target: z.literal(100),
});

/** K 线接口的基础响应结构；跨 K 线的排序和截止日约束由 ``parseSectorKlineResponse`` 完成。 */
const sectorKlineResponseSchema = z.object({
  sector_name: z.string().min(1),
  sector_level: z.union([z.literal(1), z.literal(2)]),
  requested_end_date: tradeDateSchema,
  actual_end_date: tradeDateSchema,
  price_basis: z.literal("equal_weight_composite_index"),
  bars: z.array(sectorKlineBarSchema).min(1),
  meta: sectorKlineMetaSchema,
});

/** 板块 K 线接口的已校验成功响应类型，供 Query 与后续图表组件共享。 */
export type SectorKlineResponse = z.infer<typeof sectorKlineResponseSchema>;

/**
 * 解析并校验完整 K 线响应的时间序列不变量。
 *
 * 输入：服务端 JSON 响应和请求时的截止日。
 * 输出：类型安全且交易日严格升序、唯一、未越过截止日的 K 线响应。
 * 异常：响应缺字段、数值无效、OHLC 关系异常、日期重复/倒序/越界时抛出 ``ZodError``。
 */
function parseSectorKlineResponse(payload: unknown, requestedEndDate: string): SectorKlineResponse {
  const response = sectorKlineResponseSchema.parse(payload);
  let previousTradeDate: string | undefined;
  for (const [index, bar] of response.bars.entries()) {
    if (bar.trade_date > requestedEndDate) {
      throw new z.ZodError([{
        code: z.ZodIssueCode.custom,
        path: ["bars", index, "trade_date"],
        message: "交易日不能晚于请求截止日",
      }]);
    }
    if (previousTradeDate !== undefined && bar.trade_date <= previousTradeDate) {
      throw new z.ZodError([{
        code: z.ZodIssueCode.custom,
        path: ["bars", index, "trade_date"],
        message: "交易日必须严格升序且不能重复",
      }]);
    }
    previousTradeDate = bar.trade_date;
  }
  if (response.actual_end_date !== response.bars.at(-1)?.trade_date) {
    throw new z.ZodError([{
      code: z.ZodIssueCode.custom,
      path: ["actual_end_date"],
      message: "实际截止日必须等于最后一根 K 线交易日",
    }]);
  }
  if (response.meta.bar_count !== response.bars.length) {
    throw new z.ZodError([{
      code: z.ZodIssueCode.custom,
      path: ["meta", "bar_count"],
      message: "元数据条数必须与 bars 长度一致",
    }]);
  }
  return response;
}

/**
 * 读取指定板块在截止日或之前的合成日 K 线。
 *
 * 输入：板块名称、申万层级、工作台截止日和可选的取消信号。
 * 输出：经过严格运行时校验的升序 OHLCV、成交额与数据质量元信息。
 * 异常：接口错误抛出 ``SectorRotationApiError``；响应违反契约时抛出 ``ZodError``；取消时抛出浏览器 AbortError。
 */
export async function fetchSectorKline(
  sectorName: string,
  level: 1 | 2,
  endDate: string,
  signal?: AbortSignal,
): Promise<SectorKlineResponse> {
  const payload = await requestJson(
    "/api/v1/sector-rotation/sector-kline",
    { sector_name: sectorName, level, end_date: endDate },
    signal,
  );
  return parseSectorKlineResponse(payload, endDate);
}
