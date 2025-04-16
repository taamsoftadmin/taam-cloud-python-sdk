# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileUploadResponse"]


class FileUploadResponse(BaseModel):
    content: Optional[str] = None
    """Extracted text or data URL"""

    error: Optional[str] = None
    """Error message (if any)"""

    status: Optional[bool] = None
    """Operation status"""

    type: Optional[Literal["pdf", "docx", "pptx", "xlsx", "image", "audio", "text", "error"]] = None
    """Type of the processed file"""
