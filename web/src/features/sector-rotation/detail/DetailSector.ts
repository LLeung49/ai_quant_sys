// 详情抽屉的输入类型聚合:把 v1 的字段与短期快照的字段都集中到一个文件,
// 便于 SectorDetailDrawer / useShortTermHistory / ShortTermStrip 共用。
//
// 类型约定:
// - DetailSector 列举所有 v1 详情抽屉需要的字段(明确、可读、与 api.ts 的 sectorPointSchema 解耦);
// - 短期数据通过 ShortTermSector 单字段传入,不强求合并到一个 union,
//   保持两个既有 schema 不变。
import type { LifecycleSectorFields } from "../lifecycle/meta";
import type { ShortTermSector } from "../short_term/api";

/** 详情抽屉内展示的 v1 字段集合。 */
export interface DetailSector extends LifecycleSectorFields {
  sector_name: string;
  as_of_date?: string;
  score_eligible?: boolean;
  phase_raw?: string | null;
  phase_confirmed: string | null;
  phase_age?: number | null;
  phase_confidence: number | null;
  composite_rank: number | null;
  composite_score?: number | null;
  rank_change_1d: number | null;
  top10_days_20?: number | null;
  coverage_ratio?: number | null;
  trend_level_score: number | null;
  velocity_score: number | null;
  acceleration_score: number | null;
  participation_score: number | null;
  volume_score: number | null;
}

export interface SectorDetailDrawerProps {
  sector: DetailSector;
  /** 同一行业在短期快照中的字段;null 表示当日未列入短期评分(周末 / 历史日等)。 */
  shortTerm?: ShortTermSector | null;
  /** 工作台截止日期前一交易日最近一次命中过的 Lifecycle 状态。 */
  previousLifecycleState?: string | null;
  level: 1 | 2;
  asOfDate: string;
  isLatestDate: boolean;
  onClose: () => void;
  /** 当短期列/Strip 的可点击标签或行业 chip 被选中时,联动上层选择。 */
  onSelect?: (sectorName: string) => void;
}


/**
 * 构建 modal 选择的稳定标识:三段式 `name|level|date`。
 *
 * 输入:行业名 / 行业层级 / 工作台截止日期。
 * 输出:用于 React modal 身份切换的稳定字符串,保证不会泄露给跨抽屉的回旧行情。
 * 异常:无;拼装过程为 O(1),不会跑飞。
 */
export function buildKlineModalSelectionIdentity(sectorName: string, level: 1 | 2, asOfDate: string): string {
  return "" + sectorName + "|" + level + "|" + asOfDate;
}
