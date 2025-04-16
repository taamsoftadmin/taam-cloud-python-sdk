# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import query_check_video_generation_status_params
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
from ..types.query_check_video_generation_status_response import QueryCheckVideoGenerationStatusResponse

__all__ = ["QueryResource", "AsyncQueryResource"]


class QueryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return QueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return QueryResourceWithStreamingResponse(self)

    def check_video_generation_status(
        self,
        *,
        task_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryCheckVideoGenerationStatusResponse:
        """
        Query the status of a video generation task

        Args:
          task_id: Task ID returned from video generation request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/query/video_generation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"task_id": task_id},
                    query_check_video_generation_status_params.QueryCheckVideoGenerationStatusParams,
                ),
            ),
            cast_to=QueryCheckVideoGenerationStatusResponse,
        )


class AsyncQueryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncQueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return AsyncQueryResourceWithStreamingResponse(self)

    async def check_video_generation_status(
        self,
        *,
        task_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryCheckVideoGenerationStatusResponse:
        """
        Query the status of a video generation task

        Args:
          task_id: Task ID returned from video generation request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/query/video_generation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"task_id": task_id},
                    query_check_video_generation_status_params.QueryCheckVideoGenerationStatusParams,
                ),
            ),
            cast_to=QueryCheckVideoGenerationStatusResponse,
        )


class QueryResourceWithRawResponse:
    def __init__(self, query: QueryResource) -> None:
        self._query = query

        self.check_video_generation_status = to_raw_response_wrapper(
            query.check_video_generation_status,
        )


class AsyncQueryResourceWithRawResponse:
    def __init__(self, query: AsyncQueryResource) -> None:
        self._query = query

        self.check_video_generation_status = async_to_raw_response_wrapper(
            query.check_video_generation_status,
        )


class QueryResourceWithStreamingResponse:
    def __init__(self, query: QueryResource) -> None:
        self._query = query

        self.check_video_generation_status = to_streamed_response_wrapper(
            query.check_video_generation_status,
        )


class AsyncQueryResourceWithStreamingResponse:
    def __init__(self, query: AsyncQueryResource) -> None:
        self._query = query

        self.check_video_generation_status = async_to_streamed_response_wrapper(
            query.check_video_generation_status,
        )
