import { useEffect, useMemo, useRef } from "react";
import type { ShortTermSector } from "./api";
import { getIntensityMeta, orderLabelsByPriority, parseLabelsCsv, getShortTermLabelMeta } from "./labels";
import { echarts } from "../chart/echarts";
interface Props { sectors: ShortTermSector[]; selectedSectorName?: string | null; onSelect: (name: string) => void; direction?: "up" | "down"; }
function hasAnomaly(s: ShortTermSector) { return Boolean(s.short_term_intensity && s.short_term_intensity !== "none") || parseLabelsCsv(s.short_term_labels).length > 0; }
function score(v: number | null | undefined) { return v == null ? "—" : v.toFixed(2); }
function colorFor(move: number, max: number, up: boolean) { const t = Math.min(1, Math.abs(move) / max); const light = up ? [246,180,188] : [169,225,202]; const dark = up ? [180,40,58] : [25,125,85]; return `rgb(${light.map((v,i)=>Math.round(v+(dark[i]-v)*t)).join(",")})`; }
export function ShortTermLeaders({ sectors, onSelect, direction }: Props) {
 const data=useMemo(()=>sectors.filter(s=>s.score_eligible&&hasAnomaly(s)).filter(s=>!direction||((s.ret_1??0)>=0)===(direction==="up")),[sectors,direction]); const ref=useRef<HTMLDivElement>(null);
 useEffect(()=>{ if(!ref.current)return; const chart=echarts.init(ref.current); const max=Math.max(...data.map(s=>Math.abs(s.ret_1??0)),0.01); const maxSize=Math.max(...data.map(s=>Math.abs(s.short_term_composite??0)),0.05); chart.setOption({animation:false,tooltip:{confine:true,formatter:(p:any)=>{const s=data.find(x=>x.sector_name===p.name) ?? data[p.dataIndex];const tags=orderLabelsByPriority(parseLabelsCsv(s.short_term_labels)).map(x=>getShortTermLabelMeta(x)?.label??x).join("、")||"无标签命中";return `<strong>${s.sector_name}</strong><br/>涨跌幅：${((s.ret_1??0)*100).toFixed(2)}%<br/>异动分：${score(s.short_term_composite)}<br/>强度：${getIntensityMeta(s.short_term_intensity).label}<br/>命中标签：${tags}`;}},series:[{type:"treemap",roam:false,nodeClick:false,breadcrumb:{show:false},data:data.map(s=>({name:s.sector_name,value:Math.max(Math.abs(s.short_term_composite??0),0.05),itemStyle:{color:colorFor(s.ret_1??0,max,(s.ret_1??0)>=0)},label:{show:true,overflow:"break",formatter:(p:any)=>{const ratio=Math.abs((p.value??0))/maxSize; const move=((s.ret_1??0)*100).toFixed(2); return ratio>0.22?`${s.sector_name}\n${(s.ret_1??0)>=0?"+":""}${move}%`:s.sector_name;},color:"#fff",fontSize:Math.round(10+5*Math.min(1,Math.sqrt(Math.abs(s.short_term_composite??0)/maxSize))),lineHeight:16}}))}]}); const click=(p:any)=>{const s=data.find(x=>x.sector_name===p.name) ?? data[p.dataIndex]; if(s) onSelect(s.sector_name);}; chart.on("click",click); const resize=()=>chart.resize(); window.addEventListener("resize",resize); return()=>{chart.off("click",click);window.removeEventListener("resize",resize);chart.dispose();};},[data,onSelect]);
 return <section className="short-term-leaders" aria-label={`${direction==="up"?"上涨":direction==="down"?"下跌":"异动"}热力图`}><header className="panel-header"><div><p>SHORT-TERM LEADERS</p><h2>{direction==="up"?"上涨异动":direction==="down"?"下跌异动":"异动热力图"}</h2></div></header>{data.length?(<><div ref={ref} className="short-term-leaders__chart"/><small className="short-term-leaders__count">{data.length} 个有效行业</small></>):<p className="short-term-leaders__empty">当日所有有效行业均无显著异动</p>}</section>;
}





