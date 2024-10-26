## Action Endpoints

### ==Turn On==

| Method | Endpoint          | Description                                                                         |
|:-------|:------------------|:------------------------------------------------------------------------------------|
| POST   | /switcher/turn_on | Turn a device on, optionally setting a timer for turning it back off automatically. |

--8<-- "query_params.md"

**Body**

| Key     | Type    | Required | Example |
|:--------|:--------|:---------|---------|
| minutes | integer | No       | 90      |

### ==Turn Off==

| Method | Endpoint           | Description        |
|:-------|:-------------------|:-------------------|
| POST   | /switcher/turn_off | Turn a device off. |

--8<-- "query_params.md"

### ==Stop Shutter==

| Method | Endpoint                   | Description            |
|:-------|:---------------------------|:-----------------------|
| POST   | /switcher/set_stop_shutter | Stop a shutter device. |

--8<-- "query_params.md"

### ==Control Breeze==

| Method | Endpoint                        | Description                 |
|:-------|:--------------------------------|:----------------------------|
| POST   | /switcher/control_breeze_device | Control a breeze device.    |

--8<-- "query_params.md"

**Body**

| Key              | Type    | Required | Example  |
|:-----------------|:--------|:---------|----------|
| device_state     | string  | No       | on       |
| thermostat_mode  | string  | No       | auto     |
| target_temp      | integer | No       | 25       |
| fan_level        | string  | No       | low      |
| thermostat_swing | string  | No       | off      |
| remote_id        | string  | Yes      | DLK65863 |

