# DHIS2 Integration Strategy for CHART

## Research Summary

Last updated: 2026-03-05

This document analyzes the DHIS2 ecosystem, its climate-health tools, and strategies for integrating CHART/ClimSight with DHIS2 as the primary health data infrastructure.

---

## 1. DHIS2 Overview

**What it is:** Open-source health information management system used by 80+ countries, managing health data for 3.9 billion people. Developed by HISP Centre at University of Oslo. ([DHIS2](https://dhis2.org/))

**Why it matters for CHART:** DHIS2 is the de facto standard for health data management in both Kenya and India. Any district-level health planning tool must either integrate with DHIS2 or duplicate its data -- the former is strongly preferred.

**Key capabilities:**
- Routine health data collection and reporting
- Disease surveillance and outbreak detection
- Program monitoring and evaluation
- Dashboard and analytics platform
- Mobile data collection (Android app)
- API-first architecture (comprehensive REST/JSON API)

---

## 2. DHIS2 Climate & Health Ecosystem

### DHIS2 Climate App

**URL:** https://dhis2.org/climate/features/

**What it does:**
- Imports ERA5-Land climate data directly into DHIS2 data elements
- Variables: temperature (min/mean/max), precipitation, relative humidity, vegetation index (NDVI)
- Aggregates to administrative boundaries (district, county, sub-county)
- Enables correlation of climate and health data within DHIS2 dashboards
- Automatic updates with latest ERA5-Land data

**Technical details:**
- DHIS2 app (installable from DHIS2 App Hub)
- Uses Google Earth Engine as backend for ERA5-Land processing ([DHIS2 Climate Data](https://dhis2.org/climate/climate-data/))
- Climate data stored as DHIS2 data elements alongside health data
- Can be visualized in standard DHIS2 maps and charts

### CHAP (Climate Health Analytics Platform)

**URL:** https://chap.dhis2.org/

**What it does:**
- ML-based disease forecasting inside DHIS2
- Predicts malaria, dengue, cholera using climate + health data
- Open-source modeling platform
- Standardized evaluation framework for comparing models
- 5-year project (2024-2029), Wellcome Trust funded

**Technical details:**
- Python-based modeling framework
- Integrates with DHIS2 via API
- Supports multiple ML model types
- Outputs predictions as DHIS2 data elements

### Global Fund Climate x Health Catalytic Fund (2025)

- Funding 7 African countries to implement DHIS2 climate tools
- Countries: specific list not yet public, but includes East and West African nations
- Focus: climate-sensitive disease surveillance using Climate App + CHAP
- Timeline: 2025-2027

### Current Deployments

| Country | Status | Scope |
|---|---|---|
| Uganda | Pilot | 5 districts, expanding to 15. Malaria suitability mapping. |
| Malawi | Starting Dec 2025 | 4 districts. Climate-sensitive disease surveillance. Through Mar 2027. |
| Togo | Operational | Climate-malaria dashboard. National level. |
| Ethiopia | Pilot | EWARS integration. Malaria and meningitis. |

---

## 3. DHIS2 in Kenya

- DHIS2 has been operational in Kenya since 2011
- All 47 counties report through DHIS2
- RMNCAH indicators are standard data elements
- County Health Management Teams (CHMTs) use DHIS2 for planning and reporting
- Monthly reporting cycle for most indicators
- KHIS (Kenya Health Information System) is the national DHIS2 instance

**Relevant DHIS2 data elements in Kenya:**
- ANC visits (1st, 4th+)
- Deliveries (facility, skilled birth attendant)
- Low birth weight cases
- Preterm births (where reported)
- Neonatal deaths
- Under-5 morbidity/mortality by cause
- Malaria cases in pregnancy
- IPTp coverage

---

## 4. DHIS2 in India

- HMIS (Health Management Information System) runs on DHIS2
- Covers all states and districts
- Monthly reporting from sub-center to national level
- ASHA worker reports feed into district-level aggregates
- Integrated Disease Surveillance Programme (IDSP) uses DHIS2

**Relevant DHIS2 data elements in India:**
- ANC registrations and checkups
- Institutional deliveries
- Birth weight data (where recorded)
- IMR and MMR indicators
- Malaria, dengue, chikungunya case counts
- Diarrheal disease in under-5s
- Acute respiratory infections in under-5s
- Nutrition indicators (severe acute malnutrition)

---

## 5. Integration Options

### Option A: Build as DHIS2 App

**Architecture:** CHART runs entirely within DHIS2 as a custom app.

**Pros:**
- Instant access to all health data (no integration needed)
- District officers already use DHIS2 daily
- Fits national health infrastructure
- Recognized as part of "Global Good for Climate & Health" ecosystem
- No separate deployment or login

**Cons:**
- DHIS2 app framework is constrained (React, DHIS2 UI library)
- Hard to build rich planning UIs within DHIS2 conventions
- Dependent on DHIS2 release cycles
- LLM/AI integration within DHIS2 is unprecedented
- Limited control over UX
- DHIS2 instances may have restricted internet access (blocks LLM API calls)

**Effort:** High (DHIS2 app development expertise + LLM integration challenges)

### Option B: Standalone Tool, Import from DHIS2

**Architecture:** CHART is a separate web application that reads data from DHIS2 API.

**Pros:**
- Full control over UX and technology stack
- Can build rich planning workflow (LangGraph, Streamlit/custom UI)
- Faster iteration cycles
- Easier to integrate LLM capabilities
- Can support users without DHIS2 access

**Cons:**
- Must solve DHIS2 API authentication and data synchronization
- Another tool for district officers to learn and maintain
- Risk of not being adopted (adds to tool fatigue)
- Plans and reports not visible in DHIS2

**Effort:** Medium (standard web development + DHIS2 API integration)

### Option C: Hybrid -- Standalone + DHIS2 Read/Write (Recommended)

**Architecture:** CHART as standalone planning tool that reads health data from DHIS2 and can write plans/indicators back.

**Pros:**
- Best of both worlds
- Health data comes from authoritative source (DHIS2)
- Plans can be stored back in DHIS2 as custom data elements
- Rich AI-powered planning UX
- District officers see outputs in their familiar DHIS2 dashboard
- Can function independently where DHIS2 is unavailable

**Cons:**
- Most complex to build
- Requires DHIS2 API expertise for bi-directional sync
- Must handle DHIS2 authentication (OAuth2 or PAT)
- Data mapping between CHART schema and DHIS2 data model

**Effort:** High (but delivers the most value)

---

## 6. DHIS2 API Technical Details

### Authentication

- Basic authentication (username/password) -- simple but not recommended for production
- Personal Access Tokens (PAT) -- recommended for server-to-server
- OAuth2 -- for user-facing applications with DHIS2 login
- API key -- available in newer DHIS2 versions

### Key API Endpoints

```
GET /api/dataValueSets     -- Extract health data values
GET /api/analytics          -- Aggregated analytics queries
GET /api/organisationUnits  -- Facility/district hierarchy
GET /api/dataElements       -- Data element definitions
GET /api/indicators         -- Calculated indicators
GET /api/programs           -- Tracker program data (individual-level)
POST /api/dataValueSets     -- Write data back to DHIS2
```

### Data Extraction Pattern

```python
# Example: Extract ANC visits for a county in Kenya
GET /api/analytics?dimension=dx:ANC_1ST_VISIT
    &dimension=pe:LAST_12_MONTHS
    &dimension=ou:COUNTY_ORG_UNIT_ID
    &outputIdScheme=NAME
```

### Key Considerations

- DHIS2 instances are typically behind government firewalls
- API rate limiting varies by instance
- Data completeness varies by district and indicator
- Monthly reporting lag: 1-2 months typical
- Aggregate data (not individual-level) for most indicators
- Tracker data (individual-level) available for some MNCH programs

---

## 7. Recommended Integration Architecture

```
                    DHIS2 (Kenya KHIS / India HMIS)
                    |                    ^
                    | Read               | Write back
                    | (health data,      | (plans, indicators,
                    |  org units,        |  monitoring data)
                    |  population)       |
                    v                    |
              +------------------+
              |    CHART/        |
              |    ClimSight     |
              |                  |
              |  LangGraph       |  <-- Climate Data APIs
              |  agents          |      (Open-Meteo, ERA5,
              |  RAG (KB)        |       IMD, KMD)
              |  Planning engine |
              +------------------+
                    |
                    v
              District Health Officer
              (Web UI / Reports)
```

### Phase 1 (MVP): Read-Only DHIS2 Integration

1. Read organisation unit hierarchy (districts/counties)
2. Read population denominators
3. Read key MNCH indicators (ANC visits, deliveries, child mortality)
4. Read malaria/diarrhea case counts
5. Use this data to contextualize climate-health plans

### Phase 2: Write-Back Integration

1. Define custom DHIS2 data elements for CHART outputs
2. Write seasonal preparedness plans as DHIS2 documents
3. Write monitoring indicators back to DHIS2
4. Enable DHIS2 dashboard visualization of CHART outputs

### Phase 3: Real-Time Integration

1. Subscribe to DHIS2 data updates via web hooks
2. Trigger re-analysis when new health data arrives
3. Alert district officers when climate-health thresholds are crossed
4. Integrate with DHIS2 messaging for notification delivery

---

## 8. References

- DHIS2 Climate & Health: https://dhis2.org/climate/
- DHIS2 Climate App: https://dhis2.org/climate/features/
- CHAP: https://chap.dhis2.org/
- Global Fund Catalytic Fund: https://dhis2.org/global-fund-climate-health-catalytic/
- Malawi project: https://dhis2.org/malawi-project-to-strengthen-surveillance-climate-sensitive-diseases/
- Togo dashboard: https://dhis2.org/climate-malaria-dashboard-togo/
- DHIS2 API documentation: https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/introduction.html
- DHIS2 Web API: https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/web-api.html
