# Contributing to `switcher_webapi`

:clap: First off, thank you for taking the time to contribute. :clap:

> **Note**: This repository is a docker image wrapping a python Rest API around the
> `aioswitcher` pypi module.
>
> If your contribution is a more of a *core contribution*, please consider maybe
> it belongs to the integrating module and not the wrapping docker.
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
  - [Container Structure Test](#container-structure-test)
- [Code of Conduct](#code-of-conduct)

> Please Note: the project semver is set in the [VERSION](VERSION) file.

## Documentation

- `docs/sources` is where the *restructuredText* for creating the [Sphinx Documentation](http://www.sphinx-doc.org)
  are stored for build, deployment and hosting by [Read the Docs](https://readthedocs.org/).
- `docs/Makefile` the basic *Makefile* for [Sphinx](http://www.sphinx-doc.org)
  documentation generator. From the [docs](docs/) path, type `make html` and
  [sphinx](http://www.sphinx-doc.org) will create the documentation site locally in
  `docs/build`.

## Python Code

It's basically a web server, start with [pyscripts/start_server.py](pyscripts/start_server.py),
and follow the [docs](https://switcher-webapi.tomfi.info). The file names are pretty self explanatory.

## Docker Build

Use the designated [Makefile](Makefile) [Make](https://www.gnu.org/software/make/manual/make.html) file.

```shell
# display a self explanatory help message.
make help

# will build a testing version of the docker and structure test it.
make docker-full-structure-testing
```

## Testing

### Python Test Framework

Testing is performed with [Pytest, Full-featured Python testing tool](https://docs.pytest.org).</br>
The file [pyscripts/test_server.py](pyscripts/test_server.py) holds the various test cases for the
web server, the file [pyscripts/test_server.py](pyscripts/conftest.py) holds the various mocks and
fixtures used to testing.

For automated local tests, use [Tox](https://tox.readthedocs.io).

### Container Structure Test

The container content is validated with
[container-structure-test](https://github.com/GoogleContainerTools/container-structure-test),
configured with [container_structure.yml](container_structure.yml).

```shell
container-structure-test test --force --config container_structure.yml --verbosity info --image tomerfi/switcher_webapi:latest
```

## Code of Conduct

Please check the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) markdown file.
