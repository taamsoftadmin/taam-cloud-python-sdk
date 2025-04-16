# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ...types.suno import submit_generate_music_params
from ..._base_client import make_request_options

__all__ = ["SubmitResource", "AsyncSubmitResource"]


class SubmitResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubmitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SubmitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubmitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return SubmitResourceWithStreamingResponse(self)

    def generate_music(
        self,
        *,
        mv: str | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create AI-generated music based on text prompts

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/suno/submit/music",
            body=maybe_transform(
                {
                    "mv": mv,
                    "prompt": prompt,
                    "tags": tags,
                    "title": title,
                },
                submit_generate_music_params.SubmitGenerateMusicParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSubmitResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubmitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSubmitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubmitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return AsyncSubmitResourceWithStreamingResponse(self)

    async def generate_music(
        self,
        *,
        mv: str | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create AI-generated music based on text prompts

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/suno/submit/music",
            body=await async_maybe_transform(
                {
                    "mv": mv,
                    "prompt": prompt,
                    "tags": tags,
                    "title": title,
                },
                submit_generate_music_params.SubmitGenerateMusicParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SubmitResourceWithRawResponse:
    def __init__(self, submit: SubmitResource) -> None:
        self._submit = submit

        self.generate_music = to_raw_response_wrapper(
            submit.generate_music,
        )


class AsyncSubmitResourceWithRawResponse:
    def __init__(self, submit: AsyncSubmitResource) -> None:
        self._submit = submit

        self.generate_music = async_to_raw_response_wrapper(
            submit.generate_music,
        )


class SubmitResourceWithStreamingResponse:
    def __init__(self, submit: SubmitResource) -> None:
        self._submit = submit

        self.generate_music = to_streamed_response_wrapper(
            submit.generate_music,
        )


class AsyncSubmitResourceWithStreamingResponse:
    def __init__(self, submit: AsyncSubmitResource) -> None:
        self._submit = submit

        self.generate_music = async_to_streamed_response_wrapper(
            submit.generate_music,
        )
