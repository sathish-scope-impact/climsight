# CHART EventStorming Workshop Simulator

*A simulated Big Picture + Process Level EventStorming for the Climate x Health Adaptation and Resilience Tool*

*Facilitator guidance: This document simulates what a real EventStorming workshop with county health officers, climate scientists, and engineers would produce. Use it to validate assumptions before running the actual workshop. Every sticky note below came from evidence in the positioning analysis -- not invented.*

---

## Workshop Setup

### Participants (simulated voices)

| Role | Represents | Key concern |
|---|---|---|
| **Dr. Amina** | County Health Director, Kilifi County | "I need to defend my budget to the Governor" |
| **Joseph** | Sub-county Disease Surveillance Officer | "I see the cases first but can't move resources" |
| **Dr. Wanjiku** | MOH Division of Environmental Health | "We need to align with NCCAP reporting" |
| **Peter** | Kenya Meteorological Department forecaster | "My seasonal outlook goes out but nobody acts on it" |
| **Sarah** | CHW (Community Health Worker) supervisor | "We know which bridges flood but nobody asks us" |
| **Raj** | DHIS2 technical officer | "The data is there but in 47 different formats" |
| **Engineer** | ClimSight/CHART developer | "What exactly do you need the system to do?" |

### Materials

- Orange stickies: **Domain Events** (things that happen, past tense)
- Blue stickies: **Commands** (decisions/actions that trigger events)
- Yellow stickies: **Actors** (people who issue commands)
- Purple stickies: **Policies** (automated rules, "whenever X happens, do Y")
- Pink stickies: **Hotspots** (disagreements, pain points, open questions)
- Green stickies: **External Systems** (DHIS2, KMD, Open-Meteo, etc.)
- Large red stickies: **Pivotal Events** (moments that change everything)

---

## Phase 1: Big Picture (Chaotic Exploration)

*Instructions: Everyone writes domain events on orange stickies. No ordering yet. Just dump everything that happens in climate-sensitive health planning.*

### The Wall After 20 Minutes (unordered)

```
+------------------+  +------------------+  +------------------+
| KMD seasonal     |  | Cholera outbreak  |  | AWP budget       |
| outlook issued   |  | reported          |  | submitted to     |
|                  |  |                   |  | county assembly   |
+------------------+  +------------------+  +------------------+

+------------------+  +------------------+  +------------------+
| IDSR weekly      |  | Drug supply       |  | CHW reports      |
| bulletin         |  | order placed      |  | flooding in      |
| compiled         |  |                   |  | sub-county       |
+------------------+  +------------------+  +------------------+

+------------------+  +------------------+  +------------------+
| Heat wave        |  | Emergency         |  | Seasonal rains   |
| kills 3 elderly  |  | request sent to   |  | begin earlier    |
| in Kilifi        |  | national MOH      |  | than expected    |
+------------------+  +------------------+  +------------------+

+------------------+  +------------------+  +------------------+
| Governor asks    |  | Pregnant women    |  | County health    |
| "why weren't we  |  | admitted with     |  | team quarterly   |
| prepared?"       |  | heat exhaustion   |  | review meeting   |
+------------------+  +------------------+  +------------------+

+------------------+  +------------------+  +------------------+
| KEMSA delivery   |  | Budget re-        |  | DHIS2 monthly    |
| arrives 6 weeks  |  | allocation        |  | report submitted |
| late             |  | request denied    |  |                  |
+------------------+  +------------------+  +------------------+

+------------------+  +------------------+  +------------------+
| Staff reassigned |  | Last year's AWP   |  | Training on heat |
| from outreach to |  | copy-pasted for   |  | stroke protocol  |
| emergency ward   |  | this year         |  | never happened   |
+------------------+  +------------------+  +------------------+
```

### Hotspots Discovered (pink stickies placed during chaotic phase)

