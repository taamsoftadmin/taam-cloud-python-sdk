# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["QueryCheckVideoGenerationStatusResponse", "BaseResp"]


class BaseResp(BaseModel):
    status_code: Optional[int] = None
    """Status code (0 for success)"""

    status_msg: Optional[str] = None
    """Status message"""


class QueryCheckVideoGenerationStatusResponse(BaseModel):
    base_resp: Optional[BaseResp] = None

    file_id: Optional[str] = None
    """File identifier for the generated video (only present when status is 'Success')"""

    status: Optional[Literal["Queueing", "Preparing", "Processing", "Success", "Fail"]] = None
    """Current status of the task"""

    task_id: Optional[str] = None
    """Task identifier"""
