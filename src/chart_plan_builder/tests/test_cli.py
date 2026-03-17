"""Tests for the CLI interface."""

from pathlib import Path

import pytest
from click.testing import CliRunner

from chart_plan_builder.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_version(runner):
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "chart-plan-builder" in result.output


def test_list_hazards(runner):
    result = runner.invoke(cli, ["list-hazards"])
    assert result.exit_code == 0
    assert "flooding" in result.output.lower()
    assert "heat" in result.output.lower()


def test_list_interventions(runner):
    result = runner.invoke(cli, ["list-interventions"])
    assert result.exit_code == 0
    assert "FLD-001" in result.output


def test_list_interventions_filter_hazard(runner):
    result = runner.invoke(cli, ["list-interventions", "--hazard", "flooding"])
    assert result.exit_code == 0
    assert "FLD-001" in result.output


def test_list_interventions_filter_phase(runner):
    result = runner.invoke(cli, ["list-interventions", "--phase", "pre_monsoon"])
    assert result.exit_code == 0
    # All shown should be pre_monsoon
    assert "pre_monsoon" in result.output


def test_list_interventions_invalid_hazard(runner):
    result = runner.invoke(cli, ["list-interventions", "--hazard", "earthquake"])
    assert result.exit_code != 0


def test_generate_json(runner, tmp_path):
    output = str(tmp_path / "test_plan")
    result = runner.invoke(cli, [
        "generate",
        "--district", "muzaffarpur",
        "--state", "bihar",
        "--season", "Monsoon 2026",
        "--output", output,
        "--format", "json",
    ])
    assert result.exit_code == 0
    assert Path(f"{output}.json").exists()


def test_generate_docx(runner, tmp_path):
    output = str(tmp_path / "test_plan")
    result = runner.invoke(cli, [
        "generate",
        "--district", "muzaffarpur",
        "--state", "bihar",
        "--format", "docx",
        "--output", output,
    ])
    assert result.exit_code == 0
    assert Path(f"{output}.docx").exists()


def test_generate_both(runner, tmp_path):
    output = str(tmp_path / "test_plan")
    result = runner.invoke(cli, [
        "generate",
        "--district", "muzaffarpur",
        "--state", "bihar",
        "--format", "both",
        "--output", output,
    ])
    assert result.exit_code == 0
    assert Path(f"{output}.json").exists()
    assert Path(f"{output}.docx").exists()


def test_generate_nonexistent_district(runner):
    result = runner.invoke(cli, [
        "generate",
        "--district", "nonexistent",
        "--state", "test",
    ])
    assert result.exit_code != 0
