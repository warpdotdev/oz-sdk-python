# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .aws_inference_provider_config import AwsInferenceProviderConfig

__all__ = ["InferenceProvidersConfig"]


class InferenceProvidersConfig(BaseModel):
    """Inference provider settings used for LLM calls."""

    aws: Optional[AwsInferenceProviderConfig] = None
    """Configures AWS Bedrock as the LLM inference provider for this agent or run."""
