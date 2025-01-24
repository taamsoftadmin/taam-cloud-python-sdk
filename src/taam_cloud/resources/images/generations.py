# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.images import generation_create_params
from ...types.images.image_generation_response import ImageGenerationResponse

__all__ = ["GenerationsResource", "AsyncGenerationsResource"]


class GenerationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return GenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return GenerationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        prompt: str,
        model: Literal["dall-e-3"] | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        quality: Literal["standard", "hd"] | NotGiven = NOT_GIVEN,
        size: Literal["1024x1024", "1024x1792", "1792x1024"] | NotGiven = NOT_GIVEN,
        style: Literal["natural", "vivid"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageGenerationResponse:
        """
        Create images from text descriptions

        Args:
          prompt: Text description of the desired image

          n: Number of images to generate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/images/generations",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "model": model,
                    "n": n,
                    "quality": quality,
                    "size": size,
                    "style": style,
                },
                generation_create_params.GenerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageGenerationResponse,
        )


class AsyncGenerationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return AsyncGenerationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        prompt: str,
        model: Literal["dall-e-3"] | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        quality: Literal["standard", "hd"] | NotGiven = NOT_GIVEN,
        size: Literal["1024x1024", "1024x1792", "1792x1024"] | NotGiven = NOT_GIVEN,
        style: Literal["natural", "vivid"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageGenerationResponse:
        """
        Create images from text descriptions

        Args:
          prompt: Text description of the desired image

          n: Number of images to generate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/images/generations",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "model": model,
                    "n": n,
                    "quality": quality,
                    "size": size,
                    "style": style,
                },
                generation_create_params.GenerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageGenerationResponse,
        )


class GenerationsResourceWithRawResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.create = to_raw_response_wrapper(
            generations.create,
        )


class AsyncGenerationsResourceWithRawResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.create = async_to_raw_response_wrapper(
            generations.create,
        )


class GenerationsResourceWithStreamingResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.create = to_streamed_response_wrapper(
            generations.create,
        )


class AsyncGenerationsResourceWithStreamingResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.create = async_to_streamed_response_wrapper(
            generations.create,
        )
