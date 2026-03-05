# Building CHART on ClimSight: Revised Technical Plan

## Research Summary

Last updated: 2026-03-05

This document supersedes the initial technical evaluation (`building_on_climsight.md`) by incorporating the critical analysis from Appendix A. It provides an honest, evidence-backed implementation plan that accounts for the full scope of building CHART -- not just the software engineering portion.

---

## 1. Executive Summary (Revised)

The initial evaluation claimed ClimSight is "70-80% reusable" for CHART. After critical analysis, this is **true for engineering infrastructure but misleading for overall project scope.**

**Revised assessment:** ClimSight's engineering infrastructure (LangGraph, RAG, tools, UI) covers ~80% of the *infrastructure layer*, which constitutes ~20-25% of the total CHART project. The remaining effort -- health knowledge curation, clinical validation, data partnerships, regulatory compliance, and prompt engineering -- is 100% new and represents 75-80% of total project effort.

**What this means in practice:**
- ClimSight saves 2-3 months of greenfield engineering work
- But CHART is a 12-18 month project, not a 14-week project
- The team needs public health expertise, not just software engineers
- The build strategy (extend, don't rewrite) remains correct

### Effort Distribution

| Work Category | % of Total Effort | ClimSight Contribution | Evidence |
|---|---|---|---|
| Engineering infrastructure | 20-25% | **80% reusable** | 825 lines of domain-agnostic plumbing (LangGraph wiring, RAG infra, generic tools) directly transferable |
| Health knowledge curation | 25-30% | **0% reusable** | No health KB exists; CHAMNHA took 3+ years for validated framework ([doi:10.1093/heapol/czaf028](https://doi.org/10.1093/heapol/czaf028)) |
| Clinical validation & governance | 15-20% | **0% reusable** | New requirement; no analogue in ClimSight's informational output model |
| Data partnerships & access | 15-20% | **0% reusable** | DHIS2 MoU with Kenya MOH takes 3-6 months; CHAP tool (DHIS2's own team) still "in progress" after 2+ years |
| Prompt engineering & tuning | 10-15% | **20% reusable** | Patterns transferable (e.g., `_create_tool_prompt()` at 200 lines), but health content entirely new |
| Testing & QA | 5-10% | **30% reusable** | Test patterns reusable (pytest fixtures, mock configs), but all test cases are new |

**Revised LOC estimate:** ~3,500-4,500 new lines (production + tests + prompts), not ~1,600.

---

## 2. What ClimSight Genuinely Provides

These components are reusable as-is, verified by codebase inspection:

### A. LangGraph Workflow Engine (reuse: HIGH)

**Evidence:** The graph construction at `climsight_engine.py:1338-1393` is 57 lines of wiring. Adding a new parallel agent requires 2 lines:
```python
workflow.add_node("health_rag_agent", health_rag_agent)
# Then append to the fan-in list at line 1378
```
This is proven, not hypothetical -- `smart_agent` was added exactly this way (lines 1381-1382: conditional edge, gated by `config.get('use_smart_agent', False)`).

**What transfers:**
- `StateGraph(AgentState)` orchestration pattern
- Conditional routing (`route_fromintro`, `route_after_prepare`)
- Parallel agent fan-in (`add_edge([list], "node")`)
- Thread-based sandbox isolation

**What doesn't:** All agent implementations (prompt content, data sources, domain logic).

### B. RAG System (reuse: HIGH)

**Evidence:** The `load_rag()` function (`rag.py:56-113`) uses a `db_type` parameter that selects Chroma paths via `f'chroma_path_{db_type}_openai'` (line 75). The function has zero awareness of what's in the database. Adding a health RAG means:
1. Create a new Chroma DB with health documents
2. Add `chroma_path_health_interventions_openai` to config
3. Call `load_rag(config, api_key, db_type='health_interventions')`

**What transfers:** `load_rag()`, `query_rag()`, `is_valid_rag_db()`, embedding backend abstraction (OpenAI, AITTA).

**What doesn't:** The documents in the database, the RAG query templates, the source attribution logic.

### C. Tool Execution Framework (reuse: HIGH)

**Evidence:** These tools contain zero domain logic:

| Tool | Lines | What it does | Climate-specific code |
|---|---|---|---|
| `tools/python_repl.py` | 204 | Persistent Jupyter kernel | None |
| `tools/image_viewer.py` | 89 | GPT-4V image analysis | None |
| `tools/reflection_tools.py` | 147 | Plot quality scoring (7/10 threshold) | None |
| `tools/visualization_tools.py` | 124 | File listing, viz strategy advice | None |
| `tools/package_tools.py` | ~50 | Dynamic pip install | None |
| **Total** | **~614** | **Generic execution shells** | **Zero** |

### D. Agent State Pattern (reuse: HIGH with extension)

**Evidence:** `AgentState` (`climsight_classes.py:9-45`) has 37 fields, all with Pydantic defaults. Adding new fields doesn't break existing agents because they only read fields they know about. Proven by the progressive addition of `era5_*`, `destine_*`, and `predefined_plots` fields without touching earlier agents.

### E. Streamlit UI (reuse: MODERATE)

**Evidence:** The map interaction (`streamlit_interface.py`), session management, and analysis mode selector are domain-agnostic. The UI is loosely coupled -- it calls `create_graph()` and displays results without knowing what agents produced them.

**What transfers:** Map, session, form pattern, download handler.
**What changes:** Labels, toggles, help text, health-specific output sections.

### F. Climate Data Pipeline (reuse: AS-IS for climate context)

**Evidence:** `climate_data_providers.py` has 4 providers (1,181 lines) following an abstract base class pattern. CHART still needs climate data (that's the "C" in CHART), so these providers are used unchanged. The provider pattern is also the right model for adding health data providers.

**What transfers:** All 4 existing providers, `ClimateDataResult` dataclass, ERA5 tools.
**What's new:** Health data providers following the same pattern.

---

## 3. Architecture Decisions for CHART: What to Keep, What to Simplify

ClimSight's multi-agent architecture is overengineered for data extraction but appropriately designed for synthesis and analysis. CHART should preserve what genuinely benefits from the agent pattern and simplify what doesn't.

### Where the Agent Design Genuinely Adds Value

**1. Graceful degradation.** Each agent is independent. If the RAG database is missing, the pipeline still runs -- `ipcc_rag_agent` returns `"None"` and `combine_agent` works with what it has. If ERA5 is unavailable, everything else still works. If `smart_agent` is disabled, the graph skips that node. With a rigid data pipeline, you'd need explicit error handling for every combination of failures. With agents, it's built into the architecture.

**2. LLM wrapping is valuable for translation steps.** The `data_agent` doesn't just call `get_climate(lat, lon)`. It takes raw extracted data and uses the LLM to describe it -- turning a table of numbers into natural language that `combine_agent` can reason over. Similarly, `zero_rag_agent` takes raw geographic data (soil codes, land use classifications) and produces a human-readable environmental profile. That contextualization requires language.

**3. Parallel execution is real value.** Five data sources fetched simultaneously. LangGraph gives you parallel fan-out with a declarative graph -- equivalent to `asyncio.gather()` but with built-in state management and error isolation. Wall-clock time savings are significant.

**4. The `data_analysis_agent` is genuinely agentic.** This is the one part where the agent pattern fully earns its keep. It reads extracted data, decides what analysis is relevant to the user's question, writes Python code, runs it, examines the resulting plot, decides if it's good enough, fixes it if not, and decides what to analyze next. That's an actual reasoning loop. A fixed pipeline can't do "the user asked about heat stress for pregnant women, so I should compute WBGT and overlay preterm birth risk thresholds."

**5. Composability and extensibility.** Adding a new data source = add a node + add an edge. The rest of the graph doesn't change. Making an agent optional = one config flag. This makes it easy to experiment with different configurations without rewriting the pipeline.

**6. State management is solved.** `AgentState` as a shared Pydantic model means every agent can read what every other agent produced without manually threading data through function arguments. Add a new field, populate it in one agent, consume it in another.

**7. Deterministic routing is auditable.** Given the same config, the same agents run in the same order every time. You can log exactly what happened, in what order, with what inputs. An autonomous agent that decides its own path is harder to debug and reproduce.

**8. The `intro_agent` filter saves real cost.** If someone types an irrelevant query, the pipeline exits immediately. Without it, you'd run 5 parallel agents, fetch climate data, query RAG databases -- all for nothing.

### Where CHART Should Simplify

The data extraction agents (`data_agent`, `zero_rag_agent`) are functions dressed as agents. They always run, always call the same functions, and the LLM step is pure translation. For CHART, consider:

**Option A: Keep the pattern, extend it (recommended for MVP).** The overhead of "function wrapped in agent" is small (one LLM call per agent for translation). The graceful degradation, parallel execution, and composability benefits apply equally to CHART's health data sources. Adding `health_data_agent` and `health_rag_agent` as new parallel nodes is trivial and consistent.

**Option B: Replace data extraction with Dagster pipelines (consider for production).** If CHART grows to handle batch processing (e.g., seasonal plans for all 47 Kenyan counties), Dagster provides:
- Scheduled pipeline execution (daily/weekly data refresh)
- Asset-based lineage tracking (which data produced which output)
- Built-in retry/backfill for failed data fetches
- Materialization history (when was this data last refreshed?)

**Dagster vs. LangGraph is not either/or.** The right architecture is:
- **Dagster** for the data pipeline layer: scheduled fetching of climate data, DHIS2 health indicators, ERA5 updates, intervention KB refreshes. These are deterministic, repeatable, and benefit from scheduling/monitoring.
- **LangGraph** for the reasoning layer: user query interpretation, risk assessment, intervention matching, synthesis. These require LLM reasoning and benefit from the agent pattern.

```
Dagster (data pipeline, scheduled):
  Climate data fetch --> materialized assets
  DHIS2 indicator pull --> materialized assets
  ERA5 update --> materialized assets
  KB refresh (triggered) --> materialized assets

LangGraph (reasoning, per-query):
  intro_agent --> [parallel: health_rag, climate_rag, risk_assessment]
             --> data_analysis_agent --> combine_agent
```

This separation means the LangGraph agents don't fetch data at query time -- they read from pre-materialized Dagster assets. Faster queries, cleaner architecture, and Dagster handles the failure/retry/scheduling that LangGraph agents currently do ad-hoc.

**Recommendation:** Start with Option A (extend LangGraph as-is) for Phase 1-2 MVP. Introduce Dagster in Phase 3 when batch processing and scheduled data refresh become requirements.

### CHART Agent Inventory (Minimized)

Based on this analysis, CHART needs fewer new agents than the initial evaluation proposed:

| Agent | Pattern | Justification |
|---|---|---|
| `intro_agent` | Modify prompt | Change filter to "climate-health-related" -- same cost-saving gate |
| `climate_rag_agent` | Merge `ipcc_rag_agent` + `general_rag_agent` | One agent querying both climate RAG DBs -- they do the same thing against different collections |
| `health_rag_agent` | Clone pattern | Searches health intervention KB -- genuinely new |
| `data_agent` | Keep as-is | Climate data extraction + LLM translation -- still needed |
| `health_data_agent` | New, follows `data_agent` pattern | DHIS2/published health stats extraction |
| `data_analysis_agent` | Extend tools | Add health-specific tools (risk thresholds, WBGT) -- the genuinely agentic core |
| `combine_agent` | Modify prompt | Synthesize climate + health into seasonal plan |

**Removed vs. initial plan:**
- No separate `health_risk_agent` -- folded into `data_analysis_agent` tools (it's a computation, not a reasoning loop)
- No separate `intervention_matching_agent` -- folded into `health_rag_agent` + `data_analysis_agent` (RAG search + post-filtering)
- Merge `ipcc_rag_agent` + `general_rag_agent` into single `climate_rag_agent` (they query different DBs but follow identical logic)
- `zero_rag_agent` kept but candidate for merge with `data_agent` in Phase 3

**Net result:** 7 agents (down from 9+ in initial plan), with clearer separation between data extraction (function-like) and reasoning (genuinely agentic).

---

## 4. What Must Be Built New

### A. Health Knowledge Base (CRITICAL PATH -- 3-6 months)

This is the single most underestimated dependency. The initial evaluation allocated "2 weeks (manual curation)."

**Why 2 weeks is insufficient:**

The [JOGH 2025 scoping review](https://jogh.org/2025/jogh-15-04035) identifies 79 interventions, but they are academic descriptions, not decision-support entries. Converting them requires:

1. **Evidence grading** -- The review notes evidence quality ranges from "high" (RCTs for insecticide-treated nets) to "very low" (expert opinion for institutional cooling). An ungraded Chroma DB treats all documents as equally authoritative. A district officer asking "what should I do about heat-related preterm birth?" gets RAG results ranked by text similarity, not evidence strength.

2. **Contextual adaptation** -- The RAG system uses cosine similarity (`rag.py:140-203`). A document about "cool roofs in Dhaka slums" scores high for "heat exposure in Nairobi informal settlements" (similar text), but the building materials, climate, and implementation feasibility differ completely. Each intervention needs location-specific feasibility metadata.

3. **Domain expertise** -- The [CHAMNHA project](https://doi.org/10.1093/heapol/czaf028) required a multi-disciplinary team across 3 countries working for 3+ years to produce a validated climate-health framework for pregnant women. CHART proposes comparable scope with 2 weeks of engineering time.

4. **Maintenance** -- Health evidence evolves continuously (Lancet Countdown annual updates, WHO guideline revisions). ClimSight's IPCC RAG is relatively stable (reports every 5-7 years). A health KB needs a curation pipeline, not a one-time build.

**Revised plan:**

| Phase | Duration | Deliverable | Required expertise |
|---|---|---|---|
| Source collection | 2 weeks | Raw documents from JOGH, CHAMNHA, WHO, Americares, Kenya RMNCAH-N | Research assistant |
| Structured extraction | 4 weeks | 79 interventions with evidence grade, climate trigger, MNCH outcome, implementation requirements | Public health specialist |
| Contextual tagging | 4 weeks | Location-specific feasibility scores for Kenya counties (infrastructure, supply chain, workforce) | Local health systems expert |
| Chroma DB build + validation | 2 weeks | Indexed, queryable vector store with retrieval quality benchmarks | ML engineer + domain expert |
| Review cycle | 4 weeks | Expert panel review of top-20 interventions for clinical accuracy | Clinical advisory board |
| **Total** | **~16 weeks** | **Validated health intervention KB** | **3-4 specialists** |

### B. Clinical Validation Framework (NEW REQUIREMENT -- 2-4 months)

The initial evaluation had no validation strategy. This is the gap between "the system returns relevant documents" and "the system produces recommendations a clinical expert would endorse."

**Why this is non-negotiable:**

ClimSight outputs informational narratives (`combine_agent` returns `final_answer: str`). Users are climate-literate researchers who evaluate LLM output against domain knowledge. No one is harmed by an imprecise climate outlook.

CHART outputs prescriptive action plans for district health officers. Evidence of the stakes:
- [Chersich et al. (2020)](https://doi.org/10.1016/j.envint.2020.105567): 16% increase in preterm birth risk per 1°C above 25°C mean temperature
- [Kenya has ~1 doctor per 10,000 people](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/medical-doctors-(per-10-000-population)); officers may defer to system recommendations rather than challenging them
- [Kenya's cold chain coverage](https://www.gavi.org/programmes-impact/country-hub/africa/kenya) reaches only ~76% of facilities; recommending cold-chain-dependent interventions where infrastructure doesn't exist wastes budgets

**Required components:**

1. **Structured output schemas** -- Extend ClimSight's existing Pydantic patterns. The codebase already has `routeResponse` (line 1178 of `climsight_engine.py`) and `ClimateDataResult` (`climate_data_providers.py:33-55`). Create:
   ```python
   class HealthRiskAssessment(BaseModel):
       risk_type: str                    # e.g., "heat_preterm", "malaria_transmission"
       risk_level: Literal["low", "moderate", "high", "very_high"]
       confidence: float                 # 0-1, based on data availability
       evidence_grade: Literal["high", "moderate", "low", "very_low"]
       climate_trigger: str              # e.g., ">35C for 3+ consecutive days"
       data_sources_used: list[str]      # Provenance chain
       data_gaps: list[str]              # What's missing

   class InterventionRecommendation(BaseModel):
       intervention: str
       evidence_grade: Literal["high", "moderate", "low", "very_low"]
       source: str                       # Citation
       local_feasibility: float          # 0-1, based on infrastructure assessment
       contraindications: list[str]
       implementation_requirements: list[str]
       refuse_reason: Optional[str]      # Non-empty when evidence is insufficient
   ```

2. **"Refuse to recommend" pathway** -- When evidence is insufficient, the system must say so rather than generating a plausible-sounding recommendation. ClimSight's `intro_agent` already has a "FINISH" pathway for out-of-scope queries (lines 1120-1163). CHART needs an analogous pathway for "in-scope but insufficient evidence."

3. **Clinical review gate** -- Analogous to `reflection_tools.py`'s 7/10 plot quality threshold, but for clinical accuracy. Before recommendations reach users, a structured check verifies: (a) all recommendations cite a specific source, (b) evidence grade is "moderate" or higher for action items, (c) local feasibility score accounts for infrastructure.

4. **Benchmark dataset** -- 50-100 location + health challenge pairs with expert-validated "gold standard" responses. Used for regression testing as prompts and KB evolve.

**Effort:** 2-4 months. Requires public health expert + ML engineer collaboration.

### C. Health Data Integration (2-6 months depending on DHIS2 access)

**Phase C1: Open-Meteo Seasonal Forecasts (2-3 weeks, no dependencies)**

Straightforward API integration. Create `OpenMeteoSeasonalProvider` following `ClimateDataProvider` pattern. [Open-Meteo Seasonal Forecast API](https://open-meteo.com/en/docs/seasonal-forecast-api) is free, no auth, REST.

**Caveat:** ECMWF SEAS5 has [documented low skill for East African precipitation](https://doi.org/10.1175/JCLI-D-19-0898.1) during March-May long rains. Precipitation forecasts should carry explicit confidence warnings. The [Greater Horn of Africa Climate Outlook Forum (GHACOF)](https://www.icpac.net/seasonal-forecast/) produces superior regional consensus forecasts but requires institutional relationships with [ICPAC](https://www.icpac.net/).

**Phase C2: Derived Health Indicators (1-2 weeks, depends on C1)**

Computed from existing climate data via Python REPL tool (no new infrastructure):
- Consecutive days >35°C (preterm birth risk threshold per [Chersich 2020](https://doi.org/10.1016/j.envint.2020.105567))
- Wet-bulb globe temperature (heat stress for pregnant women)
- Standardized Precipitation Index (drought / food security)
- Malaria transmission suitability index (temperature + precipitation + humidity)

**Phase C3: DHIS2 Integration (3-6 months, institutional dependency)**

**Why 4 weeks is unrealistic:**

| Challenge | Detail | Evidence |
|---|---|---|
| Institutional access | Kenya KHIS requires MoU with Division of Health Informatics | [HISP East Africa](https://www.hispeastafrica.org/) process: 3-6 months |
| Metadata complexity | 47 counties, 290 sub-counties, ~5,000 facilities, 13 metadata dimensions | [DHIS2 API docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-241/metadata.html) |
| Data quality | Missing values, delayed reporting, duplicate entries in real DHIS2 instances | Standard challenge acknowledged by [HISP documentation](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-241/collecting-data/data-quality.html) |
| Comparable project | CHAP tool (DHIS2's own team at University of Oslo) -- DHIS2 integration still "in progress" after 2+ years | [github.com/dhis2-chap/chap-core](https://github.com/dhis2-chap/chap-core) |

**Revised plan:**
1. **Month 1-2:** Begin MoU process with Kenya MOH (parallel to other development)
2. **Month 2-3:** Develop DHIS2 read tool against demo instance (`play.dhis2.org`)
3. **Month 3-4:** Test against Kenya sandbox (if access granted)
4. **Month 4-6:** Production integration, error handling, data quality filters

**Fallback (if DHIS2 access is delayed):** Build CHART MVP without DHIS2 using:
- Open-Meteo climate data (immediate, free)
- Published district-level health statistics (Kenya DHS, India NFHS)
- Curated intervention KB
- This delivers a useful tool while DHIS2 negotiations proceed

### D. Health-Specific Agents and Prompts (~4-6 weeks engineering, ongoing tuning)

**New agents to create:**

| Agent | Pattern | New Lines | Complexity |
|---|---|---|---|
| `health_rag_agent` | Clone `ipcc_rag_agent` (20 lines at `climsight_engine.py:1062-1081`) | ~50 | Low -- same `query_rag()` call with different DB |
| `health_data_agent` | Follow `data_agent` pattern (lines 854-916) | ~200 | Medium -- must integrate DHIS2/published stats |
| `health_risk_agent` | New (after `prepare_predefined_data`) | ~300 | High -- climate-to-health risk mapping with validated thresholds |
| `intervention_matching_agent` | New (after `health_risk_agent`) | ~250 | High -- RAG search filtered by risk profile + local capacity |

**Prompt engineering:**

The initial evaluation allocated "3 days" for the health system prompt. Evidence of why this is insufficient:
- ClimSight's `intro_agent` prompt (lines 1112-1165): 53 lines of carefully crafted exclusion logic
- ClimSight's `_create_tool_prompt()` (lines 476-676 of `data_analysis_agent.py`): **200 lines** of structured prompt building
- ClimSight's `combine_agent` system role: domain-specific synthesis instructions

Health prompts will be equally complex and require clinical expert review. **Revised estimate: 3-4 weeks of iterative prompt development with domain expert feedback.**

### E. Regulatory and Compliance (ongoing, 2-4 months initial)

**Not mentioned in initial evaluation. Non-negotiable for health domain.**

| Requirement | Kenya | India | Evidence |
|---|---|---|---|
| Data protection | [Data Protection Act 2019](http://kenyalaw.org/kl/fileadmin/pdfdownloads/Acts/2019/TheDataProtectionAct__No24of2019.pdf) | [Digital Personal Data Protection Act 2023](https://www.meity.gov.in/writereaddata/files/Digital%20Personal%20Data%20Protection%20Act%202023.pdf) | Health data = "sensitive personal data" in both |
| Cross-border transfer | Restricted | Restricted | Using OpenAI API sends queries to US servers |
| Medical device classification | [Pharmacy and Poisons Board](https://pharmacyboardkenya.org/) may apply | [CDSCO](https://cdsco.gov.in/) SaMD guidelines | Clinical decision support tools may qualify |
| Ethics review | [NACOSTI](https://nacosti.go.ke/) research permit required | [ICMR ethical guidelines](https://main.icmr.nic.in/content/ethical-guidelines) | If system generates clinical recommendations |

**Mitigation options:**
- Use on-premise LLM deployment (local models via AITTA -- already supported in ClimSight config) to avoid cross-border data transfer
- Frame CHART as "information synthesis" not "clinical recommendation" to avoid medical device classification
- Obtain NACOSTI research permit for pilot phase
- Partner with local institution (e.g., KEMRI in Kenya) for ethics coverage

---

## 5. Revised Implementation Roadmap

```
Phase 1: Foundation (Month 1-3)
  PARALLEL TRACK A -- Engineering (7 agents, not 9+):
    - Merge ipcc_rag_agent + general_rag_agent into climate_rag_agent
    - Health intervention Chroma DB (initial, unvalidated)
    - health_rag_agent (clone climate_rag_agent pattern, different DB)
    - health_data_agent (DHIS2 demo / published stats)
    - Open-Meteo seasonal forecast tool
    - Derived health indicators as data_analysis_agent tools (WBGT, SPI, heat days)
    - Modified intro_agent + combine_agent prompts
    - Config extensions + CHART mode toggle
    - AgentState extensions (10 new fields)
    Result: 7-agent graph returning climate + health information for any location

  PARALLEL TRACK B -- Domain:
    - Begin DHIS2 MoU process with Kenya MOH
    - Recruit public health specialist for KB curation
    - Begin structured intervention extraction (79 from JOGH + CHAMNHA)
    - Identify 3 pilot counties and county health team contacts
    - Begin NACOSTI research permit application
    Result: Institutional groundwork for Phases 2-3

Phase 2: Health Intelligence (Month 3-6)
  - Validated intervention KB (expert panel review of top-20 interventions)
  - Risk thresholds as data_analysis_agent tools (not separate agent)
  - Intervention matching via health_rag_agent + data_analysis_agent post-filtering
  - Structured output schemas (HealthRiskAssessment, InterventionRecommendation)
  - "Refuse to recommend" pathway for insufficient evidence
  - Health-specific predefined plots
  - DHIS2 tool development against demo instance
  - Benchmark dataset: 50 location+challenge pairs with expert "gold standard"
  Result: System generates risk assessments + matched interventions with evidence grades

Phase 3: Integration + Validation (Month 6-10)
  - DHIS2 production integration (if MoU granted)
  - Clinical review gate (structured validation before output)
  - Introduce Dagster for scheduled data pipelines:
      * Climate data refresh (ERA5, Open-Meteo)
      * DHIS2 health indicator pulls
      * KB update pipeline
      * LangGraph agents read from materialized Dagster assets
  - Pilot deployment in 3 Kenyan counties with county health teams
  - User feedback collection and prompt tuning
  - KB expansion based on field validation
  - Regulatory compliance verification
  - Consider merging zero_rag_agent into data_agent (simplification)
  Result: Field-tested system with validated outputs + scheduled data pipelines

Phase 4: Production + Scale (Month 10-18)
  - DHIS2 write-back (seasonal plans into DHIS2)
  - National met service integration (KMD seasonal outlooks)
  - Dagster-orchestrated batch processing for all 47 Kenyan counties
  - India expansion (NFHS data, IMD forecasts)
  - Monitoring indicator framework
  - Ongoing KB maintenance pipeline
  Result: Production system serving multiple counties/districts
```

---

## 6. Team Composition (Revised)

The initial evaluation implicitly assumed a software engineering team. CHART requires:

| Role | Why | Phase needed |
|---|---|---|
| ML/LLM engineer (1) | LangGraph extension, RAG, tool development, prompt engineering | 1-4 |
| Backend engineer (1) | DHIS2 integration, API development, data pipeline | 2-4 |
| Public health specialist (1) | KB curation, evidence grading, clinical validation, intervention contextualization | 1-3 |
| Local health systems expert (0.5) | County-level feasibility assessment, MOH relationship, user research | 1-3 |
| Clinical advisor (0.25) | Review panel for intervention recommendations, benchmark validation | 2-3 |
| Regulatory/legal advisor (0.1) | Data protection compliance, medical device classification assessment | 2-3 |

**Minimum team:** 2 engineers + 1 public health specialist. The initial evaluation's implicit assumption of "just engineers" is the single largest risk to project success.

---

## 7. Risk Register (Revised)

| # | Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| R1 | Health KB too thin -- recommendations generic | HIGH | HIGH | Start with heat x pregnancy (strongest evidence); expand iteratively; set minimum evidence grade for recommendations | Public health specialist |
| R2 | DHIS2 access blocked by institutional process | HIGH | MEDIUM | Build MVP without DHIS2 using published statistics; DHIS2 is enhancement, not prerequisite | Backend engineer |
| R3 | LLM hallucination on health interventions | MEDIUM | VERY HIGH | Structured output schemas (Pydantic), "refuse to recommend" pathway, clinical review gate, RAG-only with citations | ML engineer + clinical advisor |
| R4 | No user research -- building wrong tool | MEDIUM | HIGH | Conduct 5-10 interviews with county health officers before Phase 2; adjust UI and workflow based on findings | Local health systems expert |
| R5 | Regulatory classification as medical device | LOW | VERY HIGH | Frame as "information synthesis" not "clinical recommendation"; obtain legal opinion early; consider NACOSTI research permit route | Legal advisor |
| R6 | SEAS5 forecast skill too low for East Africa precipitation | MEDIUM | MEDIUM | Display confidence intervals; supplement with GHACOF consensus forecasts (institutional relationship needed); flag precipitation forecasts explicitly | ML engineer |
| R7 | ClimSight upstream divergence breaks CHART branch | MEDIUM | MEDIUM | Propose plugin architecture to ClimSight maintainers; contribute health extensions upstream if possible; minimize modifications to existing files | ML engineer |
| R8 | Cross-border data transfer violates data protection laws | MEDIUM | HIGH | Deploy on-premise LLM (AITTA already supported in ClimSight config); or use local models for health queries while keeping OpenAI for climate-only | Backend engineer + legal |
| R9 | Kenya pilot counties decline participation | MEDIUM | HIGH | Identify 5 candidate counties (not 3); partner with HISP East Africa for introductions; align with existing RMNCAH-N rollout schedule | Local health systems expert |
| R10 | Scope creep from "climate-health tool" to "general health planning" | HIGH | MEDIUM | Define MVP scope: heat x pregnancy in 3 Kenyan counties, period. No malaria, no cholera, no India until validated | Project lead |

---

## 8. What NOT to Build (Scope Boundaries)

Based on the critical analysis, these are explicitly out of scope for MVP:

1. **General health planning** -- CHART MVP covers heat x maternal health only. Malaria, cholera, dengue are Phase 4+.
2. **Real-time alerting** -- CHART is a seasonal planning tool, not an early warning system.
3. **DHIS2 write-back** -- Read-only in MVP. Writing plans back requires deeper institutional trust.
4. **India deployment** -- Kenya first. India expansion only after Kenya validation.
5. **Custom LLM fine-tuning** -- Use prompt engineering + RAG, not fine-tuned models.
6. **Mobile app** -- Streamlit web UI only. Mobile adds deployment complexity without validating the core value proposition.

---

## 9. Revised LOC Estimate

| Component | New Lines | Modified Lines | Files | Notes |
|---|---|---|---|---|
| `AgentState` extensions | 15 | 0 | 1 | 10 new fields with defaults |
| Health RAG agent | 50 | 10 | 2 | Clone ipcc_rag_agent + config |
| `health_risk_tool.py` | 300 | 0 | 1 new | Climate-to-health risk mapping with structured output |
| `intervention_tool.py` | 250 | 0 | 1 new | RAG search + feasibility filtering |
| `openmeteo_seasonal_tool.py` | 200 | 0 | 1 new | REST API integration |
| `dhis2_tool.py` | 400 | 0 | 1 new | Complex metadata, auth, error handling (revised up from 300) |
| `health_plots.py` | 350 | 0 | 1 new | Risk timeline, intervention matrix, seasonal plan |
| Health system prompts | 200 | 0 | config | intro_agent filter + combine_agent synthesis + tool prompts |
| Pydantic output schemas | 150 | 0 | 1 new | HealthRiskAssessment, InterventionRecommendation, SeasonalPlan |
| Clinical review gate | 100 | 0 | 1 new | Structured validation before output |
| Workflow wiring | 40 | 20 | engine | New agents + routing |
| UI extensions | 120 | 30 | streamlit_interface | CHART mode, health toggles, output sections |
| Config extensions | 80 | 0 | config | Health RAG, DHIS2, thresholds, prompts |
| **Production subtotal** | **~2,255** | **~60** | **8 new + 4 modified** | |
| Test code | ~1,200 | 0 | 6-8 new | Target 50%+ coverage of new code |
| Benchmark dataset | ~500 | 0 | 1 | 50 expert-validated test cases (JSON) |
| **Grand total** | **~3,955** | **~60** | **14-16 new + 4 modified** | |

**vs. initial estimate:** ~3,955 lines (revised) vs. ~1,595 lines (initial). The 2.5x increase comes from: test code (not estimated initially), structured output schemas (not proposed initially), clinical review gate (not proposed initially), expanded DHIS2 error handling, expanded prompt engineering, and benchmark dataset.

---

## 10. Success Criteria

**Phase 1 (Month 3):**
- System generates health-relevant RAG responses for any location in Kenya
- Open-Meteo seasonal forecast integrated and displaying with confidence warnings
- CHART mode toggle works in Streamlit UI without breaking existing ClimSight functionality

**Phase 2 (Month 6):**
- Risk assessments for heat x preterm birth validated against CHAMNHA framework thresholds
- Top-20 interventions reviewed and approved by clinical advisor
- Benchmark dataset: system matches expert recommendations in >60% of test cases
- "Refuse to recommend" fires correctly when evidence grade is "very low"

**Phase 3 (Month 10):**
- 3 Kenyan county health teams have used CHART for at least one seasonal planning cycle
- User satisfaction score >3/5 from county health officers
- Zero instances of clinically inappropriate recommendations in field use
- DHIS2 read integration working against production KHIS instance (or fallback to published data)

---

## 11. Relationship to Initial Evaluation

The initial evaluation (`building_on_climsight.md`) remains valuable as a **component-level technical reference**. Its line-by-line codebase analysis is accurate and useful for developers. This revised document adds:

1. **Honest effort distribution** -- The 70-80% reuse figure is reframed as "80% of 25%" = ~20% of total effort
2. **Non-engineering work streams** -- KB curation, clinical validation, institutional partnerships, regulatory compliance
3. **Team composition** -- Public health specialist is mandatory, not optional
4. **Scope boundaries** -- Explicit "what NOT to build" to prevent scope creep
5. **Risk register** -- 10 risks with owners and mitigations
6. **Realistic timeline** -- 12-18 months, not 14 weeks

The recommendation to build on ClimSight rather than from scratch remains correct. The architecture is sound, the infrastructure is genuinely reusable, and the "extend, don't rewrite" strategy preserves optionality. What changes is the recognition that engineering infrastructure is the easy part -- the hard part is everything else.
