# DeltaGuard AI — System Architecture (Phase 0 draft)

> স্ট্যাটাস: প্রস্তাবিত design। Phase 1-এ pilot geography ঠিক হলে চূড়ান্ত হবে।

## 1. High-level flow

```
 Data Sources (CHIRPS, ERA5, SRTM, JRC, Sentinel-1, ...)
        │  (Google Earth Engine / direct download)
        ▼
 scripts/ + ml/preprocessing   ← ingestion + validation + cleaning
        │
        ▼
 data/raw → data/processed (+ metadata JSON প্রতিটি dataset-এর জন্য)
        │
        ▼
 ml/training → ml/evaluation → models/ (versioned artifacts)
        │
        ▼
 PostgreSQL + PostGIS  (grid cells, features, risk scores, model runs)
        │
        ▼
 FastAPI backend  (GeoJSON, risk, stats, reports APIs)
        │
        ▼
 React + TypeScript + Tailwind + MapLibre/Leaflet + Recharts
```

## 2. Core design decisions

| বিষয় | সিদ্ধান্ত | কারণ |
|---|---|---|
| Spatial unit | Grid cell (যেমন ~1 km) + admin boundary (district/upazila) mapping | Rainfall/elevation raster-based; admin level শুধু summary-র জন্য |
| Pilot area | প্রথমে ১-২ অঞ্চল (Phase 1-এ নির্ধারণ, যেমন Sylhet/Sunamganj haor, বা Brahmaputra-Jamuna floodplain) | সব দেশ একসাথে করলে label ও compute ভারী হবে |
| Label source | Sentinel-1 / JRC / historical flood extent থেকে observed flood mask | Synthetic label নিষিদ্ধ (critical rule) |
| Validation | Spatial block CV + temporal split (পুরনো বছরে train, নতুন বছরে test) | Spatial autocorrelation leakage ঠেকাতে |
| Models | Logistic Regression → Random Forest → XGBoost, আগে baseline | Justified complexity |
| Explainability | Permutation importance + SHAP | Stakeholder trust |
| Product framing | **Historical risk assessment**, real-time forecast নয় | Critical rule #3, #5 |
| API | FastAPI + Pydantic schemas, SQLAlchemy + GeoAlchemy2 | Type-safe, auto docs |

## 3. Database schema (প্রাথমিক)

- `regions` (id, name, level, geom, parent_id)
- `grid_cells` (id, geom, region_id, elevation, slope, dist_to_river)
- `climate_observations` (cell_id, date, rainfall_mm, source_id)
- `flood_events` (id, cell_id, event_date, source_id, extent_flag)
- `datasets` (id, name, license, attribution, resolution, temporal_range, missing_pct, retrieved_at)
- `model_runs` (id, algorithm, params, metrics_json, git_commit, created_at)
- `risk_scores` (cell_id, model_run_id, score, category, uncertainty)

## 4. Security / config

- সব credential `.env`-এ; `.env.example` commit হয়, `.env` না।
- GEE service account ফাইল repo-র বাইরে।
- CORS allow-list, input validation (Pydantic), dependency pinning।

## 5. Deployment (target)

Docker Compose (db + backend + frontend) → GitHub Actions CI (lint, test) → cloud VM/container service (Phase 7)।
