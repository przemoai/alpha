import http

import pytest
from httpx import AsyncClient

from src.common.response import DefaultResponse


class TestHealth:
    @pytest.mark.anyio
    async def test_health(self, client: AsyncClient):
        response = await client.get("/v1/health")

        response_json = response.json()
        response_json = DefaultResponse(**response_json)

        assert response.status_code == http.HTTPStatus.OK
        assert response_json.status == http.HTTPStatus.OK
        assert response_json.message == "OK"
