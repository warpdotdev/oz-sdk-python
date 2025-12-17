# Agent

Types:

```python
from warp_agent_sdk.types import AmbientAgentConfig, AgentRunResponse
```

Methods:

- <code title="post /agent/run">client.agent.<a href="./src/warp_agent_sdk/resources/agent/agent.py">run</a>(\*\*<a href="src/warp_agent_sdk/types/agent_run_params.py">params</a>) -> <a href="./src/warp_agent_sdk/types/agent_run_response.py">AgentRunResponse</a></code>

## Tasks

Types:

```python
from warp_agent_sdk.types.agent import TaskItem, TaskSourceType, TaskState, TaskListResponse
```

Methods:

- <code title="get /agent/tasks/{taskId}">client.agent.tasks.<a href="./src/warp_agent_sdk/resources/agent/tasks.py">retrieve</a>(task_id) -> <a href="./src/warp_agent_sdk/types/agent/task_item.py">TaskItem</a></code>
- <code title="get /agent/tasks">client.agent.tasks.<a href="./src/warp_agent_sdk/resources/agent/tasks.py">list</a>(\*\*<a href="src/warp_agent_sdk/types/agent/task_list_params.py">params</a>) -> <a href="./src/warp_agent_sdk/types/agent/task_list_response.py">TaskListResponse</a></code>
