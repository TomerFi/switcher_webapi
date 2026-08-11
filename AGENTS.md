# Switcher WebAPI AGENTS.md

## AI Policy

This project has an [AI policy](AI_POLICY.md). Always read it and ensure all suggestions, code, and contributions comply. If any behavior seems to conflict with the policy, warn the user and ask for guidance.

## Project Overview

Switcher WebAPI is an aiohttp web service wrapping [aioswitcher](https://github.com/TomerFi/aioswitcher) for controlling [Switcher](http://switcher.co.il/) smart devices via REST API.

### Architecture

#### Handler Pattern

All endpoint handlers follow this structure:

1. Extract `device_type`, `ip`, `id`, and optional `login_key` from query params
2. Open `SwitcherApi` async context manager
3. Call the appropriate aioswitcher method
4. Serialize and return the result as JSON

#### Constraints

- All handlers must be `async def` and return `web.Response`
- Use `@routes.get` / `@routes.post` / `@routes.patch` / `@routes.delete` decorators
- Endpoint path constants are defined at module level in `app/webapp.py`
- Uncaught exceptions are caught by `error_middleware` and translated into 500 responses; `delete_schedule` is the only handler returning 404

## Working Environment

- Use **`uv`** for everything — package management, virtual envs, running commands. Never use `pip` or `venv` directly.
- **`pyproject.toml`** is the single source of truth for dependencies, build config, and tool settings.
- This project uses [**prek**](https://github.com/j178/prek) (pre-commit replacement). Install the hook with `uv run prek install`.
- Type annotations on all function signatures
- PEP 257 docstrings on all public modules, classes, and functions
- All request handlers must be `async`

## Linting

```bash
uv run ruff check
uv run ruff format --check
uv run ty check
```

## Testing

```bash
# run all tests
uv run pytest -v

# run a specific test
uv run pytest -v -k "test_name_goes_here"

# run tests with coverage
uv run pytest -v --cov --cov-report term-missing
```

### Adding Tests

- Mock aioswitcher in all tests — never communicate with real devices
- Use `pytest-asyncio` in auto mode (no `@pytest.mark.asyncio` decorators needed)
- Use `pytest-aiohttp` for web client testing via the `api_client` fixture
- Tests live in `app/tests/`
- Minimum 85% coverage (configured in `pyproject.toml`)

## Multi-Platform Builds

Multi-platform: amd64, arm/v7, arm64/v8.

```bash
podman buildx build \
  --build-arg BUILD_DATE=$(date -u +%Y-%m-%dT%H:%M:%SZ) \
  --build-arg VCS_REF=$(git rev-parse --short HEAD) \
  --build-arg VERSION=$(grep '^version' pyproject.toml | head -1 | cut -d'"' -f2) \
  --platform linux/amd64,linux/arm/v7,linux/arm64/v8 \
  -t switcher_webapi:<tag> .
```

## Documentation

**Key Files:**
- `README.md` — user-facing overview and quick start
- `CONTRIBUTING.md` — developer setup, workflow, IDE configuration, and commands
- `docs/` — MkDocs site with endpoint documentation

When to update docs:
- New endpoint added
- Endpoint behavior changed
- Configuration option changed
- Development workflow changed
