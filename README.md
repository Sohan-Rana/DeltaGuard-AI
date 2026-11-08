# DeltaGuard AI

**Bangladesh Climate Risk Intelligence Platform** — প্রথম ধাপে flood risk assessment।

> ⚠️ **Disclaimer:** এই প্ল্যাটফর্ম ঐতিহাসিক ঝুঁকি বিশ্লেষণ করে। এটি real-time forecast বা official disaster warning নয়।

## Status

| Phase | বিষয় | অবস্থা |
|---|---|---|
| 0 | Scaffold, architecture, checklist | ✅ চলমান/সম্পন্ন |
| 1 | Research, datasets, pilot area | ⏳ |
| 2 | Data Science (EDA, features, labels) | ⏳ |
| 3 | Machine Learning | ⏳ |
| 4 | Geospatial backend (PostGIS) | ⏳ |
| 5 | Frontend dashboard | ⏳ |
| 6 | QA | ⏳ |
| 7 | Deployment | ⏳ |

বিস্তারিত: [`docs/development_checklist.md`](docs/development_checklist.md)

## মূল নীতি
- বাস্তব ডেটা ছাড়া কিছু বানানো হয় না; synthetic flood label নয়।
- Evaluation ছাড়া accuracy claim নয়।
- Spatial + temporal validation।
- Credential শুধু `.env`-এ।

## Quick start (backend)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r backend/requirements.txt
cp .env.example .env
uvicorn backend.app.main:app --reload
# http://localhost:8000/docs
pytest backend/tests
```

Docker: `docker compose up --build`

## Docs
- [Architecture](docs/architecture.md)
- [Data sources](docs/data_sources.md)
- [Development checklist](docs/development_checklist.md)
- [Suggested additions](docs/suggested_additions.md)

## License
TBD (Phase 7-এ ঠিক হবে; dataset license আলাদা, `docs/data_sources.md` দেখুন)।
