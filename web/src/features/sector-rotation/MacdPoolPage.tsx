import { useQuery } from "@tanstack/react-query";
import { useEffect, useState } from "react";
import { requestJson } from "./api";
import { TradingCalendar } from "./filters/TradingCalendar";
import { MacdPoolChart } from "./MacdPoolChart";
type Row = {
  entity_type: string;
  stock_code: string;
  stock_name?: string | null;
  vol_ratio?: number | null;
  rsi_14?: number | null;
  adx_14?: number | null;
  kama_efficiency?: number | null;
  hurst_60?: number | null;
  change_pct?: number | null;
  macd_hist?: number | null;
  gc_label?: string | null;
};
const labels: Record<string, string> = {
  etf: "ETF",
  sector_l1: "申万一级板块",
  sector_l2: "申万二级板块",
};
function monthBounds(month: string) {
  const [year, value] = month.split("-").map(Number);
  const days = new Date(Date.UTC(year, value, 0)).getUTCDate();
  return {
    start: `${month}-01`,
    end: `${month}-${String(days).padStart(2, "0")}`,
  };
}

function trajectoryState(points?: Array<{ er: number | null; adx: number | null }>) {
  const valid = (points ?? []).filter((point) => point.er != null && point.adx != null);
  if (valid.length < 2) return "轨迹数据不足";
  const first = valid[0];
  const last = valid[valid.length - 1];
  const erDelta = (last.er as number) - (first.er as number);
  const adxDelta = (last.adx as number) - (first.adx as number);
  if (erDelta >= 0.05 && adxDelta >= 2) return "趋势强化";
  if (erDelta <= -0.05 && adxDelta <= -2) return "趋势走弱";
  if (erDelta >= 0.05 && adxDelta < 2) return "效率先行 / Emerging";
  if (erDelta < -0.05 && adxDelta >= 2) return "强度上升但变乱";
  return "结构迁移";
}
export function MacdPoolPage() {
  const datesQuery = useQuery({
    queryKey: ["macd-pool-dates"],
    queryFn: () =>
      requestJson("/api/v1/sector-rotation/macd-pool-dates", {
        level: 2,
        model_version: "v1",
      }) as Promise<{ dates: string[] }>,
  });
  const dates = datesQuery.data?.dates ?? [];
  const [selectedDate, setSelectedDate] = useState("");
  const date = selectedDate || dates[0] || "";
  const [month, setMonth] = useState(
    () => date.slice(0, 7) || new Date().toISOString().slice(0, 7),
  );
  useEffect(() => {
    if (date) setMonth(date.slice(0, 7));
  }, [date]);
  const bounds = monthBounds(month);
  const query = useQuery({
    queryKey: ["macd-pool", date],
    queryFn: () =>
      requestJson("/api/v1/sector-rotation/macd-pool", {
        as_of_date: date,
        level: 2,
        model_version: "v1",
      }) as Promise<{ groups: Record<string, Row[]> }>,
    enabled: Boolean(date),
  });
  const groups = query.data?.groups ?? {};
  const [selected, setSelected] = useState<Row | null>(null);
  const trajectoryQuery = useQuery({
    queryKey: [
      "macd-pool-trajectory",
      date,
      selected?.entity_type,
      selected?.stock_code,
    ],
    queryFn: () =>
      requestJson("/api/v1/sector-rotation/macd-pool-trajectory", {
        as_of_date: date,
        entity_type: selected!.entity_type,
        stock_code: selected!.stock_code,
        level: 2,
        model_version: "v1",
        days: 5,
      }) as Promise<{
        trajectory: {
          stock_code: string;
          points: Array<{
            as_of_date: string;
            er: number | null;
            adx: number | null;
          }>;
        };
      }>,
    enabled: Boolean(date && selected),
  });
  const allRows = Object.values(groups).flat();
  const chartPoints = allRows
    .filter((row) => row.kama_efficiency != null && row.adx_14 != null)
    .map((row) => ({
      name: row.stock_name || row.stock_code,
      code: row.stock_code,
      entityType: row.entity_type,
      er: Number(row.kama_efficiency),
      adx: Number(row.adx_14),
      volume: Number(row.vol_ratio ?? 1),
      momentum: Number(row.change_pct ?? 0),
      rsi: row.rsi_14,
      hurst: row.hurst_60,
      hist: row.macd_hist,
      gcAge: row.gc_label?.startsWith("T-") ? Number(row.gc_label.slice(2)) : null,
    }));
  const total = Object.values(groups).reduce(
    (count, rows) => count + rows.length,
    0,
  );
  return (
    <section className="rotation-page macd-pool-page" aria-label="MACD 标的池">
      <header className="panel-header">
        <div>
          <p>MACD POOL</p>
          <h2>MACD 标的池</h2>
        </div>
        <TradingCalendar
          displayedMonth={month}
          onDisplayedMonthChange={setMonth}
          tradeDates={dates.filter(
            (item) => item >= bounds.start && item <= bounds.end,
          )}
          snapshotDates={dates.filter(
            (item) => item >= bounds.start && item <= bounds.end,
          )}
          selectedDate={date}
          onDateChange={setSelectedDate}
        />
        <span>{query.isLoading ? "加载中…" : `命中 ${total} 个`}</span>
      </header>
      {query.isError ? (
        <div className="empty-panel">该日期暂无 MACD 板块池数据</div>
      ) : (
        <>
          {chartPoints.length > 0 && (
            <article className="content-panel">
              <h3>板块/ETF趋势质量</h3>
              <MacdPoolChart
                points={chartPoints}
                trajectory={trajectoryQuery.data?.trajectory}
                selectedCode={selected?.stock_code}
                stateLabel={selected && trajectoryQuery.data?.trajectory ? `${selected.stock_name || selected.stock_code}：${trajectoryState(trajectoryQuery.data.trajectory.points)}` : undefined}
                onSelect={(code) => setSelected(allRows.find((row) => row.stock_code === code) ?? null)}
              />
            </article>
          )}
          <div className="macd-ranking-grid">
          {Object.entries(labels).map(([key, label]) => (
            <article className="content-panel macd-ranking-panel" key={key}>
              <header className="panel-header ranking-header macd-ranking-header"><div><p>MACD POOL</p><h3>{label}</h3></div><span>{groups[key]?.length ?? 0} 个命中</span></header>
              {groups[key]?.length ? (
                <div className="macd-ranking">
                    {[...groups[key]]
                      .sort(
                        (a, b) =>
                          (b.adx_14 ?? 0) * (b.kama_efficiency ?? 0) -
                          (a.adx_14 ?? 0) * (a.kama_efficiency ?? 0),
                      )
                      .map((row, index) => (
                        <button
                          className={selected?.entity_type === row.entity_type && selected?.stock_code === row.stock_code ? "macd-ranking__row is-selected" : "macd-ranking__row"}
                          onClick={() => setSelected(row)}
                          key={`${key}-${row.stock_code}`}
                        >
                          <span className="macd-ranking__rank">{index + 1}</span><span className="macd-ranking__name">{row.stock_name || row.stock_code}<small>{row.stock_code}</small></span>
                          <span className="macd-ranking__phase">{row.gc_label ?? "—"}</span><strong>{((row.adx_14 ?? 0) * (row.kama_efficiency ?? 0)).toFixed(2)}</strong>
                          <span className="macd-ranking__metrics">ER {row.kama_efficiency?.toFixed(2) ?? "—"} · ADX {row.adx_14?.toFixed(1) ?? "—"} · 量比 {row.vol_ratio ?? "—"}</span>
                        </button>
                      ))}
                </div>
              ) : (
                <div className="macd-ranking-empty">暂无命中</div>
              )}
            </article>
          ))}
          </div>
        </>
      )}
    </section>
  );
}
