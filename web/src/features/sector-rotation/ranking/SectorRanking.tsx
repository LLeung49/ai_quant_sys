/** 板块轮动主视图的今日关注行业排行榜。 */
import { ArrowDown, ArrowUp, Minus } from "lucide-react";
import { getPhaseMeta } from "../labels";

export interface RankingSector {
  sector_name: string;
  score_eligible: boolean;
  composite_rank: number | null;
  composite_score: number | null;
  phase_confirmed: string | null;
  rank_change_1d: number | null;
  phase_confidence?: number | null;
}

interface SectorRankingProps {
  /** 同日完整行业快照。 */
  sectors: RankingSector[];
  /** 输入：用户选择的行业名称；输出：由父页面同步图表与详情。 */
  onSelect: (sectorName: string) => void;
  /** 当前从图表或列表选中的行业名称。 */
  selectedSectorName?: string | null;
}

/**
 * 渲染按综合排名排序的可评分行业列表。
 *
 * 输入：行业快照和选择回调。
 * 输出：可键盘操作的行业按钮；无评分资格行业不会混入默认排名。
 */
export function SectorRanking({ sectors, onSelect, selectedSectorName }: SectorRankingProps) {
  const ranked = sectors.filter((sector) => sector.score_eligible).sort((left, right) => (left.composite_rank ?? Number.MAX_SAFE_INTEGER) - (right.composite_rank ?? Number.MAX_SAFE_INTEGER));
  return (
    <aside className="sector-ranking" aria-label="今日关注行业">
      <header className="panel-header ranking-header"><div><p>RANKING</p><h2>今日关注</h2></div><span>{ranked.length} 个有效行业</span></header>
      <div className="ranking-columns" aria-hidden="true"><span>排名 / 行业</span><span>阶段</span><span>得分</span><span>变化</span></div>
      <ol>{ranked.map((sector) => {
        const phase = getPhaseMeta(sector.phase_confirmed);
        const change = sector.rank_change_1d;
        return (
        <li key={sector.sector_name}>
          <button className={selectedSectorName === sector.sector_name ? "is-selected" : ""} type="button" onClick={() => onSelect(sector.sector_name)} aria-label={`查看 ${sector.sector_name} 详情`}>
            <span className="rank">{sector.composite_rank}</span><span className="sector-name">{sector.sector_name}</span>
            <small className="phase-pill" style={{ "--phase-color": phase.color, "--phase-soft": phase.softColor } as React.CSSProperties}>{phase.label}</small>
            <strong>{sector.composite_score?.toFixed(2) ?? "—"}</strong>
            <em className={change == null || change === 0 ? "rank-flat" : change > 0 ? "rank-up" : "rank-down"}>{change == null || change === 0 ? <Minus size={12} /> : change > 0 ? <ArrowUp size={12} /> : <ArrowDown size={12} />}{change == null ? "—" : Math.abs(change)}</em>
          </button>
        </li>
      );})}</ol>
    </aside>
  );
}
