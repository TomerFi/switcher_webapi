Contributing to **switcher_webapi**
***********************************

First off, thank you for taking the time to contribute.

.. note::

   This repository hosts a docker image wrapping a Rest API around the `aioswitcher pypi module`_.

   If your contribution is a more of a *core contribution*, please consider maybe
   it belongs to the integrating module and not the wrapping docker.
   You can find the `module repository here`_.

Contributing is pretty straight-forward:
*   Fork the repository
*   Commit your changes
*   Create a pull request against the **dev** branch

Please feel free to contribute, even to this contributing guideline file, if you see fit.

.. contents:: TOC
   :local:
   :depth: 2

Items description
^^^^^^^^^^^^^^^^^

Configuration files
-------------------

*   ``.circle/config.yml`` is the configuration file for
    `CircleCi Continuous Integration and Deployment Services`_.

*   ``.codecov.yml`` is the configuration file for `CodeCov Code Coverage`_.

*   ``.coveragerc`` is the configuration file for `Coverage.py`_ creating coverage reports with
    the `pytest-cov plugin`_.

*   ``.prettierrc.yml`` is the configuration for `Prettier Opinionated Code Formatter`_ linting
    various file types (yml).

*   ``.remarkrc`` is the configuration file for `remark-lint`_ plugin for Remark_ linting md files.

*   ``bandit.yml`` is the configuration file for `Bandit common security issues finder`_ checking
    python scripts.

*   ``container_structure.yml`` is the configuration file for
    `GoogleContainerTools container-structure-test`_ validating the container content.

*   ``doc8.ini`` is the configuration file for `Doc8 Style Checker`_ checking rst file types.

*   ``mypy.ini`` is the configuration file for `MyPy Static Type Checker`_ for checking static
    types in python scripts.

*   ``package.json`` is npm's `package manager file`_ for managing dependencies, scripts and etc.

*   ``pylintrc`` is the configuration file for `Pylint Code Analysis`_ linting python scripts.

*   ``pyproject.toml`` is designated to be the main configuration file for python based on PEP518_
    (not fully operative in this project yet).

*   ``.spelling`` is the dictionary/ignore file used by both `markdown-spellcheck`_ and vale_.
    Case-insensitive words in this file will not raise a spelling mistake error.

*   ``.vale.ini`` is the configuration for vale_.

*   ``tox.ini`` is the configuration file for `Tox Testing Automation`_ testing the python code.

Docker
------

*   ``Dockerfile`` is the instruction file for building the *docker image*.

Python
------

*   ``pyscripts`` is where *python* scripts are stored.

Shell
-----

*   ``shellscripts`` is where *shell* scripts are stored.

Ignore files
------------

*   ``.dockerignore`` used for controlling what goes in the *docker image*.
*   ``.gitignore`` used for controlling what will not be pushed to *github*.
*   ``.prettierignore`` used for ignoring specific files or folders from *prettier*.
*   ``.remarkignore`` used for ignoring specific files or folders from *remark-lint*.

Requirement files
-----------------

*   ``requirements.txt`` is a list of python requirements for running the solution.

*   ``requirements_constraints.txt`` is a list of python requirements constraints.

*   ``requirements_docs.txt`` is a list of python requirements for testing and building the
    documentation.

*   ``requirements_test.txt`` is a list of python requirements for testing the solution.

Package management
------------------

The ``package.json`` file `specified by npm`_ manages our dependencies, scripts and some metadata.

Documentation
-------------

*   ``docs/sources`` is where the *rst files* for creating the `Sphinx Documentation`_ are stored
    for build, deployment and hosting by `Read the Docs`_.

*   ``docs/Makefile`` the basic *Makefile* for Sphinx_ documentation generator.
    From the ``docs`` path, type ``make html`` and sphinx_ will create the documentation site
    locally in ``docs/build``.

Continuous Integration
^^^^^^^^^^^^^^^^^^^^^^

CircleCi
--------

By hook configuration, for every pull request, CircleCi_ will execute the workflows described in
``.circleci/config.yml`` and update the PR conversation with the results.

As a final step, CircleCi_ will push the `Coverage.py XML Report`_ to both CodeCov_ for code
coverage analysis and Codacy_ for code quality analysis.
Both will of course push their results into the PR conversation.

