# Development Checklist

At the end of each phase: run the tests → verify the output → move to the next phase. Do not build on top of an unverified phase.

## Phase 0 — Scaffold
- [x] Repo structure
- [x] .gitignore, .env.example, Dockerfile, docker-compose
- [x] Architecture / data sources / checklist docs
- [x] Backend health endpoint + passing tests
- [x] Create the GitHub repo and make the first commit

## Phase 1 — Research & Planning
- [ ] Choose the pilot geography (1–2 regions) and document why
- [ ] Verify license/resolution/access of every dataset (`data_sources.md`)
- [ ] Data dictionary (`docs/data_dictionary.md`)
- [ ] Finalize the flood label strategy (which observations, which years)
- [ ] Enable Google Earth Engine access

## Phase 2 — Data Science
- [ ] Ingestion scripts (`scripts/`, `ml/preprocessing/`)
- [ ] Data validation (schema, range, missing values)
- [ ] Notebook 01: data collection
- [ ] Notebook 02: EDA
- [ ] Notebook 03: feature engineering
- [ ] Build the flood label dataset and write label-quality notes

## Phase 3 — Machine Learning
- [ ] Baseline (Logistic Regression)
- [ ] Compare Random Forest and XGBoost
- [ ] Spatial block CV + temporal split
- [ ] Precision/Recall/F1/ROC-AUC (+ PR-AUC, class imbalance)
- [ ] Feature importance + SHAP
- [ ] Calibration and uncertainty
- [ ] Save model artifact + metrics JSON
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
- [ ] Accessible color scale, responsive layout

## Phase 6 — QA
- [ ] Unit + integration tests
- [ ] Data/model validation tests
- [ ] Security review (secrets, CORS, dependencies)

## Phase 7 — Deployment
- [ ] Dockerize all services
- [ ] GitHub Actions CI/CD
- [ ] Deployment guide, API docs
- [ ] Publish MVP + final README
