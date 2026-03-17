"""Plan generator — assembles a PreparednessPlan from district profile + hazards."""

from __future__ import annotations

from pathlib import Path

import yaml

from .matching_engine import load_intervention_kb, match_interventions
from .models import (
    ClimateHazard,
    ConfidenceLevel,
    DistrictProfile,
    HazardType,
    HealthFacilities,
    MatchedIntervention,
    MonitoringIndicator,
    PreparednesssPlan,
    RevisionCheckpoint,
    Severity,
)

DATA_DIR = Path(__file__).parent / "data"


def load_district_profile(district: str) -> tuple[DistrictProfile, list[ClimateHazard]]:
    """Load a district profile and its active hazards from YAML.

    Returns (profile, active_hazards).
    """
    path = DATA_DIR / "districts" / f"{district.lower()}.yaml"
    if not path.exists():
        raise FileNotFoundError(f"No district profile found at {path}")

    with open(path) as f:
        raw = yaml.safe_load(f)

    profile = DistrictProfile(
        name=raw["name"],
        state=raw["state"],
        blocks=raw.get("blocks", []),
        population=raw["population"],
        historical_hazards=[HazardType(h) for h in raw.get("historical_hazards", [])],
        health_facilities=HealthFacilities(**raw["health_facilities"]),
        priority_populations=raw.get("priority_populations", []),
    )

    hazards: list[ClimateHazard] = []
    for h in raw.get("active_hazards", []):
        hazards.append(
            ClimateHazard(
                hazard_type=HazardType(h["hazard_type"]),
                severity=Severity(h["severity"]),
                peak_period_mw_start=h["peak_period_mw_start"],
                peak_period_mw_end=h["peak_period_mw_end"],
                health_impacts=h.get("health_impacts", []),
                confidence=ConfidenceLevel(h.get("confidence", "medium")),
            )
        )

    return profile, hazards


def _build_monitoring_indicators(
    matched: list[MatchedIntervention],
) -> list[MonitoringIndicator]:
    """Extract monitoring indicators from matched interventions."""
    indicators: list[MonitoringIndicator] = []
    seen: set[str] = set()
    for mi in matched:
        ind_text = mi.intervention.indicator
        if ind_text not in seen:
            seen.add(ind_text)
            indicators.append(
                MonitoringIndicator(
                    indicator=ind_text,
                    baseline="To be established",
                    target="As per intervention protocol",
                    reporting_frequency="Monthly",
                )
            )
    return indicators


def _default_revision_checkpoints(valid_period: str) -> list[RevisionCheckpoint]:
    """Generate standard DHAP revision checkpoints."""
    return [
        RevisionCheckpoint(
            date_description="Pre-monsoon review (MW 20)",
            trigger="Before monsoon onset — verify all pre-positioning complete",
            responsible="CMO / District Health Officer",
        ),
        RevisionCheckpoint(
            date_description="Mid-monsoon review (MW 30)",
            trigger="Mid-season assessment — adjust based on actual hazard events",
            responsible="CMO / District Health Officer",
        ),
        RevisionCheckpoint(
            date_description="Post-monsoon review (MW 44)",
            trigger="End of monsoon — lessons learned and closure",
            responsible="CMO / District Health Officer",
        ),
    ]


def generate_plan(
    profile: DistrictProfile,
    hazards: list[ClimateHazard],
    valid_period: str = "Monsoon 2026",
    kb_path: Path | None = None,
) -> PreparednesssPlan:
    """Generate a complete preparedness plan.

    Args:
        profile: District profile with demographics and facilities.
        hazards: Active climate hazards for the planning period.
        valid_period: Human-readable validity string (e.g. "Monsoon 2026").
        kb_path: Optional path to intervention KB YAML.

    Returns:
        A fully populated PreparednesssPlan.
    """
    kb = load_intervention_kb(kb_path)
    matched = match_interventions(hazards, kb)
    monitoring = _build_monitoring_indicators(matched)
    checkpoints = _default_revision_checkpoints(valid_period)

    data_sources = [
        "India Meteorological Department (IMD) seasonal forecast",
        "Integrated Disease Surveillance Programme (IDSP) data",
        "Census 2011 population data",
        "NHM facility directory",
        "CHART climate-health knowledge base v1.0",
        "District disaster management records",
    ]

    plan = PreparednesssPlan(
        district_profile=profile,
        valid_period=valid_period,
        hazards=hazards,
        interventions=matched,
        monitoring_indicators=monitoring,
        revision_checkpoints=checkpoints,
        data_sources=data_sources,
    )
    # Set auto-generated reference
    plan.plan_reference = plan.auto_plan_reference
    return plan
