# CHART Positioning Analysis: 20 Critical Questions Answered

*Based on evidence from ScopeImpact project documents (Google Drive), March 2026*

---

## I. Stakeholder & User

### 1. Who is the actual end user?

**User:** Subnational Health Managers -- County Health Directors (Kenya), District Medical Officers (India) -- and their Technical Working Groups (TWGs).

**Output need:** A Prioritized Adaptation Plan insertable into quarterly budget cycles. Not dashboards, not trend reports -- "resource-shift" recommendations (e.g., "move $X from general outreach to heat-stress clinics next month").

**Implication for CHART:** The `combine_agent` output must produce structured, actionable plans with budget line items, not narrative summaries. This is fundamentally different from ClimSight's `final_answer: str`.

*Source: CHART technical narrative for UBS.docx; CHART & CHIP_Introduction_2026.pptx*

### 2. What does the user do today without CHART?

**Current artifacts:** Annual Work Plan (AWP) in Kenya, District Health Action Plan in India.

**The gap:** Decisions are reactive (responding to outbreaks after they start) or based on historical data (last year's budget drives this year's allocation). There is no "seasonal prediction" artifact currently driving climate-sensitive health resource allocation.

**Implication for CHART:** CHART doesn't replace an existing tool -- it creates a new artifact. This means adoption requires behavior change, not just tool migration. The UI must make the output feel like a natural extension of the AWP process.

*Source: ScopeImpact_CHART introduction and update - for Kenya MOH - 15JUN2025.pptx*

### 3. How does the target user currently receive climate information?

**Channels:** KMD (Kenya Meteorological Department) seasonal outlooks or IDSR (Integrated Disease Surveillance and Response) bulletins, typically via email or WhatsApp.

**The problem:** These are technical weather reports. They don't translate "10% more rain" into "30% more malaria cases at Clinic X."

**Implication for CHART:** The core value proposition is translation -- climate signal to health action. The LLM layer is justified specifically for this translation step, not for data retrieval.

*Source: ScopeImpact_CHART introduction and update July 2025.pptx*

### 4. What decision does CHART change?

**The specific shift:** Re-allocating staff schedules or pre-positioning medical supplies (IV fluids for heat exhaustion, cholera kits) 4-6 weeks before a predicted climate event, rather than requesting them during the emergency.

**Implication for CHART:** The 4-6 week lead time defines the forecast horizon. Open-Meteo seasonal forecasts (up to 6 months) are right; ERA5 reanalysis (historical) is supporting context, not the decision driver.

*Source: CHART & CHIP_Introduction_2026.pptx*

### 5. What happens if CHART gives bad advice?

**Governance model:** Human-in-the-loop. CHART produces a draft "Adaptation Plan." The TWG must review and sign off. Liability stays within existing government oversight structures, not on the software.

**Implication for CHART:** The clinical review gate (Section 3B of building doc) is not optional -- it's the mechanism that makes the human-in-the-loop governance credible. Output must clearly mark confidence levels and evidence grades so the TWG can meaningfully review rather than rubber-stamp.

*Source: 02_CHART Protocol_India_V.2*

---

## II. Market & Landscape

### 6. Who else is doing this?

**Landscape:** WHO ClimHealth, CHIRTS, IRI tools provide global/national-level models.

**CHART's differentiation:** Hyper-local (subnational) + a costed Action Repository of 110+ health interventions. Global models tell you "heat waves are increasing." CHART tells you "pre-position IV fluids at these 3 facilities by March 15."

**Implication for CHART:** The Action Repository is the product, not the AI. The knowledge base curation (Section 3A of building doc) is the critical path, not the engineering.

*Source: CHART for WB team.pptx; CHART/CHIP deck for RockFdn meeting*

### 7. Why hasn't this been built already?

**Three bottlenecks:**
1. **Data silos:** Climate data and health data live in different ministries
2. **Scale mismatch:** Most tools are too "macro" for a district manager
3. **Translation complexity:** Converting climate science into health actions requires multidisciplinary expertise that hasn't been digitized

