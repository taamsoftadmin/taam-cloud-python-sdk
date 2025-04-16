# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import web, chat, files, query, images, models, rerank, upload, embeddings, video_generation
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, TaamCloudError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.suno import suno

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "TaamCloud",
    "AsyncTaamCloud",
    "Client",
    "AsyncClient",
]


class TaamCloud(SyncAPIClient):
    embeddings: embeddings.EmbeddingsResource
    rerank: rerank.RerankResource
    chat: chat.ChatResource
    suno: suno.SunoResource
    models: models.ModelsResource
    images: images.ImagesResource
    web: web.WebResource
    files: files.FilesResource
    upload: upload.UploadResource
    video_generation: video_generation.VideoGenerationResource
    query: query.QueryResource
    with_raw_response: TaamCloudWithRawResponse
    with_streaming_response: TaamCloudWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
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
        """Construct a new synchronous TaamCloud client instance.

        This automatically infers the `bearer_token` argument from the `TAAM_CLOUD_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("TAAM_CLOUD_BEARER_TOKEN")
        if bearer_token is None:
            raise TaamCloudError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the TAAM_CLOUD_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("TAAM_CLOUD_BASE_URL")
        if base_url is None:
            base_url = f"https://api.taam.cloud"

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
        self.web = web.WebResource(self)
        self.files = files.FilesResource(self)
        self.upload = upload.UploadResource(self)
        self.video_generation = video_generation.VideoGenerationResource(self)
        self.query = query.QueryResource(self)
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
    web: web.AsyncWebResource
    files: files.AsyncFilesResource
    upload: upload.AsyncUploadResource
    video_generation: video_generation.AsyncVideoGenerationResource
    query: query.AsyncQueryResource
    with_raw_response: AsyncTaamCloudWithRawResponse
    with_streaming_response: AsyncTaamCloudWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
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
        """Construct a new async AsyncTaamCloud client instance.

        This automatically infers the `bearer_token` argument from the `TAAM_CLOUD_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("TAAM_CLOUD_BEARER_TOKEN")
        if bearer_token is None:
            raise TaamCloudError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the TAAM_CLOUD_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("TAAM_CLOUD_BASE_URL")
        if base_url is None:
            base_url = f"https://api.taam.cloud"

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
        self.web = web.AsyncWebResource(self)
        self.files = files.AsyncFilesResource(self)
        self.upload = upload.AsyncUploadResource(self)
        self.video_generation = video_generation.AsyncVideoGenerationResource(self)
        self.query = query.AsyncQueryResource(self)
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
        self.web = web.WebResourceWithRawResponse(client.web)
        self.files = files.FilesResourceWithRawResponse(client.files)
        self.upload = upload.UploadResourceWithRawResponse(client.upload)
        self.video_generation = video_generation.VideoGenerationResourceWithRawResponse(client.video_generation)
        self.query = query.QueryResourceWithRawResponse(client.query)


class AsyncTaamCloudWithRawResponse:
    def __init__(self, client: AsyncTaamCloud) -> None:
        self.embeddings = embeddings.AsyncEmbeddingsResourceWithRawResponse(client.embeddings)
        self.rerank = rerank.AsyncRerankResourceWithRawResponse(client.rerank)
        self.chat = chat.AsyncChatResourceWithRawResponse(client.chat)
        self.suno = suno.AsyncSunoResourceWithRawResponse(client.suno)
        self.models = models.AsyncModelsResourceWithRawResponse(client.models)
        self.images = images.AsyncImagesResourceWithRawResponse(client.images)
        self.web = web.AsyncWebResourceWithRawResponse(client.web)
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)
        self.upload = upload.AsyncUploadResourceWithRawResponse(client.upload)
        self.video_generation = video_generation.AsyncVideoGenerationResourceWithRawResponse(client.video_generation)
        self.query = query.AsyncQueryResourceWithRawResponse(client.query)


class TaamCloudWithStreamedResponse:
    def __init__(self, client: TaamCloud) -> None:
        self.embeddings = embeddings.EmbeddingsResourceWithStreamingResponse(client.embeddings)
        self.rerank = rerank.RerankResourceWithStreamingResponse(client.rerank)
        self.chat = chat.ChatResourceWithStreamingResponse(client.chat)
        self.suno = suno.SunoResourceWithStreamingResponse(client.suno)
        self.models = models.ModelsResourceWithStreamingResponse(client.models)
        self.images = images.ImagesResourceWithStreamingResponse(client.images)
        self.web = web.WebResourceWithStreamingResponse(client.web)
        self.files = files.FilesResourceWithStreamingResponse(client.files)
        self.upload = upload.UploadResourceWithStreamingResponse(client.upload)
        self.video_generation = video_generation.VideoGenerationResourceWithStreamingResponse(client.video_generation)
        self.query = query.QueryResourceWithStreamingResponse(client.query)


class AsyncTaamCloudWithStreamedResponse:
    def __init__(self, client: AsyncTaamCloud) -> None:
        self.embeddings = embeddings.AsyncEmbeddingsResourceWithStreamingResponse(client.embeddings)
        self.rerank = rerank.AsyncRerankResourceWithStreamingResponse(client.rerank)
        self.chat = chat.AsyncChatResourceWithStreamingResponse(client.chat)
        self.suno = suno.AsyncSunoResourceWithStreamingResponse(client.suno)
        self.models = models.AsyncModelsResourceWithStreamingResponse(client.models)
        self.images = images.AsyncImagesResourceWithStreamingResponse(client.images)
        self.web = web.AsyncWebResourceWithStreamingResponse(client.web)
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)
        self.upload = upload.AsyncUploadResourceWithStreamingResponse(client.upload)
        self.video_generation = video_generation.AsyncVideoGenerationResourceWithStreamingResponse(
            client.video_generation
        )
        self.query = query.AsyncQueryResourceWithStreamingResponse(client.query)


Client = TaamCloud

AsyncClient = AsyncTaamCloud
