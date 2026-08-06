/** 板块轮动主视图的日期、行业层级和模型版本筛选控件。 */

import { CalendarDays, Layers3, Search } from "lucide-react";

export interface RotationFiltersProps {
  /** 可选成功运行日期，按最新到最早排序。 */
  dates: string[];
  /** 当前选择的交易日。 */
  selectedDate: string;
  /** 当前申万行业层级，仅为 1 或 2。 */
  level: 1 | 2;
  /** 当前快照模型版本。 */
  modelVersion: string;
  /** 输入：新日期；输出：通知页面更新查询状态。 */
  onDateChange: (date: string) => void;
  /** 输入：新行业层级；输出：通知页面刷新日期和快照。 */
  onLevelChange: (level: 1 | 2) => void;
  /** 当前行业名称搜索词。 */
  searchQuery?: string;
  /** 当前阶段筛选值，``all`` 表示全部。 */
  phaseFilter?: string;
  /** 输入：新搜索词；输出：同步过滤象限图和排行榜。 */
  onSearchChange?: (query: string) => void;
  /** 输入：新阶段值；输出：同步过滤象限图和排行榜。 */
  onPhaseChange?: (phase: string) => void;
}

/**
 * 渲染不含业务查询逻辑的板块轮动筛选器。
 *
 * 输入：当前选择和受控更新回调。
 * 输出：带显式标签、可键盘操作的表单控件。
 */
export function RotationFilters({ dates, selectedDate, level, modelVersion, onDateChange, onLevelChange, searchQuery = "", phaseFilter = "all", onSearchChange, onPhaseChange }: RotationFiltersProps) {
  return (
    <section className="rotation-filters" aria-label="板块轮动筛选条件">
      <div className="filter-heading"><span>观察截面</span><small>所有指标均来自当日成功快照</small></div>
      <label className="filter-field">
        <span><CalendarDays aria-hidden="true" size={14} />交易日</span>
        <select aria-label="交易日" value={selectedDate} onChange={(event) => onDateChange(event.target.value)}>
          {dates.map((date) => <option key={date} value={date}>{date}</option>)}
        </select>
      </label>
      <label className="filter-field">
        <span><Layers3 aria-hidden="true" size={14} />行业层级</span>
        <select aria-label="行业层级" value={level} onChange={(event) => onLevelChange(Number(event.target.value) as 1 | 2)}>
          <option value={1}>一级行业</option>
          <option value={2}>二级行业</option>
        </select>
      </label>
      <label className="filter-field">
        <span>确认阶段</span>
        <select aria-label="确认阶段" value={phaseFilter} onChange={(event) => onPhaseChange?.(event.target.value)}>
          <option value="all">全部阶段</option>
          <option value="accel_up">加速走强</option>
          <option value="decel_up">强势降温</option>
          <option value="reversal_confirmed">修复确认</option>
          <option value="bottoming_candidate">弱势修复观察</option>
          <option value="accel_down">加速走弱</option>
          <option value="neutral">方向未明</option>
        </select>
      </label>
      <label className="filter-field filter-field--search">
        <span><Search aria-hidden="true" size={14} />搜索行业</span>
        <input aria-label="搜索行业" value={searchQuery} placeholder="输入行业名称" onChange={(event) => onSearchChange?.(event.target.value)} />
      </label>
      <div className="model-badge"><span>模型</span><strong>{modelVersion}</strong></div>
    </section>
  );
}
