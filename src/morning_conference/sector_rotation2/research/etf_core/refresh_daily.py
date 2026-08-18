"""Explicit CLI for refreshing exposure-derived sector/ETF mappings.

This writer is intentionally separate from ``run_daily``: building candidate
snapshots remains read-only with respect to mapping data.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable
from datetime import date
from typing import Any

from .providers import (
    AKShareETFProvider,
    BasketProvider,
    LocalSWMembershipProvider,
    MembershipProvider,
    MiniQMTETFProvider,
    ProviderQualityIssue,
    refresh_sector_etf_mapping,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Explicitly refresh effective-dated SW sector ETF exposure mappings",
    )
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--level", type=int, choices=(1, 2), required=True)
    parser.add_argument("--provider", choices=("miniqmt", "akshare"), default="miniqmt")
    parser.add_argument("--min-coverage", type=float, default=0.80)
    parser.add_argument("--mapping-version", default="exposure_v1")
    parser.add_argument("--config-hash", required=True)
    return parser


def run_refresh(
    *,
    target_date: date,
    sector_level: int,
    provider_name: str,
    min_coverage: float,
    mapping_version: str,
    config_hash: str,
    query: Callable[[str, tuple[object, ...]], list[dict[str, Any]]] | None = None,
    membership_provider: MembershipProvider | None = None,
    basket_provider: BasketProvider | None = None,
    ensure_schema: Callable[[], None] | None = None,
    refresh: Callable[..., object] = refresh_sector_etf_mapping,
) -> int:
    """Refresh every locally configured sector for one exact target date."""

    if not 0 <= min_coverage <= 1:
        raise ValueError("min_coverage must be between zero and one")
    if sector_level not in (1, 2):
        raise ValueError("sector_level must be 1 or 2")
    if provider_name not in {"miniqmt", "akshare"}:
        raise ValueError(f"unsupported ETF provider: {provider_name}")

    if query is None:
        from data_ingestion.db_config import execute_query

        query = execute_query
    if ensure_schema is None:
        from .mapping import ensure_mapping_schema

        ensure_schema = ensure_mapping_schema
    ensure_schema()

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
    membership = membership_provider or LocalSWMembershipProvider(query=query)
    basket_source = basket_provider or _configured_basket_provider(provider_name)
    basket_input = basket_source.load(target_date)

    count = 0
    for sector_name in sector_names:
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
        count += int(getattr(result, "persisted_rows"))
    print(f"{target_date.isoformat()}: refreshed {count} mapping rows across {len(sector_names)} sectors")
    return count


def main(
    argv: list[str] | None = None,
    *,
    run_refresh_fn: Callable[..., int] = run_refresh,
) -> int:
    args = build_parser().parse_args(argv)
    run_refresh_fn(
        target_date=date.fromisoformat(args.as_of_date),
        sector_level=args.level,
        provider_name=args.provider,
        min_coverage=args.min_coverage,
        mapping_version=args.mapping_version,
        config_hash=args.config_hash,
    )
    return 0


def _configured_basket_provider(provider_name: str) -> BasketProvider:
    if provider_name == "miniqmt":
        return MiniQMTETFProvider()
    # AKShare is deliberately not called live.  Without an injected payload
    # and immutable provenance it produces auditable quality failures only.
    return AKShareETFProvider()


if __name__ == "__main__":
    raise SystemExit(main())

