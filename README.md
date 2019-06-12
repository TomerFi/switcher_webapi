# Switcher Boiler Unofficial Docker-based WebAPI

| Stage   | Badges                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Build   | [![CircleCI](https://circleci.com/gh/TomerFi/switcher_webapi.svg?style=shield)](https://circleci.com/gh/TomerFi/switcher_webapi) [![CodeCov](https://codecov.io/gh/TomerFi/switcher_webapi/graph/badge.svg)](https://codecov.io/gh/TomerFi/switcher_webapi) [![Requirements Status](https://requires.io/github/TomerFi/switcher_webapi/requirements.svg?)](https://requires.io/github/TomerFi/switcher_webapi/requirements/) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/bc33021329894d75943f8d0fe77b95a5)](https://www.codacy.com/app/TomerFi/switcher_webapi?utm_source=github.com&utm_medium=referral&utm_content=TomerFi/switcher_webapi&utm_campaign=Badge_Grade) [![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)                                                                 |
| Docker  | [![Docker Automated build](https://img.shields.io/docker/automated/tomerfi/switcher_webapi.svg)](https://hub.docker.com/r/tomerfi/switcher_webapi) [![Docker layers](https://images.microbadger.com/badges/image/tomerfi/switcher_webapi.svg)](https://microbadger.com/images/tomerfi/switcher_webapi) [![Docker version](https://images.microbadger.com/badges/version/tomerfi/switcher_webapi.svg)](https://microbadger.com/images/tomerfi/switcher_webapi) [![Docker commit](https://images.microbadger.com/badges/commit/tomerfi/switcher_webapi.svg)](https://microbadger.com/images/tomerfi/switcher_webapi) [![Docker license](https://images.microbadger.com/badges/license/tomerfi/switcher_webapi.svg)](https://microbadger.com/images/tomerfi/switcher_webapi)                                                                                                                             |
| GitHub  | [![GitHub release](https://img.shields.io/github/release/tomerfi/switcher_webapi.svg)](https://github.com/TomerFi/switcher_webapi/releases) [![Open Issues](https://img.shields.io/github/issues-raw/tomerfi/switcher_webapi.svg)](https://github.com/TomerFi/switcher_webapi/issues) [![Commit Activity Month](https://img.shields.io/github/commit-activity/m/tomerfi/switcher_webapi.svg)](https://github.com/TomerFi/switcher_webapi/commits/dev) [![Last Commit](https://img.shields.io/github/last-commit/tomerfi/switcher_webapi.svg)](https://github.com/TomerFi/switcher_webapi/commits/dev) [![GitHub language count](https://img.shields.io/github/languages/count/tomerfi/switcher_webapi.svg)](https://github.com/TomerFi/switcher_webapi) [![GitHub top language](https://img.shields.io/github/languages/top/tomerfi/switcher_webapi.svg)](https://github.com/TomerFi/switcher_webapi) |
| Project | [![GitHub License](https://img.shields.io/github/license/tomerfi/switcher_webapi.svg)](https://github.com/TomerFi/switcher_webapi/blob/dev/LICENSE) [![Slack Channel](https://slack.tomfi.info:8443/switcher_webapi.svg)](https://tomfi.slack.com/messages/CK4DK2Z5G) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/TomerFi/switcher_webapi)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

An asynchronous [sanic webapp](https://pypi.org/project/sanic/) running inside a [python docker image](https://hub.docker.com/_/python) using [uvloop](https://pypi.org/project/uvloop/) as the event loop.</br>
Used as a rest api wrapper for [aioswitcher](https://pypi.org/project/aioswitcher/).</br>
If you're using the [Switcher Water Heater](https://switcher.co.il/) and you want to wrap a rest api around it... you came to the right place!</br>
</br>

## Prerequisites

- Install and configure your Switcher device.
- Collect the following information from the device's following NightRang3r instructions in the [Switcher-V2-Python](https://github.com/NightRang3r/Switcher-V2-Python) repository:
  - ip_address
  - phone_id
  - device_id
  - device_pass
- Install docker.

## Please note

- If you don't want to be forced to restart the container if the device's ip address changes, please consider assigning the device with a static ip address.
- The Switcher-V2-Python repository is build with python 2.7.
- The [aioswitcher](https://github.com/TomerFi/aioswitcher) was tested with the Switcher V2 device by myself and with the Switcher Touch device by the community.
- This project was intended for local usage, it's ok if you want to use it remotely, just make sure to take the proper security measures such as reverse proxy and ssl.
- The WebAPI has a throttle mechanism to prevent overfloating the device with frequent requests, it defaults to 5 seconds throttle time.
- Some users have been reporting lately about failures using the Switcher-V2-Python script after upgrading the device firmware to 3.0, please follow the relevant issues in the script repository before doing the same.

## Install

```shell
docker run -d -p 8000:8000 \
-e CONF_DEVICE_IP_ADDR=192.168.100.157 \
-e CONF_PHONE_ID=1234 \
-e CONF_DEVICE_ID=ab1c2d \
-e CONF_DEVICE_PASSWORD=12345678 \
--name switcher_webapi tomerfi/switcher_webapi:latest"
```

You can also add another optional environment variable, `-e CONF_THROTTLE=5.0` for setting the throttle time between consecutive requests, this is optional and the default value is `5.0`.</br>

Here's an example of running the container using `docker-compose` setting the environment variables in a designated file.

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

## Usage

Once running, you can send REST requests towards the container. </br>

With the exception of the `create_schedule` requests, all the requests requiring input can take it as a json body or in the form of query parameters.</br>
</br>

### /switcher/get_state

**Method:** `GET`</br>
**Request parameters:** `None`</br>
**Response body example:**

```json
{
  "successful": true,
  "state": "on",
  "time_left": "00:47:25",
  "auto_off": "01:30:00",
  "power_consumption": 2669,
  "electric_current": 12.3
}
```

</br>

### /switcher/turn_on

**Method:** `POST`</br>
**Request parameters:**

| Key       | Required     | Description                                            |
| --------- | ------------ | ------------------------------------------------------ |
| `minutes` | **Optional** | turn on the device with an off timer of 1-180 minutes. |

**Request body example:**

```json
{
  "minutes": "30"
}
```

**Response body example:**

```json
{
  "successful": true
}
```

</br>

### /switcher/turn_off

**Method:** `POST`</br>
**Request parameters:** `None`</br>
**Response body example:**

```json
{
  "successful": true
}
```

</br>

### /switcher/set_auto_shutdown

**Method: POST**</br>
**Request parameters:**

| Key       | Required      | Description         |
| --------- | ------------- | ------------------- |
| `hours`   | **Mandatory** | hours value 1-3.    |
| `minutes` | **Mandatory** | minutes value 0-59. |

_Please note_, the auto shutdown configuration value accept any total value of hours and minutes between 1 and 3 hours.
</br>

**Request body example:**

```json
{
  "hours": "1",
  "minutes": "30"
}
```

**Response body example:**

```json
{
  "successful": true
}
```

</br>

### /switcher/set_device_name

**Method: POST**</br>
**Request parameters:**

| Key    | Required      | Description                                     |
| ------ | ------------- | ----------------------------------------------- |
| `name` | **Mandatory** | device name, accepts length of 2-32 characters. |

**Request body example:**

```json
{
  "name": "my new device name"
}
```

**Response body example:**

```json
{
  "successful": true
}
```

</br>

### /switcher/get_schedules

**Method: GET**</br></br>
**Request parameters:** `None`</br>
**Response body example:**

```json
{
  "successful": true,
  "found_schedules": true,
  "schedules": [
    {
      "schedule_id": "0",
      "enabled": true,
      "recurring": true,
      "days": [
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ],
      "start_time": "17:30",
      "end_time": "18:30",
      "duration": "1:00:00",
      "schedule_data": "0001fc01e871a35cf87fa35c",
      "next_run": "Due next Tuesday at 17:30"
    },
    {
      "schedule_id": "1",
      "enabled": true,
      "recurring": true,
      "days": ["Monday"],
      "start_time": "17:00",
      "end_time": "18:00",
      "duration": "1:00:00",
      "schedule_data": "0101020160a6c95c70b4c95c",
      "next_run": "Due tommorow at 17:00"
    }
  ]
}
```

_Please note_, the `schedules` list can contain up to 8 schedules with the identifiers of 0-7 representing the actual schedule slots on the device.</br>
</br>

### /switcher/enable_schedule

**Method: PATCH**</br>
**Request parameters:**

| Key             | Requiered     | Description                                                                                         |
| --------------- | ------------- | --------------------------------------------------------------------------------------------------- |
| `schedule_data` | **Mandatory** | the `schedule_data` associated with the chosen schedule (retrieved with `/switcher/get_schedules`). |

**Request body example:**

```json
{
  "schedule_data": "0101020160a6c95c70b4c95c"
}
```

**Response body example:**

```json
{
  "successful": true
}
```

</br>

### /switcher/disable_schedule

**Method: PATCH**</br>
**Request parameters:**

| Key             | Requiered     | Description                                                                                         |
| --------------- | ------------- | --------------------------------------------------------------------------------------------------- |
| `schedule_data` | **Mandatory** | the `schedule_data` associated with the chosen schedule (retrieved with `/switcher/get_schedules`). |

**Request body example:**

```json
{
  "schedule_data": "0101020160a6c95c70b4c95c"
}
```

**Response body example:**

```json
{
  "successful": true
}
```

</br>

### /switcher/delete_schedule

**Method: DELETE**</br>
**Request parameters:**

| Key           | Requiered     | Description                                                                                       |
| ------------- | ------------- | ------------------------------------------------------------------------------------------------- |
| `schedule_id` | **Mandatory** | the `schedule_id` associated with the chosen schedule (retrieved with `/switcher/get_schedules`). |

**Request body example:**

```json
{
  "schedule_id": "2"
}
```

**Response body example:**

```json
{
  "successful": true
}
```

</br>

### /switcher/create_schedule

**Method: PUT**</br>
**Request parameters:**

| Key             | Requiered     | Description                                                                    |
| --------------- | ------------- | ------------------------------------------------------------------------------ |
| `days`          | **Mandatory** | a list of days for the schedule to run in (empty for non-recurring schedules). |
| `start_hours`   | **Mandatory** | start time hours value 0-23.                                                   |
| `start_minutes` | **Mandatory** | start minutes value 0-59.                                                      |
| `stop_hours`    | **Mandatory** | stop time hours value 0-23.                                                    |
| `stop_minutes`  | **Mandatory** | stop minutes value 0-59.                                                       |

**Request body example:**

```json
{
  "days": ["Monday", "Wednesday", "Friday"],
  "start_hours": "20",
  "start_minutes": "30",
  "stop_hours": "21",
  "stop_minutes": "0"
}
```

**Response body example:**

```json
{
  "successful": true
}
```

Possible values for the `days` list:

- `Sunday`
- `Monday`
- `Tuesday`
- `Wednesday`
- `Thursday`
- `Friday`
- `Saturday`
  </br>

_Please note_, due to its complexity, the `create_schedule` request can take its input in the form of a json body only, query parameters will not be accepted.</br>
</br>

### Exceptions

Unless unhandled, all exceptions will return a json object in response body:

```json
{
  "successful": false,
  "message": "the error description"
}
```

## Worth Mentioning

- This project was enabled by creating the [aioswitcher pypi module](https://pypi.org/project/aioswitcher/), initially created for use with the [Home Assistant Component](https://www.home-assistant.io/components/switcher_kis).
- Not this nor would the aioswitcher project would have been able to happen without the amazing work preformed by @NightRang3r and @AviadGolan in the [Switcher-V2-Python project](https://github.com/NightRang3r/Switcher-V2-Python).
