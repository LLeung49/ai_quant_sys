import pytest

from morning_conference.sector_rotation2.research.etf_core.exposure import (
    aggregate_constituents,
    assess_sector_etfs,
    normalize_stock_code,
    rank_sector_etfs,
)


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("600000", "600000"),
        ("600000.SH", "600000"),
        ("SH600000", "600000"),
        ("000001.SZ", "000001"),
        ("sz.000001", "000001"),
        (" 300750 ", "300750"),
    ],
)
def test_normalize_stock_code_accepts_six_digit_market_variants(raw, expected):
    assert normalize_stock_code(raw) == expected


def test_aggregate_constituents_supports_code_alias_and_sums_duplicates():
    rows = [
        {"stock_code": "600000.SH", "weight": 0.12},
        {"code": "600000", "weight": 0.08},
        {"stock_code": "000001.SZ", "weight": 0.20},
    ]

    assert aggregate_constituents(rows) == {
        "600000": pytest.approx(0.20),
        "000001": pytest.approx(0.20),
    }


def test_aggregate_constituents_rejects_missing_code_or_weight():
    with pytest.raises(ValueError, match="stock code"):
        aggregate_constituents([{"weight": 0.1}])
    with pytest.raises(ValueError, match="weight"):
        aggregate_constituents([{"stock_code": "600000"}])


def test_rank_sector_etfs_sums_normalized_percentage_weights_for_sw2_overlap():
    result = rank_sector_etfs(
        {"600000", "000001"},
        {
            "510300": [
                {"stock_code": "600000.SH", "weight": 50},
                {"stock_code": "000001.SZ", "weight": 30},
                {"stock_code": "300750.SZ", "weight": 20},
            ]
        },
        min_coverage=0.9,
        weight_unit="percent",
    )

    assert len(result) == 1
    assert result[0].etf_code == "510300"
    assert result[0].exposure_weight == pytest.approx(0.8)
    assert result[0].coverage_ratio == pytest.approx(1.0)


def test_rank_sector_etfs_requires_explicit_weight_unit():
    with pytest.raises(TypeError, match="weight_unit"):
        rank_sector_etfs(
            {"600000"},
            {"510300": [{"stock_code": "600000.SH", "weight": 0.5}]},
            min_coverage=0.0,
        )


def test_rank_sector_etfs_filters_small_percent_basket_below_coverage():
    result = rank_sector_etfs(
        {"600000"},
        {
            "510300": [
                {"stock_code": "600000.SH", "weight": 0.5},
                {"stock_code": "000001.SZ", "weight": 0.5},
            ]
        },
        min_coverage=0.9,
        weight_unit="percent",
    )

    assert result == []


def test_assessment_keeps_undercoverage_observation_for_mapping_quality_audit():
    assessment = assess_sector_etfs(
        {"600000"},
        {"510300": [{"stock_code": "600000.SH", "weight": 0.7}]},
        min_coverage=0.9,
        weight_unit="decimal",
    )

    assert assessment.eligible == []
    assert assessment.rejected[0].etf_code == "510300"
    assert assessment.rejected[0].coverage_ratio == pytest.approx(0.7)
    assert assessment.rejected[0].failure_reason == "coverage_below_minimum"


def test_rank_sector_etfs_blocks_baskets_below_minimum_weight_coverage():
    result = rank_sector_etfs(
        {"600000"},
        {"510300": [{"stock_code": "600000.SH", "weight": 0.7}]},
        min_coverage=0.9,
        weight_unit="decimal",
    )

    assert result == []


def test_rank_sector_etfs_returns_deterministically_sorted_top_three():
    result = rank_sector_etfs(
        {"600000"},
        {
            "510010": {"600000": 0.5, "000001": 0.5},
            "510020": {"600000": 0.5, "000001": 0.4},
            "510005": {"600000": 0.5, "000001": 0.5},
            "510999": {"600000": 0.9, "000001": 0.1},
            "510000": {},
        },
        min_coverage=0.9,
        weight_unit="decimal",
    )

    assert [item.etf_code for item in result] == ["510999", "510005", "510010"]


def test_rank_sector_etfs_explicit_percent_mode_accepts_one_percent_component():
    result = rank_sector_etfs(
        {"600000"},
        {
            "510300": [
                {"stock_code": "600000.SH", "weight": 50},
                {"stock_code": "000001.SZ", "weight": 1},
                {"stock_code": "300750.SZ", "weight": 49},
            ]
        },
        min_coverage=0.9,
        weight_unit="percent",
    )

    assert result[0].exposure_weight == pytest.approx(0.5)
    assert result[0].coverage_ratio == pytest.approx(1.0)


def test_rank_sector_etfs_explicit_decimal_mode_rejects_whole_percent_weight():
    with pytest.raises(ValueError, match="decimal"):
        rank_sector_etfs(
            {"600000"},
            {"510300": [{"stock_code": "600000.SH", "weight": 50}]},
            min_coverage=0.9,
            weight_unit="decimal",
        )


def test_rank_sector_etfs_rejects_unknown_weight_unit():
    with pytest.raises(ValueError, match="invalid weight unit"):
        rank_sector_etfs(
            {"600000"},
            {"510300": [{"stock_code": "600000.SH", "weight": 0.5}]},
            min_coverage=0.9,
            weight_unit="basis_points",
        )


@pytest.mark.parametrize(
    ("weights", "weight_unit"),
    [
        ([0.6, 0.400001], "decimal"),
        ([60, 40.0001], "percent"),
    ],
)
def test_rank_sector_etfs_rejects_baskets_above_full_weight_coverage(
    weights,
    weight_unit,
):
    with pytest.raises(ValueError, match="exceeds 100%"):
        rank_sector_etfs(
            {"600000"},
            {
                "510300": [
                    {"stock_code": "600000.SH", "weight": weights[0]},
                    {"stock_code": "000001.SZ", "weight": weights[1]},
                ]
            },
            min_coverage=0.9,
            weight_unit=weight_unit,
        )
