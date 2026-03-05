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

---

## Appendix A: Critical Analysis -- Pros, Cons, and 5 Whys

### Pros of This Evaluation

1. **Concrete and traceable.** Every claim points to specific files and line numbers. A developer can verify each assessment against the actual codebase rather than trusting abstract claims. For example, the graph wiring analysis references the exact `add_edge` / `add_conditional_edges` calls at `climsight_engine.py:1374-1393` -- these are verifiable in 30 seconds.

2. **Phased roadmap reduces delivery risk.** Phase 1 delivers value (health RAG) without touching DHIS2 or building complex health tools. This is validated by the codebase: `ipcc_rag_agent` (lines 1062-1081) is 20 lines that call `query_rag()` and return a string. Cloning this pattern for a `health_rag_agent` is genuinely trivial if the Chroma DB exists. Each phase is independently useful, so the project doesn't fail if a later phase stalls.

3. **"Extend, don't rewrite" preserves optionality.** The LangGraph fan-in pattern at line 1378 (`workflow.add_edge([list], "prepare_predefined_data")`) demonstrates that adding new parallel agents requires only appending to the list. The existing `AgentState` (37 fields, all with defaults in `climsight_classes.py:9-45`) uses Pydantic `BaseModel` with default values, so new fields don't break existing agents. This is not hypothetical -- `smart_agent` was added this way (line 1381-1382: conditional edge, gated by config flag).

4. **Provider pattern enables incremental data source addition.** `climate_data_providers.py` has 4 concrete providers (NextGEMS at line 227, ICCP at line 470, AWICM at line 699, DestinE at line 833) all inheriting from `ClimateDataProvider` (line 58). Each is ~200-270 lines. Adding `OpenMeteoSeasonalProvider` follows the identical pattern. The 1,181-line file proves the pattern works at scale.

5. **Risk table is honest about known unknowns.** The document explicitly calls out thin intervention KB, DHIS2 access barriers, LLM hallucination, and scope creep -- rather than hiding them. However, as the Cons section below argues, this honesty doesn't go far enough.

### Cons of This Evaluation

1. **The 70-80% reuse claim is measured by component count, not by effort.** The evaluation counts 10/10 tools reusable, but look at what those tools actually are: Python REPL (`tools/python_repl.py`), image viewer (`tools/image_viewer.py`), reflection (`tools/reflection_tools.py`), visualization strategy (`tools/visualization_tools.py`). These are generic execution shells -- they don't encode any domain knowledge. The ClimSight codebase is 11,620 lines of source code across all `.py` files. The "reusable" infrastructure constitutes the plumbing, while the value-creating health domain logic (risk models, intervention matching, clinical validation) is 100% new. Counting plumbing tools as "reuse" inflates the percentage.

2. **LOC estimate (~1,600 lines) is misleadingly small.** Evidence from the codebase:
   - ClimSight's own test suite is 1,223 lines covering 34 test functions across 6 files. Even this is thin coverage for 11,620 lines of production code (10.5% ratio). CHART's ~1,600 new lines would need at minimum 800-1,600 lines of tests -- not mentioned in the estimate.
   - The `intro_agent` prompt alone (lines 1112-1165 of `climsight_engine.py`) is 53 lines of carefully crafted exclusion logic. The evaluation allocates "3 days" for the entire health system prompt, but ClimSight's `data_analysis_agent` prompt builder (`_create_tool_prompt()`, lines 476-676) is **200 lines** of prompt engineering. Health domain prompts will be equally complex.
   - Health knowledge base curation is listed as "N/A (documents)" but building the IPCC RAG database required curating, chunking, and embedding hundreds of pages of IPCC reports. Doing the same for health literature (JOGH 2025, CHAMNHA, WHO guidelines, Lancet Countdown) is comparable effort -- estimated weeks of domain expert work, not engineering.
   - No error handling budget for external APIs. The existing `era5_retrieval_tool.py` and `destine_retrieval_tool.py` contain extensive error handling for network failures, missing data, and API changes. DHIS2 and Open-Meteo tools will need the same.

