/** 选中行业的阶段解读、评分拆解和数据口径详情抽屉。*/
import { useEffect, useRef, useState } from "react";
import { ArrowDown, ArrowUp, X } from "lucide-react";
import { getPhaseMeta } from "../labels";
import { getLifecycleMeta, getLifecycleReasonLabel } from "../lifecycle/meta";
import { getCombinationConclusion } from "./combinationConclusion";
import { SectorKlineCard } from "../kline/SectorKlineCard";
import { DEFAULT_KLINE_WINDOW, type KlineWindow } from "../kline/sectorKlineConfig";
import { SectorKlineModal } from "../kline/SectorKlineModal";
import type { SectorKlineResponse } from "../kline/sectorKlineApi";
import { getIntensityMeta, getShortTermLabelMeta, orderLabelsByPriority, parseLabelsCsv } from "../short_term/labels";
import type { ShortTermSector } from "../short_term/api";
import { ShortTermStripView } from "./ShortTermStripView";
import { useShortTermHistory } from "./useShortTermHistory";
import { buildKlineModalSelectionIdentity, type DetailSector, type SectorDetailDrawerProps } from "./DetailSector";

// 重新导出以保持对上层 API 不破(测试 / 父页面都从此处引)。
export { buildKlineModalSelectionIdentity } from "./DetailSector";
export type { DetailSector, SectorDetailDrawerProps };

interface KlineModalSelection {
  /** 由行业名、行业层级和工作台日期确定的不可交换身份。*/
  identity: string;
  /** 板块行情卡已经加载并校验过的同一份响应。*/
  data: SectorKlineResponse;
}

/** 短期列中"收益与相对强度"的字段。*/
const RETURN_FIELDS: ReadonlyArray<{ field: string; label: string; format: "percent" | "slope" }> = [
  { field: "ret_1", label: "1 日绝对收益", format: "percent" },
  { field: "ret_2", label: "2 日累计收益", format: "percent" },
  { field: "rs_1", label: "1 日相对强度", format: "percent" },
  { field: "rs_2", label: "2 日累计相对强度", format: "percent" },
  { field: "rs5_accel_1d", label: "5 日强度 1 日变化", format: "percent" },
  { field: "ma5_slope", label: "MA5 日线斜率", format: "slope" },
];

/** 短期列中"个股层面广度"的字段。*/
const BREADTH_FIELDS: ReadonlyArray<{ field: string; label: string }> = [
  { field: "breadth_up", label: "上涨家数占比" },
  { field: "breadth_above_ma5", label: "站上 MA5 家数占比" },
  { field: "breadth_new_high_5", label: "5 日新高家数占比" },
  { field: "breadth_strong_1d", label: "单日强劲家数占比" },
  { field: "breadth_weak_1d", label: "单日弱势家数占比" },
  { field: "breadth_rvol_1d", label: "单日放量家数占比" },
  { field: "limit_up_ratio", label: "涨停家数占比" },
  { field: "limit_down_ratio", label: "跌停家数占比" },
];

function formatShortTermValue(field: string, v: number | null | undefined, format: "percent" | "slope"): string {
  if (v == null || Number.isNaN(v)) return "数据不足";
  if (format === "slope") return v.toFixed(4);
  return `${(v * 100).toFixed(1)}%`;
}

/** 短期命中列:展示 composite / rank / 强度 chip / 命中标签 chip / 收益 / 广度。*/
function ShortTermColumn({ shortTerm }: { shortTerm: ShortTermSector | null }) {
  if (!shortTerm) {
    return (
      <p className="short-term-empty" role="status">当日无短期评分,可在次日观察面板继续跟踪</p>
    );
  }
  const labels = orderLabelsByPriority(parseLabelsCsv(shortTerm.short_term_labels));
  const intensity = getIntensityMeta(shortTerm.short_term_intensity);
  return (
    <>
      <div className="short-term-summary">
        <div><span>短期综合分</span><strong>{shortTerm.short_term_composite?.toFixed(3) ?? "—"}</strong></div>
        <div><span>短期排名</span><strong>{shortTerm.short_term_composite_rank ?? "—"}</strong></div>
        <div>
          <span>强度</span>
          <span
            className="short-term-intensity-chip"
            style={{ background: intensity.softColor, color: intensity.color, borderColor: intensity.color }}
          >
            {intensity.label}
          </span>
        </div>
      </div>
      <section className="short-term-labels">
        <h4>命中标签</h4>
        {labels.length ? (
          <div>
            {labels.map((l) => {
              const meta = getShortTermLabelMeta(l);
              return (
                <span
                  key={l}
                  className="short-term-label-chip"
                  title={meta?.description ?? l}
                >
                  {meta?.label ?? l}
                </span>
              );
            })}
          </div>
        ) : (
          <em>无标签命中</em>
        )}
      </section>
      <section className="short-term-returns">
        <h4>收益与相对强度</h4>
        <dl>
          {RETURN_FIELDS.map((f) => {
            const value = shortTerm[f.field as keyof ShortTermSector] as number | null | undefined;
            return (
              <div key={f.field}>
                <dt>{f.label}</dt>
                <dd>{formatShortTermValue(f.field, value, f.format)}</dd>
              </div>
            );
          })}
        </dl>
      </section>
      <section className="short-term-breadth">
        <h4>个股层面广度</h4>
        <dl>
          {BREADTH_FIELDS.map((f) => {
            const value = shortTerm[f.field as keyof ShortTermSector] as number | null | undefined;
            return (
              <div key={f.field}>
                <dt>{f.label}</dt>
                <dd>{formatShortTermValue(f.field, value, "percent")}</dd>
              </div>
            );
          })}
        </dl>
      </section>
    </>
  );
}
/**
 * 展示单个行业的可解释深度研究详情。
 *
 * 输入:已选择行业的日志快照字段与关闭回调。
 * 输出:带明确关闭控件、阶段解读、分数组合和覆盖率提示的详情区域。
 */