**Implication for CHART:** Bottleneck #1 is why DHIS2 integration matters (bridges the silo). Bottleneck #2 is why the subnational focus is the moat. Bottleneck #3 is the specific job for the LLM + curated KB.

*Source: CHART technical narrative for UBS.docx*

### 8. Is Kenya the right first market?

**Rationale:** Kenya's 2010 Constitution decentralized health to 47 counties, each with its own health budget and authority. This is the perfect environment to test whether a tool can actually move money and resources locally -- because the counties have the power to act on recommendations.

**Implication for CHART:** A centralized health system (e.g., UK NHS) would be wrong -- recommendations would disappear into national bureaucracy. Kenya's decentralization means a county officer can actually shift budget based on CHART output.

*Source: ScopeImpact_CHART introduction and update - for Kenya MOH - 15JUN2025.pptx*

### 9. What's the competitive moat?

**The moat is not the code.** It's the Action Repository (vetted by experts) and embedded relationships with Ministries of Health. A competitor would need years to build the same institutional trust.

**Implication for CHART:** Open-sourcing the code (as a Digital Public Good) is safe because the code without the KB and institutional relationships has limited value. The moat is the curated knowledge + the government partnerships.

*Source: CHART vision and project*

### 10. Is the LLM the differentiator or the data?

**The differentiator is context synthesis.** A spreadsheet can handle thresholds. The LLM synthesizes qualitative local knowledge (e.g., "the bridge to Clinic B floods regularly") with quantitative data to draft a contextualized policy brief.

**Implication for CHART:** This validates the `data_analysis_agent` as the genuinely agentic core (see architecture decisions, Section 3 of building doc). But it also means the `combine_agent` prompt engineering is critical -- it must produce policy-grade prose, not academic summaries.

*Source: CHART & CHIP_Introduction_2026.pptx*

---

## III. Institutional & Policy

### 11. What does the Kenya MOH actually want?

**Evidence of demand:** The project has engaged the MOH Division of Environmental Health. Their stated interest is aligning climate adaptation with the National Climate Change Action Plan (NCCAP).

**Implication for CHART:** There is a specific institutional champion and a specific policy alignment (NCCAP). Output should reference NCCAP goals where applicable -- this makes adoption politically easier for the MOH champion.

*Source: ScopeImpact_CHART introduction and update July 2025.pptx*

### 12. What's the regulatory path?

**Classification:** CHART is framed as a Decision Support/Management Tool, not a medical diagnostic device. This places it under health informatics/planning departments, not the Pharmacy and Poisons Board.

**Implication for CHART:** This is a significant simplification. No FDA-equivalent approval needed. But it means CHART must never output diagnostic advice (e.g., "patients presenting with X should receive Y treatment"). Stay in the planning/resource allocation lane.

*Source: Technical Proposal*

### 13. How does CHART align with planning cycles?

**Synchronization:** CHART is timed to feed into the AWP cycle. If the tool produces a recommendation in October for a budget set in June, it fails.

**Implication for CHART:** This is a hard constraint on the product. The system needs to know the planning calendar and produce recommendations at the right time. This might mean scheduled batch runs (another argument for Dagster in Phase 3) timed to AWP submission deadlines.

*Source: CHART technical narrative for UBS.docx*

### 14. Who pays for ongoing operation?

**Model:** Digital Public Good (DPG). Early phases are donor-funded (Rockefeller/UBS). Long-term plan: infrastructure hosted on government servers or funded via a "Coalition" of partners.

**Implication for CHART:** LLM API costs must be minimized for sustainability. This favors: (a) smaller models where possible (gpt-4.1-nano for data agents), (b) caching/pre-computation via Dagster, (c) eventual migration to open-source models. The architecture should not be locked into expensive API calls for every query.

*Source: Overview - CHART UBS - soft launch*

### 15. What's the trust threshold?

