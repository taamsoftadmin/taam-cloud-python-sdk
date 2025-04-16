# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebCreateParams"]


class WebCreateParams(TypedDict, total=False):
    model: Required[Literal["scrape", "crawl", "map", "taam-ai-search", "crawl-status"]]
    """Type of web service to use"""

    params: object
    """Parameters specific to the selected model"""
