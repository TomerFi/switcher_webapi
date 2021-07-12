# Contributing to `switcher_webapi`</br>[![conventional-commits]][0]

:clap: First off, thank you for taking the time to contribute. :clap:

Contributing is pretty straight-forward:

- Fork the repository
- Commit your changes
- Create a pull request against the `dev` branch

## Prepare the environment

With [Python >= 3.9](https://www.python.org/) use [pip](https://pypi.org/project/pip/) to install
[tox](https://tox.readthedocs.io/):

```shell
  pip install tox
```

## Get started

```shell
tox
```

Will execute linting jobs and run python's test cases.

```shell
tox -e docs
```

Will test and build the documentation site.

```shell
Makefile help
```

Will print the various `Makefile` targets for testing and building the `Docker` image:

```shell
usage: make [target]
--------------------
targets:
********
docker-build
docker-build-no-cache
docker-remove-image
docker-run
docker-build-and-run
docker-build-no-cache-and-run
docker-tag-latest
```

> Note that Makefile will try to determine the host's architecture and set the base image accordingly.

## Early-access

An early-access image manifest is deployed to [ghcr.io](https://github.com/TomerFi/switcher_webapi/pkgs/container/switcher_webapi)
for every merge to the default branch, `dev`:

```shell
docker run -d -p 8000:8000 --name switcher_webapi ghcr.io/tomerfi/switcher_webapi:early-access
```

## Code of Conduct

Please check the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

<!-- Real Links -->
[0]: https://conventionalcommits.org
<!-- Badges Links -->
[conventional-commits]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg
