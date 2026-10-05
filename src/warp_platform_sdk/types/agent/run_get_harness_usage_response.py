# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "RunGetHarnessUsageResponse",
    "Usage",
    "UsageClaudeHarnessUsageEnvelope",
    "UsageClaudeHarnessUsageEnvelopeSnapshot",
    "UsageClaudeHarnessUsageEnvelopeSnapshotCoverage",
    "UsageClaudeHarnessUsageEnvelopeSnapshotPayload",
    "UsageClaudeHarnessUsageEnvelopeSnapshotPayloadAttribution",
    "UsageClaudeHarnessUsageEnvelopeSnapshotPayloadAttributionUsage",
    "UsageClaudeHarnessUsageEnvelopeSnapshotPayloadAttributionUsageCacheCreation",
    "UsageClaudeHarnessUsageEnvelopeSnapshotPayloadToolCalls",
    "UsageClaudeHarnessUsageEnvelopeSnapshotPayloadUsage",
    "UsageClaudeHarnessUsageEnvelopeSnapshotPayloadUsageCacheCreation",
    "UsageCodexHarnessUsageEnvelope",
    "UsageCodexHarnessUsageEnvelopeSnapshot",
    "UsageCodexHarnessUsageEnvelopeSnapshotCoverage",
    "UsageCodexHarnessUsageEnvelopeSnapshotPayload",
    "UsageCodexHarnessUsageEnvelopeSnapshotPayloadAttribution",
    "UsageCodexHarnessUsageEnvelopeSnapshotPayloadAttributionUsage",
    "UsageCodexHarnessUsageEnvelopeSnapshotPayloadToolCalls",
    "UsageCodexHarnessUsageEnvelopeSnapshotPayloadUsage",
]


class UsageClaudeHarnessUsageEnvelopeSnapshotCoverage(BaseModel):
    token_status: Literal["known", "partial", "unavailable"] = FieldInfo(alias="tokenStatus")

    tool_status: Literal["known", "partial", "unavailable"] = FieldInfo(alias="toolStatus")


class UsageClaudeHarnessUsageEnvelopeSnapshotPayloadAttributionUsageCacheCreation(BaseModel):
    ephemeral_1h_input_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    ephemeral_5m_input_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""


class UsageClaudeHarnessUsageEnvelopeSnapshotPayloadAttributionUsage(BaseModel):
    """
    Native cumulative token categories; cache counters are not added to input_tokens.
    """

    cache_creation: Optional[UsageClaudeHarnessUsageEnvelopeSnapshotPayloadAttributionUsageCacheCreation] = None

    cache_creation_input_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    cache_read_input_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    input_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    output_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""


class UsageClaudeHarnessUsageEnvelopeSnapshotPayloadAttribution(BaseModel):
    usage: Optional[UsageClaudeHarnessUsageEnvelopeSnapshotPayloadAttributionUsage] = None
    """
    Native cumulative token categories; cache counters are not added to
    input_tokens.
    """

    inference_geo: Optional[str] = None

    model: Optional[str] = None

    service_tier: Optional[str] = None

    speed: Optional[str] = None


class UsageClaudeHarnessUsageEnvelopeSnapshotPayloadToolCalls(BaseModel):
    """Native tool invocation counts.

    Total must equal the sum of byName; tool names are arbitrary map keys.
    """

    by_name: Dict[str, int] = FieldInfo(alias="byName")

    total: int


class UsageClaudeHarnessUsageEnvelopeSnapshotPayloadUsageCacheCreation(BaseModel):
    ephemeral_1h_input_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    ephemeral_5m_input_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""


class UsageClaudeHarnessUsageEnvelopeSnapshotPayloadUsage(BaseModel):
    """
    Native cumulative token categories; cache counters are not added to input_tokens.
    """

    cache_creation: Optional[UsageClaudeHarnessUsageEnvelopeSnapshotPayloadUsageCacheCreation] = None

    cache_creation_input_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    cache_read_input_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    input_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    output_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""


class UsageClaudeHarnessUsageEnvelopeSnapshotPayload(BaseModel):
    attribution: Optional[List[UsageClaudeHarnessUsageEnvelopeSnapshotPayloadAttribution]] = None

    tool_calls: Optional[UsageClaudeHarnessUsageEnvelopeSnapshotPayloadToolCalls] = FieldInfo(
        alias="toolCalls", default=None
    )
    """Native tool invocation counts.

    Total must equal the sum of byName; tool names are arbitrary map keys.
    """

    usage: Optional[UsageClaudeHarnessUsageEnvelopeSnapshotPayloadUsage] = None
    """
    Native cumulative token categories; cache counters are not added to
    input_tokens.
    """


