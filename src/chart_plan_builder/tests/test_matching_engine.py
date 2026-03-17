"""Tests for the hazard-intervention matching engine."""

import pytest

from chart_plan_builder.matching_engine import (
    load_intervention_kb,
    match_interventions,
    sequence_interventions,
)
from chart_plan_builder.models import (
    ClimateHazard,
    ConfidenceLevel,
    HazardType,
    Phase,
    Severity,
)


def test_load_intervention_kb():
    kb = load_intervention_kb()
    assert len(kb) >= 15
    for intervention in kb:
        assert intervention.id
        assert intervention.name
        assert len(intervention.target_hazards) > 0


def test_match_interventions_flooding():
    hazards = [
        ClimateHazard(
            hazard_type=HazardType.FLOODING,
            severity=Severity.ORANGE,
            peak_period_mw_start=27,
            peak_period_mw_end=37,
        )
    ]
    matched = match_interventions(hazards)
    # Should match FLD-001, FLD-002, FLD-003, WBD-001, CRS-001, CRS-002
    assert len(matched) > 0
    for mi in matched:
        assert HazardType.FLOODING in mi.intervention.target_hazards


def test_match_interventions_no_hazards():
    matched = match_interventions([])
    assert matched == []


def test_match_interventions_unmatched_hazard():
    """A hazard with no KB interventions produces no matches."""
    hazards = [
        ClimateHazard(
            hazard_type=HazardType.ULTRAVIOLET_RADIATION,
            severity=Severity.GREEN,
            peak_period_mw_start=1,
            peak_period_mw_end=10,
        )
    ]
    matched = match_interventions(hazards)
    assert matched == []


def test_match_interventions_multi_hazard():
    """Interventions targeting multiple hazards match the highest-severity one."""
    hazards = [
        ClimateHazard(
            hazard_type=HazardType.FLOODING,
            severity=Severity.YELLOW,
            peak_period_mw_start=27,
            peak_period_mw_end=37,
        ),
        ClimateHazard(
            hazard_type=HazardType.WATERBORNE_DISEASE,
            severity=Severity.RED,
            peak_period_mw_start=27,
            peak_period_mw_end=42,
        ),
    ]
    matched = match_interventions(hazards)
    # FLD-003 targets both flooding and waterborne_disease
    fld003 = [m for m in matched if m.intervention.id == "FLD-003"]
    assert len(fld003) == 1
    # Should be matched to waterborne_disease (Red > Yellow)
    assert fld003[0].matched_hazard.hazard_type == HazardType.WATERBORNE_DISEASE


def test_sequence_interventions():
    hazards = [
        ClimateHazard(
            hazard_type=HazardType.FLOODING,
            severity=Severity.ORANGE,
            peak_period_mw_start=27,
            peak_period_mw_end=37,
        ),
        ClimateHazard(
            hazard_type=HazardType.VECTOR_BORNE_DISEASE,
            severity=Severity.RED,
            peak_period_mw_start=26,
            peak_period_mw_end=40,
        ),
    ]
    matched = match_interventions(hazards)
    by_phase = sequence_interventions(matched)

    # Check that sequencing assigns numbers
    for phase, interventions in by_phase.items():
        for i, mi in enumerate(interventions, 1):
            assert mi.sequence_number == i
        # Verify sorted by severity descending
        severities = [mi.matched_hazard.severity.value for mi in interventions]
        assert severities == sorted(severities, reverse=True)
