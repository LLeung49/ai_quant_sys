"""Read-only end-to-end contract check for the delayed-shadow cockpit."""

from morning_conference.sector_rotation2.api.research_router import (
    etf_candidates,
    latest_date,
    opportunities,
    stock_candidates,
    today_summary,
)


def _date_text(value):
    return value.isoformat() if hasattr(value, "isoformat") else str(value)


def main():
    latest = latest_date(level=2, snapshot_mode="delayed_shadow")
    day = _date_text(latest["as_of_date"])
    print("latest", latest["snapshot_mode"], day)
    calls = (
        ("summary", today_summary(as_of_date=day, level=2, snapshot_mode="delayed_shadow")),
        ("sector", opportunities(as_of_date=day, level=2, snapshot_mode="delayed_shadow")),
        ("etf", etf_candidates(as_of_date=day, level=2, snapshot_mode="delayed_shadow")),
        ("stock", stock_candidates(as_of_date=day, level=2, snapshot_mode="delayed_shadow")),
    )
    for name, response in calls:
        rows = response.get("opportunities", response.get("candidates", ()))
        print(name, "mode", response["snapshot_mode"], "count", len(rows))
        if "summary" in response:
            print("summary_values", response["summary"])
        print("examples", [(row["entity_code"], row["entity_name"], row["execution_eligible_at"]) for row in rows[:3]])


if __name__ == "__main__":
    main()
