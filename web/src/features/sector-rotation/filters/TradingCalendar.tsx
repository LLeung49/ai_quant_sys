export interface TradingCalendarProps {
  displayedMonth: string;
  onDisplayedMonthChange: (month: string) => void;
  tradeDates: string[];
  snapshotDates: string[];
  selectedDate: string;
  onDateChange: (date: string) => void;
}

function parseMonth(value: string): { year: number; month: number } {
  const matched = /^(\d{4})-(\d{2})$/.exec(value);
  if (!matched) throw new Error(`Invalid displayed month: ${value}`);
  return { year: Number(matched[1]), month: Number(matched[2]) };
}

function formatMonth(year: number, month: number): string {
  return `${year}-${String(month).padStart(2, "0")}`;
}

function shiftMonth(displayedMonth: string, offset: number): string {
  const { year, month } = parseMonth(displayedMonth);
  const index = year * 12 + month - 1 + offset;
  return formatMonth(Math.floor(index / 12), (index % 12) + 1);
}

function toIsoDate(year: number, month: number, day: number): string {
  return `${formatMonth(year, month)}-${String(day).padStart(2, "0")}`;
}

/** 只呈现上游传入状态的受控月历；不以星期规则推断交易日。 */
export function TradingCalendar({ displayedMonth, onDisplayedMonthChange, tradeDates, snapshotDates, selectedDate, onDateChange }: TradingCalendarProps) {
  const { year, month } = parseMonth(displayedMonth);
  const tradeDateSet = new Set(tradeDates);
  const snapshotDateSet = new Set(snapshotDates);
  const firstWeekday = new Date(Date.UTC(year, month - 1, 1)).getUTCDay();
  const daysInMonth = new Date(Date.UTC(year, month, 0)).getUTCDate();
  const cells = Array.from({ length: firstWeekday + daysInMonth }, (_, index) => index - firstWeekday + 1);

  return (
    <section className="trading-calendar" aria-label="交易日历">
      <header className="trading-calendar__header">
        <button type="button" aria-label="上个月" onClick={() => onDisplayedMonthChange(shiftMonth(displayedMonth, -1))}>‹</button>
        <strong aria-live="polite">{displayedMonth}</strong>
        <button type="button" aria-label="下个月" onClick={() => onDisplayedMonthChange(shiftMonth(displayedMonth, 1))}>›</button>
      </header>
      <div className="trading-calendar__weekdays" aria-hidden="true">
        {["日", "一", "二", "三", "四", "五", "六"].map((weekday) => <span key={weekday}>{weekday}</span>)}
      </div>
      <div className="trading-calendar__grid" role="grid" aria-label={`${displayedMonth} 交易日历`} style={{ gridTemplateColumns: "repeat(7, minmax(0, 1fr))" }}>
        {cells.map((day, index) => {
          if (day < 1) return <span aria-hidden="true" className="trading-calendar__blank" key={`blank-${index}`} />;
          const date = toIsoDate(year, month, day);
          const isTradeDate = tradeDateSet.has(date);
          const status = snapshotDateSet.has(date) ? "snapshot" : isTradeDate ? "pending" : "closed";
          const statusLabel = status === "snapshot" ? "已生成快照" : status === "pending" ? "交易日，尚未生成快照" : "非交易日";
          return (
            <div key={date} role="gridcell">
              <button
                aria-label={`${date}，${statusLabel}`}
                aria-pressed={isTradeDate ? selectedDate === date : undefined}
                className="trading-calendar__day"
                data-date-status={status}
                disabled={!isTradeDate}
                onClick={() => onDateChange(date)}
                type="button"
              >
                {day}
              </button>
            </div>
          );
        })}
      </div>
    </section>
  );
}
