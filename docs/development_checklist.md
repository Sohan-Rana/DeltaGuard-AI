# Development Checklist

প্রতিটি phase শেষে: test চালান → output verify করুন → পরের phase-এ যান। অযাচাইকৃত phase-এর উপর build করবেন না।

## Phase 0 — Scaffold (এখন)
- [x] Repo structure
- [x] .gitignore, .env.example, Dockerfile, docker-compose
- [x] Architecture / data sources / checklist docs
- [ ] Backend health endpoint + test পাস
- [ ] GitHub repo বানিয়ে প্রথম commit

## Phase 1 — Research & Planning
- [ ] Pilot geography নির্ধারণ (১-২ অঞ্চল) ও কারণ লেখা
- [ ] প্রতিটি dataset-এর license/resolution/access যাচাই (`data_sources.md`)
- [ ] Data dictionary (`docs/data_dictionary.md`)
- [ ] Flood label কৌশল চূড়ান্ত (কোন observation, কোন বছর)
- [ ] Google Earth Engine access চালু

## Phase 2 — Data Science
- [ ] Ingestion scripts (`scripts/`, `ml/preprocessing/`)
- [ ] Data validation (schema, range, missing)
- [ ] Notebook 01 data collection
- [ ] Notebook 02 EDA
- [ ] Notebook 03 feature engineering
- [ ] Flood label dataset তৈরি ও label-quality নোট

## Phase 3 — Machine Learning
- [ ] Baseline (Logistic Regression)
- [ ] Random Forest, XGBoost তুলনা
- [ ] Spatial block CV + temporal split
- [ ] Precision/Recall/F1/ROC-AUC (+ PR-AUC, class imbalance)
- [ ] Feature importance + SHAP
- [ ] Calibration ও uncertainty
- [ ] Model artifact + metrics JSON সংরক্ষণ
- [ ] Model evaluation report

## Phase 4 — Geospatial Platform
- [ ] PostGIS schema + migrations (Alembic)
- [ ] Load pipeline (grid, features, scores)
- [ ] APIs: /regions, /risk, /stats, /reports
- [ ] GeoJSON/vector tile output

## Phase 5 — Frontend
- [ ] Landing, map, risk overview, search
- [ ] Flood risk analysis page
- [ ] Historical charts, model performance page
- [ ] Data sources + methodology pages
- [ ] Accessible color scale, responsive

## Phase 6 — QA
- [ ] Unit + integration tests
- [ ] Data/model validation tests
- [ ] Security review (secrets, CORS, deps)

## Phase 7 — Deployment
- [ ] Dockerize সব service
- [ ] GitHub Actions CI/CD
- [ ] Deployment guide, API docs
- [ ] MVP publish + final README
