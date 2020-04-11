# Switcher Boiler Unofficial REST API</br>[![shields-io-docker-version]][10] [![shields-io-docker-pulls]][10]

[![gh-python-status]][2] [![gh-docker-status]][5]</br>
[![read-the-docs]][4] [![codecov]][0] [![dependabot-status]][1]

REST API web server using [aioswitcher](https://pypi.org/project/aioswitcher/) for integrating with
the [Switcher Water Heater](https://www.switcher.co.il/).</br>
Please check out the [documentation][4].

## Docker

```shell
docker run -d -p 8000:8000 \
-e CONF_DEVICE_IP_ADDR=192.168.100.157 \
-e CONF_PHONE_ID=1234 \
-e CONF_DEVICE_ID=ab1c2d \
-e CONF_DEVICE_PASSWORD=12345678 \
--name switcher_webapi tomerfi/switcher_webapi:latest"
```

You can also add another optional environment variable:

```shell
-e CONF_THROTTLE=5.0
```

for setting the throttle time between consecutive requests,
this is optional and the default value is **5.0**.

## Docker Compose

Here's an example of running the container using *docker-compose* setting the
environment variables in a designated file.

```yaml
# docker-compose.yml
version: "3.7"

services:
    switcher_api:
    image: tomerfi/switcher_webapi:latest
    container_name: "switcher_webapi"
    env_file:
        - .env_vars
    ports:
        - 8000:8000
    restart: unless-stopped
```

```ini
# .env_vars
CONF_DEVICE_IP_ADDR=192.168.100.157
CONF_PHONE_ID=1234
CONF_DEVICE_ID=ab1c2d
CONF_DEVICE_PASSWORD=12345678
CONF_THROTTLE=5.0
```

## Contributing

The contributing guidlines are [here](.github/CONTRIBUTING.md)

## Code of Conduct

The code of conduct is [here](.github/CODE_OF_CONDUCT.md)

<!-- Real Links -->
[0]: https://codecov.io/gh/TomerFi/switcher_webapi
[1]: https://dependabot.com
[2]: https://github.com/TomerFi/switcher_webapi/actions?query=workflow%PythonTest
[4]: https://switcher-webapi.tomfi.info
[5]: https://github.com/TomerFi/switcher_webapi/actions?query=workflow%DockerTest
[10]: https://hub.docker.com/r/tomerfi/switcher_webapi
<!-- Badges Links -->
[codecov]: https://codecov.io/gh/TomerFi/switcher_webapi/graph/badge.svg
[dependabot-status]: https://api.dependabot.com/badges/status?host=github&repo=TomerFi/switcher_webapi
[gh-docker-status]: https://github.com/TomerFi/switcher_webapi/workflows/DockerTest/badge.svg
[gh-python-status]: https://github.com/TomerFi/switcher_webapi/workflows/PythonTest/badge.svg
[read-the-docs]: https://readthedocs.org/projects/switcher-webapi/badge/?version=latest
[shields-io-docker-pulls]: https://img.shields.io/docker/pulls/tomerfi/switcher_webapi.svg?logo=docker&label=pulls
[shields-io-docker-version]: https://img.shields.io/docker/v/tomerfi/switcher_webapi?color=%230A6799&logo=docker
