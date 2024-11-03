# Switcher Web API

[![version-badge]][dockerhub]
[![pulls-badge]][dockerhub]
[![license-badge]][license]<br/>
[![stage-badge]][stage]
[![pages-badge]][pages]
[![codecov-badge]][codecov]

Gain access to your local [Switcher][switcher] smart devices.

```shell
docker run -d -p 8000:8000 --name switcher_webapi tomerfi/switcher_webapi:latest
```

Check the docs: [https://switcher-webapi.tomfi.info][docs].

> [!IMPORTANT]  
> Since version 2, all endpoints require a device type. See [docs][docs].

<!-- Links -->
[codecov]: https://codecov.io/gh/TomerFi/switcher_webapi
[docs]: https://switcher-webapi.tomfi.info
[dockerhub]: https://hub.docker.com/r/tomerfi/switcher_webapi
[license]: https://github.com/TomerFi/switcher_webapi/blob/dev/LICENSE
[pages]: https://github.com/TomerFi/switcher_webapi/actions/workflows/pages.yml
[stage]: https://github.com/TomerFi/switcher_webapi/actions/workflows/stage.yml
[switcher]: https://www.switcher.co.il/
<!-- Badges -->
[codecov-badge]: https://codecov.io/gh/TomerFi/switcher_webapi/graph/badge.svg
[license-badge]: https://img.shields.io/github/license/tomerfi/switcher_webapi
[pages-badge]: https://github.com/TomerFi/switcher_webapi/actions/workflows/pages.yml/badge.svg
[pulls-badge]: https://img.shields.io/docker/pulls/tomerfi/switcher_webapi.svg?logo=docker&label=pulls
[stage-badge]: https://github.com/TomerFi/switcher_webapi/actions/workflows/stage.yml/badge.svg
[version-badge]: https://img.shields.io/docker/v/tomerfi/switcher_webapi?color=%230A6799&logo=docker

