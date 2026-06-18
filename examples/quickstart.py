#!/usr/bin/env -S uv run python
"""
Quickstart example for the Oz Agent SDK.

Demonstrates the minimal setup needed to run an agent task and poll
for results using the OzAPI client.

Usage:
    WARP_API_KEY=your_key ./examples/quickstart.py
"""

import os

from oz_agent_sdk import OzAPI

client = OzAPI(
    api_key=os.environ.get("WARP_API_KEY"),  # defaults to WARP_API_KEY env var
)

# Run an agent with a simple prompt
response = client.agent.run(
    prompt="List the files in the current directory.",
)

print(f"Agent run started — run_id: {response.run_id}")
