from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.routers import v1_router


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    print("Start")
    yield
    print("Shutdown")


app = FastAPI(lifespan=lifespan, description="Project Alpha")

app.include_router(v1_router)
