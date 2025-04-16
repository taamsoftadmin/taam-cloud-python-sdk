# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["QueryCheckVideoGenerationStatusParams"]


class QueryCheckVideoGenerationStatusParams(TypedDict, total=False):
    task_id: Required[str]
    """Task ID returned from video generation request"""
