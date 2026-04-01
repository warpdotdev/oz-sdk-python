# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["GcpProviderConfig"]


class GcpProviderConfig(BaseModel):
    """GCP Workload Identity Federation settings"""

    project_number: str
    """GCP project number"""

    workload_identity_federation_pool_id: str
    """Workload Identity Federation pool ID"""

    workload_identity_federation_provider_id: str
    """Workload Identity Federation provider ID"""
