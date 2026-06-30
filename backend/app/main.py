from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
# from api.router import api_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# CORS – React frontend będzie korzystał z API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # możesz później ograniczyć do domeny frontendu
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rejestracja routerów
# app.include_router(api_router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    return {"status": "ok", "version": settings.APP_VERSION}
