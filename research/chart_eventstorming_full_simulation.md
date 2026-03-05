# CHART EventStorming: Complete Workshop Simulation

*A full narrative simulation of a two-day EventStorming workshop for the Climate x Health Adaptation and Resilience Tool*

*Setting: Conference room, Kenya Medical Research Institute (KEMRI), Kilifi County. March 2026. Six meters of brown paper on the wall. Eight colors of sticky notes. Seven people who have never been in the same room before.*

---

## Cast

| Seat | Name | Role | Superpower | Fear |
|---|---|---|---|---|
| 1 | **Dr. Amina Mwangi** | County Health Director, Kilifi | Knows the AWP process cold; has Governor's ear | "Another donor tool that sits on a shelf" |
| 2 | **Joseph Odhiambo** | Disease Surveillance Officer, Kilifi sub-county | First to see outbreaks in DHIS2; runs IDSR | "We order too late, every single time" |
| 3 | **Dr. Wanjiku Karanja** | MOH Division of Environmental Health, Nairobi | Connects counties to national policy (NCCAP) | "Counties do their own thing; I can't coordinate" |
| 4 | **Peter Mutua** | Senior Forecaster, Kenya Meteorological Department | 15 years of seasonal outlooks; knows the models | "Nobody reads my forecasts" |
| 5 | **Sarah Kerubo** | CHW Supervisor, Malindi sub-county | Manages 45 community health workers; walks the ground | "We're always the last to know, first to respond" |
| 6 | **Raj Patel** | DHIS2 Technical Officer, Health IT unit | Built Kilifi's DHIS2 instance; maintains 3 counties | "Everyone blames the data, nobody fixes the config" |
| 7 | **The Engineer** | ClimSight/CHART developer | Built the climate pipeline; new to health | "I don't know what I don't know about this domain" |

**Facilitator:** Uses Brandolini-style facilitation. Minimal talking, maximum wall.

---




# CHART EventStorming Workshop Simulation — Phases 1 & 2

## Venue: Sarova Whitesands Beach Resort, Mombasa — Conference Room B
## Date: 15 March 2026
## Facilitator: Alberto (remote via screen, with local co-facilitator marking the wall)

---

## PHASE 1: CHAOTIC EXPLORATION (0:30–1:30)

Alberto's voice cuts through the room from the screen propped on the side table: *"Write down everything that happens in climate-sensitive health planning. One event per sticky. Past tense. Orange stickies only. Don't talk yet. Just write. Go."*

Seven people sit around a wide U-shaped table. A blank eight-metre stretch of butcher paper covers the far wall. Stacks of orange sticky notes and fat markers sit in the centre. For exactly eleven seconds, nobody moves.

Dr. Amina picks up a marker first. Then Peter. Then everyone is writing.

### The Silent Phase (0:30–0:42)

The only sounds are markers squeaking and the aircon rattling. Sarah holds her sticky note pad on her knee under the table, writing small, neat letters. Raj is already on his fourth sticky, writing fast, almost angry. The Engineer watches everyone for thirty seconds, then starts writing too, more slowly, frowning at each one.

Dr. Amina places her first sticky on the table in front of her:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Annual Work Plan was submitted    │
│   to County Treasury"               │
│                        — Dr. Amina  │
└─────────────────────────────────────┘
```

Peter, without looking up, slaps down:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Seasonal rainfall outlook was     │
│   issued by KMD"                    │
│                        — Peter      │
└─────────────────────────────────────┘
```

Joseph is writing fast, small handwriting, stacking them:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Unusual malaria cluster was       │
│   detected in IDSR weekly report"   │
│                        — Joseph     │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "IDSR bulletin was compiled        │
│   and sent to county"               │
│                        — Joseph     │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Cholera case was confirmed        │
│   at sub-county hospital"           │
│                        — Joseph     │
└─────────────────────────────────────┘
```

Raj writes with a kind of grim precision:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "DHIS2 monthly summary was         │
│   submitted by facility"            │
│                        — Raj        │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "DHIS2 data was found to have      │
│   missing fields for 12 facilities" │
│                        — Raj        │
└─────────────────────────────────────┘
```

Dr. Wanjiku writes in block capitals:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "NCCAP quarterly report was        │
│   submitted to National Treasury"   │
│                        — Dr. Wanjiku│
└─────────────────────────────────────┘
```

Sarah, still writing on her knee:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Community health volunteer        │
│   reported increased diarrhoea      │
│   cases during household visits"    │
│                        — Sarah      │
└─────────────────────────────────────┘
```

The Engineer pauses, looks at what others have written, then carefully writes:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Climate forecast data was         │
│   ingested by system"               │
│                        — Engineer   │
└─────────────────────────────────────┘
```

### The Dam Breaks (0:42–0:55)

Alberto says: *"OK. Start reading them aloud. Put them on the wall. Anywhere. No order yet."*

Peter stands first, walks to the wall, and reads as he sticks: **"Seasonal rainfall outlook was issued by KMD."**

Joseph immediately says "Wait—" and writes another sticky rapidly:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Seasonal outlook was received     │
│   by... actually, who receives it?" │
│                        — Joseph     │
└─────────────────────────────────────┘
```

He crosses out the second half and rewrites:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Seasonal outlook was emailed to   │
│   county disaster committee"        │
│                        — Joseph     │
└─────────────────────────────────────┘
```

**Peter** (turning from the wall): "It goes to NDMA and county commissioners. Not health directly."

**Dr. Amina** (looking up sharply): "Wait. We don't get the outlook directly?"

**Peter**: "It goes to the County Commissioner's office. And NDMA. The health department isn't on the distribution."

**Dr. Amina**: "You're joking."

**Peter**: "I'm not joking. The mailing list is governance and disaster management. Health was never added."

A silence. Then Dr. Amina writes, fast:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "County health dept learned about  │
│   forecast from newspaper"          │
│                        — Dr. Amina  │
└─────────────────────────────────────┘
```

She sticks it on the wall next to Peter's. Joseph laughs, then stops, because it isn't funny.

**Dr. Wanjiku** (standing, placing her stickies): "This is exactly what I've been telling Nairobi. The health sector is not in the climate information loop." She places:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Climate-health risk assessment    │
│   was requested by NCCAP unit"      │
│                        — Dr. Wanjiku│
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "County health director was asked  │
│   to report climate adaptation      │
│   actions (but had done none)"      │
│                        — Dr. Wanjiku│
└─────────────────────────────────────┘
```

Now the stickies are coming fast. People are triggering each other.

**Joseph** places a burst:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Disease threshold was exceeded    │
│   for malaria in sentinel site"     │
│                        — Joseph     │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Outbreak response team was        │
│   deployed to sub-county"           │
│                        — Joseph     │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Emergency drug request was sent   │
│   to KEMSA"                         │
│                        — Joseph     │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "KEMSA delivery arrived 7 weeks    │
│   after emergency request"          │
│                        — Joseph     │
└─────────────────────────────────────┘
```

**Dr. Amina** (from her seat, not looking up, writing): "Seven weeks is optimistic. Last October it was nine."

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "KEMSA delivery arrived after      │
│   outbreak had already peaked"      │
│                        — Dr. Amina  │
└─────────────────────────────────────┘
```

### The Engineer Asks Questions (0:55–1:05)

The Engineer has been placing stickies quietly:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Health risk score was calculated  │
│   from climate data"                │
│                        — Engineer   │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Intervention recommendation was   │
│   generated by system"              │
│                        — Engineer   │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Cost estimate was attached to     │
│   intervention plan"                │
│                        — Engineer   │
└─────────────────────────────────────┘
```

Then the Engineer turns to Joseph: "When you say 'disease threshold was exceeded,' what's the actual threshold? Is it a number? A percentage increase? Who defines it?"

**Joseph** (slightly irritated): "It's in the IDSR guidelines. Each disease has a threshold. For malaria, it's when cases exceed the third quartile of the previous five years for that epidemiological week."

**Engineer**: "So you need five years of weekly historical data, by facility, to—"

**Raj** (interrupting): "And that's the problem. I can tell you right now that maybe eighteen of Kilifi's sixty-something facilities have five years of complete weekly data in DHIS2. Maybe."

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Threshold calculation failed      │
│   because historical data was       │
│   incomplete in DHIS2"              │
│                        — Raj        │
└─────────────────────────────────────┘
```

**Engineer**: "OK, and when you say 'outbreak'—what's the formal definition? Is a single confirmed cholera case an outbreak?"

**Joseph** (more irritated): "Yes. One confirmed cholera case is an outbreak. That's the national definition."

**Dr. Wanjiku**: "He's right. Cholera is one case. Measles depends on context. It's disease-specific."

**Engineer**: "And who declares it? Is there a formal—"

**Joseph**: "The sub-county disease surveillance coordinator. Me. I verify and notify county and national."

The Engineer writes:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Outbreak was formally declared    │
│   by sub-county DSC"               │
│                        — Engineer   │
└─────────────────────────────────────┘
```

**Joseph** (looking at it): "Formally. Sure. Formally what happens is I call Dr. Amina on WhatsApp at 10pm because the IDSR form takes three days to process."

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Outbreak was reported to county   │
│   health director via WhatsApp"     │
│                        — Joseph     │
└─────────────────────────────────────┘
```

Laughter around the room. Dr. Amina nods ruefully.

### Sarah Enters the Conversation (1:05–1:18)

Sarah has been placing stickies quietly. Small handwriting, very specific:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "CHWs reported that Rare River     │
│   bridge was impassable after       │
│   three days of rain"               │
│                        — Sarah      │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Pregnant woman in Bamba was       │
│   unable to reach health facility   │
│   due to flooding"                  │
│                        — Sarah      │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "CHW reported water source         │
│   contamination after flooding"     │
│                        — Sarah      │
└─────────────────────────────────────┘
```

Nobody is really reading these yet. They're clustered at the far end of the wall. Then Sarah places one and reads it aloud, quietly:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Three children died of            │
│   diarrhoeal disease during         │
│   period between contamination      │
│   and response team arrival"        │
│                        — Sarah      │
└─────────────────────────────────────┘
```

The room goes quiet.

**Dr. Amina**: "When was this?"

**Sarah**: "November. Last November. After the short rains. Bamba sub-county. The CHWs had reported the contamination on day one. The report went to the facility. The facility reported in the monthly DHIS2 summary. By then it had been three weeks."

**Raj** (quietly): "Monthly summary. Not weekly IDSR."

**Sarah**: "The facility doesn't do weekly IDSR. They don't have the forms. Or they have the forms but no internet to submit on the electronic system, so they do paper, and the paper sits in a pile."

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Paper IDSR form sat at facility   │
│   for two weeks before reaching     │
│   sub-county"                       │
│                        — Sarah      │
└─────────────────────────────────────┘
```

**Joseph** (writing immediately):

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Electronic IDSR submission failed │
│   due to no network at facility"    │
│                        — Joseph     │
└─────────────────────────────────────┘
```

Sarah is now placing more stickies, gaining confidence:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "CHWs distributed ORS sachets from │
│   their own household stocks"       │
│                        — Sarah      │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "CHW household ORS stock was       │
│   exhausted within 4 days"          │
│                        — Sarah      │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "CHW supervisor requested          │
│   resupply but was told 'no budget  │
│   line for emergency CHW supplies'" │
│                        — Sarah      │
└─────────────────────────────────────┘
```

**Dr. Amina** stares at that last one. "There's no budget line because it's not in the AWP. It's not in the AWP because nobody told me in June that November would flood."

She writes, standing now:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "AWP was finalized in June with    │
│   no climate risk consideration"    │
│                        — Dr. Amina  │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Budget reallocation request was   │
│   submitted to Governor's office"   │
│                        — Dr. Amina  │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Governor's office took 3 weeks    │
│   to approve budget reallocation"   │
│                        — Dr. Amina  │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Emergency supplementary budget    │
│   was requested from county         │
│   assembly (too late for response)" │
│                        — Dr. Amina  │
└─────────────────────────────────────┘
```

### Hotspots Emerge (1:18–1:30)

Alberto's voice: *"Where are people arguing? Where do you disagree? Put a pink sticky on those spots. Those are hotspots — we'll come back to them."*

Peter and Dr. Amina are standing at the wall. Peter points at Dr. Amina's "learned about forecast from newspaper" sticky.

**Peter**: "I need to push back on that. We do a Greater Horn of Africa Climate Outlook Forum every March and September. We present to county governments."

**Dr. Amina**: "You present to the County Commissioner. I have never been invited. Not once in four years."

**Peter**: "That's... that's not a KMD problem. That's county coordination."

**Dr. Wanjiku**: "It is a systemic problem. The climate services architecture in Kenya does not include the health sector as a first-class recipient. I have been saying this for two years at NCCAP meetings."

Pink hotspot goes up:

```
┌─────────────────────────────────────┐
│  🩷 HOTSPOT                         │
│                                     │
│  "Health sector not on climate      │
│   forecast distribution list"       │
│                                     │
│  [Peter vs Dr. Amina vs Wanjiku]    │
└─────────────────────────────────────┘
```

Meanwhile Raj is in a separate argument with the Engineer near the right side of the wall.

**Engineer**: "So when the data_agent pulls historical disease data, it would connect to DHIS2 via the API and—"

**Raj**: "Stop. Stop right there. Which DHIS2 instance? The county one or the national one? Because they're not synchronized. Kilifi's county instance was last synced to national in... October? Maybe August. And the API is locked down. You need MoH approval for API access, which takes three months minimum, and even then you get read-only on aggregate data, not line-listed."

```
┌─────────────────────────────────────┐
│  🩷 HOTSPOT                         │
│                                     │
│  "DHIS2 data access: which          │
│   instance? API permissions?        │
│   Sync lag between county and       │
│   national?"                        │
│                                     │
│  [Raj vs Engineer]                  │
└─────────────────────────────────────┘
```

**Engineer**: "What if we don't connect to DHIS2 at all? What if we use the climate data to predict risk and the user validates against their own—"

**Raj**: "Then how do you establish the baseline? How do you show that your prediction is better than what they already know? You need the historical disease data to train anything."

The Engineer writes quietly:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Historical baseline was manually  │
│   assembled from multiple data      │
│   sources"                          │
│                        — Engineer   │
└─────────────────────────────────────┘
```

Raj snorts but doesn't disagree.

Joseph and Sarah are at the middle of the wall. Joseph points at Sarah's stickies about CHWs and field reality.

**Joseph**: "These are the events nobody else sees. This is the real surveillance system. WhatsApp groups and CHWs."

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "CHW WhatsApp group reported       │
│   spike in acute watery diarrhoea   │
│   3 days before first IDSR report"  │
│                        — Sarah      │
└─────────────────────────────────────┘
```

**Joseph**: "Three days. In cholera, three days is the difference between three cases and thirty."

More stickies go up in a rush:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "County health management team     │
│   held emergency meeting"           │
│                        — Dr. Amina  │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "ORS and Zinc tablets were         │
│   redistributed from another        │
│   sub-county's stock"               │
│                        — Dr. Amina  │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Net distribution was planned      │
│   for dry season but rains came     │
│   early — nets arrived after        │
│   malaria peak"                     │
│                        — Joseph     │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "CHAMNHA threshold was exceeded    │
│   — heat wave pushed preterm birth  │
│   risk above baseline"             │
│                        — Dr. Wanjiku│
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Maternity ward was overwhelmed    │
│   during heat event — no advance    │
│   staffing adjustment made"         │
│                        — Sarah      │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Post-disaster assessment          │
│   documented 'lessons learned'      │
│   that were not actioned"           │
│                        — Dr. Wanjiku│
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Water treatment chemicals were    │
│   requested from Public Health      │
│   office after contamination was    │
│   confirmed"                        │
│                        — Joseph     │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "KMD 7-day forecast was checked    │
│   by nobody in health department"   │
│                        — Peter      │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Donor-funded climate-health       │
│   pilot ended and system was        │
│   not maintained"                   │
│                        — Dr. Wanjiku│
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Action Repository was consulted   │
│   to find appropriate intervention" │
│                        — Engineer   │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "Intervention cost was calculated  │
│   and compared to available budget" │
│                        — Engineer   │
└─────────────────────────────────────┘
```

