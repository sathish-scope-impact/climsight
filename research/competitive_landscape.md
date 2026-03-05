# Competitive Landscape: Climate-Health Decision Support Tools

## Research Summary

Last updated: 2026-03-05

This document analyzes existing tools in the climate-health space, their capabilities, gaps, and how CHART/ClimSight differentiates.

---

## 1. Tool Comparison Matrix

| Tool | Developer | Scope | Resolution | MNCH Focus | Planning | Free/Open |
|---|---|---|---|---|---|---|
| DHIS2 Climate App | HISP/UiO + Global Fund | Climate data import into health systems | ~9 km (ERA5-Land) | No | No | Yes |
| CHAP | HISP/UiO + Wellcome Trust | ML disease forecasting | District-level | No | No | Yes |
| Khushi Baby CHVI | Khushi Baby + Google | Vulnerability indexing | Village-level | Partial | No | No |
| ClimaHealth | WHO + WMO + Wellcome Trust | Knowledge platform | N/A | Partial | No | Yes |
| Americares Toolkit | Americares + Harvard | Clinic action plans | Facility-level | Partial | Yes (clinic) | Yes |
| **CHART/ClimSight** | **Scope Impact / ClimSight** | **Seasonal preparedness planning** | **District-level** | **Yes** | **Yes** | **TBD** |

---

## 2. Detailed Tool Profiles

### DHIS2 Climate App

**URL:** https://dhis2.org/climate/features/

