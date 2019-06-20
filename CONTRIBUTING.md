# Contributing to `switcher_webapi`

First off, thank you for taking the time to contribute.

> **Note**: This repository hosts a docker image wrapping a Rest API around the
> `aioswitcher` pypi module.
>
> If your contribution is a more of a *core contribution*, please consider maybe
> it belongs to the integrating module and not the wrapping docker.
> You can find the module repository [here](https://github.com/TomerFi/aioswitcher).

Contributing is pretty straight-forward:
-   Fork the repository
-   Commit your changes
-   Create a pull request against the `dev` branch
  
Please feel free to contribute, even to this contributing guideline file, if you see fit.

**Content**
-   [Items description](#items-description)
    -   [Configuration files](#configuration-files)
    -   [Docker](#docker)
    -   [Python](#python)
    -   [Shell](#shell)
    -   [Ignore files](#ignore-files)
    -   [Requirement files](#requirement-files)
    -   [Package management](#package-management)
    -   [Documentation](#documentation)

-   [Continuous Integration](#continuous-integration)
    -   [CircleCi](#circleci)
    -   [Requires-io](#requires-io)
    -   [David-DM](#david-dm)
    -   [Snyk](#snyk)

-   [Continuous Deployment](#continuous-deployment)
    -   [Docker Hub](#docker-hub)
    -   [Read the Docs](#read-the-docs)
    -   [Metadata](#metadata)

-   [Environments and Tools](#environments-and-tools)

-   [Testing](#testing)

-   [Guidelines](#guidelines)
    -   [NPM Scripts](#npm-scripts)
    -   [Shell Scripts](#shell-scripts)
    -   [Makefile](#makefile)

-   [Chat](#chat)

-   [Best Practices](#best-practices)

-   [Code of Conduct](#code-of-conduct)

## Items description
### Configuration files
-   `.circle/config.yml` is the configuration file for [CircleCi Continuous Integration and Deployment Services](https://circleci.com/gh/TomerFi/switcher_webapi/tree/dev).

-   `.codecov.yml` is the configuration file for [CodeCov Code Coverage](https://codecov.io/gh/TomerFi/switcher_webapi).

-   `.coveragerc` is the configuration file for [Coverage.py](https://coverage.readthedocs.io/en/v4.5.x/)
    creating coverage reports with the [pytest-cov plugin](https://pytest-cov.readthedocs.io/en/latest/).

-   `.prettierrc.yml` is the configuration for [Prettier Opinionated Code Formatter](https://prettier.io/)
    linting various file types (yml).

-   `.remarkrc` is the configuration file for [remark-lint](https://github.com/remarkjs/remark-lint)
    plugin for [Remark](https://remark.js.org/) linting *markdown* files.

-   `bandit.yml` is the configuration file for [Bandit common security issues finder](https://github.com/PyCQA/bandit)
    checking python scripts.

-   `container_structure.yml` is the configuration file for [GoogleContainerTools container-structure-test](https://github.com/GoogleContainerTools/container-structure-test)
    validating the container content.

-   `doc8.ini` is the configuration file for [Doc8 Style Checker](https://github.com/openstack/doc8)
    checking rst file types.

-   `mypy.ini` is the configuration file for [MyPy Static Type Checker](https://mypy.readthedocs.io/en/latest/index.html)
    for checking static types in python scripts.

-   `package.json` is npm's [package manager file](https://docs.npmjs.com/files/package.json)
    for managing dependencies, scripts and etc.

-   `pylintrc` is the configuration file for [Pylint Code Analysis](https://www.pylint.org/)
    linting python scripts.

-   `pyproject.toml` is designated to be the main configuration file for python based on
    [PEP518](https://www.python.org/dev/peps/pep-0518/) (not fully operative in this project yet).

-   `tox.ini` is the configuration file for [Tox Testing Automation](https://tox.readthedocs.io/en/latest/)
    testing the python code.

### Docker
-   `Dockerfile` is the instruction file for building the *docker image*.

### Python
-   `pyscripts` is where *python* scripts are stored.

### Shell
-   `shellscripts` is where *shell* scripts are stored.

### Ignore files
-   `.dockerignore` used for controlling what goes in the *docker image*.
-   `.gitignore` used for controlling what will not be pushed to *github*.

### Requirement files
-   `requirements.txt` is a list of python requirements for running the solution.

-   `requirements_constraints.txt` is a list of python requirements constraints.

-   `requirements_docs.txt` is a list of python requirements for testing and building the
    documentation.

-   `requirements_test.txt` is a list of python requirements for testing the solution.

### Package management
The [package.json](package.json) file specified by [npm](https://docs.npmjs.com/files/package.json)
manages our dependencies, scripts and some metadata.

### Documentation
-   `docs/sources` is where the *rst files* for creating the [Sphinx Documentation](http://www.sphinx-doc.org/en/master/)
    are stored for build, deployment and hosting by [Read the Docs](https://readthedocs.org/).

-   `docs/Makefile` the basic *Makefile* for [Sphinx](http://www.sphinx-doc.org/en/master/)
    documentation generator. From the [docs](docs/) path, type `make html` and
    [sphinx](http://www.sphinx-doc.org/en/master/) will create the documentation site locally in
    `docs/build`.

## Continuous Integration
### CircleCi
By hook configuration, for every pull request, [CircleCi](https://circleci.com/gh/TomerFi/switcher_webapi/tree/dev)
will execute the workflows described in [.circleci/config.yml](.circleci/config.yml)
and update the PR conversation with the results.

As a final step, [CircleCi](https://circleci.com/gh/TomerFi/switcher_webapi/tree/dev) will push the
[Coverage.py XML Report](https://coverage.readthedocs.io/en/v4.5.x/) to both
[CodeCov](https://codecov.io/gh/TomerFi/switcher_webapi) for code coverage analysis and
[Codacy](https://app.codacy.com/project/TomerFi/switcher_webapi/dashboard) for code quality
analysis.</br>
Both will of course push their results into the PR conversation.

Some of the steps are considered required and may prevent the PR from being merged.
But no worries, everything is fixable.

### Requires-io
[Requires.io](https://requires.io/github/TomerFi/switcher_webapi/requirements/?branch=dev)
is keeping an eye for versions updates upon the python requirements listed in the various
[requirements files](#requirement-files) and in [tox.ini](tox.ini) file.

### David-DM
[David-DM](https://david-dm.org/TomerFi/switcher_webapi) is keeping an eye for versions updates upon
the npm requirements listed in the *package.json* file.

### Snyk
[Snyk](https://snyk.io) is keeping an eye out for vulnerabilities in our
[npm dependencies](https://app.snyk.io/org/tomerfi/project/87072022-903c-4190-9a21-58c005f20255)
and in our [pypi dependencies](https://app.snyk.io/org/tomerfi/project/e06f1010-493f-45be-bb84-a80ddba9d358).

## Continuous Deployment
### Docker Hub
When a **git-tag** with the regex of `/^[0-9.]+$/` is set, [Docker Hub Cloud](https://hub.docker.com/r/tomerfi/switcher_webapi/builds)
will build the image based on the Dockerfile instructions file and tag it twice:
-   `<git-tag>`
-   latest

### Read the Docs
By hook configuration, for every *git-release-tag* [Read the Docs](https://readthedocs.org) will
build the documentation site based on the [docs/source](docs/source) and host it with the
`stable` tag [here](https://switcher-webapi.readthedocs.io/en/stable/).

### Metadata
By hook configuration, for every *docker image* build by [Docker Hub](https://hub.docker.com/r/tomerfi/switcher_webapi)
[MicroBadger](https://microbadger.com/images/tomerfi/switcher_webapi)
will receive a notification and publish the image metadata.

## Environments and Tools
> **Please Note**: the following (Python, virtualenv, nodeenv and Tox) needs to be pre-installed.

-   The [Python scripts](pyscripts/) was written with [Python 3.7](https://www.python.org/downloads/)
    in mind, which added a quite of few tweaks and adjustments, especially in regards to
    [asyncio](https://docs.python.org/3.7/library/asyncio.html?highlight=asyncio#module-asyncio).

-   Python's [virtualenv](https://pypi.org/project/virtualenv/), a tool for segregating Python
    environments. Please install [virtualenv](https://pypi.org/project/virtualenv/).

-   Python's [nodeenv](https://pypi.org/project/nodeenv/), a tool that enables us to create a
    Node.js virtual environment in resemblance to [virtualenv](https://pypi.org/project/virtualenv/),
    the tool also allows combining [nodeenv](https://pypi.org/project/nodeenv/) within
    [virtualenv](https://pypi.org/project/virtualenv/), which is exactly what we're doing with
    `tox`.

-   [Docker](https://www.docker.com/), as some of the testing automation are
    performed within a run-once docker container.

-   [Tox](https://tox.readthedocs.io/en/latest/) for automating unit testing in your
    local environment.
    -   Please install [Tox](https://tox.readthedocs.io/en/latest/) if you want to perform
        local testing automation.

    -   Tox utilizes Python's [virtualenv](https://pypi.org/project/virtualenv/).

    -   Tox is configured with [tox.ini](tox.ini).

    -   To run tox, simply execute `tox` from the [tox.ini](tox.ini)'s path. It is recommended
        that you also run `tox --help` to get familiar with the various options such as
        `-e` and `-r` that will help you perform faster and better tests.)

> **Please note**: the rest of the steps require no installation on your behalf,
> but knowing them is important seeing they are key elements for testing with `Tox` and/or `CircleCi`.

-   *NPM Package*: [package-json-validator](https://www.npmjs.com/package/package-json-validator)
    for validating the [package.json](package.json) file.

-   *Python Module*: [doc8](https://pypi.org/project/doc8/) for checking restructured Text (rst)
    files residing in [docs/source](docs/source) used to create the documentation site.
    -   doc8 is configured with [doc8.ini](doc8.ini).

-   *Python Module*: [sphinx](https://pypi.org/project/Sphinx/) for building the documentation
    site from the restructured Text (rst) files residing in [docs/source](docs/source).
    -   It's worth mentioning that [the documentation site](https://switcher-webapi.readthedocs.io/en/stable/)
        hosted with [Read the Docs](https://readthedocs.org) is based upon the theme [sphinx-rtd-theme](https://pypi.org/project/sphinx-rtd-theme/).

-   *NPM Package*: [remark-lint](https://www.npmjs.com/package/remark-lint) which is a plugin for
    [remark](https://www.npmjs.com/package/remark) and the [remark-cli](https://www.npmjs.com/package/remark-cli)
    command line tool for linting markdown files residing at the `base path` and in `.github`.
    -   [remark-lint](https://www.npmjs.com/package/remark-lint) uses a couple of presets and tools,
        all can be found under the dependencies key in [package.json](package.json).

    -   [remark-lint](https://www.npmjs.com/package/remark-lint) is configured with [.remarkrc](.remarkrc).

-   *NPM Package*: [markdown-spellcheck](https://www.npmjs.com/package/markdown-spellcheck)
    for checking the project *markdown* files for spelling errors.
    -   [markdown-spellcheck](https://www.npmjs.com/package/markdown-spellcheck) dictionary file
        is [.spelling](.spelling).

-   *NPM Package*: [prettier](https://www.npmjs.com/package/prettier) for validating yml files
    syntax against all existing yml files.
    -   [prettier](https://www.npmjs.com/package/prettier) is configured with [.prettierrc.yml](.prettierrc.yml).

-   *Docker Image*: [koalaman/shellcheck](https://hub.docker.com/r/koalaman/shellcheck) is used
    for checking shell script residing in [shellscripts](shellscripts/).

-   *Docker Image*: [hadolint/hadolint](https://hub.docker.com/r/hadolint/hadolint) is used for
    linting the instruction file [Dockerfile](Dockerfile).

-   *Linux Tool*: [container-structure-test](https://github.com/GoogleContainerTools/container-structure-test)
    for verifying the docker image content.
    -   The tool runs with the helper script [shellscripts/container-structure-test-verify.sh](shellscripts/container-structure-test-verify.sh)
        so it will not fail if the tool is not present when running `tox` locally. But this will
        probably come up with [CircleCi](https://circleci.com/gh/TomerFi/switcher_webapi/tree/dev).
        so please consider installing the tool manually.

    -   [container-structure-test](https://github.com/GoogleContainerTools/container-structure-test)
        is configured with [container_structure.yml](container_structure.yml).

-   *Python Package*: [bandit](https://pypi.org/project/bandit/) for finding common security
    issues with against the scripts residing in [pyscripts](pyscripts/).
    -   [bandit](https://pypi.org/project/bandit/) is configured with [bandit.yml](bandit.yml).

-   *Python Package*: [flake8](https://pypi.org/project/flake8/) for checking python scripts
    residing in [pyscripts](pyscripts/).

-   *Python Package*: [pylint](https://pypi.org/project/pylint/) for linting python scripts
    residing in [pyscripts](pyscripts/).
    -   [pylint](https://pypi.org/project/pylint/) is configured with [pylintrc](pylintrc).

-   *Python Package*: [black](https://pypi.org/project/black/) for formatting python scripts
    residing in [pyscripts](pyscripts/).
    -   [black](https://pypi.org/project/black/) is still in beta phase, from this project
        point-of-view it's in examination therefore errors are ignored in `tox` and it's
        not yet configured with `circleci`.

    -   [black](https://pypi.org/project/black/) is configured with [pyproject.toml](pyproject.toml).

-   *Python Package*: [mypy](https://pypi.org/project/mypy/) for checking static typing
    tests against python scripts residing in [pyscripts](pyscripts/).
    -   [mypy](https://pypi.org/project/mypy/) is configured with [mypy.ini](mypy.ini).

-   *Python Package*: [pytest](https://pypi.org/project/pytest/) as testing framework for running
    test-cases written in [pyscripts/test_server.py](pyscripts/test_server.py).
    -   [pytest](https://pypi.org/project/pytest/) uses a bunch of awesome plugins listed in
        [requirements_test.txt](requirements_test.txt).

-   *Docker Image*: [circleci/circleci-cli](https://hub.docker.com/r/circleci/circleci-cli)
    for validating the [.circleci/config.yml](.circleci/config.yml) file.

## Testing
Testing is performed with [Pytest, Full-featured Python testing tool](https://docs.pytest.org/en/latest/).</br>
The various Rest Http request test-cases is in [pyscripts/test_server.py](pyscripts/test_server.py).</br>

For automated local tests, use `tox`.

## Guidelines
> **Please Note**: that project [semvar](https://semver.org/) is being handled in both [VERSION](VERSION)
> file for creating the docker image with [Makefile](Makefile) and [package.json](package.json)
> for packaging handling.

Here are some guidelines (recommendations) for contributing to the `switcher_webapi` project:
-   If you add a new file, please consider is it should be listed within any or all of
    the [ignore files](#ignore-files).

-   If you change something inside the `docker image` it is strongly recommended trying to verify
    it with the [container-structure-test](https://github.com/GoogleContainerTools/container-structure-test).

-   While not all the test steps in [CircleCi](.circleci/config.yml) and in [Tox](tox.ini)
    are parallel to each other, most of them are, so tests failing with `Tox` will probably
    also fail with `CircleCi`.

-   If writing python code, please remember to [static type](https://www.python.org/dev/peps/pep-0484/).

-   You can run npm's script `spell-md-interactive` for handling all spelling mistakes before
    testing.
    You can also choose to run `spell-md-report` to print a full report instead of handling the
    spelling mistakes one-by-one.
    -   [markdown-spellcheck](https://www.npmjs.com/package/markdown-spellcheck) dictionary is the
        file [.spelling](.spelling).

### NPM Scripts
Before using the scrips, you need to install the dependencies.</br>
From the [package.json](package.json) file path, run `npm install`,
Then you can execute the scripts from the same path.
-   `npm run lint-md` will run [remark](https://remark.js.org/) against *markdown* files.

-   `npm run lint-yml` will run [prettier](https://prettier.io/) against *yml* files.

-   `npm run validate-pkg` will run [package-json-validator](https://www.npmjs.com/package/package-json-validator)
    against the [package.json](package.json) file.

-   `npm run spell-md-interactive` will run [markdown-spellcheck](https://www.npmjs.com/package/markdown-spellcheck)
    against *markdown* files in an interactive manner allowing us to select the appropriate action.

-   `npm run spell-md-report` will run [markdown-spellcheck](https://www.npmjs.com/package/markdown-spellcheck)
    against *markdown* files and print the report to stdout.

### Shell Scripts
The shell scripts in `shellscripts` were written for `bash` and not for `sh`.
-   `bash shellscripts/container-structure-test-verify.sh` will verify the existence of
    [container-structure-test](https://github.com/GoogleContainerTools/container-structure-test)
    and execute it. The script will `exit 0` if the tool doesn't exists so it will not fail `tox`.

-   `bash shellscripts/push-docker-description.sh` allows the deployment of the local
    [README.md](README.md) file as a docker image description in
    [Docker Hub](https://cloud.docker.com/repository/docker/tomerfi/switcher_webapi).
    Please use it with [Makefile](#makefile) as arguments are required

-   `bash shellscripts/run-once-docker-operations.sh <add-argument-here>` will verify the
    existence of [Docker](https://www.docker.com/) before executing various run-once docker
    operations based on the following arguments, if the script find that
    [Docker](https://www.docker.com/) is not installed, it will `exit 0` so it will not fail `tox`:
    -   argument `lint-dockerfile` will execute the docker image
        [hadolint/hadolint](https://hub.docker.com/r/hadolint/hadolint) linting the local
        [Dockerfile](Dockerfile).

    -   argument `check-shellscripts` will execute the docker image
        [koalaman/shellcheck](https://hub.docker.com/r/koalaman/shellcheck) for checking
        the shell scripts residing in [shellscripts](shellscripts/).

    -   argument `generate-changelog` will execute the docker image
        [ferrarimarco/github-changelog-generator](https://hub.docker.com/r/ferrarimarco/github-changelog-generator)
        for generating a simple [CHANGELOG.md](CHANGELOG.md) based on `git-release-tags`,
        the created file can be later used as a manual base for updating the documentation site.

    -   argument `circleci-validate` will execute the docker image
        [circleci/circleci-cli](https://hub.docker.com/r/circleci/circleci-cli)
        for validating the [.circleci/config.yml](.circleci/config.yml) file.

### Makefile
Using the [Makefile](Makefile) is highly recommended,
especially in regards to docker operations, try `make help` to list all the available tasks:
-   `make docker-build` will build image from Dockerfile.

-   `make docker-build-testing-image` will build image from Dockerfile using a testing tag.

-   `make docker-remove-testing-image` will remove the testing image (must be build first).

-   `make docker-build-no-cache` will build image from Dockerfile with no caching.

-   `make structure-test` will run the container-structure-test tool against the built image
    (must be build first) using the relative container_structure.yml file.

-   `make docker-build-structure-test` will build the image and test the container structure.

-   `make docker-build-no-cache-structure-test` will build the image and test the container
    structure.

-   `make docker-full-structure-testing` will build the image with the testing tag and
    remove after structure test.

-   `make docker-tag-latest` will add latest tag before pushing the latest version.

-   `make docker-run` will run the built image as a container (must be built first).

-   `make docker-build-and-run` will build image from Dockerfile and run as container.

-   `make docker-build-no-cache-and-run` will build image from Dockerfile with no caching and
    run as container.

-   `make push-description` will push the relative README.md file as full description to docker
    hub, requires username and password arguments.

-   `make verify-environment-file` will verify the existence of the required
    environment variables file and its content.

## Chat
Feel free to join the project's public [Slack Channel](https://tomfi.slack.com/messages/CK4DK2Z5G)</br>
GitHub, Codacy Docker Hub and Snyk are integrated with the channel and keep its members updated.

## Best Practices
This project tries to follow the [CII Best Practices](https://bestpractices.coreinfrastructure.org/en/projects/2891) guidelines.

That's not an easy task and I'm not sure achieving 100% is even possible for this specific project.</br>
At the time writing this, the project has achieved 42% (The writing of this file was actually according one to those guidelines).</br>
Any contribution bumping up this percentage will be gladly embraced.

## Code of Conduct
The [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) can also be found [here](https://switcher-webapi.readthedocs.io/en/stable/conduct.html).
