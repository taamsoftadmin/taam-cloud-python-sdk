# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import video_generation_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
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
from ..types.video_generation_create_response import VideoGenerationCreateResponse

__all__ = ["VideoGenerationResource", "AsyncVideoGenerationResource"]


class VideoGenerationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VideoGenerationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return VideoGenerationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideoGenerationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return VideoGenerationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: Literal["T2V-01-Director", "I2V-01-Director", "S2V-01", "I2V-01", "I2V-01-live", "T2V-01"],
        prompt: str,
        first_frame_image: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VideoGenerationCreateResponse:
        """
        Create dynamic videos from text descriptions or images

        Args:
          model: Video generation model to use

          prompt: Text description of the video to generate. Can include camera movement
              instructions in square brackets.

          first_frame_image: Base64-encoded image data for image-to-video generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/video_generation",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "first_frame_image": first_frame_image,
                },
                video_generation_create_params.VideoGenerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoGenerationCreateResponse,
        )


class AsyncVideoGenerationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVideoGenerationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncVideoGenerationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideoGenerationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return AsyncVideoGenerationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: Literal["T2V-01-Director", "I2V-01-Director", "S2V-01", "I2V-01", "I2V-01-live", "T2V-01"],
        prompt: str,
        first_frame_image: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VideoGenerationCreateResponse:
        """
        Create dynamic videos from text descriptions or images

        Args:
          model: Video generation model to use

          prompt: Text description of the video to generate. Can include camera movement
              instructions in square brackets.

          first_frame_image: Base64-encoded image data for image-to-video generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/video_generation",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "first_frame_image": first_frame_image,
                },
                video_generation_create_params.VideoGenerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoGenerationCreateResponse,
        )


class VideoGenerationResourceWithRawResponse:
    def __init__(self, video_generation: VideoGenerationResource) -> None:
        self._video_generation = video_generation

        self.create = to_raw_response_wrapper(
            video_generation.create,
        )


class AsyncVideoGenerationResourceWithRawResponse:
    def __init__(self, video_generation: AsyncVideoGenerationResource) -> None:
        self._video_generation = video_generation

        self.create = async_to_raw_response_wrapper(
            video_generation.create,
        )


class VideoGenerationResourceWithStreamingResponse:
    def __init__(self, video_generation: VideoGenerationResource) -> None:
        self._video_generation = video_generation

        self.create = to_streamed_response_wrapper(
            video_generation.create,
        )


class AsyncVideoGenerationResourceWithStreamingResponse:
    def __init__(self, video_generation: AsyncVideoGenerationResource) -> None:
        self._video_generation = video_generation

        self.create = async_to_streamed_response_wrapper(
            video_generation.create,
        )
