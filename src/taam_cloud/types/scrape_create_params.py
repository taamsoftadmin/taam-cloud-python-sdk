# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ScrapeCreateParams"]


class ScrapeCreateParams(TypedDict, total=False):
    url: Required[str]
    """The URL to scrape"""

    formats: List[Literal["markdown", "html", "rawHtml", "links", "screenshot", "screenshot@fullPage", "json"]]

    only_main_content: Annotated[bool, PropertyInfo(alias="onlyMainContent")]
