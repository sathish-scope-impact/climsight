# Intervention Knowledge Base: Sources and Catalog

## Research Summary

Last updated: 2026-03-05

This document catalogs the sources, structure, and content needed to build a curated intervention knowledge base for CHART -- matching climate-health risks to evidence-based MNCH interventions.

---

## 1. The Challenge

No single curated database of climate-health interventions for MNCH exists. The knowledge base must be manually assembled from scattered sources:

- Scoping reviews and systematic reviews
- Project field reports (CHAMNHA, Khushi Baby, Americares)
- National policy frameworks (Kenya RMNCAH-N, Ahmedabad HAP)
- WHO/WMO guidance documents (ClimaHealth)
- Expert consultation outputs (PMNCH dialogues)

The [JOGH 2025 scoping review](https://jogh.org/2025/jogh-15-04035) is the best starting point, with 79 interventions already categorized.

---

## 2. Source Inventory

### Primary Sources

| Source | Content | Est. Entries | Quality | Accessibility |
|---|---|---|---|---|
| **JOGH 2025 scoping review** | 79 interventions across 4 socioecological levels | 79 | High (peer-reviewed) | Open access |
| **CHAMNHA project outputs** | Co-designed heat interventions for pregnant women (Kenya + Burkina Faso) | 5-10 | High (field-tested) | Publications |
| **Kenya RMNCAH-N 2025-2030** | National framework with climate-health intervention matrix | 10-15 | High (policy) | PDF |
| **Americares Climate Toolkit** | Heat/flood/wildfire action plans with pregnancy guidance | 10-15 | Medium (toolkit) | Downloadable |
| **ClimaHealth resource library** | WHO/WMO curated case studies and guidance | 20-30 | Variable | Web platform |
| **Ahmedabad HAP evaluation** | Heat action plan -- early warning, community outreach | 5-8 | High (evaluated) | Published |
| **Khushi Baby/CHIP reports** | CHW-delivered MNCH interventions in Rajasthan heat context | 5-10 | Medium (field) | Reports |

### Secondary Sources

| Source | Content | Notes |
|---|---|---|
| [ScienceDirect 2025 multilevel adaptation review](https://www.sciencedirect.com/science/article/pii/S2589004225001749) | 18 unique adaptation strategies | Categories: education, risk communication, nutrition, cash transfers, CHW programs |
| [ScienceDirect 2025 climate education review](https://www.sciencedirect.com/science/article/pii/S2667278225001087) | Climate education programs for MNH | 4 evaluated programs, all positive outcomes |
| PMNCH Feb 2025 dialogue outputs | Expert consensus on key interventions | Not yet fully published |
| CDC BRACE framework | Step-by-step climate-health adaptation planning | Framework, not specific interventions |
| WHO V&A Assessment Guidance | Vulnerability and adaptation assessment methodology | Process guidance |

---

## 3. Intervention Taxonomy (from JOGH 2025)

The [JOGH 2025 scoping review](https://jogh.org/2025/jogh-15-04035) categorized interventions into 4 socioecological levels:

### Level 1: Individual and Household (30 interventions)

Examples:
- Hydration counseling for pregnant women during heat events
- Nutrition supplementation to offset climate-related food insecurity
- Bed nets and insecticide-treated materials for vector-borne disease prevention
- Heat-protective clothing guidance for newborns
- Breastfeeding support during heat events
- Water purification at household level

### Level 2: Community and Service (18 interventions)

Examples:
- Community health worker heat alert systems (CHAMNHA Kenya model)
- Cooler community spaces for pregnant/postpartum women
- Mobile health messaging on climate-health risks
- Community-based surveillance for climate-sensitive disease outbreaks
- Group education sessions on heat-health for pregnant women
- Male spouse/mother-in-law engagement programs

### Level 3: Structural and Urban (15 interventions)

Examples:
- Shade infrastructure near health facilities
- Clean water access infrastructure
- Health facility cooling systems
- Green infrastructure for heat island mitigation
- Improved sanitation for flood-prone areas
- Road/transport infrastructure for facility access during extreme weather

### Level 4: Policy (16 interventions)

Examples:
- Heat action plans with MNCH-specific components
- Early warning systems with health messaging
- Cash transfer programs during climate events
- Employment guarantee schemes (e.g., India's MGNREGA during droughts)
- Chemoprophylaxis programs for malaria during rainy season
- Climate-health surveillance integration policies

---

## 4. Proposed Knowledge Base Schema

Each intervention entry should include:

```yaml
intervention:
  id: string                    # Unique identifier
  name: string                  # Short name
  description: string           # Full description

  # Classification
  socioecological_level: enum   # individual, community, structural, policy
  climate_hazard: list          # heat, flood, drought, vector_disease, air_pollution
  health_risk: list             # preterm_birth, stillbirth, neonatal_dehydration, malaria_pregnancy, malnutrition, ...
  target_population: list       # pregnant_women, postpartum_women, newborns, children_under5, adolescents

  # Evidence
  evidence_strength: enum       # strong, moderate, weak, expert_opinion
  evidence_sources: list        # DOIs or reference keys
  evaluated_in_lmic: boolean    # Has this been evaluated in a low/middle-income country?
  evaluated_countries: list     # Countries where evaluated

  # Implementation
  implementation_level: enum    # household, community, facility, district, national
  required_resources: list      # CHWs, supplies, infrastructure, training, funding
  estimated_cost: string        # Rough cost category: low/medium/high
  lead_time: string             # How far in advance must planning start
  seasonal_timing: string       # When to implement relative to climate event
  responsible_actor: list       # CHW, facility_staff, district_officer, national_program

  # Context
  applicable_regions: list      # Geographic applicability
  prerequisites: list           # What must be in place for this to work
  complementary_interventions: list  # What works well alongside this
  contraindications: list       # When NOT to use this
```

---

## 5. Priority Interventions for MVP

Based on evidence strength and relevance to Kenya/India, these interventions should be prioritized for the first version:

### Heat x Pregnancy (Kenya + India)

1. **CHW heat alert system** -- CHAMNHA-tested in Kilifi, Kenya. CHWs monitor heat stress and disseminate alerts to pregnant/postpartum women. Evidence: strong (field-tested). Cost: low. ([CHAMNHA Kenya, Health Policy & Planning 2025](https://doi.org/10.1093/heapol/czaf028))

2. **Hydration counseling for pregnant women** -- Targeted messaging on fluid intake during heat events. Evidence: moderate. Cost: low. ([JOGH 2025](https://jogh.org/2025/jogh-15-04035))

3. **Breastfeeding support during heat** -- Guidance on increased feeding frequency, avoiding heavy infant clothing. CHAMNHA evidence from both Kenya and Burkina Faso. Evidence: strong. Cost: low. ([CHAMNHA/LSHTM](https://www.lshtm.ac.uk/research/centres-projects-groups/chamnha))

4. **Male spouse/family engagement** -- Training key household influencers on heat-health risks for pregnant women. CHAMNHA showed mothers-in-law and spouses began assisting during heat events. Evidence: moderate. Cost: low. ([CHAMNHA Kenya](https://doi.org/10.1093/heapol/czaf028))

5. **Health facility heat preparedness** -- Cooling, hydration stations, adjusted clinic hours during extreme heat. Americares toolkit provides templates. Evidence: moderate. Cost: medium. ([Americares](https://www.americares.org/what-we-do/community-health/climate-resilient-health-clinics/))

### Vector-borne Disease x Pregnancy (Kenya)

6. **Intermittent preventive treatment in pregnancy (IPTp)** -- Sulfadoxine-pyrimethamine for malaria prevention during pregnancy, scaled up during predicted high-transmission seasons. Evidence: strong (WHO recommendation). Cost: low.

7. **LLIN distribution to pregnant women** -- Long-lasting insecticidal nets prioritized for pregnant women before rainy season. Evidence: strong (WHO recommendation). Cost: medium.

### Drought/Food Insecurity x Child Health (India + Kenya)

8. **Targeted nutrition supplementation** -- Ready-to-use therapeutic food for children under 5 and pregnant women during drought-affected seasons. Evidence: strong. Cost: medium.

9. **Cash transfer programs** -- Conditional or unconditional transfers during climate-induced food insecurity. Evidence: moderate. Cost: high.

### Flood x MNCH (Kenya)

10. **Water purification at household level** -- Chlorine tablets or ceramic filters during flood events. Evidence: strong. Cost: low.

---

## 6. Knowledge Base Population Workflow

### Phase 1: Seed from JOGH 2025 (Week 1-2)

1. Extract all 79 interventions from the scoping review
2. Classify using the schema above
3. Flag which have been evaluated in Kenya or India

### Phase 2: Enrich from CHAMNHA + Field Sources (Week 3-4)

1. Add CHAMNHA Kenya/Burkina Faso specific interventions with implementation details
2. Add Khushi Baby/Rajasthan interventions
3. Add Americares toolkit interventions (adapt from US to LMIC context)
4. Add Kenya RMNCAH-N framework interventions

### Phase 3: Expert Review (Week 5-6)

1. Review with MNCH practitioners in Kenya and India
2. Validate applicability, cost estimates, and prerequisites
3. Identify gaps in coverage

### Phase 4: Vectorize for RAG (Week 7-8)

1. Generate embeddings for each intervention entry
2. Build Chroma vector store
3. Test retrieval accuracy with sample climate-health risk queries
4. Iterate on chunking strategy and metadata filtering

---

## 7. References

- JOGH 2025 intervention mapping: https://jogh.org/2025/jogh-15-04035
- CHAMNHA Kenya: https://doi.org/10.1093/heapol/czaf028
- CHAMNHA project: https://www.lshtm.ac.uk/research/centres-projects-groups/chamnha
- Multilevel adaptation review: https://www.sciencedirect.com/science/article/pii/S2589004225001749
- Americares toolkit: https://www.americares.org/what-we-do/community-health/climate-resilient-health-clinics/
- Kenya RMNCAH-N: https://countdown2030.org/wp-content/uploads/2025/10/RMNXAH-N-for-Official-Processing.pdf
- ClimaHealth: https://climahealth.info/
- Khushi Baby: https://www.khushibaby.org/cause/climate-health
- Climate education review: https://www.sciencedirect.com/science/article/pii/S2667278225001087
- CDC BRACE: https://www.cdc.gov/climate-health/php/brace/index.html
