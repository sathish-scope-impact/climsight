# CHART: Climate-Health Adaptation and Response Tool

## Use Case for ClimSight as Technical Infrastructure

This document positions ClimSight within the CHART use case -- a climate-health decision support tool for maternal, newborn, and child health (MNCH) planning in India and Kenya.

---

## 1. What Is CHART?

CHART is a digital tool that connects **seasonal climate outlooks** to **evidence-based health interventions** for district-level health officers. It answers the question:

> "Given the climate forecast for next season in my district, what should I do now to protect pregnant women, newborns, and children?"

**The gap CHART fills:** No existing tool produces a seasonal climate-health preparedness plan that connects climate outlooks -> health risks -> evidence-based MNCH interventions -> implementation tracking. Existing tools (DHIS2 Climate, CHAP, ClimaHealth, Khushi Baby CHVI) each cover only a slice of this workflow.

### Core Workflow

1. **Climate Forecast Ingestion** -- Seasonal outlook for a specific district (temperature, precipitation, extremes)
2. **Risk Mapping** -- Which climate-sensitive health risks are elevated? (heat stress in pregnancy, vector-borne disease, malnutrition, water scarcity)
3. **Intervention Matching** -- Evidence-based actions matched to risk profile, local capacity, and season
4. **Plan Generation** -- Structured preparedness plan with timeline, resource requirements, and responsible actors
5. **Monitoring** -- Track implementation and health outcomes against climate triggers

### Target Users

- District/county health officers in India and Kenya
- Maternal-child health program managers
- Community health worker supervisors
- National RMNCAH-N planners

---

## 2. The Evidence Base

### Heat and Maternal Health (Strongest Evidence)

- Each 1C increase is associated with ~5% increase in preterm birth likelihood; heatwave days associated with ~16% increase
- Projected impact (India, 2025-2035): 353,000 heat-related preterm births across urban India
- Ahmedabad Heat Action Plan reduced heat-related mortality rate ratio from 2.34 to 1.25 at 47C, but **no maternal-specific outcomes were tracked**
- Only 6% of heat action plans globally describe monitoring for MNCH populations

### CHAMNHA Project -- Best Direct Evidence (Kenya + Burkina Faso)

