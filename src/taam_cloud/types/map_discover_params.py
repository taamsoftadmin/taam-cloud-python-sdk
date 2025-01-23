# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MapDiscoverParams"]


class MapDiscoverParams(TypedDict, total=False):
    url: Required[str]
    """The base URL to start mapping from"""

    ignore_sitemap: Annotated[bool, PropertyInfo(alias="ignoreSitemap")]
    """Ignore the website sitemap when crawling"""

    include_subdomains: Annotated[bool, PropertyInfo(alias="includeSubdomains")]
    """Include subdomains of the website"""

    limit: int
    """Maximum number of links to return"""

    search: str
    """Search query to use for mapping"""

    sitemap_only: Annotated[bool, PropertyInfo(alias="sitemapOnly")]
    """Only return links found in the website sitemap"""
