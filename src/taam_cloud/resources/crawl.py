# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import crawl_create_params
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
from ..types.crawl_response import CrawlResponse
from ..types.crawl_status_response import CrawlStatusResponse

__all__ = ["CrawlResource", "AsyncCrawlResource"]


class CrawlResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CrawlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CrawlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CrawlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return CrawlResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        url: str,
        allow_backward_links: bool | NotGiven = NOT_GIVEN,
        allow_external_links: bool | NotGiven = NOT_GIVEN,
        exclude_paths: List[str] | NotGiven = NOT_GIVEN,
        ignore_sitemap: bool | NotGiven = NOT_GIVEN,
        include_paths: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        max_depth: int | NotGiven = NOT_GIVEN,
        scrape_options: crawl_create_params.ScrapeOptions | NotGiven = NOT_GIVEN,
        webhook: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CrawlResponse:
        """
        Crawl a website with customizable options

        Args:
          url: The base URL to start crawling from

          allow_backward_links: Allow navigation to previously linked pages

          allow_external_links: Allow following external links

          exclude_paths: URL patterns to exclude from crawl

          ignore_sitemap: Ignore website sitemap

          include_paths: URL patterns to include in crawl

          limit: Maximum number of pages to crawl

          max_depth: Maximum depth to crawl

          webhook: Webhook URL for crawl events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/crawl",
            body=maybe_transform(
                {
                    "url": url,
                    "allow_backward_links": allow_backward_links,
                    "allow_external_links": allow_external_links,
                    "exclude_paths": exclude_paths,
                    "ignore_sitemap": ignore_sitemap,
                    "include_paths": include_paths,
                    "limit": limit,
                    "max_depth": max_depth,
                    "scrape_options": scrape_options,
                    "webhook": webhook,
                },
                crawl_create_params.CrawlCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrawlResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CrawlStatusResponse:
        """
        Retrieve the status and results of a crawl job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/crawl/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrawlStatusResponse,
        )


class AsyncCrawlResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCrawlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCrawlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCrawlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return AsyncCrawlResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        url: str,
        allow_backward_links: bool | NotGiven = NOT_GIVEN,
        allow_external_links: bool | NotGiven = NOT_GIVEN,
        exclude_paths: List[str] | NotGiven = NOT_GIVEN,
        ignore_sitemap: bool | NotGiven = NOT_GIVEN,
        include_paths: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        max_depth: int | NotGiven = NOT_GIVEN,
        scrape_options: crawl_create_params.ScrapeOptions | NotGiven = NOT_GIVEN,
        webhook: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CrawlResponse:
        """
        Crawl a website with customizable options

        Args:
          url: The base URL to start crawling from

          allow_backward_links: Allow navigation to previously linked pages

          allow_external_links: Allow following external links

          exclude_paths: URL patterns to exclude from crawl

          ignore_sitemap: Ignore website sitemap

          include_paths: URL patterns to include in crawl

          limit: Maximum number of pages to crawl

          max_depth: Maximum depth to crawl

          webhook: Webhook URL for crawl events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/crawl",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "allow_backward_links": allow_backward_links,
                    "allow_external_links": allow_external_links,
                    "exclude_paths": exclude_paths,
                    "ignore_sitemap": ignore_sitemap,
                    "include_paths": include_paths,
                    "limit": limit,
                    "max_depth": max_depth,
                    "scrape_options": scrape_options,
                    "webhook": webhook,
                },
                crawl_create_params.CrawlCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrawlResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CrawlStatusResponse:
        """
        Retrieve the status and results of a crawl job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/crawl/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrawlStatusResponse,
        )


class CrawlResourceWithRawResponse:
    def __init__(self, crawl: CrawlResource) -> None:
        self._crawl = crawl

        self.create = to_raw_response_wrapper(
            crawl.create,
        )
        self.retrieve = to_raw_response_wrapper(
            crawl.retrieve,
        )


class AsyncCrawlResourceWithRawResponse:
    def __init__(self, crawl: AsyncCrawlResource) -> None:
        self._crawl = crawl

        self.create = async_to_raw_response_wrapper(
            crawl.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            crawl.retrieve,
        )


class CrawlResourceWithStreamingResponse:
    def __init__(self, crawl: CrawlResource) -> None:
        self._crawl = crawl

        self.create = to_streamed_response_wrapper(
            crawl.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            crawl.retrieve,
        )


class AsyncCrawlResourceWithStreamingResponse:
    def __init__(self, crawl: AsyncCrawlResource) -> None:
        self._crawl = crawl

        self.create = async_to_streamed_response_wrapper(
            crawl.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            crawl.retrieve,
        )
