/** 板块轮动统一工作台的数据状态、回放帧与视图编排。 */
import { useEffect, useMemo, useReducer, useState } from "react";
import { CircleHelp, History, Pause, Play, Route } from "lucide-react";
import type { QuadrantSector } from "./chart/quadrantOption";
import { LazyQuadrantChart } from "./chart/LazyQuadrantChart";
import { SectorDetailDrawer, type DetailSector } from "./detail/SectorDetailDrawer";
import { RotationFilters } from "./filters/RotationFilters";
import { SectorRanking, type RankingSector } from "./ranking/SectorRanking";
import { MarketSummary } from "./summary/MarketSummary";
import { useRotationData } from "./useRotationData";
import { useReplayData } from "./useReplayData";
import { useHistoryData } from "./useHistoryData";
import { LazySectorTrajectory } from "./history/LazySectorTrajectory";
import { TrajectoryControls } from "./history/TrajectoryControls";
import { findHistoryGaps } from "./history/historyGaps";
import { addTrajectorySector } from "./history/constants";
import { PHASE_META } from "./labels";
import { ReplayControls } from "./replay/ReplayControls";
import { initialReplayState, replayReducer } from "./replay/replayState";
import { buildSectorTrail } from "./replay/sectorTrail";
import { buildReplayFrames } from "./workbench/frameState";
import { parseWorkbenchUrl, serializeWorkbenchUrl, type LabelDensity, type WorkbenchMode } from "./workbench/urlState";

