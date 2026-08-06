/** 全市场回放的无副作用日期指针状态机。 */

export type ReplaySpeed = 0.5 | 1 | 2;
export interface ReplayState { dates: string[]; index: number; playing: boolean; speed: ReplaySpeed; }
export type ReplayAction = { type: "PLAY" | "PAUSE" | "NEXT" | "PREVIOUS" } | { type: "SEEK"; index: number } | { type: "SET_SPEED"; speed: ReplaySpeed } | { type: "LOAD_DATES"; dates: string[]; preferredDate?: string };

/** 输入：回放日期；输出：从第一帧且暂停开始的播放状态。 */
export function initialReplayState(dates: string[]): ReplayState { return { dates, index: 0, playing: false, speed: 1 }; }

/**
 * 计算一次回放控制动作后的状态。
 *
 * 输入：当前状态和播放/暂停/步进/跳转动作。
 * 输出：受日期边界约束的新状态；到达最后一帧后自动暂停。
 */
export function replayReducer(state: ReplayState, action: ReplayAction): ReplayState {
  if (action.type === "LOAD_DATES") {
    const preferredIndex = action.preferredDate ? action.dates.indexOf(action.preferredDate) : -1;
    return { ...state, dates: action.dates, index: preferredIndex >= 0 ? preferredIndex : Math.max(0, action.dates.length - 1), playing: false };
  }
  const last = Math.max(0, state.dates.length - 1);
  if (action.type === "PLAY") return { ...state, playing: state.index < last };
  if (action.type === "PAUSE") return { ...state, playing: false };
  if (action.type === "SET_SPEED") return { ...state, speed: action.speed };
  if (action.type === "SEEK") return { ...state, index: Math.min(last, Math.max(0, action.index)), playing: false };
  if (action.type === "PREVIOUS") return { ...state, index: Math.max(0, state.index - 1), playing: false };
  if (state.index >= last) return { ...state, playing: false };
  return { ...state, index: state.index + 1 };
}
