/** 全市场回放日期指针状态机测试。 */
import { initialReplayState, replayReducer } from "./replayState";

describe("replayReducer", () => {
  it("播放到最后一帧时自动暂停，且不会越界", () => {
    let state = initialReplayState(["2026-08-01", "2026-08-04"]);
    state = replayReducer(state, { type: "PLAY" });
    state = replayReducer(state, { type: "NEXT" });
    expect(state).toMatchObject({ index: 1, playing: true });
    state = replayReducer(state, { type: "NEXT" });
    expect(state).toMatchObject({ index: 1, playing: false });
  });

  it("允许切换回放速度并在跳转日期后暂停", () => {
    let state = initialReplayState(["2026-08-01", "2026-08-04"]);
    state = replayReducer(state, { type: "SET_SPEED", speed: 2 });
    expect(state.speed).toBe(2);
    state = replayReducer({ ...state, playing: true }, { type: "SEEK", index: 1 });
    expect(state).toMatchObject({ index: 1, playing: false, speed: 2 });
  });
});
