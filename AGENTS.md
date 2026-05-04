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
- Endpoint path constants defined at module level in `app/webapp.py`
- Error handling must return appropriate HTTP status codes (400, 404, 500)

## Python Conventions

- Use venv (`.venv/bin/` binaries for tooling)
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

## Git Workflow

- Conventional commit format for PR titles (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`)
- Address CodeRabbit and Sourcery review comments before merging

## Code Review

When reviewing changes:
- **Code Quality**: no duplicated code, proper error handling, correct async/await patterns
- **Security**: no exposed secrets, input validation on endpoint parameters
- **Conventions**: ruff linting configured in `pyproject.toml`, tests mock aioswitcher

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

