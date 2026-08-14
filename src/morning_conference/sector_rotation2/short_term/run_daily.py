"""v2_short_term 鐭湡寮傚姩鐨勬瘡鏃ヨ繍琛屽叆鍙ｄ笌 CLI銆?

璋冪敤鏍蜂緥锛堜笌 v1 鍚屾锛?:

    $env:PYTHONPATH = "src"
    python -m morning_conference.sector_rotation2.short_term.run_daily --level 2 --as-of-date 2026-08-08
    python -m morning_conference.sector_rotation2.short_term.run_daily --level 2 --backfill-start 2026-08-01 --backfill-end 2026-08-08
    python -m morning_conference.sector_rotation2.short_term.run_daily --level 2 --as-of-date 2026-08-08 --csv-output outputs/short_term
    python -m morning_conference.sector_rotation2.short_term.run_daily --level 2 --as-of-date 2026-08-08 --dry-run --csv-output outputs/short_term

``run_short_term_for`` 鏄紪绋嬪紡鍏ュ彛锛宍`main`` 鏄?argparse CLI 鍏ュ彛锛?
浜岃€呭叡鐢ㄥ悓涓€濂楀唴閮ㄨ緟鍔╁嚱鏁般€?
"""
from __future__ import annotations

import argparse
import logging
import uuid
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from .config import DEFAULT_SHORT_TERM_CONFIG, ModelConfigShortTerm, short_term_config_hash
from ..data_loader import build_market_benchmark, load_sector_panel
from .features import build_short_term_features
from .labels import label_dataframe
from .scoring import score_short_term_panel
from .snapshot_store import (
    create_short_term_run,
    mark_short_term_run_failed,
    mark_short_term_run_succeeded,
    persist_short_term_snapshot,
)


LOGGER = logging.getLogger(__name__)


# CSV 鍒楅『搴忥細淇濈暀鏂囨。 搂7.1 涓０鏄庣殑瀛楁椤哄簭锛屼究浜庝汉鑲夋瘮瀵广€?
_CSV_COLUMNS: tuple[str, ...] = (
    "as_of_date", "sector_level", "sector_name", "model_version",
    "score_eligible",
    "ret_1", "ret_2", "ret_3",
    "rs_1", "rs_2", "rs_5", "rs5_accel_1d", "ma5_slope",
    "rvol_1_20", "rvol_1_60",
    "amount_share_today", "share_impulse_1d",
    "breadth_up", "breadth_above_ma5", "breadth_new_high_5",
    "breadth_strong_1d", "breadth_weak_1d", "breadth_rvol_1d",
    "limit_up_ratio", "limit_down_ratio",
    "streak_pos_ret", "streak_high_breadth", "streak_top_limit_up",
    "pulse_score", "volume_spike_score", "breadth_spike_score",
    "limit_score", "momentum_shift_score",
    "short_term_composite", "short_term_composite_rank",
    "short_term_labels", "short_term_intensity",
)


