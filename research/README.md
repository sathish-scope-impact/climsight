# CHART Research

This folder contains deep research conducted to position ClimSight as the technical infrastructure for [CHART (Climate-Health Adaptation and Response Tool)](../CHART_USE_CASE.md).

## Documents

| Document | Description |
|---|---|
| [climate_maternal_child_health.md](climate_maternal_child_health.md) | Evidence base on how climate change affects maternal, newborn, and child health. Covers heat x preterm birth, CHAMNHA project findings, evidence gap maps, WHO policy developments, and climate education as adaptation. |
| [competitive_landscape.md](competitive_landscape.md) | Analysis of 5 existing tools (DHIS2 Climate, CHAP, Khushi Baby CHVI, ClimaHealth, Americares). Profiles each tool's capabilities, deployment status, gaps, and relevance to CHART. Identifies the unique gap CHART fills. |
| [intervention_knowledge_base.md](intervention_knowledge_base.md) | Sources and catalog for building a curated MNCH intervention knowledge base. Includes 79 interventions from JOGH 2025, proposed schema, 10 priority interventions for MVP, and a phased population workflow. |
| [climate_data_sources.md](climate_data_sources.md) | Evaluation of climate data APIs and datasets. Covers Open-Meteo, ERA5, ECMWF SEAS5, IMD, KMD, IRI, CHIRPS. Includes recommended data strategy for MVP and production, plus derived indicators for MNCH. |
| [dhis2_integration.md](dhis2_integration.md) | DHIS2 ecosystem analysis and integration strategy. Covers DHIS2 Climate App, CHAP, Global Fund funding, DHIS2 in Kenya/India, 3 integration options, API details, and recommended phased architecture. |
| [country_context.md](country_context.md) | Country profiles for Kenya (recommended first pilot) and India (second phase). Health system structure, MNCH indicators, climate-health risks, policy frameworks, digital infrastructure, and recommended pilot locations. |

## Key Findings

1. **The evidence supports building CHART** -- climate impacts on MNCH are documented, interventions exist but are scattered, and no tool currently operationalizes this knowledge into seasonal preparedness plans.

2. **Kenya is the recommended first pilot** -- national RMNCAH-N framework already includes climate, CHAMNHA has produced Kenya-specific evidence (Kilifi), county health system is well-structured.

3. **DHIS2 is the integration backbone** -- 80+ countries, 3.9B people. Recommended hybrid approach: standalone CHART tool that reads/writes DHIS2.

4. **The intervention knowledge base is the hardest part** -- only 79 mapped interventions, most not MNCH-specific, most not evaluated in LMICs. Requires phased curation approach.

5. **Open-Meteo for MVP, national met services for production** -- free climate APIs get the prototype running; IMD/KMD seasonal outlooks add credibility for district officers.

## Research Date

All research conducted: 2026-03-05
