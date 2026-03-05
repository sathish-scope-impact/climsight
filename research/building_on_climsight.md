# Building CHART on ClimSight: Technical Evaluation

## Research Summary

Last updated: 2026-03-05

This document evaluates every ClimSight component for reuse in CHART, identifies what needs to change, and proposes a concrete implementation plan with file-level detail.

---

## 1. Executive Summary

ClimSight is **70-80% reusable** for CHART. The core infrastructure -- LangGraph orchestration, RAG system, climate data pipeline, tool-calling agents, Streamlit UI, sandbox execution -- is domain-agnostic and production-ready. The remaining 20-30% is domain-specific content (prompts, knowledge bases, health data connectors, health-specific agents) that must be built new.

**Build strategy:** Fork/branch, not rewrite. Extend ClimSight with CHART-specific modules while keeping the existing climate analysis capability intact. This allows a "climate + health" mode rather than replacing one with the other.

---

## 2. Component-by-Component Assessment

### A. LangGraph Workflow Engine

**File:** [`src/climsight/climsight_engine.py`](../src/climsight/climsight_engine.py) (1393 lines)
**Graph construction:** Lines 1338-1393

**Current workflow:**
```
START -> intro_agent -> [parallel: ipcc_rag, general_rag, data_agent, zero_rag_agent, smart_agent]
                     -> prepare_predefined_data -> [data_analysis_agent] -> combine_agent -> END
```

**Assessment: REUSE with modification**

| Sub-component | Lines | Verdict | Notes |
|---|---|---|---|
| `StateGraph(AgentState)` | 1338 | Reuse | Core framework, just add nodes |
| `intro_agent` | 1110-1212 | Modify prompt | Change filter from "climate-related" to "climate-health-related" |
| `ipcc_rag_agent` | 1062-1081 | Reuse + add health RAG | Add parallel `health_rag_agent` using same pattern |
| `general_rag_agent` | 1083-1107 | Reuse as-is | Climate literature still relevant for CHART |
| `data_agent` | 854-916 | Reuse as-is | Climate data extraction unchanged |
| `zero_rag_agent` | 723-852 | Reuse as-is | Location/environment context still needed |
| `smart_agent` | External | Modify | Add health-specific tools (see below) |
| `prepare_predefined_data` | 917-1051 | Extend | Add health-specific predefined outputs |
| `data_analysis_agent` | External | Extend | Add health analysis tools |
| `combine_agent` | 1213-1330 | Modify prompt | Change `system_role` to health-focused synthesis |
| Routing logic | 1053-1060, 1375-1393 | Extend | Add health agent routing |

**Proposed CHART workflow extension:**
```
START -> intro_agent -> [parallel: ipcc_rag, general_rag, health_rag,    <-- NEW
                                   data_agent, zero_rag_agent,
                                   smart_agent, health_data_agent]        <-- NEW
                     -> prepare_predefined_data
                     -> [data_analysis_agent]
                     -> health_risk_agent                                  <-- NEW
                     -> intervention_matching_agent                        <-- NEW
                     -> combine_agent -> END
```

**Key insight:** LangGraph's `add_edge([list], "node")` fan-in pattern (line 1378) makes it trivial to add new parallel agents. Adding `health_rag_agent` and `health_data_agent` requires ~3 lines of graph wiring.

---

### B. Agent State

**File:** [`src/climsight/climsight_classes.py`](../src/climsight/climsight_classes.py) (46 lines)

