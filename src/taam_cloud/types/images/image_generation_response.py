# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ImageGenerationResponse", "Data"]


class Data(BaseModel):
    revised_prompt: Optional[str] = None

    url: Optional[str] = None


class ImageGenerationResponse(BaseModel):
    created: Optional[int] = None

    data: Optional[List[Data]] = None
