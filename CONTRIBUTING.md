# Contributing to *switcher_webapi*

Thank you for contributing. This guide covers the essentials.

## AI Policy

This project has a clear AI policy — read [AI_POLICY.md](AI_POLICY.md) and follow it. You're responsible for everything you submit.

## Setup

```bash
git clone <repo-url>
cd switcher_webapi
uv sync --no-install-project --group dev --group docs
```

See [AGENTS.md](AGENTS.md) for linting, testing, and build commands.

## How to Add Handlers

1. Define an endpoint path constant at module level in `app/webapp.py`
2. Write the handler — it must be `async def` and return `web.Response`
3. The handler extracts `device_type`, `ip`, `id`, and optional `login_key` from query params
4. Open `SwitcherApi` as an async context manager, call the appropriate aioswitcher method, and return the serialized result
5. Register the route with the matching `@routes.get` / `@routes.post` / `@routes.patch` / `@routes.delete` decorator
6. Add tests — mock aioswitcher and test with the `api_client` fixture

## Local Checks

This project uses [prek](https://github.com/j178/prek) (pre-commit replacement) to run lint and format checks automatically before each commit.

```bash
uv run prek install
```

This installs the Git hook. After that, checks run automatically on every commit. To run them manually against all files:

```bash
uv run prek run --all-files
```

## Commit Style

- Conventional commits: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`
- One logical change per commit

## PR Process

1. Branch from `dev` with a conventional name: `feat/add-endpoint`, `fix/health-check`
2. Commit with a descriptive message
3. Run all checks before submitting: `uv run ruff check --fix && uv run ruff format && uv run ty check && uv run pytest -v --cov`
4. Open PR against `dev` with a clear description of what changed and why
5. Address feedback

