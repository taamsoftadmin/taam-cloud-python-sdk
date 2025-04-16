# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VideoGenerationCreateParams"]


class VideoGenerationCreateParams(TypedDict, total=False):
    model: Required[Literal["T2V-01-Director", "I2V-01-Director", "S2V-01", "I2V-01", "I2V-01-live", "T2V-01"]]
    """Video generation model to use"""

    prompt: Required[str]
    """Text description of the video to generate.

    Can include camera movement instructions in square brackets.
    """

    first_frame_image: str
    """Base64-encoded image data for image-to-video generation"""
