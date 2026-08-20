"""Financial data providers for Repair Alpha V1.

The provider stack mirrors the ETF Core pattern: a base protocol, a
primary concrete provider (MiniQMT) and a secondary provider for
discrepancy resolution.  Providers expose raw financial statement rows
and capital structure rows; the PIT resolver picks the latest visible row
for any given research date.
"""

from .base import (
    CapitalRow,
    FinancialProvider,
    FinancialRawRow,
    ProviderQualityIssue,
    coerce_numeric,
)
from .miniqmt import MiniQMTProvider
from .secondary import SecondaryProvider

__all__ = [
    "CapitalRow",
    "FinancialProvider",
    "FinancialRawRow",
    "MiniQMTProvider",
    "ProviderQualityIssue",
    "SecondaryProvider",
    "coerce_numeric",
]

