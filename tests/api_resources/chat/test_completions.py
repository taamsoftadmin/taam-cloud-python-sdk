# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taam_cloud import TaamCloud, AsyncTaamCloud

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: TaamCloud) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        )
        assert completion is None

    @parametrize
    def test_method_create_with_all_params(self, client: TaamCloud) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
            max_tokens=0,
            stream=True,
            temperature=0,
        )
        assert completion is None

    @parametrize
    def test_raw_response_create(self, client: TaamCloud) -> None:
        response = client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert completion is None

    @parametrize
    def test_streaming_response_create(self, client: TaamCloud) -> None:
        with client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert completion is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncTaamCloud) -> None:
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        )
        assert completion is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTaamCloud) -> None:
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
            max_tokens=0,
            stream=True,
            temperature=0,
        )
        assert completion is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTaamCloud) -> None:
        response = await async_client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert completion is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTaamCloud) -> None:
        async with async_client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert completion is None

        assert cast(Any, response.is_closed) is True
