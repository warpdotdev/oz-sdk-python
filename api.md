# Agent

Types:

```python
from warp_agent_sdk.types import AmbientAgentConfig, AgentRunResponse
```

Methods:

- <code title="post /agent/run">client.agent.<a href="./src/warp_agent_sdk/resources/agent/agent.py">run</a>(\*\*<a href="src/warp_agent_sdk/types/agent_run_params.py">params</a>) -> <a href="./src/warp_agent_sdk/types/agent_run_response.py">AgentRunResponse</a></code>

## Runs

Types:

```python
from warp_agent_sdk.types.agent import RunItem, RunSourceType, RunState, RunListResponse
```

Methods:

- <code title="get /agent/runs/{runId}">client.agent.runs.<a href="./src/warp_agent_sdk/resources/agent/runs.py">retrieve</a>(run_id) -> <a href="./src/warp_agent_sdk/types/agent/run_item.py">RunItem</a></code>
- <code title="get /agent/runs">client.agent.runs.<a href="./src/warp_agent_sdk/resources/agent/runs.py">list</a>(\*\*<a href="src/warp_agent_sdk/types/agent/run_list_params.py">params</a>) -> <a href="./src/warp_agent_sdk/types/agent/run_list_response.py">RunListResponse</a></code>
