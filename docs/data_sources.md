# Data Sources Registry

> **নিয়ম:** নিচের তথ্য Phase 0-এর প্রাথমিক নোট। License, resolution ও access status **Phase 1-এ official documentation থেকে যাচাই** করে "Verified" কলাম পূরণ করতে হবে। যাচাইয়ের আগে কোনো তথ্য চূড়ান্ত ধরা যাবে না। কোনো observation বানানো যাবে না।

| # | Dataset | ব্যবহার | Access পথ (সম্ভাব্য) | Resolution (যাচাই করতে হবে) | License/Attribution | Verified |
|---|---|---|---|---|---|---|
| 1 | NASA GPM (IMERG) | Precipitation | GEE / NASA Earthdata | ✔ যাচাই বাকি | ✔ যাচাই বাকি | ☐ |
| 2 | CHIRPS | Historical rainfall | GEE / UCSB CHC | ✔ যাচাই বাকি | ✔ যাচাই বাকি | ☐ |
| 3 | ERA5 / ERA5-Land | Climate reanalysis | Copernicus CDS / GEE | ✔ যাচাই বাকি | ✔ যাচাই বাকি | ☐ |
| 4 | SRTM | Elevation, slope | GEE / USGS | ✔ যাচাই বাকি | ✔ যাচাই বাকি | ☐ |
| 5 | JRC Global Surface Water | Water occurrence, flood history | GEE | ✔ যাচাই বাকি | ✔ যাচাই বাকি | ☐ |
| 6 | Sentinel-1 SAR | Flood extent mapping (label source) | GEE / Copernicus | ✔ যাচাই বাকি | ✔ যাচাই বাকি | ☐ |
| 7 | OpenStreetMap / HydroSHEDS | River network (distance to river) | OSM / HydroSHEDS | ✔ যাচাই বাকি | ✔ যাচাই বাকি | ☐ |
| 8 | Bangladesh admin boundaries | District/Upazila polygons | GADM / HDX / BBS | ✔ যাচাই বাকি | ✔ যাচাই বাকি | ☐ |
| 9 | BWDB water level | River gauge data | **Access অনিশ্চিত** (অনুরোধ লাগতে পারে) | — | — | ☐ |
| 10 | BMD meteorological | Station data | **Access অনিশ্চিত** | — | — | ☐ |

## প্রতিটি dataset-এর metadata ফাইল (`data/raw/<name>.metadata.json`)

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

## ঝুঁকি
- BWDB/BMD data না পেলে প্রকল্প থেমে যাবে না: satellite + reanalysis দিয়েই MVP হবে।
- Flood label-এর মান Sentinel-1/JRC processing-এর উপর নির্ভর করে; এর সীমাবদ্ধতা (cloud, vegetation, urban) docs-এ লিখতে হবে।
