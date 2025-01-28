# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taam_cloud import TaamCloud, AsyncTaamCloud
from tests.utils import assert_matches_type
from taam_cloud.types import MapResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMaps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_discover(self, client: TaamCloud) -> None:
        map = client.maps.discover(
            url="url",
        )
        assert_matches_type(MapResponse, map, path=["response"])

    @parametrize
    def test_method_discover_with_all_params(self, client: TaamCloud) -> None:
        map = client.maps.discover(
            url="url",
            ignore_sitemap=True,
            include_subdomains=True,
            limit=5000,
            search="search",
            sitemap_only=True,
        )
        assert_matches_type(MapResponse, map, path=["response"])

    @parametrize
    def test_raw_response_discover(self, client: TaamCloud) -> None:
        response = client.maps.with_raw_response.discover(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        map = response.parse()
        assert_matches_type(MapResponse, map, path=["response"])

    @parametrize
    def test_streaming_response_discover(self, client: TaamCloud) -> None:
        with client.maps.with_streaming_response.discover(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            map = response.parse()
            assert_matches_type(MapResponse, map, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMaps:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_discover(self, async_client: AsyncTaamCloud) -> None:
        map = await async_client.maps.discover(
            url="url",
        )
        assert_matches_type(MapResponse, map, path=["response"])

    @parametrize
    async def test_method_discover_with_all_params(self, async_client: AsyncTaamCloud) -> None:
        map = await async_client.maps.discover(
            url="url",
            ignore_sitemap=True,
            include_subdomains=True,
            limit=5000,
            search="search",
            sitemap_only=True,
        )
        assert_matches_type(MapResponse, map, path=["response"])

    @parametrize
    async def test_raw_response_discover(self, async_client: AsyncTaamCloud) -> None:
        response = await async_client.maps.with_raw_response.discover(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        map = await response.parse()
        assert_matches_type(MapResponse, map, path=["response"])

    @parametrize
    async def test_streaming_response_discover(self, async_client: AsyncTaamCloud) -> None:
        async with async_client.maps.with_streaming_response.discover(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            map = await response.parse()
            assert_matches_type(MapResponse, map, path=["response"])

        assert cast(Any, response.is_closed) is True