Peter places a final cluster:

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "March seasonal outlook predicted  │
│   above-normal long rains for       │
│   coastal counties"                 │
│                        — Peter      │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "September outlook predicted       │
│   enhanced short rains (IOD+)"      │
│                        — Peter      │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🟧 DOMAIN EVENT                    │
│                                     │
│  "County-specific downscaled        │
│   forecast was produced (but only   │
│   shared at GHACOF workshop)"       │
│                        — Peter      │
└─────────────────────────────────────┘
```

More pink hotspots appear:

```
┌─────────────────────────────────────┐
│  🩷 HOTSPOT                         │
│                                     │
│  "Who translates rainfall           │
│   anomaly into health risk?         │
│   NOBODY does this currently."      │
│                                     │
│  [Everyone staring at the gap]      │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🩷 HOTSPOT                         │
│                                     │
│  "CHW intelligence vs formal        │
│   surveillance: parallel systems,   │
│   no integration"                   │
│                                     │
│  [Sarah vs Joseph]                  │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🩷 HOTSPOT                         │
│                                     │
│  "Supply chain lead time (6-8 wks)  │
│   vs outbreak detection speed:      │
│   supplies always arrive late"      │
│                                     │
│  [Joseph vs Dr. Amina]              │
└─────────────────────────────────────┘
```

```
┌─────────────────────────────────────┐
│  🩷 HOTSPOT                         │
│                                     │
│  "AWP locked in June. Climate info  │
│   arrives March & September.        │
│   What can actually be changed?"    │
│                                     │
│  [Dr. Amina vs Dr. Wanjiku]         │
└─────────────────────────────────────┘
```

The wall is chaos. Forty-two orange stickies and six pink hotspots scattered across eight metres of paper. Some are clustered, some isolated. Peter's KMD stickies float on the far left with nothing connecting to them. Sarah's field-reality stickies are a dense knot near the bottom-right. Dr. Amina's budget and planning stickies form a separate constellation. Joseph's surveillance events are scattered across the middle.

Alberto says: *"Good. This is beautiful chaos. Don't touch anything. I'm taking a photo."*

The co-facilitator photographs the wall from three angles. Everyone stares at the mess. The Engineer is making notes on a laptop. Sarah is looking at the wall with an expression that says: this is the first time anyone has put what I know next to what they know.

Alberto: *"Break. Fifteen minutes. Coffee. Don't move the stickies."*

---

## PHASE 2: TIMELINE ENFORCEMENT (2:00–3:00)

Everyone is back. Coffee cups on the table. Alberto's voice: *"Now. Arrange everything left to right in time order. Find the story. Left is earliest, right is latest. Move the stickies. Argue. But find the sequence."*

### The First Argument: Where Does It Start? (2:00–2:12)

Nobody moves for five seconds. Then Peter and Dr. Amina both reach for the wall at the same time.

**Peter** grabs his "Seasonal rainfall outlook was issued by KMD" sticky and moves it to the far left. "This is where it starts. The forecast."

**Dr. Amina** shakes her head. "No. It starts here." She takes "AWP was finalized in June" and places it to the left of Peter's forecast. "The planning cycle starts before the climate signal. That's the whole problem. I've already committed the budget before you tell me what's coming."

**Dr. Wanjiku**: "She's right. The fiscal year starts July 1. The AWP is drafted in April, May, finalized June. The March outlook is technically available, but—"

**Peter**: "The March outlook IS available in March! Two months before the AWP is finalized!"

**Dr. Amina**: "Available to whom? Available on a KMD website? Available in a format that tells me how many cholera kits to order? Peter, I don't speak tercile probability. Nobody in my office does."

Silence. Peter stands there holding his sticky.

**Engineer** (carefully): "So the March outlook IS issued before the AWP deadline. The information exists in time. It's the translation that's missing."

```
┌─────────────────────────────────────┐
│  🩷 HOTSPOT                         │
│                                     │
│  "TRANSLATION GAP: forecast exists  │
│   in time for planning, but no one  │
│   converts it to health actions"    │
│                                     │
│  [THE pivotal gap — CHART lives     │
│   HERE]                             │
└─────────────────────────────────────┘
```

Alberto (from the screen): *"Mark that. That pink sticky might be the most important thing on the wall. Keep going."*

### Discovery of Parallel Timelines (2:12–2:30)

Joseph has been reorganizing his surveillance stickies. He steps back and says: "This isn't one timeline. There are at least three things happening at different speeds."

He runs his finger along the wall: "There's Peter's timeline — forecasts, twice a year. There's Dr. Amina's timeline — the budget cycle, once a year. And then there's mine — disease events, which happen whenever they happen. Could be any week."

**Sarah**: "Four. You're forgetting the rain itself. The actual rain doesn't follow the planning calendar."

Joseph nods. He grabs a marker and draws four horizontal lines across the butcher paper, top to bottom:

```
─── PLANNING CYCLE (AWP / Budget) ──────────────────────────────────────
─── CLIMATE CYCLE (KMD Forecasts / Actual Weather) ─────────────────────
─── DISEASE CYCLE (Surveillance / Outbreaks) ────────────────────────────
─── SUPPLY CHAIN (KEMSA / Commodities) ─────────────────────────────────
```

**Dr. Wanjiku**: "Five. NCCAP reporting is its own cycle. Quarterly."

Joseph adds a fifth line. Now people start moving stickies onto the correct swimlane.

**Peter** moves all his KMD stickies onto the Climate Cycle line. He places them carefully:

- **March**: "March seasonal outlook predicted above-normal long rains"
- **September**: "September outlook predicted enhanced short rains"
- And between them, nothing. A gap of six months.

**Peter** (staring at his own stickies, spaced out on the line): "I never realized how... sparse this looks. From the health side. We do monthly updates, dekadal bulletins, but the actionable seasonal signal — it's really twice a year."

**Dr. Amina** places her stickies on the Planning Cycle line:

- **April-May**: "AWP was drafted by county health management team"
- **June**: "AWP was submitted to County Treasury"
- **July 1**: "New fiscal year began"
- And then much later, after something has gone wrong: "Budget reallocation request was submitted to Governor's office" and "Governor's office took 3 weeks to approve"

She stands back. The gap between "AWP submitted" in June and "budget reallocation" in November is a vast empty stretch of paper.

**Dr. Amina**: "That's my year. I plan in June. Then I react in November. There's nothing in between. No mechanism to adjust."

### The Alignment Problem Becomes Visible (2:30–2:48)

Joseph places disease events on the Disease Cycle line. They cluster unpredictably but with a pattern:

- **April-June**: Malaria cases rising (long rains)
- **November-December**: Cholera and diarrhoeal disease (short rains)
- **January-February**: Heat-related illness (dry season)

He draws small arrows up from the disease stickies toward the Climate Cycle line. "These are lagged. The rain comes, and then three to six weeks later, the mosquitoes breed, and then two weeks after that, the cases come. So a March forecast of heavy long rains in April should tell me to expect malaria surge in late May or June."

**Peter** walks to the wall and physically moves his March forecast sticky. He draws an arrow from it pointing right and down, toward Joseph's malaria cluster. The arrow is long — spanning about two months of wall space.

**Peter**: "So my March outlook... if someone caught it and translated it... you'd have eight weeks of lead time before the malaria surge."

**Joseph**: "Eight weeks. That's exactly the KEMSA delivery time."

Everyone in the room looks at the same spot on the wall. Peter's forecast on the left. Joseph's disease surge on the right. Eight weeks of blank paper between them.

**Dr. Amina** (very quietly): "If I had known in March, I could have ordered in March. The supplies would arrive by May. Before the cases."

She sits down. She puts both hands flat on the table.

**Dr. Amina**: "I have been the County Health Director for Kilifi for four years. I have managed three cholera outbreaks and two malaria surges. Every single time, I was reactive. Every single time, the supplies came late. Every single time, I wrote a report afterward saying 'we should have pre-positioned.' And nobody ever told me that the information to do it was sitting in a PDF on the KMD website in March."

Peter looks uncomfortable. "The information is... it's probabilistic. It says 'above-normal rainfall is likely.' It doesn't say—"

**Dr. Wanjiku**: "It doesn't say 'order cholera kits.' That's the point. That translation — from 'above-normal rainfall likely' to 'order cholera kits for coastal sub-counties by end of March' — that's what doesn't exist."

The Engineer writes on a large yellow sticky and places it in the gap between Peter's forecast and Joseph's disease events:

```
┌─────────────────────────────────────┐
│  🟨 SYSTEM BOUNDARY                 │
│                                     │
│  >>> CHART LIVES HERE <<<           │
│                                     │
│  INPUT: KMD seasonal outlook        │
│  + historical disease-climate       │
│    correlation                      │
│  + CHAMNHA thresholds               │
│  + Action Repository (110+ costed   │
│    interventions)                   │
│                                     │
│  OUTPUT: "Order X cholera kits for  │
│  sub-counties Y, Z by [date].      │
│  Estimated cost: KES [amount].      │
│  Budget line: [reference]."         │
│                                     │
│                        — Engineer   │
└─────────────────────────────────────┘
```

### Peter's Disconnection (2:48–2:55)

Peter is still standing at the wall. He has moved all five of his KMD stickies to the Climate Cycle line. They sit there in their correct temporal positions — March, September, and the county-specific downscaled forecast that was shared "only at the GHACOF workshop."

He traces with his finger from each of his stickies downward, toward the other timelines. None of them connect to anything. No arrows lead from his forecasts to any planning event, any disease response, any supply chain decision.

**Peter**: "My stickies are an island."

Nobody contradicts him.

**Peter**: "We produce the outlook. We hold the press conference. We send it to the commissioners. And then..." He gestures at the blank wall below his stickies. "Nothing. It just... stops."

**Sarah** (from where she's been rearranging her CHW stickies on the Disease Cycle line, below the formal surveillance events): "We see the rain. We see the flooding. We report it. It goes up." She points to her stickies. "Your forecast comes down from the top. Our reports go up from the bottom. They never meet in the middle."

She draws two arrows on the paper. One pointing down from Peter's forecast. One pointing up from her CHW reports. They end in the same blank space, not touching.

### Temporal Constraints Crystallize (2:55–3:00)

Alberto: *"Before we stop — I want someone to write the hard deadlines on the wall. The things that cannot move."*

Dr. Amina takes a red marker and writes directly on the butcher paper:

```
FIXED DEADLINES:
- AWP submission: June (for July 1 fiscal year)
- KMD seasonal outlook: March, September
- KEMSA standard delivery: 6-8 weeks from order
- KEMSA emergency delivery: 4-6 weeks (if approved)
- Governor budget reallocation approval: 2-4 weeks
- NCCAP quarterly reports: March, June, September, December
- County Assembly supplementary budget: minimum 6 weeks to approve
```

Joseph adds:

```
- IDSR weekly report: due Monday for previous week
- Outbreak notification: immediate (in theory), 24-72 hrs (in practice)
- Cholera case fatality: can kill within hours of onset
```

Peter adds:

```
- GHACOF outlook forum: February (for March-May season)
- Downscaled county forecast: available ~2 weeks after GHACOF
- 7-day forecast: updated daily (but not used by health)
```

Everyone stands back and looks at the wall. The four swimlanes. The stickies in rough temporal order. The red deadline annotations. The pink hotspots. And the yellow sticky in the centre of the gap — where CHART lives.

**Dr. Amina** (turning to the Engineer): "So. The March forecast comes out. My AWP isn't due until June. That means I have a three-month window — March, April, May — where if someone told me what the forecast means for health, I could actually put it in the plan. I could budget for it. I wouldn't need the Governor's emergency approval. I wouldn't need a supplementary budget from the assembly. It would just be... in the plan."

**Engineer**: "That's the window. March outlook translates to health risk. Risk maps to interventions from the Action Repository. Interventions have costs. Costs go into the AWP in April. AWP is submitted in June with climate-informed budget lines. KEMSA order goes out in June or July. Supplies arrive August or September, before the short rains."

**Dr. Amina**: "And for the September outlook — it's too late for the AWP. But I could use it to trigger pre-positioning from existing stock. Or a Governor reallocation request with enough lead time."

**Joseph**: "Two windows. Two different workflows. The March window is for planning. The September window is for rapid adjustment."

**Dr. Wanjiku**: "And both of them give me something to put in the NCCAP quarterly report. Proactive climate adaptation action by the health sector. Not 'lessons learned from last outbreak.' Actual forward planning."

Alberto: *"Stop there. That's your story. Two windows. One system. The thing in the middle that doesn't exist yet. That's what you're building. Photograph the wall."*

The co-facilitator takes twelve photos. Dr. Amina is still standing at the wall, her hand resting on the yellow CHART sticky, staring at the three-month gap between the March forecast and her June AWP deadline. The gap she never knew she had.

---



# Phase 3: Process Modeling — The To-Be World (3:00–4:30)

---

The facilitator peels open four new packs of sticky notes and fans them across the table like a card dealer. Blue, yellow, purple, green. He taps each color against the wall next to the timeline from Phase 2.

"New colors, new meaning. Blue is a **command** — something someone or something decides to do. Yellow is an **actor** — a human role or team that issues the command. Purple is a **policy** — a business rule that constrains what can happen. Green is an **external system** — something outside CHART that we depend on or feed into."

He uncaps a fresh marker and draws a bracket around the gap they discovered in Phase 2 — the empty space between the orange sticky reading *"KMD seasonal outlook issued"* and the one reading *"AWP budget drafted."*

"We found the gap. Now let's fill it. What SHOULD happen between the forecast and the budget? Model the process that doesn't exist yet."

He steps back from the wall.

Nobody moves for four seconds. Then everyone moves at once.

---

## Part A: The "Happy Path" (3:00–3:30)

### The Forecast Enters the System

Peter is already at the wall. He peels a green sticky — external system — and writes in neat block capitals:

> 🟩 **KMD Climate Outlook Portal (ASEAC format)**

He places it at the far left of the gap, just after the existing orange event sticky.

"Let me be precise about what I can give you and when. The Seasonal Outlook comes out three times a year — March for MAM rains, July for JJAS, October for OND. It's issued after the ASEAC meeting — that's the Arid and Semi-Arid Lands Early Warning Bulletin plus the Greater Horn consensus. The format is a tercile probability map. Above normal, near normal, below normal rainfall. It covers the whole country at the county level."

He peels a blue command sticky and writes:

> 🟦 **Fetch seasonal forecast**

"But here's my question back to the room." He holds the sticky in the air without placing it. "Who triggers this? Does CHART go pull it automatically when it's published? Or does someone press a button?"

Raj leans forward. "If it's published on the KMD portal, I can write a scraper. Or better — Peter, do you have an API?"

Peter shakes his head. "We have a PDF. Sometimes a spreadsheet. Sometimes both, and they don't match."

The Engineer writes on a green sticky:

> 🟩 **KMD FTP / Portal (PDF + XLS, inconsistent format)**

"So the first command is actually two steps," the Engineer says. He writes a second blue sticky:

> 🟦 **Parse forecast into structured risk probabilities per county**

"This is extraction. We take Peter's PDF, we pull out the tercile probabilities for each of the 47 counties, and we structure it. This is a software task, not an AI task. Pattern matching, maybe some OCR if the PDF is scanned."

Peter nods slowly. "Sometimes it is scanned. When the photocopier is working better than the email."

A small laugh. The Engineer places both blue stickies in sequence and adds a yellow actor sticky above them:

> 🟨 **CHART System (automated)**

"No human triggers this. When the outlook is published — and we detect it — we pull and parse. If parsing fails, we alert someone." He glances at Peter. "You. We alert you."

Peter writes a purple policy sticky and slaps it beneath the blue commands:

> 🟪 **Forecast must include tercile probabilities; if narrative-only, flag for manual extraction**

"Because sometimes the Outlook is qualitative. 'Expect enhanced rainfall in the Lake Victoria basin.' That's not a probability. If that's all we have, someone human has to translate it."

Dr. Wanjiku picks up her pen. "Who is 'someone human'?"

Peter taps his own chest. "Me. Or my team. We're the only ones who can interpret the synoptic discussion."

A yellow sticky goes up:

> 🟨 **KMD Forecast Desk Officer (manual fallback)**

The facilitator nods. "Good. First command placed. What happens next?"

---

### The Translation Layer

Dr. Amina stands. She has been studying the gap, arms crossed, thinking in the language of budget justification.

"What I need — what I have never had — is a document that says: *this forecast means this risk, for these diseases, at these facilities, and here is what it will cost to prepare versus what it will cost if we don't.* That document does not exist anywhere in government. Not at national. Not at county. Nowhere."

She picks up a blue sticky.

> 🟦 **Translate climate signal to health risk**

She places it directly after the parsing step and then turns to the room. "This is the step nobody does today. This is why we're all here. The forecast says 'above-normal rainfall, 45% probability, coastal region.' What does that mean for Kilifi County Hospital? What does it mean for Malindi Sub-County? For Bamba? For the dispensaries in Ganze that flood every long rains?"

Joseph picks up a green sticky and adds it below:

> 🟩 **DHIS2 — Historical morbidity data (malaria, cholera, URTI, diarrheal disease)**

"You need the baseline," he says. "If you want to say 'above-normal rainfall increases malaria incidence,' you need to show the historical correlation. That means pulling the last five to ten years of outpatient data from DHIS2, by facility, by epidemiological week, and overlaying it against rainfall anomalies."

Raj immediately writes a purple policy sticky:

> 🟪 **If DHIS2 reporting completeness < 70% for a facility, exclude from automated analysis; flag for manual review**

"I'm putting this up now because I know what's coming," Raj says. "Half the facilities in Tana River County haven't reported consistently since 2019. If CHART builds a malaria risk score on garbage data, it will produce garbage recommendations, and people will blame the system."

Dr. Amina points at him. "What's the threshold? Why seventy percent?"

"WHO standard for surveillance data quality. Below seventy percent reporting completeness, you can't draw epidemiological conclusions."

The Engineer is writing on a blue sticky, but he holds it up before placing it.

> 🟦 **"Translate climate signal to health risk"**

"I want to be specific about what this command actually does. This is where the AI lives. Let me describe what I think happens inside this box, and you tell me if I'm wrong."

He grabs a blank sheet of paper and starts sketching.

"Input one: structured tercile forecast for a specific county. Above-normal rainfall, 45% probability, MAM 2026, Kilifi County. Input two: historical disease incidence from DHIS2 for that county — malaria cases, cholera cases, diarrheal disease, respiratory infections — correlated with past rainfall anomalies. Input three: contextual factors — does this county have a coastline? Flood-prone areas? Refugee camps? Irrigated agriculture that creates breeding sites?"

He taps the paper. "The LLM's job is to synthesize these into a risk narrative. Not a number. A narrative with structured outputs. Something like: *'Above-normal MAM rainfall in Kilifi County has historically been associated with a 30-40% increase in confirmed malaria cases in weeks 18-26, concentrated in Ganze and Magarini sub-counties. Cholera risk is elevated in peri-urban Kilifi Town due to flooding of pit latrines. Historical confidence: moderate, based on 7 of 10 years showing this pattern.'*"

Dr. Wanjiku is nodding. "That's good. But who validates that the historical correlation is real and not a hallucination?"

"That's why we have the RAG layer," the Engineer says. "We don't ask the LLM to invent correlations. We feed it the actual data — the actual DHIS2 numbers, the actual rainfall records — and we ask it to describe patterns that exist in the data. If there's no pattern, it should say so."

Peter adds a purple sticky:

> 🟪 **If confidence < 60%, flag output as "uncertain — expert review required"**

Dr. Amina immediately objects. "Sixty percent of what? Confidence in the forecast? Confidence in the correlation? Confidence in the recommendation? These are different things."

Peter: "I mean the forecast confidence. If the tercile probability is below sixty percent — meaning the most likely category is only slightly more likely than the others — then the forecast is weak. The signal is weak. Anything built on it is speculative."

Dr. Amina: "But Peter, the OND 2023 outlook for the coast was fifty-five percent above normal, and it was the worst flooding in a decade. If we'd set a sixty percent threshold, we'd have ignored it."

Peter pauses. He pulls the purple sticky off the wall, crosses out 60%, and writes a revised version:

> 🟪 **If dominant tercile probability < 50%, flag as "low confidence signal." If 50-65%, flag as "moderate confidence — recommend precautionary measures." If > 65%, flag as "high confidence — full intervention planning recommended."**

"Three tiers," he says. "And even the low confidence tier still triggers a flag. It doesn't trigger silence."

Dr. Amina nods. "That I can work with. Because I can take 'moderate confidence' to the county assembly. I cannot take 'the computer isn't sure.'"

The Engineer updates the policy sticky's placement and adds a note beneath it:

> 🟪 **Confidence tiering applies to the climate signal only. Health risk confidence is assessed separately based on data quality + evidence strength.**

---

### Matching Risks to Interventions

Joseph stands up. He's been waiting for this part.

"Once we know the risks, we need to match them to interventions. And I don't mean vague interventions like 'strengthen malaria prevention.' I mean: *For Bamba Health Centre, which serves 12,000 people in a flood-prone area, pre-position 2,400 RDTs, 1,200 doses of ACTs, 500 ORS packets, and 50 cholera kits. Delivery deadline: Week 10, before the rains start in Week 12.*"

He writes a blue command sticky:

> 🟦 **Match risks to interventions (from Action Repository)**

And a green sticky:

> 🟩 **Action Repository — evidence-based intervention database (climate-health pairs)**

"This repository doesn't exist yet," the Engineer says. "We need to build it. What goes in it?"

Joseph starts listing. Dr. Amina joins. Sarah, who has been quiet, suddenly speaks up.

"I'll tell you what goes in it. For malaria, during high-rainfall seasons: community-level larviciding — but only in areas with stagnant water within 500 meters of homesteads. Mass net distribution — but only if the last distribution was more than two years ago. IRS — but only if the sub-county has a trained spray team. RDT and ACT pre-positioning at facility level."

She peels a purple sticky:

> 🟪 **If cold-chain required but facility has no functional cold-chain, exclude intervention and flag alternative**

"This is real," she says. "You cannot recommend we pre-position IV artesunate at a dispensary that has no refrigerator. Or where the refrigerator hasn't worked since March. CHART has to know which facilities have cold-chain and which don't. Otherwise you're sending supplies that will spoil."

The Engineer writes another green sticky:

> 🟩 **Kenya MFL (Master Facility List) — facility attributes, cold-chain status, staffing level**

Raj: "The MFL is maintained by the Division of Health Informatics. It's... partially accurate. Cold-chain status was last updated in 2022 for most counties."

Sarah: "Then CHART should ask me. I know which facilities have working fridges. I know which ones have been broken for two years. Let me update it."

A yellow actor sticky goes up:

> 🟨 **CHW Supervisor (facility ground-truth validation)**

And a blue command:

> 🟦 **Validate facility readiness data (quarterly)**

The facilitator points at the wall. "We're building something. Let's keep going. What does the output look like?"

---

### Generating the Draft Plan

Dr. Amina takes control. She picks up a blue sticky and holds it like a gavel.

> 🟦 **Generate draft adaptation plan (AWP-compatible format)**

"This is the document I take to the county assembly health committee. It has to look like every other budget document they've seen. It has to use the county government format. Line items. Budget codes. Justification narratives. If it looks like a 'tech report' or a 'science document,' they will not read it."

She starts listing the required elements, counting on her fingers:

"One: Executive summary — two paragraphs, plain language. 'Based on KMD seasonal outlook and historical disease patterns, Kilifi County faces elevated malaria and cholera risk during the MAM 2026 season. This plan outlines preparedness interventions estimated at KES 4.2 million, compared to an estimated response cost of KES 18 million if no action is taken.'

"Two: Risk summary table — disease, sub-county, risk level, confidence level.

"Three: Intervention table — intervention, facility/sub-county, quantity, unit cost, total cost, budget code, procurement timeline, KEMSA order reference.

"Four: Cost of inaction comparison."

She peels a purple sticky and places it with force:

> 🟪 **Must include cost-of-inaction comparison (estimated response cost if no preparedness action taken)**

"This is non-negotiable. When I go to the Governor and say 'I need four million shillings for malaria preparedness,' the first question is always 'why should we spend money on something that hasn't happened yet?' The only answer that works is: 'Because if we don't, we'll spend eighteen million on emergency response, plus thirty-seven people will die, and the Daily Nation will put it on the front page.'"

Dr. Wanjiku writes a purple sticky:

> 🟪 **CHART never auto-submits to county assembly. All outputs are DRAFT for human review.**

"I want to be absolutely clear about this," she says. "This system advises. It does not decide. It does not submit. It does not commit government funds. A human reviews, modifies, approves, and submits. Always."

The Engineer nods emphatically. "Agreed. That's a hard architectural constraint. The system produces drafts. A human owns the submit action."

He places a yellow actor sticky:

> 🟨 **County Health Director (plan owner)**

And writes beneath it in small letters: *"Accountable for all submissions. CHART is a tool, not an authority."*

---

### The Technical Working Group Review

Dr. Wanjiku takes over. She's the governance person, and this is where governance lives.

"The draft plan goes to the county Technical Working Group. Every county has one — or is supposed to. Health, environment, water, agriculture, meteorology. They review the plan, challenge the assumptions, and approve or reject."

Blue stickies:

> 🟦 **Review with TWG**
> 🟦 **Approve / Reject / Modify plan**

Yellow stickies:

> 🟨 **County TWG (multi-sector)**

Purple sticky:

> 🟪 **TWG quorum of 3+ sector representatives required for approval**

"Why three?" Joseph asks.

"Because if only health reviews it, it's just a health plan. If health, water, and meteorology review it, it's a multi-sector adaptation plan. That matters for NCCAP reporting. That matters for Green Climate Fund proposals. That matters for everything."

Peter adds: "And I want a meteorologist on that TWG. Not just receiving the plan for information — actually reviewing whether the climate interpretation is correct."

A new yellow sticky:

> 🟨 **County Meteorological Officer (TWG member — forecast validation)**

---

### Into the Budget and Supply Chain

Joseph places the final command stickies in the happy path:

> 🟦 **Insert approved plan into AWP budget**
> 🟦 **Place supply pre-positioning order with KEMSA**

Green stickies:

> 🟩 **IFMIS (Integrated Financial Management Information System)**
> 🟩 **KEMSA Order Management System**

"Once the TWG approves, two things happen in parallel," Joseph says. "The budget allocation gets entered into IFMIS — that's the county financial system. And the supply order goes to KEMSA. KEMSA needs the order six to eight weeks before the delivery date. Which means..." He traces the timeline backward. "If MAM rains start Week 12, I need delivery by Week 10, which means the KEMSA order goes in by Week 2 at the latest. Which means TWG approval by Week 1. Which means the draft plan must be ready by Week 50 of the previous year. Which means the KMD OND outlook — no, wait, the March outlook comes out in February..."

He stops. He's staring at the timeline.

"The March-to-May forecast is issued in late February. KEMSA needs the order by early January. The plan needs to be approved before the forecast exists."

Silence.

Peter: "The forecast discussion starts in early February. Sometimes late January. But the formal outlook isn't issued until the third or fourth week of February."

Dr. Amina: "So we need to use the *previous* season's data and the pre-season discussion notes to start the draft plan, and then update it when the formal outlook arrives?"

The Engineer is already modifying the process model on the wall. He draws a dotted arrow from an earlier point — the October outlook — looping forward.

"Two-pass system," he says. "First pass: use the OND outlook plus historical baselines to generate a *preliminary* plan in November-December. This is enough for KEMSA pre-positioning of standard items — RDTs, ORS, bed nets — things you need every rainy season regardless. Second pass: when the MAM outlook is issued in February, update the risk assessment and modify the plan. Add cholera-specific interventions if the signal is strong enough. Adjust quantities up or down."

He writes two new blue stickies:

> 🟦 **Generate preliminary plan (based on climatological baseline + OND outlook)**
> 🟦 **Update plan with MAM-specific forecast (when available)**

Joseph exhales. "That... actually works. Because the baseline items — RDTs, ACTs, ORS — I need those every season. The forecast just changes the quantities and the priority sub-counties."

Purple sticky from Joseph:

> 🟪 **Baseline supplies (RDTs, ORS, ACTs) ordered on climatological average regardless of forecast. Forecast adjusts quantities ±30% and prioritizes sub-counties.**

Dr. Amina is smiling for the first time in the workshop. "So the system doesn't wait for the forecast to start working. It starts from the historical pattern and refines."

"Exactly," the Engineer says. "The AI doesn't replace the forecast. It integrates the forecast into an existing planning cycle that *already should be happening* but doesn't happen because nobody connects the dots."

---

### The Process Model Takes Shape

The facilitator steps back. The wall now has a clear sequence. He reads it aloud, pointing to each sticky:

```
                        THE HAPPY PATH — CHART PROCESS MODEL
                        ═════════════════════════════════════

  🟩 KMD Portal          🟩 DHIS2              🟩 MFL              🟩 Action
  (PDF/XLS)              (Morbidity)           (Facilities)         Repository
      │                      │                      │                    │
      ▼                      ▼                      ▼                    │
 ┌─────────┐           ┌──────────┐          ┌───────────┐              │
 │🟦 Fetch  │           │🟦 Pull   │          │🟦 Validate│              │
 │ forecast │           │ baseline │          │ facility  │              │
 │          │           │ epi data │          │ readiness │              │
 └────┬─────┘           └────┬─────┘          └─────┬─────┘              │
      │                      │                      │                    │
      │    🟪 If parse fails,│    🟪 If <70%        │                    │
      │    manual extraction │    completeness,     │  🟪 If cold-chain  │
      │                      │    exclude facility  │  broken, exclude   │
      │                      │                      │  cold-chain items  │
      ▼                      ▼                      ▼                    │
 ┌─────────┐           ┌──────────────────────────────┐                  │
 │🟦 Parse  │           │  🟦 Translate climate signal │◄─────────────────┘
 │ into     │──────────▶│     to health risk           │
 │ struct.  │           │                              │
 │ data     │           │  ┌────────────────────────┐  │
 └──────────┘           │  │ 🟨 CHART AI ENGINE     │  │
                        │  │    (LLM + RAG + Data)  │  │
                        │  └────────────────────────┘  │
                        │                              │
                        │  🟪 Confidence tiering:      │
                        │  <50% = low, 50-65% = mod,   │
                        │  >65% = high                  │
                        └──────────────┬───────────────┘
                                       │
                                       ▼
                        ┌──────────────────────────────┐
                        │ 🟦 Match risks to            │
                        │    interventions              │
                        │                              │
                        │ 🟪 Baseline supplies always;  │
                        │    forecast adjusts ±30%      │
                        └──────────────┬───────────────┘
                                       │
                                       ▼
                        ┌──────────────────────────────┐
                        │ 🟦 Generate draft             │
                        │    adaptation plan            │
                        │                              │
                        │ 🟪 AWP format required        │
                        │ 🟪 Must include cost of       │
                        │    inaction comparison        │
                        │ 🟪 NEVER auto-submit          │
                        └──────────────┬───────────────┘
                                       │
                            🟨 County Health Director
                               (plan owner)
                                       │
                                       ▼
                        ┌──────────────────────────────┐
                        │ 🟦 Review with TWG            │
                        │                              │
                        │ 🟨 County TWG (multi-sector)  │
                        │ 🟨 County Met Officer          │
                        │                              │
                        │ 🟪 Quorum of 3+ sectors       │
                        └──────────────┬───────────────┘
                                       │
                              ┌────────┼────────┐
                              ▼        ▼        ▼
                          APPROVE   MODIFY   REJECT
                              │        │        │
                              │    (loop back)  (end)
                              │
                              ▼
                 ┌────────────────────────────┐
                 │  🟦 Insert into AWP budget  │──▶ 🟩 IFMIS
                 │  🟦 Place KEMSA order       │──▶ 🟩 KEMSA OMS
                 │                            │
                 │  🟪 KEMSA order ≥ 6 weeks   │
                 │     before delivery date    │
                 └────────────────────────────┘
