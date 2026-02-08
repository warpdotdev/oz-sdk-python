# Agent

Types:

```python
from oz_agent_sdk.types import (
    AgentSkill,
    AmbientAgentConfig,
    CloudEnvironmentConfig,
    McpServerConfig,
    UserProfile,
    AgentListResponse,
    AgentRunResponse,
)
```

Methods:

- <code title="get /agent">client.agent.<a href="./src/oz_agent_sdk/resources/agent/agent.py">list</a>(\*\*<a href="src/oz_agent_sdk/types/agent_list_params.py">params</a>) -> <a href="./src/oz_agent_sdk/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="post /agent/run">client.agent.<a href="./src/oz_agent_sdk/resources/agent/agent.py">run</a>(\*\*<a href="src/oz_agent_sdk/types/agent_run_params.py">params</a>) -> <a href="./src/oz_agent_sdk/types/agent_run_response.py">AgentRunResponse</a></code>

## Runs

Types:

```python
from oz_agent_sdk.types.agent import (
    ArtifactItem,
    RunItem,
    RunSourceType,
    RunState,
    RunListResponse,
    RunCancelResponse,
)
```

Methods:

- <code title="get /agent/runs/{runId}">client.agent.runs.<a href="./src/oz_agent_sdk/resources/agent/runs.py">retrieve</a>(run_id) -> <a href="./src/oz_agent_sdk/types/agent/run_item.py">RunItem</a></code>
- <code title="get /agent/runs">client.agent.runs.<a href="./src/oz_agent_sdk/resources/agent/runs.py">list</a>(\*\*<a href="src/oz_agent_sdk/types/agent/run_list_params.py">params</a>) -> <a href="./src/oz_agent_sdk/types/agent/run_list_response.py">RunListResponse</a></code>
- <code title="post /agent/runs/{runId}/cancel">client.agent.runs.<a href="./src/oz_agent_sdk/resources/agent/runs.py">cancel</a>(run_id) -> str</code>

## Schedules

Types:

```python
from oz_agent_sdk.types.agent import (
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