**Pathway:** Trust is built through Participatory Co-design. Health officers help build the Action Repository during the pilot phase, making them more likely to trust outputs when the tool goes live.

**Implication for CHART:** The KB curation process is not just a data task -- it's a trust-building exercise. The 3-6 month timeline for the health KB (Section 3A) should include county health officer workshops, not just desk research by public health specialists.

*Source: 02_CHART Protocol_India_V.2*

---

## IV. Evidence & Impact

### 16. How do we measure success for funders?

**Intermediate metrics (month 12-18):**
- **Uptake:** Did the county include CHART recommendations in their signed AWP?
- **Resource shift:** Did budget move from "general" to "climate-specific" categories?

**Implication for CHART:** These metrics require tracking actual government planning documents, not system usage metrics. The evaluation framework needs access to pre/post AWP documents from pilot counties.

*Source: CHART Closing Report; Technical Proposal*

### 17. What's the counterfactual?

**Testing design:** The India protocol uses a comparison model -- CHART-assisted planning vs. standard government planning -- to prove AI-driven decisions are more specific and timely.

**Implication for CHART:** This is a quasi-experimental design. It means we need both CHART counties and control counties. The benchmark dataset (50 test cases in Section 9 of building doc) should include cases where "standard planning" would give a different answer than CHART.

*Source: 02_CHART Protocol_India_V.2*

### 18. Is there a published evidence gap CHART fills?

**The gap:** "Subnational Operationalization." Plenty of research on climate-health links exists. Almost no evidence exists on how a local manager should respond. CHART fills the implementation gap between science and action.

**Implication for CHART:** This is the strongest positioning statement. CHART is not "AI for climate" or "AI for health." It's "the missing layer between climate science and local health action." Every pitch, paper, and README should lead with this framing.

*Source: Technical Proposal*

### 19. What ethical review is needed?

**Status:** IRB approval and NACOSTI permits required because health managers will make real-world resource decisions based on patient trend data.

**Implication for CHART:** NACOSTI timeline is 2-3 months minimum. This is on the critical path for Phase 3 pilot deployment. Must be initiated in Phase 1 (already in the roadmap Track B).

*Source: CHART Protocol_India (reference)*

### 20. What's the failure mode we're most afraid of?

**The fear:** Institutional inertia. Even if the AI is perfect, the tool fails if political or financial systems are too rigid to allow a health officer to move a budget based on a prediction.

**Implication for CHART:** This is not a technical risk -- it's a change management risk. It means Phase 3 pilot deployment needs a "change champion" in each county, not just a software deployment. The TWG co-design workshops (Question 15) are the mitigation.

*Source: CHART vision and project; CHART/CHIP deck for RockFdn meeting*

---

## Summary: What This Means for the Technical Build

### The Action Repository is the product
The 110+ costed interventions, not the AI, are what makes CHART unique. Engineering effort should prioritize KB quality, retrieval accuracy, and evidence grading over model sophistication.

### The LLM earns its keep at the translation layer
Converting "10% more rainfall" into "pre-position cholera kits at Facility X by March 15" is the specific job. The `data_analysis_agent` reasoning loop and `combine_agent` synthesis are where the AI adds genuine value.

### Output format must match the AWP process
The final output is not a report -- it's a draft budget amendment. Structured Pydantic schemas (HealthRiskAssessment, InterventionRecommendation, SeasonalPlan) must produce artifacts that map directly to AWP line items.

### Cost minimization is a sustainability requirement
DPG model means no expensive API calls per query long-term. Architecture should support: cached data (Dagster), smaller models for extraction agents, pre-computed seasonal plans for common scenarios.

### Trust is built through co-design, not accuracy metrics
Getting county health officers involved in building the KB is the adoption strategy. This is not a "build it and they will come" product.

### The biggest risk is not technical
Institutional inertia -- governments too rigid to act on predictions -- is the primary failure mode. No amount of engineering solves this; it requires change management embedded in the pilot design.
