# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SubmitGenerateMusicParams"]


class SubmitGenerateMusicParams(TypedDict, total=False):
    mv: str

    prompt: str

    tags: str

    title: str
