# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AwsInferenceProviderConfig"]


class AwsInferenceProviderConfig(BaseModel):
    """
    Configures AWS Bedrock as the LLM inference provider for this
    agent or run.
    """

    disabled: Optional[bool] = None
    """If true, opt out of Bedrock at this layer."""

    region: Optional[str] = None
    """AWS region used for STS when assuming the Bedrock inference role."""

    role_arn: Optional[str] = None
    """IAM role ARN to assume when calling Bedrock."""
