# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taam_cloud import TaamCloud, AsyncTaamCloud

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRerank:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: TaamCloud) -> None:
        rerank = client.rerank.create(
            documents=["string"],
            model="model",
            query="query",
        )
        assert rerank is None

    @parametrize
    def test_method_create_with_all_params(self, client: TaamCloud) -> None:
        rerank = client.rerank.create(
            documents=["string"],
            model="model",
            query="query",
            top_n=0,
        )
        assert rerank is None

    @parametrize
    def test_raw_response_create(self, client: TaamCloud) -> None:
        response = client.rerank.with_raw_response.create(
            documents=["string"],
            model="model",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rerank = response.parse()
        assert rerank is None

    @parametrize
    def test_streaming_response_create(self, client: TaamCloud) -> None:
        with client.rerank.with_streaming_response.create(
            documents=["string"],
            model="model",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rerank = response.parse()
            assert rerank is None

        assert cast(Any, response.is_closed) is True


class TestAsyncRerank:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncTaamCloud) -> None:
        rerank = await async_client.rerank.create(
            documents=["string"],
            model="model",
            query="query",
        )
        assert rerank is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTaamCloud) -> None:
        rerank = await async_client.rerank.create(
            documents=["string"],
            model="model",
            query="query",
            top_n=0,
        )
        assert rerank is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTaamCloud) -> None:
        response = await async_client.rerank.with_raw_response.create(
            documents=["string"],
            model="model",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rerank = await response.parse()
        assert rerank is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTaamCloud) -> None:
        async with async_client.rerank.with_streaming_response.create(
            documents=["string"],
            model="model",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rerank = await response.parse()
            assert rerank is None

        assert cast(Any, response.is_closed) is True
