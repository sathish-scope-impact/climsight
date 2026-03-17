"""Hazard-intervention matching engine.

Loads the intervention knowledge base, matches interventions to active hazards,
and sequences them by phase and severity.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from .models import (
    ClimateHazard,
    EvidenceQuality,
    HazardType,
    Intervention,
    MatchedIntervention,
    Phase,
)

DATA_DIR = Path(__file__).parent / "data"


def load_intervention_kb(path: Path | None = None) -> list[Intervention]:
    """Load the intervention knowledge base from YAML."""
    if path is None:
        path = DATA_DIR / "intervention_kb.yaml"
    with open(path) as f:
        raw = yaml.safe_load(f)

    interventions: list[Intervention] = []
    for entry in raw["interventions"]:
        interventions.append(
            Intervention(
                id=entry["id"],
                name=entry["name"],
                description=entry["description"].strip(),
                target_hazards=[HazardType(h) for h in entry["target_hazards"]],
                trigger_condition=entry["trigger_condition"].strip()
                if isinstance(entry["trigger_condition"], str)
                else str(entry["trigger_condition"]).strip(),
                responsible_officer_role=entry["responsible_officer_role"],
                indicator=entry["indicator"],
                evidence_quality=EvidenceQuality(
                    entry.get("evidence_quality", "moderate")
                ),
                phase=Phase(entry["phase"]),
            )
        )
    return interventions


def match_interventions(
    hazards: list[ClimateHazard],
    kb: list[Intervention] | None = None,
) -> list[MatchedIntervention]:
    """Match interventions to active hazards.

    For each intervention in the KB, if any of its target_hazards matches an
    active hazard, create a MatchedIntervention. When an intervention targets
    multiple active hazards, it is matched to the highest-severity one.
    """
    if kb is None:
        kb = load_intervention_kb()

    hazard_map: dict[HazardType, ClimateHazard] = {}
    for h in hazards:
        # Keep the highest severity if duplicate hazard types
        if h.hazard_type not in hazard_map or h.severity.value > hazard_map[h.hazard_type].severity.value:
            hazard_map[h.hazard_type] = h

    matched: list[MatchedIntervention] = []
    for intervention in kb:
        # Find the best (highest severity) matching hazard
        best_hazard: ClimateHazard | None = None
        for target in intervention.target_hazards:
            if target in hazard_map:
                if best_hazard is None or hazard_map[target].severity.value > best_hazard.severity.value:
                    best_hazard = hazard_map[target]

        if best_hazard is not None:
            matched.append(
                MatchedIntervention(
                    intervention=intervention,
                    matched_hazard=best_hazard,
                )
            )

    return matched


def sequence_interventions(
    matched: list[MatchedIntervention],
) -> dict[Phase, list[MatchedIntervention]]:
    """Group by phase and sort within phase by hazard severity (desc)."""
    by_phase: dict[Phase, list[MatchedIntervention]] = {p: [] for p in Phase}
    for mi in matched:
        by_phase[mi.intervention.phase].append(mi)

    for phase in by_phase:
        by_phase[phase].sort(
            key=lambda m: m.matched_hazard.severity.value, reverse=True
        )
        for idx, mi in enumerate(by_phase[phase], 1):
            mi.sequence_number = idx

    return by_phase
