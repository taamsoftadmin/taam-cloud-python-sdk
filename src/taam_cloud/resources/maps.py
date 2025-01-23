# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import map_discover_params
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
from ..types.map_response import MapResponse

__all__ = ["MapsResource", "AsyncMapsResource"]


class MapsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MapsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return MapsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MapsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return MapsResourceWithStreamingResponse(self)

    def discover(
        self,
        *,
        url: str,
        ignore_sitemap: bool | NotGiven = NOT_GIVEN,
        include_subdomains: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        sitemap_only: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MapResponse:
        """
        Discover and map all links on a website

        Args:
          url: The base URL to start mapping from

          ignore_sitemap: Ignore the website sitemap when crawling

          include_subdomains: Include subdomains of the website

          limit: Maximum number of links to return

          search: Search query to use for mapping

          sitemap_only: Only return links found in the website sitemap

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/map",
            body=maybe_transform(
                {
                    "url": url,
                    "ignore_sitemap": ignore_sitemap,
                    "include_subdomains": include_subdomains,
                    "limit": limit,
                    "search": search,
                    "sitemap_only": sitemap_only,
                },
                map_discover_params.MapDiscoverParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MapResponse,
        )


class AsyncMapsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMapsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMapsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMapsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return AsyncMapsResourceWithStreamingResponse(self)

    async def discover(
        self,
        *,
        url: str,
        ignore_sitemap: bool | NotGiven = NOT_GIVEN,
        include_subdomains: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        sitemap_only: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MapResponse:
        """
        Discover and map all links on a website

        Args:
          url: The base URL to start mapping from

          ignore_sitemap: Ignore the website sitemap when crawling

          include_subdomains: Include subdomains of the website

          limit: Maximum number of links to return

          search: Search query to use for mapping

          sitemap_only: Only return links found in the website sitemap

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/map",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "ignore_sitemap": ignore_sitemap,
                    "include_subdomains": include_subdomains,
                    "limit": limit,
                    "search": search,
                    "sitemap_only": sitemap_only,
                },
                map_discover_params.MapDiscoverParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MapResponse,
        )


class MapsResourceWithRawResponse:
    def __init__(self, maps: MapsResource) -> None:
        self._maps = maps

        self.discover = to_raw_response_wrapper(
            maps.discover,
        )


class AsyncMapsResourceWithRawResponse:
    def __init__(self, maps: AsyncMapsResource) -> None:
        self._maps = maps

        self.discover = async_to_raw_response_wrapper(
            maps.discover,
        )


class MapsResourceWithStreamingResponse:
    def __init__(self, maps: MapsResource) -> None:
        self._maps = maps

        self.discover = to_streamed_response_wrapper(
            maps.discover,
        )


class AsyncMapsResourceWithStreamingResponse:
    def __init__(self, maps: AsyncMapsResource) -> None:
        self._maps = maps

        self.discover = async_to_streamed_response_wrapper(
            maps.discover,
        )
