# DeltaGuard AI — System Architecture (Phase 0 draft)

> Status: proposed design. To be finalized once the pilot geography is chosen in Phase 1.

## 1. High-level flow

```
 Data Sources (CHIRPS, ERA5, SRTM, JRC, Sentinel-1, ...)
        │  (Google Earth Engine / direct download)
        ▼
 scripts/ + ml/preprocessing   ← ingestion + validation + cleaning
        │
        ▼
 data/raw → data/processed (+ a metadata JSON for every dataset)
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

| Topic | Decision | Reason |
|---|---|---|
| Spatial unit | Grid cell (e.g. ~1 km) + admin boundary (district/upazila) mapping | Rainfall/elevation data are raster-based; admin level is used for summaries only |
| Pilot area | Start with 1–2 regions (decided in Phase 1, e.g. the Sylhet/Sunamganj haor, or the Brahmaputra-Jamuna floodplain) | Covering the whole country at once makes labeling and compute too heavy |
| Label source | Observed flood mask from Sentinel-1 / JRC / historical flood extent | Synthetic labels are forbidden (critical rule) |
| Validation | Spatial block CV + temporal split (train on older years, test on newer years) | Prevents spatial-autocorrelation leakage |
| Models | Logistic Regression → Random Forest → XGBoost, baseline first | Justified complexity |
| Explainability | Permutation importance + SHAP | Stakeholder trust |
| Product framing | **Historical risk assessment**, not a real-time forecast | Critical rules #3 and #5 |
| API | FastAPI + Pydantic schemas, SQLAlchemy + GeoAlchemy2 | Type-safe, auto-generated docs |

## 3. Database schema (initial)

- `regions` (id, name, level, geom, parent_id)
- `grid_cells` (id, geom, region_id, elevation, slope, dist_to_river)
- `climate_observations` (cell_id, date, rainfall_mm, source_id)
- `flood_events` (id, cell_id, event_date, source_id, extent_flag)
- `datasets` (id, name, license, attribution, resolution, temporal_range, missing_pct, retrieved_at)
- `model_runs` (id, algorithm, params, metrics_json, git_commit, created_at)
- `risk_scores` (cell_id, model_run_id, score, category, uncertainty)

## 4. Security / config

- All credentials live in `.env`; `.env.example` is committed, `.env` is not.
- The GEE service account file is kept outside the repo.
- CORS allow-list, input validation (Pydantic), dependency pinning.

## 5. Deployment (target)

Docker Compose (db + backend + frontend) → GitHub Actions CI (lint, test) → cloud VM/container service (Phase 7).
