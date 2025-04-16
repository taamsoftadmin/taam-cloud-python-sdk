# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taam_cloud import TaamCloud, AsyncTaamCloud
from tests.utils import assert_matches_type
from taam_cloud.types import QueryCheckVideoGenerationStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_check_video_generation_status(self, client: TaamCloud) -> None:
        query = client.query.check_video_generation_status(
            task_id="task_id",
        )
        assert_matches_type(QueryCheckVideoGenerationStatusResponse, query, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_check_video_generation_status(self, client: TaamCloud) -> None:
        response = client.query.with_raw_response.check_video_generation_status(
            task_id="task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryCheckVideoGenerationStatusResponse, query, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_check_video_generation_status(self, client: TaamCloud) -> None:
        with client.query.with_streaming_response.check_video_generation_status(
            task_id="task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryCheckVideoGenerationStatusResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQuery:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_check_video_generation_status(self, async_client: AsyncTaamCloud) -> None:
        query = await async_client.query.check_video_generation_status(
            task_id="task_id",
        )
        assert_matches_type(QueryCheckVideoGenerationStatusResponse, query, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_check_video_generation_status(self, async_client: AsyncTaamCloud) -> None:
        response = await async_client.query.with_raw_response.check_video_generation_status(
            task_id="task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryCheckVideoGenerationStatusResponse, query, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_check_video_generation_status(self, async_client: AsyncTaamCloud) -> None:
        async with async_client.query.with_streaming_response.check_video_generation_status(
            task_id="task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryCheckVideoGenerationStatusResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True
