# Switcher Web API</br>[![docker-version]][1] [![docker-pulls]][1] [![license-badge]][3]

[![gh-build-status]][2] [![gh-pages-status]][4] [![codecov]][0]

Containerized web service integrating with various [Switcher][5] smart devices.

## Install

```shell
docker run -d -p 8000:8000 --name switcher_webapi tomerfi/switcher_webapi:latest
```

## Links

- [aioswitcher's wiki pages][6] for a list of supported devices.
- [aioswitcher's discovery script][7] for discovering devices on your network.
- [documentation site][4] for a more detailed usage section.
- [wiki pages][8] for additional information.

## Usage Examples

### Get State

Get the current state of a device.

Request:

```http
GET http://localhost:8000/switcher/get_state?id=ab1c2d&ip=1.2.3.4
```

Response:

```json
{
  "state": "ON",
  "time_left": "00:09:57",
  "time_on": "00:35:03",
  "auto_shutdown": "02:30:00",
  "power_consumption": 2623,
  "electric_current": 11.9
}
```

### Turn On

Turn on without a timer:

```http
POST http://localhost:8000/switcher/turn_on?id=ab1c2d&ip=1.2.3.4
```

Turn on with a 15 minutes timer:

```http
POST http://localhost:8000/switcher/turn_on?id=ab1c2d&ip=1.2.3.4
Content-Type: "application/json"

{
    "minutes": 15
}
```

### Turn Off

Turn off a device:

```http
POST http://localhost:8000/switcher/turn_off?id=ab1c2d&ip=1.2.3.4
```

### Set Auto Shutdown

Set the auto shutdown value to 3 hours:

```http
PATCH http://localhost:8000/switcher/set_auto_shutdown?id=ab1c2d&ip=1.2.3.4
Content-Type: "application/json"

{
    "hours": 3
}
```

Set the auto shutdown value to 2 hours and 30 minutes:

```http
PATCH http://localhost:8000/switcher/set_auto_shutdown?id=ab1c2d&ip=1.2.3.4
Content-Type: "application/json"

{
    "hours": 2,
    "minutes": 30
}
```

### Set Name

Set the device's name to MySwitcher:

```http
PATCH http://localhost:8000/switcher/set_name?id=ab1c2d&ip=1.2.3.4
Content-Type: "application/json"

{
    "name": "MySwitcher"
}
```

### Create a Schedule

Create a non-recurring schedule for 17:00-18:30:

```http
POST http://localhost:8000/switcher/create_schedule?id=ab1c2d&ip=1.2.3.4
Content-Type: "application/json"

{
    "start": "17:00",
    "stop": "18:30"
}
```

Create a recurring schedule for 23:00-23:30 on Sunday, Monday, and Friday:

```http
POST http://localhost:8000/switcher/create_schedule?id=ab1c2d&ip=1.2.3.4
Content-Type: "application/json"

{
    "start": "23:00",
    "stop": "23:30",
    "days": ["Sunday", "Monday", "Friday"]
}
```

### Delete a Schedule

Delete schedule id 7:

```http
DELETE http://localhost:8000/switcher/delete_schedule?id=ab1c2d&ip=1.2.3.4
Content-Type: "application/json"

{
    "schedule": "7"
}
```

### Get Schdeules

Get the schedules information from a device.

Request:

```http
GET http://localhost:8000/switcher/get_schedules?id=ab1c2d&ip=1.2.3.4
```

Response:

```json
[
  {
    "schedule_id": "0",
    "recurring": true,
    "days": [
      "SUNDAY",
      "FRIDAY",
      "MONDAY"
    ],
    "start_time": "23:00",
    "end_time": "23:30",
    "duration": "0:30:00",
    "display": "Due next Friday at 23:00"
  },
  {
    "schedule_id": "1",
    "recurring": false,
    "days": [],
    "start_time": "17:00",
    "end_time": "18:30",
    "duration": "1:30:00",
    "display": "Due today at 17:00"
  }
]
```

## Contributing

The contributing guidelines are [here][9]

## Code of Conduct

The code of conduct is [here][10]

## Thanks

- Designing and testing by [Shay][11].
- Testing, support, and community procedures by [Dima][12].

<!-- Real Links -->
[0]: https://codecov.io/gh/TomerFi/switcher_webapi
[1]: https://hub.docker.com/r/tomerfi/switcher_webapi
[2]: https://github.com/TomerFi/switcher_webapi/actions/workflows/pre_release.yml
[3]: https://github.com/TomerFi/switcher_webapi
[4]: https://switcher-webapi.tomfi.info
[5]: https://www.switcher.co.il/
[6]: https://github.com/TomerFi/aioswitcher/wiki
[7]: https://github.com/TomerFi/aioswitcher/blob/dev/scripts/discover_devices.py
[8]: https://github.com/TomerFi/switcher_webapi/wiki
[9]: https://github.com/TomerFi/switcher_webapi/blob/dev/.github/CONTRIBUTING.md
[10]: https://github.com/TomerFi/switcher_webapi/blob/dev/.github/CODE_OF_CONDUCT.md
[11]: https://github.com/thecode
[12]: https://github.com/dmatik
<!-- Badges Links -->
[codecov]: https://codecov.io/gh/TomerFi/switcher_webapi/graph/badge.svg
[docker-pulls]: https://img.shields.io/docker/pulls/tomerfi/switcher_webapi.svg?logo=docker&label=pulls
[docker-version]: https://img.shields.io/docker/v/tomerfi/switcher_webapi?color=%230A6799&logo=docker
[gh-build-status]: https://github.com/TomerFi/switcher_webapi/actions/workflows/pre_release.yml/badge.svg
[gh-pages-status]: https://github.com/TomerFi/switcher_webapi/actions/workflows/pages_deploy.yml/badge.svg
[license-badge]: https://img.shields.io/github/license/tomerfi/switcher_webapi
