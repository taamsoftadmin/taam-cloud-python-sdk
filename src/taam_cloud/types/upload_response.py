# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UploadResponse"]


class UploadResponse(BaseModel):
    content: Optional[str] = None

    error: Optional[str] = None

    status: Optional[bool] = None

    type: Optional[str] = None