The [CHAMNHA project](https://www.lshtm.ac.uk/research/centres-projects-groups/chamnha) (LSHTM + Aga Khan University) is the largest heat x MNH intervention study in sub-Saharan Africa:

- Extreme heat associated with: stillbirth, premature birth, neonatal dehydration, maternal hypertension, disrupted breastfeeding, reduced health facility access
- **Kenya intervention (Kilifi):** Community health volunteers monitor heat stress, disseminate alerts to pregnant/postpartum women, co-designed cooler community spaces
- **Key finding:** "For women in Kenya, heat exposure and water shortages are inextricably linked -- interventions addressing either hazard in isolation may have limited efficacy"
- Behavior change interventions showed positive outcomes: women reported better understanding of heat-health effects; family members began assisting with household chores during heat events

### Intervention Evidence -- Thin but Growing

A [2025 JOGH scoping review](https://jogh.org/2025/jogh-15-04035) mapped 79 interventions across 4 categories:

| Category | Count | Examples |
|---|---|---|
| Individual/household | 30 | Hydration counseling, nutrition supplementation, bed nets |
| Community/service | 18 | CHW heat alerts, cooler spaces, mobile health messaging |
| Structural/urban | 15 | Shade infrastructure, clean water access, facility cooling |
| Policy | 16 | Heat action plans, early warning systems, cash transfers |

**Critical gap:** These interventions are largely nonspecific to MNCH. Panelists flagged "lack of knowledge on cost-effective and affordable solutions for LMICs."

---

## 3. Competitive Landscape

| Tool | Who | What It Does | What It Doesn't Do |
|---|---|---|---|
| **DHIS2 Climate App** | HISP/UiO + Global Fund | Imports ERA5 climate data into national DHIS2 health systems. 80+ countries. | No intervention matching. Surveillance, not planning. |
| **CHAP** | HISP/UiO + Wellcome Trust | ML disease forecasting inside DHIS2. Predicts malaria, dengue, cholera. | Forecasts burden, doesn't recommend interventions. No MNCH focus. |
| **Khushi Baby CHVI** | Khushi Baby + Google | Village-level Climate Health Vulnerability Index for Rajasthan (80M people). | Vulnerability scoring only. No seasonal planning. India-only. |
| **ClimaHealth** | WHO + WMO + Wellcome Trust | Global knowledge platform for climate-health resources and case studies. | Resource library, not a planning tool. No district-level output. |
| **Americares Toolkit** | Americares + Harvard | Clinic-level heat/flood/wildfire action plans with pregnancy guidance. | US-focused (expanding). Clinic-level, not district-level. |

**CHART's unique value:** The **planning layer** on top of surveillance and forecasting tools. CHAP tells you "malaria will spike in July in Kisumu County." CHART tells you "here are 4 evidence-based interventions for malaria prevention during pregnancy in Kisumu, with implementation timeline and resource requirements."

---

## 4. ClimSight as CHART Infrastructure

ClimSight provides the technical backbone for CHART. The mapping between CHART needs and ClimSight components:

| CHART Capability | ClimSight Component | Status |
|---|---|---|
| Forecast climate hazards for a location | `climate_data_providers.py` + ERA5 climatology tool + Open-Meteo API | Existing |
| Retrieve scientific evidence on climate-health risks | `rag.py` + Chroma vector store | Existing (needs MNCH knowledge base) |
| Gather geographic/environmental context | `geo_functions.py` + `environmental_functions.py` | Existing |
| AI-powered synthesis of multi-source data | `combine_agent` + `data_analysis_agent` | Existing |
| Multi-agent orchestration with parallel data gathering | LangGraph workflow in `climsight_engine.py` | Existing |
| Intervention matching from curated knowledge base | RAG over intervention KB (replace IPCC reports) | **New -- to build** |
| Seasonal preparedness plan generation | New planning agent | **New -- to build** |
| District-level health data integration (DHIS2) | DHIS2 API connector | **New -- to build** |
| Monitoring and outcome tracking | Tracking interface | **New -- to build** |

### What Exists and Can Be Reused

1. **Multi-agent architecture** -- LangGraph state machine with parallel agent execution, state sharing via `AgentState`, and sequential synthesis
2. **Climate data pipeline** -- ERA5 climatology extraction, climate model projections (nextGEMS, AWI-CM), Open-Meteo integration path
3. **RAG system** -- Chroma-based vector search with multiple embedding backends (OpenAI, AITTA, Mistral)
4. **Data analysis agent** -- Tool-calling agent with Python REPL, ERA5 retrieval, visualization, and reflection tools
5. **Predefined plots** -- Climate comparison visualizations with ERA5 overlay

### What Needs to Be Built

1. **MNCH Intervention Knowledge Base** -- Curated from CHAMNHA outputs, JOGH 2025 scoping review, Americares toolkit, Kenya RMNCAH-N framework, ClimaHealth resources, Khushi Baby field reports
2. **Climate-Health Risk Mapping Agent** -- Translates climate forecasts into health risk profiles specific to MNCH (e.g., "sustained temperatures >35C for 5+ days" -> "elevated preterm birth risk, neonatal dehydration risk, breastfeeding disruption risk")
3. **Intervention Matching Agent** -- RAG-powered agent that matches risk profiles to evidence-based interventions, filtered by local capacity and season
4. **Plan Generation Agent** -- Synthesizes risks + interventions into structured preparedness plans with timelines, resource requirements, and responsible actors
5. **DHIS2 Integration Layer** -- Read health facility data, population denominators, and historical health outcomes; write back plans and monitoring indicators

---

## 5. Climate Data Sources for CHART

| Source | Resolution | Coverage | Cost | Seasonal Forecast? | Best For |
|---|---|---|---|---|---|
| Open-Meteo Climate API | 10 km | Global, 1950-2050 | Free | Yes (ECMWF SEAS5, 36km, 7 months) | MVP climate baseline |
| Open-Meteo Historical API | 1-11 km | Global | Free | No | "What happened last season" |
| DHIS2 Climate App (ERA5-Land) | ~9 km | Global | Free | No | If building on DHIS2 |
| IMD (India Meteorological Dept) | District-level | India | Government access | Yes (seasonal outlook) | India-specific forecasts |
| KMD (Kenya Met Dept) | County-level | Kenya | Government access | Yes (MAM/OND forecasts) | Kenya-specific forecasts |
| ERA5 Reanalysis | ~31 km | Global, 1940-present | Free (CDS API) | No (historical only) | Climatological baselines |

**Recommendation:** Use Open-Meteo for MVP. For production, integrate national meteorological services (IMD, KMD) which produce seasonal outlooks in formats district officers already recognize.

---

## 6. Intervention Knowledge Base -- Sources

No single curated database exists. The KB must be assembled from:

| Source | Content | Estimated Entries | Format |
|---|---|---|---|
| CHAMNHA project outputs | Co-designed heat interventions for pregnant women (Kenya + Burkina Faso) | 5-10 | Publications + field reports |
| JOGH 2025 intervention mapping | 79 interventions across 4 socioecological levels for MNCH x climate | 79 | Scoping review |
| Americares Climate Toolkit | Heat/flood/wildfire action plans with pregnancy-specific guidance | 10-15 | Structured toolkit |
| Kenya RMNCAH-N 2025-2030 | National framework with climate-health intervention matrix | 10-15 | Policy document |
| ClimaHealth resource library | WHO/WMO curated case studies and guidance documents | 20-30 | Web platform |
| Khushi Baby/CHIP reports | CHW-delivered MNCH interventions in Rajasthan heat context | 5-10 | Field reports |
| Ahmedabad HAP evaluation | India's first heat action plan -- early warning, community outreach | 5-8 | Published evaluation |

**Starting point:** The JOGH 2025 scoping review (79 interventions already categorized), cross-referenced with CHAMNHA's Kenya-specific evidence.

---

## 7. DHIS2 Integration Strategy

DHIS2 is deployed in 80+ countries and manages health data for 3.9 billion people. The Global Fund Climate x Health Catalytic Fund (2025) is funding 7 African countries to implement DHIS2 climate tools.

### Integration Options

| Approach | Pros | Cons |
|---|---|---|
| **Build as DHIS2 module** | Instant health data access. Officers already use DHIS2. | Constrained app framework. Hard to build rich planning UIs. |
| **Standalone, import from DHIS2** | Full UX control. Faster iteration. | Must solve data integration. Another tool to learn. |
| **Hybrid: standalone + DHIS2 read/write** | Best of both. Health data in, plans stored back. | Most complex. Requires DHIS2 API expertise. |

**Recommended:** Hybrid approach. ClimSight/CHART as standalone planning tool that reads health data from DHIS2 and can export plans back. Positions as the **planning layer on top of CHAP's predictions**.

---

## 8. Country Context

### Kenya (Recommended First Pilot)

- **National framework ready:** RMNCAH-N 2025-2030 explicitly includes climate change interventions
- **Direct evidence available:** CHAMNHA produced Kenya-specific interventions (Kilifi county)
- **Health system structure:** 47 counties with county health management teams, well-structured for district-level planning
- **Projected impact:** Framework projects saving 27,995 child lives, 4,611 maternal lives, preventing 11,071 stillbirths over 5 years
- **ROI:** KSh 12.50 for every shilling invested

### India (Second Phase)

- **Scale challenge:** 700+ districts across diverse agroecological zones
- **No national climate-MNCH framework** yet, though emerging state-level efforts
- **Pioneering work:** Khushi Baby CHVI covers 80M people in Rajasthan; Ahmedabad HAP is a model for heat interventions
- **IMD seasonal forecasts** are district-level and well-established
- **CHW infrastructure:** ASHA workers provide a delivery channel for climate-health interventions

---

## 9. Key References

### Research

- CHAMNHA Kenya intervention: [Health Policy & Planning 2025](https://doi.org/10.1093/heapol/czaf028)
- JOGH 2025 intervention mapping: [Interventions for MNCH x air pollution/heat](https://jogh.org/2025/jogh-15-04035)
- Multilevel adaptation for MCH: [ScienceDirect 2025](https://www.sciencedirect.com/science/article/pii/S2589004225001749)
- Climate x maternal health evidence gap map: [PLOS 2024](https://journals.plos.org/globalpublichealth/article?id=10.1371/journal.pgph.0003540)
- MNCH in heat action plans scoping review: [PMC 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12143117/)
- Climate education as adaptation: [ScienceDirect 2025](https://www.sciencedirect.com/science/article/pii/S2667278225001087)

### Platforms and Tools

- ClimaHealth: [climahealth.info](https://climahealth.info/)
- DHIS2 Climate & Health: [dhis2.org/climate](https://dhis2.org/climate/)
- CHAP Modeling Platform: [chap.dhis2.org](https://chap.dhis2.org/)
- Khushi Baby CHVI: [khushibaby.org/cause/climate-health](https://www.khushibaby.org/cause/climate-health)
- Americares Climate Toolkit: [americares.org](https://www.americares.org/what-we-do/community-health/climate-resilient-health-clinics/)

### Policy

- Kenya RMNCAH-N 2025-2030: [countdown2030.org](https://countdown2030.org/wp-content/uploads/2025/10/RMNXAH-N-for-Official-Processing.pdf)
- PMNCH Climate-MNCH Dialogue Feb 2025: [pmnch.who.int](https://pmnch.who.int/news-and-events/news/item/03-03-2025-addressing-the-impacts-of-climate-change-on-maternal-newborn-and-child-health-and-building-climate-resilient-societies)
- WHO Climate-Informed Health Programmes: [who.int](https://www.who.int/teams/environment-climate-change-and-health/climate-change-and-health/country-support/building-climate-resilient-health-systems/climate-informed-health-programmes)
- CDC BRACE Framework: [cdc.gov](https://www.cdc.gov/climate-health/php/brace/index.html)

### Data Sources

- Open-Meteo Climate API: [open-meteo.com/en/docs/climate-api](https://open-meteo.com/en/docs/climate-api)
- Open-Meteo Seasonal Forecast API: [open-meteo.com/en/docs/seasonal-forecast-api](https://open-meteo.com/en/docs/seasonal-forecast-api)
