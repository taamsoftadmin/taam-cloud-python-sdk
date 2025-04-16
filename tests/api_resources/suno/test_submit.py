# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taam_cloud import TaamCloud, AsyncTaamCloud

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubmit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_generate_music(self, client: TaamCloud) -> None:
        submit = client.suno.submit.generate_music()
        assert submit is None

    @pytest.mark.skip()
    @parametrize
    def test_method_generate_music_with_all_params(self, client: TaamCloud) -> None:
        submit = client.suno.submit.generate_music(
            mv="mv",
            prompt="A relaxing jazz piano piece with soft drums",
            tags="jazz, relaxing, piano",
            title="Relaxing Jazz",
        )
        assert submit is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_generate_music(self, client: TaamCloud) -> None:
        response = client.suno.submit.with_raw_response.generate_music()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submit = response.parse()
        assert submit is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_generate_music(self, client: TaamCloud) -> None:
        with client.suno.submit.with_streaming_response.generate_music() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submit = response.parse()
            assert submit is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSubmit:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate_music(self, async_client: AsyncTaamCloud) -> None:
        submit = await async_client.suno.submit.generate_music()
        assert submit is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate_music_with_all_params(self, async_client: AsyncTaamCloud) -> None:
        submit = await async_client.suno.submit.generate_music(
            mv="mv",
            prompt="A relaxing jazz piano piece with soft drums",
            tags="jazz, relaxing, piano",
            title="Relaxing Jazz",
        )
        assert submit is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_generate_music(self, async_client: AsyncTaamCloud) -> None:
        response = await async_client.suno.submit.with_raw_response.generate_music()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submit = await response.parse()
        assert submit is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_generate_music(self, async_client: AsyncTaamCloud) -> None:
        async with async_client.suno.submit.with_streaming_response.generate_music() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submit = await response.parse()
            assert submit is None

        assert cast(Any, response.is_closed) is True
