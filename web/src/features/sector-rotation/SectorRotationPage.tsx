/** 板块轮动统一工作台的数据状态、回放帧与视图编排。 */
import { useEffect, useMemo, useReducer, useState } from "react";
import { CircleHelp, History, Pause, Play, Route } from "lucide-react";
import type { QuadrantSector } from "./chart/quadrantOption";
import { LazyQuadrantChart } from "./chart/LazyQuadrantChart";
import { SectorDetailDrawer, type DetailSector } from "./detail/SectorDetailDrawer";
import { RotationFilters } from "./filters/RotationFilters";
import { SectorRanking, type RankingSector } from "./ranking/SectorRanking";
import { MarketSummary } from "./summary/MarketSummary";
import { ShortTermAnomalyModule } from "./short_term/ShortTermAnomalyModule";
import { useRotationData } from "./useRotationData";
import { useReplayData } from "./useReplayData";
import { useHistoryData } from "./useHistoryData";
import { LazySectorTrajectory } from "./history/LazySectorTrajectory";
import { LifecycleBands } from "./history/LifecycleBands";
import { TrajectoryControls } from "./history/TrajectoryControls";
import { findHistoryGaps } from "./history/historyGaps";
import { addTrajectorySector } from "./history/constants";
import { PHASE_META } from "./labels";
import { ReplayControls } from "./replay/ReplayControls";
import { initialReplayState, replayReducer } from "./replay/replayState";
import { buildSectorTrail } from "./replay/sectorTrail";
import { buildReplayFrames } from "./workbench/frameState";
import { parseWorkbenchUrl, serializeWorkbenchUrl, type LabelDensity, type WorkbenchMode } from "./workbench/urlState";
import { findPreviousLifecycle, hasLifecycleCoverage, matchesLifecycleFilter } from "./lifecycle/derive";
import type { LifecycleFilter } from "./lifecycle/meta";
import type { SectorPoint } from "./api";
import { useShortTermHaloSectors } from "./short_term/useShortTermHaloSectors";
import { buildShortTermHaloIndex } from "./chart/shortTermHalo";
import { SHORT_TERM_LABEL_DIRECTION_COLOR } from "./chart/shortTermHalo";
import type { ShortTermHaloInfo } from "./chart/shortTermHalo";
import type { ShortTermSector } from "./short_term/api";

type DisplaySector = SectorPoint & QuadrantSector & RankingSector & DetailSector & {
  as_of_date: string;
  market_regime?: string;
  regime_multiplier?: number | null;
};

const OBSERVATION_FOCUSES: Array<{ label: string; lifecycle: LifecycleFilter; changedOnly: boolean }> = [
  { label: "全部", lifecycle: "all", changedOnly: false },
  { label: "趋势", lifecycle: "trending", changedOnly: false },
  { label: "修复/初启", lifecycle: "repair_or_emerging", changedOnly: false },
  { label: "风险提示", lifecycle: "risk", changedOnly: false },
  { label: "今日 Lifecycle 变化", lifecycle: "all", changedOnly: true },
];

function LifecycleFilterReset({ lifecycleAvailable, lifecycleFilter, changedOnly, onLifecycleChange, onChangedOnlyChange }: {
  lifecycleAvailable: boolean;
  lifecycleFilter: LifecycleFilter;
  changedOnly: boolean;
  onLifecycleChange: (filter: LifecycleFilter) => void;
  onChangedOnlyChange: (changedOnly: boolean) => void;
}) {
  useEffect(() => {
    if (lifecycleAvailable) return;
    if (lifecycleFilter !== "all") onLifecycleChange("all");
    if (changedOnly) onChangedOnlyChange(false);
  }, [changedOnly, lifecycleAvailable, lifecycleFilter, onChangedOnlyChange, onLifecycleChange]);
  return null;
}

/**
 * 渲染单日观察与动态回放共用的板块轮动工作台。
 *
 * 输入：无；状态来自 URL、只读 API 和用户交互。
 * 输出：同一展示日期驱动的市场摘要、象限图、排行榜、详情与历史轨迹。
 */
