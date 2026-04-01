# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AwsProviderConfig"]


class AwsProviderConfig(BaseModel):
    """AWS IAM role assumption settings"""

    role_arn: str
    """AWS IAM role ARN to assume"""
