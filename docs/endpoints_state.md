## State Endpoints

### ==Get State==

| Method | Endpoint            | Description                            |
|:-------|:--------------------|:---------------------------------------|
| GET    | /switcher/get_state | Returns the current state of a device. | 

--8<-- "query_params.md"

**State Response**

| Key               | Type    | Example  |
|:------------------|:--------|:---------|
| state             | string  | ON       |
| time_left         | string  | 01:15:32 |
| time_on           | string  | 00:14:28 |
| auto_shutdown     | string  | 02:30:00 |
| power_consumption | string  | 1274     |
| electric_current  | string  | 16.4     |

### ==Get Breeze State==

| Method | Endpoint                   | Description                                    |
|:-------|:---------------------------|:-----------------------------------------------|
| GET    | /switcher/get_breeze_state | Returns the current state of Breeze devices.   |

--8<-- "query_params.md"

**Breeze State Response**

| Key                | Type    | Example  |
|:-------------------|:--------|:---------|
| state              | string  | ON       |
| mode               | string  | COOL     |
| fan_level          | string  | AUTO     |
| temperature        | integer | 9.5      |
| target_temperature | string  | 0,       |
| swing              | string  | ON       |
| remote_id          | string  | DLK65863 |

### ==Get Shutter State==

| Method | Endpoint                    | Description                                   |
|:-------|:----------------------------|:----------------------------------------------|
| GET    | /switcher/get_shutter_state | Returns the current state of Shutter devices. |

--8<-- "query_params.md"

### ==Get Light State==

| Method | Endpoint                    | Description                                   |
|:-------|:----------------------------|:----------------------------------------------|
| GET    | /switcher/get_light_state | Returns the current state of Light devices. |

--8<-- "query_params.md"

**Shutter State Response**

| Key       | Type    | Example      |
|:----------|:--------|:-------------|
| direction | string  | SHUTTER_STOP |
| position  | integer | 95           |

