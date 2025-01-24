# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taam_cloud import TaamCloud, AsyncTaamCloud
from tests.utils import assert_matches_type
from taam_cloud.types import UploadResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_upload(self, client: TaamCloud) -> None:
        client_ = client.upload(
            file=b"raw file contents",
        )
        assert_matches_type(UploadResponse, client_, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: TaamCloud) -> None:
        client_ = client.upload(
            file=b"raw file contents",
            enable_ocr=True,
            enable_vision=True,
            save_all=True,
        )
        assert_matches_type(UploadResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: TaamCloud) -> None:
        response = client.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(UploadResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: TaamCloud) -> None:
        with client.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(UploadResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_upload(self, async_client: AsyncTaamCloud) -> None:
        client = await async_client.upload(
            file=b"raw file contents",
        )
        assert_matches_type(UploadResponse, client, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncTaamCloud) -> None:
        client = await async_client.upload(
            file=b"raw file contents",
            enable_ocr=True,
            enable_vision=True,
            save_all=True,
        )
        assert_matches_type(UploadResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncTaamCloud) -> None:
        response = await async_client.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(UploadResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncTaamCloud) -> None:
        async with async_client.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(UploadResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True
