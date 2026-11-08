# Data Sources Registry

> **Rule:** The information below is preliminary Phase 0 notes. License, resolution and access status **must be verified against the official documentation in Phase 1**, and the "Verified" column filled in. Nothing is final until verified. No observations may be fabricated.

| # | Dataset | Use | Access route (likely) | Resolution (to verify) | License/Attribution | Verified |
|---|---|---|---|---|---|---|
| 1 | NASA GPM (IMERG) | Precipitation | GEE / NASA Earthdata | ✔ to verify | ✔ to verify | ☐ |
| 2 | CHIRPS | Historical rainfall | GEE / UCSB CHC | ✔ to verify | ✔ to verify | ☐ |
| 3 | ERA5 / ERA5-Land | Climate reanalysis | Copernicus CDS / GEE | ✔ to verify | ✔ to verify | ☐ |
| 4 | SRTM | Elevation, slope | GEE / USGS | ✔ to verify | ✔ to verify | ☐ |
| 5 | JRC Global Surface Water | Water occurrence, flood history | GEE | ✔ to verify | ✔ to verify | ☐ |
| 6 | Sentinel-1 SAR | Flood extent mapping (label source) | GEE / Copernicus | ✔ to verify | ✔ to verify | ☐ |
| 7 | OpenStreetMap / HydroSHEDS | River network (distance to river) | OSM / HydroSHEDS | ✔ to verify | ✔ to verify | ☐ |
| 8 | Bangladesh admin boundaries | District/Upazila polygons | GADM / HDX / BBS | ✔ to verify | ✔ to verify | ☐ |
| 9 | BWDB water level | River gauge data | **Access uncertain** (a formal request may be needed) | — | — | ☐ |
| 10 | BMD meteorological | Station data | **Access uncertain** | — | — | ☐ |

## Per-dataset metadata file (`data/raw/<name>.metadata.json`)

```json
{
  "name": "",
  "source_url": "",
  "license": "",
  "attribution": "",
  "spatial_resolution": "",
  "temporal_resolution": "",
  "temporal_range": "",
  "retrieved_at": "",
  "missing_value_notes": "",
  "processing_notes": ""
}
```

## Risks
- If BWDB/BMD data cannot be obtained, the project does not stop: the MVP will be built from satellite and reanalysis data alone.
- The quality of flood labels depends on Sentinel-1/JRC processing; its limitations (clouds, vegetation, urban areas) must be documented.