type DisplaySector = QuadrantSector & RankingSector & DetailSector & {
  as_of_date: string;
  market_regime?: string;
  regime_multiplier?: number | null;
};

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
  const [mode, setMode] = useState<WorkbenchMode>(initialUrl.mode);
  const [labelDensity, setLabelDensity] = useState<LabelDensity>(initialUrl.labelDensity);
  const [historyWindow, setHistoryWindow] = useState<5 | 20 | 60>(initialUrl.historyWindow);
  const { dates, snapshot, latestDate } = useRotationData(level, "v1", selectedDate);
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
  const displayDate = mode === "replay" ? replayDate : latestDate;

  useEffect(() => {
    const nextSearch = serializeWorkbenchUrl({ date: displayDate, level, mode, phase: phaseFilter, query: searchQuery, sector: selectedSectorName, historyWindow, labelDensity });
    window.history.replaceState(null, "", `${window.location.pathname}${nextSearch}`);
  }, [displayDate, historyWindow, labelDensity, level, mode, phaseFilter, searchQuery, selectedSectorName]);

  useEffect(() => {
    if (selectedDate && !dates.data?.includes(selectedDate)) setSelectedDate(undefined);
  }, [dates.data, selectedDate]);

  useEffect(() => {
    if (!selectedSectorName) return;
    setComparisonSectors((current) => addTrajectorySector(current, selectedSectorName));
  }, [selectedSectorName]);

  if (dates.isLoading || snapshot.isLoading) return <section className="loading-panel" aria-live="polite">正在加载最新板块快照…</section>;
  if (dates.isError || snapshot.isError) return <section className="loading-panel" role="alert">读取板块轮动数据失败，请稍后重试或检查 API 服务。</section>;
  if (!snapshot.data) return <section className="loading-panel">当前层级尚无已成功运行的板块快照。</section>;

  const snapshotSectors = snapshot.data.sectors as unknown as DisplaySector[];
  const replayFrame = replayDate ? replayFrames.byDate[replayDate] ?? [] : [];
  const sectors = mode === "replay" && replayFrame.length > 0 ? replayFrame : snapshotSectors;
  const filteredSectors = sectors.filter((sector) => {
    const matchesSearch = !searchQuery.trim() || sector.sector_name.includes(searchQuery.trim());
    const matchesPhase = phaseFilter === "all" || sector.phase_confirmed === phaseFilter;
    return matchesSearch && matchesPhase;
  });
  const eligible = sectors.filter((sector) => Boolean(sector.score_eligible)).length;
  const accelerating = sectors.filter((sector) => sector.phase_confirmed === "accel_up").length;
  const risk = sectors.filter((sector) => sector.phase_confirmed === "accel_down" || sector.phase_confirmed === "decel_up").length;
  const selected = sectors.find((sector) => sector.sector_name === selectedSectorName) ?? snapshotSectors.find((sector) => sector.sector_name === selectedSectorName);
  const trail = mode === "replay" ? buildSectorTrail(replayPoints, selectedSectorName, replayDate ?? "", 10) : [];
  const historyPoints = (history.data ?? []) as { as_of_date: string; sector_name: string; velocity_score: number | null; acceleration_score: number | null }[];
  const historyDates = [...(dates.data ?? [])].sort().slice(-historyWindow);
  const trajectories = comparisonSectors.map((sectorName) => ({
    sector_name: sectorName,
    points: historyDates.map((date) => historyPoints.find((point) => point.sector_name === sectorName && point.as_of_date === date) ?? { as_of_date: date, velocity_score: null, acceleration_score: null }),
  }));
  const historyGaps = findHistoryGaps(historyDates, comparisonSectors, historyPoints);

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
      const preferred = replayState.dates.indexOf(latestDate ?? "");
      replayDispatch({ type: "SEEK", index: preferred >= 0 ? preferred : Math.max(0, replayState.dates.length - 1) });
    }
  };

  return <div className="rotation-page">
    <RotationFilters dates={mode === "replay" ? [...replayState.dates].reverse() : dates.data ?? []} selectedDate={displayDate ?? ""} level={level} modelVersion="v1" onDateChange={handleDateChange} onLevelChange={(nextLevel) => { setLevel(nextLevel); setSelectedDate(undefined); setSelectedSectorName(null); setComparisonSectors([]); setMode("snapshot"); }} searchQuery={searchQuery} phaseFilter={phaseFilter} onSearchChange={setSearchQuery} onPhaseChange={setPhaseFilter} />
    <MarketSummary marketRegime={sectors[0]?.market_regime ?? "range"} eligibleCount={eligible} acceleratingCount={accelerating} riskCount={risk} />
    <section className="rotation-workspace">
      <article className="chart-panel">
        <header className="panel-header">
          <div><p>ROTATION WORKBENCH · {displayDate} · 数据源截止 {snapshot.data.meta.source_max_trade_date ?? "待确认"}</p><h2>行业轮动象限</h2></div>
          <div className="chart-actions">
            <div className="segmented-control workbench-mode" aria-label="象限图模式"><button className={mode === "snapshot" ? "is-active" : ""} type="button" onClick={() => handleModeChange("snapshot")}>单日观察</button><button className={mode === "replay" ? "is-active" : ""} type="button" onClick={() => handleModeChange("replay")}>{mode === "replay" && replayState.playing ? <Pause size={12} /> : <Play size={12} />}动态回放</button></div>
            <button className="method-link" type="button" title="横轴为趋势速度，纵轴为趋势加速度；分数均为当日行业截面相对值"><CircleHelp aria-hidden="true" size={15} />如何阅读</button>
          </div>
        </header>
        <div className="chart-subtoolbar">
          <div className="phase-legend">{Object.entries(PHASE_META).filter(([key]) => key !== "neutral").map(([key, meta]) => <span key={key}><i style={{ background: meta.color }} />{meta.label}</span>)}</div>
          <label className="label-density"><span>标注密度</span><select value={labelDensity} onChange={(event) => setLabelDensity(event.target.value as LabelDensity)}><option value="compact">精简</option><option value="focus">关注</option><option value="all">全部</option></select></label>
        </div>
        {mode === "replay" && <ReplayControls dates={replayState.dates} index={replayState.index} playing={replayState.playing} speed={replayState.speed} dispatch={replayDispatch} />}
        {filteredSectors.length > 0 ? <LazyQuadrantChart sectors={filteredSectors} selectedSectorName={selectedSectorName} onSelect={setSelectedSectorName} labelDensity={labelDensity} trail={trail} /> : <div className="empty-panel">当前筛选条件下没有可展示行业</div>}
        <footer className="chart-note"><span>气泡大小：量能活跃度</span><span>透明度：阶段置信度</span><span>描边：行业内部参与度</span>{mode === "replay" && selectedSectorName && <span className="trail-note"><Route size={11} />虚线：{selectedSectorName} 近10日尾迹</span>}<span>坐标分数不是收益率</span></footer>
      </article>
      <SectorRanking sectors={filteredSectors} selectedSectorName={selectedSectorName} onSelect={setSelectedSectorName} />
    </section>
    {selected && <SectorDetailDrawer sector={selected} onClose={() => setSelectedSectorName(null)} />}
    {comparisonSectors.length > 0 && <section className="sector-history content-panel"><header className="panel-header"><div><p>SECTOR TRAJECTORY</p><h2><History aria-hidden="true" />行业轨迹对比</h2></div><div className="segmented-control">{([5, 20, 60] as const).map((windowValue) => <button className={historyWindow === windowValue ? "is-active" : ""} key={windowValue} type="button" onClick={() => setHistoryWindow(windowValue)}>{windowValue} 日</button>)}</div></header><TrajectoryControls sectorNames={comparisonSectors} onRemove={(sectorName) => { setComparisonSectors((current) => current.filter((item) => item !== sectorName)); if (selectedSectorName === sectorName) setSelectedSectorName(null); }} />{history.isLoading ? <div className="trajectory-loading">正在加载行业历史轨迹…</div> : <LazySectorTrajectory trajectories={trajectories} />}{historyGaps.length > 0 && <div className="history-gaps"><strong>数据缺口</strong>{historyGaps.map((gap) => <span key={gap.sector_name}>{gap.sector_name}：{gap.dates.length} 个交易日缺少有效坐标（轨迹已断开）</span>)}</div>}</section>}
  </div>;
}