class UsageClaudeHarnessUsageEnvelopeSnapshot(BaseModel):
    coverage: UsageClaudeHarnessUsageEnvelopeSnapshotCoverage

    payload: UsageClaudeHarnessUsageEnvelopeSnapshotPayload


class UsageClaudeHarnessUsageEnvelope(BaseModel):
    captured_at: datetime = FieldInfo(alias="capturedAt")

    capture_sequence: int = FieldInfo(alias="captureSequence")

    execution_id: int = FieldInfo(alias="executionId")

    harness: Literal["CLAUDE_CODE"]

    metrics_version: Literal[1] = FieldInfo(alias="metricsVersion")
    """Server-owned storage format metadata, not the producer's parser version."""

    snapshot: UsageClaudeHarnessUsageEnvelopeSnapshot


class UsageCodexHarnessUsageEnvelopeSnapshotCoverage(BaseModel):
    token_status: Literal["known", "partial", "unavailable"] = FieldInfo(alias="tokenStatus")

    tool_status: Literal["known", "partial", "unavailable"] = FieldInfo(alias="toolStatus")


class UsageCodexHarnessUsageEnvelopeSnapshotPayloadAttributionUsage(BaseModel):
    """Native checkpoint counters.

    Cached input and reasoning output may overlap other categories; no derived total is inferred.
    """

    cache_write_input_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    cached_input_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    input_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    output_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    reasoning_output_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    total_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""


class UsageCodexHarnessUsageEnvelopeSnapshotPayloadAttribution(BaseModel):
    usage: Optional[UsageCodexHarnessUsageEnvelopeSnapshotPayloadAttributionUsage] = None
    """Native checkpoint counters.

    Cached input and reasoning output may overlap other categories; no derived total
    is inferred.
    """

    inference_geo: Optional[str] = None

    model: Optional[str] = None

    service_tier: Optional[str] = None

    speed: Optional[str] = None


class UsageCodexHarnessUsageEnvelopeSnapshotPayloadToolCalls(BaseModel):
    """Native tool invocation counts.

    Total must equal the sum of byName; tool names are arbitrary map keys.
    """

    by_name: Dict[str, int] = FieldInfo(alias="byName")

    total: int


class UsageCodexHarnessUsageEnvelopeSnapshotPayloadUsage(BaseModel):
    """Native checkpoint counters.

    Cached input and reasoning output may overlap other categories; no derived total is inferred.
    """

    cache_write_input_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    cached_input_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    input_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    output_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    reasoning_output_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""

    total_tokens: Optional[int] = None
    """A native count. Absent or null means unmeasured, not zero."""


class UsageCodexHarnessUsageEnvelopeSnapshotPayload(BaseModel):
    attribution: Optional[List[UsageCodexHarnessUsageEnvelopeSnapshotPayloadAttribution]] = None

    tool_calls: Optional[UsageCodexHarnessUsageEnvelopeSnapshotPayloadToolCalls] = FieldInfo(
        alias="toolCalls", default=None
    )
    """Native tool invocation counts.

    Total must equal the sum of byName; tool names are arbitrary map keys.
    """

    usage: Optional[UsageCodexHarnessUsageEnvelopeSnapshotPayloadUsage] = None
    """Native checkpoint counters.

    Cached input and reasoning output may overlap other categories; no derived total
    is inferred.
    """


class UsageCodexHarnessUsageEnvelopeSnapshot(BaseModel):
    coverage: UsageCodexHarnessUsageEnvelopeSnapshotCoverage

    payload: UsageCodexHarnessUsageEnvelopeSnapshotPayload


class UsageCodexHarnessUsageEnvelope(BaseModel):
    captured_at: datetime = FieldInfo(alias="capturedAt")

    capture_sequence: int = FieldInfo(alias="captureSequence")

    execution_id: int = FieldInfo(alias="executionId")

    harness: Literal["CODEX"]

    metrics_version: Literal[1] = FieldInfo(alias="metricsVersion")
    """Server-owned storage format metadata, not the producer's parser version."""

    snapshot: UsageCodexHarnessUsageEnvelopeSnapshot


Usage: TypeAlias = Annotated[
    Union[UsageClaudeHarnessUsageEnvelope, UsageCodexHarnessUsageEnvelope], PropertyInfo(discriminator="harness")
]


class RunGetHarnessUsageResponse(BaseModel):
    available: bool

    conversation_id: str

    run_id: str

    age_seconds: Optional[int] = None

    usage: Optional[Usage] = None