export function SectorRotationPage() {
  const [initialUrl] = useState(() => parseWorkbenchUrl(window.location.search));
  const [level, setLevel] = useState<1 | 2>(initialUrl.level);
  const [selectedDate, setSelectedDate] = useState<string | undefined>(initialUrl.date);
  const [selectedSectorName, setSelectedSectorName] = useState<string | null>(initialUrl.sector);
  const [comparisonSectors, setComparisonSectors] = useState<string[]>(initialUrl.sector ? [initialUrl.sector] : []);
  const [searchQuery, setSearchQuery] = useState(initialUrl.query);
  const [phaseFilter, setPhaseFilter] = useState(initialUrl.phase);
  const [lifecycleFilter, setLifecycleFilter] = useState<LifecycleFilter>(initialUrl.lifecycle);
  const [changedOnly, setChangedOnly] = useState(initialUrl.changedOnly);
  const [mode, setMode] = useState<WorkbenchMode>(initialUrl.mode);
  const [labelDensity, setLabelDensity] = useState<LabelDensity>(initialUrl.labelDensity);
  const [historyWindow, setHistoryWindow] = useState<5 | 20 | 60>(initialUrl.historyWindow);
  const { dates, snapshot, loadedSnapshotDate } = useRotationData(level, "v1", selectedDate);
  const replay = useReplayData(dates.data ?? [], level, "v1");
  const replayPoints = (replay.data ?? []) as unknown as DisplaySector[];
  const replayFrames = useMemo(() => buildReplayFrames<DisplaySector>(replayPoints), [replay.data]);
  const [replayState, replayDispatch] = useReducer(replayReducer, [], initialReplayState);
  const history = useHistoryData(comparisonSectors, dates.data ?? [], level, "v1");

  useEffect(() => {
    if (replayFrames.dates.length > 0) replayDispatch({ type: "LOAD_DATES", dates: replayFrames.dates, preferredDate: initialUrl.date ?? selectedDate });
  }, [replayFrames.dates.join("|")]);

  useEffect(() => {
    if (!replayState.playing) return undefined;
    const timer = window.setInterval(() => replayDispatch({ type: "NEXT" }), 900 / replayState.speed);
    return () => window.clearInterval(timer);
  }, [replayState.playing, replayState.speed]);

  const replayDate = replayState.dates[replayState.index];
  const displayDate = mode === "replay" ? replayDate : loadedSnapshotDate;
  const urlDate = mode === "replay" ? displayDate : selectedDate;

  const haloQuery = useShortTermHaloSectors(level, displayDate);
  const shortTermHaloByName = useMemo<ReadonlyMap<string, ShortTermHaloInfo>>(
    () => (mode === "snapshot" && !haloQuery.isLoading ? buildShortTermHaloIndex(haloQuery.sectors) : new Map()),
    [mode, haloQuery.isLoading, haloQuery.sectors],
  );

  useEffect(() => {
    const nextSearch = serializeWorkbenchUrl({ date: urlDate, level, mode, phase: phaseFilter, query: searchQuery, sector: selectedSectorName, historyWindow, labelDensity, lifecycle: lifecycleFilter, changedOnly });
    window.history.replaceState(null, "", `${window.location.pathname}${nextSearch}`);
  }, [changedOnly, historyWindow, labelDensity, level, lifecycleFilter, mode, phaseFilter, searchQuery, selectedSectorName, urlDate]);

  useEffect(() => {
    if (!selectedSectorName) return;
    setComparisonSectors((current) => addTrajectorySector(current, selectedSectorName));
  }, [selectedSectorName]);

  /**
   * 选中行业在 v2_short_term 快照中的完整字段,用于主工作台抽屉透出"短期命中"。
   * 与 ShortTermAnomalyModule / 象限图光晕共用同一份 haloQuery,
   * 二次点击走 TanStack Query 缓存,无额外请求。
   * 在 replay 模式下 haloQuery 仍然按当前 displayDate(= replayDate)查询,
   * 因此短期命中列对应的就是抽屉顶部标注的 asOfDate,语义与 v1 列保持一致。
   * 必须位于下方三个 loading 早返 early return 之前,避免加载 / 失败分支中 React 调用 hooks 顺序不一致。
   */
  const selectedShortTerm = useMemo<ShortTermSector | null>(() => {
    if (!selectedSectorName) return null;
    if (haloQuery.isLoading || haloQuery.isError) return null;
    return haloQuery.sectors.find((sector) => sector.sector_name === selectedSectorName) ?? null;
  }, [haloQuery.sectors, haloQuery.isLoading, haloQuery.isError, selectedSectorName]);

  if (dates.isLoading || (mode === "snapshot" && snapshot.isLoading)) return <section className="loading-panel" aria-live="polite">正在加载最新板块快照…</section>;
  if (dates.isError || (mode === "snapshot" && snapshot.isError)) return <section className="loading-panel" role="alert">读取板块轮动数据失败，请稍后重试或检查 API 服务。</section>;
  if (mode === "snapshot" && !snapshot.data) return <section className="loading-panel">当前层级尚无已成功运行的板块快照。</section>;

  // 回放视图不读取任何 snapshot 响应字段；快照查询即使仍在后台执行，也不得影响回放展示。
  const snapshotSectors = mode === "snapshot" ? (snapshot.data?.sectors ?? []) as unknown as DisplaySector[] : [];
  const replayFrame = replayDate ? replayFrames.byDate[replayDate] ?? [] : [];
  const replayUnavailable = mode === "replay" && replayFrame.length === 0;
  // 回放模式只可信任当前帧；帧缺失时宁可展示空态，也不能泄漏最新快照。
  const sectors = mode === "replay" ? replayFrame : snapshotSectors;
  const lifecycleAvailable = hasLifecycleCoverage(sectors);
  const filteredSectors = sectors.filter((sector) => {
    const matchesSearch = !searchQuery.trim() || sector.sector_name.includes(searchQuery.trim());
    const matchesPhase = phaseFilter === "all" || sector.phase_confirmed === phaseFilter;
    const matchesLifecycle = !lifecycleAvailable || matchesLifecycleFilter(sector, lifecycleFilter, changedOnly);
    return matchesSearch && matchesPhase && matchesLifecycle;
  });
  const selected = mode === "replay"
    ? replayFrame.find((sector) => sector.sector_name === selectedSectorName)
    : snapshotSectors.find((sector) => sector.sector_name === selectedSectorName);
  const trail = mode === "replay" ? buildSectorTrail(replayPoints, selectedSectorName, replayDate ?? "", 10) : [];
  const historyPoints = (history.data ?? []).map((point: SectorPoint) => ({
    as_of_date: point.as_of_date ?? "",
    sector_name: point.sector_name,
    velocity_score: typeof point.velocity_score === "number" ? point.velocity_score : null,
    acceleration_score: typeof point.acceleration_score === "number" ? point.acceleration_score : null,
    lifecycle_state: point.lifecycle_state,
    lifecycle_reason: point.lifecycle_reason,
    lifecycle_changed: point.lifecycle_changed,
    lifecycle_age: point.lifecycle_age,
  }));
  const historyDates = [...(dates.data ?? [])].sort().slice(-historyWindow);
  const visibleHistoryDates = displayDate ? historyDates.filter((date) => date <= displayDate) : [];
  const lifecycleHistoryPoints = displayDate ? historyPoints.filter((point) => point.as_of_date <= displayDate) : [];
  const previousLifecycleState = selected && displayDate
    ? findPreviousLifecycle(lifecycleHistoryPoints, selected.sector_name, displayDate)?.lifecycle_state
    : undefined;
  const trajectories = comparisonSectors.map((sectorName) => ({
    sector_name: sectorName,
    points: visibleHistoryDates.map((date) => historyPoints.find((point) => point.sector_name === sectorName && point.as_of_date === date) ?? { as_of_date: date, velocity_score: null, acceleration_score: null }),
  }));
  const historyGaps = findHistoryGaps(visibleHistoryDates, comparisonSectors, historyPoints);
  const sourceCutoff = mode === "replay" ? displayDate ?? "暂无可用回放日期" : snapshot.data?.meta.source_max_trade_date ?? "待确认";

  const handleDateChange = (date: string) => {
    if (mode === "replay") {
      const index = replayState.dates.indexOf(date);
      if (index >= 0) replayDispatch({ type: "SEEK", index });
      return;
    }
    setSelectedDate(date);
  };

  const handleModeChange = (nextMode: WorkbenchMode) => {
    setMode(nextMode);
    replayDispatch({ type: "PAUSE" });
    if (nextMode === "replay") {
      const preferred = replayState.dates.indexOf(loadedSnapshotDate ?? "");
      replayDispatch({ type: "SEEK", index: preferred >= 0 ? preferred : Math.max(0, replayState.dates.length - 1) });
    }
  };

  return <div className="rotation-page">
    <RotationFilters dates={mode === "replay" ? [...replayState.dates].reverse() : dates.data ?? []} selectedDate={mode === "replay" ? displayDate ?? "" : selectedDate ?? loadedSnapshotDate ?? ""} level={level} modelVersion="v1" onDateChange={handleDateChange} onLevelChange={(nextLevel) => { setLevel(nextLevel); setSelectedDate(undefined); setSelectedSectorName(null); setComparisonSectors([]); setMode("snapshot"); }} searchQuery={searchQuery} phaseFilter={phaseFilter} onSearchChange={setSearchQuery} onPhaseChange={setPhaseFilter} lifecycleFilter={lifecycleFilter} changedOnly={changedOnly} lifecycleDisabled={!lifecycleAvailable} onLifecycleChange={setLifecycleFilter} onChangedOnlyChange={setChangedOnly} />
    {mode === "snapshot" && selectedDate && loadedSnapshotDate && selectedDate !== loadedSnapshotDate && <p role="status">{selectedDate} 的板块轮动快照尚未生成，当前展示 {loadedSnapshotDate} 的最近成功快照。</p>}
    <MarketSummary marketRegime={sectors[0]?.market_regime ?? "range"} />
    {mode === "snapshot" && displayDate && <ShortTermAnomalyModule level={level} asOfDate={displayDate} availableDates={dates.data} />}

    <LifecycleFilterReset lifecycleAvailable={lifecycleAvailable} lifecycleFilter={lifecycleFilter} changedOnly={changedOnly} onLifecycleChange={setLifecycleFilter} onChangedOnlyChange={setChangedOnly} />
    <section className="rotation-workspace">
      <article className="chart-panel">
        <header className="panel-header">
          <div><p>ROTATION WORKBENCH · {displayDate} · 数据源截止 {sourceCutoff}</p><h2>行业轮动象限</h2></div>
          <div className="chart-actions">
            <div className="segmented-control workbench-mode" aria-label="象限图模式"><button className={mode === "snapshot" ? "is-active" : ""} type="button" onClick={() => handleModeChange("snapshot")}>单日观察</button><button className={mode === "replay" ? "is-active" : ""} type="button" onClick={() => handleModeChange("replay")}>{mode === "replay" && replayState.playing ? <Pause size={12} /> : <Play size={12} />}动态回放</button></div>
            <div className="observation-focus-wrap">
              <div className="segmented-control observation-focus" role="group" aria-label="观察重点">
                {OBSERVATION_FOCUSES.map((focus) => {
                  const isAll = focus.lifecycle === "all" && !focus.changedOnly;
                  const isActive = lifecycleAvailable
                    ? lifecycleFilter === focus.lifecycle && changedOnly === focus.changedOnly
                    : isAll;
                  return <button key={focus.label} className={isActive ? "is-active" : ""} type="button" aria-pressed={isActive} disabled={!lifecycleAvailable && !isAll} onClick={() => { setLifecycleFilter(focus.lifecycle); setChangedOnly(focus.changedOnly); }}>{focus.label}</button>;
                })}
              </div>
              {!lifecycleAvailable && <p className="observation-focus-note">该快照缺少 Lifecycle 数据，暂不能筛选观察重点。</p>}
            </div>
            <button className="method-link" type="button" title="横轴为趋势速度，纵轴为趋势加速度；分数均为当日行业截面相对值"><CircleHelp aria-hidden="true" size={15} />如何阅读</button>
          </div>
        </header>
        <div className="chart-subtoolbar">
          <div className="phase-legend">{Object.entries(PHASE_META).filter(([key]) => key !== "neutral").map(([key, meta]) => <span key={key}><i style={{ background: meta.color }} />{meta.label}</span>)}</div>
          <label className="label-density"><span>标注密度</span><select value={labelDensity} onChange={(event) => setLabelDensity(event.target.value as LabelDensity)}><option value="compact">精简</option><option value="focus">关注</option><option value="all">全部</option></select></label>
        </div>
        {mode === "snapshot" && (
          <div className="quadrant-anomaly-legend" role="group" aria-label="短期异动信号图例">
            <span className="quadrant-anomaly-legend__title">短期异动方向</span>
            {([
              { key: "up",        label: "涨红",     swatch: SHORT_TERM_LABEL_DIRECTION_COLOR.pulse_up },
              { key: "down",      label: "跌绿",     swatch: SHORT_TERM_LABEL_DIRECTION_COLOR.pulse_down },
              { key: "volume",    label: "量能",     swatch: SHORT_TERM_LABEL_DIRECTION_COLOR.volume_spike },
              { key: "rebound",   label: "反弹",     swatch: SHORT_TERM_LABEL_DIRECTION_COLOR.short_rebound_candidate },
              { key: "breakdown", label: "破位",     swatch: SHORT_TERM_LABEL_DIRECTION_COLOR.short_breakdown_candidate },
            ] as const).map((entry) => (
              <span key={entry.key} className="quadrant-anomaly-legend__item" data-tone={entry.key}>
                <i style={{ background: entry.swatch }} aria-hidden="true" />
                <span>{entry.label}</span>
              </span>
            ))}
            <span className="quadrant-anomaly-legend__divider" aria-hidden="true">强度</span>
            {([
              // 强度档演示色与 INTENSITY_META 完全对齐,保证图例颜色与抽屉 / KPI / 候选情景里的 chip 一致。
              // alpha 区分强 / 中 / 弱:实色 = 强,0.86 = 中,0.66 = 弱。
              { key: "intense",   label: "强异动",   swatch: "rgba(255, 107, 53, 1)" },
              { key: "moderate",  label: "中等异动", swatch: "rgba(240, 182, 90, 0.86)" },
              { key: "mild",      label: "轻度异动", swatch: "rgba(103, 195, 162, 0.66)" },
            ] as const).map((entry) => (
              <span key={entry.key} className="quadrant-anomaly-legend__item" data-tone={`intensity-${entry.key}`}>
                <i style={{ background: entry.swatch }} aria-hidden="true" />
                <span>{entry.label}</span>
              </span>
            ))}
            <span className="quadrant-anomaly-legend__hint">当日命中短期标签的行业在右上角展示主标签形状；颜色按方向(涨红/跌绿/量能/反弹/破位)区分,透明度与形状大小随强度递减。</span>
          </div>
        )}
        {mode === "replay" && <ReplayControls dates={replayState.dates} index={replayState.index} playing={replayState.playing} speed={replayState.speed} dispatch={replayDispatch} />}
        {replayUnavailable
          ? <div className="empty-panel" role="status">{replay.isLoading ? "回放数据加载中" : "回放数据暂不可用"}</div>
          : filteredSectors.length > 0
            ? <LazyQuadrantChart sectors={filteredSectors} selectedSectorName={selectedSectorName} onSelect={setSelectedSectorName} labelDensity={labelDensity} trail={trail} shortTermHaloByName={mode === "snapshot" ? shortTermHaloByName : undefined} />
            : <div className="empty-panel">当前筛选条件下没有可展示行业</div>}
        <footer className="chart-note"><span>气泡大小：量能活跃度</span><span>透明度：阶段置信度</span><span>描边：行业内部参与度</span>{mode === "replay" && selectedSectorName && <span className="trail-note"><Route size={11} />虚线：{selectedSectorName} 近10日尾迹</span>}<span>坐标分数不是收益率</span></footer>
      </article>
      <SectorRanking sectors={filteredSectors} selectedSectorName={selectedSectorName} onSelect={setSelectedSectorName} />
    </section>
    {selected && displayDate && <SectorDetailDrawer
      sector={selected}
      shortTerm={selectedShortTerm}
      level={level}
      asOfDate={displayDate}
      isLatestDate={displayDate === dates.data?.[0]}
      previousLifecycleState={previousLifecycleState}
      onClose={() => setSelectedSectorName(null)}
    />}
    {comparisonSectors.length > 0 && <section className="sector-history content-panel"><header className="panel-header"><div><p>SECTOR TRAJECTORY</p><h2><History aria-hidden="true" />行业轨迹对比</h2></div><div className="segmented-control">{([5, 20, 60] as const).map((windowValue) => <button className={historyWindow === windowValue ? "is-active" : ""} key={windowValue} type="button" onClick={() => setHistoryWindow(windowValue)}>{windowValue} 日</button>)}</div></header><TrajectoryControls sectorNames={comparisonSectors} onRemove={(sectorName) => { setComparisonSectors((current) => current.filter((item) => item !== sectorName)); if (selectedSectorName === sectorName) setSelectedSectorName(null); }} />{history.isLoading ? <div className="trajectory-loading">正在加载行业历史轨迹…</div> : history.isError ? <div className="history-error" role="status">历史轨迹暂不可用，当前快照保持可用。</div> : <><LazySectorTrajectory trajectories={trajectories} /><LifecycleBands sectorNames={comparisonSectors.slice(0, 5)} points={lifecycleHistoryPoints} expectedDates={visibleHistoryDates} /></>}{!history.isError && historyGaps.length > 0 && <div className="history-gaps"><strong>数据缺口</strong>{historyGaps.map((gap) => <span key={gap.sector_name}>{gap.sector_name}：{gap.dates.length} 个交易日缺少有效坐标（轨迹已断开）</span>)}</div>}</section>}
  </div>;
}

