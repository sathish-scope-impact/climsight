"""Tests for plan generation and DOCX output."""

import json
from pathlib import Path

import pytest

from chart_plan_builder.plan_generator import generate_plan, load_district_profile
from chart_plan_builder.models import Phase


def test_load_muzaffarpur_profile():
    profile, hazards = load_district_profile("muzaffarpur")
    assert profile.name == "Muzaffarpur"
    assert profile.state == "Bihar"
    assert profile.population > 0
    assert len(hazards) > 0
    assert len(profile.blocks) > 0


def test_load_nonexistent_district():
    with pytest.raises(FileNotFoundError):
        load_district_profile("nonexistent_district")


def test_generate_plan_muzaffarpur():
    profile, hazards = load_district_profile("muzaffarpur")
    plan = generate_plan(profile, hazards, valid_period="Monsoon 2026")

    assert plan.district_profile.name == "Muzaffarpur"
    assert len(plan.hazards) > 0
    assert len(plan.interventions) > 0
    assert len(plan.monitoring_indicators) > 0
    assert len(plan.revision_checkpoints) == 3
    assert len(plan.data_sources) > 0
    assert "CHART-BIH-MUZAFFARPUR" in plan.auto_plan_reference


def test_plan_json_serialization():
    profile, hazards = load_district_profile("muzaffarpur")
    plan = generate_plan(profile, hazards)

    json_str = plan.model_dump_json(indent=2)
    data = json.loads(json_str)

    assert data["district_profile"]["name"] == "Muzaffarpur"
    assert isinstance(data["interventions"], list)
    assert len(data["interventions"]) > 0


def test_plan_has_all_phases_covered():
    profile, hazards = load_district_profile("muzaffarpur")
    plan = generate_plan(profile, hazards)
    by_phase = plan.interventions_by_phase()

    # Muzaffarpur should have interventions in all three phases
    assert len(by_phase[Phase.PRE_MONSOON]) > 0
    assert len(by_phase[Phase.ACTIVE_MONSOON]) > 0
    assert len(by_phase[Phase.POST_MONSOON]) > 0


def test_generate_docx(tmp_path: Path):
    from chart_plan_builder.docx_generator import generate_docx

    profile, hazards = load_district_profile("muzaffarpur")
    plan = generate_plan(profile, hazards, valid_period="Monsoon 2026")

    output_path = tmp_path / "test_plan.docx"
    result = generate_docx(plan, output_path)

    assert result == output_path
    assert output_path.exists()
    assert output_path.stat().st_size > 0
