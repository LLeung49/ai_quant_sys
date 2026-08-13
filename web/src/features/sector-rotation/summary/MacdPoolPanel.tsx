import { useQuery } from "@tanstack/react-query";
import { requestJson } from "../api";

type Row = { entity_type: string; stock_code: string; stock_name?: string | null };
const labels: Record<string, string> = { etf: "ETF", sector_l1: "申万一级板块", sector_l2: "申万二级板块" };

export function MacdPoolPanel({ asOfDate, level }: { asOfDate: string; level: number }) {
  const query = useQuery({ queryKey: ["macd-pool", asOfDate, level], queryFn: () => requestJson("/api/v1/sector-rotation/macd-pool", { as_of_date: asOfDate, level, model_version: "v1" }) as Promise<{ groups: Record<string, Row[]> }> });
  if (query.isLoading) return <section className="content-panel"><p>MACD 板块池加载中…</p></section>;
  if (query.isError) return <section className="content-panel"><p>MACD 板块池暂不可用</p></section>;
  const groups = query.data?.groups ?? {};
  return <section className="content-panel" aria-label="MACD 板块池"><header className="panel-header"><div><p>MACD POOL</p><h2>MACD 板块池</h2></div></header>{Object.entries(labels).map(([key, label]) => <div key={key}><h3>{label}（{groups[key]?.length ?? 0}）</h3><div>{(groups[key] ?? []).map((row) => <span key={`${key}-${row.stock_code}`} style={{ marginRight: 8 }}>{row.stock_name || row.stock_code}</span>)}</div></div>)}</section>;
}
