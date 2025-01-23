# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taam_cloud import TaamCloud, AsyncTaamCloud
from tests.utils import assert_matches_type
from taam_cloud.types import CrawlResponse, CrawlStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCrawl:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: TaamCloud) -> None:
        crawl = client.crawl.create(
            url="url",
        )
        assert_matches_type(CrawlResponse, crawl, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: TaamCloud) -> None:
        crawl = client.crawl.create(
            url="url",
            allow_backward_links=True,
            allow_external_links=True,
            exclude_paths=["string"],
            ignore_sitemap=True,
            include_paths=["string"],
            limit=0,
            max_depth=0,
            scrape_options={
                "actions": [
                    {
                        "milliseconds": 0,
                        "type": "wait",
                        "selector": "selector",
                    }
                ],
                "exclude_tags": ["string"],
                "formats": ["markdown"],
                "headers": {"foo": "bar"},
                "include_tags": ["string"],
                "json_options": {
                    "prompt": "prompt",
                    "schema": {},
                    "system_prompt": "systemPrompt",
                },
                "location": {
                    "country": "country",
                    "languages": ["string"],
                },
                "mobile": True,
                "only_main_content": True,
                "remove_base64_images": True,
                "skip_tls_verification": True,
                "timeout": 0,
                "wait_for": 0,
            },
            webhook="webhook",
        )
        assert_matches_type(CrawlResponse, crawl, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: TaamCloud) -> None:
        response = client.crawl.with_raw_response.create(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(CrawlResponse, crawl, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: TaamCloud) -> None:
        with client.crawl.with_streaming_response.create(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(CrawlResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: TaamCloud) -> None:
        crawl = client.crawl.retrieve(
            "id",
        )
        assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TaamCloud) -> None:
        response = client.crawl.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TaamCloud) -> None:
        with client.crawl.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: TaamCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.crawl.with_raw_response.retrieve(
                "",
            )


class TestAsyncCrawl:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncTaamCloud) -> None:
        crawl = await async_client.crawl.create(
            url="url",
        )
        assert_matches_type(CrawlResponse, crawl, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTaamCloud) -> None:
        crawl = await async_client.crawl.create(
            url="url",
            allow_backward_links=True,
            allow_external_links=True,
            exclude_paths=["string"],
            ignore_sitemap=True,
            include_paths=["string"],
            limit=0,
            max_depth=0,
            scrape_options={
                "actions": [
                    {
                        "milliseconds": 0,
                        "type": "wait",
                        "selector": "selector",
                    }
                ],
                "exclude_tags": ["string"],
                "formats": ["markdown"],
                "headers": {"foo": "bar"},
                "include_tags": ["string"],
                "json_options": {
                    "prompt": "prompt",
                    "schema": {},
                    "system_prompt": "systemPrompt",
                },
                "location": {
                    "country": "country",
                    "languages": ["string"],
                },
                "mobile": True,
                "only_main_content": True,
                "remove_base64_images": True,
                "skip_tls_verification": True,
                "timeout": 0,
                "wait_for": 0,
            },
            webhook="webhook",
        )
        assert_matches_type(CrawlResponse, crawl, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTaamCloud) -> None:
        response = await async_client.crawl.with_raw_response.create(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(CrawlResponse, crawl, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTaamCloud) -> None:
        async with async_client.crawl.with_streaming_response.create(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(CrawlResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTaamCloud) -> None:
        crawl = await async_client.crawl.retrieve(
            "id",
        )
        assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTaamCloud) -> None:
        response = await async_client.crawl.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTaamCloud) -> None:
        async with async_client.crawl.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(CrawlStatusResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTaamCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.crawl.with_raw_response.retrieve(
                "",
            )