Some of the steps are considered required and may prevent the PR from being merged.
But no worries, everything is fixable.

Requires-io
-----------

`Requires.io`_ is keeping an eye for versions updates upon the python requirements listed in the
various ``requirements files`` and in ``tox.ini`` file.

David-DM
--------

`David-DM`_ is keeping an eye for versions updates upon the npm requirements listed in the
*package.json* file.

Snyk
----

Snyk_ is keeping an eye out for vulnerabilities in our `npm dependencies`_,
our  `pypi dependencies`_ and our `docker image dependencies`_.

Continuous Deployment
^^^^^^^^^^^^^^^^^^^^^

Docker Hub
----------

When a **git-tag** with the regex of ``/^[0-9.]+$/`` is set, `Docker Hub Cloud`_ will build the
image based on the ``Dockerfile`` instructions file and tag it twice:
-   ``<git-tag>``
-   latest

Read the Docs
-------------

By hook configuration, for every *git-release-tag* `Read the Docs`_ will build the documentation
site based on the ``docs/source`` and host it with the `stable tag`_.

Metadata
--------

By hook configuration, for every *docker image* build by `Docker Hub`_, MicroBadger_ will receive
a notification and publish the image metadata.

Environments and Tools
^^^^^^^^^^^^^^^^^^^^^^

.. note::

   The following (Python, virtualenv, nodeenv and Tox) needs to be pre-installed before local
   testing with ``tox``.

*   The Python scripts in ``pyscripts`` was written with `Python 3.7`_ in mind,
    which added a few tweaks and adjustments, especially in regards to asyncio_.

*   Python's virtualenv_, a tool for segregating Python environments.

*   Python's nodeenv_, a tool that enables us to create Node.js virtual environment in resemblance
    to virtualenv_, the tool also allows combining nodeenv inside virtualenv_, which is exactly
    what we're doing with ``tox``.

*   Docker_, as some of the testing automation are performed within a run-once docker container.

*   Tox_ for automating unit testing in your local environment.
    *   Tox utilizes Python's virtualenv_.

    *   Tox is configured with ``tox.ini``.

    *   To run tox, simply execute ``tox`` from ``tox.ini``'s path. It is recommended that you
        also run ``tox --help`` to get familiar with the various options such as ``-e`` and ``-r``
        that will help you perform faster and better tests.)

.. note::

   **Please note**: the rest of the steps require no installation on your behalf,
   but knowing them is important seeing they are key elements for testing with ``Tox`` and/or
   ``CircleCi``.

*   *NPM Package*: `package-json-validator`_ for validating the ``package.json`` file.

*   *Python Module*: doc8_ for checking restructured text (rst) files residing in ``docs/source``
    and used to create the documentation site.

    *   doc8 is configured with ``doc8.ini``.

*   *Docker Image*: `jdkato/vale`_ for linting restructured text files residing in ``docs/source``
    for spelling/syntax mistakes.

    *   `jdkato/vale`_ ignore file is ``.spelling``.

    *   `jdkato/vale`_ is configured with ``.vale.ini``.

*   *Python Module*: sphinx_ for building the documentation site from the restructured Text (rst)
    files residing in ``docs/source``.

    *   It's worth mentioning that `the documentation site`_ hosted with `Read the Docs`_ is based
        upon the theme `sphinx-rtd-theme`_

*   *NPM Package*: `remark-lint`_ which is a plugin for Remark_ and the `remark-cli`_ command line
    tool for linting *markdown* files residing at the base path and in ``.github``.

    *   `remark-lint`_ uses a couple of presets and tools, all can be found under the dependencies
        key in ``package.json``.

    *   `remark-lint`_ ignore list is the file ``.remarkignore``.

    *   `remark-lint`_ is configured with ``.remarkrc``.

*   *NPM Package*: `markdown-spellcheck`_ for checking the project *markdown* files for spelling
    errors.

    *   `markdown-spellcheck`_ dictionary file is ``.spelling``.

*   *NPM Package*: prettier_ for validating yml files syntax against all existing yml files.

    *   prettier_ ignore list is the file ``.prettierignore``.

    *   prettier_ is configured with ``.prettierrc.yml``.

*   *Docker Image*: `koalaman/shellcheck`_ is used for checking shell script residing in
    ``shellscripts``.

