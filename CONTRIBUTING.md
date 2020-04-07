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
- [Container Structure](#container-structure)
- [Testing](#testing)
- [Code of Conduct](#code-of-conduct)

## Documentation

- `docs/sources` is where the *restructuredText* for creating the [Sphinx Documentation](http://www.sphinx-doc.org)
  are stored for build, deployment and hosting by [Read the Docs](https://readthedocs.org/).
- `docs/Makefile` the basic *Makefile* for [Sphinx](http://www.sphinx-doc.org)
  documentation generator. From the [docs](docs/) path, type `make html` and
  [sphinx](http://www.sphinx-doc.org) will create the documentation site locally in
  `docs/build`.

## Container Structure

The container content is validated with
[container-structure-test](https://github.com/GoogleContainerTools/container-structure-test),
configured with [container_structure.yml](container_structure.yml).

```shell
container-structure-test test --force --config container_structure.yml --verbosity info --image tomerfi/switcher_webapi:latest
```

## Testing

Testing is performed with [Pytest, Full-featured Python testing tool](https://docs.pytest.org).</br>
The various test-cases are in [tests](tests).

For automated local tests, use [Tox](https://tox.readthedocs.io).

## Code of Conduct

Please check the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) markdown file.
