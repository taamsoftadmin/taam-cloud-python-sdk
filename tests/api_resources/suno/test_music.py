# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taam_cloud import TaamCloud, AsyncTaamCloud

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMusic:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_submit(self, client: TaamCloud) -> None:
        music = client.suno.music.submit()
        assert music is None

    @parametrize
    def test_method_submit_with_all_params(self, client: TaamCloud) -> None:
        music = client.suno.music.submit(
            mv="mv",
            prompt="prompt",
            tags="tags",
            title="title",
        )
        assert music is None

    @parametrize
    def test_raw_response_submit(self, client: TaamCloud) -> None:
        response = client.suno.music.with_raw_response.submit()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        music = response.parse()
        assert music is None

    @parametrize
    def test_streaming_response_submit(self, client: TaamCloud) -> None:
        with client.suno.music.with_streaming_response.submit() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            music = response.parse()
            assert music is None

        assert cast(Any, response.is_closed) is True


class TestAsyncMusic:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_submit(self, async_client: AsyncTaamCloud) -> None:
        music = await async_client.suno.music.submit()
        assert music is None

    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncTaamCloud) -> None:
        music = await async_client.suno.music.submit(
            mv="mv",
            prompt="prompt",
            tags="tags",
            title="title",
        )
        assert music is None

    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncTaamCloud) -> None:
        response = await async_client.suno.music.with_raw_response.submit()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        music = await response.parse()
        assert music is None

    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncTaamCloud) -> None:
        async with async_client.suno.music.with_streaming_response.submit() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            music = await response.parse()
            assert music is None

        assert cast(Any, response.is_closed) is True
