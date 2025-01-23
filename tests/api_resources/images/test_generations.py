# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taam_cloud import TaamCloud, AsyncTaamCloud
from tests.utils import assert_matches_type
from taam_cloud.types.images import ImageGenerationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: TaamCloud) -> None:
        generation = client.images.generations.create(
            prompt="prompt",
        )
        assert_matches_type(ImageGenerationResponse, generation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: TaamCloud) -> None:
        generation = client.images.generations.create(
            prompt="prompt",
            model="dall-e-3",
            n=0,
            quality="standard",
            size="1024x1024",
            style="natural",
        )
        assert_matches_type(ImageGenerationResponse, generation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: TaamCloud) -> None:
        response = client.images.generations.with_raw_response.create(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(ImageGenerationResponse, generation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: TaamCloud) -> None:
        with client.images.generations.with_streaming_response.create(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(ImageGenerationResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGenerations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncTaamCloud) -> None:
        generation = await async_client.images.generations.create(
            prompt="prompt",
        )
        assert_matches_type(ImageGenerationResponse, generation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTaamCloud) -> None:
        generation = await async_client.images.generations.create(
            prompt="prompt",
            model="dall-e-3",
            n=0,
            quality="standard",
            size="1024x1024",
            style="natural",
        )
        assert_matches_type(ImageGenerationResponse, generation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTaamCloud) -> None:
        response = await async_client.images.generations.with_raw_response.create(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(ImageGenerationResponse, generation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTaamCloud) -> None:
        async with async_client.images.generations.with_streaming_response.create(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(ImageGenerationResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True
