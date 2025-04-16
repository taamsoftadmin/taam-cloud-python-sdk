# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import web_create_params
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
from ..types.web_create_response import WebCreateResponse

__all__ = ["WebResource", "AsyncWebResource"]


class WebResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WebResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return WebResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: Literal["scrape", "crawl", "map", "taam-ai-search", "crawl-status"],
        params: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebCreateResponse:
        """
        Unified endpoint for web scraping, crawling, mapping and AI search

        Args:
          model: Type of web service to use

          params: Parameters specific to the selected model

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/web",
            body=maybe_transform(
                {
                    "model": model,
                    "params": params,
                },
                web_create_params.WebCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebCreateResponse,
        )


class AsyncWebResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWebResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return AsyncWebResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: Literal["scrape", "crawl", "map", "taam-ai-search", "crawl-status"],
        params: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebCreateResponse:
        """
        Unified endpoint for web scraping, crawling, mapping and AI search

        Args:
          model: Type of web service to use

          params: Parameters specific to the selected model

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/web",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "params": params,
                },
                web_create_params.WebCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebCreateResponse,
        )


class WebResourceWithRawResponse:
    def __init__(self, web: WebResource) -> None:
        self._web = web

        self.create = to_raw_response_wrapper(
            web.create,
        )


class AsyncWebResourceWithRawResponse:
    def __init__(self, web: AsyncWebResource) -> None:
        self._web = web

        self.create = async_to_raw_response_wrapper(
            web.create,
        )


class WebResourceWithStreamingResponse:
    def __init__(self, web: WebResource) -> None:
        self._web = web

        self.create = to_streamed_response_wrapper(
            web.create,
        )


class AsyncWebResourceWithStreamingResponse:
    def __init__(self, web: AsyncWebResource) -> None:
        self._web = web

        self.create = async_to_streamed_response_wrapper(
            web.create,
        )
