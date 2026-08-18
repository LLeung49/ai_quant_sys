from datetime import date

import pytest

from morning_conference.sector_rotation2.research.calendar import TradingCalendar


def test_shift_uses_market_dates() -> None:
    calendar = TradingCalendar([date(2026, 8, 14), date(2026, 8, 17), date(2026, 8, 18)])
    assert calendar.shift(date(2026, 8, 17), 1) == date(2026, 8, 18)
    assert calendar.shift(date(2026, 8, 17), -1) == date(2026, 8, 14)


def test_calendar_rejects_non_market_date() -> None:
    calendar = TradingCalendar([date(2026, 8, 17)])
    assert date(2026, 8, 16) not in calendar
    with pytest.raises(ValueError, match="not a trading date"):
        calendar.shift(date(2026, 8, 16), 1)
