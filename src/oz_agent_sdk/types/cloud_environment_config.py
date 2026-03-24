# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CloudEnvironmentConfig", "GitHubRepo", "Providers", "ProvidersAws", "ProvidersGcp"]


class GitHubRepo(BaseModel):
    owner: str
    """GitHub repository owner (user or organization)"""

    repo: str
    """GitHub repository name"""


class ProvidersAws(BaseModel):
    """AWS IAM role assumption settings"""

    role_arn: str
    """AWS IAM role ARN to assume"""


class ProvidersGcp(BaseModel):
    """GCP Workload Identity Federation settings"""

    project_number: str
    """GCP project number"""

    workload_identity_federation_pool_id: str
    """Workload Identity Federation pool ID"""

    workload_identity_federation_provider_id: str
    """Workload Identity Federation provider ID"""


class Providers(BaseModel):
    """Optional cloud provider configurations for automatic auth"""

    aws: Optional[ProvidersAws] = None
    """AWS IAM role assumption settings"""

    gcp: Optional[ProvidersGcp] = None
    """GCP Workload Identity Federation settings"""


class CloudEnvironmentConfig(BaseModel):
    """Configuration for a cloud environment used by scheduled agents"""

    description: Optional[str] = None
    """Optional description of the environment"""

    docker_image: Optional[str] = None
    """Docker image to use (e.g., "ubuntu:latest" or "registry/repo:tag")"""

    github_repos: Optional[List[GitHubRepo]] = None
    """List of GitHub repositories to clone into the environment"""

    name: Optional[str] = None
    """Human-readable name for the environment"""

    providers: Optional[Providers] = None
    """Optional cloud provider configurations for automatic auth"""

    setup_commands: Optional[List[str]] = None
    """Shell commands to run during environment setup"""