```
!!! HOTSPOT: Peter (KMD) says "I send the outlook every March and September"
    Dr. Amina says "I've never seen it"
    Joseph says "I get it on WhatsApp but don't know what to do with it"
    --> TRANSLATION GAP: climate info exists but doesn't reach decision-makers
        in actionable form

!!! HOTSPOT: Joseph says "I report cases to DHIS2 weekly"
    Raj says "But the county team only looks at DHIS2 quarterly"
    Dr. Amina says "I look at it when preparing AWP, once a year"
    --> FREQUENCY MISMATCH: surveillance is weekly, planning is annual

!!! HOTSPOT: Sarah (CHW supervisor) says "We told the county the bridge
    would flood again. Nobody recorded it anywhere."
    --> LOCAL KNOWLEDGE LOSS: qualitative field intelligence has no system

!!! HOTSPOT: Dr. Amina says "I can't move budget without Governor approval"
    Dr. Wanjiku says "But counties have health autonomy since 2010"
    Dr. Amina says "On paper. Try telling the Governor you want to
    reallocate his flagship program's money."
    --> INSTITUTIONAL INERTIA: legal authority != practical authority
        (This is the #1 risk from positioning analysis, Question 20)

!!! HOTSPOT: Joseph says "KEMSA takes 6-8 weeks to deliver"
    Dr. Amina says "So by the time I order during an outbreak, it's over"
    --> LEAD TIME CONSTRAINT: supply chain needs 6-8 week advance notice
        (This validates the 4-6 week forecast horizon from Question 4)
```

---

## Phase 2: Timeline Ordering

*Instructions: Now arrange events left-to-right in chronological order. Find the narrative.*

### The Enforced Timeline

```
TIME -->

PLANNING CYCLE (annual, starting ~June):
=========================================

[Last year's]    [AWP budget]     [County        [AWP           [Budget
 AWP copy-   -->  drafted by  -->  assembly   -->  approved  -->  disbursed
 pasted]          health team]     review]                        to depts]

     |                                                               |
     v                                                               v
  "We use last                                              "Money is locked
   year's numbers                                            for 12 months"
   because we have
   nothing better"


CLIMATE CYCLE (seasonal, ~March and ~October):
==============================================

[KMD seasonal]   [Outlook     [Seasonal     [Climate        [Climate
 outlook     -->  forwarded -->  rains    -->  event      -->  event
 issued]          via WhatsApp]  begin]       (flood/heat)]   peaks]

     |                              |               |              |
     v                              v               v              v
  "Nobody                      "Earlier than    "Cases start    "Emergency
   translates                    expected"       showing up      mode"
   this for us"                                  in DHIS2"


RESPONSE CYCLE (reactive, days-weeks):
======================================

[Cases spike   [IDSR         [County health   [Emergency     [KEMSA
 in DHIS2] -->  bulletin  -->  team       -->   request   -->  delivery
                compiled]      emergency        to national    arrives
                               meeting]         MOH]           6 wks later]

     |              |               |                              |
     v              v               v                              v
  "Already       "Compiled on    "Staff pulled     ......    "Outbreak
   too late"      Friday,         from outreach                is over"
                  read Monday"    to emergency"
```

### **PIVOTAL EVENT** Identified (large red sticky)

```
  +================================================+
  |                                                  |
  |   >>> THE GAP <<<                                |
  |                                                  |
  |   Between "KMD outlook issued" and              |
  |   "AWP budget drafted" there is NOTHING.        |
  |                                                  |
  |   No process, no tool, no person translates     |
  |   the seasonal forecast into a budget action.   |
  |                                                  |
  |   THIS IS WHERE CHART LIVES.                    |
  |                                                  |
  +================================================+
```

---

## Phase 3: Process Level (Commands, Actors, Policies)

*Instructions: For the gap identified above, model the TO-BE process -- what CHART enables.*

### Process: Seasonal Adaptation Planning (the new artifact)

