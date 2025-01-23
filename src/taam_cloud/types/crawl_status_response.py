# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CrawlStatusResponse", "Data", "DataMetadata"]


class DataMetadata(BaseModel):
    description: Optional[str] = None

    error: Optional[str] = None

    language: Optional[str] = None

    source_url: Optional[str] = FieldInfo(alias="sourceURL", default=None)

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)

    title: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Data(BaseModel):
    html: Optional[str] = None

    links: Optional[List[str]] = None

    markdown: Optional[str] = None

    metadata: Optional[DataMetadata] = None

    raw_html: Optional[str] = FieldInfo(alias="rawHtml", default=None)

    screenshot: Optional[str] = None


class CrawlStatusResponse(BaseModel):
    completed: Optional[int] = None
    """Number of successfully crawled pages"""

    credits_used: Optional[int] = FieldInfo(alias="creditsUsed", default=None)
    """Credits consumed by the crawl"""

    data: Optional[List[Data]] = None

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)
    """Expiration date of the crawl data"""

    next: Optional[str] = None
    """URL to retrieve next batch of data"""

    status: Optional[Literal["scraping", "completed", "failed"]] = None
    """Current status of the crawl"""

    total: Optional[int] = None
    """Total number of pages attempted"""
