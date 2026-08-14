/** 板块轮动工作台中的“次日研究观察候选面板”：把同日短期异动标签归并为 4 个研究情景。 */
import { useEffect, useMemo, useState } from "react";
import {
  CornerDownLeft,
  CornerDownRight,
  Siren,
  TrendingUp,
} from "lucide-react";
import type { ShortTermSector } from "./api";
import {
  getNextDayWatchGroupMeta,
  getShortTermLabelMeta,
  orderLabelsByPriority,
  parseLabelsCsv,
  type NextDayWatchGroupMeta,
} from "./labels";
import {
  NEXT_DAY_WATCH_GROUP_ORDER,
  type NextDayWatchGroupId,
  buildNextDayWatchGroups,
} from "./nextDayWatch";
import { HintIcon } from "../HintIcon";

const ICON_COMPONENT = {
  "trending-up": TrendingUp,
  siren: Siren,
  "corner-down-left": CornerDownLeft,
  "corner-down-right": CornerDownRight,
} as const;

const PREVIEW_LIMIT = 5;

function formatScore(value: number | null | undefined): string | null {
  if (value == null || Number.isNaN(value)) return null;
  return value.toFixed(2);
}

function summarizeTopLabels(sector: ShortTermSector): string {
  const labels = orderLabelsByPriority(parseLabelsCsv(sector.short_term_labels));
  if (labels.length === 0) return "无标签";
  const first = labels[0];
  return getShortTermLabelMeta(first)?.label ?? first;
}

export interface NextDayWatchPanelProps {
  /** 同日的完整短期异动快照中的 sectors。组件只读，不修改也不缓存 sector 字段。 */
  sectors: ShortTermSector[];
  /** 点击候选板块时的回调；面板本身不维护详情抽屉状态。 */
  onSelect: (sectorName: string) => void;
}

/**
 * 把同日快照中已评分的板块映射为 4 张固定顺序的研究情景卡。
 *
 * 输入：与短期异动模块同日同层级的 sectors 列表、点击回调。
 * 输出：4 张卡片 + 默认折叠的展开按钮；切换 sectors 时通过 useEffect 重置展开状态。
 * 边界：所有候选均为“次日研究观察”，不提供买卖、仓位或收益判断。
 */
export function NextDayWatchPanel({ sectors, onSelect }: NextDayWatchPanelProps) {
  const groups = useMemo(() => buildNextDayWatchGroups(sectors), [sectors]);
  const [expanded, setExpanded] = useState<Record<string, boolean>>({});

  // 切换快照（日期 / 层级）时收起所有分组，避免上一日的展开状态被带入新快照。
  useEffect(() => {
    setExpanded({});
  }, [sectors]);

  return (
    <section className="next-day-watch" aria-label="次日研究观察候选">
      <header className="next-day-watch__header">
        <div>
          <p>NEXT-DAY WATCH</p>
          <h2>次日研究观察候选</h2>
        </div>
        <span className="next-day-watch__caption">
          基于当日完整有效快照，仅供研究观察，不构成投资建议。
        </span>
      </header>

      <div className="next-day-watch__grid" data-testid="next-day-watch-grid">
        {groups.map((group) => (
          <WatchGroupCard
            key={group.id}
            groupId={group.id}
            sectors={group.sectors}
            isExpanded={Boolean(expanded[group.id])}
            onToggleExpanded={() =>
              setExpanded((prev) => ({ ...prev, [group.id]: !prev[group.id] }))
            }
            onSelect={onSelect}
          />
        ))}
      </div>
    </section>
  );
}

interface WatchGroupCardProps {
  groupId: NextDayWatchGroupId;
  sectors: ShortTermSector[];
  isExpanded: boolean;
  onToggleExpanded: () => void;
  onSelect: (sectorName: string) => void;
}

function WatchGroupCard({ groupId, sectors, isExpanded, onToggleExpanded, onSelect }: WatchGroupCardProps) {
  const meta = getNextDayWatchGroupMeta(groupId) as NextDayWatchGroupMeta;
  const Icon = ICON_COMPONENT[meta.iconName] ?? TrendingUp;
  const visible = isExpanded ? sectors : sectors.slice(0, PREVIEW_LIMIT);
  const hasOverflow = sectors.length > PREVIEW_LIMIT;

  return (
    <article
      className="next-day-watch__card"
      data-tone={meta.tone}
      data-group={groupId}
      aria-label={`${meta.title}研究观察候选`}
    >
      <header className="next-day-watch__card-header">
        <div className="next-day-watch__card-title">
          <Icon aria-hidden="true" size={16} />
          <span>{meta.title}</span>
          <HintIcon text={meta.hint} tone="cool" placement="top" />
        </div>
        <span className="next-day-watch__card-count" aria-label={`命中 ${sectors.length} 个板块`}>
          {sectors.length}
        </span>
      </header>

      <p className="next-day-watch__card-description">{meta.description}</p>

      {visible.length === 0 ? (
        <p className="next-day-watch__card-empty">今日无此类信号</p>
      ) : (
        <ul className="next-day-watch__sector-list">
          {visible.map((sector) => {
            const scoreText = formatScore(sector.short_term_composite);
            const scoreLabel = scoreText ?? "综合分数据不足";
            return (
              <li key={sector.sector_name}>
                <button
                  type="button"
                  className="next-day-watch__sector-button"
                  onClick={() => onSelect(sector.sector_name)}
                  aria-label={`查看 ${sector.sector_name} 短期异动详情`}
                  title={`${sector.sector_name}｜${summarizeTopLabels(sector)}｜${scoreLabel}`}
                >
                  <span className="next-day-watch__sector-name">{sector.sector_name}</span>
                  <span className="next-day-watch__sector-meta">
                    <span className="next-day-watch__sector-label">{summarizeTopLabels(sector)}</span>
                    <span className="next-day-watch__sector-score">
                      {scoreText == null ? "数据不足" : scoreText}
                    </span>
                  </span>
                </button>
              </li>
            );
          })}
        </ul>
      )}

      {hasOverflow && (
        <button
          type="button"
          className="next-day-watch__toggle"
          onClick={onToggleExpanded}
          aria-expanded={isExpanded}
        >
          {isExpanded ? "收起" : `展开全部 ${sectors.length} 个`}
        </button>
      )}
    </article>
  );
}

/** 仅供测试使用，导出卡片展开折叠键常量以避免测试里魔法字符串。 */
export const __NEXT_DAY_WATCH_GROUP_ORDER_FOR_TEST = NEXT_DAY_WATCH_GROUP_ORDER;
