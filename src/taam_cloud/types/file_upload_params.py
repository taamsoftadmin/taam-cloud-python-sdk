# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["FileUploadParams"]


class FileUploadParams(TypedDict, total=False):
    file: Required[FileTypes]
    """File to upload"""

    enable_ocr: Literal["true", "false"]
    """Enable OCR for image processing"""

    enable_vision: Literal["true", "false"]
    """Enable vision-based processing for images"""

    extract_mode: Literal["default", "embeddings"]
    """Extraction mode: 'default' or 'embeddings'"""

    images_only: Literal["true", "false"]
    """Extract only images from documents"""

    page_based: Literal["true", "false"]
    """Return page-based structured response"""

    remove_headers: Literal["true", "false"]
    """Remove headers/footers from documents"""

    save_all: Literal["true", "false"]
    """Save file to configured storage"""

    text_only: Literal["true", "false"]
    """Extract only text content"""

    vision_only: Literal["true", "false"]
    """Process with vision only"""