*   *Docker Image*: `hadolint/hadolint`_ is used for linting the instruction file ``Dockerfile``.

*   *Linux Tool*: `container-structure-test`_ for verifying the docker image content.

    *   The tool runs with the helper script ``shellscripts/container-structure-test-verify.sh``,
        it will not fail if the tool is not present when running ``tox`` locally.
        But this will probably come up with CircleCi_ so please consider installing the tool
        manually.

    *   `container-structure-test`_ is configured with ``container_structure.yml``.

*   *Python Package*: bandit_ for finding common security issues with against the scripts residing
    in ``pyscripts``.
    *   bandit_ is configured with ``bandit.yml``.

*   *Python Package*: flake8_ for checking python scripts residing in ``pyscripts``.

*   *Python Package*: pylint_ for linting python scripts residing in ``pyscripts``.
    *   pylint_ is configured with ``pylintrc``.

*   *Python Package*: black_ for formatting python scripts residing in ``pyscripts``.

    *   black_ is still in beta phase, from this project point-of-view it's in examination,
        therefore errors are ignored in ``tox`` and it's not yet configured with ``circleci``.

    *   black_ is configured with ``pyproject.toml``.

*   *Python Package*: mypy_ for checking static typing tests against python scripts residing in
    ``pyscripts``.
    *   mypy_ is configured with ``mypy.ini``.

*   *Python Package*: pytest_ as testing framework for running test-cases written in
    ``pyscripts/test_server.py``.
    *   pytest_ uses a bunch of awesome plugins listed in ``requirements_test.txt``.

*   *Docker Image*: `circleci/circleci-cli`_ for validating the ``.circleci/config.yml`` file.

Testing
^^^^^^^

Testing is performed with `Pytest, Full-featured Python testing tool`_.
The various Rest Http request test-cases is in ``pyscripts/test_server.py``.

For automated local tests, use ``tox``.

Guidelines
^^^^^^^^^^

.. note::

   The project's semvar_ is being handled in both ``VERSION`` file for creating the docker image
   with ``Makefile`` and in ``package.json`` for packaging handling.

Here are some guidelines (recommendations) for contributing to the ``switcher_webapi`` project:

*   If you add a new file, please consider is it should be listed within any or all of the
    ``ignore files``.

*   If you change something inside the ``docker image`` it is strongly recommended verifying
    it with the `container-structure-test`_

*   While not all the test steps in ``CircleCi`` and in ``Tox`` are parallel to each other,
    most of them are, so tests failing with ``Tox`` will probably also fail with ``CircleCi``.

*   If you're writing python code, please remember to `static type`_ your code or else it will
    probably fail ``mypy`` tests.

*   You can run npm's script ``spell-md-interactive`` for handling all spelling mistakes before
    testing.
    You can also choose to run ``spell-md-report`` to print a full report instead of handling the
    spelling mistakes one-by-one.
    *   `markdown-spellcheck`_ dictionary is the file ``.spelling``.

NPM Scripts
-----------

Before using the scrips, you need to install the dependencies.
From the ``package.json`` file path, run ``npm install``,
Then you can execute the scripts from the same path.

*   ``npm run lint-md`` will `run remark`_ against *markdown* files.

*   ``npm run lint-yml`` will `run prettier`_ against *yml* files.

*   ``npm run validate-pkg`` will run `package-json-validator`_ against the ``package.json`` file.

*   ``npm run spell-md-interactive`` will run `markdown-spellcheck`_ against *markdown* files in an
    interactive manner allowing us to select the appropriate action.

*   ``npm run spell-md-report`` will run `markdown-spellcheck`_ against *markdown* files and print
    the report to stdout.

Shell Scripts
-------------

.. note::

   The shell scripts in ``shellscripts`` were written for ``bash`` and not for ``sh``.

*   ``bash shellscripts/container-structure-test-verify.sh`` will verify the existence of
    `container-structure-test`_ and execute it. The script will ``exit 0`` if the tool doesn't
    exists so it will not fail ``tox``.

*   ``bash shellscripts/push-docker-description.sh`` allows the deployment of the local
    ``README.md`` file as a docker image description in `Docker Hub`_. Please use it with
    ``Makefile`` as arguments are required.