```

"That," says Dr. Amina, "is the process that doesn't exist."

"Not yet," the Engineer says.

"Not *yet,*" she agrees.

---

## Part B: The "Unhappy Paths" (3:30–4:00)

The facilitator pulls out red sticky notes — a color no one has seen yet.

"Red is for **hotspots** — things that can go wrong. I want you to break this beautiful happy path. Every person in this room: tell me how this fails."

### Raj's Nightmare: The Data Isn't There

Raj goes first, because he's been bracing for this.

"Tana River County. Forty-two health facilities. Twelve of them reported consistently to DHIS2 in 2024. Twelve out of forty-two. That's twenty-nine percent reporting completeness. My seventy-percent policy just excluded the entire county."

He places a red sticky:

> 🔴 **DHIS2 data missing for entire county/sub-county — system cannot generate risk assessment**

"And it's worse than missing. Sometimes the data is there but wrong. Kilifi County Hospital reported zero malaria cases in June 2023. Zero. During peak season. Someone entered the data into the wrong reporting period. It went into DHIS2 as June, but it was actually January through March, bulk-entered six months late."

Another red sticky:

> 🔴 **DHIS2 data present but incorrect — system generates wrong risk assessment with high confidence**

"That second one is more dangerous," the Engineer says. "Missing data, we can detect. Wrong data that looks right — that's a silent failure."

Dr. Amina: "So what do we do?"

Raj thinks for a moment. "Anomaly detection. If CHART is pulling five years of malaria data for Kilifi, and one month shows zero cases when every other year shows two thousand, flag it. Don't silently include it. Don't silently exclude it. Flag it and say: *'Anomalous data point detected for Kilifi County Hospital, June 2023. Zero malaria cases reported against a five-year average of 1,847. This data point has been excluded from the baseline calculation. Recommend verification with sub-county health records officer.'*"

The Engineer writes a purple policy:

> 🟪 **If any facility-month data point deviates > 2 standard deviations from its 5-year mean, flag as anomalous. Exclude from automated baseline. Include explanation in draft plan.**

Joseph adds: "And for counties with less than seventy percent reporting — we don't just say 'no data.' We fall back to sub-county aggregate data. Or county aggregate. Or we use the nearest county with similar epidemiological profile as a proxy. Kilifi and Kwale are similar. Tana River and Garissa are similar. We can build a similarity index."

A new blue command:

> 🟦 **If facility-level data insufficient, cascade: facility → sub-county → county → epidemiological proxy county**

Purple policy:

> 🟪 **If proxy data used, plan must state: "Based on proxy data from [County X]. Actual risk may differ. On-the-ground validation recommended before KEMSA order finalized."**

---

### Peter's Fear: The Forecast Is Wrong

Peter stands up slowly. He has been dreading this conversation.

"The March 2024 MAM outlook for the coast. We said near-normal to below-normal rainfall. Fifty-five percent probability of below normal. What happened? Above-normal rainfall. Flooding in Tana River. Cholera outbreak in Mombasa. The forecast was wrong."

Red sticky:

> 🔴 **Forecast tercile verification: wrong category realized**

"If CHART had existed then, it would have generated a plan saying 'low malaria risk, reduce pre-positioning.' And the opposite happened."

Dr. Amina: "This is why the cost-of-inaction comparison matters. Even when the forecast says low risk, we should show what happens if it's wrong. If we de-prioritize cholera preparedness for Kilifi based on a below-normal rainfall forecast, and the rains come heavy anyway, what's the damage?"

The Engineer: "We can build that in. Every plan includes a 'what-if-forecast-is-wrong' sensitivity section. Not a full alternative plan — but a table showing: if the opposite tercile realizes, here are the top three additional interventions that would be needed, and here is the estimated cost of emergency procurement versus pre-positioning."

Purple policy:

> 🟪 **Every plan must include a forecast-sensitivity section: "If the opposite tercile realizes, the following additional interventions would be needed at an estimated emergency procurement cost of KES [X]."**

Peter adds another dimension. "Also — I want to be clear about what the forecast *is.* It's not a prediction. It's a probability statement. When I say forty-five percent above normal, I'm saying it's the most likely category, but there's a fifty-five percent chance it's not. CHART has to communicate that correctly. Not 'the forecast says it will rain heavily.' Rather: 'the forecast indicates elevated probability of above-normal rainfall.'"

Purple policy:

> 🟪 **CHART must use probabilistic language reflecting the tercile forecast. Never say "will happen." Always say "elevated probability" or "increased likelihood."**

---

### Dr. Amina's Reality: The Governor Says No

Dr. Amina doesn't stand up. She leans back in her chair and speaks to the ceiling.

"The plan is perfect. The TWG approved it. The evidence is strong. The cost-of-inaction is terrifying. I take it to the county executive committee. The Governor looks at it and says: 'We're building a stadium this quarter. There's no money for mosquito nets.'"

Red sticky:

> 🔴 **County executive rejects approved plan due to political priorities**

"This happens," she says flatly. "Not sometimes. Often. In 2023, Kilifi County allocated eleven percent of the health budget to preventive services. The national target is thirty percent. The difference went to curative services — which are more visible, more politically rewarding. You can cut a ribbon on a new maternity wing. You can't cut a ribbon on 'we prevented a cholera outbreak.'"

Silence in the room.

"So what does CHART do?" the facilitator asks.

Dr. Amina sits forward. "Two things. First: the cost-of-inaction comparison has to be devastating. Not just financial — political. 'If this outbreak occurs and preparedness was rejected, the estimated media coverage based on similar events in Turkana 2022 and Mandera 2023 includes national news coverage for an average of 8 days.' I know that sounds cynical. It's how counties work."

The Engineer shifts uncomfortably. "Can we... quantify media coverage in a health tool?"

"You don't have to quantify it. You cite the precedent. 'In the 2022 Turkana cholera outbreak, where county preparedness funding had been reallocated, the national response cost was KES 42 million, and the Governor faced a Senate health committee inquiry.' That's a fact. That's in the public record. CHART can cite it."

Purple policy:

> 🟪 **Cost-of-inaction section should include precedent cases from Kenyan counties where similar risks materialized without preparedness, citing documented response costs and accountability actions.**

"Second thing," Dr. Amina continues. "When the Governor says no, I need CHART to help me find alternative funding. CFF — County Climate Finance. Green Climate Fund county allocations. DANIDA health system strengthening grants. USAID PMI funding for malaria. If the AWP won't fund it, maybe a partner will. But I need to know what's available and what the application requirements are before my window closes."

Blue command:

> 🟦 **If AWP insertion rejected, identify alternative funding sources with application deadlines**

Green sticky:

> 🟩 **Partner Funding Database (GCF, DANIDA, USAID PMI, WHO, UNICEF, etc.)**

Joseph mutters: "Now you're building a grant-writing AI."

Dr. Amina: "I'm building a survival tool."

---

### Joseph's Weekly Frustration: KEMSA Can't Deliver

Joseph takes the red stickies.

"I placed the order eight weeks ago. KEMSA confirmed. The delivery date was last Monday. It's Thursday. No delivery. No communication. When I call, the warehouse officer in Mombasa says the consignment is 'in transit.' It's been 'in transit' for two weeks."

Red sticky:

> 🔴 **KEMSA delivery delayed past critical pre-positioning window**

"Or worse: the delivery arrives, but it's wrong. I ordered 2,400 RDTs for *Plasmodium falciparum*. They sent 2,400 RDTs for *P. vivax*. Which is useless on the coast — *vivax* is less than five percent of our malaria cases."

Red sticky:

> 🔴 **KEMSA delivers wrong items / wrong specifications**

"What does CHART do about this?" Joseph asks. "It's not a data problem. It's a logistics problem."

The Engineer: "CHART can't fix KEMSA. But it can do two things. One: track the order status and alert you — and the TWG — if the delivery window is at risk. Two: trigger a contingency plan."

Blue command:

> 🟦 **If KEMSA delivery delayed > 1 week past due date, trigger contingency procurement alert**

"Contingency means what?" Joseph asks.

"Alternative sourcing. Mission for Essential Drugs and Supplies — MEDS. Direct facility-to-facility redistribution if neighboring counties have surplus. Emergency procurement through county own-source revenue."

Purple policy:

> 🟪 **If KEMSA delivery is >50% likely to miss the season-start deadline, system recommends: (1) escalation to KEMSA regional manager, (2) reallocation from lower-risk sub-counties, (3) alternative procurement via MEDS.**

Joseph: "I like the reallocation option. If Malindi is moderate risk and Ganze is high risk, and KEMSA only delivered to Malindi, redistribute from Malindi to Ganze. But that requires the Malindi sub-county pharmacist to agree."

Sarah: "Good luck with that."

Joseph: "Exactly. Which is why it needs to come from the county health director, not from a software system."

Yellow sticky added to the contingency pathway:

> 🟨 **County Health Director (authorizes inter-facility redistribution)**

---

### The Engineer's Question: No Evidence Available

The Engineer has been quiet during the political and logistical failures. Now he raises the question that's been nagging him.

"What happens when someone asks about a climate-health link that doesn't have good evidence? For example: Dr. Amina, you mentioned heat-related preterm birth earlier. Is there strong evidence that above-normal temperatures during OND in coastal Kenya increase preterm birth rates?"

Dr. Amina: "There's emerging evidence globally. A few studies from sub-Saharan Africa. Nothing specific to Kenya's coast."

"So if CHART is asked to generate a plan for heat-related maternal health interventions in Kilifi, what does it do? Make something up? Extrapolate from Bangladesh? Say nothing?"

Dr. Wanjiku: "It should say what it knows and what it doesn't. 'Limited evidence suggests a potential association between extreme heat events and adverse birth outcomes in sub-Saharan Africa (citation, citation). No Kenya-specific studies are available. The following interventions are recommended as no-regret measures based on general maternal health best practices, not climate-specific evidence: ensure adequate hydration supplies at ANC clinics, schedule community health visits during morning hours, provide heat-health messaging through existing ANC contacts.'"

Red sticky:

> 🔴 **Insufficient evidence for specific climate-health link in local context**

Blue command:

> 🟦 **If evidence insufficient, generate "no-regret" recommendations only + flag evidence gap for research**

The Engineer writes a critical purple policy:

> 🟪 **CHART must distinguish between: (a) evidence-based recommendations (strong local evidence), (b) extrapolated recommendations (evidence from analogous contexts), and (c) no-regret recommendations (good practice regardless of climate). Each recommendation must be labeled accordingly.**

"This is the 'refuse to recommend' pathway," the Engineer says. "For category (a), CHART recommends with confidence. For category (b), CHART recommends with caveats. For category (c), CHART recommends general best practices. But there's a category (d): the link is so speculative that even no-regret recommendations would be misleading."

Purple policy:

> 🟪 **If the climate-health link has fewer than 3 peer-reviewed sources in the RAG database, classify as "evidence gap" and recommend only standard-of-care interventions. Do not attribute them to climate adaptation.**

Dr. Wanjiku: "And feed those evidence gaps back to research institutions. KEMRI. University of Nairobi School of Public Health. If CHART keeps getting asked about heat and preterm birth in Kenya and has no evidence, that's a research signal."

---

The facilitator surveys the wall. The red stickies form a constellation of failure modes around the happy path, each one connected to a mitigation policy or alternative command. The process model has grown from a clean linear flow into something messier and more honest.

```
                    UNHAPPY PATHS — FAILURE MODES
                    ══════════════════════════════

    🔴 DHIS2 data missing          🔴 DHIS2 data wrong
         │                              │
         ▼                              ▼
    🟦 Cascade to proxy           🟪 Anomaly detection
    🟪 Label as proxy data        🟪 Flag > 2 SD deviation
                                  🟪 Exclude + explain

    🔴 Forecast wrong             🔴 Governor rejects plan
         │                              │
         ▼                              ▼
    🟪 Sensitivity section        🟦 Alternative funding search
    🟪 Probabilistic language     🟪 Cite precedent cases
    🟪 "What if opposite"        🟨 County Health Director
         scenario                      escalates

    🔴 KEMSA delivery delayed     🔴 KEMSA delivers wrong items
         │                              │
         ▼                              ▼
    🟦 Contingency alert          🟦 Verify order against spec
    🟪 Escalate → MEDS →          🟪 Photo verification at
       redistribute                    delivery point

    🔴 No evidence for link
         │
         ▼
    🟪 3-tier evidence labeling
    🟪 < 3 sources = evidence gap
    🟦 No-regret recommendations only
    🟦 Flag for research
