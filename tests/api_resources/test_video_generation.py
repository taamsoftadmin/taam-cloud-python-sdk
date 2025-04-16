# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taam_cloud import TaamCloud, AsyncTaamCloud
from tests.utils import assert_matches_type
from taam_cloud.types import VideoGenerationCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVideoGeneration:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: TaamCloud) -> None:
        video_generation = client.video_generation.create(
            model="T2V-01-Director",
            prompt="A spaceship landing on a distant planet [camera panning right]",
        )
        assert_matches_type(VideoGenerationCreateResponse, video_generation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: TaamCloud) -> None:
        video_generation = client.video_generation.create(
            model="T2V-01-Director",
            prompt="A spaceship landing on a distant planet [camera panning right]",
            first_frame_image="first_frame_image",
        )
        assert_matches_type(VideoGenerationCreateResponse, video_generation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: TaamCloud) -> None:
        response = client.video_generation.with_raw_response.create(
            model="T2V-01-Director",
            prompt="A spaceship landing on a distant planet [camera panning right]",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video_generation = response.parse()
        assert_matches_type(VideoGenerationCreateResponse, video_generation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: TaamCloud) -> None:
        with client.video_generation.with_streaming_response.create(
            model="T2V-01-Director",
            prompt="A spaceship landing on a distant planet [camera panning right]",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video_generation = response.parse()
            assert_matches_type(VideoGenerationCreateResponse, video_generation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVideoGeneration:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTaamCloud) -> None:
        video_generation = await async_client.video_generation.create(
            model="T2V-01-Director",
            prompt="A spaceship landing on a distant planet [camera panning right]",
        )
        assert_matches_type(VideoGenerationCreateResponse, video_generation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTaamCloud) -> None:
        video_generation = await async_client.video_generation.create(
            model="T2V-01-Director",
            prompt="A spaceship landing on a distant planet [camera panning right]",
            first_frame_image="first_frame_image",
        )
        assert_matches_type(VideoGenerationCreateResponse, video_generation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTaamCloud) -> None:
        response = await async_client.video_generation.with_raw_response.create(
            model="T2V-01-Director",
            prompt="A spaceship landing on a distant planet [camera panning right]",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video_generation = await response.parse()
        assert_matches_type(VideoGenerationCreateResponse, video_generation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTaamCloud) -> None:
        async with async_client.video_generation.with_streaming_response.create(
            model="T2V-01-Director",
            prompt="A spaceship landing on a distant planet [camera panning right]",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video_generation = await response.parse()
            assert_matches_type(VideoGenerationCreateResponse, video_generation, path=["response"])

        assert cast(Any, response.is_closed) is True