**Assessment: EXTEND (add fields, don't change existing)**

Current `AgentState` has 30 fields. CHART needs ~10 new fields:

```python
# New fields for CHART (add to AgentState)
health_rag_agent_response: str = ""         # Health literature RAG results
health_data_agent_response: dict = {}       # DHIS2/health data extraction
health_risk_assessment: dict = {}           # Climate -> health risk mapping
intervention_recommendations: list = []     # Matched interventions
seasonal_plan: dict = {}                    # Generated preparedness plan
health_indicators: dict = {}               # MNCH indicators for location
district_context: dict = {}                # Administrative/health system context
health_data_dir: str = ""                  # Health data output directory
health_predefined_plots: list = []         # Health-specific visualizations
monitoring_indicators: list = []           # Plan monitoring metrics
```

**Risk:** None. Pydantic `BaseModel` with defaults means all new fields are optional. Existing agents won't break.

---

### C. RAG System

**File:** [`src/climsight/rag.py`](../src/climsight/rag.py)
**File:** [`src/climsight/embedding_utils.py`](../src/climsight/embedding_utils.py)

**Assessment: REUSE as-is, add new knowledge bases**

The RAG system is already multi-database:
- `ipcc_rag_agent` queries IPCC Chroma DB
- `general_rag_agent` queries general reports Chroma DB
- DestinE tool queries its own parameter Chroma DB ([`destine_retrieval_tool.py`](../src/climsight/tools/destine_retrieval_tool.py))

**What to add:**
1. **Health intervention Chroma DB** -- curated from [JOGH 2025](https://jogh.org/2025/jogh-15-04035), [CHAMNHA](https://doi.org/10.1093/heapol/czaf028), [Americares toolkit](https://www.americares.org/what-we-do/community-health/climate-resilient-health-clinics/), [Kenya RMNCAH-N](https://countdown2030.org/wp-content/uploads/2025/10/RMNXAH-N-for-Official-Processing.pdf)
2. **Health evidence Chroma DB** -- climate-health epidemiological literature (WHO reports, Lancet Countdown, etc.)

**Config addition** (in `config.yml`):
```yaml
health_rag_settings:
  chroma_path_interventions_openai: "rag_db/health_interventions_openai"
  chroma_path_evidence_openai: "rag_db/health_evidence_openai"
  document_path_interventions: './data/health/interventions/'
  document_path_evidence: './data/health/evidence/'
```

**Implementation:** Clone the `ipcc_rag_agent` pattern (lines 1062-1081 of `climsight_engine.py`). Create `health_rag_agent` that queries intervention DB. ~50 lines of new code.

---

### D. Climate Data Pipeline

**File:** [`src/climsight/climate_data_providers.py`](../src/climsight/climate_data_providers.py)
**File:** [`src/climsight/tools/era5_climatology_tool.py`](../src/climsight/tools/era5_climatology_tool.py)
**File:** [`src/climsight/tools/era5_retrieval_tool.py`](../src/climsight/tools/era5_retrieval_tool.py)

**Assessment: REUSE as-is + add Open-Meteo provider**

The provider pattern (`ClimateDataProvider` abstract base class returning `ClimateDataResult`) is designed for extensibility. Current providers: nextGEMS, ICCP, AWI_CM, DestinE.

**New provider needed:** `OpenMeteoSeasonalProvider`
- Implements `ClimateDataProvider` interface
- Calls [Open-Meteo Seasonal Forecast API](https://open-meteo.com/en/docs/seasonal-forecast-api) (ECMWF SEAS5, 36km, 7 months ahead)
- Returns probabilistic forecasts (51 ensemble members) as `ClimateDataResult`
- Free, no API key, REST interface

**Implementation effort:** ~200 lines (new file `src/climsight/tools/openmeteo_seasonal_tool.py`). Follow the pattern in `era5_retrieval_tool.py`.

**Also needed:** Derived health-relevant indicators computed from existing climate data:
- Consecutive days >35C (preterm birth risk threshold)
- Wet-bulb globe temperature (heat stress for pregnant women)
- Standardized Precipitation Index (drought / food security)
- Malaria transmission suitability index (temperature + precipitation + humidity)

These can be computed in `data_analysis_agent` via Python REPL tool -- no new infrastructure needed.

---

### E. Smart Agent (Information Gathering)

**File:** [`src/climsight/smart_agent.py`](../src/climsight/smart_agent.py) (300+ lines)

**Assessment: EXTEND with health-specific tools**

Current tools:
1. **Wikipedia search** -- location context (population, geography, climate)
2. **RAG search** -- IPCC/general climate literature
3. **ECOCROP search** -- crop suitability database

**CHART additions:**
1. **Health vulnerability lookup** -- query disease transmission thresholds (temperature ranges for malaria, dengue, cholera)
2. **Health facility search** -- nearest facilities, capacity, services available
3. **DHIS2 indicator query** -- pull MNCH indicators for the district

**Implementation:** Add 2-3 new tools following the ECOCROP pattern (lines ~260-300 of `smart_agent.py`). Each tool is a function registered via LangChain's `StructuredTool`. ~100 lines per tool.

---

### F. Data Analysis Agent

**File:** [`src/climsight/data_analysis_agent.py`](../src/climsight/data_analysis_agent.py) (600+ lines)

**Assessment: REUSE + add health-specific tools**

The agent already has a powerful tool set:
- Python REPL (persistent Jupyter kernel) -- [`tools/python_repl.py`](../src/climsight/tools/python_repl.py)
- ERA5 retrieval -- [`tools/era5_retrieval_tool.py`](../src/climsight/tools/era5_retrieval_tool.py)
- DestinE search + retrieval -- [`tools/destine_retrieval_tool.py`](../src/climsight/tools/destine_retrieval_tool.py)
- Image viewer (GPT-4V analysis) -- [`tools/image_viewer.py`](../src/climsight/tools/image_viewer.py)
- Reflection (plot quality scoring) -- [`tools/reflection_tools.py`](../src/climsight/tools/reflection_tools.py)
- Visualization strategy -- [`tools/visualization_tools.py`](../src/climsight/tools/visualization_tools.py)
- Predefined plots -- [`tools/predefined_plots.py`](../src/climsight/tools/predefined_plots.py)

**CHART tools to add:**

| New Tool | File | Purpose |
|---|---|---|
| `health_risk_calculator` | `tools/health_risk_tool.py` | Compute climate-health risk scores from climate data + epidemiological thresholds |
| `intervention_matcher` | `tools/intervention_tool.py` | RAG search over intervention KB, filtered by risk profile + local capacity |
| `dhis2_query` | `tools/dhis2_tool.py` | Pull health indicators from DHIS2 API for the district |
| `openmeteo_seasonal` | `tools/openmeteo_seasonal_tool.py` | Fetch seasonal forecast for next 7 months |
| `health_predefined_plots` | `tools/health_plots.py` | Disease-climate correlation, epidemic timeline, vulnerability map |

**Registration:** Add to tools list in `data_analysis_agent.py` (~line 595). Add descriptions to `_create_tool_prompt()` (~line 120). Following the [CLAUDE.md guidance](../CLAUDE.md#adding-new-tools-to-data-analysis-agent).

---

### G. Existing Tools -- Reuse Assessment

| Tool | File | CHART Reuse | Notes |
|---|---|---|---|
| Python REPL | `tools/python_repl.py` | **As-is** | Persistent Jupyter kernel for health data analysis, epidemiological modeling, visualization |
| Image Viewer | `tools/image_viewer.py` | **As-is** | Analyze health-climate plots via GPT-4V |
| Reflection | `tools/reflection_tools.py` | **As-is** | Quality scoring for health visualizations (7/10 threshold) |
| Visualization Strategy | `tools/visualization_tools.py` | **As-is** | Domain-agnostic visualization advice |
| ERA5 Climatology | `tools/era5_climatology_tool.py` | **As-is** | Climate baseline still needed for CHART |
| ERA5 Retrieval | `tools/era5_retrieval_tool.py` | **As-is** | Historical climate time series |
| DestinE Retrieval | `tools/destine_retrieval_tool.py` | **As-is** | Climate projections (SSP3-7.0) |
| Predefined Plots | `tools/predefined_plots.py` | **Extend** | Add health-specific plot types alongside existing climate plots |
| Get Data Components | `tools/get_data_components.py` | **As-is** | Extract specific climate variables |
| Package Tools | `tools/package_tools.py` | **As-is** | Dynamic pip install for health packages |

**10 out of 10 existing tools are reusable.** 3 need extensions, 7 work as-is.

---

### H. Geographic, Environmental, Economic Functions

| Module | File | CHART Reuse | Notes |
|---|---|---|---|
| `geo_functions.py` | Location, land/water detection, elevation, soil, land use | **As-is** | All location context relevant for health planning |
| `environmental_functions.py` | Biodiversity (GBIF), natural hazards (GDIS) | **Extend** | Add disease vector habitat lookup (GBIF for mosquito species), epidemic history |
| `economic_functions.py` | Population data and projections | **As-is** | Population denominators critical for health burden calculations |
| `climate_functions.py` | Load/extract climate model data | **As-is** | Climate data extraction unchanged |
| `extract_climatedata_functions.py` | Model-specific data handling | **As-is** | Handles variable naming across models |

---

### I. Configuration System

**File:** [`config.yml`](../config.yml) (381 lines)

**Assessment: EXTEND with health sections**

New config sections needed:

```yaml
# ============ CHART Health Configuration ============
chart_mode: true  # Enable CHART health analysis mode

# Health RAG databases
health_rag_settings:
  enabled: true
  chroma_path_interventions: "rag_db/health_interventions"
  chroma_path_evidence: "rag_db/health_evidence"
  document_path_interventions: './data/health/interventions/'
  document_path_evidence: './data/health/evidence/'

# DHIS2 Integration
dhis2_settings:
  enabled: false  # Enable DHIS2 health data integration
  base_url: ""    # e.g., "https://khis.health.go.ke/api"
  auth_type: "pat"  # "basic", "pat", or "oauth2"
  # token set via DHIS2_API_TOKEN environment variable

# Health risk thresholds
health_thresholds:
  heat_preterm_risk_temp: 35.0     # Celsius, consecutive days trigger
  heat_preterm_risk_days: 3        # Consecutive days above threshold
  malaria_temp_min: 18.0           # Minimum for transmission
  malaria_temp_max: 34.0           # Maximum for transmission
  cholera_flood_threshold: 50.0    # mm/day precipitation trigger

# Health-specific system prompt (overrides system_role for CHART)
health_system_role: |
  You are a climate-health decision support system...
  [CHART-specific combine_agent prompt]

# Open-Meteo seasonal forecast
openmeteo_seasonal:
  enabled: true
  forecast_months: 7
```

**The config system is YAML-based and fully extensible.** New sections don't affect existing functionality.

---

### J. Streamlit UI

**File:** [`src/climsight/streamlit_interface.py`](../src/climsight/streamlit_interface.py)

**Assessment: EXTEND with health mode UI**

The UI currently has:
- Map with click-to-select location
- Text input for question
- Toggles for ERA5, DestinE, smart agent, data analysis
- Climate data source dropdown
- Output display with text, plots, downloadable datasets

**CHART additions:**
- Toggle: "Enable CHART health analysis mode"
- When enabled: show health-specific options (district selection, MNCH indicators toggle, DHIS2 connection)
- Health-specific output sections (risk assessment, intervention recommendations, seasonal plan)
- Additional predefined health plots

**The UI is Streamlit-based** -- modular, easy to extend with `st.sidebar` toggles and `st.tabs`. Not tightly coupled to specific agents.

---

### K. Data Container and Streaming

| Module | File | Verdict |
|---|---|---|
| `data_container.py` | DataFrames, figures, xarray datasets | **As-is** -- domain-agnostic container |
| `stream_handler.py` | Progress updates for UI | **As-is** -- just change message strings |
| `terminal_interface.py` | CLI mode | **As-is** -- useful for batch health analysis |

---

## 3. New Components to Build

### Priority 1: Health Knowledge Base (Week 1-4)

| Component | Effort | Dependencies |
|---|---|---|
| Curate intervention documents from [JOGH 2025](https://jogh.org/2025/jogh-15-04035), [CHAMNHA](https://doi.org/10.1093/heapol/czaf028), [Americares](https://www.americares.org/what-we-do/community-health/climate-resilient-health-clinics/) | 2 weeks (manual curation) | None |
| Build Chroma vector store for interventions | 2 days | Curated documents |
| Build Chroma vector store for health evidence | 2 days | Curated documents |
| Create `health_rag_agent` (clone of `ipcc_rag_agent` pattern) | 1 day | Chroma DBs |

### Priority 2: Health Risk Mapping (Week 3-6)

| Component | Effort | Dependencies |
|---|---|---|
| `tools/health_risk_tool.py` -- climate-to-health risk scoring | 1 week | Health thresholds research |
| `tools/intervention_tool.py` -- RAG-powered intervention matching | 1 week | Intervention Chroma DB |
| Health-specific prompts for `combine_agent` (`health_system_role`) | 3 days | Risk tool + intervention tool |
| Extend `AgentState` with health fields | 1 day | None |

### Priority 3: Seasonal Forecast Integration (Week 4-6)

| Component | Effort | Dependencies |
|---|---|---|
| `tools/openmeteo_seasonal_tool.py` -- Open-Meteo seasonal forecast | 3 days | None (free API) |
| Derived health indicators (heat stress, drought, malaria suitability) | 3 days | Climate data pipeline |
| `tools/health_plots.py` -- health-specific predefined plots | 1 week | Health risk tool |

### Priority 4: DHIS2 Integration (Week 6-10)

| Component | Effort | Dependencies |
|---|---|---|
| `tools/dhis2_tool.py` -- read health indicators from DHIS2 | 2 weeks | DHIS2 instance access |
| District-level health context agent | 1 week | DHIS2 tool |
| Write-back of plans to DHIS2 | 2 weeks | Phase 2 |

### Priority 5: UI and Config (Week 8-10)

| Component | Effort | Dependencies |
|---|---|---|
| CHART mode toggle in Streamlit UI | 2 days | All above |
| `config_chart.yml` -- CHART-specific config | 1 day | All above |
| Health-specific output formatting | 3 days | Combine agent prompt |

---

## 4. What NOT to Change

These components work as-is and should not be modified:

1. **LangGraph framework** -- just add nodes, don't restructure
2. **RAG infrastructure** (`rag.py`, `embedding_utils.py`) -- add new DBs, don't change the query mechanism
3. **Climate data providers** -- add new providers, don't modify existing ones
4. **Python REPL tool** -- already supports arbitrary analysis
5. **Image viewer / reflection tools** -- domain-agnostic
6. **Geographic functions** -- all location context is health-relevant
7. **Population data** -- critical denominator for health metrics
8. **Data container** -- domain-agnostic packaging
9. **Stream handler** -- just update message strings
10. **Download data pattern** -- extend `data_sources.yml` with health data URLs

---

## 5. Risk Assessment

| Risk | Impact | Mitigation |
|---|---|---|
| Health intervention KB is too thin (only 79 interventions mapped) | CHART recommendations will be generic | Start with heat x pregnancy (strongest evidence from [CHAMNHA](https://doi.org/10.1093/heapol/czaf028)); expand iteratively |
| DHIS2 access requires institutional agreements | Blocks health data integration | Build MVP without DHIS2; use Open-Meteo + curated health context. Add DHIS2 in Phase 2 |
| Open-Meteo seasonal forecast at 36km too coarse for districts | Forecasts may not capture local variation | Supplement with [IMD](https://mausam.imd.gov.in/) (India) and [KMD](https://meteo.go.ke/) (Kenya) seasonal outlooks |
| LLM hallucination on health interventions | Dangerous if acted upon | RAG-only responses for interventions (no free-form generation); add citations + confidence scores |
| Prompt engineering for health domain is harder than climate | Incorrect risk assessments | Use structured output (Pydantic models) for risk scores; validate against known epidemiological thresholds |
| Scope creep from climate tool to health planning tool | Dilutes focus, delays delivery | Define MVP scope strictly: heat x pregnancy in 3 Kenyan counties. Expand only after validation |

---

## 6. Recommended Implementation Order

```
Phase 1: "Climate + Health RAG" (4 weeks)
  - Health intervention Chroma DB
  - Health evidence Chroma DB
  - health_rag_agent (parallel to existing RAG agents)
  - Modified combine_agent prompt for health synthesis
  - Config extensions
  Result: ClimSight that also returns health-relevant information for any location

Phase 2: "Health Risk Scoring" (4 weeks)
  - health_risk_tool (climate -> health risk mapping)
  - intervention_tool (risk -> intervention matching)
  - Open-Meteo seasonal forecast tool
  - Health-specific predefined plots
  - CHART mode toggle in UI
  Result: District officers get risk scores + matched interventions for upcoming season

Phase 3: "DHIS2 + Planning" (6 weeks)
  - DHIS2 read integration (health indicators, org units)
  - Seasonal preparedness plan generation
  - Health-specific output formatting
  - Monitoring indicator framework
  Result: Full CHART workflow from climate forecast to implementable plan

Phase 4: "Production + Scale" (ongoing)
  - DHIS2 write-back
  - National met service integration (IMD, KMD)
  - Multi-district batch processing
  - User feedback loop
  - KB expansion based on field validation
```

---

## 7. Lines of Code Estimate

| Component | New Lines | Modified Lines | Files |
|---|---|---|---|
| `AgentState` extensions | 15 | 0 | 1 |
| Health RAG agent | 50 | 10 | 2 (engine + config) |
| `health_risk_tool.py` | 250 | 0 | 1 new |
| `intervention_tool.py` | 200 | 0 | 1 new |
| `openmeteo_seasonal_tool.py` | 200 | 0 | 1 new |
| `dhis2_tool.py` | 300 | 0 | 1 new |
| `health_plots.py` | 300 | 0 | 1 new |
| Health system prompt | 100 | 0 | config |
| Workflow wiring | 30 | 20 | engine |
| UI extensions | 100 | 30 | streamlit_interface |
| Config extensions | 50 | 0 | config |
| Health data curation | N/A (documents) | N/A | data/ |
| **Total** | **~1,595** | **~60** | **6 new + 4 modified** |

**Bottom line:** ~1,600 new lines of code + 60 modified lines + curated health documents. The existing 5,000+ lines of ClimSight infrastructure remain untouched.