```
ACTOR            COMMAND                EVENT                     POLICY/SYSTEM
-----            -------                -----                     -------------

[Peter/KMD]      Issue seasonal    -->  Seasonal outlook    -->   [Open-Meteo]
                 outlook                received                  [KMD API]


                                             |
                                             v

[CHART]          Fetch climate    -->  Climate forecast     -->   [POLICY: Auto-trigger
                 forecast data         retrieved for              when new seasonal
                                       county                    outlook available]

[CHART]          Fetch health     -->  Health baseline      -->   [DHIS2]
                 baseline              retrieved                  [Published stats]

[CHART]          Fetch local      -->  Environmental        -->   [ClimSight existing
                 context               profile built              geo/env agents]

                                             |
                                             v

[CHART]          Translate        -->  Risk assessment      -->   [POLICY: Use CHAMNHA
                 climate signal        generated                  thresholds. If
                 to health risk                                   confidence < 60%,
                                                                  flag as uncertain]

[CHART]          Match risks      -->  Interventions        -->   [POLICY: Filter by
                 to interventions      matched with               local feasibility.
                                       evidence grades            If cold-chain needed
                                                                  and facility has none,
                                                                  exclude intervention]

[CHART]          Generate draft   -->  Seasonal adaptation  -->   [POLICY: Format must
                 adaptation plan       plan generated             match AWP line items.
                                                                  Include cost estimates.
                                                                  Include uncertainty
                                                                  warnings.]

                                             |
                                             v

[Dr. Amina]      Review draft     -->  Plan reviewed        -->   [POLICY: TWG must
                 with TWG              by TWG                     have quorum of 3+
                                                                  to approve]

[Dr. Amina]      Accept / Modify  -->  Plan approved        -->   [POLICY: Human-in-
                 / Reject plan                                    the-loop. CHART
                                                                  never auto-submits]

[Dr. Amina]      Insert into      -->  AWP amendment        -->   [County budget
                 AWP budget            submitted                  system]

                                             |
                                             v

[Joseph]         Pre-position     -->  Supplies ordered     -->   [KEMSA]
                 supplies based        6 weeks before
                 on plan               predicted event

[Sarah/CHWs]     Adjust community -->  Outreach schedule    -->   [CHW coordination
                 outreach              updated                    WhatsApp group]
                 schedule
```

### Read Models (what each actor needs to see)

```
DR. AMINA needs:                    JOSEPH needs:
+---------------------------+       +---------------------------+
| SEASONAL ADAPTATION PLAN  |       | SUPPLY PRE-POSITIONING    |
|                           |       |                           |
| County: Kilifi            |       | Facility: Kilifi County   |
| Period: Apr-Jun 2026      |       |           Hospital        |
|                           |       |                           |
| Risk 1: Heat x preterm    |       | Item        | Qty  | By  |
|   Confidence: HIGH (82%)  |       | IV fluids   | 200  | Mar |
|   Evidence: CHAMNHA       |       | ORS packets | 500  | Mar |
|   Action: Pre-position    |       | Cholera kit | 50   | Mar |
|     IV fluids at 3 facs   |       +---------------------------+
|   Cost: KES 450,000       |
|   AWP line: 4.2.1         |       PETER (KMD) needs:
|                           |       +---------------------------+
| Risk 2: Flood x cholera   |       | FEEDBACK LOOP             |
|   Confidence: MED (61%)   |       |                           |
|   Evidence: WHO guideline  |       | My outlook for Kilifi was |
|   Action: Cholera kit     |       | used by 3 counties.       |
|     pre-positioning       |       | Outcome: supplies pre-    |
|   Cost: KES 200,000       |       | positioned, 40% fewer     |
|   AWP line: 4.3.2         |       | emergency requests.       |
|                           |       |                           |
| TOTAL BUDGET SHIFT:       |       | (This closes the feedback |
|   KES 650,000 from        |       |  loop that makes Peter    |
|   general -> climate-     |       |  care about making his    |
|   specific                |       |  outlooks actionable)     |
+---------------------------+       +---------------------------+

SARAH (CHW supervisor) needs:       DR. WANJIKU (MOH) needs:
+---------------------------+       +---------------------------+
| COMMUNITY ALERT           |       | NCCAP ALIGNMENT REPORT    |
|                           |       |                           |
| Period: Apr-Jun 2026      |       | Counties using CHART: 3   |
| Your area: Malindi sub-co |       | Adaptation plans filed: 7 |
|                           |       | Budget shifted: KES 2.1M  |
| Key messages for mothers: |       | Aligned NCCAP goals:      |
| - Stay hydrated           |       |   Goal 4.2, 4.3, 5.1     |
| - Attend clinic if temp   |       |                           |
|   >38C during pregnancy   |       | (This is what Dr. Wanjiku |
| - Boil water if flooding  |       |  reports to national MOH  |
|   reported upstream       |       |  and international donors)|
+---------------------------+       +---------------------------+
```

---

## Phase 4: Design Level (Bounded Contexts + Aggregates)

