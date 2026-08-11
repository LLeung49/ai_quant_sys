/** 板块轮动统一工作台的可分享 URL 状态。 */

import { LIFECYCLE_FILTER_VALUES, type LifecycleFilter } from "../lifecycle/meta";

export type WorkbenchMode = "snapshot" | "replay";
export type LabelDensity = "compact" | "focus" | "all";

export interface WorkbenchUrlState {
  date?: string;
  level: 1 | 2;
  mode: WorkbenchMode;
  phase: string;
  query: string;
  sector: string | null;
  historyWindow: 5 | 20 | 60;
  labelDensity: LabelDensity;
  lifecycle: LifecycleFilter;
  changedOnly: boolean;
}

/**
 * 从浏览器查询字符串恢复研究现场。
 *
 * 输入：带或不带 ``?`` 的 URL 查询字符串。
 * 输出：经过枚举边界校验的工作台状态；非法值回退为产品默认值。
 */
export function parseWorkbenchUrl(search: string): WorkbenchUrlState {
  const params = new URLSearchParams(search);
  const level = params.get("level") === "1" ? 1 : 2;
  const mode = params.get("mode") === "replay" ? "replay" : "snapshot";
  const windowValue = Number(params.get("window"));
  const historyWindow = ([5, 20, 60] as const).includes(windowValue as 5 | 20 | 60) ? windowValue as 5 | 20 | 60 : 20;
  const densityValue = params.get("labels");
  const labelDensity: LabelDensity = densityValue === "compact" || densityValue === "all" ? densityValue : "focus";
  const rawLifecycle = params.get("lifecycle");
  const lifecycle: LifecycleFilter = LIFECYCLE_FILTER_VALUES.includes(rawLifecycle as LifecycleFilter)
    ? rawLifecycle as LifecycleFilter
    : "all";
  const changedOnly = params.get("changed") === "1";
  return {
    date: params.get("date") || undefined,
    level,
    mode,
    phase: params.get("phase") || "all",
    query: params.get("q") || "",
    sector: params.get("sector") || null,
    historyWindow,
    labelDensity,
    lifecycle,
    changedOnly,
  };
}

/**
 * 将工作台状态序列化为稳定查询字符串。
 *
 * 输入：已校验的完整工作台状态。
 * 输出：以 ``?`` 开头的查询字符串；空搜索和空行业不写入 URL。
 */
export function serializeWorkbenchUrl(state: WorkbenchUrlState): string {
  const params = new URLSearchParams();
  if (state.date) params.set("date", state.date);
  params.set("level", String(state.level));
  params.set("mode", state.mode);
  params.set("phase", state.phase);
  params.set("window", String(state.historyWindow));
  params.set("labels", state.labelDensity);
  params.set("lifecycle", state.lifecycle);
  if (state.changedOnly) params.set("changed", "1");
  if (state.query) params.set("q", state.query);
  if (state.sector) params.set("sector", state.sector);
  return `?${params.toString()}`;
}
