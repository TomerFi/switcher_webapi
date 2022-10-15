# Contributing to *switcher_webapi*

:clap: First off, thank you for taking the time to contribute. :clap:

- Fork the repository
- Create a new branch on your fork
- Commit your changes
- Create a pull request against the `dev` branch

## Early-access

An early-access image manifest is deployed to [ghcr.io](https://github.com/TomerFi/switcher_webapi/pkgs/container/switcher_webapi)
for every merge to the default branch, `dev`:

```shell
docker run -d -p 8000:8000 --name switcher_webapi ghcr.io/tomerfi/switcher_webapi:early-access
```

> Note: *ghcr.io* requires *GitHub* login.

## Project walk through

A [Python](https://www.python.org/) WebApp running inside a container,<br/>
the documentation site is built with [MkDocs](https://www.mkdocs.org/).

- [app/webapp.py](https://github.com/TomerFi/switcher_webapi/blob/dev/app/webapp.py) the application file
- [app/tests/](https://github.com/TomerFi/switcher_webapi/tree/dev/app/tests) unit tests
- [Dockerfile](https://github.com/TomerFi/switcher_webapi/blob/dev/Dockerfile) image instructions
- [docs](https://github.com/TomerFi/switcher_webapi/tree/dev/docs) sources for the documentation site

The released image is deployed to [Docker Hub](https://hub.docker.com/r/tomerfi/switcher_webapi).

> Note: *Docker Hub* requires login.

## Prepare the environment

With [Python >= 3.10](https://www.python.org/) use [pip](https://pypi.org/project/pip/) to install
[tox](https://tox.readthedocs.io/):

```shell
pip install tox
```

## Build commands

- `tox` will execute linting jobs and run python's test cases
- `tox -e docs` will test and build the documentation site
- `make` will use `docker buildx` to build the multi-platform image

> Note that if you haven't done so before, you need to create your own local custom build profile.

## Code development

Activate the development virtual environment (after running `tox`):

```shell
source .tox/dev/bin/activate
```

Deactivate with:

```shell
deactivate
```

For dependency updates, update the virtual environment:

```shell
tox -r
```

Once inside the virtual environment, you can the various linters:

```shell
black --check app/
flake8 --count --statistics app/
isort --check-only app/
mypy --ignore-missing-imports app/
yamllint --format colored --strict .
```

And run the tests:

```shell
pytest -v --cov --cov-report term
```

## Docs development

Activate the development virtual environment (after running `tox -e docs`):

```shell
source .tox/docs/bin/activate
```

Deactivate with:

```shell
deactivate
```

For dependency updates, update the virtual environment:

```shell
tox -e docs -r
```

Once inside the virtual environment, you can build the documentation site:

```shell
mkdocs build
```

Or even serve it locally while watching the sources and reloading for modifications:

```shell
mkdocs serve
```

## Extra linters

For CI purposes, we use two more linters outside the scope of *Python*.

If use use [npm](https://www.npmjs.com/), you can lint the *Dockerfile*:

```shell
make dockerfile-lint
```

If you use [deno](https://deno.land/#installation), you can verify license headers on sources:

```shell
make verify-license-headers
```
