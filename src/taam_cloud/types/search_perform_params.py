# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SearchPerformParams", "ChatModel", "EmbeddingModel"]


class SearchPerformParams(TypedDict, total=False):
    chat_model: Required[Annotated[ChatModel, PropertyInfo(alias="chatModel")]]

    embedding_model: Required[Annotated[EmbeddingModel, PropertyInfo(alias="embeddingModel")]]

    focus_mode: Required[
        Annotated[
            Literal[
                "webSearch", "academicSearch", "writingAssistant", "wolframAlphaSearch", "youtubeSearch", "redditSearch"
            ],
            PropertyInfo(alias="focusMode"),
        ]
    ]
    """Specifies which focus mode to use for search"""


class ChatModel(TypedDict, total=False):
    model: Required[Literal["gpt-3.5-turbo", "gpt-4", "gpt-4o", "gpt-4o-mini"]]

    provider: Required[Literal["custom_openai"]]

    custom_openai_base_url: Annotated[str, PropertyInfo(alias="customOpenAIBaseURL")]

    custom_openai_key: Annotated[str, PropertyInfo(alias="customOpenAIKey")]


class EmbeddingModel(TypedDict, total=False):
    model: Required[
        Literal[
            "text-embedding-3-large",
            "text-embedding-3-small",
            "text-embedding-ada-002",
            "jina-embeddings-v3",
            "jina-embeddings-v2-base-en",
            "jina-embeddings-v2-base-zh",
            "jina-embeddings-v2-base-code",
        ]
    ]

    provider: Required[Literal["custom_openai"]]