```

"We've broken it beautifully," the facilitator says. "Now let's close the loop."

---

## Part C: The Feedback Loop (4:00–4:30)

Peter has been staring at the far right end of the process model — the point where the KEMSA order is placed and the supplies are (theoretically) delivered. Past that point, the wall is empty. The old orange event stickies from Phase 2 pick up again with *"Rains begin"* and *"Disease cases reported"* and *"Outbreak response activated"* — but there's no connection between what CHART planned and what actually happened.

"I have a question," Peter says. He's still facing the wall, not the room. "Do I ever find out if my forecast was useful?"

The room goes quiet. Not the tense silence of a disagreement — the silence of a penny dropping.

"Right now," Peter continues, turning around, "I issue the outlook in February. Counties do... whatever they do with it. Usually nothing. Sometimes someone calls me and says 'Peter, you were wrong.' Nobody calls me when I'm right. Nobody tells me if the forecast led to action. Nobody tells me how many lives were saved because we predicted the rains correctly."

He sits down, crosses his arms. "And honestly? That's why my forecasts aren't getting better. I have no feedback. I don't know which forecasts are useful to health planners and which ones aren't. I don't know if the county-level resolution matters or if you need sub-county. I don't know if tercile probabilities are the right format or if you need something else. I'm operating in a vacuum."

Dr. Amina is nodding slowly. "And I have the same problem in reverse. I make a plan — if I manage to make one at all — and after the season, nobody evaluates whether it worked. Did the pre-positioned RDTs actually reach the patients who needed them? Did the cholera kits arrive before or after the outbreak? I have a reporting obligation to the national MOH through the NCCAP framework, but the report is always qualitative. 'We implemented preparedness measures.' Not: 'We implemented these specific measures, and here were the outcomes.'"

Dr. Wanjiku stands up. "This is *exactly* what I need for NCCAP reporting. Right now I get county reports that say 'climate adaptation activities were undertaken.' Forty-seven counties, forty-seven identical sentences. I need: 'CHART recommended X intervention based on Y forecast. Intervention was Z percent implemented. Observed disease incidence was W percent below/above the expected baseline.' That is an outcome metric. That is something I can put in front of the National Climate Change Council."

She picks up a blue sticky.

> 🟦 **Track intervention implementation status (post-season)**

And another:

> 🟦 **Compare observed outcomes to CHART predictions (seasonal verification)**

And a third:

> 🟦 **Generate impact report (forecast utility + intervention effectiveness + health outcomes)**

She places them to the right of the KEMSA order, extending the timeline past the end of the season.

"Who does this?" Joseph asks. "Who goes back and checks whether the plan worked?"

"CHART does the data work," the Engineer says. "After the season ends, CHART pulls three things." He writes green stickies:

> 🟩 **KMD verified rainfall data (post-season)**
> 🟩 **DHIS2 disease incidence (actual, post-season)**
> 🟩 **KEMSA delivery confirmation records**

"It compares what was forecast to what happened. It compares what was recommended to what was delivered. It compares expected disease incidence to actual. And it generates a verification report."

He writes a blue command:

> 🟦 **Generate seasonal verification report**

"The report says things like: 'MAM 2026 forecast for Kilifi: above-normal rainfall, 45% probability. Observed: above-normal rainfall by 23% relative to 1991-2020 climatology. Forecast category: correct. CHART-recommended interventions: 5 of 7 implemented. Malaria case fatality rate: 0.3% against predicted 0.8% without intervention. Estimated impact: 14 deaths averted, KES 12.4 million in emergency response costs avoided.'"

Peter is writing furiously on stickies. He places a yellow actor and a blue command:

> 🟨 **KMD Forecast Verification Unit**
> 🟦 **Feed health-outcome data back to KMD for forecast skill assessment**

"This changes everything for me," Peter says, his voice rising. "Right now, I verify my forecasts against *rain gauge data only.* Did it rain as much as I predicted? That's a meteorological verification. But what I've never been able to do is *impact verification.* Was my forecast *useful?* Did it lead to *action?* Did that action save *lives?*"

He draws an arrow on the wall with his marker — a long, sweeping arrow from the verification report all the way back to the first green sticky at the beginning of the happy path, the KMD Climate Outlook Portal.

"If I know that my MAM forecast for Kilifi led to pre-positioned cholera kits that prevented 340 cholera cases, I will fight for better resolution, better lead time, better communication of that forecast. I will go to my director and say: 'We need to invest in sub-county level forecasting because the county level wasn't granular enough for Ganze versus Malindi.' I have *evidence* that my work matters."

Dr. Wanjiku is standing at the wall now, connecting stickies with drawn arrows. "And I take that same report — with the same numbers — to the National Climate Change Council. I say: 'In MAM 2026, CHART-enabled adaptation planning across 12 pilot counties resulted in an estimated KES 148 million in avoided emergency response costs and 167 averted deaths. Here is the county-by-county breakdown. Here is the methodology. Here is the forecast verification. Here are the DHIS2 records.' That is an NCCAP Monitoring, Reporting and Verification deliverable. That is something that unlocks the next round of Green Climate Fund financing."

She places a green sticky at the very end of the extended timeline:

> 🟩 **NCCAP MRV Framework (National Climate Change Council)**

And a blue command:

> 🟦 **Submit verified impact data to NCCAP reporting pipeline**

Joseph leans forward. "And KEMSA. If the verification report shows that KEMSA delivered late to four counties and the outcomes in those counties were worse, that's accountability data. That goes to the KEMSA board. That goes to the Senate health committee."

> 🟩 **KEMSA Performance Monitoring**
> 🟦 **Feed delivery performance data to KEMSA accountability framework**

Sarah, who has been listening with the focused intensity of someone who has watched systems fail at the last mile for years, speaks.

"And the community health workers. Do we find out if the messaging worked? If I tell my CHWs to do household visits about cholera prevention — boil water, wash hands, use ORS early — do I find out if the households that were visited had better outcomes than the ones that weren't?"

She places a tentative blue sticky:

> 🟦 **Track CHW household visit completion vs. health outcomes at facility level**

"That's hard," Raj says. "CHW reporting is on paper in most sub-counties. eCHIS — the electronic Community Health Information System — is only in a few counties."

Sarah: "Kilifi has eCHIS. We can start there."

Green sticky:

> 🟩 **eCHIS (where available) — CHW activity data**

Purple policy:

> 🟪 **Feedback loop reporting is mandatory for CHART-participating counties. Quarterly during season, end-of-season verification within 8 weeks of season end.**

---

### The Loop Closes

The Engineer steps back to look at the full wall. The process model now forms a circle — or rather, a spiral. The verification report feeds back to three places: KMD (better forecasts), national MOH (NCCAP reporting), and the next season's CHART planning cycle (better baselines).

He draws the final connection on the wall — from the impact report back to the DHIS2 data quality step at the beginning.

"The verification process itself improves the data. When we go back and compare CHART predictions to actual outcomes, we find the data gaps. We find the facilities that didn't report. We find the anomalies. Each cycle, the baseline data gets better, the predictions get better, the plans get better."

```
            THE COMPLETE CHART PROCESS MODEL — WITH FEEDBACK LOOP
            ═══════════════════════════════════════════════════════

         ┌──────────────────────────────────────────────────────────┐
         │                                                          │
         ▼                                                          │
    🟩 KMD Outlook ──▶ 🟦 Fetch ──▶ 🟦 Parse                      │
                                        │                           │
    🟩 DHIS2 ─────────────────────────▶ │                           │
    🟩 MFL ───────────────────────────▶ │                           │
    🟩 Action Repo ───────────────────▶ │                           │
                                        ▼                           │
                              🟦 Translate climate                  │
                                 signal → health risk               │
                              🟨 CHART AI Engine                    │
                                        │                           │
                                        ▼                           │
                              🟦 Match risks →                     │
                                 interventions                      │
                                        │                           │
                                        ▼                           │
                              🟦 Generate draft plan                │
                              🟨 County Health Director             │
                                        │                           │
                                        ▼                           │
                              🟦 TWG Review                        │
                              🟨 County TWG                         │
                                        │                           │
                                   ┌────┴────┐                      │
                                   ▼         ▼                      │
                              APPROVE    REJECT──▶🟦 Alt. Funding   │
                                   │                                │
                                   ▼                                │
                              🟦 AWP Insert + 🟦 KEMSA Order        │
                                   │                                │
                                   ▼                                │
                            ════════════════                        │
                            ║  SEASON  ║                            │
                            ║ HAPPENS  ║                            │
                            ════════════════                        │
                                   │                                │
                                   ▼                                │
                      ┌─────────────────────────┐                   │
                      │ 🟦 Track implementation  │                   │
                      │ 🟦 Compare predictions   │                   │
                      │    to observed outcomes  │                   │
                      │ 🟦 Generate impact report│                   │
                      └────────────┬────────────┘                   │
                                   │                                │
                    ┌──────────────┼──────────────┐                 │
                    ▼              ▼              ▼                 │
              🟩 NCCAP MRV   🟩 KEMSA Perf.  🟨 KMD Forecast      │
              (Dr. Wanjiku)  (Accountability)  Verification ────────┘
                                               (Peter)

         ═══════════════════════════════════════════════
         The feedback arrow completes the spiral.
         Each cycle: better forecasts, better data,
         better plans, better outcomes, better evidence.
         ═══════════════════════════════════════════════
