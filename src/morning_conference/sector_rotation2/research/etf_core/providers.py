"""Strict, injectable inputs for SW membership and ETF exposure mappings.

Provider adapters deliberately return unavailable results instead of guessing
weights, units, or source dates.  This keeps redemption-list quantities and
stale holdings from silently becoming daily exposure mappings.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from datetime import date
import math
from typing import Any, Literal, Protocol

from .exposure import ExposureAssessment, assess_sector_etfs


WeightUnit = Literal["decimal", "percent"]


@dataclass(frozen=True)
class ProviderQualityIssue:
    """Machine-readable reason why a provider input cannot be mapped."""

    code: str
    detail: str


@dataclass(frozen=True)
class ProviderProvenance:
    """Immutable provider-reported metadata accompanying a basket payload."""

    provider_reported_date: date | str | None
    weight_unit: str | None
    source_reference: str | None


@dataclass(frozen=True)
class SWMembershipInput:
    """One sector membership snapshot, or a structured unavailable result."""

    sector_name: str
    sector_level: int
    member_codes: tuple[str, ...] = ()
    as_of_date: date | None = None
    asof_mode: str = "current_mapping"
    source_provider: str = "trade_stock_status"
    quality_issue: ProviderQualityIssue | None = None

    @property
    def available(self) -> bool:
        return self.quality_issue is None and bool(self.member_codes) and self.as_of_date is not None

    @classmethod
    def unavailable(
        cls,
        *,
        sector_name: str,
        sector_level: int,
        issue: ProviderQualityIssue,
        source_provider: str = "trade_stock_status",
        as_of_date: date | None = None,
    ) -> "SWMembershipInput":
        return cls(
            sector_name=sector_name,
            sector_level=sector_level,
            source_provider=source_provider,
            as_of_date=as_of_date,
            quality_issue=issue,
        )


@dataclass(frozen=True)
class ETFBasketInput:
    """Normalized ETF component rows plus their explicitly declared metadata."""

    baskets: dict[str, tuple[dict[str, object], ...]]
    as_of_date: date | None
    weight_unit: WeightUnit | None
    source_provider: str
    source_reference: str | None = None
    quality_issue: ProviderQualityIssue | None = None

    @property
    def available(self) -> bool:
        return (
            self.quality_issue is None
            and bool(self.baskets)
            and self.as_of_date is not None
            and self.weight_unit in {"decimal", "percent"}
            and bool(str(self.source_provider or "").strip())
            and bool(str(self.source_reference or "").strip())
        )

    @classmethod
    def unavailable(
        cls,
        *,
        source_provider: str,
        issue: ProviderQualityIssue,
        as_of_date: date | None = None,
        weight_unit: WeightUnit | None = None,
        source_reference: str | None = None,
    ) -> "ETFBasketInput":
        return cls(
            baskets={},
            as_of_date=as_of_date,
            weight_unit=weight_unit,
            source_provider=source_provider,
            source_reference=source_reference,
            quality_issue=issue,
        )


@dataclass(frozen=True)
class MappingRefreshResult:
    """Observable outcome of refreshing one sector/date mapping event."""

    persisted_rows: int
    assessment: ExposureAssessment
    quality_issue: ProviderQualityIssue | None = None


class MembershipProvider(Protocol):
    def load(self, sector_name: str, sector_level: int, target_date: date) -> SWMembershipInput: ...


class BasketProvider(Protocol):
    def load(self, target_date: date) -> ETFBasketInput: ...


class LocalSWMembershipProvider:
    """Read the current SW1/SW2 membership stored in ``trade_stock_status``.

    The table is a current-state mapping, not a point-in-time history.  It is
    therefore valid only for the provider's injected current date.
    """

    def __init__(
        self,
        *,
        query: Callable[[str, tuple[object, ...]], list[dict[str, Any]]] | None = None,
        current_date: Callable[[], date] = date.today,
    ) -> None:
        self._query = query
        self._current_date = current_date

    def load(self, sector_name: str, sector_level: int, target_date: date) -> SWMembershipInput:
        field = _sector_field(sector_level)
        observed_date = self._current_date()
        if target_date != observed_date:
            return SWMembershipInput.unavailable(
                sector_name=sector_name,
                sector_level=sector_level,
                as_of_date=observed_date,
                issue=ProviderQualityIssue(
                    "membership_date_mismatch",
                    f"trade_stock_status current_mapping is dated {observed_date.isoformat()}, target is {target_date.isoformat()}",
                ),
            )
        query = self._query
        if query is None:
            from data_ingestion.db_config import execute_query

            query = execute_query
        rows = query(
            f"""SELECT DISTINCT status.stock_code FROM trade_stock_status AS status
                  WHERE status.{field} = %s ORDER BY status.stock_code ASC""",
            (sector_name,),
        )
        member_codes = tuple(
            str(row["stock_code"]) for row in rows
            if row.get("stock_code") is not None and str(row["stock_code"]).strip()
        )
        if not member_codes:
            return SWMembershipInput.unavailable(
                sector_name=sector_name,
                sector_level=sector_level,
                as_of_date=observed_date,
                issue=ProviderQualityIssue(
                    "missing_sector_members",
                    f"trade_stock_status has no members for sector_{sector_level}={sector_name}",
                ),
            )
        return SWMembershipInput(
            sector_name=sector_name,
            sector_level=sector_level,
            member_codes=member_codes,
            as_of_date=observed_date,
            asof_mode="current_mapping",
            source_provider="trade_stock_status",
        )


class MiniQMTETFProvider:
    """Extract weighted ETF baskets from MiniQMT redemption-list records.

    ``xtdata.get_etf_info`` commonly exposes only ``成份股代码`` in
    ``成份股信息``.  Such rows are unusable for exposure and are rejected; no
    equal weight or redemption quantity is ever substituted.
    """

    def __init__(
        self,
        *,
        client: object | None = None,
        provenance: ProviderProvenance | None = None,
    ) -> None:
        self._client = client
        self._provenance = provenance

    def load(self, target_date: date) -> ETFBasketInput:
        client = self._client
        if client is None:
            from xtquant import xtdata

            client = xtdata
        try:
            client.download_etf_info()
            raw = client.get_etf_info()
        except Exception as exc:
            return _basket_unavailable("miniqmt", "provider_error", str(exc))
        if not isinstance(raw, Mapping) or not raw:
            return _basket_unavailable("miniqmt", "missing_etf_universe", "get_etf_info returned no ETF records")
        return _parse_miniqmt_records(
            raw,
            target_date=target_date,
            provenance=self._provenance,
        )


class AKShareETFProvider:
    """Parse an injected AKShare holdings frame with explicit provenance.

    The adapter intentionally has no implicit endpoint call: callers must
    inject a dataframe or a client/loader.  AKShare holdings can be quarterly,
    so a declared source date must exactly match the mapping target date.
    """

    def __init__(
        self,
        *,
        dataframe: object | None = None,
        client: object | None = None,
        provenance: ProviderProvenance | None = None,
    ) -> None:
        self._dataframe = dataframe
        self._client = client
        self._provenance = provenance

    def load(self, target_date: date) -> ETFBasketInput:
        try:
            data = self._dataframe if self._dataframe is not None else _load_injected_akshare_client(self._client)
            rows = _records(data)
        except Exception as exc:
            return ETFBasketInput.unavailable(
                source_provider="akshare",
                issue=ProviderQualityIssue("provider_error", str(exc)),
            )
        payload_metadata = rows[0] if rows else {}
        source_date, unit, source_reference, issue = _resolve_provenance(
            explicit=self._provenance,
            payload=payload_metadata,
            target_date=target_date,
            default_source_reference=None,
        )
        if issue is not None:
            return ETFBasketInput.unavailable(
                source_provider="akshare", issue=issue, as_of_date=source_date,
                weight_unit=unit, source_reference=source_reference,
            )
        if self._provenance is None:
            issue = _validate_akshare_row_provenance(
                rows,
                source_date=source_date,
                weight_unit=unit,
                source_reference=source_reference,
            )
            if issue is not None:
                return ETFBasketInput.unavailable(
                    source_provider="akshare", issue=issue, as_of_date=source_date,
                    weight_unit=unit, source_reference=source_reference,
                )
        if not rows:
            return ETFBasketInput.unavailable(
                source_provider="akshare",
                issue=ProviderQualityIssue("missing_etf_baskets", "holdings source returned no rows"),
                as_of_date=source_date,
                weight_unit=unit,
                source_reference=source_reference,
            )
        baskets: dict[str, list[dict[str, object]]] = {}
        for row in rows:
            etf_code = _first_value(row, ("etf_code", "基金代码", "基金编码"))
            stock_code = _first_value(row, ("stock_code", "股票代码", "证券代码", "持仓代码"))
            weight = _first_value(row, ("weight", "持仓占比", "权重", "占净值比例"))
            if etf_code is None:
                return _basket_unavailable("akshare", "missing_etf_code", "holdings row has no recognized ETF code", source_date, unit, source_reference)
            if stock_code is None:
                return _basket_unavailable("akshare", "missing_constituent_code", f"{etf_code} row has no recognized stock code", source_date, unit, source_reference)
            if weight is None:
                return _basket_unavailable("akshare", "missing_constituent_weight", f"{etf_code}/{stock_code} has no recognized weight", source_date, unit, source_reference)
            try:
                numeric_weight = _numeric_weight(weight)
            except ValueError:
                return _basket_unavailable("akshare", "invalid_constituent_weight", f"{etf_code}/{stock_code} has invalid weight", source_date, unit, source_reference)
            baskets.setdefault(str(etf_code), []).append({"stock_code": str(stock_code), "weight": numeric_weight})
        return ETFBasketInput(
            baskets={code: tuple(items) for code, items in baskets.items()},
            as_of_date=source_date,
            weight_unit=unit,
            source_provider="akshare",
            source_reference=source_reference,
        )


def refresh_sector_etf_mapping(
    *,
    sector_name: str,
    sector_level: int,
    target_date: date,
    membership_provider: MembershipProvider | Callable[..., SWMembershipInput],
    basket_provider: BasketProvider | Callable[..., ETFBasketInput],
    min_coverage: float,
    mapping_version: str,
    config_hash: str,
    persist: Callable[..., int] | None = None,
) -> MappingRefreshResult:
    """Assess and persist one mapping event without ever using stale inputs."""

    membership = _invoke_membership_provider(
        membership_provider, sector_name, sector_level, target_date,
    )
    if not membership.available:
        return _persist_unavailable(
            sector_name=sector_name, sector_level=sector_level, target_date=target_date,
            membership=membership, baskets=None,
            issue=membership.quality_issue or ProviderQualityIssue("missing_sector_members", "membership is unavailable"),
            min_coverage=min_coverage, mapping_version=mapping_version, config_hash=config_hash,
            persist=persist,
        )
    baskets = _invoke_basket_provider(basket_provider, target_date)
    if not baskets.available:
        return _persist_unavailable(
            sector_name=sector_name, sector_level=sector_level, target_date=target_date,
            membership=membership, baskets=baskets,
            issue=baskets.quality_issue or _basket_contract_issue(baskets),
            min_coverage=min_coverage, mapping_version=mapping_version, config_hash=config_hash,
            persist=persist,
        )
    if membership.as_of_date != target_date or baskets.as_of_date != target_date:
        issue = ProviderQualityIssue(
            "source_date_mismatch",
            f"membership={membership.as_of_date}, constituents={baskets.as_of_date}, target={target_date}",
        )
        return _persist_unavailable(
            sector_name=sector_name, sector_level=sector_level, target_date=target_date,
            membership=membership, baskets=baskets, issue=issue,
            min_coverage=min_coverage, mapping_version=mapping_version, config_hash=config_hash,
            persist=persist,
        )
    try:
        assessment = assess_sector_etfs(
            membership.member_codes,
            baskets.baskets,
            min_coverage,
            weight_unit=baskets.weight_unit,
        )
    except (TypeError, ValueError) as exc:
        issue = ProviderQualityIssue("invalid_etf_basket", str(exc))
        return _persist_unavailable(
            sector_name=sector_name, sector_level=sector_level, target_date=target_date,
            membership=membership, baskets=baskets, issue=issue,
            min_coverage=min_coverage, mapping_version=mapping_version, config_hash=config_hash,
            persist=persist,
        )
    persist_fn = persist or _default_persist()
    count = persist_fn(
        sector_name=sector_name,
        sector_level=sector_level,
        as_of_date=target_date,
        assessment=assessment,
        source_as_of_date=baskets.as_of_date,
        source_provider=baskets.source_provider,
        membership_as_of_date=membership.as_of_date,
        constituent_as_of_date=baskets.as_of_date,
        mapping_version=mapping_version,
        config_hash=config_hash,
        weight_unit=baskets.weight_unit,
        source_reference=baskets.source_reference,
        min_coverage=min_coverage,
    )
    return MappingRefreshResult(count, assessment)


def _persist_unavailable(
    *,
    sector_name: str,
    sector_level: int,
    target_date: date,
    membership: SWMembershipInput,
    baskets: ETFBasketInput | None,
    issue: ProviderQualityIssue,
    min_coverage: float,
    mapping_version: str,
    config_hash: str,
    persist: Callable[..., int] | None,
) -> MappingRefreshResult:
    assessment = ExposureAssessment(eligible=[], rejected=[])
    persist_fn = persist or _default_persist()
    count = persist_fn(
        sector_name=sector_name,
        sector_level=sector_level,
        as_of_date=target_date,
        assessment=assessment,
        source_as_of_date=baskets.as_of_date if baskets else None,
        source_provider=(str(baskets.source_provider or "").strip() or "unknown") if baskets else membership.source_provider,
        membership_as_of_date=membership.as_of_date,
        constituent_as_of_date=baskets.as_of_date if baskets else None,
        mapping_version=mapping_version,
        config_hash=config_hash,
        weight_unit=baskets.weight_unit if baskets else None,
        source_reference=baskets.source_reference if baskets else None,
        min_coverage=min_coverage,
        membership_asof_mode=membership.asof_mode,
        quality_failure_reason=f"{issue.code}: {issue.detail}",
    )
    return MappingRefreshResult(count, assessment, issue)


def _parse_miniqmt_records(
    raw: Mapping[object, object],
    *,
    target_date: date,
    provenance: ProviderProvenance | None,
) -> ETFBasketInput:
    baskets: dict[str, tuple[dict[str, object], ...]] = {}
    common_date: date | None = None
    common_unit: WeightUnit | None = None
    common_reference: str | None = None
    for key, value in raw.items():
        if not isinstance(value, Mapping):
            return _basket_unavailable("miniqmt", "invalid_etf_record", f"ETF record {key!r} is not a mapping")
        etf_code = _first_value(value, ("etf_code", "stock_code", "code", "基金代码")) or key
        if etf_code is None or not str(etf_code).strip():
            return _basket_unavailable("miniqmt", "missing_etf_code", "ETF record has no recognized code")
        source_date, unit, source_reference, issue = _resolve_provenance(
            explicit=provenance,
            payload=value,
            target_date=target_date,
            default_source_reference="xtdata.get_etf_info",
        )
        if issue is not None:
            return ETFBasketInput.unavailable(
                source_provider="miniqmt", issue=issue, as_of_date=source_date,
                weight_unit=unit, source_reference=source_reference,
            )
        if common_date is not None and source_date != common_date:
            return _basket_unavailable("miniqmt", "inconsistent_source_dates", "ETF records have different source dates")
        if common_unit is not None and unit != common_unit:
            return _basket_unavailable("miniqmt", "inconsistent_weight_units", "ETF records have different weight units", source_date)
        if common_reference is not None and source_reference != common_reference:
            return _basket_unavailable("miniqmt", "inconsistent_source_references", "ETF records have different source references", source_date, unit)
        common_date, common_unit, common_reference = source_date, unit, source_reference
        components = _first_value(value, ("成份股信息", "components", "constituents"))
        component_rows = _component_records(components)
        if not component_rows:
            return _basket_unavailable("miniqmt", "missing_etf_components", f"{etf_code} has no recognized component rows", source_date, unit, source_reference)
        parsed: list[dict[str, object]] = []
        for component_key, component in component_rows:
            stock_code = _first_value(component, ("成份股代码", "stock_code", "code", "证券代码")) or component_key
            weight = _first_value(component, ("weight", "权重", "成份股权重", "持仓占比"))
            if stock_code is None or not str(stock_code).strip():
                return _basket_unavailable("miniqmt", "missing_constituent_code", f"{etf_code} has a component without a recognized code", source_date, unit, source_reference)
            if weight is None:
                return _basket_unavailable("miniqmt", "missing_constituent_weight", f"{etf_code}/{stock_code} has no recognized weight", source_date, unit, source_reference)
            try:
                numeric_weight = _numeric_weight(weight)
            except ValueError:
                return _basket_unavailable("miniqmt", "invalid_constituent_weight", f"{etf_code}/{stock_code} has invalid weight", source_date, unit, source_reference)
            parsed.append({"stock_code": str(stock_code), "weight": numeric_weight})
        baskets[str(etf_code)] = tuple(parsed)
    return ETFBasketInput(
        baskets=baskets,
        as_of_date=common_date,
        weight_unit=common_unit,
        source_provider="miniqmt",
        source_reference=common_reference,
    )


def _component_records(value: object) -> list[tuple[object | None, Mapping[str, object]]]:
    if isinstance(value, Mapping):
        return [(key, item) for key, item in value.items() if isinstance(item, Mapping)]
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return [(None, item) for item in value if isinstance(item, Mapping)]
    return []


def _records(data: object) -> list[Mapping[str, object]]:
    if data is None:
        return []
    if hasattr(data, "to_dict"):
        rows = data.to_dict("records")
    elif isinstance(data, Sequence) and not isinstance(data, (str, bytes)):
        rows = data
    else:
        raise TypeError("holdings source must be a dataframe or sequence of rows")
    if not all(isinstance(row, Mapping) for row in rows):
        raise TypeError("holdings rows must be mappings")
    return list(rows)


def _load_injected_akshare_client(client: object | None) -> object:
    if client is None:
        raise ValueError("AKShare dataframe or client/loader is required")
    if callable(client):
        return client()
    loader = getattr(client, "load_etf_holdings", None)
    if callable(loader):
        return loader()
    raise TypeError("AKShare client must be callable or expose load_etf_holdings()")


def _invoke_membership_provider(
    provider: MembershipProvider | Callable[..., SWMembershipInput],
    sector_name: str,
    sector_level: int,
    target_date: date,
) -> SWMembershipInput:
    load = getattr(provider, "load", None)
    return load(sector_name, sector_level, target_date) if callable(load) else provider(sector_name, sector_level, target_date)


def _invoke_basket_provider(
    provider: BasketProvider | Callable[..., ETFBasketInput],
    target_date: date,
) -> ETFBasketInput:
    load = getattr(provider, "load", None)
    return load(target_date) if callable(load) else provider(target_date)


def _default_persist() -> Callable[..., int]:
    from .mapping import persist_exposure_assessment

    return persist_exposure_assessment


def _validate_source_date(value: object, target_date: date) -> tuple[date | None, ProviderQualityIssue | None]:
    if value is None or value == "":
        return None, ProviderQualityIssue("missing_source_date", "provider did not declare a source as-of date")
    try:
        parsed = value if type(value) is date else date.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None, ProviderQualityIssue("invalid_source_date", f"invalid source as-of date: {value!r}")
    if parsed != target_date:
        return parsed, ProviderQualityIssue(
            "source_date_mismatch",
            f"provider source date is {parsed.isoformat()}, target is {target_date.isoformat()}",
        )
    return parsed, None


def _resolve_provenance(
    *,
    explicit: ProviderProvenance | None,
    payload: Mapping[object, object],
    target_date: date,
    default_source_reference: str | None,
) -> tuple[date | None, WeightUnit | None, str | None, ProviderQualityIssue | None]:
    if explicit is not None:
        raw_date = explicit.provider_reported_date
        raw_unit = explicit.weight_unit
        source_reference = explicit.source_reference
    else:
        raw_date = _first_value(payload, ("source_as_of_date", "as_of_date", "截止日期", "日期"))
        raw_unit = _first_value(payload, ("weight_unit", "unit", "权重单位"))
        source_reference = _first_value(payload, ("source_reference", "source_ref", "来源引用"))
        if source_reference is None:
            source_reference = default_source_reference
    source_date, issue = _validate_source_date(raw_date, target_date)
    if issue is not None:
        return source_date, None, _clean_reference(source_reference), issue
    unit, issue = _validate_weight_unit(raw_unit)
    if issue is not None:
        return source_date, unit, _clean_reference(source_reference), issue
    reference = _clean_reference(source_reference)
    if reference is None:
        return source_date, unit, None, ProviderQualityIssue(
            "missing_source_reference", "provider provenance has no source reference",
        )
    return source_date, unit, reference, None


def _validate_akshare_row_provenance(
    rows: Sequence[Mapping[str, object]],
    *,
    source_date: date | None,
    weight_unit: WeightUnit | None,
    source_reference: str | None,
) -> ProviderQualityIssue | None:
    for row in rows[1:]:
        raw_date = _first_value(row, ("source_as_of_date", "as_of_date", "截止日期", "日期"))
        try:
            row_date = raw_date if type(raw_date) is date else date.fromisoformat(str(raw_date))
        except (TypeError, ValueError):
            row_date = None
        if row_date != source_date:
            return ProviderQualityIssue(
                "inconsistent_provider_reported_date",
                f"AKShare rows report different source dates: {source_date} and {raw_date!r}",
            )
        raw_unit = _first_value(row, ("weight_unit", "unit", "权重单位"))
        row_unit, unit_issue = _validate_weight_unit(raw_unit)
        if unit_issue is not None or row_unit != weight_unit:
            return ProviderQualityIssue(
                "inconsistent_weight_unit",
                f"AKShare rows report different weight units: {weight_unit!r} and {raw_unit!r}",
            )
        row_reference = _clean_reference(
            _first_value(row, ("source_reference", "source_ref", "来源引用")),
        )
        if row_reference != source_reference:
            return ProviderQualityIssue(
                "inconsistent_source_reference",
                f"AKShare rows report different source references: {source_reference!r} and {row_reference!r}",
            )
    return None


def _basket_contract_issue(baskets: ETFBasketInput) -> ProviderQualityIssue:
    if not str(baskets.source_provider or "").strip():
        return ProviderQualityIssue("missing_source_provider", "ETF basket source provider is empty")
    if not (baskets.source_reference or "").strip():
        return ProviderQualityIssue("missing_source_reference", "ETF basket source reference is empty")
    if baskets.as_of_date is None:
        return ProviderQualityIssue("missing_source_date", "ETF basket source date is missing")
    if baskets.weight_unit not in {"decimal", "percent"}:
        return ProviderQualityIssue("missing_weight_unit", "ETF basket weight unit is missing or invalid")
    return ProviderQualityIssue("missing_etf_baskets", "ETF baskets are unavailable")


def _clean_reference(value: object) -> str | None:
    if value is None:
        return None
    reference = str(value).strip()
    return reference or None


def _validate_weight_unit(value: object) -> tuple[WeightUnit | None, ProviderQualityIssue | None]:
    if value is None or str(value).strip() == "":
        return None, ProviderQualityIssue("missing_weight_unit", "provider did not declare a weight unit")
    normalized = str(value).strip().lower()
    aliases: dict[str, WeightUnit] = {
        "decimal": "decimal",
        "percent": "percent",
        "%": "percent",
        "百分比": "percent",
    }
    unit = aliases.get(normalized)
    if unit is None:
        return None, ProviderQualityIssue("invalid_weight_unit", f"unsupported weight unit: {value!r}")
    return unit, None


def _numeric_weight(value: object) -> float:
    try:
        weight = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"invalid weight: {value!r}") from exc
    if not math.isfinite(weight) or weight < 0:
        raise ValueError(f"invalid weight: {value!r}")
    return weight


def _first_value(row: Mapping[object, object], names: Sequence[str]) -> object | None:
    for name in names:
        if name in row and row[name] is not None and str(row[name]).strip() != "":
            return row[name]
    return None


def _basket_unavailable(
    provider: str,
    code: str,
    detail: str,
    as_of_date: date | None = None,
    weight_unit: WeightUnit | None = None,
    source_reference: str | None = None,
) -> ETFBasketInput:
    return ETFBasketInput.unavailable(
        source_provider=provider,
        issue=ProviderQualityIssue(code, detail),
        as_of_date=as_of_date,
        weight_unit=weight_unit,
        source_reference=source_reference,
    )


def _sector_field(sector_level: int) -> str:
    if sector_level not in (1, 2):
        raise ValueError("sector_level must be 1 or 2")
    return f"sector_{sector_level}"


# Descriptive compatibility alias for callers that name the backing table.
TradeStockStatusMembershipProvider = LocalSWMembershipProvider
