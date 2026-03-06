# Bridging the Translation Gap: A Landscape Analysis of Digital Platforms for Climate-Informed Health Decision-Making

**Authors:** [Scope Impact team + collaborators — to be confirmed]

**Date:** March 2026

**Version:** Draft 1.0

---

## Executive Summary

Climate change is an escalating threat to human health, with the WHO projecting 250,000 additional climate-related deaths annually by 2050. Pregnant women, newborns, and children are disproportionately vulnerable — heatwave days are associated with a ~16% increase in preterm birth risk, yet only 4 of the world's Heat Health Action Plans include interventions for maternity and neonatal care.

A growing ecosystem of digital platforms now addresses parts of the climate-health challenge: surveillance systems import climate data into health dashboards, machine learning models forecast disease outbreaks, and vulnerability indices score population-level risk. Yet a critical gap persists. **No existing tool translates seasonal climate forecasts into costed, localized health intervention plans for subnational decision-makers.** District health officers receive climate outlooks that say "10% more rainfall expected" but nothing that converts this into "pre-position cholera kits at Facility X by March 15."

This white paper maps the current landscape of climate-health digital platforms, analyzes evidence of impact and adoption barriers, and identifies this "translation gap" as the central unmet need. We find that existing tools cluster on the left side of a value chain — from climate data ingestion through disease forecasting and risk assessment — while the planning, implementation, and monitoring steps remain entirely unaddressed by digital tools. We conclude with future directions describing how emerging AI capabilities (multi-agent architectures, retrieval-augmented generation, structured output schemas) could bridge this gap, and outline the design principles such a tool would need to follow.

---

## 1. Introduction

Climate change represents a fundamental threat to human health, with pregnant women and newborns among the most susceptible populations (WHO, JOGH 2024). The evidence base has strengthened considerably in recent years:

- Each 1°C increase in ambient temperature is associated with ~5% increase in preterm birth likelihood (PLOS Climate 2025)
- Heatwave days are associated with ~16% increase in preterm birth risk (PLOS Climate 2025)
- Projected impact in India alone: 353,000 heat-related preterm births across urban centers between 2025-2035
- The CHAMNHA project found extreme heat associated with increased stillbirth rates in Kenya and Burkina Faso, with risk increasing with duration of exposure, not just peak temperature (LSHTM)

Yet the translation of this evidence into operational health responses remains weak. A 2025 review of Heat Health Action Plans globally found that while 83% identified children as at-risk and 52% named pregnant women, only 14% mentioned postpartum or breastfeeding mothers, and only 4 plans included interventions to improve care in maternity facilities (PMC 2025). Clear interventions to address climate change impacts on maternal, newborn, and child health (MNCH) are "rarely proposed or elaborated" in national policies (JOGH 2024).

In parallel, a wave of digital health and climate platforms has emerged, backed by significant investment — over $1 billion in philanthropic commitments at COP28 alone, the Wellcome Trust's £14.5 million for DHIS2 climate tools, and the Global Fund's $50 million Climate x Health Catalytic Fund. These platforms represent genuine progress in making climate data accessible to health systems. But a systematic look at what they do — and what they don't — reveals a persistent gap between climate awareness and health action.

This white paper provides a structured landscape analysis of the major digital platforms operating at the intersection of climate and health, identifies the specific functions they serve and the functions they leave unaddressed, and examines what it would take to close the gap.

**Scope and methodology:** This is a structured landscape analysis, not a systematic review. We surveyed platform documentation, peer-reviewed literature, funder reports, and project documents from 2022-2026, focusing on tools with demonstrated deployment or active development. We organize findings around a value chain framework that maps each platform's function from climate data ingestion through to health action.

---

## 2. The Climate-Health Platform Ecosystem

We organize the landscape around a six-stage value chain:

```
Climate Data → Disease Forecast → Risk Assessment → Plan → Implement → Monitor
```

Existing platforms cluster overwhelmingly in the first three stages. The final three — planning, implementation, and monitoring — remain unaddressed by any digital tool we identified.

### 2.1 Health Information Infrastructure

**DHIS2 Climate App** (HISP/University of Oslo + Global Fund)

The most significant infrastructure development is the integration of climate data into DHIS2, the open-source health information system used by 80+ countries managing data for 3.9 billion people. The DHIS2 Climate App imports ERA5-Land climate data (temperature, precipitation, humidity, vegetation index) directly into DHIS2 data elements, enabling correlation with health outcomes within existing dashboards.

