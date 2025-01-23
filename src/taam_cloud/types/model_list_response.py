# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ModelListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    type: Optional[str] = None


class ModelListResponse(BaseModel):
    data: Optional[List[Data]] = None
