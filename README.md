<!--lint disable maximum-heading-length-->
# Switcher Water Heater Unofficial Docker-based WebAPI</br>[![shields-io-maintenance]][12] [![microbadger-docker-version]][9] [![microbadger-docker-license]][11] [![shields-io-docker-pulls]][10]

| Stage     | Badges                                                                                                             |
| --------- | ------------------------------------------------------------------------------------------------------------------ |
| `Build`   | [![circleci]][2] [![shields-io-docker-cloud-build-status]][3] [![codecov]][0] [![codacy]][1] [![read-the-docs]][4] |
| `Package` | [![requires-io]][5] [![david-dm-dev-package-json-dependencies-status]][7]                                          |
| `Etc`     |  [![greenkeeper-badge]][17] [![code-style-black]][15] [![checked-with-mypy]][16]                                   |

An asynchronous [sanic webapp](https://pypi.org/project/sanic/) running inside a [python docker image](https://hub.docker.com/_/python) using [uvloop](https://pypi.org/project/uvloop/) as the event loop.</br>
Used as a rest api wrapper for [aioswitcher](https://pypi.org/project/aioswitcher/).</br>

If you're using the [Switcher Water Heater](https://switcher.co.il/) and you want to wrap a rest api around it... you came to the right place!</br>

For full install and usage instructions,
Please check out the [Switcher water heater WebAPI documentation](https://switcher-webapi.readthedocs.io)
hosted with [readthedocs.io](https://readthedocs.org/).

<!-- Real Links -->
[0]: https://codecov.io/gh/TomerFi/switcher_webapi
[1]: https://www.codacy.com/app/TomerFi/switcher_webapi?utm_source=github.com&utm_medium=referral&utm_content=TomerFi/switcher_webapi&utm_campaign=Badge_Grade
[2]: https://circleci.com/gh/TomerFi/switcher_webapi
[3]: https://hub.docker.com/r/tomerfi/switcher_webapi/builds
[4]: https://switcher-webapi.readthedocs.io/en/stable/?badge=stable
[5]: https://requires.io/github/TomerFi/switcher_webapi/requirements
[7]: https://david-dm.org/TomerFi/switcher_webapi
[9]: https://microbadger.com/images/tomerfi/switcher_webapi
[10]: https://hub.docker.com/r/tomerfi/switcher_webapi
[11]: https://github.com/TomerFi/switcher_webapi/blob/dev/LICENSE
[12]: https://github.com/TomerFi/switcher_webapi
[15]: https://black.readthedocs.io/en/stable/
[16]: http://mypy-lang.org/
[17]: https://greenkeeper.io/
<!-- Badges Links -->
[checked-with-mypy]: http://www.mypy-lang.org/static/mypy_badge.svg
[circleci]: https://circleci.com/gh/TomerFi/switcher_webapi.svg?style=shield
[codacy]: https://api.codacy.com/project/badge/Grade/bc33021329894d75943f8d0fe77b95a5
[codecov]: https://codecov.io/gh/TomerFi/switcher_webapi/graph/badge.svg
[code-style-black]: https://img.shields.io/badge/code%20style-black-000000.svg
[david-dm-dev-package-json-dependencies-status]: https://david-dm.org/TomerFi/switcher_webapi/status.svg
[greenkeeper-badge]: https://badges.greenkeeper.io/TomerFi/switcher_webapi.svg
[microbadger-docker-license]: https://images.microbadger.com/badges/license/tomerfi/switcher_webapi.svg
[microbadger-docker-version]: https://images.microbadger.com/badges/version/tomerfi/switcher_webapi.svg
[read-the-docs]: https://readthedocs.org/projects/switcher-webapi/badge/?version=stable
[requires-io]: https://requires.io/github/TomerFi/switcher_webapi/requirements.svg
[shields-io-docker-cloud-build-status]: https://img.shields.io/docker/cloud/build/tomerfi/switcher_webapi.svg
[shields-io-docker-pulls]: https://img.shields.io/docker/pulls/tomerfi/switcher_webapi.svg
[shields-io-maintenance]: https://img.shields.io/badge/Maintained%3F-yes-green.svg
