"""CLI interface for CHART Plan Builder."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click
import yaml

from . import __version__
from .docx_generator import generate_docx
from .matching_engine import load_intervention_kb
from .models import HazardType, Phase
from .plan_generator import generate_plan, load_district_profile

DATA_DIR = Path(__file__).parent / "data"


@click.group()
@click.version_option(version=__version__, prog_name="chart-plan-builder")
def cli() -> None:
    """CHART Plan Builder — Climate x Health Adaptation and Resilience Tool.

    Generates district-level climate-health preparedness plans as
    structured JSON and DOCX output.
    """


@cli.command()
@click.option("--district", required=True, help="District name (must have a YAML profile)")
@click.option("--state", required=True, help="State name")
@click.option("--season", default="Monsoon 2026", help="Planning season label")
@click.option("--output", "-o", default=None, help="Output file path (.docx or .json)")
@click.option("--format", "fmt", type=click.Choice(["docx", "json", "both"]), default="both",
              help="Output format")
@click.option("--kb-path", default=None, type=click.Path(exists=True),
              help="Path to intervention KB YAML (default: built-in)")
def generate(
    district: str,
    state: str,
    season: str,
    output: str | None,
    fmt: str,
    kb_path: str | None,
) -> None:
    """Generate a preparedness plan for a district."""
    try:
        profile, hazards = load_district_profile(district)
    except FileNotFoundError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)

    # Override state if provided (profile YAML is source of truth but CLI can override)
    if state.lower() != profile.state.lower():
        click.echo(
            f"Note: CLI state '{state}' differs from profile state '{profile.state}'. "
            f"Using profile value."
        )

    kb = Path(kb_path) if kb_path else None
    plan = generate_plan(profile, hazards, valid_period=season, kb_path=kb)

    click.echo(f"Plan generated: {plan.auto_plan_reference}")
    click.echo(f"  District: {profile.name}, {profile.state}")
    click.echo(f"  Hazards: {len(hazards)}")
    click.echo(f"  Matched interventions: {len(plan.interventions)}")

    base_name = output or f"plan_{district.lower()}"

    if fmt in ("json", "both"):
        json_path = base_name if base_name.endswith(".json") else f"{base_name}.json"
        json_path = Path(json_path)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(plan.model_dump_json(indent=2))
        click.echo(f"  JSON: {json_path}")

    if fmt in ("docx", "both"):
        docx_path = base_name if base_name.endswith(".docx") else f"{base_name}.docx"
        generate_docx(plan, Path(docx_path))
        click.echo(f"  DOCX: {docx_path}")


@cli.command("list-hazards")
def list_hazards() -> None:
    """Show the 16-hazard taxonomy."""
    taxonomy_path = DATA_DIR / "hazard_taxonomy.yaml"
    with open(taxonomy_path) as f:
        data = yaml.safe_load(f)

    click.echo("CHART 16-Hazard Taxonomy")
    click.echo("=" * 50)
    for h in data["hazards"]:
        click.echo(f"\n  {h['id']}: {h['name']}")
        click.echo(f"    {h['description']}")
        for impact in h.get("health_impact_categories", []):
            click.echo(f"      - {impact}")


@cli.command("list-interventions")
@click.option("--hazard", default=None, help="Filter by hazard type")
@click.option("--phase", default=None, type=click.Choice(["pre_monsoon", "active_monsoon", "post_monsoon"]),
              help="Filter by phase")
def list_interventions(hazard: str | None, phase: str | None) -> None:
    """List interventions from the knowledge base."""
    kb = load_intervention_kb()

    if hazard:
        try:
            hazard_type = HazardType(hazard)
        except ValueError:
            click.echo(f"Error: Unknown hazard type '{hazard}'", err=True)
            click.echo(f"Valid types: {', '.join(h.value for h in HazardType)}", err=True)
            sys.exit(1)
        kb = [i for i in kb if hazard_type in i.target_hazards]

    if phase:
        phase_enum = Phase(phase)
        kb = [i for i in kb if i.phase == phase_enum]

    click.echo(f"Interventions ({len(kb)} found)")
    click.echo("=" * 60)
    for i in kb:
        targets = ", ".join(h.value for h in i.target_hazards)
        click.echo(f"\n  [{i.id}] {i.name}")
        click.echo(f"    Phase: {i.phase.value} | Targets: {targets}")
        click.echo(f"    Evidence: {i.evidence_quality.value}")
        click.echo(f"    Trigger: {i.trigger_condition[:80]}")


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