*   ``bash shellscripts/run-once-docker-operations.sh <add-argument-here>`` will verify the
    existence of Docker_ before executing various *run-once docker operations* based on the
    following arguments. If the script find that Docker_ is not installed, it will ``exit 0``
    so it will not fail ``tox``:

    *   **argument**: ``lint-dockerfile`` will execute the docker image `hadolint/hadolint`_
        linting the local ``Dockerfile``.

    *   **argument**: ``check-shellscripts`` will execute the docker image `koalaman/shellcheck`_
        for checking the shell scripts residing in ``shellscripts``.

    *   **argument**: ``generate-changelog`` will execute the docker image
        `ferrarimarco/github-changelog-generator`_ for generating a simple ``CHANGELOG.md`` based
        on ``git-release-tags``.
        The created file can be later used as a manual base for updating the documentation site.

    *   **argument**: ``circleci-validate`` will execute the docker image `circleci/circleci-cli`_
        for validating the ``.circleci/config.yml`` file.

    *   argument ``vale-rstdocs`` will execute the docker image `jdkato/vale`_ checking for
        spelling or syntax mistakes in restructured text file residing in ``docs/source``.

Makefile
--------

Using the ``Makefile`` is highly recommended, especially in regards to docker operations.
Try ``make help`` to list all the available tasks:
*   ``make docker-build`` will build image from relative ``Dockerfile``.

*   ``make docker-build-testing-image`` will build image from relative ``Dockerfile`` using
    a testing tag.

*   ``make docker-remove-testing-image`` will remove the testing image (must be build first).

*   ``make docker-build-no-cache`` will build image from ``Dockerfile`` with no caching.

*   ``make structure-test`` will run the container-structure-test tool against the built image
    (must be build first) using the relative ``container_structure.yml`` file.

*   ``make docker-build-structure-test`` will build the image and test the container structure.

*   ``make docker-build-no-cache-structure-test`` will build the image and test the container
    structure.

