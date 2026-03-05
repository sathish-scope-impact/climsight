# Climate Data Sources for CHART

## Research Summary

Last updated: 2026-03-05

This document evaluates available climate data APIs and datasets for use in CHART, covering seasonal forecasts, historical climatology, and real-time weather data relevant to India and Kenya.

---

## 1. Source Comparison

| Source | Resolution | Coverage | Cost | Seasonal Forecast | Historical Data | API Available |
|---|---|---|---|---|---|---|
| Open-Meteo Climate API | 10 km | Global, 1950-2050 | Free (non-commercial) | No (projections only) | Yes | Yes (REST) |
| Open-Meteo Seasonal Forecast API | 36 km | Global | Free | Yes (ECMWF SEAS5, 7 months) | No | Yes (REST) |
| Open-Meteo Historical Weather API | 1-11 km | Global | Free | No | Yes (1940-present) | Yes (REST) |
| DHIS2 Climate App (ERA5-Land) | ~9 km | Global | Free | No | Yes | Via DHIS2 |
| ERA5 Reanalysis (CDS) | ~31 km | Global, 1940-present | Free | No | Yes | Yes (CDS API) |
| ERA5-Land | ~9 km | Global, 1950-present | Free | No | Yes | Yes (CDS API) |
| ECMWF SEAS5 (direct) | ~36 km | Global | Institutional | Yes (7 months) | No | Yes (MARS/CDS) |
| IMD (India) | District-level | India | Government | Yes (seasonal outlook) | Yes | Limited |
| KMD (Kenya) | County-level | Kenya | Government | Yes (MAM/OND) | Limited | Limited |
| IRI Data Library | Variable | Global (tropics focus) | Free | Yes (multi-model) | Yes | Yes |
| CHIRPS (precipitation) | ~5 km | 50S-50N | Free | No | Yes (1981-present) | Yes |

---

## 2. Detailed Source Profiles

### Open-Meteo (Recommended for MVP)

**URL:** https://open-meteo.com/

