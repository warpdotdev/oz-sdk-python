# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .aws_provider_config import AwsProviderConfig
from .gcp_provider_config import GcpProviderConfig

__all__ = ["CloudEnvironmentConfig", "GitHubRepo", "Providers"]


class GitHubRepo(BaseModel):
    owner: str
    """GitHub repository owner (user or organization)"""

    repo: str
    """GitHub repository name"""


class Providers(BaseModel):
    """Optional cloud provider configurations for automatic auth"""

    aws: Optional[AwsProviderConfig] = None
    """AWS IAM role assumption settings"""

    gcp: Optional[GcpProviderConfig] = None
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
