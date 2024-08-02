from fastapi import APIRouter
from fastapi_utils.cbv import cbv
from starlette import status

from src.common.response import DefaultResponse

v1_health = APIRouter(tags=["health"])


@cbv(v1_health)
class HealthRouter:
    @v1_health.get(
        "/health", status_code=status.HTTP_200_OK, response_model=DefaultResponse, response_model_exclude_none=True
    )
    async def health_check(self) -> DefaultResponse:
        """Health Check Endpoint.

        This endpoint returns the health status of the application.
        """
        return DefaultResponse(status=status.HTTP_200_OK, message="OK")
