## Configuration Endpoints

### ==Set Name==

| Method | Endpoint           | Description               |
|:-------|:-------------------|:--------------------------|
| PATCH  | /switcher/set_name | Set the name of a device. |

--8<-- "query_params.md"

**Body**

| Key  | Type   | Required | Example          |
|:-----|:-------|:---------|------------------|
| name | string | Yes      | MySwitcherDevice |

### ==Set Auto Shutdown==

| Method | Endpoint                    | Description                                       |
|:-------|:----------------------------|:--------------------------------------------------|
| PATCH  | /switcher/set_auto_shutdown | Set the auto shutdown configuration for a device. |

--8<-- "query_params.md"

**Body**

| Key     | Type    | Required | Example |
|:--------|:--------|:---------|---------|
| hours   | integer | Yes      | 2       |
| minutes | integer | No       | 30      |

### ==Set Shutter Position==

| Method | Endpoint                       | Description                                                     |
|:-------|:-------------------------------|:----------------------------------------------------------------|
| POST   | /switcher/set_shutter_position | Set the shutter position of the Runner and Runner Mini devices. |

--8<-- "query_params.md"

**Body**

| Key       | Type   | Required | Example |
|:----------|:-------|:---------|---------|
| position  | string | Yes      | 50      |
