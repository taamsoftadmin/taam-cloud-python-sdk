# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Mapping, cast
from typing_extensions import Literal

import httpx

from ..types import upload_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.upload_create_response import UploadCreateResponse

__all__ = ["UploadResource", "AsyncUploadResource"]


class UploadResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return UploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return UploadResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file: FileTypes,
        enable_ocr: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        enable_vision: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        extract_mode: Literal["default", "embeddings"] | NotGiven = NOT_GIVEN,
        images_only: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        page_based: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        remove_headers: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        save_all: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        text_only: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        vision_only: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UploadCreateResponse:
        """
        Process various file types including documents, images, and audio files with
        advanced extraction options

        Args:
          file: File to upload

          enable_ocr: Enable OCR for image processing

          enable_vision: Enable vision-based processing for images

          extract_mode: Extraction mode: 'default' or 'embeddings'

          images_only: Extract only images from documents

          page_based: Return page-based structured response

          remove_headers: Remove headers/footers from documents

          save_all: Save file to configured storage

          text_only: Extract only text content

          vision_only: Process with vision only

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "enable_ocr": enable_ocr,
                "enable_vision": enable_vision,
                "extract_mode": extract_mode,
                "images_only": images_only,
                "page_based": page_based,
                "remove_headers": remove_headers,
                "save_all": save_all,
                "text_only": text_only,
                "vision_only": vision_only,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return cast(
            UploadCreateResponse,
            self._post(
                "/upload",
                body=maybe_transform(body, upload_create_params.UploadCreateParams),
                files=files,
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, UploadCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncUploadResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return AsyncUploadResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file: FileTypes,
        enable_ocr: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        enable_vision: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        extract_mode: Literal["default", "embeddings"] | NotGiven = NOT_GIVEN,
        images_only: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        page_based: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        remove_headers: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        save_all: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        text_only: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        vision_only: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UploadCreateResponse:
        """
        Process various file types including documents, images, and audio files with
        advanced extraction options

        Args:
          file: File to upload

          enable_ocr: Enable OCR for image processing

          enable_vision: Enable vision-based processing for images

          extract_mode: Extraction mode: 'default' or 'embeddings'

          images_only: Extract only images from documents

          page_based: Return page-based structured response

          remove_headers: Remove headers/footers from documents

          save_all: Save file to configured storage

          text_only: Extract only text content

          vision_only: Process with vision only

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "enable_ocr": enable_ocr,
                "enable_vision": enable_vision,
                "extract_mode": extract_mode,
                "images_only": images_only,
                "page_based": page_based,
                "remove_headers": remove_headers,
                "save_all": save_all,
                "text_only": text_only,
                "vision_only": vision_only,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return cast(
            UploadCreateResponse,
            await self._post(
                "/upload",
                body=await async_maybe_transform(body, upload_create_params.UploadCreateParams),
                files=files,
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, UploadCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class UploadResourceWithRawResponse:
    def __init__(self, upload: UploadResource) -> None:
        self._upload = upload

        self.create = to_raw_response_wrapper(
            upload.create,
        )


class AsyncUploadResourceWithRawResponse:
    def __init__(self, upload: AsyncUploadResource) -> None:
        self._upload = upload

        self.create = async_to_raw_response_wrapper(
            upload.create,
        )


class UploadResourceWithStreamingResponse:
    def __init__(self, upload: UploadResource) -> None:
        self._upload = upload

        self.create = to_streamed_response_wrapper(
            upload.create,
        )


class AsyncUploadResourceWithStreamingResponse:
    def __init__(self, upload: AsyncUploadResource) -> None:
        self._upload = upload

        self.create = async_to_streamed_response_wrapper(
            upload.create,
        )