*   ``make docker-full-structure-testing``` will build the image with the testing tag and remove
    after structure test.

*   ``make docker-tag-latest`` will add latest tag before pushing the latest version.

*   ``make docker-run`` will run the built image as a container (must be built first).

*   ``make docker-build-and-run`` will build image from ``Dockerfile`` and run as container.

*   ``make docker-build-no-cache-and-run`` will build image from ``Dockerfile`` with no caching
    and run as container.

*   ``make push-description`` will push the relative ``README.md`` file as full description to
    docker hub, requires username and password arguments.

*   ``make verify-environment-file`` will verify the existence of the required environment
    variables file and its content.

Chat
^^^^

Feel free to join the project's public `Slack Channel`_.
GitHub, Codacy Docker Hub and Snyk are integrated with the channel and keeping its members updated.

Best Practices
^^^^^^^^^^^^^^

This project tries to follow the `CII Best Practices`_ guidelines.
That's not an easy task and I'm not sure achieving 100% is even possible for this specific project.
At the time writing this, the project has achieved 42%.
(The writing of this file was actually according one to those guidelines).

Any contribution bumping up this percentage will be gladly embraced.

.. _aioswitcher pypi module: https://pypi.org/project/aioswitcher/
.. _module repository here: https://github.com/TomerFi/aioswitcher
.. _CircleCi Continuous Integration and Deployment Services: https://circleci.com/gh/TomerFi/switcher_webapi/tree/dev
.. _CodeCov Code Coverage: https://codecov.io/gh/TomerFi/switcher_webapi
.. _Coverage.py: https://coverage.readthedocs.io/en/v4.5.x/
.. _pytest-cov plugin: https://pytest-cov.readthedocs.io/en/latest/
.. _Prettier Opinionated Code Formatter: https://prettier.io/
.. _remark-lint: https://github.com/remarkjs/remark-lint
.. _Remark: https://remark.js.org/
.. _Bandit common security issues finder: https://github.com/PyCQA/bandit
.. _GoogleContainerTools container-structure-test: https://github.com/GoogleContainerTools/container-structure-test
.. _Doc8 Style Checker: https://github.com/openstack/doc8
.. _MyPy Static Type Checker: https://mypy.readthedocs.io/en/latest/index.html
.. _package manager file: https://docs.npmjs.com/files/package.json
.. _Pylint Code Analysis: https://www.pylint.org/
.. _Tox Testing Automation: https://tox.readthedocs.io/en/latest/
.. _specified by npm: https://docs.npmjs.com/files/package.json
.. _Sphinx Documentation: http://www.sphinx-doc.org/en/master/
.. _Read the Docs: https://readthedocs.org/
.. _Sphinx: http://www.sphinx-doc.org/en/master/
.. _CircleCi: https://circleci.com/gh/TomerFi/switcher_webapi/tree/dev
.. _Coverage.py XML Report: https://coverage.readthedocs.io/en/v4.5.x/
.. _CodeCov: https://codecov.io/gh/TomerFi/switcher_webapi
.. _Codacy: https://app.codacy.com/project/TomerFi/switcher_webapi/dashboard
.. _Requires.io: https://requires.io/github/TomerFi/switcher_webapi/requirements/?branch=dev
.. _David-DM: https://david-dm.org/TomerFi/switcher_webapi
.. _Docker Hub Cloud: https://hub.docker.com/r/tomerfi/switcher_webapi/builds
.. _stable tag: https://switcher-webapi.readthedocs.io/en/stable
.. _Docker Hub: https://hub.docker.com/r/tomerfi/switcher_webapi
.. _MicroBadger: https://microbadger.com/images/tomerfi/switcher_webapi
.. _Python 3.7: https://www.python.org/downloads/
.. _asyncio: https://docs.python.org/3.7/library/asyncio.html?highlight=asyncio#module-asyncio
.. _virtualenv: https://pypi.org/project/virtualenv/
.. _nodeenv: https://pypi.org/project/nodeenv/
.. _Docker: https://www.docker.com/
.. _Tox: https://tox.readthedocs.io/en/latest/
.. _package-json-validator: https://www.npmjs.com/package/package-json-validator
.. _doc8: https://pypi.org/project/doc8/
.. _the documentation site: https://switcher-webapi.readthedocs.io/en/stable/
.. _sphinx-rtd-theme: https://pypi.org/project/sphinx-rtd-theme/
.. _remark-cli: https://www.npmjs.com/package/remark-cli
.. _prettier: https://www.npmjs.com/package/prettier
.. _koalaman/shellcheck: https://hub.docker.com/r/koalaman/shellcheck
.. _hadolint/hadolint: https://hub.docker.com/r/hadolint/hadolint
.. _container-structure-test: https://github.com/GoogleContainerTools/container-structure-test
.. _bandit: https://pypi.org/project/bandit/
.. _flake8: https://pypi.org/project/flake8/
.. _pylint: https://pypi.org/project/pylint/
.. _mypy: https://pypi.org/project/mypy/
.. _pytest: https://pypi.org/project/pytest/
.. _ferrarimarco/github-changelog-generator: https://hub.docker.com/r/ferrarimarco/github-changelog-generator
.. _circleci/circleci-cli: https://hub.docker.com/r/circleci/circleci-cli
.. _Pytest, Full-featured Python testing tool: https://docs.pytest.org/en/latest/
.. _semvar: https://semver.org/
.. _static type: https://www.python.org/dev/peps/pep-0484/
.. _run remark: https://remark.js.org/
.. _run prettier: https://prettier.io/
.. _Docker: https://www.docker.com/
.. _Slack Channel: https://tomfi.slack.com/messages/CK4DK2Z5G
.. _CII Best Practices: https://bestpractices.coreinfrastructure.org/en/projects/2891
.. _black: https://pypi.org/project/black/
.. _PEP518: https://www.python.org/dev/peps/pep-0518/
.. _markdown-spellcheck: https://www.npmjs.com/package/markdown-spellcheck
.. _snyk: https://snyk.io
.. _npm dependencies: https://app.snyk.io/org/tomerfi/project/87072022-903c-4190-9a21-58c005f20255
.. _pypi dependencies: https://app.snyk.io/org/tomerfi/project/e06f1010-493f-45be-bb84-a80ddba9d358
.. _vale: https://errata-ai.github.io/vale/
.. _jdkato/vale: https://hub.docker.com/r/jdkato/vale
.. _docker image dependencies: https://app.snyk.io/org/tomerfi/project/efb45c0a-f64b-4db5-8976-966508b78cd8
