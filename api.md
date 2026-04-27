# Agent

Types:

```python
from oz_agent_sdk.types import (
    AgentSkill,
    AmbientAgentConfig,
    AwsProviderConfig,
    CloudEnvironment,
    CloudEnvironmentConfig,
    Error,
    ErrorCode,
    GcpProviderConfig,
    McpServerConfig,
    Scope,
    UserProfile,
    AgentListResponse,
    AgentGetArtifactResponse,
    AgentListEnvironmentsResponse,
    AgentRunResponse,
)
```

Methods:

- <code title="get /agent">client.agent.<a href="./src/oz_agent_sdk/resources/agent/agent.py">list</a>(\*\*<a href="src/oz_agent_sdk/types/agent_list_params.py">params</a>) -> <a href="./src/oz_agent_sdk/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="get /agent/artifacts/{artifactUid}">client.agent.<a href="./src/oz_agent_sdk/resources/agent/agent.py">get_artifact</a>(artifact_uid) -> <a href="./src/oz_agent_sdk/types/agent_get_artifact_response.py">AgentGetArtifactResponse</a></code>
- <code title="get /agent/environments">client.agent.<a href="./src/oz_agent_sdk/resources/agent/agent.py">list_environments</a>(\*\*<a href="src/oz_agent_sdk/types/agent_list_environments_params.py">params</a>) -> <a href="./src/oz_agent_sdk/types/agent_list_environments_response.py">AgentListEnvironmentsResponse</a></code>
- <code title="post /agent/runs">client.agent.<a href="./src/oz_agent_sdk/resources/agent/agent.py">run</a>(\*\*<a href="src/oz_agent_sdk/types/agent_run_params.py">params</a>) -> <a href="./src/oz_agent_sdk/types/agent_run_response.py">AgentRunResponse</a></code>

## Runs

Types:

```python
from oz_agent_sdk.types.agent import (
    ArtifactItem,
    RunItem,
    RunSourceType,
    RunState,
    RunCancelResponse,
    RunListHandoffAttachmentsResponse,
)
```

Methods:

- <code title="get /agent/runs/{runId}">client.agent.runs.<a href="./src/oz_agent_sdk/resources/agent/runs.py">retrieve</a>(run_id) -> <a href="./src/oz_agent_sdk/types/agent/run_item.py">RunItem</a></code>
- <code title="get /agent/runs">client.agent.runs.<a href="./src/oz_agent_sdk/resources/agent/runs.py">list</a>(\*\*<a href="src/oz_agent_sdk/types/agent/run_list_params.py">params</a>) -> <a href="./src/oz_agent_sdk/types/agent/run_item.py">SyncRunsCursorPage[RunItem]</a></code>
- <code title="post /agent/runs/{runId}/cancel">client.agent.runs.<a href="./src/oz_agent_sdk/resources/agent/runs.py">cancel</a>(run_id) -> str</code>
- <code title="get /agent/runs/{runId}/handoff/attachments">client.agent.runs.<a href="./src/oz_agent_sdk/resources/agent/runs.py">list_handoff_attachments</a>(run_id) -> <a href="./src/oz_agent_sdk/types/agent/run_list_handoff_attachments_response.py">RunListHandoffAttachmentsResponse</a></code>
- <code title="post /agent/runs/{runId}/followups">client.agent.runs.<a href="./src/oz_agent_sdk/resources/agent/runs.py">submit_followup</a>(run_id, \*\*<a href="src/oz_agent_sdk/types/agent/run_submit_followup_params.py">params</a>) -> object</code>

## Schedules

Types:

```python
from oz_agent_sdk.types.agent import (
    ScheduledAgentHistoryItem,
    ScheduledAgentItem,
    ScheduleListResponse,
    ScheduleDeleteResponse,
)
```

Methods:

