# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WebCreateResponse", "Usage"]


class Usage(BaseModel):
    completion_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None


class WebCreateResponse(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the request"""

    created: Optional[int] = None
    """Unix timestamp of when the request was created"""

    data: Optional[object] = None
    """Model-specific response data"""

    model: Optional[str] = None
    """Model used for the request"""

    object: Optional[str] = None
    """Type of completion (e.g., scrape.completion)"""

    system_fingerprint: Optional[str] = None

    usage: Optional[Usage] = None
