# DeltaGuard AI

**Bangladesh Climate Risk Intelligence Platform** — starting with historical flood risk assessment.

> ⚠️ **Disclaimer:** This platform provides historical risk analysis. It is **not** a real-time forecast and **not** an official disaster warning.

## Status

| Phase | Topic | Status |
|---|---|---|
| 0 | Scaffold, architecture, checklist | ✅ Done |
| 1 | Research, datasets, pilot area | ⏳ |
| 2 | Data science (EDA, features, labels) | ⏳ |
| 3 | Machine learning | ⏳ |
| 4 | Geospatial backend (PostGIS) | ⏳ |
| 5 | Frontend dashboard | ⏳ |
| 6 | QA | ⏳ |
| 7 | Deployment | ⏳ |

Details: [`docs/development_checklist.md`](docs/development_checklist.md)

## Principles
- No fabricated data: only real data is used, and no synthetic flood labels.
- No accuracy claims without evaluation.
- Spatial and temporal validation.
- Credentials live only in `.env`.

## Quick start (backend)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r backend/requirements-dev.txt
cp .env.example .env             # Windows: copy .env.example .env
uvicorn backend.app.main:app --reload
# API docs: http://localhost:8000/docs
python -m pytest
```

Docker: `docker compose up --build`

## Docs
- [Architecture](docs/architecture.md)
- [Data sources](docs/data_sources.md)
- [Development checklist](docs/development_checklist.md)
- [Suggested additions](docs/suggested_additions.md)

## License
The source code is released under the [MIT License](LICENSE).
Datasets used by this project have their own licenses; see [`docs/data_sources.md`](docs/data_sources.md).
