# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SearchResponse", "Source", "SourceMetadata"]


class SourceMetadata(BaseModel):
    title: Optional[str] = None

    url: Optional[str] = None


class Source(BaseModel):
    metadata: Optional[SourceMetadata] = None

    page_content: Optional[str] = FieldInfo(alias="pageContent", default=None)


class SearchResponse(BaseModel):
    message: Optional[str] = None

    sources: Optional[List[Source]] = None
