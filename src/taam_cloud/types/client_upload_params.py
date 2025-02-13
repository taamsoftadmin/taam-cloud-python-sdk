# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["ClientUploadParams"]


class ClientUploadParams(TypedDict, total=False):
    file: Required[FileTypes]
    """File to upload"""

    enable_ocr: bool
    """Enable OCR processing"""

    enable_vision: bool
    """Enable Vision processing"""

    save_all: bool
    """Save raw files"""