```

---

### The Adoption Insight

Dr. Wanjiku is staring at the feedback loop arrow — the one running from Peter's verification unit all the way back to the KMD Outlook at the top. She taps it.

"This is the adoption mechanism," she says quietly. Then louder: "This is *the* adoption mechanism."

Everyone turns.

"We've been talking about CHART as if the hard part is building it. The hard part isn't building it. The hard part is getting people to use it. Getting counties to change their planning cycle. Getting KMD to issue forecasts in a machine-readable format. Getting KEMSA to respond to lead-time requirements. Getting Governors to fund prevention over stadiums."

She traces the feedback loop with her finger. "But if Peter issues a forecast, and CHART translates it into a plan, and the plan is implemented, and we can show — with verified data — that the forecast saved lives... then Peter fights to make his forecasts better. Then Dr. Amina fights to get the next plan funded. Then the Governor starts asking 'where is the CHART plan for next season?' because the *Daily Nation* wrote about how Kilifi prevented a cholera outbreak. Then KEMSA pre-positions supplies on time because they know someone is tracking their delivery performance."

She places one final purple sticky in the center of the feedback loop:

> 🟪 **Feedback loop is not optional infrastructure. It is the primary adoption and sustainability mechanism. Without it, CHART is a report generator. With it, CHART is a system that gets stronger every season.**

Peter looks at the purple sticky. He reads it twice. Then he looks at Dr. Wanjiku.

"If I see my forecast save thirty-seven lives in Kilifi, I will personally drive to Nairobi and present to the National Treasury for CHART funding."

"Write that down," Dr. Amina says. "We'll hold you to it."

---

The facilitator checks the clock. 4:28 PM.

The wall is covered. Blue commands trace a path from forecast to plan to order to season to verification to feedback. Yellow actors stand at every decision point — no automated action without a human owner. Purple policies constrain the system at every junction — thresholds, quorum requirements, evidence standards, format requirements. Green external systems mark every integration point where CHART must connect to something it doesn't control. Red hotspots mark every failure mode, each one paired with a mitigation.

"Phase 3 complete," the facilitator says. "You've modeled a process that doesn't exist yet. In Phase 4, we'll turn this into bounded contexts and start drawing system boundaries. But first — tea. And everyone needs to initial the stickies they wrote. If this system gets built, I want to know whose requirement is whose."

Dr. Amina is already initialing her cost-of-inaction sticky. Peter is photographing the entire wall with his phone, meticulously, panel by panel. Joseph is counting the external system dependencies — he's up to eleven. Sarah is explaining the cold-chain policy to the Engineer, who is asking follow-up questions about which specific vaccine-adjacent supplies require refrigeration. Raj is redrawing the data quality cascade on a notebook, adding edge cases nobody mentioned.

Dr. Wanjiku stands at the center of the wall, looking at the feedback loop arrow. She takes out her phone and sends a text to her director at national MOH. It reads: *"Workshop going well. Found the NCCAP MRV solution we've been looking for. It's not a reporting template. It's a system. Will brief Monday."*

---



# Phase 4: Design Level — Bounded Contexts, Aggregates, and Read Models

*Day 2 morning. The room has been rearranged. Yesterday's event flow still stretches across the wall, but the facilitator has cleared a second wall and set up a large whiteboard. Blue-tape lines divide the whiteboard into quadrants. The Engineer has brought a laptop projecting a blank Miro board as backup, but the group gravitates toward the physical whiteboard. Coffee is strong. The energy is different today — less exploratory, more architectural.*

---

## Part A: Bounded Context Discovery

### The Word That Means Four Things

The facilitator uncaps a red marker and writes a single word in the center of the whiteboard:

**RISK**

"Before we draw any boxes," the facilitator says, "I want to do an exercise. I heard this word at least fifty times yesterday. I want each of you to tell me what it means. Not the textbook definition. What it means when you say it at your desk on a Monday morning."

Peter goes first. He stands and points at the climate timeline from yesterday's wall.

"Risk for me is a probabilistic statement. When I say there is a risk of above-normal rainfall in the October-November-December season, I mean the tercile probability exceeds forty percent. It is a climatological statement. I am saying the atmosphere is configured in a way that favors certain outcomes. I am not saying it will rain. I am saying the probability distribution is shifted."

He pauses. "I would write it as P(rainfall > 75th percentile) = 0.45. That is what risk means to me."

The facilitator writes on the whiteboard:

> **Peter (KMD):** Risk = probability of climate anomaly. Units: tercile probabilities. Timeframe: seasonal.

Dr. Amina is already shaking her head — not in disagreement, but in recognition of the gap.

"When I hear 'risk' in my office, I am thinking about money. I am thinking: if I do nothing about this forecast, and the worst happens, how much of my Annual Work Plan will I have to cannibalize to fund emergency response? When the rains came in 2023 and we had that cholera outbreak in Malindi sub-county, I had to redirect fourteen million shillings from routine immunization. That is risk to me. Financial exposure from inaction."

> **Dr. Amina (County Health Director):** Risk = financial exposure from emergency response. Units: KES. Timeframe: fiscal year.

Joseph leans forward. "For me, risk is clinical. I look at our DHIS2 data from previous similar seasons, and I calculate expected case counts above baseline. If we normally see two hundred malaria cases per month in Kilifi North and I think we will see five hundred, that excess of three hundred cases is the risk. Each case means drugs, bed-nights, possibly a death. I can put a number on each component."

> **Joseph (Surveillance Officer):** Risk = expected case count above baseline. Units: cases, commodities, DALYs. Timeframe: epidemiological weeks.

Sarah speaks last, and her definition is the most concrete.

"Risk is whether Bi Mwanajuma in Matsangoni can get to the dispensary when she needs to. If the road floods, she cannot. If the CHW cannot reach her homestead, she does not get her mosquito net. If the community meeting cannot happen because the chief's hall is waterlogged, we cannot do health education. Risk is access. Can we physically reach people and can they physically reach services?"

> **Dr. Amina (County Health Director):** Risk = financial exposure from emergency response. Units: KES.
> **Joseph (Surveillance):** Risk = expected cases above baseline. Units: cases, commodities.
> **Sarah (CHW Supervisor):** Risk = physical accessibility of services. Units: passable/impassable roads, reachable/unreachable households.
> **Peter (KMD):** Risk = probability of climate anomaly. Units: tercile probabilities.

The facilitator steps back and gestures at the four definitions. "Four people. One word. Four completely different meanings. Four different units. This is not a vocabulary problem to be solved with a glossary. This is a boundary."

The Engineer nods vigorously. "This is exactly what Eric Evans means by bounded contexts. Each of these definitions is internally consistent. Peter's team would never confuse what 'risk' means among themselves. Dr. Amina's budget team would never confuse it. The confusion only happens at the boundaries — when Peter's forecast crosses into Dr. Amina's world."

Dr. Wanjiku, who has been listening quietly, adds a fifth dimension. "At the national level, risk means something else again. It means Kenya's progress against NCCAP indicators. It is reputational and political. But let us not add that complexity today."

The facilitator draws a dotted line on the whiteboard. "Agreed. Let us stay with the operational system. But notice what just happened. We found boundaries by finding where language diverges."

### Drawing the Lines

The Engineer moves to the whiteboard and begins sketching. "Let me propose some boundaries based on what we heard yesterday and what we just surfaced. Tell me where I am wrong."

He draws four large rounded rectangles:

```
┌─────────────────────┐    ┌─────────────────────────────┐
│                     │    │                             │
│      CLIMATE        │    │     HEALTH RISK             │
│    INTELLIGENCE     │───▶│     TRANSLATION             │
│                     │    │                             │
│  (Peter's world)    │    │  (the NEW core domain)      │
│                     │    │                             │
└─────────────────────┘    └──────────────┬──────────────┘
                                          │
                                          │
┌─────────────────────┐    ┌──────────────▼──────────────┐
│                     │    │                             │
│     HEALTH          │    │     ADAPTATION              │
│     DATA            │───▶│     PLANNING                │
│                     │    │                             │
│  (Raj's world)      │    │  (Dr. Amina's world)        │
│                     │    │                             │
└─────────────────────┘    └─────────────────────────────┘
```

"Climate Intelligence is Peter's world. It speaks in tercile probabilities, anomalies, return periods, SSP scenarios. It ingests KMD forecasts and ClimSight model outputs. Its job is to answer: what is the climate doing, and how unusual is it?"

Peter nods. "Yes. And I want to be clear — this context should not try to interpret health implications. That is not our expertise. We provide the signal. Someone else provides the meaning."

"Exactly," the Engineer says. "Which brings us to the second context. Health Risk Translation. This is the new thing. This is the core domain — the thing that does not exist today and is the reason CHART needs to be built. It takes a climate signal and produces a health risk statement. It answers: given this forecast, what health outcomes do we expect, with what confidence, based on what evidence?"

Dr. Amina sits up. "This is the gap we identified yesterday. The translation layer."

"Right. And notice — inside this context, 'risk' means something very specific. It means a structured assessment linking a climate signal to a health outcome with a confidence score and an evidence grade. It is neither Peter's definition nor yours nor Joseph's. It is its own language."

Joseph raises a hand. "But it needs to speak all of our languages at its boundaries. It needs to take Peter's tercile probability as input and produce something I can use to calculate case counts and something Dr. Amina can use to calculate budget impact."

"That is the job of the boundary," the Engineer says, drawing arrows between the boxes. "Inside each context, the language is pure. At the boundary, we translate."

He continues. "Adaptation Planning is Dr. Amina's world. It speaks in AWP line items, budget codes, KEMSA procurement timelines, TWG approval workflows. Its job is to take a risk assessment and produce an actionable plan that fits into county government processes."

Dr. Amina taps the table. "This is important. The output of CHART must be a document I can take to the TWG. It must look like something that belongs in our planning process, not like a research paper."

"And finally, Health Data. This is Raj's world. DHIS2 indicators, facility-level reporting, historical baselines. It provides the epidemiological context that Health Risk Translation needs to do its work."

Raj shifts uncomfortably. "I want to flag that DHIS2 is a nightmare to work with cleanly. The data model has UIDs for everything. A malaria case in DHIS2 is not a 'malaria case' — it is data element `qXkHKjHpFM9` in organisation unit `jNb63DIHuwU` for period `202410`. We will need a serious translation layer."

The Engineer marks Raj's context with a hatched border. "Anti-corruption layer. Essential. We will come back to that."

### The Action Repository Debate

Dr. Wanjiku raises a concern that has been simmering. "Where does the intervention catalog live? Both the Risk Translation context and the Adaptation Planning context need to know about interventions. When Risk Translation says 'distribute LLINs,' and when Planning says 'budget for LLIN distribution' — are they talking about the same thing or different things?"

The Engineer pauses. This is the question he was hoping someone would ask.

"I would argue," he says carefully, "that the Action Repository should be its own bounded context. Clean separation. It is a reference data domain — a catalog of possible interventions with their evidence bases, costs, prerequisites, and supply chain requirements. Both Risk Translation and Planning consume it but neither owns it."

Dr. Wanjiku frowns. "In practice, that means we maintain a separate service with its own data model and its own deployment lifecycle. For what? A lookup table?"

"It is not a lookup table," the Engineer says. "It has behavior. An intervention has eligibility criteria, contraindications, cost models that depend on scale, cold chain requirements that depend on geography. The LLIN distribution intervention for Kilifi with its coastal humidity and road network is not the same operation as LLIN distribution for Turkana."

"He is right about the complexity," Joseph says. "But I think Dr. Wanjiku is also right that making it a separate bounded context is over-engineering for where we are. We are not building a platform for all of Africa. We are building a tool for forty-seven counties in Kenya."

The room goes quiet for a moment.

Dr. Amina breaks the silence. "Can we do something in between? Something that is shared but has a clear contract?"

The Engineer nods slowly. "A Shared Kernel. Both the Risk Translation and Planning contexts share a common set of intervention definitions. We define the schema once — as a Pydantic model with strict validation — and both contexts import it. The contract is the schema. If either context needs to change how interventions are represented, both teams must agree."

He sketches on the board:

```
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│                    SHARED KERNEL                               │
│                    (Action Repository)                         │
│                                                                │
│    InterventionDefinition:                                     │
│      - id: str                                                 │
│      - name: str (e.g., "LLIN mass distribution")              │
│      - category: enum [VECTOR_CONTROL, WASH, NUTRITION, ...]   │
│      - evidence_grade: enum [A, B, C]                          │
│      - base_cost_kes_per_capita: float                         │
│      - prerequisites: list[Prerequisite]                       │
│      - cold_chain_required: bool                               │
│      - kemsa_lead_time_days: int                               │
│      - community_acceptability: enum [HIGH, MEDIUM, LOW]       │
│                                                                │
│    Pydantic schema = the contract                              │
│                                                                │
└────────────────────────────────────────────────────────────────┘
         ▲                              ▲
         │ imports                       │ imports
         │                              │
┌────────┴────────────┐    ┌────────────┴─────────────────┐
│  HEALTH RISK        │    │  ADAPTATION                  │
│  TRANSLATION        │    │  PLANNING                    │
└─────────────────────┘    └──────────────────────────────┘
```

Sarah speaks up firmly. "I see 'community_acceptability' on that list. Good. But I want to tell you why. In 2022, we tried to do indoor residual spraying in parts of Kaloleni. The community refused. They said the spray smells bad and stains the walls. We wasted two weeks and six hundred thousand shillings on a campaign that reached thirty percent coverage. If the system recommends IRS without flagging that Kaloleni has low acceptability, it will be making the same mistake a human planner already made."

The Engineer adds a note next to `community_acceptability`: *"Source: CHW ground-truth data. Must be updateable per sub-county."*

Dr. Wanjiku nods at the Shared Kernel diagram. "I can accept this. But I want it documented that if the Action Repository grows complex enough to need its own lifecycle — its own versioning, its own approval process for adding new interventions — we revisit this decision and promote it to a full bounded context."

"Agreed. We note it as a known evolution point," the facilitator says, writing it on a yellow sticky note and placing it on the wall.

---

## Part B: Aggregate Design

### Climate Intelligence Aggregates

The Engineer switches to a fresh section of the whiteboard. "Now let us go inside each bounded context and identify the core aggregates. An aggregate is a cluster of objects that we treat as a unit for the purpose of data changes. It has a root entity that controls access and enforces invariants."

He starts with Climate Intelligence. "This is the most straightforward because it maps closely to ClimSight's existing data model."

```
CLIMATE INTELLIGENCE
═══════════════════════════════════════════════════════

┌─ SeasonalForecast ──────────────────────────────────┐
│  forecast_id: UUID                                  │
│  source: enum [KMD_BULLETIN, CLIMSIGHT, ICPAC]      │
│  location: {county, lat, lon}                       │
│  period: {season, year}  (e.g., OND-2026)           │
│  variables:                                         │
│    - rainfall_tercile_probs: {below, normal, above} │
│    - temperature_anomaly_deg_c: float               │
│    - wind_anomaly: float | null                     │
│  confidence: float (0.0 - 1.0)                      │
│  issued_date: date                                  │
│  raw_model_outputs: list[ModelRun]                  │
└─────────────────────────────────────────────────────┘

┌─ ClimatologyBaseline ───────────────────────────────┐
│  location: {county, lat, lon}                       │
│  source: ERA5_10YR_CLIMATOLOGY                      │
│  period: {start_year, end_year}                     │
│  monthly_normals:                                   │
│    - temperature_2m: float[12]                      │
│    - precipitation: float[12]                       │
│    - wind_speed: float[12]                          │
│  percentiles: {p10, p25, p50, p75, p90}             │
└─────────────────────────────────────────────────────┘

┌─ EnvironmentalProfile ──────────────────────────────┐
│  location: {county, lat, lon}                       │
│  elevation_m: float                                 │
│  soil_type: str                                     │
│  land_use: str                                      │
│  flood_return_periods: dict[int, float]             │
│  drought_history: list[DroughtEvent]                │
│  proximity_to_coast_km: float                       │
└─────────────────────────────────────────────────────┘
```

Peter examines the diagram. "I want to make sure `raw_model_outputs` is preserved. Different models give different signals. The GloSea6 ensemble may say one thing, the ECMWF SEAS5 another. When CHART picks one signal, we need to know which model drove the assessment. For accountability."

"Agreed," says the Engineer. "The SeasonalForecast aggregate keeps provenance. We never throw away the model-level detail."

Dr. Wanjiku adds: "And `issued_date` is critical. A forecast from August is stale by November. We need to enforce that downstream consumers know the age of the forecast they are using."

The Engineer draws a small note: *"Invariant: SeasonalForecast must have issued_date < current_date - max_staleness_days (configurable, default 90)."*

### Health Risk Translation Aggregates — The Core Domain

"Now," says the Engineer, taking a breath, "the hard one."

He writes **HealthRiskAssessment** in large letters. "This is the aggregate that does not exist today. This is the thing CHART is building. Let us design it together."

He starts listing fields. The room immediately erupts.

"Climate signal as input." He writes `climate_signal`.

"What type?" asks Peter. "A reference to the SeasonalForecast? A summary? The raw tercile probabilities?"

"A structured summary," the Engineer says. "We do not want this aggregate to depend on the internal structure of Climate Intelligence. We translate at the boundary. So the climate signal here is a value object — a snapshot of the relevant climate information, expressed in Health Risk Translation's own language."

```
climate_signal:
  variable: enum [EXCESS_RAINFALL, DEFICIT_RAINFALL, HIGH_TEMP, ...]
  magnitude: enum [MODERATE, SEVERE, EXTREME]
  probability: float
  source_forecast_id: UUID  (traceability link, not a foreign key)
```

Joseph nods. "Good. So this context does not care about tercile probabilities per se. It cares about 'excess rainfall, severe, probability 0.45.' That is a translation."

"Exactly. Now — health outcome." The Engineer writes `health_outcome`.

Dr. Amina jumps in immediately. "This must be in language I can put in front of the TWG. Not ICD-10 codes. Not 'increased vector breeding potential.' I need: 'Malaria cases in children under five are expected to increase by forty to sixty percent above the five-year average in Kilifi North and Malindi sub-counties.'"

Joseph counters: "But I also need the actual numbers. If you tell me forty to sixty percent increase and I know the baseline is two hundred cases per month, I need to calculate that I need supplies for an additional eighty to one hundred twenty cases. I need structured data, not a paragraph."

The Engineer holds up both hands. "You are both right. And this is exactly why we need both structured data and an LLM-generated summary. The aggregate stores the machine-readable data. The read model — we will get to that — generates the human-readable version for each audience."

He sketches the full aggregate:

```
HEALTH RISK TRANSLATION
═══════════════════════════════════════════════════════

┌─ HealthRiskAssessment ──────────────────────────────┐
│  assessment_id: UUID                                │
│  created_at: datetime                               │
│  location: {county, sub_counties: list[str]}        │
│  period: {season, year}                             │
│                                                     │
│  climate_signal:                                    │
│    variable: enum                                   │
│    magnitude: enum [MODERATE, SEVERE, EXTREME]      │
│    probability: float                               │
│    source_forecast_id: UUID                         │
│                                                     │
│  health_outcome:                                    │
│    disease: str (e.g., "malaria")                   │
│    icd10_chapter: str (e.g., "B50-B54")             │
│    affected_population: str (e.g., "children <5")   │
│    population_at_risk: int                          │
│    baseline_monthly_cases: float                    │
│    predicted_increase_pct: {low: float, high: float}│
│    predicted_excess_cases: {low: int, high: int}    │
│                                                     │
│  relative_risk: float                               │
│  confidence_score: float (0.0 - 1.0)               │
│  evidence_source: list[EvidenceReference]           │
│  evidence_grade: enum [A, B, C]                     │
│    A = peer-reviewed Kenya-specific study            │
│    B = regional/continental study or IPCC finding    │
│    C = expert judgment or analogous context          │
│                                                     │
│  threshold_basis:                                   │
│    threshold_type: str                              │
│    threshold_value: float                           │
│    threshold_source: str                            │
│    exceeded: bool                                   │
│                                                     │
│  llm_narrative: str  (generated, not authored)      │
│  llm_model_version: str  (provenance)               │
│  uncertainty_warnings: list[str]                    │
│                                                     │
│  INVARIANTS:                                        │
│  - confidence_score < 0.4 → must include            │
│    "LOW CONFIDENCE" warning                         │
│  - evidence_grade == C → must include               │
│    "EXPERT JUDGMENT ONLY" warning                   │
│  - refuse_to_assess if no evidence linkage exists   │
│    between climate_signal and health_outcome        │
└─────────────────────────────────────────────────────┘
```

Dr. Wanjiku studies the invariants. "I like the refuse-to-assess rule. Yesterday we said the system should not hallucinate causal links. This enforces it at the aggregate level. If there is no evidence — not even expert judgment — linking this particular climate signal to this particular health outcome, the system should say 'I cannot assess this' rather than guess."

"What about compound risks?" Joseph asks. "Flooding causes both waterborne disease and disruption to routine services. Those are two different HealthRiskAssessments?"

"Yes," the Engineer says firmly. "One assessment per climate-signal-to-health-outcome link. They share the same climate signal but produce different health outcomes. The Adaptation Planning context downstream can group them."

The Engineer moves to the second aggregate.

```
┌─ InterventionMatch ─────────────────────────────────┐
│  match_id: UUID                                     │
│  assessment_id: UUID  (parent HealthRiskAssessment)  │
│                                                     │
│  matched_interventions:                             │
│    - intervention_id: str (from Shared Kernel)      │
│      intervention_name: str                         │
│      evidence_grade: enum [A, B, C]                 │
│      estimated_cost_kes: float                      │
│      cost_basis: str (per capita / per facility)    │
│      feasibility:                                   │
│        cold_chain_available: bool                   │
│        staff_available: bool                        │
│        budget_available: bool                       │
│        supply_lead_time_ok: bool                    │
│        community_acceptability: enum                │
│        overall_feasible: bool                       │
│      priority_rank: int                             │
│                                                     │
│  infeasible_interventions:                          │
│    - intervention_id: str                           │
│      reason: str                                    │
│      (e.g., "cold chain not available at 3 of 7    │
│       facilities in Malindi sub-county")            │
│                                                     │
│  INVARIANTS:                                        │
│  - At least one intervention must be feasible,      │
│    OR explicitly state "no feasible intervention    │
│    identified" with escalation flag                 │
│  - Infeasible interventions preserved for           │
│    transparency (show what was considered)          │
└─────────────────────────────────────────────────────┘
```

Sarah studies the feasibility block. "I see `community_acceptability`. Thank you. But how is this populated? Where does the data come from?"

The Engineer turns to her. "Initially, from a static lookup table based on your team's experience. We would sit down with you and your CHW supervisors across the sub-counties and code their knowledge. 'IRS in Kaloleni: LOW. LLINs in Kilifi South: HIGH. ORS distribution everywhere: HIGH.' Over time, the feedback loop updates this — if an intervention was deployed and uptake was low, we downgrade acceptability."

Sarah considers this. "That is acceptable. But I want to be the one who reviews those initial values. Not someone in Nairobi guessing."

"Absolutely. Ground truth comes from the ground."

### Adaptation Planning Aggregates

The Engineer moves to the third context. "This is where the system produces what Dr. Amina actually takes to the TWG."

```
ADAPTATION PLANNING
═══════════════════════════════════════════════════════

┌─ SeasonalAdaptationPlan ────────────────────────────┐
│  plan_id: UUID                                      │
│  county: str (e.g., "Kilifi")                       │
│  period: {season, year} (e.g., OND-2026)            │
│  created_at: datetime                               │
│  created_by: str (system-generated, human-reviewed) │
│                                                     │
│  risks: list[RiskSummary]                           │
│    - assessment_id: UUID                            │
│      disease: str                                   │
│      severity: enum [WATCH, ALERT, EMERGENCY]       │
│      affected_sub_counties: list[str]               │
│      headline: str (plain language)                 │
│                                                     │
│  actions: list[PlannedAction]                       │
│    - intervention_id: str                           │
│      intervention_name: str                         │
│      target_sub_counties: list[str]                 │
│      target_facilities: list[str]                   │
│      target_population: int                         │
│      budget_kes: float                              │
│      awp_line_item: str (e.g., "4.2.1 - Vector     │
│        Control, Preventive")                        │
│      budget_source: enum [EXISTING_AWP, EMERGENCY   │
│        FUND, REALLOCATION, UNFUNDED]                │
│      implementation_start: date                     │
│      implementation_end: date                       │
│      responsible_officer: str                       │
│                                                     │
│  budget_impact:                                     │
│    total_additional_kes: float                      │
│    funded_kes: float                                │
│    unfunded_gap_kes: float                          │
│    reallocations: list[{from_line, to_line, amount}]│
│                                                     │
│  cost_of_inaction_estimate:                         │
│    estimated_emergency_spend_kes: float             │
│    estimated_excess_cases: int                      │
│    estimated_excess_deaths: int                     │
│    methodology: str                                 │
│    confidence: enum [HIGH, MEDIUM, LOW]             │
│                                                     │
│  uncertainty_warnings: list[str]                    │
│    (MANDATORY when any input confidence < 0.70)     │
│                                                     │
│  twg_approval_status:                               │
│    status: enum [DRAFT, SUBMITTED, REVIEWED,        │
│                  APPROVED, REJECTED, REVISED]        │
│    twg_meeting_date: date | null                    │
│    twg_comments: str | null                         │
│    approved_by: str | null                          │
│                                                     │
│  INVARIANTS:                                        │
│  - Cannot submit to TWG if uncertainty_warnings     │
│    is empty AND any risk has confidence < 0.70      │
│    (must be honest about uncertainty)               │
│  - budget_source must be specified for every action │
│  - UNFUNDED actions require justification narrative │
│  - cost_of_inaction is REQUIRED (even if rough)     │
└─────────────────────────────────────────────────────┘
```

Dr. Amina reads the aggregate field by field, nodding slowly, then stops at `cost_of_inaction_estimate`.

"This," she says, putting her finger on it. "This is the most politically important field in the entire system. When I go to the TWG and say 'I need eight million shillings for malaria preparedness,' the first question is always 'Where does the money come from?' But when I say 'If we spend eight million now, we avoid thirty million in emergency response and prevent an estimated forty deaths,' that changes the conversation entirely."

She pauses. "I have been making this argument with napkin math for years. If CHART can produce this estimate with actual evidence backing, with a confidence level, with a methodology I can cite — that is transformative."

The Engineer nods but adds a caution. "The methodology field is critical here. We must be transparent that this is a model estimate with assumptions. The system should never present cost-of-inaction as a precise number. It is a range with stated assumptions."

"Better a transparent estimate than no estimate at all," Dr. Amina says. "Right now, the TWG has zero quantitative basis for comparing 'prepare' versus 'wait and respond.'"

The Engineer continues with the second aggregate:

```
┌─ SupplyPrePositioningOrder ─────────────────────────┐
│  order_id: UUID                                     │
│  plan_id: UUID (parent SeasonalAdaptationPlan)       │
│  facility: {name, mfl_code, sub_county}             │
│                                                     │
│  items: list[OrderItem]                             │
│    - commodity: str (e.g., "AL 20mg tablets")       │
│      kemsa_code: str                                │
│      quantity_required: int                         │
│      stock_on_hand: int | null                      │
│      quantity_to_order: int                         │
│      unit_cost_kes: float                           │
│      total_cost_kes: float                          │
│                                                     │
│  order_deadline: date                               │
│  kemsa_lead_time_days: int (typically 30-90)        │
│  season_onset_expected: date                        │
│  buffer_days: int (default 14)                      │
│                                                     │
│  INVARIANTS:                                        │
│  - order_deadline = season_onset_expected            │
│    - kemsa_lead_time_days - buffer_days             │
│  - If order_deadline < today, flag as URGENT         │
│    with escalation to county pharmacist             │
│  - quantity_to_order = max(0, quantity_required     │
│    - stock_on_hand) when stock data available       │
└─────────────────────────────────────────────────────┘
```

Joseph practically jumps out of his chair. "Yes. This. This is what I need. Right now I do this on a spreadsheet and I always get the timing wrong because KEMSA lead times vary by commodity. Antimalarials are usually thirty days. ORS sachets can take sixty. RDTs have been ninety days recently because of global supply issues."

He points at the invariant. "This calculation — order deadline equals onset minus lead time minus buffer — this alone would prevent the situation we had last year where we ordered commodities two weeks before the rains and they arrived six weeks after the outbreak peaked."

Raj adds a concern: "Stock-on-hand data. It is in DHIS2 but the reporting completeness for logistics data is terrible. Maybe fifty percent of facilities report stock levels monthly. We need to handle the case where stock_on_hand is null."

"Hence `int | null`," the Engineer says. "When stock data is unavailable, we order the full predicted quantity and flag it: 'stock levels unknown at this facility — order may be redundant if existing stock is sufficient.' Better to over-order than under-order when lives are at stake."

### Health Data Aggregates

Raj moves to the whiteboard for his context. He is uncomfortable drawing architecture diagrams, but he knows this data better than anyone.

```
HEALTH DATA
═══════════════════════════════════════════════════════

┌─ DHIS2HealthBaseline ───────────────────────────────┐
│  baseline_id: UUID                                  │
│  location: {county, sub_county, facility | null}    │
│  period_type: enum [MONTHLY, WEEKLY, ANNUAL]        │
│  period_range: {start, end}                         │
│                                                     │
│  indicator_values: list[IndicatorValue]             │
│    - chart_indicator: str                           │
│      (e.g., "malaria_cases_under5")                 │
│      dhis2_uid: str                                 │
│      (e.g., "qXkHKjHpFM9")                         │
│      dhis2_name: str                                │
│      (e.g., "105-2.1 OPD Malaria (Total) <5 Yrs")  │
│      values: list[{period, value}]                  │
│      five_year_mean: float                          │
│      five_year_p75: float                           │
│      five_year_p90: float                           │
│                                                     │
│  reporting_completeness:                            │
│    expected_reports: int                             │
│    received_reports: int                            │
│    completeness_pct: float                          │
│    quality_flag: enum [GOOD, FAIR, POOR, UNUSABLE]  │
│      GOOD: >= 80%                                   │
│      FAIR: 60-79%                                   │
│      POOR: 40-59%                                   │
│      UNUSABLE: < 40%                                │
│                                                     │
│  facility_metadata: list[FacilityInfo]              │
│    - mfl_code: str                                  │
│      name: str                                      │
│      level: enum [DISPENSARY, HEALTH_CENTRE,        │
│                   SUB_COUNTY_HOSPITAL, COUNTY_REF]   │
│      has_cold_chain: bool                           │
│      has_lab: bool                                  │
│      catchment_population: int                      │
│      road_accessibility: enum [ALL_WEATHER,         │
│        SEASONAL, DRY_ONLY]                          │
│                                                     │
│  INVARIANTS:                                        │
│  - If quality_flag == UNUSABLE, downstream          │
│    consumers MUST be warned                         │
│  - All DHIS2 UIDs resolved to human-readable        │
│    CHART concepts at ingestion time, not query time │
│  - Raw DHIS2 data preserved for audit               │
└─────────────────────────────────────────────────────┘
```

Raj explains the anti-corruption layer with visible frustration. "DHIS2 is a powerful system but it was not designed for programmatic consumption. Every county can customize their data entry forms. Kilifi might report malaria under data element `qXkHKjHpFM9`. Mombasa might use a different UID because they configured their forms differently. The indicator names have cryptic prefixes like '105-2.1' that refer to the MOH paper register numbering system from 2014."

He draws a wall between DHIS2 and the rest of the system.

```
    DHIS2 (raw)          Anti-Corruption Layer          CHART (clean)
  ┌──────────────┐    ┌────────────────────────┐    ┌──────────────────┐
  │ UIDs         │    │                        │    │                  │
  │ Cryptic names│───▶│  UID → concept mapping │───▶│ "malaria_cases   │
  │ Missing data │    │  Completeness scoring  │    │    _under5"      │
  │ Inconsistent │    │  Gap interpolation     │    │                  │
  │ periods      │    │  Period normalization   │    │  Clean, typed,   │
  │              │    │                        │    │  validated       │
  └──────────────┘    └────────────────────────┘    └──────────────────┘
```

"This mapping table," Raj says, pointing at the middle box, "is the single most important piece of configuration in the entire Health Data context. If we get it wrong, every downstream calculation is wrong. And it needs to be maintained by someone who understands both DHIS2 and the health indicators — which is approximately four people in Kenya."

Dr. Wanjiku speaks up. "The Division of Health Information maintains the official indicator reference. We can provide the authoritative mapping. But Raj is right — it requires ongoing maintenance as DHIS2 configurations change."

---

## Part C: Read Models — What Each User Sees

The facilitator switches the group's attention. "We have our aggregates. Now let us talk about what people actually see. Remember — aggregates are about data integrity and business rules. Read models are about answering specific questions for specific users. They can combine data from multiple aggregates, reshape it, summarize it, translate it."

He hands each persona a blank piece of paper. "Draw what you need to see. Not a wireframe. Just the information."

### Dr. Amina's Dashboard: "The TWG Briefing"

Dr. Amina does not draw. She writes a list.

"When I open CHART on a Monday morning before the TWG meets on Wednesday, I need to see:

1. A headline. 'OND-2026 Seasonal Risk Assessment for Kilifi County — 3 elevated risks identified.'
2. Each risk in a traffic-light format. Red for emergency, amber for alert, green for watch. With a one-sentence summary a non-expert can understand.
3. For each risk, the recommended actions with budget amounts. In Kenya shillings. Not dollars.
4. Which AWP line item each action maps to. I need to know if this is something I can fund from my existing budget or if I need to request additional funds.
5. The cost-of-inaction number. If I do nothing, this is what I will spend on emergency response. If I act now, this is what I spend proactively. Show me the difference.
6. Uncertainty warnings. If the confidence is below seventy percent, tell me plainly. Do not bury it.
7. A 'Submit to TWG' button that generates a formatted document matching our county planning template."

She pauses. "And for the love of all that is good, do not make me click through ten screens to find this. One page. One scrollable page."

### Joseph's Alert View: "The Supply Calculator"

Joseph draws a table:

| Facility | Disease | Current Stock | Predicted Need | Gap | Order By | KEMSA Lead Time | Status |
|----------|---------|--------------|----------------|-----|----------|-----------------|--------|
| Kilifi County Hospital | Malaria | AL: 5,000 doses | AL: 12,000 doses | 7,000 | 15-Aug | 30 days | ORDER NOW |
| Malindi Sub-County | Cholera | ORS: 2,000 | ORS: 8,000 | 6,000 | 01-Aug | 60 days | OVERDUE |
| Bamba Dispensary | Malaria | AL: 200 | AL: 800 | 600 | 15-Aug | 30 days | ORDER NOW |

"I need this at facility level. I need to sort by urgency. I need to see which orders are already overdue given KEMSA lead times. I need to export to Excel because that is what the county pharmacist accepts. And I need an aggregate view by sub-county for my weekly report."

### Sarah's Community Brief: "The CHW Toolkit"

Sarah draws something completely different from everyone else. She draws a single page with large text:

```
╔══════════════════════════════════════════════════╗
║  KILIFI NORTH - TAARIFA YA AFYA YA JAMII        ║
║  (Community Health Brief)                        ║
║                                                  ║
║  MSIMU: Oktoba-Novemba-Desemba 2026             ║
║                                                  ║
║  ⚠ TAHADHARI: Mvua nyingi zinatarajiwa.          ║
║    Malaria inaweza kuongezeka.                   ║
║                                                  ║
║  HATUA ZA KUCHUKUA:                              ║
║  1. Lala ndani ya neti ya mbu kila usiku         ║
║  2. Ondoa maji yaliyotuama karibu na nyumba      ║
║  3. Mtoto akipata homa, peleka hospitali SIKU    ║
║     HIYO HIYO                                    ║
║                                                  ║
║  TAREHE YA MKUTANO WA JAMII: 5 Oktoba 2026      ║
║  MAHALI: Baraza la Chief, Matsangoni             ║
╚══════════════════════════════════════════════════╝
```

"Printed on one page. In Swahili. With the Giriama translation on the back for the areas where Swahili is a second language. No graphs. No percentages. Action-oriented. And at the bottom, the date and location of the community meeting where the CHW will explain this in person."

The room is quiet for a moment. The gap between Sarah's information need and the aggregates on the whiteboard is enormous — and bridging it is exactly what a read model does.

### Peter's Feedback Report: "The Forecast Impact Tracker"

Peter writes a more structured request. "This is the one I have wanted for twenty years. I issue a forecast. It goes into the void. I never know if anyone used it or if it helped. I need:

- Which counties received this forecast through CHART
- Which counties generated adaptation plans based on it
- What actions were taken
- Three months later: what actually happened — was the forecast accurate? Were the actions effective? What was the outcome in terms of cases averted?

This closes the loop. This makes KMD relevant to health planning in a way we have never been."

### Dr. Wanjiku's NCCAP Alignment Report: "The National Dashboard"

Dr. Wanjiku describes a different kind of view entirely. "I need to aggregate across all forty-seven counties. I need to map county-level adaptation actions to National Climate Change Action Plan goals. I need to show the Cabinet Secretary a single page that says: 'This quarter, twenty-three counties used climate-informed health planning. Estimated cases averted: twelve thousand. Estimated cost savings: four hundred million shillings. NCCAP Goal 7.2 on health adaptation: forty-eight percent of counties compliant.'"

She adds: "And I need this formatted for the National Climate Change Council reporting template. Not a new format. Their format."

### The Realization

The Engineer has been writing furiously, listing all five views on the whiteboard. He steps back, counts them, looks at the aggregates, and then a visible shift crosses his face.

"These are not five different applications," he says slowly. "They are not five different databases. They are five different read models projecting from the same underlying aggregates."

He draws lines from the aggregates to the views:

```
         AGGREGATES                          READ MODELS
    ┌─────────────────┐
    │ SeasonalForecast │─────────────────┐
    └─────────────────┘                  │
    ┌─────────────────┐                  │
    │ HealthRisk      │──┬──┬──┬──┐      │
    │ Assessment      │  │  │  │  │      │
    └─────────────────┘  │  │  │  │      │
    ┌─────────────────┐  │  │  │  │      │
    │ InterventionMatch│──┤  │  │  │      │
    └─────────────────┘  │  │  │  │      │
    ┌─────────────────┐  │  │  │  │      │
    │ Seasonal        │──┤  │  │  ├────▶ Dr. Amina's Dashboard
    │ AdaptationPlan  │  │  │  │  │      (risk headlines + budget
    └─────────────────┘  │  │  │  │       + AWP mapping + CoI)
    ┌─────────────────┐  │  │  │  │
    │ SupplyPrePos    │──┘  │  │  ├────▶ Joseph's Alert View
    │ Order           │     │  │  │      (facility supply table
    └─────────────────┘     │  │  │       + KEMSA deadlines)
    ┌─────────────────┐     │  │  │
    │ DHIS2Health     │─────┘  │  ├────▶ Sarah's Community Brief
    │ Baseline        │        │  │      (Swahili plain language
    └─────────────────┘        │  │       + action items)
    ┌─────────────────┐        │  │
    │ Climatology     │────────┘  ├────▶ Peter's Feedback Report
    │ Baseline        │           │      (forecast → action →
    └─────────────────┘           │       outcome linkage)
    ┌─────────────────┐           │
    │ Environmental   │───────────┴────▶ Dr. Wanjiku's NCCAP
    │ Profile         │                  Alignment Report
    └─────────────────┘                  (cross-county aggregate
                                          + national indicators)
```

"Same data. Five projections. The LLM is a crucial part of this architecture — it is what generates Sarah's Swahili community brief from the same HealthRiskAssessment that generates Joseph's facility-level supply table. The LLM is a read model transformer."

Dr. Amina smiles. "So when Sarah needs the message in Giriama, we do not rebuild the assessment. We add a language parameter to the read model."

"Exactly."

Peter adds: "And when I need my feedback report, the system does not need a separate data collection effort. It just reads the existing adaptation plans and outcome data and projects them through my lens."

The Engineer writes in large letters at the top of the whiteboard: **WRITE MODEL = AGGREGATES (truth). READ MODELS = PROJECTIONS (views).**

---

## Part D: Context Map

The Engineer takes the last clean section of the whiteboard. "Let us draw the full context map. How do these bounded contexts relate to each other? Who talks to whom, and what language do they use at the boundary?"

He draws carefully:

```
                         CONTEXT MAP — CHART System
═══════════════════════════════════════════════════════════════════════

                    ┌──────────────────────────────┐
                    │     EXTERNAL: KMD SYSTEM      │
                    │  (Conformist — we accept      │
                    │   their format as-is)         │
                    └──────────────┬───────────────┘
                                   │ KMD bulletin PDF
                                   │ (parsed by CHART)
                                   ▼
  ┌────────────────────────────────────────────────────────────┐
  │                    CLIMATE INTELLIGENCE                     │
  │                                                            │
  │  Language: tercile probabilities, anomalies, SSP           │
  │           scenarios, return periods, ERA5 normals           │
  │                                                            │
  │  Key Aggregates:                                           │
  │    SeasonalForecast, ClimatologyBaseline,                  │
  │    EnvironmentalProfile                                    │
  │                                                            │
  └────────┬──────────────────────────────────────────────┬────┘
           │                                              │
           │ Published Language:                           │
           │   ClimateSignalDTO                            │
           │   {variable, magnitude,                       │
           │    probability, forecast_id}                  │
           │                                              │
           ▼                                              │
  ┌────────────────────────────────────────────┐          │
  │       HEALTH RISK TRANSLATION              │          │
  │       ★ CORE DOMAIN ★                      │          │
  │                                            │◄─────────┘
  │  Language: health outcomes, relative risk,  │   ERA5 baseline
  │           evidence grades, confidence       │   for anomaly
  │           scores, thresholds                │   context
  │                                            │
  │  Key Aggregates:                           │
  │    HealthRiskAssessment,                   │
  │    InterventionMatch                       │
  │                                            │
  │  ┌──────────────────────────────────┐      │
  │  │    SHARED KERNEL                 │      │
  │  │    (Action Repository)           │      │
  │  │                                  │      │
  │  │  InterventionDefinition schema   │      │
  │  │  (Pydantic contract)             │      │
  │  └──────────────┬───────────────────┘      │
  │                 │                          │
  └────────┬────────┼──────────────────────────┘
           │        │
           │        │ Shared Kernel
           │        │ (same schema, both sides)
           │        │
           │  ┌─────▼──────────────────────────────────────┐
           │  │       ADAPTATION PLANNING                   │
           │  │                                            │
           │  │  Language: AWP line items, budget codes,    │
           │  │           KES amounts, TWG approval,        │
           │  │           KEMSA procurement timelines        │
           │  │                                            │
           │  │  Key Aggregates:                           │
           │  │    SeasonalAdaptationPlan,                 │
           │  │    SupplyPrePositioningOrder               │
           │  │                                            │
           │  └──────────────────────────────────────────  ┘
           │
           │ Published Language:
           │   HealthBaselineDTO
           │   {indicator, baseline_mean,
           │    baseline_p75, completeness,
           │    quality_flag}
           │
  ┌────────┴──────────────────────────────────────────────┐
  │         HEALTH DATA                                    │
  │                                                        │
  │  Language: CHART indicator names (clean),              │
  │           completeness scores, facility metadata        │
  │                                                        │
  │  Key Aggregates:                                       │
  │    DHIS2HealthBaseline                                 │
  │                                                        │
  │  ┌──────────────────────────────────────────────┐      │
  │  │  ACL (Anti-Corruption Layer)                  │      │
  │  │                                              │      │
  │  │  DHIS2 UIDs ──→ CHART concepts               │      │
  │  │  Raw periods ──→ normalized periods           │      │
  │  │  Missing data ──→ flagged gaps                │      │
  │  └──────────────────────────────────────────────┘      │
  │                         ▲                              │
  └─────────────────────────┼──────────────────────────────┘
                            │
                    ┌───────┴──────────────────────┐
                    │     EXTERNAL: DHIS2 API       │
                    │  (Anti-Corruption Layer —      │
                    │   we translate their model     │
                    │   into ours)                   │
                    └──────────────────────────────┘
```

The Engineer adds annotations around the map:

**Relationship types used:**

```
CHART ──[Conformist]──▶ KMD System
  "We accept KMD's bulletin format. If they change it, we adapt.
   We have no leverage to ask them to change for us."

CHART ──[ACL]──▶ DHIS2
  "DHIS2 is a critical data source but its internal model is
   hostile to clean consumption. We build a translation layer
   and never let DHIS2 concepts leak into our core domain."

Climate Intelligence ──[Published Language]──▶ Health Risk Translation
  "ClimateSignalDTO is the contract. Climate Intelligence can
   change its internals freely as long as it produces valid DTOs."

Health Risk Translation ◄──[Published Language]── Health Data
  "HealthBaselineDTO is the contract. Same principle."

Health Risk Translation ──[Shared Kernel]──▶ Adaptation Planning
  "InterventionDefinition is co-owned. Changes require agreement
   from both contexts. Enforced via shared Pydantic schema in a
   common package."
```

Dr. Wanjiku looks at the map and points at a gap. "What about the feedback loop? Yesterday we said outcomes feed back into the system. Where does that appear?"

The Engineer adds a dashed line:

```
  Adaptation Planning ──── outcomes data ────▶ Health Data
       (what was done)    (3-6 months later)   (what happened)
                                                     │
                                                     ▼
                                              Health Risk Translation
                                              (recalibrate models)
                                                     │
                                                     ▼
                                              Climate Intelligence
                                              (forecast verification)
```

"The feedback loop crosses all four contexts," the Engineer says. "Outcomes observed in Health Data update the evidence base in Health Risk Translation and provide forecast verification data to Climate Intelligence. This is a long-running process — seasons, not seconds. We model it as domain events, not synchronous calls."

Peter is visibly moved. "Forecast verification. If CHART can tell me, six months after I issued a forecast, that my prediction of above-normal rainfall was correct and that the health interventions triggered by that forecast averted an estimated two thousand cases of malaria — that is the most meaningful feedback I have ever received in my career."

Dr. Amina stands and looks at the full context map. "I want to say something to this group. I have been in planning meetings for fifteen years. I have never seen anyone draw a map of how climate information becomes a health action. This map — these boxes and arrows — this is the institutional knowledge that exists in fragments across all of our heads. Nobody has ever put it together."

She turns to the Engineer. "Build this. Not all of it at once. But build the Health Risk Translation core first. That is the piece that does not exist anywhere today. Climate Intelligence exists in ClimSight. Adaptation Planning exists in our county processes, even if imperfectly. Health Data exists in DHIS2. The missing piece — the core domain — is the translation. Build that, and everything else connects."

The facilitator captures the moment with a photograph of the whiteboard, then writes the final sticky note of the workshop:

> **STRATEGIC CLASSIFICATION**
> - **Core Domain:** Health Risk Translation (build, differentiate, invest)
> - **Supporting Domain:** Climate Intelligence (leverage ClimSight, extend)
> - **Supporting Domain:** Adaptation Planning (model existing county processes)
> - **Generic Domain:** Health Data (integrate DHIS2, do not reinvent)
> - **Shared Kernel:** Action Repository (co-owned, Pydantic contract)

The whiteboard is full. The event storm wall is full. The room is full of yellow sticky notes and red lines and four different definitions of risk, now properly housed in four different bounded contexts that know exactly how to talk to each other.

*Phase 4 complete. The group breaks for lunch, and the Engineer opens a laptop to start translating aggregates into Pydantic models before the ideas cool.*

---



# Phase 5: SYNTHESIS — WHAT DID WE LEARN?

## Final 60 Minutes

The facilitator steps back from the wall. It spans nearly four metres now — a sprawling landscape of orange, blue, green, yellow, and pink sticky notes, connected by arrows drawn in marker, circled in different colours, punctuated by red exclamation marks at the hotspots. The Kilifi Bay breeze has loosened one corner of the butcher paper, and Sarah reaches over to press it back down.

"Alright," the facilitator says. "We've been standing at this wall for three and a half hours. We've generated" — she counts quickly — "forty-seven domain events, five aggregates, four bounded contexts, and about a dozen arguments. Now I want everyone to sit down, drink some water, and answer one question: **What did you learn today that you did not know when you walked in this morning?**"

Chairs scrape. Joseph refills his water bottle from the dispenser in the corner. Dr. Wanjiku checks her phone — three missed calls from Nairobi — and sets it face-down on the table.

"Let's go around the room," the facilitator says. "One discovery each. Then we'll see if the group found things nobody found alone."

---

## Part A: The 10 Discoveries

### Discovery 1: Dr. Amina — "We have data. We lack wiring."

Dr. Amina stands. She doesn't go to the wall — she's memorised it by now. She speaks slowly, the way someone does when they're rearranging their understanding in real time.

"I have been writing grant proposals for six years. Every single one says the same thing: *'County health systems lack adequate data for climate-responsive planning.'* I believed it. I believed it this morning when I walked in."

She pauses.

"I don't believe it anymore."

She points at Peter. "KMD has been producing seasonal outlooks since 2011. They're good. Peter showed us — the March-April-May 2023 outlook correctly predicted above-normal rainfall in the coastal strip. It was issued on 15 February." She points at Raj. "DHIS2 had malaria case data for every facility in Kilifi. Weekly. Going back to 2019." She points at a cluster of sticky notes near the middle of the wall. "KEMSA has a procurement pipeline. Not a great one, but it exists."

"So what's the problem?" She lets the question hang. "The problem is that nobody connects them. Peter's forecast goes to the County Commissioner's office, where it sits in a WhatsApp group. My DHIS2 data goes into the monthly MOH 711 report, where it becomes a table nobody reads until there's an outbreak. And KEMSA doesn't know either of these things exist."

She turns to the engineer. "CHART is not a data source. I want to be very clear about this because if you build it as a data source, we already have those and they're not helping. CHART is a **connector**. It's a translation layer. It takes three things that already exist — forecasts, case data, supply chains — and wires them together so that a decision falls out the other end."

The room is quiet. Joseph is nodding.

"That's what I learned," Dr. Amina says. "The gap isn't information. The gap is translation."

---

### Discovery 2: Peter — "My forecasts enter a void."

Peter clears his throat. He's the quietest person in the room, and he speaks with the careful precision of someone who works in probabilities for a living.

"Fifteen years," he says. "I have been producing seasonal outlooks for fifteen years. First at the regional centre in Nairobi, then for the county-level downscaled products. Every season: MAM, JJAS, OND. Three outlooks a year. That's forty-five outlooks."

He looks at his hands. "Until today, I have never been in a room where someone told me what happened after they received one."

Sarah shifts uncomfortably. Dr. Amina looks at the table.

"I'm not blaming anyone," Peter says quickly. "The format is wrong. I know that now. I write: *'There is a 45% probability of above-normal rainfall in the coastal and southeastern lowlands during the March-April-May season.'* That is a correct statement. But Dr. Amina cannot take that to the county assembly. She cannot take a probability to a procurement meeting."

He stands and walks to the wall, pointing at the sticky note where the group identified the translation gap — the orange note reading **KMD Outlook Issued** next to the pink note reading **AWP Budget Line Exists** with a wide gap between them annotated in red marker: **NOBODY DOES THIS**.

"What she needs is: *'Based on the seasonal outlook, Kilifi County should expect approximately 15-25% more rainfall than normal during April and May, which based on historical patterns is associated with a 30-40% increase in malaria cases in lowland sub-counties. This means an estimated additional 3,200 cases requiring approximately 4,800 additional courses of ACTs and 2,000 additional RDTs.'*"

He turns to face the group. "I cannot produce that statement. I am a meteorologist, not a doctor. But CHART can produce it — because CHART has both my forecast AND Dr. Amina's case data AND the historical relationship between them."

He sits down. "That is my discovery. My forecasts are useful. They have always been useful. They just need a translator."

---

### Discovery 3: Joseph — "I have to order before I see."

Joseph stands up fast, the way someone does when they've been holding something in.

"I want to talk about KEMSA," he says. "I have been a disease surveillance officer for nine years. My entire training — all of it — is about **response**. I see cases go up on the DHIS2 dashboard. I investigate. I report. I request supplies."

He walks to the wall and puts his finger on the sticky note labelled **KEMSA Order Placed**. "This note says 6-8 weeks lead time. **Six to eight weeks.** Do you understand what that means?"

He traces the timeline they mapped in Phase 2 — the four parallel tracks running across the wall.

"The KMD outlook comes out in mid-February for the March-April-May season. The rains start in mid-March. Malaria cases start rising in late April — four to six weeks after the rains. They peak in June." He taps the KEMSA note. "If I wait until I *see* cases in late April and then order, the supplies arrive in **July**. The peak is in June. I've missed it entirely."

He turns around. "This means I have to place my order in **February** — before a single additional case has appeared. I have to order based on a *forecast*, not an *observation*. This is the complete opposite of everything I was trained to do."

The room absorbs this. Dr. Amina is drawing a timeline on her notepad.

"Currently," Joseph continues, "my order trigger is: *cases exceed threshold → request supplies*. CHART's order trigger has to be: *forecast indicates likely case increase → pre-position supplies*. That's not surveillance. That's **anticipatory logistics**. I've never done it. Nobody in my office has done it. And we can't do it without something that tells us how many additional courses of ACTs to order based on a rainfall probability."

He sits down. "I didn't know any of this at nine o'clock this morning."

---

### Discovery 4: Sarah — "My knowledge has a system now."

Sarah has been quiet for the last hour of the workshop, scribbling notes on the back of an envelope. She stands slowly.

"I was worried about today," she says. "Everyone here has degrees. Doctor this, engineer that. I'm a community health worker supervisor. I finished secondary school in Malindi. When I got the invitation, I almost didn't come."

Dr. Amina starts to say something, but Sarah holds up her hand.

"Let me finish. I almost didn't come. But then during the event mapping, when I said — 'the bridge to Kibaoni floods every April and when it floods the ambulance from Kilifi South Sub-County Hospital cannot cross, and the 4,200 people in Kibaoni and Mwangea have no emergency access for three to four weeks' — suddenly everyone was writing sticky notes."

She's right. The facilitator looks at the wall. There are four sticky notes directly traceable to Sarah's comment: **Access Route Blocked** (orange domain event), **Facility Accessibility Assessment** (blue command), **Pre-Position Supplies at Cut-Off Facilities** (green policy), and a red exclamation mark with the note **"What else don't we know about physical access?"**

"Peter's satellite doesn't know about that bridge," Sarah says. "DHIS2 doesn't know about that bridge. But I know about it because I walk across it every Tuesday on the way to the Kibaoni community health unit. And I know twenty more things like it. The borehole at Chasimba that goes saline during the dry season. The path to Ruruma dispensary that becomes impassable when the Sabaki River is high. The fact that Uyombo Health Centre's cold chain fails every time there's a power cut during a storm, which is every major storm."

She looks at the engineer. "My knowledge matters. It always mattered. It just never had a **system** to live in. If CHART gives it a system — if there's a place where I can say *'this road floods at this GPS coordinate when rainfall exceeds this amount'* — then I'm not just a CHW supervisor. I'm a sensor."

The engineer is writing fast. He underlines the word **sensor** twice.

---

### Discovery 5: Raj — "The inconsistency is worse than you think."

Raj stands. He's been unusually tense all day — the person who knows where the bodies are buried and has been waiting for someone to ask.

"I need to show you something," he says. He opens his laptop and turns it so the room can see. "This is the DHIS2 instance for Kilifi County. I'm going to search for malaria."

He types. The screen fills with results.

"Here is the indicator for confirmed malaria cases. Its UID is `bMcwwoVXbDz`. This is the correct, national-level indicator aligned to the MOH 711 reporting form." He pauses. "Now let me show you Mombasa County."

He switches to another browser tab. "Same indicator. Confirmed malaria cases. UID: `Tt5TAvdfdVK`."

Joseph frowns. "Why is it different?"

"Because Mombasa created a custom indicator in 2018 when they were doing a malaria micro-stratification exercise. They never deleted it. They never re-mapped it. Their weekly malaria data has been going into a **county-specific indicator** for five years."

Raj switches tabs again. "Kwale County. They have *three* UIDs for malaria. One for outpatient confirmed cases: `jK4enb5kPQj`. One for inpatient: `qX9IDfnVqho`. And one for 'malaria tested,' which someone set up in 2020 during a data quality assessment and which is still receiving data: `RhJbg8rOBJN`. The outpatient indicator is missing data for all of 2021 because someone changed the data entry form and forgot to re-link it."

The room is silent.

"I have more," Raj says. He's not enjoying this. "Precipitation. In the DHIS2 climate module pilot — the one WHO supported in 2019 — rainfall data was entered manually by facility staff. In Kilifi, the unit is millimetres. In Kwale, someone entered it in centimetres for six months before anyone noticed. In Mombasa, the data element was created but never populated. It has zero values for every period."

He closes the laptop. "The anti-corruption layer we discussed in Phase 4 — the one that normalizes DHIS2 data before CHART can use it — is not optional. It is not a nice-to-have. If CHART consumes raw DHIS2 data, it will produce nonsense. It will tell Dr. Amina that Mombasa had zero malaria cases in 2022 because it was reading from the wrong indicator. It will tell her that Kwale had twice as many cases as Kilifi because it was double-counting outpatient and tested."

He looks at the engineer. "Build the anti-corruption layer first. Before the agents. Before the risk assessment. Before anything. Because if the input data is wrong, everything downstream is wrong, and nobody will trust CHART again after one bad report."

The engineer nods slowly. On his notepad he writes: **DHIS2 ACL = prerequisite, not component.**

---

### Discovery 6: Dr. Wanjiku — "Five counties give me a national report."

Dr. Wanjiku has been watching the bounded context discussion with particular interest. She stands now with the energy of someone who's seen a solution to a problem she wasn't allowed to talk about.

"I came here thinking CHART was a county tool," she says. "A tool for Dr. Amina. Good for Kilifi, maybe useful for a few other coastal counties. I was here as a stakeholder, not a user."

She walks to the wall and points at the read model they designed for her persona — the **National Aggregation Dashboard**.

"I was wrong. Let me explain what my life is like. Kenya submitted its updated National Climate Change Action Plan — the NCCAP 2023-2027 — in 2023. It commits us to 'climate-resilient health systems' and 'integrated climate-health surveillance.' Beautiful language. The problem is reporting. Every year, I have to report to the National Climate Change Council on what the health sector has actually *done*. How many adaptation actions were implemented. What they cost. What outcomes they produced."

She picks up a marker and draws on the butcher paper: a large arrow pointing from the county-level bounded contexts up to a box labelled **NCCAP Report**.

"Currently, I get this information by sending emails to forty-seven counties and receiving replies from maybe twelve, in twelve different formats, three months late. It takes my team four months to compile the national health adaptation report. By the time we submit it, the data is eighteen months old."

She turns to face the group. "If five counties use CHART — just five — Kilifi, Mombasa, Kwale, Tana River, Lamu — I can aggregate their adaptation plans automatically. CHART already produces structured output: interventions, costs, timelines, health outcomes. If the output schema is standardized — and we designed it to be — then national aggregation is a **query**, not a research project."

She pauses. "CHART isn't a county tool. It's a county tool that produces national reporting as a side effect. And that side effect is what will get the national government to fund its rollout."

Dr. Amina is smiling. "That's the budget argument I've been looking for."

---

### Discovery 7: The Engineer — "We need fewer agents than I thought."

The engineer stands. He's been the most active person at the wall all day, and his hands are stained with marker ink in four colours.

"I came in with an architecture diagram," he says. "Nine agents. I was proud of it. It was clean, modular, and completely wrong."

He walks to the wall and points at the bounded context map.

"Looking at this wall, I can see that three of my proposed agents aren't agents at all. Let me explain what I mean by that."

He picks up a marker. "An **agent** is something that makes decisions under uncertainty. It reasons, it plans, it adapts. A **tool** is something that executes a defined function given defined inputs. A **retrieval** is something that finds and filters information."

He draws three columns on a blank section of butcher paper.

"**Health Risk Assessment** — I had this as an agent. It's not. It takes a climate forecast, looks up historical health correlations for that location, and computes a risk score. There's no reasoning involved. It's a function. It's a **tool**."

"**Intervention Matching** — I had this as an agent. It's not. It takes a risk profile, queries the Action Repository for interventions that match the disease, the risk level, and the budget, and returns a ranked list. That's **retrieval plus filtering**. Not agentic."

"**Data Analysis** — this IS an agent. It has to write code to compute things we can't pre-define. If Dr. Amina asks 'what would happen if I shifted 20% of my malaria budget to dengue preparedness,' the agent needs to reason about that, generate a computation, execute it, check the result, and possibly revise. That's agentic."

"**Synthesis** — this IS an agent. Turning structured data into a politically-framed adaptation plan that Dr. Amina can present to the county assembly requires understanding audience, emphasis, and framing. That's reasoning under uncertainty."

He writes on the butcher paper:

```
AGENTS (truly agentic):
  1. Data Analysis Agent (code generation, computation)
  2. Synthesis/Combine Agent (political framing, narrative)

TOOLS (deterministic functions):
  3. Climate Data Extraction
  4. Health Risk Assessment
  5. DHIS2 Data Retrieval (with anti-corruption layer)
  6. ERA5 Climatology Extraction
  7. Intervention Matching (retrieval + filter from Action Repository)

ORCHESTRATION:
  - LangGraph state machine routes between them
  - The graph IS the "planning agent" — no separate planner needed
```

"Seven components. Two agents, five tools, one orchestration layer. Not nine agents. The wall told me that."

---

### Discovery 8: COLLECTIVE — "Four clocks, zero synchronisation."

The facilitator stands. "Now let's talk about what the *group* discovered that no individual brought in."

She walks to the Phase 2 timeline — the four parallel tracks still visible on the wall, annotated with red markers where they misalign.

"I want everyone to look at these four timelines and tell me what you see."

Silence. Then Joseph speaks.

"They're all on different calendars."

"Exactly," the facilitator says. "Let's list them."

She writes on a fresh sheet of butcher paper as the group calls them out:

| Cycle | Calendar | Key Dates |
|---|---|---|
| **KMD Seasonal Outlook** | Three seasons: MAM, JJAS, OND | Issued ~6 weeks before season start (mid-Feb, mid-Jun, mid-Sep) |
| **County AWP Budget** | Fiscal year: July → June | Draft due November, approved January-February, disbursement starts March |
| **KEMSA Procurement** | Rolling, 6-8 week lead time | Orders can be placed anytime, but emergency orders take 12+ weeks |
| **Disease Transmission** | Ecological, follows rainfall with 4-6 week lag | MAM peak: June. OND peak: January-February |

Peter stares at the table. "The MAM outlook is issued in mid-February. The AWP is already approved by then. There's no budget line for anything the forecast might tell us."

Dr. Amina nods grimly. "Unless we built the forecast INTO the AWP during drafting. Which means CHART needs to produce a **preliminary risk assessment** in October or November, based on the best available forecast at that time, so I can include contingency budget lines in the draft AWP."

"But I don't issue the MAM outlook until February," Peter says.

"So what do you have in October?" Dr. Amina asks.

"The global model runs. The ENSO outlook. The Indian Ocean Dipole status. I could produce a preliminary probability — very rough — but I never have because nobody has ever asked me to."

The facilitator writes in red marker: **CHART's hardest job is not the AI. It's synchronising four clocks.**

The engineer adds: "This means the system needs to operate in at least two modes. An **early warning mode** in October-November that produces rough estimates for AWP planning, and a **tactical mode** in February-March that refines those estimates for procurement. Same pipeline, different confidence levels, different outputs."

Dr. Wanjiku, watching from the side of the room, says: "This is why every climate-health project fails. They build beautiful dashboards that produce information at the wrong time for the decisions that need to be made. CHART has to be designed around the **decision calendar**, not the **data calendar**."

The facilitator underlines this three times.

---

### Discovery 9: COLLECTIVE — "The TWG is not overhead. It's the legitimacy engine."

The discussion about the Technical Working Group review step — the one flagged in Phase 3 as a potential bottleneck — resurfaces unexpectedly.

The engineer raises it. "I want to revisit the TWG review. In my original design, I had it as optional. A 'human-in-the-loop' that could be turned off once the system proved reliable. Looking at the wall, I think I was wrong, but I want to hear from the people who actually sit on TWGs."

Dr. Amina doesn't hesitate. "If you remove the TWG review, I will not use CHART."

The room goes quiet.

"Let me explain," she says. "When I take an adaptation plan to the county assembly — to the Budget Committee, chaired by the Member of County Assembly for Kaloleni — I need to be able to say: *'This plan was reviewed and endorsed by the County Health Management Team and the technical working group.'* If I say: *'This plan was produced by an AI system,'* I will be laughed out of the chamber. And I will deserve it."

Joseph adds: "It's not just politics. The TWG catches errors. Last year, the national malaria programme recommended distributing long-lasting insecticidal nets in August. The TWG pointed out that August is the dry season on the coast — there are no mosquitoes. The nets would be stolen or repurposed before the rains came. They shifted distribution to February. No algorithm would have caught that."

Peter nods. "In meteorology, we have the same principle. The automated forecast goes through a human forecaster who checks it against local knowledge before it's issued. We call it 'forecaster-in-the-loop.' Not because the automation is wrong — usually it's right — but because when it's wrong, it's wrong in ways that destroy credibility for years."

The facilitator writes: **TWG review = legitimacy engine. Removing it makes CHART faster but unusable. Build the review step as a CORE feature, not an afterthought.**

The engineer crosses out a line in his notebook. "I had a 'bypass TWG' configuration flag. I'm removing it. The TWG step is mandatory. The system should make the review as easy as possible — structured output, highlighted assumptions, one-click approve/request-revision — but it cannot be skipped."

---

### Discovery 10: COLLECTIVE — "The feedback loop is the adoption flywheel."

The facilitator points to the very last sticky note on the wall — a green one that Sarah added during the unhappy-path discussion: **KMD Never Learns If Forecast Was Useful.**

"This one almost fell off the wall," the facilitator says. "But I think it might be the most important note up there. Let's talk about it."

Peter speaks first, and there's an edge of frustration in his voice that hasn't been there all day.

"You know what I receive after issuing an outlook? Nothing. Silence. I have no idea if the February 2023 forecast helped anyone. I have no idea if the rainfall materialised as predicted. I mean, I know from the rain gauge data eventually — but I don't know if the health system used it, if they ordered supplies, if the supplies arrived, if cases went up, if the forecast was relevant to any decision anyone made."

He pauses. "So every season, I produce the next outlook with the same assumptions, the same format, the same distribution list. I have no feedback signal. I'm optimising in the dark."

Dr. Amina turns to him. "What if, at the end of each season, CHART sent you a report? Something like: *'Your MAM 2026 outlook predicted above-normal rainfall in Kilifi. Actual rainfall was 127% of the long-term mean. Based on your forecast, Kilifi County pre-positioned 4,800 additional courses of ACTs. Malaria cases increased by 34%, consistent with the predicted risk level. The pre-positioned supplies were deployed to 12 facilities, covering 89% of the additional caseload. Estimated lives saved: 18-24.'*"

Peter stares at her. "If I received that report, I would spend the next six months improving my coastal downscaling model. I would fight my director for the budget to maintain the Kilifi automatic weather station. I would — " He stops. "I would know my work mattered."

The facilitator writes slowly: **Feedback from CHART to KMD = the adoption flywheel.**

The engineer picks up the thread. "This is a systems dynamics insight. If Peter gets feedback, he improves his forecasts. If forecasts improve, CHART's risk assessments improve. If risk assessments improve, Dr. Amina trusts the system more. If she trusts it more, she uses it more. If she uses it more, there's more data to feed back to Peter. It's a virtuous cycle."

He draws it on the butcher paper:

```
Better forecasts → Better risk assessments → Better plans
       ↑                                          ↓
  Improved KMD    ←    Feedback reports    ←   Outcomes
  downscaling            to Peter              tracked
```

"Without the feedback loop," he says, "CHART is a one-shot tool. With it, CHART is a **learning system** that gets better every season. The feedback mechanism isn't Phase 3. It's **Phase 1**. If we don't build it from the start, we won't have the data to make it work later."

Dr. Wanjiku adds quietly: "This is also what I need for NCCAP reporting. Did the adaptation plan work? What was the health outcome? The feedback loop gives me impact data, not just activity data. That's what the international climate finance mechanisms want to see."

The facilitator steps back. Ten discoveries are on the wall now, each one challenging an assumption the group held when they walked in. She photographs them all.

---

## Part B: Priority Dot-Vote

The facilitator reaches into her bag and pulls out a sheet of coloured dot stickers — red, blue, and green. She tears off strips and hands three dots to each person.

"Seven people, three dots each. Twenty-one dots total. I've listed the major components we identified. Vote for what we should build FIRST."

She writes the candidates on a clean sheet:

```
1. DHIS2 Anti-Corruption Layer (data normalization)
2. Climate Forecast Ingestion (KMD outlook → structured data)  
3. Health Risk Assessment (forecast → disease risk scores)
4. Intervention Matching (risk → costed interventions from Action Repository)
5. AWP-Formatted Output (structured plan → county assembly document)
6. TWG Review Interface (approve/revise/reject workflow)
7. Feedback Report to KMD (season-end outcome report)
8. ERA5/Climate Data Pipeline (historical baseline extraction)
```

People stand, stickers in hand, and move to the wall.

**Raj** places all three dots on #1 (DHIS2 Anti-Corruption Layer). "Without clean input data, nothing else works." Nobody is surprised.

**Peter** puts one dot on #2 (Forecast Ingestion), one on #7 (Feedback Report), and one on #3 (Risk Assessment). His priorities are the bookends — getting his data in and getting results back.

**Joseph** places two dots on #4 (Intervention Matching) and one on #1 (DHIS2 Anti-Corruption Layer). "I need to know WHAT to order and HOW MUCH. That's intervention matching."

**Sarah** puts one dot on #5 (AWP-Formatted Output) — "because if Dr. Amina can't use it, we built nothing" — one on #6 (TWG Review), and one on #1 (DHIS2 Anti-Corruption Layer).

**Dr. Wanjiku** distributes evenly: one on #5 (AWP Output), one on #7 (Feedback Report), one on #3 (Risk Assessment).

**The Engineer** places dots on #1 (DHIS2 ACL), #3 (Risk Assessment), and #8 (ERA5 Pipeline). The technical foundation.

**Dr. Amina** has been standing in front of the wall for a full minute, dots in hand, not placing them. The room waits.

She puts all three dots on #5 (AWP-Formatted Output).

The facilitator tallies:

```
#1  DHIS2 Anti-Corruption Layer:    ████  (4 votes)
#5  AWP-Formatted Output:           ████  (4 votes)  
#3  Health Risk Assessment:          ███  (3 votes)
#7  Feedback Report to KMD:          ██  (2 votes)
#4  Intervention Matching:            ██  (2 votes)
#2  Climate Forecast Ingestion:       █  (1 vote)
#6  TWG Review Interface:             █  (1 vote)
#8  ERA5/Climate Data Pipeline:       █  (1 vote)
```

"It's a tie," the facilitator says. "DHIS2 cleanup and AWP output. The plumbing and the packaging."

An argument breaks out — politely, but with force.

**The Engineer** makes the case for the risk assessment. "Logically, you build from the bottom up. Clean the data, compute the risk, match the interventions, format the output. You can't format an output you haven't computed."

**Raj** agrees. "The anti-corruption layer is the foundation. Everything is built on top of it."

**Dr. Amina** shakes her head. "No. I understand the engineering logic. But you're wrong about what will happen in practice."

She stands. "Let me tell you what will happen if you build the risk assessment first. You'll spend four months building a beautiful risk model. You'll show it to me. I'll say: *'This is very interesting. What do I do with it?'* You'll say: *'We're building the output module next.'* I'll say: *'Call me when it's ready.'* And I'll go back to doing things the way I've always done them."

She pauses. "Now let me tell you what happens if you build the output first. You come to me in four weeks with a mock adaptation plan. It's formatted like my AWP. It has budget lines I recognise. It has intervention names from the Kenya Essential Package for Health. It has a column for 'climate rationale' that I can show the county assembly. The numbers are fake — placeholder data — but the FORMAT is right."

"I will take that mock-up to my next County Health Management Team meeting. I will say: *'This is what CHART will produce. Does this format work for our planning process?'* My team will give feedback. They'll say: *'Add a column for sub-county breakdown. Change the budget categories to match the IFMIS codes. Include the facility-level distribution plan.'* And now you have REAL requirements from REAL users."

She looks at the engineer. "If the output doesn't look like something I can take to the county assembly, I will never use it — no matter how accurate the risk assessment is. The output format is not the last thing you build. It's the FIRST thing you validate."

Silence.

The engineer writes in his notebook: **Output-first development. Validate the container before filling it.**

The facilitator marks the resolution: "Priority 1: AWP-formatted output mock-up with placeholder data, validated by Dr. Amina's team. Priority 2: DHIS2 anti-corruption layer. Priority 3: Health risk assessment. These three become the MVP."

---

## Part C: Commitments and Next Steps

The facilitator distributes index cards. "Write down one specific thing you will deliver, with a date, that moves CHART forward. This is not aspirational. This is a commitment."

Each person writes. Then reads aloud.

---

**Dr. Amina** stands first. "I will provide three real Annual Work Plans from Kilifi County — FY 2023/24, 2024/25, and the current 2025/26 draft — within two weeks. I will redact any sensitive budget figures and replace them with representative numbers, but the FORMAT, the line items, the structure, the IFMIS codes, and the county assembly presentation template will all be authentic. I will also include one example of a supplementary budget request triggered by a disease outbreak, so the team can see what an emergency budget modification looks like."

**Delivery: 19 March 2026.**

---

**Peter** nods. "I will provide six historical seasonal outlooks in machine-readable format. MAM and OND for 2023, 2024, and 2025. Currently these exist only as PDF documents with maps. I will extract the county-level probability terciles into a CSV file with columns for county, season, below-normal probability, near-normal probability, and above-normal probability. I will also include the raw ENSO and IOD index values that informed each outlook."

He adds: "This is not a trivial task. I will need to reconstruct some of the data from archived model runs. But I can do it."

**Delivery: 2 April 2026.**

---

**Joseph** stands. "I will map the KEMSA procurement process for Kilifi County with exact timelines. This means: date of order submission, date of order acknowledgment, date of dispatch, date of delivery to county depot, date of distribution to sub-county stores, and date of delivery to individual facilities. I will do this for three actual orders from the last twelve months — one routine quarterly order, one emergency order placed during the 2025 dengue outbreak, and one that was delayed. I will note every bottleneck and the actual duration of each step."

**Delivery: 26 March 2026.**

---

**Sarah** looks at her index card. "I will document twenty local knowledge items about flood-prone areas and facility access in Kilifi County. For each item, I will record: the GPS coordinates, the type of hazard — flooding, road washout, bridge collapse, landslide — the approximate rainfall threshold that triggers it, the facilities and populations affected, and the typical duration of access disruption. I already know most of these from memory. I will verify them with my CHWs during our next monthly meeting."

She adds, almost as an afterthought: "I will also take photos. You engineers like photos."

**Delivery: 26 March 2026.**

---

**Raj** is already typing on his laptop. "I will create a DHIS2 indicator mapping document for three counties: Kilifi, Mombasa, and Kwale. For each county, I will list every health indicator relevant to climate-sensitive diseases — malaria, dengue, cholera, acute respiratory infections, diarrhoeal diseases, malnutrition — with its UID, its name, its data element composition, its reporting frequency, and the date range for which data is available. I will flag every inconsistency: duplicate indicators, missing data periods, unit mismatches, and deprecated data elements that are still receiving data."

He looks up. "This will be ugly. The document will probably be forty pages long. But it's necessary."

**Delivery: 9 April 2026.**

---

**Dr. Wanjiku** stands. "I will share the NCCAP reporting template — the one my division uses to report health sector adaptation actions to the National Climate Change Council. I will also share the Kenya Health Sector Adaptation Plan monitoring framework, which specifies the indicators we report against. If CHART's output schema can be mapped to these templates, national aggregation becomes automatic."

She pauses. "I will also provide a letter of support from the Division of Environmental Health. Not legally binding, but it signals national interest. That letter will help Dr. Amina's budget request at the county level."

**Delivery: 19 March 2026.**

---

**The Engineer** is last. He stands and speaks carefully.

"I commit to building a prototype of Dr. Amina's read model within four weeks. This will be a Streamlit interface that displays a mock Seasonal Adaptation Plan formatted as an AWP addendum. It will use placeholder data — fake risk scores, fake intervention lists, fake budget numbers — but the structure will match the real AWP format that Dr. Amina provides."

"The purpose is not to demonstrate AI. The purpose is to validate the output format before we build the AI that generates it. Dr. Amina's team will review the mock-up and provide feedback. We will iterate on the format until they say: *'Yes, I could take this to the county assembly.'* Only then will we build the pipeline that fills it with real data."

He adds: "I will also set up a shared repository where all the committed documents — AWPs, forecasts, KEMSA timelines, DHIS2 mappings, local knowledge database — can be collected and version-controlled."

**Delivery: 2 April 2026 (prototype); 12 March 2026 (shared repository).**

---

The facilitator collects all the index cards and photographs them. "These are binding. I'll send a follow-up email on Monday with all commitments and dates. If anyone is blocked, contact the engineer — he's the integrator."

---

## Part D: The Wall Photo

The facilitator picks up her phone and moves to the far end of the conference room. She needs the widest angle possible. The wall stretches nearly four metres — two sheets of butcher paper taped together, every centimetre covered.

She takes six overlapping photos, then one panorama.

Here is what the wall looks like:

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                     │
│  ┌─ZONE 1: AS-IS EVENTS──────────────────────────────────────────────────────────┐  │
│  │                                                                               │  │
│  │  [KMD Outlook    [Outlook Shared    [County Receives    ██████████████████    │  │
│  │   Produced]       via WhatsApp]      PDF]               ██  GAP: NOBODY  ██    │  │
│  │   (orange)        (orange)           (orange)           ██  TRANSLATES   ██    │  │
│  │                                                         ██  THIS INTO    ██    │  │
│  │  [DHIS2 Data     [Monthly MOH 711   [Annual Report     ██  BUDGET LINES ██    │  │
│  │   Entered at      Compiled]          Submitted]         ██████████████████    │  │
│  │   Facility]       (orange)           (orange)                  │              │  │
│  │   (orange)                                              (RED EXCLAMATION)     │  │
│  │                                                                               │  │
│  │  [KEMSA Order    [8 Weeks Pass]     [Supplies Arrive   [Outbreak Already      │  │
│  │   Placed]         (orange)           at County Depot]    Peaked]              │  │
│  │   (orange)                           (orange)            (HOTSPOT 🔴)         │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                     │
│  ┌─ZONE 2: FOUR PARALLEL TIMELINES (Phase 2)────────────────────────────────────┐  │
│  │                                                                               │  │
│  │  AWP:     |--Nov Draft--|--Jan Approve--|--Mar Disburse--|                    │  │
│  │  KMD:          |--Feb Outlook--|                    |--Sep Outlook--|         │  │
│  │  KEMSA:   |.....6-8 wks.....|.....6-8 wks.....|.....6-8 wks.....|          │  │
│  │  Disease: |         |--Apr Rains--|--Jun Peak--|              |--Jan Peak--| │  │
│  │                                                                               │  │
│  │  RED ARROWS marking misalignments between all four tracks                     │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                     │
│  ┌─ZONE 3: TO-BE PROCESS MODEL (Phase 3) ───────────────────────────────────────┐  │
│  │                                                                               │  │
│  │  [Ingest        [Extract         [Compute        [Match            [Generate │  │
│  │   KMD            DHIS2            Health          Interventions     AWP       │  │
│  │   Outlook]       Baseline]        Risk]           from Action       Addendum] │  │
│  │   (blue cmd)     (blue cmd)       (blue cmd)      Repository]       (blue)   │  │
│  │      │              │                │             (blue cmd)           │      │  │
│  │      ▼              ▼                ▼                │                ▼      │  │
│  │  [Climate       [DHIS2 Health    [Health Risk     [Intervention    [Seasonal │  │
│  │   Intelligence]  Data BC]         Translation     Plan             Adapt.    │  │
│  │   (circled       (circled         BC]             Generated]        Plan      │  │
│  │    BLUE)          PURPLE)         (circled         (orange)         Produced] │  │
│  │                                    GREEN)                           (orange)  │  │
│  │                                                                       │      │  │
│  │                                                          ┌────────────┘      │  │
│  │                                                          ▼                    │  │
│  │                                                   [TWG Reviews    [Plan       │  │
│  │                                                    Plan]          Approved    │  │
│  │                                                    (yellow        OR          │  │
│  │                                                     policy)      Revised]     │  │
│  │                                                                   (orange)    │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                     │
│  ┌─ZONE 4: BOUNDED CONTEXTS (Phase 4)───────┐  ┌─ZONE 5: AGGREGATES ───────────┐  │
│  │                                           │  │                               │  │
│  │   ╔═══BLUE═══╗    ╔══GREEN═══╗           │  │  HealthRiskAssessment (tool)  │  │
│  │   ║ Climate  ║    ║ Health   ║           │  │  InterventionMatch (retrieval)│  │
│  │   ║ Intel.   ║───>║ Risk     ║           │  │  SeasonalAdaptationPlan (agg) │  │
│  │   ╚══════════╝    ║ Transl.  ║           │  │  SupplyPrePosition (agg)      │  │
│  │                    ╚══════════╝           │  │  DHIS2HealthBaseline (agg)    │  │
│  │   ╔═PURPLE════╗         │                │  │                               │  │
│  │   ║ Health    ║         ▼                │  │  ┌─SHARED KERNEL──────────┐   │  │
│  │   ║ Data      ║   ╔══ORANGE══╗           │  │  │ Action Repository     │   │  │
│  │   ║ (DHIS2)   ║──>║ Adapt.  ║           │  │  │ (110+ interventions)  │   │  │
│  │   ╚══════════╝    ║ Planning ║           │  │  └───────────────────────┘   │  │
│  │                    ╚══════════╝           │  │                               │  │
│  └───────────────────────────────────────────┘  └───────────────────────────────┘  │
│                                                                                     │
│  ┌─ZONE 6: 10 DISCOVERIES (Phase 5) ────────────────────────────────────────────┐  │
│  │                                                                               │  │
│  │  1. CHART = connector    4. Sarah = sensor    7. 7 not 9 components          │  │
│  │  2. Forecasts need       5. DHIS2 ACL is      8. Four clocks problem         │  │
│  │     translator              prerequisite       9. TWG = legitimacy            │  │
│  │  3. Order before see     6. 5 counties =      10. Feedback = flywheel        │  │
│  │                             national report                                   │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                     │
│  DOT VOTES: #5 AWP Output ████  #1 DHIS2 ACL ████  #3 Risk Assessment ███       │  │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

The facilitator looks at it one more time. "That's three and a half hours of work by seven people who didn't know each other this morning. Not bad."

She turns off the lights as the group files out, the wall still glowing with coloured stickies in the afternoon light from the window overlooking Kilifi Creek.

---

## Part E: What This Simulation Got Wrong

This EventStorming workshop was a simulation — conducted by an AI reasoning about what would happen if these people gathered in a room. It is useful. It is also, in several important ways, likely wrong. Intellectual honesty requires flagging where.

### 1. Persona Availability

The simulation assumes all seven participants spent four hours in a room together. In reality:

- **Dr. Amina** (County Health Director) is one of the busiest public officials in the county. Getting four uninterrupted hours would require scheduling months in advance and competing with county assembly sessions, partner meetings, and outbreak responses. She would more likely send a deputy — who would not have the same authority to make commitments.
- **Peter** (KMD forecaster) is based in Nairobi, not Kilifi. He might join virtually, which fundamentally changes the dynamics of standing at a wall together.
- **Dr. Wanjiku** (national MOH) would almost certainly not attend a county-level workshop in person. Her participation would be a 30-minute virtual presentation at best.
- **Sarah** (CHW supervisor) might not be invited at all. Health system workshops in Kenya tend to be populated by officers, not frontline workers. Her inclusion would require deliberate facilitation choices.

### 2. Undiscoverable Domain Events

The simulation generated events based on documented processes and reasonable inference. A real workshop would surface events that no amount of desk research can anticipate:

- Internal politics between the county Department of Health and Department of Finance that block budget modifications
- Specific donor-funded programmes (e.g., a Global Fund malaria grant) that have their own supply chains parallel to KEMSA and that cover 60% of ACTs in the county — making the KEMSA timeline less relevant than we assumed
- County-specific data quirks: perhaps Kilifi's DHIS2 instance was migrated in 2022 and lost three months of data
- The existence of a parallel WhatsApp-based early warning system that CHWs already use informally and that CHART would need to integrate with, not replace
- Inter-county dynamics — Kilifi and Mombasa share a county referral hospital, and disease surveillance data flows between them in undocumented ways

### 3. Assumptions About Kenya's Health System That May Be Wrong

- **AWP flexibility**: We assumed the Annual Work Plan is rigid and requires formal modification. In practice, some counties have significant discretionary funds that can be redirected informally. The bureaucratic constraint may be less binding than modelled.
- **KEMSA as sole supplier**: Several counties have begun procuring medical supplies through county-level tenders, bypassing KEMSA. The 6-8 week KEMSA lead time may be avoidable.
- **DHIS2 data quality**: We assumed the data exists but is inconsistent. In some facilities, data is not entered at all — CHWs fill paper registers that are never digitised. The problem may be missing data, not just inconsistent data.
- **TWG functionality**: We assumed TWGs meet regularly and make decisions. In practice, some county TWGs are dormant, meeting only when a partner (NGO) convenes them. CHART may need to revitalise the TWG mechanism, not just plug into it.

### 4. Why Running This For Real Is Still Necessary

This simulation has value: it identified the translation gap, the four-clock problem, the anti-corruption layer requirement, the output-first development strategy, and the feedback flywheel. These are structural insights that desk research alone would not have surfaced as clearly.

But a simulation cannot replace the real workshop because:

- **Power dynamics are invisible in simulation.** Who interrupts whom, who defers to whom, whose sticky notes get placed prominently — these reveal the actual decision-making hierarchy, which may differ from the org chart.
- **Emotional reactions reveal priorities.** When Joseph said "I have to order before I see," we scripted his surprise. In a real workshop, his actual reaction — anger? resignation? excitement? — would tell us how deep the workflow change needs to go.
- **The wall generates emergent insights.** Physical proximity of sticky notes triggers connections that no sequential document can replicate. Someone glances from a KMD sticky to a KEMSA sticky and says "wait — these two events happen in the same week but nobody knows." That spatial cognition is lost in text.
- **Commitment is social, not textual.** When Dr. Amina writes a delivery date on an index card in front of six colleagues, the commitment has social weight. When an AI writes it in a simulation, it has none.

Run this workshop for real. Use this simulation as a preparation guide — a hypothesis about what will happen, to be tested against what actually happens when real people stand at a real wall.

---

## Part F: Mapping Workshop Outputs to CHART Build Plan

The following table maps each workshop discovery to a specific section of the building document and identifies the action required.

| # | Workshop Discovery | Building Doc Section | Action Required |
|---|---|---|---|
| 1 | CHART is a connector, not a data source — translates existing KMD, DHIS2, KEMSA data | Section 1B: Positioning & Value Proposition | **Confirmed.** Sharpen positioning language: CHART connects existing systems, does not replace them. Remove any language implying CHART generates novel data. |
| 2 | KMD forecasts need health-contextualised translation, not raw relay | Section 3: Climate Intelligence Bounded Context | **Refine.** Climate Intelligence BC must output health-relevant variables (e.g., "vector breeding suitability index"), not raw tercile probabilities. Add a translation sub-component. |
| 3 | KEMSA 6-8 week lead time inverts surveillance workflow to anticipatory logistics | Section 3: Adaptation Planning Bounded Context | **Add.** Explicitly model KEMSA procurement timeline as a constraint in the SupplyPrePositioningOrder aggregate. Order trigger = forecast-based, not case-based. |
| 4 | CHW local knowledge (flood routes, facility access) is critical non-digital data | Section 3: Health Data Bounded Context / Data Sources | **Add new data layer.** Create a "Local Knowledge Registry" entity within Health Data BC. Define ingestion workflow for GPS-tagged access disruption records. |
| 5 | DHIS2 indicator UIDs vary across counties; anti-corruption layer is prerequisite | Section 3: Health Data Bounded Context | **Elevate priority.** Move DHIS2 anti-corruption layer from "data quality" subsection to a first-class architectural component. Specify per-county UID mapping tables. |
| 6 | Five counties using CHART enables automated NCCAP national reporting | Section 1C: Stakeholder Analysis / Section 5: Scaling Strategy | **Add.** Include national aggregation as a designed capability from v1, not a future enhancement. Define output schema compatibility with NCCAP monitoring framework. |
| 7 | Only 2 genuinely agentic components (Data Analysis, Synthesis); rest are tools | Section 3: Agent Architecture | **Restructure.** Reduce from 9 agents to 7 components (2 agents + 5 tools). Re-classify HealthRiskAssessment as tool, InterventionMatching as retrieval+filter. Update LangGraph node definitions. |
| 8 | Four misaligned calendars (AWP, KMD, KEMSA, disease) are the core synchronisation challenge | Section 2: System Requirements / Section 3: Orchestration | **Add.** Define dual-mode operation: Early Warning Mode (October-November, rough estimates for AWP drafting) and Tactical Mode (February-March, refined estimates for procurement). Add calendar alignment logic to orchestrator. |
| 9 | TWG review is a legitimacy engine, not optional overhead | Section 4: Human-in-the-Loop Design | **Enforce.** Remove any "bypass TWG" configuration. Design TWG review as mandatory step with structured input (highlighted assumptions, one-click approve/revise). Define SLA for review turnaround. |
| 10 | Feedback loop to KMD is the adoption flywheel | Section 5: Monitoring & Evaluation / Section 3: Architecture | **Add.** Design season-end feedback report as a core output artifact. Include: forecast accuracy, actions taken, health outcomes, estimated impact. Route to KMD and MOH. Build from Phase 1. |
| 11 | Output format (AWP addendum) must be validated before AI pipeline is built | Section 6: Development Roadmap | **Reorder.** Move output format validation to Sprint 1. Build Streamlit mock-up with placeholder data. Validate with Dr. Amina's team before building ingestion or risk assessment. |
| 12 | Action Repository (110+ costed interventions) is a shared kernel across all BCs | Section 3: Data Architecture | **Confirm and detail.** Define Action Repository as a shared kernel with clear ownership (MOH). Specify CRUD permissions: Health Risk Translation reads, Adaptation Planning reads, MOH curates. Version-control intervention costs. |
| 13 | Read models differ sharply by persona (Dr. Amina needs AWP format; Joseph needs supply list; Dr. Wanjiku needs aggregated metrics) | Section 4: User Interface Design | **Add.** Design five distinct read models as specified in Phase 4. Each read model is a projection of the same underlying data, not a separate system. |
| 14 | ERA5 observational overlay is essential for forecast calibration and trust-building | Section 3: Climate Intelligence BC | **Confirmed.** ERA5 climatology tool provides ground truth for bias-correcting KMD forecasts. Retain ERA5 integration as core capability. Add display of forecast vs. ERA5 historical comparison in output. |
| 15 | Dr. Amina's decisive argument: output-first development strategy | Section 6: Development Roadmap / MVP Definition | **Restructure MVP.** MVP = AWP-formatted output (validated format) + DHIS2 anti-corruption layer (clean inputs) + basic health risk assessment. NOT: full agent pipeline with placeholder output. |
| 16 | Peter has never received feedback on forecast utility in 15 years — this is a systemic failure CHART can fix | Section 1A: Problem Statement | **Strengthen.** Add KMD feedback gap to problem statement. Position CHART as closing the loop not just for health planning but for forecast improvement. |
| 17 | Sarah's bridge-flooding-at-Kibaoni example reveals need for sub-county physical access modelling | Section 3: Health Risk Translation BC | **Add.** Include facility accessibility as a risk dimension alongside disease incidence. HealthRiskAssessment tool should accept access disruption data and adjust intervention plans (e.g., pre-position at cut-off facilities). |
| 18 | The unhappy path (TWG rejects plan, KEMSA stockout, forecast busted) must be designed, not patched | Section 3: Error Handling / Section 4: Unhappy Paths | **Add.** Define explicit unhappy-path handlers for: forecast inversion, supply chain failure, DHIS2 data gap, TWG rejection. Each unhappy path triggers a specific recovery workflow, not a generic error message. |
| 19 | Dual confidence modes needed: rough October estimate for AWP drafting vs. refined February estimate for procurement | Section 3: Climate Intelligence BC / Orchestration | **Add.** Climate Intelligence must expose a confidence level on all outputs. Downstream components must propagate uncertainty. AWP draft mode accepts wider confidence intervals; procurement mode requires narrower ones. |
| 20 | CHART must align output schema with IFMIS budget codes used by county treasuries | Section 4: Output Specification | **Add.** Obtain IFMIS code taxonomy from Kilifi County treasury. Map intervention costs to IFMIS programme codes. AWP addendum must use IFMIS-compatible budget line structure or county finance officers will reject it. |

---

## What Changes in the Build Plan

The workshop revealed three things that fundamentally alter the build sequence:

**First, build the container before the contents.** The original plan assumed a bottom-up build: ingest data, compute risk, match interventions, generate output. Dr. Amina's argument inverts this. The AWP-formatted output template must be validated with real county health managers before a single line of agent code is written. A beautiful risk assessment that produces output in the wrong format is useless. A rough risk assessment that produces output in the right format is adoptable.

**Second, the DHIS2 anti-corruption layer is load-bearing infrastructure, not a data quality feature.** Raj's examples — different UIDs across counties, unit mismatches, phantom indicators — mean that CHART cannot trust any DHIS2 data it receives without per-county normalisation. This layer must be built, tested, and validated against real county data before the Health Risk Assessment tool can produce meaningful results. It belongs in Sprint 1, not Sprint 3.

**Third, the feedback loop to KMD is not a monitoring feature — it is the adoption mechanism.** Without it, Peter has no incentive to improve his forecasts, Dr. Amina has no evidence that forecast-based planning works, and Dr. Wanjiku has no impact data for national reporting. The feedback report must be designed from the start as a first-class output artifact, with the same care given to the AWP addendum. It closes the virtuous cycle that makes CHART a learning system rather than a one-shot tool.

The revised build sequence becomes:

1. **Sprint 1 (Weeks 1-4):** Output format validation. Build Streamlit mock-up of AWP addendum using Dr. Amina's real AWP templates. Validate with Kilifi CHMT. Simultaneously, begin DHIS2 indicator mapping with Raj.
2. **Sprint 2 (Weeks 5-8):** DHIS2 anti-corruption layer. Ingest real Kilifi/Mombasa/Kwale data. Normalise indicators. Validate against known case counts.
3. **Sprint 3 (Weeks 9-12):** Climate Intelligence pipeline. Ingest KMD historical outlooks (Peter's CSV). Extract ERA5 climatology. Build Health Risk Assessment tool.
4. **Sprint 4 (Weeks 13-16):** Integration. Connect risk assessment to intervention matching via Action Repository. Generate real AWP addendum from real data. TWG review interface.
5. **Sprint 5 (Weeks 17-20):** Feedback loop. Season-end report generation. KMD forecast verification. National aggregation for Dr. Wanjiku.

This is not the sequence an engineer would choose. It is the sequence that a county health director would use. And she is the user.
