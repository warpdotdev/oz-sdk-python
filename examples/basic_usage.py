#!/usr/bin/env -S uv run python
"""Basic usage example for the Oz API Python SDK.

Demonstrates how to:
  - Create a client using the WARP_API_KEY environment variable
  - Start an agent run with a simple prompt
  - Print the resulting run_id
"""

import os

from oz_agent_sdk import OzAPI

# The client automatically reads WARP_API_KEY from the environment.
client = OzAPI(
    api_key=os.environ.get("WARP_API_KEY"),
)

response = client.agent.run(
    prompt="Say hello and report back.",
)

print(f"Agent run started — run_id: {response.run_id}")
