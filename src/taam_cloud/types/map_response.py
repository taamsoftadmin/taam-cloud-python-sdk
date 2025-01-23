# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["MapResponse"]


class MapResponse(BaseModel):
    links: Optional[List[str]] = None

    success: Optional[bool] = None
