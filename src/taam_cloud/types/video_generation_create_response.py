# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VideoGenerationCreateResponse", "BaseResp"]


class BaseResp(BaseModel):
    status_code: Optional[int] = None
    """Status code (0 for success)"""

    status_msg: Optional[str] = None
    """Status message"""


class VideoGenerationCreateResponse(BaseModel):
    base_resp: Optional[BaseResp] = None

    task_id: Optional[str] = None
    """Unique identifier for the generation task"""
