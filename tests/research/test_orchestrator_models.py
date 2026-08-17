from morning_conference.sector_rotation2.research.orchestrator.config import OrchestratorConfig
from morning_conference.sector_rotation2.research.orchestrator.models import OpportunityState, Playbook


def test_opportunity_states_cover_the_shadow_sector_contract() -> None:
    assert {state.value for state in OpportunityState} == {
        "trend_reinforced", "trend_continue", "trend_conflict", "recovery_early",
        "recovery_confirming", "recovery_confirmed", "repair_watch", "cooling_watch",
        "risk_reduce", "avoid", "neutral",
    }


def test_playbooks_cover_all_actionable_and_observation_modes() -> None:
    assert {playbook.value for playbook in Playbook} == {
        "trend_follow", "repair_probe", "early_repair", "hold_only", "risk_reduce", "avoid", "observe",
    }


def test_orchestrator_config_has_a_versioned_default() -> None:
    assert OrchestratorConfig().model_version == "sector_opportunity_v1"
