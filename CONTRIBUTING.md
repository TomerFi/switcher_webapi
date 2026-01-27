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

[Docker][docker] multi-platform image running a [Python][python] web app. The doc site is built with [MkDocs][mkdocs].

- [app/webapp.py](https://github.com/TomerFi/switcher_webapi/blob/dev/app/webapp.py) the application file
- [app/tests/](https://github.com/TomerFi/switcher_webapi/tree/dev/app/tests) unit tests
- [Dockerfile](https://github.com/TomerFi/switcher_webapi/blob/dev/Dockerfile) image instructions
- [docs](https://github.com/TomerFi/switcher_webapi/tree/dev/docs) sources for the documentation site

The released image is deployed to [Docker Hub][docker_hub].

## Development

### Setup

Create and activate a virtual environment:

```shell
# Unix/Linux/macOS
python -m venv .venv
source .venv/bin/activate

# Windows (Command Prompt)
python -m venv .venv
.venv\Scripts\activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:

```shell
pip install -r requirements.txt -r requirements_test.txt -r requirements_docs.txt
```

### Linting

Run linters using [ruff][ruff]:

```shell
ruff check app/
ruff format --check app/
mypy --ignore-missing-imports app/
```

### Testing

Run tests using [pytest][pytest]:

```shell
# run all tests
pytest -v

# run a specific test
pytest -v -k "test_name_goes_here"

# run tests with coverage
pytest -v --cov --cov-report term-missing
```

### Documentation

Generate and serve the docs site:

```shell
# generate the docs site
mkdocs build

# serve the docs site locally
mkdocs serve
```

<!-- LINKS -->
[docker]: https://www.docker.com/
[docker_hub]: https://hub.docker.com/r/tomerfi/switcher_webapi
[ghcr]: https://github.com/TomerFi/switcher_webapi/pkgs/container/switcher_webapi
[mkdocs]: https://www.mkdocs.org/
[pytest]: https://docs.pytest.org/
[python]: https://www.python.org/
[ruff]: https://docs.astral.sh/ruff/