Deployment is advancing: the Global Fund's Climate x Health Catalytic Fund (2025) is funding 7 African countries; Uganda is piloting district-level malaria suitability mapping in 5 districts expanding to 15; Malawi launched a 4-district surveillance project in December 2025; and Togo has an operational climate-malaria dashboard at national level.

**What it doesn't do:** The Climate App provides surveillance and correlation — it shows that temperature and malaria cases move together. It does not recommend interventions, forecast future risk, or support seasonal planning. It has no MNCH-specific analysis.

### 2.2 Disease Forecasting

**CHAP** (Climate Health Analytics Platform, HISP/University of Oslo + Wellcome Trust)

CHAP provides machine learning disease forecasting integrated with DHIS2, predicting malaria, dengue, and cholera outbreaks using combined climate and health data. It is a 5-year project (2024-2029) under active development, being piloted alongside the Climate App in Malawi and Uganda.

**Ethiopia EWARS** (ClimaHealth/WHO-WMO)

The Early Warning Alert and Response System in Ethiopia has demonstrated predictive capability, forecasting malaria outbreaks in Bahir Dar and enabling emergency preparedness.

**What forecasting doesn't do:** These tools predict disease burden but stop there. CHAP can say "malaria will spike in July in Kisumu County" — but it does not say "here are 4 evidence-based interventions for malaria prevention during pregnancy in Kisumu, with implementation timeline and cost."

### 2.3 Vulnerability Assessment

**Khushi Baby CHVI** (India)

The Climate Health Vulnerability Index provides village-level vulnerability scoring for Rajasthan (80 million people), using PCA and regression on exposure, sensitivity, and adaptive capacity indicators. It integrates digital health records from community health worker-delivered MNCH services and is establishing causal links between climate variables and health outcomes.

**CDC BRACE Framework** (United States)

The Building Resilience Against Climate Effects framework provides a step-by-step methodology for climate-health adaptation planning, used primarily by US state and local health departments.

**Ahmedabad Heat Action Plan** (India)

India's first city-level HAP (2013), now a model for 23+ Indian cities, includes early warning, public awareness, medical preparedness, and cool roofs. Evaluation showed reduced heat-related mortality (rate ratio from 2.34 to 1.25 at 47°C). However, it tracks no maternal-specific outcomes.

**What vulnerability assessment doesn't do:** Scoring identifies *who* is vulnerable and *where*, but not *what to do about it*. Khushi Baby's CHVI can flag a high-risk village, but produces no seasonal planning workflow, no intervention matching, and no implementation tracking.

### 2.4 Knowledge Platforms

**ClimaHealth** (WHO + WMO + Wellcome Trust)

The first global knowledge platform for climate and health (launched October 2022), with a resource library of case studies, guidance documents, and tools. It covers 4 themes across 66 countries with 90+ health focal points. A valuable knowledge repository, but a library — not a planning tool. It provides no district-level output, no climate data integration, and no intervention matching for specific locations and seasons.

**Americares Climate Resilience Toolkit** (US, expanding to Philippines)

Provides clinic-level heat, wildfire, and flood action plans with patient-facing materials, including pregnancy-specific guidance. Used by 180+ clinics in the US. But it is facility-focused (not district-level), uses generic guidance (not location-specific climate data), and has no health system integration.

### 2.5 Summary: Where Platforms Sit in the Value Chain

| Platform | Climate Data | Forecast | Risk Assessment | Plan | Implement | Monitor |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| DHIS2 Climate App | **Yes** | No | No | No | No | No |
| CHAP | Yes | **Yes** | No | No | No | No |
| Khushi Baby CHVI | Yes | No | **Yes** | No | No | No |
| Ahmedabad HAP | Partial | Partial | **Yes** | Partial | Partial | No |
| ClimaHealth | No | No | No | No | No | No |
| Americares Toolkit | No | No | Partial | **Partial** | No | No |

**The right side of this value chain — planning, implementation, and monitoring — is essentially unoccupied by digital tools.** The Ahmedabad HAP and Americares Toolkit partially address planning, but neither integrates climate forecast data with localized health intervention recommendations at the subnational level.

*[Placeholder: Table will be enriched with additional platforms from Airtable database when available]*

---

## 3. Evidence of Impact and Adoption Barriers

### 3.1 What Works

