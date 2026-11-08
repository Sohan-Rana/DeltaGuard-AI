from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings

DISCLAIMER = (
    "DeltaGuard AI historical risk assessment প্রদান করে। এটি real-time forecast "
    "বা official disaster warning নয়।"
)

app = FastAPI(
    title="DeltaGuard AI API",
    version="0.1.0",
    description=DISCLAIMER,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in settings.cors_origins.split(",") if o.strip()],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "version": app.version}


@app.get("/api/v1/disclaimer")
def disclaimer() -> dict:
    return {"disclaimer": DISCLAIMER}
