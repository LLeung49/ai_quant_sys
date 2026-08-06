/** 选中行业的阶段解释、评分证据和数据口径详情抽屉。 */
import { useEffect, useRef } from "react";
import { ArrowDown, ArrowUp, BarChart3, CalendarClock, ShieldAlert, X } from "lucide-react";
import { getPhaseMeta } from "../labels";

export interface DetailSector {
  sector_name: string; phase_confirmed: string | null; phase_age: number | null; phase_confidence: number | null;
  composite_rank: number | null; rank_change_1d: number | null; coverage_ratio: number | null;
  trend_level_score: number | null; velocity_score: number | null; acceleration_score: number | null;
  participation_score: number | null; volume_score: number | null;
}

interface SectorDetailDrawerProps { sector: DetailSector; onClose: () => void; }

/**
 * 展示单个板块的可解释研究详情。
 *
 * 输入：已选择行业的日快照字段与关闭回调。
 * 输出：带明确关闭控件、阶段解释、分数组成和覆盖率提示的详情区域。
 */
export function SectorDetailDrawer({ sector, onClose }: SectorDetailDrawerProps) {
  const phase = sector.phase_confirmed ?? "neutral";
  const phaseMeta = getPhaseMeta(phase);
  const closeRef = useRef<HTMLButtonElement>(null);
  const scores = [["趋势位置", sector.trend_level_score], ["趋势速度", sector.velocity_score], ["趋势加速度", sector.acceleration_score], ["参与度", sector.participation_score], ["量能活跃度", sector.volume_score]];
  useEffect(() => {
    closeRef.current?.focus();
    const handleKeyDown = (event: KeyboardEvent) => { if (event.key === "Escape") onClose(); };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [onClose]);

  return <div className="detail-layer" role="presentation" onMouseDown={(event) => { if (event.target === event.currentTarget) onClose(); }}>
    <aside className="sector-detail" aria-label={`${sector.sector_name} 详情`}>
      <header className="detail-header">
        <div><p>SECTOR INSIGHT</p><h2>{sector.sector_name}</h2></div>
        <button ref={closeRef} className="icon-button" type="button" aria-label="关闭详情" onClick={onClose}><X aria-hidden="true" /></button>
      </header>
      <section className="detail-conclusion" style={{ "--phase-color": phaseMeta.color, "--phase-soft": phaseMeta.softColor } as React.CSSProperties}>
        <span className="phase-pill">{phaseMeta.label}</span><p>{phaseMeta.description}</p>
      </section>
      <div className="detail-evidence">
        <article><CalendarClock aria-hidden="true" /><span>阶段持续</span><strong>{sector.phase_age ?? "—"} 日</strong></article>
        <article><BarChart3 aria-hidden="true" /><span>综合排名</span><strong>#{sector.composite_rank ?? "—"}</strong></article>
        <article><ShieldAlert aria-hidden="true" /><span>阶段置信度</span><strong>{sector.phase_confidence == null ? "—" : `${(sector.phase_confidence * 100).toFixed(0)}%`}</strong></article>
      </div>
      <section className="score-breakdown"><div className="detail-section-title"><span>评分拆解</span><small>-1 至 1 的当日截面相对得分</small></div>
        <dl>{scores.map(([name, value]) => <div key={name as string}><dt>{name}</dt><dd><span className="score-track"><i style={{ width: `${typeof value === "number" ? Math.max(0, Math.min(100, (value + 1) * 50)) : 0}%` }} /></span><b>{typeof value === "number" ? value.toFixed(2) : "数据不足"}</b></dd></div>)}</dl>
      </section>
      <section className="detail-metrics"><div className="detail-section-title"><span>排名与数据质量</span></div>
        <div><span>单日排名变化</span><strong>{sector.rank_change_1d == null ? "—" : <>{sector.rank_change_1d >= 0 ? <ArrowUp size={14} /> : <ArrowDown size={14} />}{Math.abs(sector.rank_change_1d)}</>}</strong></div>
        <div><span>数据覆盖率</span><strong>{sector.coverage_ratio == null ? "数据不足" : `${(sector.coverage_ratio * 100).toFixed(0)}%`}</strong></div>
      </section>
      <footer className="detail-risk">模型阶段是研究观察信号，不代表未来收益；请结合自身风险承受能力独立判断。</footer>
    </aside>
  </div>;
}