The strongest evidence of impact comes from the Ahmedabad HAP, which demonstrated measurable reductions in heat-related mortality after implementation. The CHAMNHA project in Kenya and Burkina Faso has produced the most relevant evidence for MNCH specifically:

- In Kilifi County, Kenya, community health volunteers were trained to monitor heat stress and disseminate alerts to pregnant and postpartum women. Women reported better understanding of heat effects; mothers-in-law and male spouses began assisting with household chores during heat events (Health Policy & Planning 2025).
- In Burkina Faso, behavior change interventions (interviews, videos, illustrated discussions) reduced adverse heat-related health impacts among pregnant women. Integration into routine practice was found to be feasible (Health Policy & Planning 2025).
- Climate education programs targeting maternal and newborn health, reviewed across LMICs and the US, all reported positive outcomes. Two programs that assessed health impacts found significant reductions in adverse outcomes (ScienceDirect 2025).

Common success factors across implementations include government ownership, simple and actionable outputs, multi-stakeholder coordination, and integration with existing planning cycles.

### 3.2 What Doesn't Work

Despite growing investment, evidence of scaled implementation remains thin:

- A 2024 scoping review found "very little evidence of actual implementation" of climate-health digital tools beyond pilot phases
- A 2022 Lancet Planetary Health assessment concluded that "no place in the world" has a fully integrated climate-health early warning system
- Only 2 implementation science studies on climate-health responses were identified in a 2025 Lancet Planetary Health review
- CHAP, developed by DHIS2's own team at the University of Oslo with Wellcome Trust funding, remains "in progress" after 2+ years of development — illustrating the difficulty of even well-resourced efforts

### 3.3 Adoption Barriers

| Category | Barrier | Evidence |
|---|---|---|
| **Technical** | Connectivity gaps | 17.8% of African households have internet access |
| | Interoperability | DHIS2 integration requires metadata mapping across 13 dimensions |
| | Data quality | Missing values, delayed reporting common in DHIS2 instances |
| **Organizational** | Staff turnover | District health officers rotate frequently; institutional knowledge lost |
| | No response protocols | Climate data arrives but no standard operating procedure for acting on it |
| | Tool fatigue | Each new platform adds another interface for already-burdened staff |
| **Institutional** | Cross-ministry coordination | Climate data (meteorological department) and health data (health ministry) sit in different ministries |
| | Planning cycle misalignment | Climate forecasts don't align with annual budget submission deadlines |
| | DHIS2 access requires MoU | Institutional agreements take 3-6 months; CHAP's own integration remains incomplete |
| **Political** | Sustaining political will | Pilot support doesn't guarantee scale-up funding |

The "last mile" problem is acute: most tools are designed for national or regional analysis, but health resource allocation decisions are made at the district or county level. The decision-maker who could act on a climate-health recommendation — a County Health Director in Kenya, a District Medical Officer in India — often has no digital tool designed for their role.

---

## 4. The Funding Landscape

Investment in climate-health tools has accelerated sharply since 2022:

| Commitment | Source | Amount | Focus |
|---|---|---|---|
| COP28 climate-health declaration (2023) | 35+ philanthropies | $300M+ | Climate and health broadly |
| DHIS2 Climate & Health | Wellcome Trust | £14.5M | CHAP + Climate App |
| Climate x Health Catalytic Fund (2025) | Global Fund | $50M | 7 African countries, DHIS2 tools |
| WHO Health & Climate Initiative | Rockefeller Foundation | $100M | WHO-WMO programme |
| Climate-health research | Wellcome Trust | £22.7M | 24 research teams globally |
| Kenya RMNCAH-N 2025-2030 | Multiple (national budget + donors) | Not disclosed | National MNCH framework including climate |
| Climate adaptation (agricultural focus) | Gates Foundation | $1.4B | Primarily agriculture, some health co-benefits |

Despite this investment, health remains a small share of total climate finance — rising from 1% in 2018 to 9% in 2022, but far below the estimated $22 billion annual need. Over 50% of Africa's adaptation financing comes as loans rather than grants, creating sustainability concerns for health systems.

A notable pattern: funding flows primarily toward **infrastructure** (DHIS2 integration, data platforms) and **research** (evidence generation, forecasting models), with very little directed toward **operational planning tools** for subnational health managers. The translation gap exists in funding as well as in technology.

*[Placeholder: Additional funding data from Airtable database to be integrated]*

---