**Climate API** ([open-meteo.com/en/docs/climate-api](https://open-meteo.com/en/docs/climate-api))
- Regional downscaled climate models from CMIP6 HighResMip
- 10 km resolution, 1950-2050
- Daily resolution with standard variables: temperature (min/max/mean), precipitation, wind speed, relative humidity
- Multiple models available for ensemble/uncertainty analysis
- Can compute derived indicators: days >30C, drought duration, growing degree days

**Seasonal Forecast API** ([open-meteo.com/en/docs/seasonal-forecast-api](https://open-meteo.com/en/docs/seasonal-forecast-api))
- ECMWF SEAS5 and EC46 models
- 36 km resolution, 51 ensemble members
- Up to 7 months ahead (SEAS5) or 46 days (EC46)
- **Not bias-corrected** -- must be interpreted as area forecasts
- Variables: temperature, precipitation, wind, pressure, cloud cover

**Historical Weather API**
- ERA5 and ERA5-Land reanalysis data via simple REST API
- 1-11 km resolution depending on region
- Global coverage from 1940 to present
- Hourly and daily aggregation available

**Pricing:** Free for non-commercial use (<10,000 requests/day). No API key required. Commercial plans available.

**Limitations for India/Kenya:**
- Seasonal forecast at 36 km is too coarse for fine district-level use in many cases
- India and Kenya may rely on coarser global models (11 km+) rather than 1-2 km high-res models available in Europe/US
- No bias correction against local observations

---

### ERA5 / ERA5-Land (via Copernicus CDS)

**URL:** https://cds.climate.copernicus.eu/

- ERA5: 31 km resolution, hourly, 1940-present
- ERA5-Land: 9 km resolution, hourly, 1950-present (land only)
- Gold standard for historical climatology
- Used by DHIS2 Climate App as primary data source
- ClimSight already integrates ERA5 via Arraylake (requires API key)

**Variables relevant to CHART:**
- 2m temperature (for heat stress)
- Total precipitation (for flood/drought)
- 10m wind (for storm events)
- Soil moisture (for drought/agriculture)
- Relative humidity (for heat index/wet-bulb temperature)

**Limitations:**
- Historical only -- no forecasts
- Large data volumes for time series extraction
- CDS API can be slow during peak usage

---

### ECMWF SEAS5 (Seasonal Forecast)

**URL:** https://www.ecmwf.int/en/forecasts/datasets/set-v

- The source data behind Open-Meteo's seasonal forecast API
- 36 km resolution, 51 ensemble members, 7 months ahead
- Updated monthly (around 13th of each month)
- Provides probabilistic forecasts (tercile categories: below/near/above normal)

**Access:**
- Free via CDS API for research
- Open-Meteo provides a simpler REST wrapper
- Can also access via DHIS2 Climate App (limited)

---

### India Meteorological Department (IMD)

**URL:** https://mausam.imd.gov.in/

- Official seasonal outlooks for India (Southwest Monsoon, Northeast Monsoon)
- District-level climate normals and historical data
- Extended range forecasts (2-4 weeks)
- Heat wave warnings and alerts

**Access:** Government portal, some data freely available, detailed data requires institutional access.

**Relevance:** IMD seasonal outlooks are the reference standard for Indian district officers. CHART should ingest and interpret IMD forecasts rather than substitute with Open-Meteo.

---

### Kenya Meteorological Department (KMD)

**URL:** https://meteo.go.ke/

- Seasonal outlooks for March-April-May (MAM) and October-November-December (OND) rainy seasons
- County-level climate summaries
- Drought and flood early warnings via Kenya FEWS NET

**Access:** Seasonal outlooks published as PDFs; limited programmatic access.

**Relevance:** KMD seasonal outlooks drive agricultural and health planning in Kenya. County health officers reference MAM/OND forecasts. CHART should align with these established seasonal calendars.

---

### IRI Data Library (Columbia University)

**URL:** https://iridl.ldeo.columbia.edu/

- Multi-model seasonal forecast products
- Climate Predictability Tool (CPT) for downscaling
- Focus on tropical regions (strong coverage of India and East Africa)
- Used by many national meteorological services in developing countries

**Relevance:** Provides calibrated seasonal forecasts for the tropics. Better suited for Kenya/India than raw ECMWF output. Could be used for forecast verification.

---

### CHIRPS (Climate Hazards Group InfraRed Precipitation with Station)

**URL:** https://www.chc.ucsb.edu/data/chirps

- ~5 km resolution precipitation dataset
- 50S-50N coverage, 1981-present
- Blends satellite imagery with station data
- Widely used for drought monitoring in East Africa

**Relevance:** High-resolution precipitation data for drought/flood risk assessment. Better resolution than ERA5 for precipitation in Kenya.

---

## 3. Recommended Data Strategy

### MVP (Phase 1)

| Need | Source | Rationale |
|---|---|---|
| Seasonal forecast | Open-Meteo Seasonal Forecast API | Free, simple REST API, 7 months ahead |
| Historical baseline | Open-Meteo Historical Weather API | Free, easy to compute climatological normals |
| Climate projections | Open-Meteo Climate API | CMIP6 models at 10 km |

**Why Open-Meteo for MVP:** Zero-cost, no API key needed, simple REST interface, global coverage. Allows rapid prototyping without institutional data agreements.

### Production (Phase 2)

| Need | Source | Rationale |
|---|---|---|
| Seasonal forecast (India) | IMD seasonal outlook + IRI | District officers already use IMD; adds credibility |
| Seasonal forecast (Kenya) | KMD MAM/OND outlook + IRI | County officers reference KMD; seasonal calendar alignment |
| Historical baseline | ERA5-Land via CDS or DHIS2 | Higher resolution (9 km); DHIS2 already imports this |
| Precipitation (Kenya) | CHIRPS | 5 km resolution; standard for East Africa drought monitoring |
| Heat stress indicators | ERA5 + derived metrics | Wet-bulb temperature, heat index, consecutive hot days |

### Derived Indicators for MNCH

Beyond raw climate variables, CHART needs derived indicators:

| Indicator | Derivation | Health Relevance |
|---|---|---|
| Consecutive days >35C | ERA5/Open-Meteo 2m temp | Preterm birth risk threshold |
| Wet-bulb globe temperature (WBGT) | Temperature + humidity + radiation | Heat stress for outdoor work (pregnant women) |
| Standardized Precipitation Index (SPI) | Precipitation anomaly | Drought severity for food security |
| Flood risk index | Precipitation intensity + soil moisture | Waterborne disease, facility access |
| Malaria transmission suitability | Temperature + precipitation + humidity | Seasonal malaria prediction |
| Growing season anomaly | Precipitation + temperature | Crop yield / nutrition security |

---

## 4. Data Integration with ClimSight

ClimSight already supports:
- ERA5 reanalysis via Arraylake (`tools/era5_retrieval_tool.py`)
- ERA5 climatology extraction (`tools/era5_climatology_tool.py`)
- Climate model projections via provider pattern (`climate_data_providers.py`)
- DestinE Climate DT retrieval (`tools/destine_retrieval_tool.py`)

**New integrations needed for CHART:**
1. Open-Meteo Seasonal Forecast API client (new provider)
2. Open-Meteo Historical Weather API client (new provider)
3. Derived indicator computation (heat stress, drought, flood risk)
4. IMD/KMD forecast ingestion (PDF parsing or manual entry for MVP)

---

## 5. References

- Open-Meteo: https://open-meteo.com/
- Open-Meteo Climate API: https://open-meteo.com/en/docs/climate-api
- Open-Meteo Seasonal Forecast API: https://open-meteo.com/en/docs/seasonal-forecast-api
- Copernicus Climate Data Store: https://cds.climate.copernicus.eu/
- ERA5-Land: https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land
- IMD: https://mausam.imd.gov.in/
- KMD: https://meteo.go.ke/
- IRI Data Library: https://iridl.ldeo.columbia.edu/
- CHIRPS: https://www.chc.ucsb.edu/data/chirps
- DHIS2 Climate Data: https://dhis2.org/climate/climate-data/
