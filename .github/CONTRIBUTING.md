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

Will execute linting jobs and run the python's test cases.

```shell
tox -e docs
```

Will test and build the documentation site.

```shell
Makefile help
```

Will print the various `Makefile` instruction for testing and building the `Docker` image:

```shell
help:  Show this help.
docker-build:  build image from Dockerfile.
docker-build-testing-image:  build image from Dockerfile using a testing tag.
docker-remove-testing-image:  remove the testing image (must be build first).
docker-build-no-cache:  build image from Dockerfile with no caching.
structure-test:  run the container-structure-test tool against the built testing image (must be build first) using the relative container_structure.yml file
docker-build-structure-test:  build the image and test the container structure
docker-build-no-cache-structure-test:  build the image with no caching and test the container structure
docker-full-structure-testing:  build the image with the testing tag and remove after structure test
docker-tag-latest:  add latest tag before pushing the latest version
docker-run:  run the built image as a container (must be built first).
docker-build-and-run:  build image from Dockerfile and run as container.
docker-build-no-cache-and-run:  build image from Dockerfile with no caching and run as container.
```

## Code of Conduct

Please check the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

<!-- Real Links -->
[0]: https://conventionalcommits.org
<!-- Badges Links -->
[conventional-commits]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg
