"""Explicit CLI for refreshing exposure-derived sector/ETF mappings.

This writer is intentionally separate from ``run_daily``: building candidate
snapshots remains read-only with respect to mapping data.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable
from datetime import date
import json
import math
from pathlib import Path
from typing import Any

from .freshness import assess_holdings_freshness
from .providers import (
    AKShareETFProvider,
    BasketProvider,
    ETFBasketInput,
    LocalSWMembershipProvider,
    MembershipProvider,
    MiniQMTETFProvider,
    ProviderQualityIssue,
    refresh_sector_etf_mapping,
    select_freshest_basket,
)


class AuditedJSONBasketProvider:
    """Load actual constituent weights from a strict, auditable JSON file."""

    _ROOT_FIELDS = {
        "provider_reported_date", "weight_unit", "source_provider",
        "source_reference", "baskets",
    }
    _CONSTITUENT_FIELDS = {"stock_code", "weight"}

    def __init__(self, path: str | Path) -> None:
        self._path = Path(path)

    def load(self, target_date: date) -> ETFBasketInput:
        try:
            payload = json.loads(self._path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise ValueError(f"invalid basket JSON {self._path}: {exc}") from exc
        if not isinstance(payload, dict):
            raise ValueError("basket JSON root must be an object")
        missing = self._ROOT_FIELDS - payload.keys()
        extra = payload.keys() - self._ROOT_FIELDS
        if missing:
            raise ValueError(f"basket JSON missing required field(s): {', '.join(sorted(missing))}")
        if extra:
            raise ValueError(f"basket JSON has unsupported field(s): {', '.join(sorted(extra))}")

        reported_date = _strict_iso_date(payload["provider_reported_date"])
        weight_unit = payload["weight_unit"]
        if weight_unit not in {"decimal", "percent"}:
            raise ValueError("weight_unit must be 'decimal' or 'percent'")
        source_provider = _nonblank_string(payload["source_provider"], "source_provider")
        source_reference = _nonblank_string(payload["source_reference"], "source_reference")
        raw_baskets = payload["baskets"]
        if not isinstance(raw_baskets, dict) or not raw_baskets:
            raise ValueError("baskets must be a non-empty object")

        baskets: dict[str, tuple[dict[str, object], ...]] = {}
        for raw_etf_code, raw_rows in raw_baskets.items():
            etf_code = _nonblank_string(raw_etf_code, "ETF code")
            if not isinstance(raw_rows, list) or not raw_rows:
                raise ValueError(f"baskets[{etf_code!r}] must be a non-empty array")
            rows: list[dict[str, object]] = []
            for index, raw_row in enumerate(raw_rows):
                if not isinstance(raw_row, dict) or set(raw_row) != self._CONSTITUENT_FIELDS:
                    raise ValueError(
                        f"baskets[{etf_code!r}][{index}] must contain only stock_code and weight",
                    )
                stock_code = _nonblank_string(raw_row["stock_code"], "stock_code")
                weight = raw_row["weight"]
                if isinstance(weight, bool) or not isinstance(weight, (int, float)):
                    raise ValueError(f"baskets[{etf_code!r}][{index}].weight must be numeric")
                numeric_weight = float(weight)
                if not math.isfinite(numeric_weight) or numeric_weight < 0:
                    raise ValueError(f"baskets[{etf_code!r}][{index}].weight must be finite and non-negative")
                rows.append({"stock_code": stock_code, "weight": numeric_weight})
            baskets[etf_code] = tuple(rows)

        return ETFBasketInput(
            baskets=baskets,
            as_of_date=reported_date,
            weight_unit=weight_unit,
            source_provider=source_provider,
            source_reference=source_reference,
            basket_source_priority="audited_json_override",
            etf_codes=tuple(sorted(baskets)),
            constituent_codes={
                code: tuple(str(item["stock_code"]) for item in items)
                for code, items in baskets.items()
            },
            cross_check_status="not_run",
            cross_check_detail="audited JSON override bypassed automatic source comparison",
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Explicitly refresh effective-dated SW sector ETF exposure mappings",
    )
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--level", type=int, choices=(1, 2), required=True)
    parser.add_argument("--provider", choices=("auto", "miniqmt", "akshare"), default="auto")
    parser.add_argument("--min-coverage", type=float, default=0.80)
    parser.add_argument("--mapping-version", default="exposure_v1")
    parser.add_argument("--config-hash", required=True)
    parser.add_argument(
        "--basket-json",
        type=Path,
        help=(
            "Audited ETF basket JSON containing provider_reported_date, weight_unit, "
            "source_provider, source_reference and per-ETF constituent weights"
        ),
    )
    return parser


def run_refresh(
    *,
    target_date: date,
    sector_level: int,
    provider_name: str,
    min_coverage: float,
    mapping_version: str,
    config_hash: str,
    basket_json_path: Path | None = None,
    query: Callable[[str, tuple[object, ...]], list[dict[str, Any]]] | None = None,
    membership_provider: MembershipProvider | None = None,
    basket_provider: BasketProvider | None = None,
    miniqmt_provider: BasketProvider | None = None,
    akshare_provider: BasketProvider | None = None,
    ensure_schema: Callable[[], None] | None = None,
    refresh: Callable[..., object] = refresh_sector_etf_mapping,
    progress: Callable[[str], None] | None = None,
) -> int:
    """Refresh every locally configured sector for one exact target date."""

    if not 0 <= min_coverage <= 1:
        raise ValueError("min_coverage must be between zero and one")
    if sector_level not in (1, 2):
        raise ValueError("sector_level must be 1 or 2")
    if provider_name not in {"auto", "miniqmt", "akshare"}:
        raise ValueError(f"unsupported ETF provider: {provider_name}")

    if query is None:
        from data_ingestion.db_config import execute_query

        query = execute_query
    if ensure_schema is None:
        from .mapping import ensure_mapping_schema

        ensure_schema = ensure_mapping_schema
    report = progress or (lambda _message: None)
    ensure_schema()
    report("[refresh] mapping schema ready")

    rows = query(
        f"""SELECT DISTINCT status.sector_{sector_level} AS sector_name
              FROM trade_stock_status AS status
              WHERE status.sector_{sector_level} IS NOT NULL
                AND TRIM(status.sector_{sector_level}) <> ''
              ORDER BY status.sector_{sector_level} ASC""",
        (),
    )
    sector_names = tuple(
        str(row["sector_name"]) for row in rows
        if row.get("sector_name") is not None and str(row["sector_name"]).strip()
    )
    report(f"[refresh] loaded {len(sector_names)} SW{sector_level} sectors")
    membership = membership_provider or LocalSWMembershipProvider(query=query)
    if basket_provider is not None and basket_json_path is not None:
        raise ValueError("basket_provider and basket_json_path are mutually exclusive")
    if basket_provider is not None:
        report(f"[refresh] loading {_provider_label(provider_name)} ETF baskets")
        basket_input = basket_provider.load(target_date)
    elif basket_json_path is not None:
        report("[refresh] loading audited JSON ETF baskets")
        basket_input = AuditedJSONBasketProvider(basket_json_path).load(target_date)
    elif provider_name == "auto":
        report("[refresh] loading MiniQMT ETF baskets")
        miniqmt_input = (miniqmt_provider or MiniQMTETFProvider()).load(target_date)
        report(_basket_progress("MiniQMT", miniqmt_input))
        report("[refresh] loading AKShare ETF baskets")
        akshare_input = (akshare_provider or AKShareETFProvider(progress=report)).load(target_date)
        report(_basket_progress("AKShare", akshare_input))
        basket_input = select_freshest_basket(
            miniqmt_input,
            akshare_input,
            target_date,
            min_coverage=min_coverage,
        )
    elif provider_name == "miniqmt" and miniqmt_provider is not None:
        report("[refresh] loading MiniQMT ETF baskets")
        basket_input = miniqmt_provider.load(target_date)
    elif provider_name == "akshare" and akshare_provider is not None:
        report("[refresh] loading AKShare ETF baskets")
        basket_input = akshare_provider.load(target_date)
    else:
        report(f"[refresh] loading {_provider_label(provider_name)} ETF baskets")
        basket_input = _configured_basket_provider(provider_name).load(target_date)
    if provider_name != "auto":
        report(_basket_progress(basket_input.source_provider or provider_name, basket_input))
    report(_selected_basket_progress(basket_input))

    count = 0
    freshness_counts = {"fresh": 0, "aging": 0, "stale": 0}
    quality_failure_count = 0
    for index, sector_name in enumerate(sector_names, start=1):
        report(f"[refresh] sector {index}/{len(sector_names)}: {sector_name}")
        result = refresh(
            sector_name=sector_name,
            sector_level=sector_level,
            target_date=target_date,
            membership_provider=membership,
            basket_provider=lambda _target, value=basket_input: value,
            min_coverage=min_coverage,
            mapping_version=mapping_version,
            config_hash=config_hash,
        )
        persisted_rows = int(getattr(result, "persisted_rows"))
        count += persisted_rows
        report(f"[refresh] sector {index}/{len(sector_names)}: persisted {persisted_rows} rows")
        if _is_quality_failure(result):
            quality_failure_count += persisted_rows
        elif basket_input.as_of_date is not None:
            status = assess_holdings_freshness(basket_input.as_of_date, target_date).status
            freshness_counts[status] += persisted_rows
    print(
        f"{target_date.isoformat()}: refreshed {count} mapping rows across {len(sector_names)} sectors; "
        f"chosen_source={basket_input.source_provider}; "
        f"fresh={freshness_counts['fresh']} aging={freshness_counts['aging']} "
        f"stale={freshness_counts['stale']} quality_failure={quality_failure_count}",
    )
    return count


def main(
    argv: list[str] | None = None,
    *,
    run_refresh_fn: Callable[..., int] = run_refresh,
) -> int:
    args = build_parser().parse_args(argv)
    refresh_kwargs = dict(
        target_date=date.fromisoformat(args.as_of_date),
        sector_level=args.level,
        provider_name=args.provider,
        min_coverage=args.min_coverage,
        mapping_version=args.mapping_version,
        config_hash=args.config_hash,
    )
    if args.basket_json is not None:
        refresh_kwargs["basket_json_path"] = args.basket_json
    run_refresh_fn(**refresh_kwargs, progress=print)
    return 0


def _configured_basket_provider(provider_name: str) -> BasketProvider:
    if provider_name == "miniqmt":
        return MiniQMTETFProvider()
    return AKShareETFProvider()


def _is_quality_failure(result: object) -> bool:
    """Identify persisted failure events without changing the DB migration boundary."""

    if getattr(result, "quality_issue", None) is not None:
        return True
    assessment = getattr(result, "assessment", None)
    return assessment is not None and not bool(getattr(assessment, "eligible", ()))


def _basket_progress(label: str, basket: ETFBasketInput) -> str:
    label = _provider_label(label)
    if basket.available:
        reported_date = basket.as_of_date.isoformat() if basket.as_of_date is not None else "unknown"
        return f"[refresh] {label}: available; etfs={len(basket.baskets)}; reported_date={reported_date}"
    reason = basket.quality_issue.code if basket.quality_issue is not None else "unavailable"
    return f"[refresh] {label}: unavailable; reason={reason}"


def _selected_basket_progress(basket: ETFBasketInput) -> str:
    label = _provider_label(str(basket.source_provider or "auto"))
    if not basket.available:
        return f"[refresh] no complete ETF basket selected; reason={basket.quality_issue.code if basket.quality_issue else 'unavailable'}"
    reported_date = basket.as_of_date.isoformat() if basket.as_of_date is not None else "unknown"
    return f"[refresh] selected {label} ETF baskets; etfs={len(basket.baskets)}; reported_date={reported_date}"


def _provider_label(value: str) -> str:
    """Format known provider identifiers consistently in operator output."""

    return {"miniqmt": "MiniQMT", "akshare": "AKShare"}.get(value.casefold(), value)


def _strict_iso_date(value: object) -> date:
    if not isinstance(value, str):
        raise ValueError("provider_reported_date must be an ISO date string")
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("provider_reported_date must be an ISO date string") from exc
    if parsed.isoformat() != value:
        raise ValueError("provider_reported_date must use YYYY-MM-DD")
    return parsed


def _nonblank_string(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty string")
    return value.strip()


if __name__ == "__main__":
    raise SystemExit(main())
