# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taam_cloud import TaamCloud, AsyncTaamCloud
from tests.utils import assert_matches_type
from taam_cloud.types import SearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_perform(self, client: TaamCloud) -> None:
        search = client.searches.perform(
            chat_model={
                "model": "gpt-3.5-turbo",
                "provider": "custom_openai",
            },
            embedding_model={
                "model": "text-embedding-3-large",
                "provider": "custom_openai",
            },
            focus_mode="webSearch",
        )
        assert_matches_type(SearchResponse, search, path=["response"])

    @parametrize
    def test_method_perform_with_all_params(self, client: TaamCloud) -> None:
        search = client.searches.perform(
            chat_model={
                "model": "gpt-3.5-turbo",
                "provider": "custom_openai",
                "custom_openai_base_url": "customOpenAIBaseURL",
                "custom_openai_key": "customOpenAIKey",
            },
            embedding_model={
                "model": "text-embedding-3-large",
                "provider": "custom_openai",
            },
            focus_mode="webSearch",
        )
        assert_matches_type(SearchResponse, search, path=["response"])

    @parametrize
    def test_raw_response_perform(self, client: TaamCloud) -> None:
        response = client.searches.with_raw_response.perform(
            chat_model={
                "model": "gpt-3.5-turbo",
                "provider": "custom_openai",
            },
            embedding_model={
                "model": "text-embedding-3-large",
                "provider": "custom_openai",
            },
            focus_mode="webSearch",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchResponse, search, path=["response"])

    @parametrize
    def test_streaming_response_perform(self, client: TaamCloud) -> None:
        with client.searches.with_streaming_response.perform(
            chat_model={
                "model": "gpt-3.5-turbo",
                "provider": "custom_openai",
            },
            embedding_model={
                "model": "text-embedding-3-large",
                "provider": "custom_openai",
            },
            focus_mode="webSearch",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearches:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_perform(self, async_client: AsyncTaamCloud) -> None:
        search = await async_client.searches.perform(
            chat_model={
                "model": "gpt-3.5-turbo",
                "provider": "custom_openai",
            },
            embedding_model={
                "model": "text-embedding-3-large",
                "provider": "custom_openai",
            },
            focus_mode="webSearch",
        )
        assert_matches_type(SearchResponse, search, path=["response"])

    @parametrize
    async def test_method_perform_with_all_params(self, async_client: AsyncTaamCloud) -> None:
        search = await async_client.searches.perform(
            chat_model={
                "model": "gpt-3.5-turbo",
                "provider": "custom_openai",
                "custom_openai_base_url": "customOpenAIBaseURL",
                "custom_openai_key": "customOpenAIKey",
            },
            embedding_model={
                "model": "text-embedding-3-large",
                "provider": "custom_openai",
            },
            focus_mode="webSearch",
        )
        assert_matches_type(SearchResponse, search, path=["response"])

    @parametrize
    async def test_raw_response_perform(self, async_client: AsyncTaamCloud) -> None:
        response = await async_client.searches.with_raw_response.perform(
            chat_model={
                "model": "gpt-3.5-turbo",
                "provider": "custom_openai",
            },
            embedding_model={
                "model": "text-embedding-3-large",
                "provider": "custom_openai",
            },
            focus_mode="webSearch",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchResponse, search, path=["response"])

    @parametrize
    async def test_streaming_response_perform(self, async_client: AsyncTaamCloud) -> None:
        async with async_client.searches.with_streaming_response.perform(
            chat_model={
                "model": "gpt-3.5-turbo",
                "provider": "custom_openai",
            },
            embedding_model={
                "model": "text-embedding-3-large",
                "provider": "custom_openai",
            },
            focus_mode="webSearch",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True
