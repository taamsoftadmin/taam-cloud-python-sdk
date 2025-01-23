# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taam_cloud import TaamCloud, AsyncTaamCloud
from tests.utils import assert_matches_type
from taam_cloud.types import ScrapeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScrape:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: TaamCloud) -> None:
        scrape = client.scrape.create(
            url="url",
        )
        assert_matches_type(ScrapeResponse, scrape, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: TaamCloud) -> None:
        scrape = client.scrape.create(
            url="url",
            formats=["markdown"],
            only_main_content=True,
        )
        assert_matches_type(ScrapeResponse, scrape, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: TaamCloud) -> None:
        response = client.scrape.with_raw_response.create(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scrape = response.parse()
        assert_matches_type(ScrapeResponse, scrape, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: TaamCloud) -> None:
        with client.scrape.with_streaming_response.create(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scrape = response.parse()
            assert_matches_type(ScrapeResponse, scrape, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScrape:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncTaamCloud) -> None:
        scrape = await async_client.scrape.create(
            url="url",
        )
        assert_matches_type(ScrapeResponse, scrape, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTaamCloud) -> None:
        scrape = await async_client.scrape.create(
            url="url",
            formats=["markdown"],
            only_main_content=True,
        )
        assert_matches_type(ScrapeResponse, scrape, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTaamCloud) -> None:
        response = await async_client.scrape.with_raw_response.create(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scrape = await response.parse()
        assert_matches_type(ScrapeResponse, scrape, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTaamCloud) -> None:
        async with async_client.scrape.with_streaming_response.create(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scrape = await response.parse()
            assert_matches_type(ScrapeResponse, scrape, path=["response"])

        assert cast(Any, response.is_closed) is True
