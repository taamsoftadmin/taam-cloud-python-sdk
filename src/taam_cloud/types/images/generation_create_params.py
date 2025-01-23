# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GenerationCreateParams"]


class GenerationCreateParams(TypedDict, total=False):
    prompt: Required[str]
    """Text description of the desired image"""

    model: Literal["dall-e-3"]

    n: int
    """Number of images to generate"""

    quality: Literal["standard", "hd"]

    size: Literal["1024x1024", "1024x1792", "1792x1024"]

    style: Literal["natural", "vivid"]
