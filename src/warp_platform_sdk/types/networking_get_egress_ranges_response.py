# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["NetworkingGetEgressRangesResponse"]


class NetworkingGetEgressRangesResponse(BaseModel):
    cidrs: List[str]
    """Canonical, deduplicated IPv4 and IPv6 network ranges."""
