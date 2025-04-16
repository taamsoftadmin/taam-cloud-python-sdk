# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["FileRetrieveResponse", "BaseResp", "File"]


class BaseResp(BaseModel):
    status_code: Optional[int] = None
    """Status code (0 for success)"""

    status_msg: Optional[str] = None
    """Status message"""


class File(BaseModel):
    bytes: Optional[int] = None
    """File size in bytes"""

    created_at: Optional[int] = None
    """Unix timestamp of when the file was created"""

    download_url: Optional[str] = None
    """URL to download the file"""

    file_id: Optional[str] = None
    """File identifier"""

    filename: Optional[str] = None
    """Name of the file"""

    purpose: Optional[str] = None
    """Purpose of the file"""


class FileRetrieveResponse(BaseModel):
    base_resp: Optional[BaseResp] = None

    file: Optional[File] = None
