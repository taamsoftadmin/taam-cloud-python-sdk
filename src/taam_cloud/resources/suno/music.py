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
from ...types.suno import music_submit_params
from ..._base_client import make_request_options

__all__ = ["MusicResource", "AsyncMusicResource"]


class MusicResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MusicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return MusicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MusicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return MusicResourceWithStreamingResponse(self)

    def submit(
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
        Generate music

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
                music_submit_params.MusicSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMusicResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMusicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMusicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMusicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return AsyncMusicResourceWithStreamingResponse(self)

    async def submit(
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
        Generate music

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
                music_submit_params.MusicSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MusicResourceWithRawResponse:
    def __init__(self, music: MusicResource) -> None:
        self._music = music

        self.submit = to_raw_response_wrapper(
            music.submit,
        )


class AsyncMusicResourceWithRawResponse:
    def __init__(self, music: AsyncMusicResource) -> None:
        self._music = music

        self.submit = async_to_raw_response_wrapper(
            music.submit,
        )


class MusicResourceWithStreamingResponse:
    def __init__(self, music: MusicResource) -> None:
        self._music = music

        self.submit = to_streamed_response_wrapper(
            music.submit,
        )


class AsyncMusicResourceWithStreamingResponse:
    def __init__(self, music: AsyncMusicResource) -> None:
        self._music = music

        self.submit = async_to_streamed_response_wrapper(
            music.submit,
        )