@dataclass(frozen=True)
class ShortTermRunResult:
    """鍗曟棩鐭湡杩愯鐨勪笉鍙彉缁撴灉銆?""

    run_id: str
    as_of_date: str
    sector_level: int
    model_version: str
    config_hash: str
    eligible_sector_count: int
    skipped_sector_count: int
    snapshot_rows: int


def _attach_member_counters(features: pd.DataFrame, members: dict[str, tuple[int, int]]) -> pd.DataFrame:
    """鎶婂閮ㄨ绠楃殑 ``eligible_member_count``銆乣`valid_member_count`` 鎸傚洖鍒扮壒寰佽〃銆?""
    if not members:
        features["eligible_member_count"] = pd.NA
        features["valid_member_count"] = pd.NA
        return features
    counts = pd.DataFrame.from_dict(members, orient="index", columns=["eligible_member_count", "valid_member_count"])
    return features.join(counts)


def run_short_term_for(
    sector_level: int,
    as_of_date: str,
    config: ModelConfigShortTerm | None = None,
    panel: dict[str, pd.DataFrame] | None = None,
    benchmark: pd.DataFrame | None = None,
) -> ShortTermRunResult:
    """瀵瑰崟涓氦鏄撴棩鎵ц瀹屾暣鐨勭煭鏈熷紓鍔ㄦ祦姘寸嚎锛堢紪绋嬪紡鍏ュ彛锛夈€?

    姝ラ锛?
        1. 鐢熸垚杩愯 UUID 涓庨厤缃搱甯岋紱
        2. 鍐欏叆 ``running`` 瀹¤琛岋紱
        3. 鍔犺浇鏉垮潡闈㈡澘骞舵瀯寤哄師濮嬬壒寰侊紱
        4. 鍚堟垚鐭湡璇勫垎锛?
        5. 搴旂敤寮傚姩鏍囩涓庡己搴﹀垎绾э紱
        6. 鎵归噺 upsert 鐭湡蹇収锛?
        7. 鏇存柊瀹¤琛屼负 succeeded銆?

    寮傚父:
        浠讳綍姝ラ澶辫触閮戒細鎶婂璁¤鏍囪涓?failed 骞跺師鏍锋姏鍑恒€?
    """
    cfg = config or DEFAULT_SHORT_TERM_CONFIG
    run_id = str(uuid.uuid4())
    config_hash = short_term_config_hash(cfg)

    create_short_term_run(
        run_id=run_id,
        as_of_date=as_of_date,
        sector_level=sector_level,
        model_version=cfg.model_version,
        config_hash=config_hash,
        source_max_trade_date=as_of_date,
    )

    try:
        features = build_short_term_features(sector_level, as_of_date, cfg)
        if features.empty:
            mark_short_term_run_succeeded(run_id, eligible_sector_count=0, skipped_sector_count=0)
            LOGGER.warning("鐭湡鐗瑰緛涓虹┖锛?s level=%s", as_of_date, sector_level)
            return ShortTermRunResult(
                run_id=run_id,
                as_of_date=as_of_date,
                sector_level=sector_level,
                model_version=cfg.model_version,
                config_hash=config_hash,
                eligible_sector_count=0,
                skipped_sector_count=0,
                snapshot_rows=0,
            )

        scored = score_short_term_panel(features, cfg)
        labelled = label_dataframe(scored, cfg)
        # ``coverage_ratio`` 鐢辫皟鐢ㄦ柟鏍规嵁鎴愬憳鏄犲皠璁＄畻鍚庢敞鍏ワ紱鏈鏋剁暀 NaN 鍗犱綅銆?
        labelled["coverage_ratio"] = pd.NA
        snapshot_rows = persist_short_term_snapshot(
            labelled,
            as_of_date=as_of_date,
            sector_level=sector_level,
            model_version=cfg.model_version,
            run_id=run_id,
        )
        eligible_count = int(labelled["score_eligible"].sum())
        skipped_count = int((~labelled["score_eligible"].fillna(False)).sum())
        mark_short_term_run_succeeded(
            run_id,
            eligible_sector_count=eligible_count,
            skipped_sector_count=skipped_count,
        )
        LOGGER.info(
            "鐭湡杩愯瀹屾垚锛?s level=%s eligible=%s skipped=%s rows=%s",
            as_of_date, sector_level, eligible_count, skipped_count, snapshot_rows,
        )
        return ShortTermRunResult(
            run_id=run_id,
            as_of_date=as_of_date,
            sector_level=sector_level,
            model_version=cfg.model_version,
            config_hash=config_hash,
            eligible_sector_count=eligible_count,
            skipped_sector_count=skipped_count,
            snapshot_rows=snapshot_rows,
        )
    except Exception as exc:  # noqa: BLE001 - 闇€鎹曡幏骞舵妸瀹¤琛岀疆 failed銆?
        mark_short_term_run_failed(run_id, repr(exc))
        LOGGER.exception("鐭湡杩愯澶辫触锛?s level=%s", as_of_date, sector_level)
        raise


# ---------- CLI 鍐呴儴杈呭姪 --------------------------------------------------------


def _build_pipeline(level: int, as_of_date: str, config: ModelConfigShortTerm) -> pd.DataFrame:
    """澶嶅埢 ``run_short_term_for`` 鐨勬祦姘寸嚎浣嗚烦杩囧啓搴擄紱杩斿洖鏍囪杩囧厓淇℃伅鐨?DataFrame銆?""
    features = build_short_term_features(level, as_of_date, config)
    if features.empty:
        return pd.DataFrame()
    features = _attach_member_counters(features, {})
    features["coverage_ratio"] = pd.NA
    features["as_of_date"] = as_of_date
    features["sector_level"] = level
    features["model_version"] = config.model_version
    features["sector_name"] = features.index.astype(str)
    scored = score_short_term_panel(features, config)
    return label_dataframe(scored, config)


def _write_csv(frame: pd.DataFrame, output_dir: Path, as_of_date: str) -> Path | None:
    """鎶婂綋鏃ョ殑鐭湡蹇収鍐欏叆 CSV锛屽垪椤哄簭涓庢枃妗?搂7.1 瀵归綈銆?""
    if frame.empty:
        LOGGER.warning("鏃犲彲鍐欏叆 CSV 鐨勬澘鍧楋細%s", as_of_date)
        return None
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / f"short_term_{as_of_date.replace('-', '')}.csv"
    available = [column for column in _CSV_COLUMNS if column in frame.columns]
    frame.loc[:, available].to_csv(csv_path, index=False, encoding="utf-8-sig")
    LOGGER.info("宸插啓鍏?CSV锛?s锛?s 琛岋級", csv_path, len(frame))
    return csv_path


def _run_one_date(
    level: int,
    as_of_date: str,
    config: ModelConfigShortTerm,
    csv_output: Path | None,
    dry_run: bool,
) -> ShortTermRunResult | None:
    """CLI 鍗曟棩鎵ц鍣紱``dry_run=True`` 鏃惰烦杩囦换浣曞啓搴撴搷浣溿€?""
    if dry_run:
        LOGGER.info("[dry-run] 寮€濮嬭绠?%s level=%s", as_of_date, level)
        frame = _build_pipeline(level, as_of_date, config)
        if csv_output:
            _write_csv(frame, csv_output, as_of_date)
        LOGGER.info(
            "[dry-run] %s level=%s锛?s 涓澘鍧楋紝score_eligible=%s",
            as_of_date, level,
            len(frame), int(frame["score_eligible"].sum()) if "score_eligible" in frame else 0,
        )
        return None
    result = run_short_term_for(level, as_of_date, config)
    if csv_output and result.snapshot_rows > 0:
        # 钀藉簱鎴愬姛鍚?CSV 浠呬綔浜鸿倝澶囨煡锛涗粠璇诲簱鍐嶆媺涓€娆★紝閬垮厤浜屾鎵ц娴佹按绾裤€?
        from .api.repository import ShortTermRepository  # 灞€閮?import锛岄伩鍏?CLI 鍚姩闃舵鍔犺浇 FastAPI 渚濊禆銆?
        rows = ShortTermRepository().load_snapshot(as_of_date, level, config.model_version)
        if rows:
            _write_csv(pd.DataFrame(rows), csv_output, as_of_date)
    return result


def _list_trade_dates(level: int, start_date: str, end_date: str) -> list[str]:
    """杩斿洖鍥炲～鍖洪棿鍐呭彲鐢ㄧ殑浜ゆ槗鏃ュ垪琛紱涓?v1 ``run_daily.list_trade_dates`` 琛屼负涓€鑷淬€?""
    from ..data_loader import load_sector_panel
    panel = load_sector_panel(level=level, start_date=start_date, end_date=end_date, min_history_days=1)
    if not panel:
        return []
    all_dates: set[str] = set()
    for frame in panel.values():
        for date in frame.index:
            iso = date.strftime("%Y-%m-%d")
            if start_date <= iso <= end_date:
                all_dates.add(iso)
    return sorted(all_dates)


# ---------- CLI 鍏ュ彛 ------------------------------------------------------------


def main() -> None:
    """瑙ｆ瀽 CLI 鍙傛暟骞舵墽琛屽崟鏃ユ垨鍖洪棿鍥炲～銆?""
    parser = argparse.ArgumentParser(description="杩愯 sector_rotation2 v2_short_term 鐭湡寮傚姩娴佹按绾?)
    parser.add_argument("--level", type=int, required=True, choices=(1, 2), help="鐢充竾琛屼笟灞傜骇")
    parser.add_argument("--as-of-date", help="鍗曟棩浜ゆ槗鏃ワ紝鏍煎紡 YYYY-MM-DD")
    parser.add_argument("--backfill-start", help="鍥炲～璧峰浜ゆ槗鏃ワ紝闇€涓?--backfill-end 鍚屾椂鎻愪緵")
    parser.add_argument("--backfill-end", help="鍥炲～缁撴潫浜ゆ槗鏃ワ紝闇€涓?--backfill-start 鍚屾椂鎻愪緵")
    parser.add_argument("--model-version", default="v2_short_term", help="鐭湡妯″瀷鐗堟湰锛堥粯璁?v2_short_term锛?)
    parser.add_argument("--csv-output", help="鍙€夛細鎶婂綋鏃ョ煭鏈熷揩鐓ц惤鐩樺埌璇ョ洰褰曠殑 CSV锛屾枃浠跺悕 short_term_YYYYMMDD.csv")
    parser.add_argument("--dry-run", action="store_true", help="鍙绠椾笉鍐欏簱锛涘彲涓?--csv-output 鎼厤鐢ㄤ簬鏈湴妫€瑙?)
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=("DEBUG", "INFO", "WARNING", "ERROR"),
        help="缁堢鏃ュ織绾у埆",
    )
    args = parser.parse_args()

    if bool(args.backfill_start) ^ bool(args.backfill_end):
        parser.error("--backfill-start 涓?--backfill-end 蹇呴』鍚屾椂鎻愪緵")
    if not args.as_of_date and not (args.backfill_start and args.backfill_end):
        parser.error("蹇呴』鎻愪緵 --as-of-date 鎴栧畬鏁寸殑 --backfill-start/--backfill-end 鍖洪棿")

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s %(levelname)-8s %(name)s - %(message)s",
    )

    config = ModelConfigShortTerm(model_version=args.model_version)
    csv_dir = Path(args.csv_output).resolve() if args.csv_output else None

    if args.backfill_start and args.backfill_end:
        trade_dates = _list_trade_dates(args.level, args.backfill_start, args.backfill_end)
        if not trade_dates:
            LOGGER.warning("鍥炲～鍖洪棿 [%s, %s] 鍦?level=%s 涓嬫病鏈夊彲鐢ㄤ氦鏄撴棩", args.backfill_start, args.backfill_end, args.level)
            return
        LOGGER.info(
            "寮€濮嬪洖濉細level=%s model=%s dates=%s config_hash=%s dry_run=%s",
            args.level, config.model_version, trade_dates, short_term_config_hash(config), args.dry_run,
        )
        success = 0
        for trade_date in trade_dates:
            try:
                result = _run_one_date(args.level, trade_date, config, csv_dir, args.dry_run)
                if result is not None or args.dry_run:
                    success += 1
            except Exception:
                LOGGER.exception("鍥炲～鏃ユ湡澶辫触锛?s", trade_date)
                if not args.dry_run:
                    raise
        LOGGER.info("鍥炲～瀹屾垚锛氭垚鍔?%s / 鍏?%s", success, len(trade_dates))
    else:
        _run_one_date(args.level, args.as_of_date, config, csv_dir, args.dry_run)


if __name__ == "__main__":
    main()