*Instructions: From the process model, identify where the boundaries are.*

### Bounded Contexts That Emerge

```
+------------------------------------------------------------------+
|                                                                    |
|  CONTEXT 1: CLIMATE INTELLIGENCE                                   |
|  (Existing ClimSight -- reuse as-is)                               |
|                                                                    |
|  Aggregates:                                                       |
|  - ClimateForcast (seasonal projection for location)              |
|  - EnvironmentalProfile (soil, elevation, land use, hazards)       |
|  - ERA5Climatology (historical baseline)                           |
|                                                                    |
|  Language: "temperature anomaly", "precipitation percentile",      |
|            "return period", "SSP scenario"                         |
|                                                                    |
+------------------------------------------------------------------+
          |
          | publishes: ClimateRiskSignal
          v
+------------------------------------------------------------------+
|                                                                    |
|  CONTEXT 2: HEALTH RISK TRANSLATION  <<< THE NEW CORE >>>         |
|                                                                    |
|  Aggregates:                                                       |
|  - HealthRiskAssessment                                            |
|      - climate_signal (from Context 1)                             |
|      - health_outcome (e.g., "preterm birth", "cholera")           |
|      - population_at_risk (from DHIS2 / published stats)          |
|      - confidence_score (0-100)                                    |
|      - evidence_source (CHAMNHA, WHO, peer-reviewed)               |
|      - threshold_basis (e.g., ">25C mean = 16% PTB increase")     |
|                                                                    |
|  - InterventionMatch                                               |
|      - matched_interventions[] (from Action Repository)            |
|      - feasibility_filter (cold chain? staff available? budget?)   |
|      - evidence_grade (A/B/C)                                      |
|      - estimated_cost_KES                                          |
|                                                                    |
|  Language: "relative risk", "WBGT", "evidence grade",              |
|            "intervention feasibility", "NNT"                       |
|                                                                    |
+------------------------------------------------------------------+
          |
          | publishes: RankedInterventionList
          v
+------------------------------------------------------------------+
|                                                                    |
|  CONTEXT 3: ADAPTATION PLANNING                                    |
|                                                                    |
|  Aggregates:                                                       |
|  - SeasonalAdaptationPlan                                          |
|      - county, period, planning_cycle                              |
|      - risk_assessments[] (from Context 2)                         |
|      - recommended_actions[] with AWP line item mapping            |
|      - total_budget_shift                                          |
|      - uncertainty_warnings[]                                      |
|      - twg_approval_status (draft | reviewed | approved | rejected)|
|                                                                    |
|  - SupplyPrePositioning                                            |
|      - facility, items[], quantities, deadline                     |
|      - lead_time_check (KEMSA 6-8 weeks factored in)              |
|                                                                    |
|  Language: "AWP line item", "budget shift", "pre-position",        |
|            "quarterly allocation", "Governor approval"             |
|                                                                    |
+------------------------------------------------------------------+
          |
          | publishes: ApprovedPlan
          v
+------------------------------------------------------------------+
|                                                                    |
|  CONTEXT 4: HEALTH DATA (external, anti-corruption layer)          |
|                                                                    |
|  Aggregates:                                                       |
|  - DHIS2HealthBaseline                                             |
|      - indicator_values[] (ANC visits, malaria cases, etc.)        |
|      - reporting_period, completeness_score                        |
|      - facility_metadata (cold chain?, staffing level?)            |
|                                                                    |
|  - PublishedHealthStats                                            |
|      - source (DHS, KNBS, WHO)                                     |
|      - indicator, value, year, admin_level                         |
|                                                                    |
|  Language: "data element", "organisation unit", "reporting rate",  |
|            "completeness"                                          |
|                                                                    |
|  NOTE: This context translates DHIS2's internal language into      |
|  CHART's domain language. DHIS2 says "data element UID abc123".    |
|  CHART says "malaria cases in Kilifi, March 2026".                 |
|                                                                    |
+------------------------------------------------------------------+
```

### Context Map (relationships)

```
Climate Intelligence ---[published language: ClimateRiskSignal]---> Health Risk Translation

Health Data ---[anti-corruption layer]---> Health Risk Translation
  (DHIS2 is messy, inconsistent, 47 different county configs.
   The ACL normalizes this before it touches the core domain.)

Health Risk Translation ---[published language: RankedInterventionList]---> Adaptation Planning

Action Repository ---[shared kernel]---> Health Risk Translation
  (Both contexts need to agree on what an "intervention" is.
   The Pydantic schema is the shared kernel.)
```

