"""Pydantic v2 data models for CHART Plan Builder."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, computed_field


# ---------------------------------------------------------------------------
# Enums & taxonomies
# ---------------------------------------------------------------------------

class HazardType(str, Enum):
    """16-hazard taxonomy used by CHART."""
    FLOODING = "flooding"
    HEAT_WAVE = "heat_wave"
    CYCLONE = "cyclone"
    DROUGHT = "drought"
    COLD_WAVE = "cold_wave"
    LIGHTNING = "lightning"
    LANDSLIDE = "landslide"
    DUST_STORM = "dust_storm"
    WILDFIRE = "wildfire"
    RIVERINE_EROSION = "riverine_erosion"
    SEA_LEVEL_RISE = "sea_level_rise"
    AIR_POLLUTION = "air_pollution"
    VECTOR_BORNE_DISEASE = "vector_borne_disease"
    WATERBORNE_DISEASE = "waterborne_disease"
    ULTRAVIOLET_RADIATION = "ultraviolet_radiation"
    HUMIDITY_EXTREME = "humidity_extreme"


class Severity(int, Enum):
    """IMD-style 4-level severity scale."""
    GREEN = 1   # No significant impact
    YELLOW = 2  # Moderate impact
    ORANGE = 3  # Severe impact
    RED = 4     # Very severe impact


SEVERITY_LABELS: dict[Severity, str] = {
    Severity.GREEN: "Green",
    Severity.YELLOW: "Yellow",
    Severity.ORANGE: "Orange",
    Severity.RED: "Red",
}


class Phase(str, Enum):
    """Seasonal phases for monsoon-context India planning."""
    PRE_MONSOON = "pre_monsoon"
    ACTIVE_MONSOON = "active_monsoon"
    POST_MONSOON = "post_monsoon"


# Meteorological week ranges for each phase (India monsoon context)
PHASE_MW_RANGES: dict[Phase, tuple[int, int]] = {
    Phase.PRE_MONSOON: (20, 24),
    Phase.ACTIVE_MONSOON: (25, 38),
    Phase.POST_MONSOON: (39, 43),
}


class EvidenceQuality(str, Enum):
    HIGH = "high"
    MODERATE = "moderate"
    LOW = "low"


class ConfidenceLevel(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


# ---------------------------------------------------------------------------
# Core models
# ---------------------------------------------------------------------------

class HealthFacilities(BaseModel):
    """Health facility counts for a district."""
    phcs: int = Field(description="Number of Primary Health Centres")
    scs: int = Field(description="Number of Sub-Centres")
    district_hospitals: int = Field(default=0)
    chcs: int = Field(default=0, description="Community Health Centres")


class DistrictProfile(BaseModel):
    """District-level profile for plan generation."""
    name: str
    state: str
    blocks: list[str] = Field(default_factory=list)
    population: int
    historical_hazards: list[HazardType] = Field(default_factory=list)
    health_facilities: HealthFacilities
    priority_populations: list[str] = Field(default_factory=list)


class ClimateHazard(BaseModel):
    """A climate hazard active in the planning period."""
    hazard_type: HazardType
    severity: Severity
    peak_period_mw_start: int = Field(ge=1, le=52)
    peak_period_mw_end: int = Field(ge=1, le=52)
    health_impacts: list[str] = Field(default_factory=list)
    confidence: ConfidenceLevel = ConfidenceLevel.MEDIUM


class Intervention(BaseModel):
    """A single preparedness intervention from the knowledge base."""
    id: str
    name: str
    description: str
    target_hazards: list[HazardType]
    trigger_condition: str
    responsible_officer_role: str
    indicator: str
    evidence_quality: EvidenceQuality = EvidenceQuality.MODERATE
    phase: Phase


class MatchedIntervention(BaseModel):
    """An intervention matched to a specific hazard in the plan."""
    intervention: Intervention
    matched_hazard: ClimateHazard
    sequence_number: int = 0


class MonitoringIndicator(BaseModel):
    """Indicator for the monitoring framework section."""
    indicator: str
    baseline: str
    target: str
    reporting_frequency: str = "Monthly"


class RevisionCheckpoint(BaseModel):
    """Scheduled plan revision checkpoint."""
    date_description: str
    trigger: str
    responsible: str = "CMO / District Health Officer"


class PreparednesssPlan(BaseModel):
    """Complete district preparedness plan — the main output artifact."""
    district_profile: DistrictProfile
    plan_reference: str = ""
    valid_period: str
    hazards: list[ClimateHazard]
    interventions: list[MatchedIntervention]
    monitoring_indicators: list[MonitoringIndicator] = Field(default_factory=list)
    revision_checkpoints: list[RevisionCheckpoint] = Field(default_factory=list)
    data_sources: list[str] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=datetime.utcnow)

    @computed_field  # type: ignore[misc]
    @property
    def auto_plan_reference(self) -> str:
        if self.plan_reference:
            return self.plan_reference
        district = self.district_profile.name.upper()
        state = self.district_profile.state.upper()[:3]
        ts = self.generated_at.strftime("%Y%m%d")
        return f"CHART-{state}-{district}-{ts}"

    def interventions_by_phase(self) -> dict[Phase, list[MatchedIntervention]]:
        """Return interventions grouped and sorted by phase then severity."""
        result: dict[Phase, list[MatchedIntervention]] = {p: [] for p in Phase}
        for mi in self.interventions:
            result[mi.intervention.phase].append(mi)
        for phase in result:
            result[phase].sort(
                key=lambda m: m.matched_hazard.severity.value, reverse=True
            )
        # Assign sequence numbers within phase
        for phase_interventions in result.values():
            for idx, mi in enumerate(phase_interventions, 1):
                mi.sequence_number = idx
        return result