## 5. Critical Gaps

### 5.1 The Translation Gap

The central finding of this analysis is that the climate-health platform ecosystem has consolidated around surveillance, forecasting, and risk assessment — the **"what is happening"** and **"what might happen"** questions — while leaving the **"what should we do about it"** question almost entirely unaddressed by digital tools.

No tool we identified produces a **seasonal climate-health preparedness plan** for a district health officer that:

1. Connects a seasonal climate forecast to specific local health risks
2. Matches those risks to evidence-based interventions appropriate for the setting
3. Accounts for local capacity, infrastructure, and supply chain constraints
4. Generates a structured implementation plan with timelines and cost estimates
5. Aligns with the existing annual/quarterly planning cycle

This is the translation gap: climate science exists, health data exists, intervention evidence exists — but no system synthesizes them into the seasonal adaptation plan that a subnational health manager needs to act.

### 5.2 The Intervention Knowledge Gap

A prerequisite for closing the translation gap is a curated, structured knowledge base of climate-health interventions. No such database exists. The most comprehensive source is a 2025 JOGH scoping review identifying 79 interventions across 4 socioecological levels:

| Level | Count | Examples |
|---|---|---|
| Individual/Household | 30 | Hydration counseling, bed nets, breastfeeding support during heat |
| Community/Service | 18 | CHW heat alert systems, cooler community spaces, mHealth messaging |
| Structural/Urban | 15 | Shade near facilities, clean water infrastructure, facility cooling |
| Policy/Systemic | 16 | Heat action plans with MNCH components, cash transfers, early warning |

Most of these interventions are academic descriptions, not operational decision-support entries. They lack evidence grading, cost estimates, local feasibility assessment, implementation requirements, and contraindications. Converting scattered research into a decision-ready knowledge base is a multi-month, multi-disciplinary undertaking — arguably the hardest component of any planning tool.

### 5.3 The MNCH-Specific Gap

Climate-health tools predominantly focus on infectious disease (malaria, dengue, cholera). MNCH is systematically underserved:

- No existing platform has an MNCH-specific module
- Heat Health Action Plans rarely disaggregate outcomes by pregnancy status
- Khushi Baby's CHVI is the only tool integrating climate vulnerability with MNCH service data — but it covers only vulnerability scoring, not intervention planning
- The CHAMNHA project has produced the strongest MNCH-specific evidence, but it covers only Kenya and Burkina Faso and has not been digitized into a reusable tool

---

## 6. Future Directions: Toward a Climate-Health Adaptation Planning Tool

The gaps identified in this analysis point toward a specific unmet need: a digital tool that sits between climate forecasting and health service delivery, translating seasonal predictions into actionable, localized plans. Based on the evidence reviewed, we outline the design principles such a tool would need to follow.

### 6.1 Design Principles

**Build on existing infrastructure, don't replace it.** DHIS2 is the health data backbone in 80+ countries. A planning tool should read from DHIS2, not duplicate it. Similarly, climate data should come from established sources (ERA5, national meteorological services) rather than proprietary data pipelines. The role of a new tool is synthesis and planning, not data collection.

**The curated knowledge base is the product.** Emerging AI capabilities — multi-agent architectures, retrieval-augmented generation (RAG), structured output schemas — provide the mechanism for synthesis. But the differentiating value lies in the curated intervention knowledge base: a structured, evidence-graded, contextually tagged collection of climate-health interventions that can be matched to local conditions. Building this knowledge base requires public health expertise, not just software engineering. The CHAMNHA project took 3+ years to produce a validated framework for one population in one country; a useful knowledge base must be designed for iterative expansion as evidence grows.

**Match the planning artifact, not the dashboard.** The end user is a County Health Director or District Medical Officer making quarterly budget decisions. Their planning artifact is the Annual Work Plan (AWP), not a dashboard. A useful tool produces draft seasonal adaptation plans insertable into the AWP — budget line items, implementation timelines, responsible actors — not narrative reports or trend visualizations.

**Human-in-the-loop governance is non-negotiable.** Any tool generating health resource recommendations must operate under clinical review. A Technical Working Group should review and approve recommendations before implementation. The system must clearly communicate confidence levels and evidence grades so that reviewers can meaningfully assess rather than rubber-stamp outputs. When evidence is insufficient, the system must explicitly say so rather than generating plausible-sounding recommendations.

