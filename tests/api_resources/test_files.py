# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taam_cloud import TaamCloud, AsyncTaamCloud
from tests.utils import assert_matches_type
from taam_cloud.types import FileUploadResponse, FileRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: TaamCloud) -> None:
        file = client.files.retrieve(
            file_id="file_id",
        )
        assert_matches_type(FileRetrieveResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: TaamCloud) -> None:
        response = client.files.with_raw_response.retrieve(
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileRetrieveResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: TaamCloud) -> None:
        with client.files.with_streaming_response.retrieve(
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileRetrieveResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_upload(self, client: TaamCloud) -> None:
        file = client.files.upload(
            file=b"raw file contents",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_upload_with_all_params(self, client: TaamCloud) -> None:
        file = client.files.upload(
            file=b"raw file contents",
            enable_ocr="true",
            enable_vision="true",
            extract_mode="default",
            images_only="true",
            page_based="true",
            remove_headers="true",
            save_all="true",
            text_only="true",
            vision_only="true",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upload(self, client: TaamCloud) -> None:
        response = client.files.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upload(self, client: TaamCloud) -> None:
        with client.files.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileUploadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTaamCloud) -> None:
        file = await async_client.files.retrieve(
            file_id="file_id",
        )
        assert_matches_type(FileRetrieveResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTaamCloud) -> None:
        response = await async_client.files.with_raw_response.retrieve(
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileRetrieveResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTaamCloud) -> None:
        async with async_client.files.with_streaming_response.retrieve(
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileRetrieveResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload(self, async_client: AsyncTaamCloud) -> None:
        file = await async_client.files.upload(
            file=b"raw file contents",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncTaamCloud) -> None:
        file = await async_client.files.upload(
            file=b"raw file contents",
            enable_ocr="true",
            enable_vision="true",
            extract_mode="default",
            images_only="true",
            page_based="true",
            remove_headers="true",
            save_all="true",
            text_only="true",
            vision_only="true",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncTaamCloud) -> None:
        response = await async_client.files.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncTaamCloud) -> None:
        async with async_client.files.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUploadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