---

## Phase 5: What the Workshop Revealed

### Discovery 1: CHART is three products, not one

| Product | User | Artifact | Frequency |
|---|---|---|---|
| **Seasonal Adaptation Plan** | County Health Director | AWP amendment with budget lines | 2x/year (aligned to rainy seasons) |
| **Supply Pre-positioning Alert** | Disease Surveillance Officer | Facility-level supply order list | 4-6 weeks before predicted event |
| **Community Health Brief** | CHW Supervisor | Plain-language key messages | Monthly during risk season |

**Implication:** Phase 1 builds the Seasonal Adaptation Plan only. The other two are downstream derivatives that can be generated from the same data in Phase 2-3.

### Discovery 2: The feedback loop is the adoption mechanism

Peter (KMD) sends outlooks that nobody uses. If CHART shows him that his outlook led to 3 counties pre-positioning supplies and reducing emergency requests by 40%, he becomes an evangelist. **The reporting/feedback feature is not a nice-to-have -- it's the adoption flywheel.**

### Discovery 3: KEMSA lead time is a hard constraint

The 6-8 week KEMSA delivery timeline means CHART must produce recommendations at least 8 weeks before a predicted climate event. Combined with the 4-6 week forecast confidence window, this means:

```
Usable planning window:

|-- Forecast issued --|-- 4-6 weeks confidence --|
                      |-- KEMSA needs 6-8 weeks --|

Overlap: CHART must trigger at forecast issuance,
not wait for confidence to improve.
Result: recommendations will always carry uncertainty.
The TWG review step handles this -- not the algorithm.
```

### Discovery 4: The real data problem is DHIS2 inconsistency, not absence

Raj's sticky notes reveal: DHIS2 has the data, but Kilifi County uses different indicator codes than Mombasa County. The DHIS2 tool needs a metadata normalization layer, not just an API client. This is why the LOC estimate for `dhis2_tool.py` was revised up to 400 lines.

### Discovery 5: Sarah's local knowledge is the LLM's unique input

"The bridge to Clinic B floods every March" is not in any database. It's in Sarah's head. CHART's `data_analysis_agent` is the only component that can synthesize this kind of qualitative input with quantitative forecasts. **This is the specific capability that justifies the LLM over a spreadsheet** (Question 10).

Future feature: a simple form where CHWs can submit local knowledge ("road X impassable when river rises") that gets stored and fed into the context for their sub-county.

### Discovery 6: Governor politics is the real bottleneck

Dr. Amina's hotspot -- "try telling the Governor you want to reallocate his flagship program's money" -- reveals that CHART's output must be politically navigable. This means:

- Frame as "addition" not "reallocation" where possible
- Reference the Governor's own climate pledges (NCCAP alignment)
- Show cost of inaction ("last year's emergency response cost KES X; pre-positioning costs KES X/3")
- The `combine_agent` prompt must produce politically savvy framing, not just clinical recommendations

---

## Phase 6: Mapping to CHART Architecture

### EventStorming artifacts --> Code artifacts

| EventStorming Artifact | CHART Implementation |
|---|---|
| **Bounded Context 1:** Climate Intelligence | Existing ClimSight agents (data_agent, climate_rag_agent, ERA5 tools) |
| **Bounded Context 2:** Health Risk Translation | `data_analysis_agent` tools: `health_risk_tool.py`, `intervention_tool.py` |
| **Bounded Context 3:** Adaptation Planning | `combine_agent` with AWP-formatted output schemas |
| **Bounded Context 4:** Health Data | `dhis2_tool.py` with anti-corruption normalization layer |
| **Aggregate:** HealthRiskAssessment | Pydantic schema in `health_schemas.py` |
| **Aggregate:** SeasonalAdaptationPlan | Pydantic schema in `health_schemas.py` |
| **Aggregate:** SupplyPrePositioning | Pydantic schema (Phase 2) |
| **Policy:** CHAMNHA thresholds | Config-driven thresholds in `health_risk_tool.py` |
| **Policy:** Feasibility filter | `intervention_tool.py` post-filter |
| **Policy:** Human-in-the-loop | Clinical review gate + TWG approval status field |
| **Policy:** KEMSA lead time | 8-week minimum in seasonal planning logic |
| **Read Model:** Dr. Amina's plan | `combine_agent` output format |
| **Read Model:** Joseph's supply list | `health_plots.py` supply pre-positioning view |
| **Read Model:** Sarah's community brief | Phase 2 derivative output |
| **Read Model:** Peter's feedback loop | Phase 3 reporting feature |
| **Hotspot:** Translation gap | **This is CHART's entire value proposition** |
| **Hotspot:** DHIS2 inconsistency | Anti-corruption layer in `dhis2_tool.py` |
| **Hotspot:** Governor politics | `combine_agent` prompt: political framing |
| **Hotspot:** Local knowledge loss | Future: CHW input form --> context injection |

