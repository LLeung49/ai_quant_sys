/** 板块详情抽屉中的日 K 线缩略卡：只负责查询状态外壳和缩略图入口。 */
import { Expand, RefreshCw } from "lucide-react";
import type { RefObject } from "react";
import { SectorRotationApiError } from "../api";
import { KlineErrorBoundary } from "./KlineErrorBoundary";
import { LazySectorKlineChart } from "./LazySectorKlineChart";
import { KLINE_WINDOWS, type KlineWindow } from "./sectorKlineConfig";
import { useSectorKline } from "./useSectorKline";
import type { SectorKlineResponse } from "./sectorKlineApi";

/** 板块行情缩略卡的输入属性。 */
export interface SectorKlineCardProps {
  /** 当前详情抽屉选中的板块名称。 */
  sectorName: string;
  /** 当前申万行业层级。 */
  level: 1 | 2;
  /** 工作台当前显示的交易日期，而非浏览器当天。 */
  asOfDate: string;
  /** 当前工作台日期是否为可用数据中的最新日期。 */
  isLatestDate: boolean;
  /** 由抽屉持有的当前可见交易日窗口。 */
  visibleCount: KlineWindow;
  /** 用户切换 60/120/250 日窗口时的回调。 */
  onVisibleCountChange: (visibleCount: KlineWindow) => void;
  /** 父级抽屉接收已加载 response 并打开放大 dialog，弹窗不得重新发起行情请求。 */
  onExpand: (data: SectorKlineResponse) => void;
  /** 放大按钮的焦点引用，供原生 dialog 关闭后恢复焦点。 */
  expandButtonRef?: RefObject<HTMLButtonElement | null>;
}

/**
 * 将后端价格口径转换为用户可读的中文说明。
 *
 * 输入：K 线接口的固定 ``price_basis`` 枚举值。
 * 输出：可在抽屉标题区域展示的中文数据口径。
 * 异常：未知口径返回原始值，避免接口新增枚举时将整个详情抽屉渲染失败。
 */
function getPriceBasisLabel(priceBasis: string): string {
  return priceBasis === "equal_weight_composite_index" ? "等权合成指数" : priceBasis;
}

/**
 * 渲染当前板块在工作台截止日之前的缩略 K 线、数据质量提示和局部失败状态。
 *
 * 输入：板块、层级、工作台日期、缓存新鲜度、窗口状态以及放大/窗口切换回调。
 * 输出：加载骨架、正常缩略三联图、空数据提示或可重试的局部错误区；不会影响抽屉其他内容。
 * 异常：HTTP、网络和图表初始化异常分别由 TanStack Query 与 ``KlineErrorBoundary`` 降级展示。
 */
export function SectorKlineCard({
  sectorName,
  level,
  asOfDate,
  isLatestDate,
  visibleCount,
  onVisibleCountChange,
  onExpand,
  expandButtonRef,
}: SectorKlineCardProps) {
  // 缩略图与后续弹窗共享同一 Query Key；窗口切换仅传给图表，不会重复请求 API。
  const query = useSectorKline({ sectorName, level, endDate: asOfDate, enabled: true, isLatestDate });

  if (query.isLoading) {
    return <section className="sector-kline-card sector-kline-card--loading" aria-label="正在加载板块行情">
      <div className="sector-kline-card__skeleton" />
      <div className="sector-kline-card__skeleton sector-kline-card__skeleton--short" />
    </section>;
  }

  if (query.isError) {
    const error = query.error;
    if (error instanceof SectorRotationApiError && error.code === "SECTOR_KLINE_NOT_FOUND") {
      return <section className="sector-kline-card sector-kline-card--empty">
        <h3>板块行情</h3>
        <p>该板块在指定日期前暂无有效行情</p>
      </section>;
    }
    const requestId = error instanceof SectorRotationApiError ? error.requestId : "unknown";
    return <section className="sector-kline-card sector-kline-card--error" role="alert">
      <h3>板块行情</h3>
      <p>读取板块行情失败，请稍后重试</p>
      <small>请求编号：{requestId}</small>
      <button type="button" onClick={() => void query.refetch()} aria-label="重试板块行情"><RefreshCw aria-hidden="true" size={13} />重试</button>
    </section>;
  }

  if (!query.data) return null;

  const { data } = query;
  const visibleBars = Math.min(visibleCount, data.meta.bar_count);
  const warmupUsed = Math.max(0, data.meta.bar_count - visibleBars);
  const warmupSufficient = warmupUsed >= data.meta.warmup_target;

  return <section className="sector-kline-card" aria-label={`${sectorName} 板块行情`}>
    <header className="sector-kline-card__header">
      <div>
        <h3>板块行情</h3>
        <p>截至 {data.actual_end_date} · {getPriceBasisLabel(data.price_basis)}</p>
      </div>
      <button ref={expandButtonRef} type="button" className="sector-kline-card__expand" onClick={() => onExpand(data)} aria-label={`放大查看${sectorName}行情`}>
        <Expand aria-hidden="true" size={14} />放大查看
      </button>
    </header>
    <div className="sector-kline-card__toolbar" aria-label="行情可见窗口">
      {KLINE_WINDOWS.map((windowValue) => <button
        key={windowValue}
        type="button"
        className={visibleCount === windowValue ? "is-active" : ""}
        aria-label={`显示最近 ${windowValue} 个交易日`}
        aria-pressed={visibleCount === windowValue}
        onClick={() => onVisibleCountChange(windowValue)}
      >{windowValue} 日</button>)}
    </div>
    {data.meta.skipped_bar_count > 0 && <p className="sector-kline-card__notice">有 {data.meta.skipped_bar_count} 个交易日行情异常已跳过</p>}
    {!warmupSufficient && <p className="sector-kline-card__notice">长期指标仍在形成</p>}
    <KlineErrorBoundary>
      <LazySectorKlineChart
        bars={data.bars}
        mode="compact"
        visibleCount={visibleCount}
        ariaLabel={`${sectorName} 截至 ${data.actual_end_date} 的日 K 线、成交量与 MACD 缩略图`}
      />
    </KlineErrorBoundary>
  </section>;
}
