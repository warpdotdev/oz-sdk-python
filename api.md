# Agent

Types:

```python
from warp_platform_sdk.types import (
    AgentConfigSnapshot,
    AgentSkill,
    AwsInferenceProviderConfig,
    AwsProviderConfig,
    Environment,
    EnvironmentConfig,
    Error,
    ErrorCode,
    GcpProviderConfig,
    Harness,
    HarnessAuthSecrets,
    InferenceProvidersConfig,
    McpServerConfig,
    MemoryStoreRef,
    Scope,
    SecretRef,
    SessionSharingConfig,
    UserProfile,
    AgentListResponse,
    AgentGetArtifactResponse,
    AgentGetRunByExternalReferenceResponse,
    AgentListEnvironmentsResponse,
    AgentListModelsResponse,
    AgentRunResponse,
)
```

Methods:

- <code title="get /agent">client.agent.<a href="./src/warp_platform_sdk/resources/agent/agent.py">list</a>(\*\*<a href="src/warp_platform_sdk/types/agent_list_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="get /agent/artifacts/{artifactUid}/download">client.agent.<a href="./src/warp_platform_sdk/resources/agent/agent.py">download_artifact</a>(artifact_uid) -> BinaryAPIResponse</code>
- <code title="get /agent/artifacts/{artifactUid}">client.agent.<a href="./src/warp_platform_sdk/resources/agent/agent.py">get_artifact</a>(artifact_uid) -> <a href="./src/warp_platform_sdk/types/agent_get_artifact_response.py">AgentGetArtifactResponse</a></code>
- <code title="get /agent/run-by-external-reference">client.agent.<a href="./src/warp_platform_sdk/resources/agent/agent.py">get_run_by_external_reference</a>(\*\*<a href="src/warp_platform_sdk/types/agent_get_run_by_external_reference_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/agent_get_run_by_external_reference_response.py">AgentGetRunByExternalReferenceResponse</a></code>
- <code title="get /agent/environments">client.agent.<a href="./src/warp_platform_sdk/resources/agent/agent.py">list_environments</a>(\*\*<a href="src/warp_platform_sdk/types/agent_list_environments_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/agent_list_environments_response.py">AgentListEnvironmentsResponse</a></code>
- <code title="get /agent/models">client.agent.<a href="./src/warp_platform_sdk/resources/agent/agent.py">list_models</a>() -> <a href="./src/warp_platform_sdk/types/agent_list_models_response.py">AgentListModelsResponse</a></code>
- <code title="post /agent/runs">client.agent.<a href="./src/warp_platform_sdk/resources/agent/agent.py">run</a>(\*\*<a href="src/warp_platform_sdk/types/agent_run_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/agent_run_response.py">AgentRunResponse</a></code>

## Runs

Types:

```python
from warp_platform_sdk.types.agent import (
    ArtifactItem,
    ConversationStep,
    RunItem,
    RunSourceType,
    RunState,
    RunCancelResponse,
    RunGetConversationResponse,
    RunGetHarnessUsageResponse,
    RunGetTimelineResponse,
    RunListHandoffAttachmentsResponse,
    RunSubmitFollowupResponse,
)
```

Methods:

- <code title="get /agent/runs/{runId}">client.agent.runs.<a href="./src/warp_platform_sdk/resources/agent/runs.py">retrieve</a>(run_id) -> <a href="./src/warp_platform_sdk/types/agent/run_item.py">RunItem</a></code>
- <code title="get /agent/runs">client.agent.runs.<a href="./src/warp_platform_sdk/resources/agent/runs.py">list</a>(\*\*<a href="src/warp_platform_sdk/types/agent/run_list_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/agent/run_item.py">SyncRunsCursorPage[RunItem]</a></code>
- <code title="post /agent/runs/{runId}/cancel">client.agent.runs.<a href="./src/warp_platform_sdk/resources/agent/runs.py">cancel</a>(run_id) -> str</code>
- <code title="get /agent/runs/{runId}/conversation">client.agent.runs.<a href="./src/warp_platform_sdk/resources/agent/runs.py">get_conversation</a>(run_id) -> <a href="./src/warp_platform_sdk/types/agent/run_get_conversation_response.py">RunGetConversationResponse</a></code>
- <code title="get /agent/runs/{runId}/harness-usage">client.agent.runs.<a href="./src/warp_platform_sdk/resources/agent/runs.py">get_harness_usage</a>(run_id) -> <a href="./src/warp_platform_sdk/types/agent/run_get_harness_usage_response.py">RunGetHarnessUsageResponse</a></code>
- <code title="get /agent/runs/{runId}/timeline">client.agent.runs.<a href="./src/warp_platform_sdk/resources/agent/runs.py">get_timeline</a>(run_id) -> <a href="./src/warp_platform_sdk/types/agent/run_get_timeline_response.py">RunGetTimelineResponse</a></code>
- <code title="get /agent/runs/{runId}/transcript">client.agent.runs.<a href="./src/warp_platform_sdk/resources/agent/runs.py">get_transcript</a>(run_id) -> BinaryAPIResponse</code>
- <code title="post /agent/runs/{runId}/interrupt">client.agent.runs.<a href="./src/warp_platform_sdk/resources/agent/runs.py">interrupt</a>(run_id) -> object</code>
- <code title="get /agent/runs/{runId}/handoff/attachments">client.agent.runs.<a href="./src/warp_platform_sdk/resources/agent/runs.py">list_handoff_attachments</a>(run_id) -> <a href="./src/warp_platform_sdk/types/agent/run_list_handoff_attachments_response.py">RunListHandoffAttachmentsResponse</a></code>
- <code title="post /agent/runs/{runId}/followups">client.agent.runs.<a href="./src/warp_platform_sdk/resources/agent/runs.py">submit_followup</a>(run_id, \*\*<a href="src/warp_platform_sdk/types/agent/run_submit_followup_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/agent/run_submit_followup_response.py">RunSubmitFollowupResponse</a></code>

## Schedules

Types:

```python
from warp_platform_sdk.types.agent import (
    ScheduledAgentHistoryItem,
    ScheduledAgentItem,
    ScheduleListResponse,
    ScheduleDeleteResponse,
)
```

Methods:

- <code title="post /agent/schedules">client.agent.schedules.<a href="./src/warp_platform_sdk/resources/agent/schedules.py">create</a>(\*\*<a href="src/warp_platform_sdk/types/agent/schedule_create_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/agent/scheduled_agent_item.py">ScheduledAgentItem</a></code>
- <code title="get /agent/schedules/{scheduleId}">client.agent.schedules.<a href="./src/warp_platform_sdk/resources/agent/schedules.py">retrieve</a>(schedule_id) -> <a href="./src/warp_platform_sdk/types/agent/scheduled_agent_item.py">ScheduledAgentItem</a></code>
- <code title="put /agent/schedules/{scheduleId}">client.agent.schedules.<a href="./src/warp_platform_sdk/resources/agent/schedules.py">update</a>(schedule_id, \*\*<a href="src/warp_platform_sdk/types/agent/schedule_update_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/agent/scheduled_agent_item.py">ScheduledAgentItem</a></code>
- <code title="get /agent/schedules">client.agent.schedules.<a href="./src/warp_platform_sdk/resources/agent/schedules.py">list</a>() -> <a href="./src/warp_platform_sdk/types/agent/schedule_list_response.py">ScheduleListResponse</a></code>
- <code title="delete /agent/schedules/{scheduleId}">client.agent.schedules.<a href="./src/warp_platform_sdk/resources/agent/schedules.py">delete</a>(schedule_id) -> <a href="./src/warp_platform_sdk/types/agent/schedule_delete_response.py">ScheduleDeleteResponse</a></code>
- <code title="post /agent/schedules/{scheduleId}/pause">client.agent.schedules.<a href="./src/warp_platform_sdk/resources/agent/schedules.py">pause</a>(schedule_id) -> <a href="./src/warp_platform_sdk/types/agent/scheduled_agent_item.py">ScheduledAgentItem</a></code>
- <code title="post /agent/schedules/{scheduleId}/resume">client.agent.schedules.<a href="./src/warp_platform_sdk/resources/agent/schedules.py">resume</a>(schedule_id) -> <a href="./src/warp_platform_sdk/types/agent/scheduled_agent_item.py">ScheduledAgentItem</a></code>

## Agent

Types:

```python
from warp_platform_sdk.types.agent import (
    AgentResponse,
    AutoMemoryResponse,
    CreateAgentRequest,
    ListAgentIdentitiesResponse,
    MemoryResponse,
    MemoryStoreAttachmentResponse,
    UpdateAgentRequest,
)
```

Methods:

- <code title="post /agent/identities">client.agent.agent.<a href="./src/warp_platform_sdk/resources/agent/agent_.py">create</a>(\*\*<a href="src/warp_platform_sdk/types/agent/agent_create_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/agent/agent_response.py">AgentResponse</a></code>
- <code title="put /agent/identities/{uid}">client.agent.agent.<a href="./src/warp_platform_sdk/resources/agent/agent_.py">update</a>(uid, \*\*<a href="src/warp_platform_sdk/types/agent/agent_update_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/agent/agent_response.py">AgentResponse</a></code>
- <code title="get /agent/identities">client.agent.agent.<a href="./src/warp_platform_sdk/resources/agent/agent_.py">list</a>(\*\*<a href="src/warp_platform_sdk/types/agent/agent_list_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/agent/list_agent_identities_response.py">ListAgentIdentitiesResponse</a></code>
- <code title="delete /agent/identities/{uid}">client.agent.agent.<a href="./src/warp_platform_sdk/resources/agent/agent_.py">delete</a>(uid) -> None</code>
- <code title="get /agent/identities/{uid}">client.agent.agent.<a href="./src/warp_platform_sdk/resources/agent/agent_.py">get</a>(uid) -> <a href="./src/warp_platform_sdk/types/agent/agent_response.py">AgentResponse</a></code>

## Sessions

Types:

```python
from warp_platform_sdk.types.agent import SessionCheckRedirectResponse
```

Methods:

- <code title="get /agent/sessions/{sessionUuid}/redirect">client.agent.sessions.<a href="./src/warp_platform_sdk/resources/agent/sessions.py">check_redirect</a>(session_uuid) -> <a href="./src/warp_platform_sdk/types/agent/session_check_redirect_response.py">SessionCheckRedirectResponse</a></code>

## Conversations

Types:

```python
from warp_platform_sdk.types.agent import (
    ConversationRetrieveResponse,
    ConversationCheckRedirectResponse,
    ConversationInterruptResponse,
    ConversationSubmitFollowupResponse,
)
```

Methods:

- <code title="get /agent/conversations/{conversation_id}">client.agent.conversations.<a href="./src/warp_platform_sdk/resources/agent/conversations.py">retrieve</a>(conversation_id) -> <a href="./src/warp_platform_sdk/types/agent/conversation_retrieve_response.py">ConversationRetrieveResponse</a></code>
- <code title="get /agent/conversations/{conversationId}/redirect">client.agent.conversations.<a href="./src/warp_platform_sdk/resources/agent/conversations.py">check_redirect</a>(conversation_id) -> <a href="./src/warp_platform_sdk/types/agent/conversation_check_redirect_response.py">ConversationCheckRedirectResponse</a></code>
- <code title="get /agent/conversations/{conversation_id}/screenshots/{screenshot_uid}/download">client.agent.conversations.<a href="./src/warp_platform_sdk/resources/agent/conversations.py">download_screenshot</a>(screenshot_uid, \*, conversation_id) -> BinaryAPIResponse</code>
- <code title="get /agent/conversations/{conversation_id}/transcript">client.agent.conversations.<a href="./src/warp_platform_sdk/resources/agent/conversations.py">get_transcript</a>(conversation_id) -> BinaryAPIResponse</code>
- <code title="post /agent/conversations/{conversation_id}/interrupt">client.agent.conversations.<a href="./src/warp_platform_sdk/resources/agent/conversations.py">interrupt</a>(conversation_id) -> <a href="./src/warp_platform_sdk/types/agent/conversation_interrupt_response.py">ConversationInterruptResponse</a></code>
- <code title="post /agent/conversations/{conversation_id}/followups">client.agent.conversations.<a href="./src/warp_platform_sdk/resources/agent/conversations.py">submit_followup</a>(conversation_id, \*\*<a href="src/warp_platform_sdk/types/agent/conversation_submit_followup_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/agent/conversation_submit_followup_response.py">ConversationSubmitFollowupResponse</a></code>

# Networking

Types:

```python
from warp_platform_sdk.types import NetworkingGetEgressRangesResponse
```

Methods:

- <code title="get /networking/egress-ranges">client.networking.<a href="./src/warp_platform_sdk/resources/networking.py">get_egress_ranges</a>() -> <a href="./src/warp_platform_sdk/types/networking_get_egress_ranges_response.py">NetworkingGetEgressRangesResponse</a></code>

# Factories

Types:

```python
from warp_platform_sdk.types import Factory
```

Methods:

- <code title="get /factory">client.factories.<a href="./src/warp_platform_sdk/resources/factories/factories.py">list</a>(\*\*<a href="src/warp_platform_sdk/types/factory_list_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/factory.py">SyncFactoriesCursorPage[Factory]</a></code>
- <code title="get /factory/{uid}">client.factories.<a href="./src/warp_platform_sdk/resources/factories/factories.py">get</a>(uid) -> <a href="./src/warp_platform_sdk/types/factory.py">Factory</a></code>

## Runs

Types:

```python
from warp_platform_sdk.types.factories import RunCreateResponse
```

Methods:

- <code title="post /factory/{uid}/runs">client.factories.runs.<a href="./src/warp_platform_sdk/resources/factories/runs.py">create</a>(uid, \*\*<a href="src/warp_platform_sdk/types/factories/run_create_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/factories/run_create_response.py">RunCreateResponse</a></code>

## Tasks

Types:

```python
from warp_platform_sdk.types.factories import Task
```

Methods:

- <code title="post /factory/{uid}/tasks">client.factories.tasks.<a href="./src/warp_platform_sdk/resources/factories/tasks.py">create</a>(uid, \*\*<a href="src/warp_platform_sdk/types/factories/task_create_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/factories/task.py">Task</a></code>
- <code title="patch /factory/{uid}/tasks/{task_uid}">client.factories.tasks.<a href="./src/warp_platform_sdk/resources/factories/tasks.py">update</a>(task_uid, \*, uid, \*\*<a href="src/warp_platform_sdk/types/factories/task_update_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/factories/task.py">Task</a></code>
- <code title="get /factory/{uid}/tasks">client.factories.tasks.<a href="./src/warp_platform_sdk/resources/factories/tasks.py">list</a>(uid, \*\*<a href="src/warp_platform_sdk/types/factories/task_list_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/factories/task.py">SyncFactoryTasksCursorPage[Task]</a></code>
- <code title="delete /factory/{uid}/tasks/{task_uid}">client.factories.tasks.<a href="./src/warp_platform_sdk/resources/factories/tasks.py">delete</a>(task_uid, \*, uid) -> None</code>
- <code title="post /factory/{uid}/tasks/{task_uid}/cancel">client.factories.tasks.<a href="./src/warp_platform_sdk/resources/factories/tasks.py">cancel</a>(task_uid, \*, uid) -> <a href="./src/warp_platform_sdk/types/factories/task.py">Task</a></code>
- <code title="get /factory/{uid}/tasks/{task_uid}">client.factories.tasks.<a href="./src/warp_platform_sdk/resources/factories/tasks.py">get</a>(task_uid, \*, uid) -> <a href="./src/warp_platform_sdk/types/factories/task.py">Task</a></code>
- <code title="get /factory/{uid}/task-by-conversation">client.factories.tasks.<a href="./src/warp_platform_sdk/resources/factories/tasks.py">get_by_conversation</a>(uid, \*\*<a href="src/warp_platform_sdk/types/factories/task_get_by_conversation_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/factories/task.py">Task</a></code>
- <code title="get /factory/{uid}/task-by-run">client.factories.tasks.<a href="./src/warp_platform_sdk/resources/factories/tasks.py">get_by_run</a>(uid, \*\*<a href="src/warp_platform_sdk/types/factories/task_get_by_run_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/factories/task.py">Task</a></code>

## Files

Types:

```python
from warp_platform_sdk.types.factories import FileValidateResponse
```

Methods:

- <code title="post /factory-files/validate">client.factories.files.<a href="./src/warp_platform_sdk/resources/factories/files/files.py">validate</a>(\*\*<a href="src/warp_platform_sdk/types/factories/file_validate_params.py">params</a>) -> <a href="./src/warp_platform_sdk/types/factories/file_validate_response.py">FileValidateResponse</a></code>

### Schemas

Types:

```python
from warp_platform_sdk.types.factories.files import (
    SchemaRetrieveResponse,
    SchemaListResponse,
    SchemaGetDocumentResponse,
)
```

Methods:

- <code title="get /factory-files/schemas/{schema_version}">client.factories.files.schemas.<a href="./src/warp_platform_sdk/resources/factories/files/schemas.py">retrieve</a>(schema_version) -> <a href="./src/warp_platform_sdk/types/factories/files/schema_retrieve_response.py">SchemaRetrieveResponse</a></code>
- <code title="get /factory-files/schemas">client.factories.files.schemas.<a href="./src/warp_platform_sdk/resources/factories/files/schemas.py">list</a>() -> <a href="./src/warp_platform_sdk/types/factories/files/schema_list_response.py">SchemaListResponse</a></code>
- <code title="get /factory-files/schemas/{schema_version}/{document}">client.factories.files.schemas.<a href="./src/warp_platform_sdk/resources/factories/files/schemas.py">get_document</a>(document, \*, schema_version) -> <a href="./src/warp_platform_sdk/types/factories/files/schema_get_document_response.py">SchemaGetDocumentResponse</a></code>
