#!/usr/bin/env python3
"""
Warp Agent CLI - A demo application using the Warp Python SDK.

This CLI allows you to:
- Run agent tasks with custom prompts
- Check the status of running tasks
- List recent tasks
"""

import argparse
import os
import sys
import time
from datetime import datetime

from warp_agent_sdk import WarpAPI
from warp_agent_sdk.types.agent import TaskState


def create_client() -> WarpAPI:
    """Create and return a Warp API client."""
    api_key = os.environ.get("WARP_API_KEY")
    if not api_key:
        print("Error: WARP_API_KEY environment variable is not set.")
        print("Please set it with: export WARP_API_KEY='your-api-key'")
        sys.exit(1)
    return WarpAPI(api_key=api_key)


def format_timestamp(dt: datetime) -> str:
    """Format a datetime object for display."""
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def format_state(state: TaskState) -> str:
    """Format task state with color indicators."""
    state_icons = {
        "QUEUED": "⏳",
        "PENDING": "🔄",
        "CLAIMED": "🔒",
        "INPROGRESS": "▶️",
        "SUCCEEDED": "✅",
        "FAILED": "❌",
    }
    return f"{state_icons.get(state, '❓')} {state}"


def run_task(args: argparse.Namespace) -> None:
    """Run a new agent task."""
    client = create_client()
    
    print(f"🚀 Submitting task: {args.prompt}")
    print("-" * 50)
    
    config = {}
    if args.model:
        config["model_id"] = args.model
    if args.environment:
        config["environment_id"] = args.environment
    if args.base_prompt:
        config["base_prompt"] = args.base_prompt
    
    response = client.agent.run(
        prompt=args.prompt,
        config=config if config else None,
    )
    
    print(f"Task ID: {response.task_id}")
    print(f"State: {format_state(response.state)}")
    
    if args.wait:
        print("\n⏳ Waiting for task to complete...")
        wait_for_task(client, response.task_id)


def wait_for_task(client: WarpAPI, task_id: str) -> None:
    """Poll task status until completion."""
    terminal_states = {"SUCCEEDED", "FAILED"}
    
    while True:
        task = client.agent.tasks.retrieve(task_id)
        print(f"  Status: {format_state(task.state)}", end="\r")
        
        if task.state in terminal_states:
            print()  # New line after status
            print("-" * 50)
            print(f"Task completed with state: {format_state(task.state)}")
            if task.session_link:
                print(f"Session link: {task.session_link}")
            if task.status_message and task.status_message.message:
                print(f"Message: {task.status_message.message}")
            break
        
        time.sleep(2)


def get_task(args: argparse.Namespace) -> None:
    """Get details of a specific task."""
    client = create_client()
    
    print(f"🔍 Fetching task: {args.task_id}")
    print("-" * 50)
    
    task = client.agent.tasks.retrieve(args.task_id)
    
    print(f"Task ID:    {task.task_id}")
    print(f"Title:      {task.title}")
    print(f"State:      {format_state(task.state)}")
    print(f"Created:    {format_timestamp(task.created_at)}")
    print(f"Updated:    {format_timestamp(task.updated_at)}")
    print(f"Prompt:     {task.prompt[:100]}{'...' if len(task.prompt) > 100 else ''}")
    
    if task.source:
        print(f"Source:     {task.source}")
    if task.session_link:
        print(f"Session:    {task.session_link}")
    if task.status_message and task.status_message.message:
        print(f"Message:    {task.status_message.message}")


def list_tasks(args: argparse.Namespace) -> None:
    """List recent tasks."""
    client = create_client()
    
    print("📋 Listing recent tasks")
    print("-" * 80)
    
    params = {}
    if args.limit:
        params["limit"] = args.limit
    if args.state:
        params["state"] = args.state
    
    response = client.agent.tasks.list(**params)
    
    if not response.items:
        print("No tasks found.")
        return
    
    # Print header
    print(f"{'ID':<36} {'State':<15} {'Title':<30}")
    print("-" * 80)
    
    for task in response.items:
        title = task.title[:28] + ".." if len(task.title) > 30 else task.title
        print(f"{task.task_id:<36} {format_state(task.state):<15} {title:<30}")
    
    print("-" * 80)
    print(f"Total: {len(response.items)} tasks")


def main() -> None:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Warp Agent CLI - Interact with the Warp API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s run "Fix the bug in auth.go"
  %(prog)s run "Write tests for utils.py" --wait
  %(prog)s run "Refactor the database module" --model claude-sonnet-4
  %(prog)s get abc123-task-id
  %(prog)s list --limit 10
  %(prog)s list --state INPROGRESS
        """,
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Run command
    run_parser = subparsers.add_parser("run", help="Run a new agent task")
    run_parser.add_argument("prompt", help="The task prompt/instruction for the agent")
    run_parser.add_argument(
        "--wait", "-w",
        action="store_true",
        help="Wait for the task to complete",
    )
    run_parser.add_argument(
        "--model", "-m",
        help="LLM model to use (e.g., claude-sonnet-4)",
    )
    run_parser.add_argument(
        "--environment", "-e",
        help="Environment ID to run the agent in",
    )
    run_parser.add_argument(
        "--base-prompt", "-b",
        help="Custom base prompt for the agent",
    )
    run_parser.set_defaults(func=run_task)
    
    # Get command
    get_parser = subparsers.add_parser("get", help="Get details of a specific task")
    get_parser.add_argument("task_id", help="The task ID to retrieve")
    get_parser.set_defaults(func=get_task)
    
    # List command
    list_parser = subparsers.add_parser("list", help="List recent tasks")
    list_parser.add_argument(
        "--limit", "-l",
        type=int,
        default=10,
        help="Maximum number of tasks to return (default: 10)",
    )
    list_parser.add_argument(
        "--state", "-s",
        choices=["QUEUED", "PENDING", "CLAIMED", "INPROGRESS", "SUCCEEDED", "FAILED"],
        help="Filter tasks by state",
    )
    list_parser.set_defaults(func=list_tasks)
    
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        sys.exit(1)
    
    try:
        args.func(args)
    except KeyboardInterrupt:
        print("\n\nOperation cancelled.")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
