# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "UploadCreateResponse",
    "FileUploadResponse",
    "FileEmbeddingsResponse",
    "FileEmbeddingsResponseData",
    "FileEmbeddingsResponseDataData",
    "FileEmbeddingsResponseDataDataChunk",
    "FileEmbeddingsResponseDataDataMetadata",
    "FileEmbeddingsResponseUsage",
]


class FileUploadResponse(BaseModel):
    content: Optional[str] = None
    """Extracted text or data URL"""

    error: Optional[str] = None
    """Error message (if any)"""

    status: Optional[bool] = None
    """Operation status"""

    type: Optional[Literal["pdf", "docx", "pptx", "xlsx", "image", "audio", "text", "error"]] = None
    """Type of the processed file"""


class FileEmbeddingsResponseDataDataChunk(BaseModel):
    content: Optional[str] = None
    """Text content of the chunk"""

    from_page: Optional[int] = None
    """Page number the chunk is from"""

    total_tokens: Optional[int] = None
    """Number of tokens in the chunk"""


class FileEmbeddingsResponseDataDataMetadata(BaseModel):
    description: Optional[str] = None
    """Document description"""

    language: Optional[str] = None
    """Document language"""

    title: Optional[str] = None
    """Document title"""


class FileEmbeddingsResponseDataData(BaseModel):
    chunks: Optional[List[FileEmbeddingsResponseDataDataChunk]] = None

    metadata: Optional[FileEmbeddingsResponseDataDataMetadata] = None


class FileEmbeddingsResponseData(BaseModel):
    data: Optional[FileEmbeddingsResponseDataData] = None

    success: Optional[bool] = None


class FileEmbeddingsResponseUsage(BaseModel):
    total_chunks: Optional[int] = None
    """Total number of chunks"""

    total_extracted_text: Optional[int] = None
    """Total characters of extracted text"""

    total_pages: Optional[int] = None
    """Total number of pages"""

    total_tokens: Optional[int] = None
    """Total number of tokens"""


class FileEmbeddingsResponse(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the request"""

    created: Optional[int] = None
    """Unix timestamp when the request was created"""

    data: Optional[FileEmbeddingsResponseData] = None

    error: Optional[str] = None
    """Error message (if any)"""

    object: Optional[str] = None
    """Object type (e.g., 'chunks')"""

    type: Optional[str] = None
    """Type of the processed file"""

    usage: Optional[FileEmbeddingsResponseUsage] = None


UploadCreateResponse: TypeAlias = Union[FileUploadResponse, FileEmbeddingsResponse]
