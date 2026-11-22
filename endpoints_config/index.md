## Configuration Endpoints

### Set Name

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| PATCH | /switcher/set\_name | Set the name of a device. |

**Query Params**

| Param | Type | Description | Required | Example |
| :--- | :--- | :--- | :--- | :--- |
| type | [Device Type](<https://switcher-webapi.figenblat.com/device_types/index.md>) | the type of the selected device | Yes | mini |
| id | string | the id of the selected device | Yes | ab1c2d |
| key | string | the login key of the selected device | No | 18 |
| ip | string | the ip address of the selected device | Yes | 10.0.0.1 |
| index | integer | the circuit number to operate | No | 0 |
| token | string | the user token from Switcher API | No | zvVvd7JxtN7CgvkD1Psujw== |

**Body**

| Key | Type | Required | Example |
| :--- | :--- | :--- | --- |
| name | string | Yes | MySwitcherDevice |

### Set Auto Shutdown

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| PATCH | /switcher/set\_auto\_shutdown | Set the auto shutdown configuration for a device. |

**Query Params**

| Param | Type | Description | Required | Example |
| :--- | :--- | :--- | :--- | :--- |
| type | [Device Type](<https://switcher-webapi.figenblat.com/device_types/index.md>) | the type of the selected device | Yes | mini |
| id | string | the id of the selected device | Yes | ab1c2d |
| key | string | the login key of the selected device | No | 18 |
| ip | string | the ip address of the selected device | Yes | 10.0.0.1 |
| index | integer | the circuit number to operate | No | 0 |
| token | string | the user token from Switcher API | No | zvVvd7JxtN7CgvkD1Psujw== |

**Body**

| Key | Type | Required | Example |
| :--- | :--- | :--- | --- |
| hours | integer | Yes | 2 |
| minutes | integer | No | 30 |

### Set Shutter Position

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | /switcher/set\_shutter\_position | Set the shutter position of the Runner and Runner Mini devices. |

**Query Params**

| Param | Type | Description | Required | Example |
| :--- | :--- | :--- | :--- | :--- |
| type | [Device Type](<https://switcher-webapi.figenblat.com/device_types/index.md>) | the type of the selected device | Yes | mini |
| id | string | the id of the selected device | Yes | ab1c2d |
| key | string | the login key of the selected device | No | 18 |
| ip | string | the ip address of the selected device | Yes | 10.0.0.1 |
| index | integer | the circuit number to operate | No | 0 |
| token | string | the user token from Switcher API | No | zvVvd7JxtN7CgvkD1Psujw== |

**Body**

| Key | Type | Required | Example |
| :--- | :--- | :--- | --- |
| position | string | Yes | 50 |
