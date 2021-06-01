# Contributing to `switcher_webapi`

:clap: First off, thank you for taking the time to contribute. :clap:

> **Note**: This repository is a docker image wrapping a Python REST API server around the
> `aioswitcher` pypi module.
>
> If your contribution is a more of a *core contribution*,</br>
> Please consider perhaps it belongs to the integrating module and not the wrapping docker.</br>
> You can find the module repository [here](https://github.com/TomerFi/aioswitcher).

Contributing is pretty straight-forward:

- Fork the repository
- Commit your changes
- Create a pull request against the `dev` branch

Please feel free to contribute, even to this contributing guideline file, if you see fit.

- [Documentation](#documentation)
- [Python Code](#python-code)
- [Docker Build](#docker-build)
- [Testing](#testing)
  - [Python Test Framework](#python-test-framework)
  - [Local Testing](#local-testing)
  - [Container Structure Test](#container-structure-test)
- [Code of Conduct](#code-of-conduct)

> **Important Note**: the project's `semver` is set in the [VERSION](../VERSION) file as it is used
> by [setup.py](../setup.py), [Makefile](../Makefile), and [docs/conf.py](../docs/conf.py).

## Documentation

- `docs/sources` is where the *restructuredText* for creating the [Sphinx Documentation](http://www.sphinx-doc.org)
  are stored for build, deployment and hosting by [Read the Docs](https://readthedocs.org/).
- `docs/Makefile` the basic *Makefile* for [Sphinx](http://www.sphinx-doc.org)
  documentation generator. From the [docs](docs/) path, type `make html` and
  [sphinx](http://www.sphinx-doc.org) will create the documentation site locally in
  `docs/build`.

## Python Code

It's basically a web server, start with [switcher_webapi/start_server.py](../switcher_webapi/start_server.py),
and follow the [docs](https://switcher-webapi.tomfi.info). The file names are pretty self explanatory.

## Docker Build

Use the designated [Makefile](../Makefile) [Make](https://www.gnu.org/software/make/manual/make.html) file.

```shell
# display a self explanatory help message.
make help
```

```text
help:  Show this help.
docker-build:  build image from Dockerfile.
docker-build-testing-image:  build image from Dockerfile using a testing tag.
docker-remove-testing-image:  remove the testing image (must be build first).
docker-build-no-cache:  build image from Dockerfile with no caching.
structure-test:  run the container-structure-test tool against the built testing image (must be build first) using the relative container_structure.yml file
docker-build-structure-test:  build the image and test the container structure
docker-build-no-cache-structure-test:  build the image and test the container structure
docker-full-structure-testing:  build the image with the testing tag and remove after structure test
docker-tag-latest:  add latest tag before pushing the latest version
docker-run:  run the built image as a container (must be built first).
docker-build-and-run:  build image from Dockerfile and run as container.
docker-build-no-cache-and-run:  build image from Dockerfile with no caching and run as container.
verify-environment-file:  verify the existence of the required environment variables file.
```

## Testing

### Python Test Framework

Testing is performed with [Pytest, Full-featured Python testing tool](https://docs.pytest.org).</br>
The file [tests/test_server.py](../tests/test_server.py) holds the various test cases for the
web server, the file [tests/conftest.py](../tests/conftest.py) holds the various mocks and
fixtures used to testing.

### Local Testing

For automated local tests, use [Tox](https://tox.readthedocs.io).</br>

### Container Structure Test

The container content is validated with
[container-structure-test](https://github.com/GoogleContainerTools/container-structure-test),
configured with [container_structure.yml](../container_structure.yml).</br>

> Using the [Makefile](../Makefile) can achieve the same in a cleaner way.

```shell
container-structure-test test --force --config container_structure.yml --verbosity info --image tomerfi/switcher_webapi:latest
```

## Code of Conduct

Please check the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) guidelines.
