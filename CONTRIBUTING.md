# Contributing to switcher_webapi, dockerized solution for integrating with your Switcher water heater

First off, thank you for taking the time to contribute.

> **Note**: This repository hosts a docker image wrapping a Rest API around the `aioswitcher` pypi module.
> If your contribution is a more of a *core contribution*, please consider maybe it belongs to the integrating module and not the wrapping docker.
> You can find the module repository [here](https://github.com/TomerFi/aioswitcher).

Contributing is pretty straight-forward:
-   Fork the repository
-   Commit your changes
-   Create a pull request against the `dev` branch
  
Please feel free to contribute, even to this contributing file, if you see fit.

## Items description
### Configuration files
-   `.circle/config.yml` is the configuration file for [CircleCi Continuous Integration and Deployment Services](https://circleci.com/gh/TomerFi/switcher_webapi/tree/dev).
-   `.codecov.yml` is the configuration file for [CodeCov Code Coverage](https://codecov.io/gh/TomerFi/switcher_webapi).
-   `.coveragerc` is the configuration file for [Coverage.py](https://coverage.readthedocs.io/en/v4.5.x/) creating coverage reports with the [pytest-cov plugin](https://pytest-cov.readthedocs.io/en/latest/).
-   `.prettierrc.yml` is the configuration for [Prettier Opinionated Code Formatter](https://prettier.io/) linting various file types (yml).
-   `.remarkrc` is the configuration file for [remark-lint](https://github.com/remarkjs/remark-lint) plugin for [Remark](https://remark.js.org/) linting md files.
-   `bandit.yml` is the configuration file for [Bandit common security issues finder](https://github.com/PyCQA/bandit) checking python scripts.
-   `container_structure.yml` is the configuration file for [GoogleContainerTools container-structure-test](https://github.com/GoogleContainerTools/container-structure-test) validating the container content.
-   `doc8.ini` is the configuration file for [Doc8 Style Checker](https://github.com/openstack/doc8) checking rst file types.
-   `mypy.ini` is the configuration file for [MyPy Static Type Checker](https://mypy.readthedocs.io/en/latest/index.html) for checking static types in python scripts.
-   `package.json` is npm's [package manager file](https://docs.npmjs.com/files/package.json) for managing dependencies, scripts and etc.
-   `pylintrc` is the configuration file for [Pylint Code Analysis](https://www.pylint.org/) linting python scripts.
-   `tox.ini` is the configuration file for [Tox Testing Automation](https://tox.readthedocs.io/en/latest/) testing the python code.

### Docker
-   `Dockerfile` is the instruction file for building the *docker image*.

### Python
-   `.pyscripts` is where *python* scripts are stored.

### Shell
-   `.shellscripts` is where *shell* scripts are stored.

### Ignore files
-   `.dockerignore` used for controlling what goes in the *docker image*.
-   `.gitignore` used for controlling what will not be pushed to *github*.
-   `.prettierignore` used for setting ignore list for *prettier code formatter*.

### Requirement files
-   `requirements.txt` is a list of python requirements for running the solution.
-   `requirements_constraints.txt` is a list of python requirements constraints.
-   `requirements_docs.txt` is a list of python requirements for testing and building the documentation.
-   `requirements_test.txt` is a list of python requirements for testing the solution.

### Tools
-   `Makefile` a make tool designed to ease the work with *docker*.
-   `Version` the semvar source for the various tools (Makefile and etc.)

### Documentation
-   `docs/sources` is where the *rst files* for creating the [Sphinx Documentation](http://www.sphinx-doc.org/en/master/) are stored for build, deploy and host by [Read the Docs](https://readthedocs.org/).
-   `docs/Makefile` the basic *Makefile* for [Sphinx](http://www.sphinx-doc.org/en/master/) documentation generator.

## Continuous Integration
### CircleCi
By hook configuration, for every pull request, [CircleCi](https://circleci.com/gh/TomerFi/switcher_webapi/tree/dev) will execute the workflows described in [.circle/config.yml](.circle/config.yml) and update the PR converstation with the results.

As a final step, [CircleCi](https://circleci.com/gh/TomerFi/switcher_webapi/tree/dev) will push the [Coverage.py XML Report](https://coverage.readthedocs.io/en/v4.5.x/) to both
[CodeCov](https://codecov.io/gh/TomerFi/switcher_webapi) for code coverage analysis and [Codacy](https://app.codacy.com/project/TomerFi/switcher_webapi/dashboard) for code quality analysis.
Both will of course push their results into the PR converstation.

Some of the steps are considered required and may prevent the PR from being merged.
But no worries, everything is fixable.

### Requires.io
[Requires.io](https://requires.io/github/TomerFi/switcher_webapi/requirements/?branch=dev) is keeping an eye for versions updates upon the python requirements listed in the various *requirements files* and in the *tox.ini* file.

### David-DM
[David-DM](https://david-dm.org/TomerFi/switcher_webapi) is keeping an eye for versions updates upon the npm requirements listed in the *package.json* file.

## Continuous Deployment
### Docker Hub
When a **git-tag** with the regex of `/^[0-9.]+$/` is set, [Docker Hub Cloud](https://hub.docker.com/r/tomerfi/switcher_webapi/builds) will build the image based on the Dockerfile instructions file and tag it twice:
-   `<git-tag>`
-   latest

### Read the Docs
By hook configuration, for every *git-release-tag* [Read the Docs](https://readthedocs.org) will build the documentation site based on the [docs/source](folder) and host it with the `stable` tag [here](https://switcher-webapi.readthedocs.io/en/stable/).

### Metadata
By hook configuration, for every *docker image* build by [Docker Hub](https://hub.docker.com/r/tomerfi/switcher_webapi) [MicroBadger](https://microbadger.com/images/tomerfi/switcher_webapi) will receive a notification and publish the image metadata.

## Testing
Testing is performed with [Pytest, Full-featured Python testing tool](https://docs.pytest.org/en/latest/).</br>
The various Rest Http requests test-cases is in [pyscripts/test_server.py](pyscripts/test_server.py).

## Environments, Linters, Checkers, Validators and Tools
This project a bunch of awesome tools designed to keep the bugs away:

-   The [Python scripts](pyscripts/) was written with [Python 3.7](https://www.python.org/downloads/) in mind, which added a quite of few tweaks and adjustments, espcisally in regards to [asyncio](https://docs.python.org/3.7/library/asyncio.html?highlight=asyncio#module-asyncio).

-   Python's [virtualenv](https://pypi.org/project/virtualenv/), a tool for segregating Python environments. Please install [virtualenv](https://pypi.org/project/virtualenv/).

-   Python's [nodeenv](https://pypi.org/project/nodeenv/), a tool that enables us to create a Node.js virtual environment in resemblance to [virtualenv](https://pypi.org/project/virtualenv/), the tool also allowes combining [nodeenv](https://pypi.org/project/nodeenv/) within [virtualenv](https://pypi.org/project/virtualenv/), which is exactly what we're doing,

-   [Docker](https://www.docker.com/), as some of the testing automations are performed within a run-once docker container.

-   [Tox](https://tox.readthedocs.io/en/latest/) for automating unit testing in your local environment.
    -   Please install [Tox](https://tox.readthedocs.io/en/latest/) if you want to perform local testing automations.
    -   Tox utilizes Python's [virtualenv](https://pypi.org/project/virtualenv/).
    -   Tox is configured with [tox.ini](tox.ini).
    -   To run tox, simply execute `tox` from the [tox.ini](tox.ini)'s path. (It is recommended that you also run `tox --help` to get famillair with the various options such as `-e` and `-r` that will help you perform faster and better tests.)

> **Please note**: the rest of the steps require no installation on your behalf, but knowning them is important seeing they are key elements for testing with `Tox` and/or `CircleCi`.

-   *NPM Package*: [package-json-validator](https://www.npmjs.com/package/package-json-validator) to validate the [package.json](package.json) file.

-   *Python Module*: [doc8](https://pypi.org/project/doc8/) for checking reStructuredText (rst) files residing in [docs/source](docs/source) used to create the documentation site.
    -   doc8 is configured with [doc8.ini](doc8.ini).

-   *Python Module*: [sphinx](https://pypi.org/project/Sphinx/) for building the documentation site from the reStructuredText (rst) files residing in [docs/source](docs/source).
    -   It's worth mentioning that [the documentation site](https://switcher-webapi.readthedocs.io/en/stable/) hosted with [Read the Docs](https://readthedocs.org) is based upon the theme [sphinx-rtd-theme](https://pypi.org/project/sphinx-rtd-theme/).

-   *NPM Package*: [remark-lint](https://www.npmjs.com/package/remark-lint) which is a plugin for [remark](https://www.npmjs.com/package/remark) and the [remark-cli](https://www.npmjs.com/package/remark-cli) command line tool for linting markdown files residing at the `base path` and in `.github`.
    -   [remark-lint](https://www.npmjs.com/package/remark-lint) uses a couple of prestes and tools, all can be found under the dependencies key in [package.json](package.json).
    -   [remark-lint](https://www.npmjs.com/package/remark-lint) is configured with [.remarkrc](.remarkrc).

-   *NPM Package*: [prettier](https://www.npmjs.com/package/prettier) for validating yml files syntax againt all existing yml files.
    -   Ignoring files with [prettier](https://www.npmjs.com/package/prettier) is done using the [.prettierignore](.prettierignore) file.
    -   [prettier](https://www.npmjs.com/package/prettier) is configured with [.prettierrc.yml](.prettierrc.yml).

-   *Docker Image*: [koalaman/shellcheck](https://hub.docker.com/r/koalaman/shellcheck) is used to check shell script residing in [shellscripts](shellscripts/).

-   *Docker Image*: [hadolint/hadolint](https://hub.docker.com/r/hadolint/hadolint) is used for linting the instruction file Dockerfile.

-   *Linux Tool*: [container-structure-test](https://github.com/GoogleContainerTools/container-structure-test) for verifing the docker image content.
    -   The tool runs with the helper script [shellscripts/container-structure-test-verify.sh](shellscripts/container-structure-test-verify.sh) so it will not fail if the tool is not present when running `tox` localy. But it will come up in [CircleCi](https://circleci.com/gh/TomerFi/switcher_webapi/tree/dev) so please consider installing the tool manually.
    -   [container-structure-test](https://github.com/GoogleContainerTools/container-structure-test) is configured with [container_structure.yml](container_structure.yml).

-   *Python Package*: [bandit](https://pypi.org/project/bandit/) for finding common security issues with against the scripts residing in [pyscripts](pyscripts/).
    -   [bandit](https://pypi.org/project/bandit/) is configured with [bandit.yml](bandit.yml).

-   *Python Package*: [flake8](https://pypi.org/project/flake8/) for checking python scripts residing in [pyscripts](pyscripts/).

-   *Python Package*: [pylint](https://pypi.org/project/pylint/) for linting python scripts residing in [pyscripts](pyscripts/).
    -   [pylint](https://pypi.org/project/pylint/) is configured with [pylintrc](pylintrc).

-   *Python Package*: [mypy](https://pypi.org/project/mypy/) for checking static typing tests against python scripts residing in [pyscripts](pyscripts/).
    -   [mypy](https://pypi.org/project/mypy/) is configured with [mypy.ini](mypy.ini).

-   *Python Package*: [pytest](https://pypi.org/project/pytest/) as testing framework for running test-cases written in [pyscripts/test_server.py](pyscripts/test_server.py).
    -   [pytest](https://pypi.org/project/pytest/) uses a bunch of awesome plugins listed in [requirements_test.txt](requirements_test.txt).

-   *Docker Image*: [circleci/circleci-cli](https://hub.docker.com/r/circleci/circleci-cli) for validating the [.circleci/config.yml](.circleci/config.yml) file.

## Guidelines
Here are some guidelines (recommendations) for contributing to the `switcher_webapi` project:
-   If you add a new file, please consider is it should be listed within any or all of  the [ignore files](#ignore-files).
-   If you change something inside the `docker image` it is stronglly recommended trying to verify it with the [container-structure-test](https://github.com/GoogleContainerTools/container-structure-test).
-   While not all the test steps in [CircleCi](.circle/config.yml) and in [Tox](tox.ini) are parallel to eachother, most of them are, so tests failing with `Tox` will probably also fail with `CircleCi`.
-   It's highly recommended using the [Makefile](Makefile), espcisally in regards to docker operations, try `make help` to list all the available tasks.
-   If regards to docker, the [shellscripts/push-docker-description.sh](shellscripts/push-docker-description.sh) allowed deployment of the description section in [Docker Hub](https://cloud.docker.com/repository/docker/tomerfi/switcher_webapi).
-   If needed, you can re-generate the [CHANGELOG.md](CHANGELOG.md) file using [shellscripts/run-once-docker-operations.sh](shellscripts/run-once-docker-operations.sh), just run `bash shellscripts/run-once-docker-operations.sh generate-changelog] from the file path.
-   If writing python code, please remember to [static type](https://www.python.org/dev/peps/pep-0484/).

## Chat
Feel free to join the project's public [Slack Channel](https://tomfi.slack.com/messages/CK4DK2Z5G)</br>
GitHub, Codacy and Docker Hub are integrated with the channel and keep its members updated.

## Best Practices
This project tries to follow the [CII Best Practices](https://bestpractices.coreinfrastructure.org/en/projects/2891) guidelines.

That's not an easy task and I'm not sure achieving 100% is even possible for this specific project.</br>
At the time writing this, the project has achieved 42%.</br>
Any contribution bumping up this percentage will be gladly embraced.
