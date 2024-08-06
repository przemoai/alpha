from fastapi import APIRouter

from src.health.router import v1_health

v1_router = APIRouter(prefix="/v1", tags=["v1"])
v1_router.include_router(v1_health)
