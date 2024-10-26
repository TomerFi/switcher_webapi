## Schedule Endpoints

### ==Get Schedules==

| Method | Endpoint                | Description                                         |
|:-------|:------------------------|:----------------------------------------------------|
| GET    | /switcher/get_schedules | Returns an array of schedule objects from a device. |

--8<-- "query_params.md"

**Schedule Object**

| Key         | Type      | Example                  |
|:------------|:----------|:-------------------------|
| schedule_id | string    | 0                        |
| recurring   | boolean   | true                     |
| days        | [string]  | [FRIDAY, SUNDAY, MONDAY] |
| start_time  | string    | 23:30                    |
| duration    | string    | 0:30:00                  |
| display     | string    | Due next Friday at 23:00 |

### ==Delete a Schedule==

| Method | Endpoint                  | Description                            |
|:-------|:--------------------------|:---------------------------------------|
| DELETE | /switcher/delete_schedule | Delete a known schedule from a device. |

--8<-- "query_params.md"

**Body**

| Key       | Type   | Required | Example |
|:----------|:-------|:---------|---------|
| schedule  | string | Yes      | 7       |

### ==Create a Schedule==

| Method | Endpoint                  | Description                        |
|:-------|:--------------------------|:-----------------------------------|
| POST   | /switcher/create_schedule | Create a new schedule on a device. |

--8<-- "query_params.md"

**Body**

| Key     | Type     | Required | Example               |
|:--------|:---------|:---------|-----------------------|
| start   | string   | Yes      | 17:00                 |
| stop    | string   | Yes      | 18:30                 |
| days    | [string] | No       | [Wednesday, Saturday] |
