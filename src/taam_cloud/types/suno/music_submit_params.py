# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MusicSubmitParams"]


class MusicSubmitParams(TypedDict, total=False):
    mv: str

    prompt: str

    tags: str

    title: str
