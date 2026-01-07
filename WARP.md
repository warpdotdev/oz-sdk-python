# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is the official Python SDK for the Warp API, providing convenient access to the Warp API REST API. The SDK is **generated code** created using [Stainless](https://www.stainless.com/) from an OpenAPI specification. Most files are auto-generated, with exceptions for `src/warp_agent_sdk/lib/` and `examples/` directories which are manually maintained.

## Development Commands

### Setup
```bash
# Bootstrap the development environment (installs uv, Python, and dependencies)
./scripts/bootstrap
```

### Testing
```bash
# Run full test suite (tests with both Pydantic v1 and v2, multiple Python versions)
./scripts/test

# Run specific tests
uv run pytest tests/test_client.py

# Tests require a mock Prism server running on port 4010
# The test script will automatically start one if not running
# To manually start: ./scripts/mock --daemon
```

### Linting and Type Checking
```bash
# Run all linters (ruff, pyright, mypy)
./scripts/lint

# Run with auto-fix
./scripts/lint --fix

# Format code
./scripts/format
```

### Building
```bash
# Build distribution packages (.tar.gz and .whl)
uv build
```

## Code Architecture

### Generated vs Manual Code

**Generated code** (DO NOT manually edit - changes will be overwritten):
- `src/warp_agent_sdk/_client.py` - Main client classes (WarpAPI, AsyncWarpAPI)
- `src/warp_agent_sdk/resources/` - API resource classes
- `src/warp_agent_sdk/types/` - Type definitions and models
- Most utility files in `src/warp_agent_sdk/_utils/`

**Manual code** (safe to edit):
- `src/warp_agent_sdk/lib/` - Custom library code
- `examples/` - Example scripts
- `tests/` - Test files

### Core Components

**Client Architecture**:
- `WarpAPI` (sync) and `AsyncWarpAPI` (async) are the main entry points
- Both inherit from `SyncAPIClient` and `AsyncAPIClient` base classes
- Support for both `httpx` (default) and `aiohttp` (optional) HTTP backends
- API key authentication via `Authorization: Bearer` header
- Default base URL: `https://app.warp.dev/api/v1`

**Resource Structure**:
- Resources are organized hierarchically (e.g., `client.agent.tasks.retrieve()`)
- Each resource has sync/async variants and raw/streaming response wrappers
- Main resource: `AgentResource` with `run()` method and nested `TasksResource`

**Type System**:
- Uses Pydantic models for request/response validation
- TypedDict for nested parameters
- Custom types: `NotGiven`, `Omit` for optional parameters
- Supports both Pydantic v1 and v2

## Environment Variables

- `WARP_API_KEY` - API key for authentication (required)
- `WARP_API_BASE_URL` - Override default base URL
- `WARP_API_LOG` - Enable logging (`info` or `debug`)
- `TEST_API_BASE_URL` - Use custom API endpoint for tests

## Testing Conventions

- Tests use `pytest` with `pytest-asyncio` for async tests
- Both sync and async variants must be tested
- Tests run against a mock Prism server based on OpenAPI spec
- Tests run with both Pydantic v1 and v2 on Python 3.9 and 3.14+
- Use `respx` for mocking HTTP requests in tests

## Development Workflow

1. **Making changes**: 
   - Only edit files in `lib/` and `examples/` directories
   - Other changes should be made to the OpenAPI spec and regenerated

2. **Adding examples**:
   - Create executable Python scripts in `examples/`
   - Use shebang: `#!/usr/bin/env -S uv run python`
   - Make executable: `chmod +x examples/<your-example>.py`

3. **Code quality**:
   - Run `./scripts/format` before committing
   - Ensure `./scripts/lint` passes
   - Run `./scripts/test` to verify changes

## Package Management

- Uses [uv](https://docs.astral.sh/uv/) for fast, reliable dependency management
- `pyproject.toml` defines project metadata and dependencies
- `uv.lock` pins exact versions for reproducibility
- `requirements-dev.lock` exported for pip compatibility