### Revised agent responsibilities (informed by EventStorming)

```
intro_agent
  Was: "Is this climate-related?"
  Now: "Is this climate-health planning related?"
  New filter: reject diagnostic queries ("what drug should I prescribe?")
              accept planning queries ("how should I prepare for heat season?")

climate_rag_agent (merged)
  Context 1: Climate Intelligence
  Queries both IPCC and general climate RAG DBs

health_rag_agent (new)
  Context 2: Health Risk Translation (knowledge retrieval)
  Queries Action Repository (110+ interventions)
  Returns evidence grades and feasibility metadata

data_agent (existing)
  Context 1: Climate Intelligence (data extraction)
  Unchanged -- climate data retrieval + LLM translation

health_data_agent (new)
  Context 4: Health Data
  DHIS2 normalization + published stats
  Anti-corruption layer: county-specific indicator mapping

data_analysis_agent (extended)
  Context 2: Health Risk Translation (reasoning)
  NEW tools: WBGT calculation, threshold application, risk scoring
  THIS IS WHERE THE TRANSLATION HAPPENS
  "10% more rain" --> "30% more cholera cases" --> "pre-position 50 kits"

combine_agent (modified)
  Context 3: Adaptation Planning
  Produces SeasonalAdaptationPlan formatted for AWP
  Political framing in prompt ("cost of inaction" language)
  Uncertainty warnings mandatory when confidence < 70%
```

---

## How to Run This for Real

### Pre-workshop (1 week before)

1. Print the simulated wall above on A0 paper as a starting point
2. Send participants the 3 "read model" mockups and ask: "Would you use this?"
3. Prepare blank stickies in all colors
4. Book a room with 6+ meters of empty wall space

### Workshop day (4-6 hours)

| Time | Activity | Goal |
|---|---|---|
| 0:00-0:30 | Introductions + rules | Everyone writes, no hierarchy |
| 0:30-1:30 | Chaotic exploration | Fill the wall with orange stickies |
| 1:30-2:00 | Break + silent reading | Everyone walks the wall |
| 2:00-3:00 | Timeline ordering | Left-to-right narrative emerges |
| 3:00-3:30 | Hotspot identification | Pink stickies on disagreements |
| 3:30-4:30 | Process modeling (TO-BE) | Blue commands, yellow actors, purple policies |
| 4:30-5:00 | Priority vote | Dot-vote on which process to build first |
| 5:00-5:30 | Wrap-up | Photograph wall, assign follow-ups |

### Post-workshop deliverables

1. Photograph of the entire wall (the artifact)
2. Typed-up domain events list (validate against this simulator)
3. Hotspot register (feed into risk register, Section 7 of building doc)
4. Bounded context diagram (validate against Section 3 architecture decisions)
5. Read model mockups revised based on feedback (feed into UI design)

### Validation questions for real workshop

Compare real workshop output against this simulation:

- [ ] Did the same pivotal event emerge (translation gap between forecast and AWP)?
- [ ] Did KEMSA lead time surface as a hard constraint?
- [ ] Did DHIS2 inconsistency emerge as a technical hotspot?
- [ ] Did political/Governor dynamics surface as institutional risk?
- [ ] Did participants identify the same three "products" (plan, supply list, community brief)?
- [ ] What did we get WRONG in this simulation?

That last question is the most valuable. Whatever the real workshop reveals that this simulation missed is the gap in our domain understanding.
