# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RequestUsage"]


class RequestUsage(BaseModel):
    """Resource usage information for the run"""

    compute_cost: Optional[float] = None
    """Cost of compute resources for the run"""

    inference_cost: Optional[float] = None
    """Cost of LLM inference for the run"""
