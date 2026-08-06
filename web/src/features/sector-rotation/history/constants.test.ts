/** 行业轨迹上限与追加规则测试。 */
import { addTrajectorySector, MAX_TRAJECTORY_SECTORS } from "./constants";

describe("addTrajectorySector", () => {
  it("允许加入第五个行业，并在已满时保留原有五个行业", () => {
    const four = ["A", "B", "C", "D"];
    const five = addTrajectorySector(four, "E");

    expect(MAX_TRAJECTORY_SECTORS).toBe(5);
    expect(five).toEqual(["A", "B", "C", "D", "E"]);
    expect(addTrajectorySector(five, "F")).toBe(five);
    expect(addTrajectorySector(five, "A")).toBe(five);
  });
});
