"""Tests for CHART Plan Builder data models."""

from datetime import datetime

import pytest

from chart_plan_builder.models import (
    ClimateHazard,
    ConfidenceLevel,
    DistrictProfile,
    HazardType,
    HealthFacilities,
    Intervention,
    MatchedIntervention,
    MonitoringIndicator,
    Phase,
    PreparednesssPlan,
    RevisionCheckpoint,
    Severity,
    SEVERITY_LABELS,
    PHASE_MW_RANGES,
    EvidenceQuality,
)


def test_hazard_type_enum_has_16_members():
    assert len(HazardType) == 16


def test_severity_labels():
    assert SEVERITY_LABELS[Severity.GREEN] == "Green"
    assert SEVERITY_LABELS[Severity.RED] == "Red"


def test_phase_mw_ranges():
    assert PHASE_MW_RANGES[Phase.PRE_MONSOON] == (20, 24)
    assert PHASE_MW_RANGES[Phase.ACTIVE_MONSOON] == (25, 38)
    assert PHASE_MW_RANGES[Phase.POST_MONSOON] == (39, 43)


def test_district_profile_creation():
    profile = DistrictProfile(
        name="TestDistrict",
        state="TestState",
        population=100000,
        health_facilities=HealthFacilities(phcs=10, scs=50),
    )
    assert profile.name == "TestDistrict"
    assert profile.health_facilities.phcs == 10
    assert profile.blocks == []
    assert profile.priority_populations == []


def test_climate_hazard_validation():
    hazard = ClimateHazard(
        hazard_type=HazardType.FLOODING,
        severity=Severity.ORANGE,
        peak_period_mw_start=27,
        peak_period_mw_end=37,
        health_impacts=["Drowning"],
    )
    assert hazard.severity == Severity.ORANGE
    assert hazard.severity.value == 3


def test_climate_hazard_invalid_mw():
    with pytest.raises(Exception):
        ClimateHazard(
            hazard_type=HazardType.FLOODING,
            severity=Severity.GREEN,
            peak_period_mw_start=0,  # Invalid: must be >= 1
            peak_period_mw_end=37,
        )


def test_intervention_model():
    intervention = Intervention(
        id="TST-001",
        name="Test Intervention",
        description="A test",
        target_hazards=[HazardType.FLOODING, HazardType.WATERBORNE_DISEASE],
        trigger_condition="Test trigger",
        responsible_officer_role="CMO",
        indicator="Test indicator",
        phase=Phase.PRE_MONSOON,
    )
    assert len(intervention.target_hazards) == 2
    assert intervention.evidence_quality == EvidenceQuality.MODERATE


def test_preparedness_plan_auto_reference():
    plan = PreparednesssPlan(
        district_profile=DistrictProfile(
            name="Muzaffarpur",
            state="Bihar",
            population=100000,
            health_facilities=HealthFacilities(phcs=10, scs=50),
        ),
        valid_period="Monsoon 2026",
        hazards=[],
        interventions=[],
        generated_at=datetime(2026, 3, 17),
    )
    assert plan.auto_plan_reference == "CHART-BIH-MUZAFFARPUR-20260317"


def test_interventions_by_phase():
    hazard = ClimateHazard(
        hazard_type=HazardType.FLOODING,
        severity=Severity.ORANGE,
        peak_period_mw_start=27,
        peak_period_mw_end=37,
    )
    intervention_pre = Intervention(
        id="T1", name="Pre", description="d",
        target_hazards=[HazardType.FLOODING],
        trigger_condition="t", responsible_officer_role="r",
        indicator="i", phase=Phase.PRE_MONSOON,
    )
    intervention_active = Intervention(
        id="T2", name="Active", description="d",
        target_hazards=[HazardType.FLOODING],
        trigger_condition="t", responsible_officer_role="r",
        indicator="i", phase=Phase.ACTIVE_MONSOON,
    )
    plan = PreparednesssPlan(
        district_profile=DistrictProfile(
            name="Test", state="TS", population=1,
            health_facilities=HealthFacilities(phcs=1, scs=1),
        ),
        valid_period="Test",
        hazards=[hazard],
        interventions=[
            MatchedIntervention(intervention=intervention_pre, matched_hazard=hazard),
            MatchedIntervention(intervention=intervention_active, matched_hazard=hazard),
        ],
    )
    by_phase = plan.interventions_by_phase()
    assert len(by_phase[Phase.PRE_MONSOON]) == 1
    assert len(by_phase[Phase.ACTIVE_MONSOON]) == 1
    assert len(by_phase[Phase.POST_MONSOON]) == 0