**Align with planning cycles.** Climate forecasts are useful only if they arrive at the right time. A seasonal adaptation tool must synchronize with budget submission deadlines and planning calendars. A recommendation produced in October for a budget set in June is useless. This favors scheduled batch processing timed to planning cycles over on-demand queries.

**Design for sustainability.** A Digital Public Good model — open-source code, locally deployable, minimal recurring costs — is essential for government adoption. LLM API costs must be minimized through caching, pre-computation, and use of smaller models where appropriate.

### 6.2 Where AI Adds Genuine Value

The specific value of AI in this context is not data retrieval or visualization — those are well-served by existing tools. The value is **translation**: synthesizing qualitative local knowledge ("the bridge to Clinic B floods regularly") with quantitative climate and health data to draft a contextualized policy brief. This requires:

- **Retrieval-augmented generation** over curated intervention knowledge bases, enabling evidence-graded recommendations with source citations
- **Multi-agent architectures** for parallel information gathering from climate, health, and knowledge sources with graceful degradation when data is unavailable
- **Structured output schemas** enforcing evidence grades, confidence levels, and provenance chains — preventing the generation of unsupported recommendations
- **Tool-calling agents** capable of computing derived health indicators (wet-bulb globe temperature, heat stress indices) from raw climate data

### 6.3 Implementation Context

Kenya presents the strongest case for initial implementation: its 2010 Constitution devolved health governance to 47 counties, each with budget authority — meaning county officers can actually act on recommendations. The national RMNCAH-N Investment Framework 2025-2030 explicitly includes climate change interventions. CHAMNHA has produced Kenya-specific intervention evidence from Kilifi County. DHIS2 has been operational since 2011 across all counties. And an engaged research community (Aga Khan University, KEMRI, LSHTM) provides the domain expertise essential for knowledge base curation.

India, with 766 districts across diverse agroecological zones, presents a higher-complexity second phase. Emerging state-level efforts — Rajasthan's Khushi Baby CHVI, Ahmedabad's HAP, the national NAPCCHH framework — provide building blocks, but no national climate-MNCH policy framework yet exists comparable to Kenya's.

### 6.4 What Makes This Hard

The honest assessment is that building a climate-health planning tool is primarily a knowledge curation and institutional partnership challenge, not a technology challenge. Based on our analysis:

- Engineering infrastructure (workflow engines, RAG systems, data pipelines) represents ~20-25% of the total effort
- Health knowledge curation — extracting, grading, contextualizing, and validating interventions — represents 25-30%
- Clinical validation and governance — structured review processes, benchmark datasets, safety pathways — represents 15-20%
- Data partnerships and institutional access — DHIS2 MoUs, meteorological service relationships, ethics review — represents 15-20%

The team composition required is fundamentally cross-disciplinary: ML/LLM engineers working alongside public health specialists, local health systems experts, and clinical advisors. The biggest risk is not technical failure — it is institutional inertia, where the political and financial systems are too rigid to allow a health officer to shift budget allocations based on a seasonal prediction.

---

## 7. Conclusion

The climate-health digital platform ecosystem has made significant progress in making climate data visible to health systems. DHIS2's climate integration, CHAP's disease forecasting, and tools like Khushi Baby's vulnerability index represent genuine advances. Philanthropic investment exceeding $1 billion signals strong institutional commitment.

Yet a fundamental gap persists. The platforms that exist answer "what is the climate doing?" and "what disease burden might result?" but not "what should a district health officer do about it next quarter?" This translation gap — between climate science and local health action — is where the greatest unmet need lies, and where emerging AI capabilities are most relevant.

Closing this gap requires more than technology. It requires curated intervention knowledge bases built with domain expertise, clinical validation frameworks that prevent harm, institutional partnerships that take months to establish, and participatory co-design that builds the trust necessary for adoption. The hardest part is not the engineering — it is the knowledge curation, the institutional relationships, and the change management that makes a district health officer confident enough to shift resources based on a seasonal prediction.

The field has consolidated around surveillance and forecasting. Planning and implementation is the frontier.

---

## References

### Evidence Base: Climate and MNCH

