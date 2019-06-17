<!--lint disable maximum-line-length-->
# Switcher Boiler Unofficial Docker-based WebAPI

| Stage   | Badges                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Code    | [![CircleCI](https://circleci.com/gh/TomerFi/switcher_webapi.svg?style=shield)](https://circleci.com/gh/TomerFi/switcher_webapi) [![CodeCov](https://codecov.io/gh/TomerFi/switcher_webapi/graph/badge.svg)](https://codecov.io/gh/TomerFi/switcher_webapi) [![Requirements Status](https://requires.io/github/TomerFi/switcher_webapi/requirements.svg?)](https://requires.io/github/TomerFi/switcher_webapi/requirements/) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/bc33021329894d75943f8d0fe77b95a5)](https://www.codacy.com/app/TomerFi/switcher_webapi?utm_source=github.com&utm_medium=referral&utm_content=TomerFi/switcher_webapi&utm_campaign=Badge_Grade) [![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)                                                                 |
| Docs    | [![Documentation Status](https://readthedocs.org/projects/switcher-webapi/badge/?version=stable)](https://switcher-webapi.readthedocs.io/en/stable/?badge=stable)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Docker  | [![Docker Automated build](https://img.shields.io/docker/automated/tomerfi/switcher_webapi.svg)](https://hub.docker.com/r/tomerfi/switcher_webapi) [![Docker layers](https://images.microbadger.com/badges/image/tomerfi/switcher_webapi.svg)](https://microbadger.com/images/tomerfi/switcher_webapi) [![Docker version](https://images.microbadger.com/badges/version/tomerfi/switcher_webapi.svg)](https://microbadger.com/images/tomerfi/switcher_webapi) [![Docker commit](https://images.microbadger.com/badges/commit/tomerfi/switcher_webapi.svg)](https://microbadger.com/images/tomerfi/switcher_webapi) [![Docker license](https://images.microbadger.com/badges/license/tomerfi/switcher_webapi.svg)](https://microbadger.com/images/tomerfi/switcher_webapi)                                                                                                                             |
| GitHub  | [![GitHub release](https://img.shields.io/github/release/tomerfi/switcher_webapi.svg)](https://github.com/TomerFi/switcher_webapi/releases) [![Open Issues](https://img.shields.io/github/issues-raw/tomerfi/switcher_webapi.svg)](https://github.com/TomerFi/switcher_webapi/issues) [![Commit Activity Month](https://img.shields.io/github/commit-activity/m/tomerfi/switcher_webapi.svg)](https://github.com/TomerFi/switcher_webapi/commits/dev) [![Last Commit](https://img.shields.io/github/last-commit/tomerfi/switcher_webapi.svg)](https://github.com/TomerFi/switcher_webapi/commits/dev) [![GitHub language count](https://img.shields.io/github/languages/count/tomerfi/switcher_webapi.svg)](https://github.com/TomerFi/switcher_webapi) [![GitHub top language](https://img.shields.io/github/languages/top/tomerfi/switcher_webapi.svg)](https://github.com/TomerFi/switcher_webapi) |
| Project | [![GitHub License](https://img.shields.io/github/license/tomerfi/switcher_webapi.svg)](https://github.com/TomerFi/switcher_webapi/blob/dev/LICENSE) [![Slack Channel](https://slack.tomfi.info:8443/switcher_webapi.svg)](https://tomfi.slack.com/messages/CK4DK2Z5G) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/TomerFi/switcher_webapi) [![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/2891/badge)](https://bestpractices.coreinfrastructure.org/projects/2891)                                                                                                                                                                                                                                                                                                                                                    |

An asynchronous [sanic webapp](https://pypi.org/project/sanic/) running inside a [python docker image](https://hub.docker.com/_/python) using [uvloop](https://pypi.org/project/uvloop/) as the event loop.</br>
Used as a rest api wrapper for [aioswitcher](https://pypi.org/project/aioswitcher/).</br>

If you're using the [Switcher Water Heater](https://switcher.co.il/) and you want to wrap a rest api around it... you came to the right place!</br>

For full install and usage instructions,
Please check out the [Switcher water heater WebAPI documentation](https://switcher-webapi.readthedocs.io) hosted with *readthedocs.io.*
