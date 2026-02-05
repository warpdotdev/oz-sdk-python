# Warp Agent CLI Demo

A demo CLI application built with the [Warp Python SDK](https://github.com/warpdotdev/warp-sdk-python) that demonstrates how to interact with the Warp Agent API.

## Features

- **Run Tasks**: Submit new agent tasks with custom prompts
- **Monitor Tasks**: Check the status of running tasks with real-time polling
- **List Tasks**: View recent tasks with filtering options

## Installation

```bash
# From the examples directory
pip install warp-agent-sdk
pip install -e .
```

## Configuration

Set your Warp API key as an environment variable:

```bash
export WARP_API_KEY='your-api-key'
```

## Usage

### Run a new task

```bash
# Basic usage
warp-cli run "Fix the bug in auth.go"

# Wait for completion
warp-cli run "Write tests for utils.py" --wait

# Specify a model
warp-cli run "Refactor the database module" --model claude-sonnet-4

# Use a specific environment
warp-cli run "Deploy to staging" --environment your-env-id

# Custom base prompt
warp-cli run "Review this PR" --base-prompt "You are a senior code reviewer."
```

### Get task details

```bash
warp-cli get <task-id>
```

### List recent tasks

```bash
# List last 10 tasks (default)
warp-cli list

# Limit results
warp-cli list --limit 5

# Filter by state
warp-cli list --state INPROGRESS
warp-cli list --state SUCCEEDED
```

## Example Output

```
$ warp-cli run "Fix the bug in auth.go"
🚀 Submitting task: Fix the bug in auth.go
--------------------------------------------------
Task ID: abc123-def456-ghi789
State: ⏳ QUEUED

$ warp-cli list
📋 Listing recent tasks
--------------------------------------------------------------------------------
ID                                   State           Title
--------------------------------------------------------------------------------
abc123-def456-ghi789                 ▶️ INPROGRESS   Fix the bug in auth.go
xyz789-uvw456-rst123                 ✅ SUCCEEDED    Add unit tests
--------------------------------------------------------------------------------
Total: 2 tasks
```

## API Reference

This CLI demonstrates the following SDK capabilities:

- `client.agent.run()` - Run a new agent task
- `client.agent.tasks.retrieve()` - Get details of a specific task
- `client.agent.tasks.list()` - List recent tasks

For more details, see the [Warp SDK documentation](https://github.com/warpdotdev/warp-sdk-python).