export function SectorDetailDrawer({
  sector,
  shortTerm = null,
  previousLifecycleState,
  level,
  asOfDate,
  isLatestDate,
  onClose,
  onSelect,
}: SectorDetailDrawerProps) {
  const phase = sector.phase_confirmed ?? "neutral";
  const phaseMeta = getPhaseMeta(phase);
  const lifecycle = getLifecycleMeta(sector.lifecycle_state);
  const previousLifecycle = previousLifecycleState == null ? null : getLifecycleMeta(previousLifecycleState);
  const conclusion = getCombinationConclusion(phase, sector.lifecycle_state);
  const closeRef = useRef<HTMLButtonElement>(null);
  const expandButtonRef = useRef<HTMLButtonElement>(null);
  // 窗口状态由抽屉统一持有,使缩略图和后续弹窗可共享同一观察区间且不重新读取行情。
  const [visibleCount, setVisibleCount] = useState<KlineWindow>(DEFAULT_KLINE_WINDOW);
  // Modal 只保存缩略卡已加载的响应;不持有独立 Query,确保放大时不产生第二个网络请求。
  const [klineModalSelection, setKlineModalSelection] = useState<KlineModalSelection | null>(null);

  // 短期历史 strip 数据。
  const history = useShortTermHistory(level, asOfDate, sector.sector_name);

  const currentModalIdentity = buildKlineModalSelectionIdentity(sector.sector_name, level, asOfDate);
  // 渲染期同步比较可防止 React effect 执行前的一帧旧行情,不将旧响应交给新抽屉。
  const activeKlineModal = klineModalSelection?.identity === currentModalIdentity ? klineModalSelection : null;

  const scores: ReadonlyArray<readonly [string, number | null | undefined]> = [
    ["趋势位置", sector.trend_level_score],
    ["趋势速度", sector.velocity_score],
    ["趋势加速度", sector.acceleration_score],
    ["参与度", sector.participation_score],
    ["量能活跃度", sector.volume_score],
  ];

  useEffect(() => {
    // 仅在抽屉首次挂载或切换至另一板块/层级时做聚焦;Modal 状态变更不得抢占焦点。
    closeRef.current?.focus();
  }, [level, sector.sector_name]);

  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key !== "Escape") return;
      // 最内层行情弹窗优先消费 Escape;下一次 Escape 才能关闭外层详情抽屉。
      if (activeKlineModal) {
        setKlineModalSelection(null);
        return;
      }
      onClose();
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [activeKlineModal, onClose]);

  useEffect(() => {
    // 行业、层级或工作台日期切换时关闭旧行情,防止历史数据闪现到新抽屉。
    if (klineModalSelection && klineModalSelection.identity !== currentModalIdentity) setKlineModalSelection(null);
  }, [currentModalIdentity, klineModalSelection]);

  return (
    <div
      className="detail-layer"
      role="presentation"
      onMouseDown={(event) => {
        if (event.target === event.currentTarget) onClose();
      }}
    >
      <aside className="sector-detail" aria-label={`${sector.sector_name} 详情`}>
        <header className="detail-header">
          <div>
            <p>SECTOR INSIGHT</p>
            <h2>{sector.sector_name}</h2>
          </div>
          <button ref={closeRef} className="icon-button" type="button" aria-label="关闭详情" onClick={onClose}>
            <X aria-hidden="true" />
          </button>
        </header>
        <section className={`detail-combination-conclusion tone-${conclusion.tone}`} aria-label="组合研究结论">
          <p className="detail-combination-conclusion__eyebrow">组合研究结论</p>
          <h3>{conclusion.title}</h3>
          <p className="detail-combination-conclusion__guidance">{conclusion.guidance}</p>
          <div className="detail-combination-reason">
            <span>原因</span>
            <strong>{getLifecycleReasonLabel(sector.lifecycle_reason)}</strong>
          </div>
          <div className="detail-lifecycle-metrics">
            <div><span>持续天数</span><strong>{sector.lifecycle_age == null ? "数据不足" : `${sector.lifecycle_age} 日`}</strong></div>
            <div><span>今日变化</span><strong>{sector.lifecycle_changed == null ? "数据不足" : sector.lifecycle_changed ? "是" : "否"}</strong></div>
            <div><span>前态 → 当前态</span><strong>{previousLifecycle ? `${previousLifecycle.label} → ${lifecycle.label}` : "前一状态暂不可用"}</strong></div>
          </div>
          <p className="detail-combination-conclusion__notice">Lifecycle 为市场状态观察标签,不构成交易建议。</p>
        </section>
        <section className="detail-market-context" aria-label="板块行情信息">
          <p>板块行情</p>
          <strong>价格口径: 申万{level === 1 ? "一级" : "二级"}行业等权合成指数日线收盘价</strong>
          <span>截至日期: {asOfDate}</span>
        </section>
        <section className="detail-two-col" aria-label="短期命中与中长期观察">
          <div className="detail-col detail-col--short-term">
            <h3 className="detail-col__title">短期命中</h3>
            <ShortTermColumn shortTerm={shortTerm ?? null} />
          </div>
          <div className="detail-col detail-col--v1">
            <h3 className="detail-col__title">中长期观察</h3>
            <section className="score-breakdown">
              <div className="detail-section-title">
                <span>评分拆解</span>
                <small>-1 至 1 的当日截面相对得分</small>
              </div>
              <dl>
                {scores.map(([name, value]) => (
                  <div key={name as string}>
                    <dt>{name}</dt>
                    <dd>
                      <span className="score-track">
                        <i style={{ width: `${typeof value === "number" ? Math.max(0, Math.min(100, (value + 1) * 50)) : 0}%` }} />
                      </span>
                      <b>{typeof value === "number" ? value.toFixed(2) : "数据不足"}</b>
                    </dd>
                  </div>
                ))}
              </dl>
            </section>
            <section className="detail-metrics">
              <div className="detail-section-title"><span>排名与数据质量</span></div>
              <div>
                <span>单日排名变化</span>
                <strong>
                  {sector.rank_change_1d == null
                    ? "—"
                    : (
                      <>
                        {sector.rank_change_1d >= 0 ? <ArrowUp size={14} /> : <ArrowDown size={14} />}
                        {Math.abs(sector.rank_change_1d)}
                      </>
                    )}
                </strong>
              </div>
              <div>
                <span>数据覆盖率</span>
                <strong>{sector.coverage_ratio == null ? "数据不足" : `${(sector.coverage_ratio * 100).toFixed(0)}%`}</strong>
              </div>
              <div>
                <span>综合排名</span>
                <strong>{sector.composite_rank == null ? "—" : sector.composite_rank}</strong>
              </div>
            </section>
            <section className="detail-phase">
              <div className="detail-section-title"><span>阶段 / 置信度</span></div>
              <div><span>当前阶段</span><strong>{phaseMeta.label}</strong></div>
              <div><span>阶段置信度</span><strong>{sector.phase_confidence == null ? "数据不足" : sector.phase_confidence.toFixed(2)}</strong></div>
              <div><span>阶段持续天数</span><strong>{sector.phase_age == null ? "数据不足" : `${sector.phase_age} 日`}</strong></div>
            </section>
          </div>
        </section>
        <ShortTermStripView
          history={history.response}
          sectorName={sector.sector_name}
          asOfDate={asOfDate}
          isLoading={history.isLoading}
          isError={history.isError}
        />
        <SectorKlineCard
          sectorName={sector.sector_name}
          level={level}
          asOfDate={asOfDate}
          isLatestDate={isLatestDate}
          visibleCount={visibleCount}
          onVisibleCountChange={setVisibleCount}
          expandButtonRef={expandButtonRef}
          onExpand={(data) => setKlineModalSelection({ identity: currentModalIdentity, data })}
        />
        <footer className="detail-risk">模型阶段是研究观察信号,不代表未来收益;请结合自身风险承受能力独立判断。</footer>
      </aside>
      {activeKlineModal && (
        <SectorKlineModal
          key={activeKlineModal.identity}
          data={activeKlineModal.data}
          visibleCount={visibleCount}
          onVisibleCountChange={setVisibleCount}
          openerRef={expandButtonRef}
          phaseLabel={phaseMeta.label}
          onClose={() => setKlineModalSelection(null)}
        />
      )}
    </div>
  );
}