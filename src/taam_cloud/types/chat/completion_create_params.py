# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CompletionCreateParams", "Message"]


class CompletionCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    model: Required[str]

    max_tokens: int

    stream: bool
    """Whether to stream the response"""

    temperature: float


class Message(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["user", "assistant", "system"]]