- <code title="post /agent/schedules">client.agent.schedules.<a href="./src/oz_agent_sdk/resources/agent/schedules.py">create</a>(\*\*<a href="src/oz_agent_sdk/types/agent/schedule_create_params.py">params</a>) -> <a href="./src/oz_agent_sdk/types/agent/scheduled_agent_item.py">ScheduledAgentItem</a></code>
- <code title="get /agent/schedules/{scheduleId}">client.agent.schedules.<a href="./src/oz_agent_sdk/resources/agent/schedules.py">retrieve</a>(schedule_id) -> <a href="./src/oz_agent_sdk/types/agent/scheduled_agent_item.py">ScheduledAgentItem</a></code>
- <code title="put /agent/schedules/{scheduleId}">client.agent.schedules.<a href="./src/oz_agent_sdk/resources/agent/schedules.py">update</a>(schedule_id, \*\*<a href="src/oz_agent_sdk/types/agent/schedule_update_params.py">params</a>) -> <a href="./src/oz_agent_sdk/types/agent/scheduled_agent_item.py">ScheduledAgentItem</a></code>
- <code title="get /agent/schedules">client.agent.schedules.<a href="./src/oz_agent_sdk/resources/agent/schedules.py">list</a>() -> <a href="./src/oz_agent_sdk/types/agent/schedule_list_response.py">ScheduleListResponse</a></code>
- <code title="delete /agent/schedules/{scheduleId}">client.agent.schedules.<a href="./src/oz_agent_sdk/resources/agent/schedules.py">delete</a>(schedule_id) -> <a href="./src/oz_agent_sdk/types/agent/schedule_delete_response.py">ScheduleDeleteResponse</a></code>
- <code title="post /agent/schedules/{scheduleId}/pause">client.agent.schedules.<a href="./src/oz_agent_sdk/resources/agent/schedules.py">pause</a>(schedule_id) -> <a href="./src/oz_agent_sdk/types/agent/scheduled_agent_item.py">ScheduledAgentItem</a></code>
- <code title="post /agent/schedules/{scheduleId}/resume">client.agent.schedules.<a href="./src/oz_agent_sdk/resources/agent/schedules.py">resume</a>(schedule_id) -> <a href="./src/oz_agent_sdk/types/agent/scheduled_agent_item.py">ScheduledAgentItem</a></code>

## Agent

Types:

```python
from oz_agent_sdk.types.agent import (
    AgentResponse,
    CreateAgentRequest,
    ListAgentIdentitiesResponse,
    UpdateAgentRequest,
)
```

Methods:

- <code title="post /agent/identities">client.agent.agent.<a href="./src/oz_agent_sdk/resources/agent/agent_.py">create</a>(\*\*<a href="src/oz_agent_sdk/types/agent/agent_create_params.py">params</a>) -> <a href="./src/oz_agent_sdk/types/agent/agent_response.py">AgentResponse</a></code>
- <code title="put /agent/identities/{uid}">client.agent.agent.<a href="./src/oz_agent_sdk/resources/agent/agent_.py">update</a>(uid, \*\*<a href="src/oz_agent_sdk/types/agent/agent_update_params.py">params</a>) -> <a href="./src/oz_agent_sdk/types/agent/agent_response.py">AgentResponse</a></code>
- <code title="get /agent/identities">client.agent.agent.<a href="./src/oz_agent_sdk/resources/agent/agent_.py">list</a>() -> <a href="./src/oz_agent_sdk/types/agent/list_agent_identities_response.py">ListAgentIdentitiesResponse</a></code>
- <code title="delete /agent/identities/{uid}">client.agent.agent.<a href="./src/oz_agent_sdk/resources/agent/agent_.py">delete</a>(uid) -> None</code>

## Sessions

Types:

```python
from oz_agent_sdk.types.agent import SessionCheckRedirectResponse
```

Methods:

- <code title="get /agent/sessions/{sessionUuid}/redirect">client.agent.sessions.<a href="./src/oz_agent_sdk/resources/agent/sessions.py">check_redirect</a>(session_uuid) -> <a href="./src/oz_agent_sdk/types/agent/session_check_redirect_response.py">SessionCheckRedirectResponse</a></code>
