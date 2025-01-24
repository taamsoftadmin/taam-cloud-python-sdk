# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .music import (
    MusicResource,
    AsyncMusicResource,
    MusicResourceWithRawResponse,
    AsyncMusicResourceWithRawResponse,
    MusicResourceWithStreamingResponse,
    AsyncMusicResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SunoResource", "AsyncSunoResource"]


class SunoResource(SyncAPIResource):
    @cached_property
    def music(self) -> MusicResource:
        return MusicResource(self._client)

    @cached_property
    def with_raw_response(self) -> SunoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SunoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SunoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return SunoResourceWithStreamingResponse(self)


class AsyncSunoResource(AsyncAPIResource):
    @cached_property
    def music(self) -> AsyncMusicResource:
        return AsyncMusicResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSunoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSunoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSunoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/taamsoftadmin/taam-cloud-python-sdk#with_streaming_response
        """
        return AsyncSunoResourceWithStreamingResponse(self)


class SunoResourceWithRawResponse:
    def __init__(self, suno: SunoResource) -> None:
        self._suno = suno

    @cached_property
    def music(self) -> MusicResourceWithRawResponse:
        return MusicResourceWithRawResponse(self._suno.music)


class AsyncSunoResourceWithRawResponse:
    def __init__(self, suno: AsyncSunoResource) -> None:
        self._suno = suno

    @cached_property
    def music(self) -> AsyncMusicResourceWithRawResponse:
        return AsyncMusicResourceWithRawResponse(self._suno.music)


class SunoResourceWithStreamingResponse:
    def __init__(self, suno: SunoResource) -> None:
        self._suno = suno

    @cached_property
    def music(self) -> MusicResourceWithStreamingResponse:
        return MusicResourceWithStreamingResponse(self._suno.music)


class AsyncSunoResourceWithStreamingResponse:
    def __init__(self, suno: AsyncSunoResource) -> None:
        self._suno = suno

    @cached_property
    def music(self) -> AsyncMusicResourceWithStreamingResponse:
        return AsyncMusicResourceWithStreamingResponse(self._suno.music)
