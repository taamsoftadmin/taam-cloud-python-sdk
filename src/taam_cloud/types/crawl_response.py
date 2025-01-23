# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CrawlResponse"]


class CrawlResponse(BaseModel):
    id: Optional[str] = None

    success: Optional[bool] = None

    url: Optional[str] = None