3. **No clinical validation strategy.** For a tool that will influence health resource allocation affecting pregnant women and children, the evaluation mentions no:
   - Comparison against existing epidemiological models (e.g., [Malaria Atlas Project](https://malariaatlas.org/) for malaria, [WHO heat-health guidelines (2021)](https://www.who.int/publications/i/item/9789240038509) for heat stress)
   - Ethics review or IRB process (required for any system processing health data or making clinical recommendations in both [Kenya](https://nacosti.go.ke/) and [India](https://main.icmr.nic.in/content/ethical-guidelines))
   - False positive/negative analysis for risk scores and intervention recommendations
   - Expert review protocol before deployment -- the CHAMNHA project itself took 3+ years from concept to [validated framework](https://doi.org/10.1093/heapol/czaf028)
   - Liability framework if recommendations prove harmful (who is responsible when an LLM-recommended intervention fails?)

4. **DHIS2 integration is severely underestimated.** "2 weeks read + 2 weeks write" ignores well-documented complexity:
   - DHIS2 metadata model has [13 dimensions](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-241/metadata.html) including org unit hierarchies (Kenya has 47 counties, 290 sub-counties, ~5,000 facilities), indicator definitions, data element groups, and category combinations
   - Institutional access requires MOH Data Sharing Agreements. The [Kenya Health Information System (KHIS)](https://hiskenya.org/) requires formal MoU with the Division of Health Informatics. Timeline: typically 3-6 months ([HISP East Africa](https://www.hispeastafrica.org/) can facilitate but does not fast-track)
   - [DHIS2 API documentation](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-241/introduction.html) describes pagination, field filtering, and rate limiting complexities
   - Real-world evidence: the [CHAP tool](https://github.com/dhis2-chap/chap-core) (Climate Health Anticipation Platform), built by DHIS2's own team at University of Oslo, has been in development since 2023 and DHIS2 integration is still listed as "in progress" as of 2025

5. **Hallucination mitigation is insufficient.** "RAG-only responses for interventions" does not solve the problem. Evidence from the codebase:
   - The `combine_agent` (lines 1213-1330 of `climsight_engine.py`) uses free-form LLM generation with a system prompt. Even though RAG provides source documents, the LLM synthesizes them without structured output validation. The `routeResponse` Pydantic model used in `intro_agent` (line 1178) shows structured output *is* possible in this codebase -- but the evaluation doesn't propose it for health recommendations.
   - RAG retrieval uses cosine similarity (`query_rag` at `rag.py:140-203`), which can surface semantically similar but clinically inappropriate documents. Example: a document about "heat stress interventions in agriculture" might score high for "heat stress interventions for pregnant women" -- same terms, completely different clinical context.
   - No human-in-the-loop review is proposed before recommendations reach end users. Compare with the existing `reflection_tools.py` which uses a 7/10 quality threshold for plots -- a similar "clinical review gate" for health recommendations is absent.

6. **"Fork/branch" strategy creates a maintenance burden with no sync plan.** ClimSight is actively developed -- the git log shows ongoing commits to `climsight_engine.py`, `data_analysis_agent.py`, and `config.yml`. As the upstream codebase evolves (new agents, API changes, dependency updates), the CHART branch will diverge. The evaluation proposes no strategy for staying in sync -- no mention of upstream contribution, cherry-picking, modular packaging, or plugin architecture. Each provider in `climate_data_providers.py` (227-833+ lines each) is tightly coupled to the engine; modifying the provider interface upstream would break CHART's health providers.

7. **No user research validates the assumed workflow.** The evaluation assumes district health officers need a map-based, LLM-powered tool that generates seasonal preparedness plans. But there is no evidence of:
   - User interviews with target users in Kenya or India
   - Workflow analysis of how district officers currently make decisions (the [Kenya RMNCAH-N Investment Case](https://countdown2030.org/wp-content/uploads/2025/10/RMNXAH-N-for-Official-Processing.pdf) describes their current workflow, which is spreadsheet and meeting-based)
   - Comparison with tools they already use (DHIS2 dashboards, Excel, paper-based Annual Work Plans)
   - Assessment of LLM trust and digital literacy in target user populations (Kenya's [digital health strategy](https://www.health.go.ke/) notes significant gaps in rural county digital infrastructure)

8. **Regulatory and compliance gaps.** Health data in Kenya is governed by the [Data Protection Act (2019)](http://kenyalaw.org/kl/fileadmin/pdfdownloads/Acts/2019/TheDataProtectionAct__No24of2019.pdf) and in India by the [Digital Personal Data Protection Act (2023)](https://www.meity.gov.in/writereaddata/files/Digital%20Personal%20Data%20Protection%20Act%202023.pdf). The evaluation mentions no:
   - Data governance framework (health data is classified as "sensitive personal data" in both jurisdictions)
   - Patient data anonymization requirements (DHIS2 aggregate data may still contain identifiable district-level patterns)
   - Cross-border data transfer rules (relevant if using OpenAI API -- patient data sent to US-hosted LLMs may violate both countries' data localization provisions)
   - Health-specific regulatory requirements for decision support tools (Kenya's [PPB](https://pharmacyboardkenya.org/) and India's [CDSCO](https://cdsco.gov.in/) may classify clinical decision support as a medical device)

9. **Kenya pilot scope is aspirational, not grounded.** "3 Kenyan counties" are unnamed, data availability is unconfirmed, and no MOH partnership is established. The [CHAMNHA project](https://doi.org/10.1093/heapol/czaf028) -- which is the closest comparable -- worked in Burkina Faso, Kenya, and Ethiopia with institutional partnerships that took over a year to establish. Without a specific county partner who has agreed to participate and share DHIS2 access, the pilot timeline is fiction.

10. **Open-Meteo as primary seasonal forecast has accuracy limitations.** The evaluation correctly notes 36km resolution may be too coarse, but understates the problem: ECMWF SEAS5 (which Open-Meteo redistributes) has [documented low skill for East African precipitation](https://doi.org/10.1175/JCLI-D-19-0898.1) during the long rains (March-May), which is precisely the season most relevant for waterborne disease forecasting. The [Greater Horn of Africa Climate Outlook Forum (GHACOF)](https://www.icpac.net/seasonal-forecast/) produces regional consensus forecasts that outperform individual model runs -- but integrating GHACOF requires institutional relationships with [ICPAC](https://www.icpac.net/), not just an API call.

---

### 5 Whys Analysis

The central claim of this evaluation is: **"ClimSight is 70-80% reusable for CHART."** This claim drives the entire implementation strategy -- fork rather than build, 14-week timeline, ~1,600 LOC. If the claim is wrong, the strategy collapses. Let's stress-test it.

#### Why 1: Why do we claim 70-80% reusability?

**Because 10 of 10 existing tools are reusable, and 7 of 10 major components (LangGraph engine, RAG system, climate pipeline, data analysis agent, geo functions, config system, UI) can be used as-is or with minor modifications.**

This is true at the infrastructure level. Evidence from the codebase:
- The LangGraph graph construction (`climsight_engine.py:1338-1393`) is 57 lines of wiring. Adding a new parallel agent requires 2 lines: `workflow.add_node("health_rag_agent", health_rag_agent)` and appending to the fan-in list at line 1378. This is proven by how `smart_agent` was added -- conditional on a config flag (lines 1381-1382).
- The RAG `load_rag()` function (`rag.py:56-113`) uses a `db_type` parameter that selects the Chroma path from config via `f'chroma_path_{db_type}_openai'`. Adding a health RAG literally means adding a config entry and passing `db_type='health_interventions'`. The function doesn't know what's in the database.
- The Python REPL (`tools/python_repl.py`), image viewer (`tools/image_viewer.py`), and reflection tools (`tools/reflection_tools.py`) contain zero climate-specific logic.

But the 70-80% figure conflates "components we don't need to rewrite" with "fraction of the work that's already done." These are very different things.

#### Why 2: Why is "components we don't rewrite" different from "work that's already done"?

**Because infrastructure is necessary but not sufficient for delivering CHART's value. The value-creating work -- health knowledge, risk models, clinical validation, data partnerships -- is entirely new and lives outside ClimSight's codebase.**

Evidence: look at what ClimSight's "reusable" components actually do vs. what creates user value:

| Component | Lines | What it does | Domain knowledge encoded |
|---|---|---|---|
| `python_repl.py` | 204 | Executes arbitrary Python in Jupyter kernel | Zero |
| `image_viewer.py` | 89 | Sends image to GPT-4V for description | Zero |
| `reflection_tools.py` | 147 | Scores plot quality on 1-10 scale | Zero |
| `visualization_tools.py` | 124 | Lists files, suggests viz strategy | Zero |
| LangGraph wiring | 57 | Connects nodes in a DAG | Zero |
| RAG infrastructure | 204 | Loads Chroma DB, queries, returns docs | Zero |
| **Total "reusable"** | **~825** | **Generic execution plumbing** | **Zero domain knowledge** |

Now compare with where ClimSight's actual climate value lives:

| Component | Lines | Domain knowledge |
|---|---|---|
| `climate_data_providers.py` | 1,181 | 4 providers with model-specific variable mappings, coordinate systems, time handling |
| `predefined_plots.py` | 600+ | ERA5 variable maps, cross-model column matching, wind speed computation |
| `climsight_engine.py` prompts | ~300 | Climate-specific exclusion rules, data agent instructions, combine agent synthesis |
| `smart_agent.py` tools | 300+ | ECOCROP database queries, climate-relevant Wikipedia extraction |
| Climate NetCDF files | ~8GB | The actual data |

CHART needs the *equivalent* of the second table for the health domain: health data providers, health-specific plots, health prompts, health tools, and curated health data. This is the 20-30% that the evaluation identifies as "new" -- but it's where 70-80% of the actual project effort will concentrate.

The LOC estimate reflects this blind spot: ~1,600 new lines sounds small, but the evaluation categorizes health knowledge curation as "N/A (documents)" -- effectively assigning zero engineering effort to the single most critical dependency. For context, ClimSight's own `download_data.py` downloads ~8GB of climate data that took years of scientific effort to produce. CHART's health knowledge base doesn't exist yet.

#### Why 3: Why is health knowledge curation the most critical and most underestimated dependency?

**Because CHART's trustworthiness depends entirely on the quality of its knowledge base, and building a clinically validated health knowledge base is a fundamentally different task from software engineering.**

The evaluation identifies 79 interventions from [JOGH 2025](https://jogh.org/2025/jogh-15-04035) and proposes a Chroma vector store. But turning academic papers into a decision-support knowledge base requires work that the codebase cannot shortcut:

- **Domain expertise** to select, validate, and contextualize interventions (a public health specialist, not a software engineer). The [CHAMNHA project](https://doi.org/10.1093/heapol/czaf028) required a multi-disciplinary team across 3 countries working for 3+ years to produce a validated climate-health framework. The evaluation proposes "2 weeks (manual curation)" for comparable scope.
- **Evidence grading** -- not all 79 interventions have equal evidence strength. The JOGH 2025 systematic review itself notes that evidence quality ranges from "high" (RCTs for insecticide-treated nets) to "very low" (expert opinion for institutional cooling). An ungraded RAG database treats all documents as equally authoritative.
- **Contextual adaptation** -- an intervention proven in Bangladesh may not apply in arid Kenya. The RAG system's cosine similarity (`rag.py:140-203`) retrieves based on text similarity, not clinical context. A document about "cool roofs reducing heat exposure in Dhaka slums" will score high for a query about "heat exposure in Nairobi informal settlements" -- similar text, but the building materials, climate patterns, and implementation feasibility are completely different.
- **Ongoing maintenance** -- health evidence evolves. The Lancet Countdown publishes annual updates; WHO guidelines change. ClimSight's IPCC RAG database is relatively stable (IPCC reports are published every 5-7 years). A health KB needs a curation pipeline, not a one-time build.
- **Liability review** -- if CHART recommends an intervention and outcomes worsen, who bears responsibility? This question has no analogue in ClimSight's climate domain.

None of this is addressable by reusing ClimSight's RAG infrastructure. The `load_rag()` and `query_rag()` functions store and retrieve documents; the hard problem is what goes into those documents and whether the retrieval produces clinically appropriate results.

#### Why 4: Why is clinical appropriateness harder to achieve than technical retrieval accuracy?

**Because health recommendations have life-or-death consequences, and the failure mode of an LLM-powered health tool is not "wrong answer" but "confidently wrong answer that gets acted upon."**

ClimSight's climate analysis can be approximate. The `data_agent` (lines 854-916) extracts temperature and precipitation projections; if the temperature projection is off by 1°C or the precipitation forecast has 30% error, the `combine_agent` synthesizes a slightly less accurate climate narrative. The user -- typically a climate-literate researcher -- can evaluate this against their domain knowledge. No one is harmed by an imprecise climate outlook.

CHART operates in a fundamentally different risk regime:

- **False negative** (failing to flag heat-preterm risk): A district doesn't pre-position neonatal supplies. Evidence: [Chersich et al. (2020)](https://doi.org/10.1016/j.envint.2020.105567) found that heat exposure during pregnancy is associated with a 16% increase in preterm birth risk per 1°C increase in mean temperature above 25°C. Missing this threshold in a forecast has direct clinical consequences.
- **False positive** (flagging cholera risk when conditions don't support it): Scarce resources are diverted from actual needs. In Kenya's 47 counties, health budgets are allocated annually via the [County Integrated Development Plans](https://www.devolution.go.ke/). Misallocating even 5% of a county's health budget based on a false alarm has real opportunity cost.
- **Inappropriate intervention** (suggesting cold-chain-dependent vaccines in an area without reliable electricity): [Kenya's cold chain coverage](https://www.gavi.org/programmes-impact/country-hub/africa/kenya) reaches only ~76% of facilities. Recommending a cold-chain-dependent intervention to a facility without it wastes limited procurement budgets.

The evaluation's mitigation -- "RAG-only responses, citations, confidence scores" -- addresses the technical mechanism but not the clinical validation. The `combine_agent`'s system prompt (`config['system_role']`) gives the LLM free-form synthesis authority. ClimSight trusts this because climate information is informational. CHART cannot afford the same trust level for prescriptive health recommendations.

This is why the evaluation needs a validation strategy: not just "does the system return relevant documents?" but "does the system produce recommendations that a clinical expert would endorse for this specific context?"

#### Why 5: Why doesn't ClimSight's architecture inherently address the trust and validation challenge?

**Because ClimSight was designed as an information synthesis tool (combining data sources for a knowledgeable user), not as a prescriptive decision-support tool (recommending actions to a potentially non-expert user in a high-stakes domain).**

This is visible throughout the codebase. The `combine_agent` prompt (`climsight_engine.py:1213-1330`) asks the LLM to synthesize climate information into a narrative. It does not:
- Constrain outputs to a validated intervention list
- Require confidence scores or evidence grades
- Include structured output validation (compare with `intro_agent`'s `routeResponse` Pydantic model at line 1178, which *does* use structured output -- proving the pattern exists but wasn't applied to the combine step)
- Provide a "refuse to recommend" pathway when evidence is insufficient

This is the deepest asymmetry between ClimSight and CHART:

| Dimension | ClimSight (evidence from codebase) | CHART (required) |
|---|---|---|
| **Output type** | Informational narrative (`combine_agent` returns `final_answer: str`) | Prescriptive action plan (needs structured `InterventionRecommendation` Pydantic model) |
| **User expertise** | Climate-literate researchers (can evaluate LLM output) | District health officers ([Kenya has ~1 doctor per 10,000 people](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/medical-doctors-(per-10-000-population)); officers may defer to system) |
| **Error consequence** | Suboptimal planning (no harm) | Misallocated health resources, preventable morbidity/mortality |
| **Validation standard** | "Is climate data approximately correct?" (verified by `reflection_tools.py` 7/10 threshold for plots) | "Would a clinical expert endorse this for *this specific district*?" (no analogue exists in codebase) |
| **Regulatory regime** | None (climate information is unregulated) | [Kenya Data Protection Act 2019](http://kenyalaw.org/kl/fileadmin/pdfdownloads/Acts/2019/TheDataProtectionAct__No24of2019.pdf); potential [medical device classification](https://pharmacyboardkenya.org/) |
| **Trust model** | User verifies against domain knowledge | User may lack domain knowledge to challenge recommendations |

ClimSight's architecture is excellent at the first task -- synthesizing multiple data sources into coherent information. But CHART needs guardrails that go beyond architecture:

- **Clinical review gates** before recommendations reach users (no analogue in ClimSight; the `reflection_tools.py` quality gate is for plot aesthetics, not clinical accuracy)
- **Structured output schemas** validated against epidemiological models (the codebase has `routeResponse` at line 1178 and `ClimateDataResult` in `climate_data_providers.py:33-55` -- these patterns should be extended to `HealthRiskAssessment` and `InterventionRecommendation` Pydantic models with required fields like `evidence_grade`, `confidence_interval`, and `contraindications`)
- **Explainability** that lets a district officer understand *why* a recommendation was made (not just "the RAG found this document" -- `query_rag` returns source filenames at `rag.py:185-195` but not reasoning chains)
- **Feedback loops** where field outcomes update the knowledge base (ClimSight's Chroma DBs are static; health KBs need a curation pipeline)
- **Graceful degradation** when data is missing (common in low-resource settings; ClimSight's `data_agent` returns `"No data available"` as a string -- CHART needs structured missing-data handling that adjusts confidence scores)

None of these are architectural problems that ClimSight's LangGraph workflow solves. They are product design, clinical governance, and operational challenges that require expertise beyond software engineering.

---

### 5 Whys Summary

| Level | Question | Finding |
|---|---|---|
| **Why 1** | Why 70-80% reusable? | Infrastructure (LangGraph, RAG, tools) is domain-agnostic -- genuinely reusable |
| **Why 2** | Why isn't infrastructure = work done? | Value-creating work (health knowledge, validation, data access) is entirely new |
| **Why 3** | Why is health knowledge the critical gap? | Building a clinically validated KB requires domain expertise, evidence grading, and ongoing curation -- not software engineering |
| **Why 4** | Why is clinical validation so hard? | Health recommendations are high-stakes; failure modes include confidently wrong actions with real human consequences |
| **Why 5** | Why can't architecture solve this? | ClimSight is an information tool; CHART is a prescriptive decision-support tool. The gap is trust, validation, and governance -- not plumbing |

### Bottom Line (Revised)

ClimSight provides strong **engineering infrastructure** for CHART. The LangGraph workflow, RAG system, and tool-calling framework will save 2-3 months of greenfield development. This is real and valuable.

But the 70-80% reuse figure creates a false sense of proximity to a working CHART. The actual effort distribution is closer to:

| Work Category | % of Total Effort | ClimSight Contribution |
|---|---|---|
| Engineering infrastructure | 20-25% | **80% reusable** (LangGraph, RAG, tools, UI) |
| Health knowledge curation | 25-30% | **0% reusable** (entirely new domain) |
| Clinical validation & governance | 15-20% | **0% reusable** (new requirement) |
| Data partnerships & access | 15-20% | **0% reusable** (institutional, not technical) |
| Prompt engineering & tuning | 10-15% | **20% reusable** (patterns transferable, content new) |
| Testing & QA | 5-10% | **30% reusable** (test patterns, not test cases) |

**Restated:** ClimSight saves ~80% of ~25% of the total effort = **~20% of the overall CHART project.** This is meaningful but far from "70-80% done." The evaluation should be read as "here's how to efficiently build CHART's technical foundation" rather than "CHART is mostly built."

The recommendation to build CHART on ClimSight remains sound -- but the timeline (14 weeks to Phase 3), budget, and team composition (pure software engineering) need significant revision to account for health domain expertise, clinical validation, institutional partnerships, and regulatory compliance.
