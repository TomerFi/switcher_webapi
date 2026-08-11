# switcher_webapi

An aiohttp web service wrapping [aioswitcher](https://github.com/TomerFi/aioswitcher) for controlling Switcher smart devices via REST API.

## Architecture

### Handler Pattern

All endpoint handlers follow this structure:

1. Extract `device_type`, `ip`, `id`, and optional `login_key` from query params
2. Open `SwitcherApi` async context manager
3. Call the appropriate aioswitcher method
4. Serialize and return the result as JSON

### Constraints

- All handlers must be `async def` and return `web.Response`
- Use `@routes.get` / `@routes.post` / `@routes.patch` / `@routes.delete` decorators
- Endpoint path constants are defined at module level in `app/webapp.py`
- Uncaught exceptions are caught by `error_middleware` and translated into 500 responses; `delete_schedule` is the only handler returning 404

## Python Conventions

- Use uv for dependency management and tool execution
- Type annotations on all function signatures
- PEP 257 docstrings on all public modules, classes, and functions
- All request handlers must be `async`
- Ruff for linting and formatting (not flake8/black/isort)
- Configuration lives in `pyproject.toml`
- Line length: 88 characters

## Testing

- Mock aioswitcher in all tests — never communicate with real devices
- Use `pytest-asyncio` in auto mode (no `@pytest.mark.asyncio` decorators needed)
- Use `pytest-aiohttp` for web client testing via the `api_client` fixture
- Tests live in `app/tests/`
- Minimum 85% coverage (configured in `pyproject.toml`)

## Container Builds

- Multi-platform: amd64, arm/v7, arm64/v8
- Dockerfile must run as a non-root user

### Multi-Platform Builds

Requires QEMU emulation (`/usr/share/qemu/binfmt.d/*` copied to `/etc/binfmt.d/`).

```bash
podman buildx build \
  --build-arg BUILD_DATE=$(date -u +%Y-%m-%dT%H:%M:%SZ) \
  --build-arg VCS_REF=$(git rev-parse --short HEAD) \
  --build-arg VERSION=$(grep '^version' pyproject.toml | head -1 | cut -d'"' -f2) \
  --platform linux/amd64,linux/arm/v7,linux/arm64/v8 \
  -t switcher_webapi:<tag> .
```

## Git Workflow

- Conventional commit format for PR titles (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`)
- Address CodeRabbit and Sourcery review comments before merging

## Code Review

When reviewing changes:
- **Code Quality**: no duplicated code, proper error handling, correct async/await patterns
- **Security**: no exposed secrets, input validation on endpoint parameters
- **Conventions**: ruff linting configured in `pyproject.toml`, tests mock aioswitcher

## AI Policy

This project has an [AI policy](AI_POLICY.md). Always read it and ensure all suggestions, code, and contributions comply. If any behavior seems to conflict with the policy, warn the user and ask for guidance.

## Documentation

**Key Files:**
- `README.md` — user-facing overview and quick start
- `CONTRIBUTING.md` — developer setup, workflow, and IDE configuration
- `docs/` — MkDocs site with endpoint documentation

When to update docs:
- New endpoint added
- Endpoint behavior changed
- Configuration option changed
- Development workflow changed

