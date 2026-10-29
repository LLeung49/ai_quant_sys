import { useQuery } from "@tanstack/react-query";
import { X } from "lucide-react";
import { useEffect, useRef, useState } from "react";
import { z } from "zod";
import { requestJson } from "../api";
import { KlineErrorBoundary } from "../kline/KlineErrorBoundary";
import { LazySectorKlineChart } from "../kline/LazySectorKlineChart";
import { KLINE_WINDOWS, DEFAULT_KLINE_WINDOW, type KlineWindow } from "../kline/sectorKlineConfig";
import { fetchSectorKline } from "../kline/sectorKlineApi";

type MarketData = {
  actual_end_date: string;
  bars: Array<{ trade_date: string; timestamp: number; open: number; high: number; low: number; close: number; volume: number; amount: number }>;
  meta: { bar_count: number; skipped_bar_count: number; warmup_target: number };
};

const etfResponseSchema = z.object({
  stock_code: z.string(),
  actual_end_date: z.string(),
  bars: z.array(z.object({
    trade_date: z.string(), timestamp: z.number(), open: z.number(), high: z.number(),
    low: z.number(), close: z.number(), volume: z.number(), amount: z.number(),
  })).min(1),
  meta: z.object({ bar_count: z.number(), skipped_bar_count: z.number(), warmup_target: z.number() }),
});

interface MarketOnlyDrawerProps {
  name: string;
  code: string;
  entityType: string;
  asOfDate: string;
  onClose: () => void;
}

export function MarketOnlyDrawer({ name, code, entityType, asOfDate, onClose }: MarketOnlyDrawerProps) {
  const closeRef = useRef<HTMLButtonElement>(null);
  const [visibleCount, setVisibleCount] = useState<KlineWindow>(DEFAULT_KLINE_WINDOW);
  const isEtf = entityType === "etf";
  const level: 1 | 2 = entityType === "sector_l1" ? 1 : 2;
  const query = useQuery<MarketData>({
    queryKey: ["macd-market-kline", entityType, code, asOfDate],
    queryFn: ({ signal }): Promise<MarketData> => isEtf
      ? requestJson("/api/v1/sector-rotation/etf-kline", { stock_code: code, end_date: asOfDate }, signal).then((payload) => etfResponseSchema.parse(payload))
      : fetchSectorKline(code, level, asOfDate, signal),
    enabled: Boolean(asOfDate),
  });

  useEffect(() => { closeRef.current?.focus(); }, [code, entityType]);
  useEffect(() => {
    const handleEscape = (event: KeyboardEvent) => { if (event.key === "Escape") onClose(); };
    window.addEventListener("keydown", handleEscape);
    return () => window.removeEventListener("keydown", handleEscape);
  }, [onClose]);

  const title = isEtf ? "ETF 行情" : "板块行情";
  return <div className="detail-layer" role="presentation" onMouseDown={(event) => {
    if (event.target === event.currentTarget) onClose();
  }}>
    <aside className="sector-detail" aria-label={`${name} 详情`}>
      <header className="detail-header">
        <div><p>{isEtf ? "ETF MARKET" : "SECTOR MARKET"}</p><h2>{name}</h2></div>
        <button ref={closeRef} className="icon-button" type="button" aria-label="关闭详情" onClick={onClose}><X aria-hidden="true" /></button>
      </header>
      <section className="sector-kline-card" aria-label={`${name} ${title}`}>
        <header className="sector-kline-card__header"><div><h3>{title}</h3><p>{code} · {query.data ? `截至 ${query.data.actual_end_date}` : `截至 ${asOfDate}`} · {isEtf ? "前复权" : "等权合成指数"}</p></div></header>
        {query.isLoading && <p role="status">正在加载行情…</p>}
        {query.isError && <div role="alert"><p>行情暂不可用</p><button type="button" onClick={() => void query.refetch()}>重试</button></div>}
        {query.data && <>
          <div className="sector-kline-card__toolbar" aria-label="行情可见窗口">
            {KLINE_WINDOWS.map((value) => <button key={value} type="button" className={visibleCount === value ? "is-active" : ""} aria-label={`显示最近 ${value} 个交易日`} aria-pressed={visibleCount === value} onClick={() => setVisibleCount(value)}>{value} 日</button>)}
          </div>
          {query.data.meta.skipped_bar_count > 0 && <p className="sector-kline-card__notice">有 {query.data.meta.skipped_bar_count} 个交易日行情异常已跳过</p>}
          <KlineErrorBoundary><LazySectorKlineChart bars={query.data.bars} mode="compact" visibleCount={visibleCount} ariaLabel={`${name} 截至 ${query.data.actual_end_date} 的日 K 线、成交量与 MACD 缩略图`} /></KlineErrorBoundary>
        </>}
      </section>
    </aside>
  </div>;
}