**What it does:**
- Imports ERA5-Land climate data (temperature, precipitation, humidity, vegetation index) directly into DHIS2 data elements ([DHIS2 Climate Features](https://dhis2.org/climate/features/))
- Allows health program managers to correlate climate variables with health outcomes within existing DHIS2 dashboards
- Aggregates climate data to administrative boundaries (district/county level)
- Part of the DHIS2 platform used by 80+ countries for health information management

**Deployment status:**
- Global Fund Climate x Health Catalytic Fund (2025) funding 7 African countries ([DHIS2 Global Fund](https://dhis2.org/global-fund-climate-health-catalytic/))
- Uganda pilot: district-level malaria suitability mapping in 5 districts, expanding to 15
- Malawi pilot (Dec 2025 - Mar 2027): 4 districts for climate-sensitive disease surveillance ([DHIS2 Malawi](https://dhis2.org/malawi-project-to-strengthen-surveillance-climate-sensitive-diseases/))
- Togo: Climate-malaria dashboard operational ([DHIS2 Togo](https://dhis2.org/climate-malaria-dashboard-togo/))

**What it doesn't do:**
- No intervention recommendations
- No MNCH-specific analysis
- No seasonal forecasting (historical/recent data only)
- No planning workflow -- purely surveillance and correlation
- No AI/LLM synthesis

**Relevance to CHART:** Primary data source for health outcomes. CHART should read from DHIS2, not replicate it.

---

### CHAP (Climate Health Analytics Platform)

**URL:** https://chap.dhis2.org/

**What it does:**
- Machine learning disease forecasting integrated with DHIS2 ([CHAP](https://chap.dhis2.org/))
- Predicts malaria, dengue, cholera outbreaks using climate + health data
- Open-source modeling platform with standardized evaluation framework
- Supports multiple ML model types and ensemble approaches
- 5-year project (2024-2029), funded by Wellcome Trust

**Deployment status:**
- Under active development
- Integration with DHIS2 Climate App for combined surveillance + forecasting
- Being piloted alongside Climate App in Malawi and Uganda

**What it doesn't do:**
- No MNCH focus (infectious disease only)
- Forecasts disease burden but doesn't recommend interventions
- No planning or implementation tracking
- No adaptation strategy matching

**Relevance to CHART:** CHART positions as the **planning layer on top of CHAP's predictions**. CHAP says "malaria will spike in July in Kisumu County." CHART says "here are 4 evidence-based interventions for malaria prevention during pregnancy in Kisumu, with implementation timeline."

---

### Khushi Baby CHVI (Climate Health Vulnerability Index)

**URL:** https://www.khushibaby.org/cause/climate-health

**What it does:**
- Village-level Climate Health Vulnerability Index for Rajasthan, India (80M people) ([Khushi Baby](https://www.khushibaby.org/cause/climate-health))
- Uses PCA + regression on exposure, sensitivity, and adaptive capacity indicators ([data.org](https://data.org/playbooks/lessons-from-indias-data-capacity-accelerator-for-climate-and-health/c/fellowships-in-action/creating-a-granular-chvi-and-establishing-causal-links-between-climate-and-health-outcomes/))
- Integrates digital health records from CHW-delivered MNCH services
- Supported by India Health Fund and Google
- Establishing causal links between climate variables and health outcomes at granular level

**Deployment status:**
- Operational in Rajasthan
- Expanding to additional Indian states
- Part of data.org's Data Capacity Accelerator for Climate and Health

**What it doesn't do:**
- Vulnerability scoring only -- no intervention matching
- No seasonal planning workflow
- No seasonal forecasting
- India-only (Rajasthan-specific)
- Not open-source

**Relevance to CHART:** Complementary in India context. Khushi Baby's CHVI provides the vulnerability assessment; CHART provides the seasonal planning response. Potential data-sharing partnership for Indian pilot.

---

### ClimaHealth

**URL:** https://climahealth.info/

**What it does:**
- First global knowledge platform for climate and health (launched 2022) ([WHO announcement](https://www.who.int/news/item/31-10-2022-who-and-wmo-launch-a-new-knowledge-platform-for-climate-and-health))
- Developed by WHO and WMO Joint Office, supported by Wellcome Trust ([ClimaHealth](https://climahealth.info/))
- Resource library with case studies, guidance documents, tools, events
- Covers 4 themes: urban climate/health, infectious diseases, climate/nutrition, resilient health systems ([WHO-WMO Joint Programme](https://climahealth.info/who-wmo-joint-programme/))
- 90+ health focal points in 66 countries nominated from NMHSs and RCCs
- Supports EWARS (Early Warning and Response Systems) for climate-sensitive diseases ([Ethiopia EWARS](https://climahealth.info/resource-library/developing-early-warning-alert-and-response-systems-ewars-to-combat-climate-sensitive-diseases-in-ethiopia/))

**Deployment status:**
- Operational globally
- Ethiopia EWARS: predicted malaria outbreaks in Bahir Dar, enabling emergency preparedness
- Growing resource library

**What it doesn't do:**
- Resource library, not a planning tool
- No district-level output or actionable plans
- No climate data integration or visualization
- No AI/LLM synthesis
- No intervention matching for specific locations/seasons

**Relevance to CHART:** Knowledge source for building the intervention knowledge base. ClimaHealth's curated resources can feed CHART's RAG system. Not a competitor -- complementary knowledge platform.

---

### Americares Climate Resilience Toolkit

**URL:** https://www.americares.org/what-we-do/community-health/climate-resilient-health-clinics/

**What it does:**
- Clinic-level heat/wildfire/flood action plans with patient-facing materials ([Americares](https://www.americares.org/what-we-do/community-health/climate-resilient-health-clinics/))
- Developed with Harvard C-CHANGE and Johnson & Johnson
- Includes pregnancy-specific guidance for heat exposure
- Structured toolkit with implementation checklists
- Training materials for healthcare workers

**Deployment status:**
- Primarily US-focused
- Expanding to Philippines (2025)
- 180+ clinics using toolkit in the US

**What it doesn't do:**
- Clinic-level, not district-level planning
- No climate data integration (generic guidance, not location-specific)
- No seasonal forecasting
- No DHIS2 or health system integration
- Limited to facility-based interventions (no community/household level)

**Relevance to CHART:** Excellent source for intervention content, especially pregnancy-specific heat guidance. Can be adapted for CHART's knowledge base. Facility-level interventions complement CHART's district-level planning.

---

## 3. The Gap CHART Fills

None of the existing tools produce a **seasonal climate-health preparedness plan** for district health officers that:

1. Connects climate outlook data to specific health risks
2. Matches risks to evidence-based MNCH interventions
3. Accounts for local capacity and seasonal patterns
4. Generates structured implementation plans with timelines
5. Tracks implementation and health outcomes

### Value Chain Position

```
Climate Data --> Disease Forecast --> Risk Assessment --> Plan --> Implement --> Monitor
     ^                ^                    ^                ^         ^           ^
  DHIS2 Climate     CHAP              Khushi Baby       CHART     CHART       CHART
  Open-Meteo                          (vulnerability)   (unique)  (unique)    (unique)
```

CHART occupies the **right side** of this value chain -- the planning, implementation, and monitoring steps that no other tool addresses.

---

## 4. Potential Partnerships

| Partner | What They Bring | What CHART Brings |
|---|---|---|
| DHIS2/HISP | Health data infrastructure, 80+ country deployment | MNCH-focused planning layer |
| CHAP | Disease forecasting models | Planning response to forecasts |
| Khushi Baby | Village-level vulnerability data (India) | Seasonal intervention planning |
| ClimaHealth | Curated knowledge resources | Operationalized knowledge into plans |
| Americares | Clinic-level intervention content | District-level scaling and localization |
| CHAMNHA/LSHTM | Kenya-specific intervention evidence | Digital tool to scale interventions |

---

## 5. Risk: Scope Impact's CHART

Scope Impact (Helsinki, Finland) is building a tool called CHART with UBS Optimus Foundation funding. Key details:

- **Partners:** Medic (predictive climate-health models), in-country partners in India and Kenya
- **Status (2024):** Mapped climate-health risks, built first digital prototype
- **AI ambitions:** Predictive models for climate-triggered health risks, ML for resilience assessments
- **Accelerator:** Joined Tech To The Rescue "AI for Changemakers" accelerator (Feb 2025)
- **No public technical architecture disclosed**

This is either: (a) the same project this work supports, (b) a potential partner, or (c) a competitor. Clarify relationship before proceeding with public-facing work.