1. PLOS Climate 2025. Heat exposure and preterm birth risk. https://journals.plos.org/climate/article/file?id=10.1371/journal.pclm.0000637&type=printable
2. CHAMNHA/LSHTM. Climate, Heat and Maternal and Neonatal Health in Africa. https://www.lshtm.ac.uk/research/centres-projects-groups/chamnha
3. CHAMNHA Kenya intervention. Health Policy & Planning 2025. https://doi.org/10.1093/heapol/czaf028
4. CHAMNHA Burkina Faso intervention. Health Policy & Planning 2025. https://academic.oup.com/heapol/article-pdf/40/7/708/63386252/czaf030.pdf
5. WHO overview of reviews on climate and MNCH. JOGH 2024. https://jogh.org/2024/jogh-14-04128
6. MNCH in Heat Health Action Plans. PMC 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12143117/
7. Evidence gap map: climate x maternal health. PLOS Global Public Health 2024. https://journals.plos.org/globalpublichealth/article?id=10.1371/journal.pgph.0003540
8. Climate education for MNH. ScienceDirect 2025. https://www.sciencedirect.com/science/article/pii/S2667278225001087
9. Multilevel adaptation strategies. ScienceDirect 2025. https://www.sciencedirect.com/science/article/pii/S2589004225001749
10. WHO climate and health projections. Public Health Reviews 2024. https://www.ssph-journal.org/journals/public-health-reviews/articles/10.3389/phrs.2024.1607553/full
11. PMNCH Dialogue on Climate and MNCH. February 2025. https://pmnch.who.int/news-and-events/news/item/03-03-2025-addressing-the-impacts-of-climate-change-on-maternal-newborn-and-child-health-and-building-climate-resilient-societies

### Intervention Knowledge

12. JOGH 2025 scoping review: 79 climate-health interventions. https://jogh.org/2025/jogh-15-04035
13. Kenya RMNCAH-N Investment Framework 2025-2030. https://countdown2030.org/wp-content/uploads/2025/10/RMNXAH-N-for-Official-Processing.pdf
14. Americares Climate Resilience Toolkit. https://www.americares.org/what-we-do/community-health/climate-resilient-health-clinics/

### Platforms and Tools

15. DHIS2 Climate App. https://dhis2.org/climate/features/
16. DHIS2 Climate Data. https://dhis2.org/climate/climate-data/
17. CHAP (Climate Health Analytics Platform). https://chap.dhis2.org/
18. DHIS2 Global Fund Climate x Health Catalytic Fund. https://dhis2.org/global-fund-climate-health-catalytic/
19. DHIS2 Malawi climate-sensitive disease surveillance. https://dhis2.org/malawi-project-to-strengthen-surveillance-climate-sensitive-diseases/
20. DHIS2 Togo climate-malaria dashboard. https://dhis2.org/climate-malaria-dashboard-togo/
21. ClimaHealth (WHO-WMO). https://climahealth.info/
22. WHO-WMO ClimaHealth launch announcement. https://www.who.int/news/item/31-10-2022-who-and-wmo-launch-a-new-knowledge-platform-for-climate-and-health
23. Ethiopia EWARS. https://climahealth.info/resource-library/developing-early-warning-alert-and-response-systems-ewars-to-combat-climate-sensitive-diseases-in-ethiopia/
24. Khushi Baby CHVI. https://www.khushibaby.org/cause/climate-health
25. Khushi Baby — data.org Data Capacity Accelerator. https://data.org/playbooks/lessons-from-indias-data-capacity-accelerator-for-climate-and-health/
26. Ahmedabad Heat Action Plan. https://www.exemplars.health/stories/ahmedabad-indias-heat-action-plan
27. Ahmedabad HAP evaluation. PMC. https://pmc.ncbi.nlm.nih.gov/articles/PMC6236972/
28. CDC BRACE Framework. https://www.cdc.gov/climate-health/php/brace/index.html

### Funding and Policy

29. Wellcome Trust DHIS2 funding. https://dhis2.org/climate/
30. Kenya Climate Change Act 2016. https://www.klrc.go.ke/
31. India NAPCCHH. https://ncdc.mohfw.gov.in/
32. India NHM RMNCH+A. https://nhm.gov.in/

### Data Sources

33. Copernicus Climate Data Store (ERA5). https://cds.climate.copernicus.eu/
34. Open-Meteo Climate API. https://open-meteo.com/en/docs/climate-api
35. Kenya Meteorological Department. https://meteo.go.ke/
36. India Meteorological Department. https://mausam.imd.gov.in/
37. IRI Data Library. https://iridl.ldeo.columbia.edu/
38. CHIRPS precipitation data. https://www.chc.ucsb.edu/data/chirps
