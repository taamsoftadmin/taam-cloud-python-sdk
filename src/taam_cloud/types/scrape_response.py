# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ScrapeResponse", "Data", "DataActions", "DataMetadata"]


class DataActions(BaseModel):
    screenshots: Optional[List[str]] = None


class DataMetadata(BaseModel):
    description: Optional[str] = None

    error: Optional[str] = None

    language: Optional[str] = None

    source_url: Optional[str] = FieldInfo(alias="sourceURL", default=None)

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)

    title: Optional[str] = None


class Data(BaseModel):
    actions: Optional[DataActions] = None

    html: Optional[str] = None

    links: Optional[List[str]] = None

    llm_extraction: Optional[object] = None

    markdown: Optional[str] = None

    metadata: Optional[DataMetadata] = None

    raw_html: Optional[str] = FieldInfo(alias="rawHtml", default=None)

    screenshot: Optional[str] = None

    warning: Optional[str] = None


class ScrapeResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
