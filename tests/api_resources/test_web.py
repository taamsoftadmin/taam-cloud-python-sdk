# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taam_cloud import TaamCloud, AsyncTaamCloud
from tests.utils import assert_matches_type
from taam_cloud.types import WebCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWeb:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: TaamCloud) -> None:
        web = client.web.create(
            model="scrape",
        )
        assert_matches_type(WebCreateResponse, web, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: TaamCloud) -> None:
        web = client.web.create(
            model="scrape",
            params={},
        )
        assert_matches_type(WebCreateResponse, web, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: TaamCloud) -> None:
        response = client.web.with_raw_response.create(
            model="scrape",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebCreateResponse, web, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: TaamCloud) -> None:
        with client.web.with_streaming_response.create(
            model="scrape",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebCreateResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWeb:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTaamCloud) -> None:
        web = await async_client.web.create(
            model="scrape",
        )
        assert_matches_type(WebCreateResponse, web, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTaamCloud) -> None:
        web = await async_client.web.create(
            model="scrape",
            params={},
        )
        assert_matches_type(WebCreateResponse, web, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTaamCloud) -> None:
        response = await async_client.web.with_raw_response.create(
            model="scrape",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebCreateResponse, web, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTaamCloud) -> None:
        async with async_client.web.with_streaming_response.create(
            model="scrape",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebCreateResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True
