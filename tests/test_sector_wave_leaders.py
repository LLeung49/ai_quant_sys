from datetime import date, timedelta

from morning_conference.sector_rotation2.api.sector_waves import detect_rising_waves, rank_wave_leaders


def _bars(closes):
    return [
        {"trade_date": (date(2026, 1, 1) + timedelta(days=index)).isoformat(),
         "timestamp": index + 1, "close": close, "high": close + 1, "low": close - 1}
        for index, close in enumerate(closes)
    ]


def test_detect_rising_waves_confirms_peak_and_keeps_open_wave():
    bars = _bars([100, 96, 100, 105, 104, 109, 103, 101, 108, 112])
    bars[3]["high"] = 120  # 中途影线可高于收盘价峰值，红框应覆盖整个波段的影线。
    bars[4]["low"] = 90
    waves = detect_rising_waves(bars)
    assert [(wave["start_date"], wave["end_date"], wave["is_confirmed"]) for wave in waves] == [
        ("2026-01-02", "2026-01-06", True),
        ("2026-01-08", "2026-01-10", False),
    ]
    assert waves[0]["base_date"] == "2026-01-01"
    assert waves[0]["sector_change_pct"] == 9.0
    assert waves[0]["start_low"] == 90
    assert waves[0]["end_high"] == 120


def test_detect_rising_waves_keeps_every_wave_in_loaded_bars():
    closes = [100]
    for _ in range(8):
        closes.extend([90, 100, 94])
    waves = detect_rising_waves(_bars(closes))
    assert len(waves) == 8
    assert all(wave["is_confirmed"] for wave in waves)


def test_rank_wave_leaders_uses_prestart_close_and_omits_missing_or_bad_prices():
    wave = {"base_date": "2026-01-01", "start_date": "2026-01-02", "end_date": "2026-01-06"}
    rows = [
        {"stock_code": "000001.SZ", "stock_name": "甲", "trade_date": "2026-01-01", "close": 10},
        {"stock_code": "000001.SZ", "stock_name": "甲", "trade_date": "2026-01-06", "close": 16},
        {"stock_code": "000002.SZ", "stock_name": "乙", "trade_date": "2026-01-01", "close": 20},
        {"stock_code": "000002.SZ", "stock_name": "乙", "trade_date": "2026-01-06", "close": 30},
        {"stock_code": "000003.SZ", "stock_name": "丙", "trade_date": "2026-01-06", "close": 99},
        {"stock_code": "000004.SZ", "stock_name": "丁", "trade_date": "2026-01-01", "close": 0},
        {"stock_code": "000004.SZ", "stock_name": "丁", "trade_date": "2026-01-06", "close": 9},
    ]
    assert rank_wave_leaders(wave, rows) == [
        {"rank": 1, "stock_code": "000001.SZ", "stock_name": "甲", "change_pct": 60.0},
        {"rank": 2, "stock_code": "000002.SZ", "stock_name": "乙", "change_pct": 50.0},
    ]
