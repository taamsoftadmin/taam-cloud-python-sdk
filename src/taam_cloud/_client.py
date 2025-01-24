# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import client_upload_params
from ._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    FileTypes,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    get_async_library,
    async_maybe_transform,
)
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .resources import maps, crawl, models, rerank, scrape, searches, embeddings
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, TaamCloudError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .resources.chat import chat
from .resources.suno import suno
from .resources.images import images
from .types.upload_response import UploadResponse

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "TaamCloud",
    "AsyncTaamCloud",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://newapi.taam.cloud",
    "environment_1": "https://uploud.taam.cloud",
    "environment_2": "https://crawl.taam.cloud",
    "environment_3": "https://apisearch.taam.cloud",
}


class TaamCloud(SyncAPIClient):
    embeddings: embeddings.EmbeddingsResource
    rerank: rerank.RerankResource
    chat: chat.ChatResource
    suno: suno.SunoResource
    models: models.ModelsResource
    images: images.ImagesResource
    crawl: crawl.CrawlResource
    scrape: scrape.ScrapeResource
    maps: maps.MapsResource
    searches: searches.SearchesResource
    with_raw_response: TaamCloudWithRawResponse
    with_streaming_response: TaamCloudWithStreamedResponse

    # client options
    bearer_token: str

    _environment: Literal["production", "environment_1", "environment_2", "environment_3"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1", "environment_2", "environment_3"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous taam-cloud client instance.

        This automatically infers the `bearer_token` argument from the `BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("BEARER_TOKEN")
        if bearer_token is None:
            raise TaamCloudError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        self._environment = environment

        base_url_env = os.environ.get("TAAM_CLOUD_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `TAAM_CLOUD_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.embeddings = embeddings.EmbeddingsResource(self)
        self.rerank = rerank.RerankResource(self)
        self.chat = chat.ChatResource(self)
        self.suno = suno.SunoResource(self)
        self.models = models.ModelsResource(self)
        self.images = images.ImagesResource(self)
        self.crawl = crawl.CrawlResource(self)
        self.scrape = scrape.ScrapeResource(self)
        self.maps = maps.MapsResource(self)
        self.searches = searches.SearchesResource(self)
        self.with_raw_response = TaamCloudWithRawResponse(self)
        self.with_streaming_response = TaamCloudWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1", "environment_2", "environment_3"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def upload(
        self,
        *,
        file: FileTypes,
        enable_ocr: bool | NotGiven = NOT_GIVEN,
        enable_vision: bool | NotGiven = NOT_GIVEN,
        save_all: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UploadResponse:
        """
        Upload and process files with optional OCR and Vision capabilities

        Args:
          file: File to upload

          enable_ocr: Enable OCR processing

          enable_vision: Enable Vision processing

          save_all: Save raw files

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
                "save_all": save_all,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self.post(
            "/upload",
            body=maybe_transform(body, client_upload_params.ClientUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncTaamCloud(AsyncAPIClient):
    embeddings: embeddings.AsyncEmbeddingsResource
    rerank: rerank.AsyncRerankResource
    chat: chat.AsyncChatResource
    suno: suno.AsyncSunoResource
    models: models.AsyncModelsResource
    images: images.AsyncImagesResource
    crawl: crawl.AsyncCrawlResource
    scrape: scrape.AsyncScrapeResource
    maps: maps.AsyncMapsResource
    searches: searches.AsyncSearchesResource
    with_raw_response: AsyncTaamCloudWithRawResponse
    with_streaming_response: AsyncTaamCloudWithStreamedResponse

    # client options
    bearer_token: str

    _environment: Literal["production", "environment_1", "environment_2", "environment_3"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1", "environment_2", "environment_3"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async taam-cloud client instance.

        This automatically infers the `bearer_token` argument from the `BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("BEARER_TOKEN")
        if bearer_token is None:
            raise TaamCloudError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        self._environment = environment

        base_url_env = os.environ.get("TAAM_CLOUD_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `TAAM_CLOUD_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.embeddings = embeddings.AsyncEmbeddingsResource(self)
        self.rerank = rerank.AsyncRerankResource(self)
        self.chat = chat.AsyncChatResource(self)
        self.suno = suno.AsyncSunoResource(self)
        self.models = models.AsyncModelsResource(self)
        self.images = images.AsyncImagesResource(self)
        self.crawl = crawl.AsyncCrawlResource(self)
        self.scrape = scrape.AsyncScrapeResource(self)
        self.maps = maps.AsyncMapsResource(self)
        self.searches = searches.AsyncSearchesResource(self)
        self.with_raw_response = AsyncTaamCloudWithRawResponse(self)
        self.with_streaming_response = AsyncTaamCloudWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1", "environment_2", "environment_3"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def upload(
        self,
        *,
        file: FileTypes,
        enable_ocr: bool | NotGiven = NOT_GIVEN,
        enable_vision: bool | NotGiven = NOT_GIVEN,
        save_all: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UploadResponse:
        """
        Upload and process files with optional OCR and Vision capabilities

        Args:
          file: File to upload

          enable_ocr: Enable OCR processing

          enable_vision: Enable Vision processing

          save_all: Save raw files

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
                "save_all": save_all,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self.post(
            "/upload",
            body=await async_maybe_transform(body, client_upload_params.ClientUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class TaamCloudWithRawResponse:
    def __init__(self, client: TaamCloud) -> None:
        self.embeddings = embeddings.EmbeddingsResourceWithRawResponse(client.embeddings)
        self.rerank = rerank.RerankResourceWithRawResponse(client.rerank)
        self.chat = chat.ChatResourceWithRawResponse(client.chat)
        self.suno = suno.SunoResourceWithRawResponse(client.suno)
        self.models = models.ModelsResourceWithRawResponse(client.models)
        self.images = images.ImagesResourceWithRawResponse(client.images)
        self.crawl = crawl.CrawlResourceWithRawResponse(client.crawl)
        self.scrape = scrape.ScrapeResourceWithRawResponse(client.scrape)
        self.maps = maps.MapsResourceWithRawResponse(client.maps)
        self.searches = searches.SearchesResourceWithRawResponse(client.searches)

        self.upload = to_raw_response_wrapper(
            client.upload,
        )


class AsyncTaamCloudWithRawResponse:
    def __init__(self, client: AsyncTaamCloud) -> None:
        self.embeddings = embeddings.AsyncEmbeddingsResourceWithRawResponse(client.embeddings)
        self.rerank = rerank.AsyncRerankResourceWithRawResponse(client.rerank)
        self.chat = chat.AsyncChatResourceWithRawResponse(client.chat)
        self.suno = suno.AsyncSunoResourceWithRawResponse(client.suno)
        self.models = models.AsyncModelsResourceWithRawResponse(client.models)
        self.images = images.AsyncImagesResourceWithRawResponse(client.images)
        self.crawl = crawl.AsyncCrawlResourceWithRawResponse(client.crawl)
        self.scrape = scrape.AsyncScrapeResourceWithRawResponse(client.scrape)
        self.maps = maps.AsyncMapsResourceWithRawResponse(client.maps)
        self.searches = searches.AsyncSearchesResourceWithRawResponse(client.searches)

        self.upload = async_to_raw_response_wrapper(
            client.upload,
        )


class TaamCloudWithStreamedResponse:
    def __init__(self, client: TaamCloud) -> None:
        self.embeddings = embeddings.EmbeddingsResourceWithStreamingResponse(client.embeddings)
        self.rerank = rerank.RerankResourceWithStreamingResponse(client.rerank)
        self.chat = chat.ChatResourceWithStreamingResponse(client.chat)
        self.suno = suno.SunoResourceWithStreamingResponse(client.suno)
        self.models = models.ModelsResourceWithStreamingResponse(client.models)
        self.images = images.ImagesResourceWithStreamingResponse(client.images)
        self.crawl = crawl.CrawlResourceWithStreamingResponse(client.crawl)
        self.scrape = scrape.ScrapeResourceWithStreamingResponse(client.scrape)
        self.maps = maps.MapsResourceWithStreamingResponse(client.maps)
        self.searches = searches.SearchesResourceWithStreamingResponse(client.searches)

        self.upload = to_streamed_response_wrapper(
            client.upload,
        )


class AsyncTaamCloudWithStreamedResponse:
    def __init__(self, client: AsyncTaamCloud) -> None:
        self.embeddings = embeddings.AsyncEmbeddingsResourceWithStreamingResponse(client.embeddings)
        self.rerank = rerank.AsyncRerankResourceWithStreamingResponse(client.rerank)
        self.chat = chat.AsyncChatResourceWithStreamingResponse(client.chat)
        self.suno = suno.AsyncSunoResourceWithStreamingResponse(client.suno)
        self.models = models.AsyncModelsResourceWithStreamingResponse(client.models)
        self.images = images.AsyncImagesResourceWithStreamingResponse(client.images)
        self.crawl = crawl.AsyncCrawlResourceWithStreamingResponse(client.crawl)
        self.scrape = scrape.AsyncScrapeResourceWithStreamingResponse(client.scrape)
        self.maps = maps.AsyncMapsResourceWithStreamingResponse(client.maps)
        self.searches = searches.AsyncSearchesResourceWithStreamingResponse(client.searches)

        self.upload = async_to_streamed_response_wrapper(
            client.upload,
        )


Client = TaamCloud

AsyncClient = AsyncTaamCloud
