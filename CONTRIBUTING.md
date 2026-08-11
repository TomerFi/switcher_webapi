# Contributing to *switcher_webapi*

:clap: First off, thank you for taking the time to contribute. :clap:

- Fork the repository
- Create a new branch on your fork
- Commit your changes
- Create a pull request against the `dev` branch

## Early-access

Early-access image deployed to [GitHub container registry][ghcr]:

```shell
docker run -d -p 8000:8000 --name switcher_webapi ghcr.io/tomerfi/switcher_webapi:early-access
```

## Project

[Docker][docker] multi-platform image running a [Python][python] web app. Supported platforms: amd64, arm/v7, arm64/v8.

When building locally, build for all three platforms.

## AI Policy

This project has a clear AI policy — read [AI_POLICY.md](AI_POLICY.md) and follow it. You're responsible for everything you submit.

The doc site is built with [MkDocs][mkdocs].

- [app/webapp.py](https://github.com/TomerFi/switcher_webapi/blob/dev/app/webapp.py) the application file
- [app/tests/](https://github.com/TomerFi/switcher_webapi/tree/dev/app/tests) unit tests
- [Dockerfile](https://github.com/TomerFi/switcher_webapi/blob/dev/Dockerfile) image instructions
- [docs](https://github.com/TomerFi/switcher_webapi/tree/dev/docs) sources for the documentation site

The released image is deployed to [Docker Hub][docker_hub].

## Development

### Setup

Install [uv](https://docs.astral.sh/uv/), then:

```shell
uv sync --no-install-project --group dev --group docs
```

### Linting

Run linters using [ruff][ruff]:

```shell
uv run ruff check .
uv run ruff format --check .
uv run mypy app/
```

### Testing

Run tests using [pytest][pytest]:

```shell
# run all tests
uv run pytest -v

# run a specific test
uv run pytest -v -k "test_name_goes_here"

# run tests with coverage
uv run pytest -v --cov --cov-report term-missing
```

### Documentation

Generate and serve the docs site:

```shell
# generate the docs site
uv run mkdocs build

# serve the docs site locally
uv run mkdocs serve
```

### Cursor IDE

If using [Cursor][cursor], agents and commands are available in `.cursor/`:

**Agents:**

- `code-reviewer` - Reviews code before committing
- `test-writer` - Writes tests using pytest-asyncio
- `docs-writer` - Updates documentation
- `smoke-tester` - Runs E2E smoke tests on the container

**Commands:**

- `/lint` - Run linting checks
- `/test` - Run tests
- `/serve-docs` - Serve docs locally
- `/stop-docs` - Stop docs server
- `/image-build` - Build container image
- `/dockerfile-lint` - Lint Dockerfile with hadolint

<!-- LINKS -->
[cursor]: https://cursor.sh/
[docker]: https://www.docker.com/
[docker_hub]: https://hub.docker.com/r/tomerfi/switcher_webapi
[ghcr]: https://github.com/TomerFi/switcher_webapi/pkgs/container/switcher_webapi
[mkdocs]: https://www.mkdocs.org/
[pytest]: https://docs.pytest.org/
[python]: https://www.python.org/
[ruff]: https://docs.astral.sh/ruff/
