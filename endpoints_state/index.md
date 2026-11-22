## State Endpoints

### Get State

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | /switcher/get\_state | Returns the current state of a device. |

**Query Params**

| Param | Type | Description | Required | Example |
| :--- | :--- | :--- | :--- | :--- |
| type | [Device Type](<https://switcher-webapi.figenblat.com/device_types/index.md>) | the type of the selected device | Yes | mini |
| id | string | the id of the selected device | Yes | ab1c2d |
| key | string | the login key of the selected device | No | 18 |
| ip | string | the ip address of the selected device | Yes | 10.0.0.1 |
| index | integer | the circuit number to operate | No | 0 |
| token | string | the user token from Switcher API | No | zvVvd7JxtN7CgvkD1Psujw== |

**State Response**

| Key | Type | Example |
| :--- | :--- | :--- |
| state | string | ON |
| time\_left | string | 01:15:32 |
| time\_on | string | 00:14:28 |
| auto\_shutdown | string | 02:30:00 |
| power\_consumption | string | 1274 |
| electric\_current | string | 16.4 |

### Get Breeze State

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | /switcher/get\_breeze\_state | Returns the current state of Breeze devices. |

**Query Params**

| Param | Type | Description | Required | Example |
| :--- | :--- | :--- | :--- | :--- |
| type | [Device Type](<https://switcher-webapi.figenblat.com/device_types/index.md>) | the type of the selected device | Yes | mini |
| id | string | the id of the selected device | Yes | ab1c2d |
| key | string | the login key of the selected device | No | 18 |
| ip | string | the ip address of the selected device | Yes | 10.0.0.1 |
| index | integer | the circuit number to operate | No | 0 |
| token | string | the user token from Switcher API | No | zvVvd7JxtN7CgvkD1Psujw== |

**Breeze State Response**

| Key | Type | Example |
| :--- | :--- | :--- |
| state | string | ON |
| mode | string | COOL |
| fan\_level | string | AUTO |
| temperature | integer | 9.5 |
| target\_temperature | string | 0, |
| swing | string | ON |
| remote\_id | string | DLK65863 |

### Get Shutter State

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | /switcher/get\_shutter\_state | Returns the current state of Shutter devices. |

**Query Params**

| Param | Type | Description | Required | Example |
| :--- | :--- | :--- | :--- | :--- |
| type | [Device Type](<https://switcher-webapi.figenblat.com/device_types/index.md>) | the type of the selected device | Yes | mini |
| id | string | the id of the selected device | Yes | ab1c2d |
| key | string | the login key of the selected device | No | 18 |
| ip | string | the ip address of the selected device | Yes | 10.0.0.1 |
| index | integer | the circuit number to operate | No | 0 |
| token | string | the user token from Switcher API | No | zvVvd7JxtN7CgvkD1Psujw== |

**Shutter State Response**

| Key | Type | Example |
| :--- | :--- | :--- |
| direction | string | SHUTTER\_STOP |
| position | integer | 95 |

### Get Light State

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | /switcher/get\_light\_state | Returns the current state of Light devices. |

**Query Params**

| Param | Type | Description | Required | Example |
| :--- | :--- | :--- | :--- | :--- |
| type | [Device Type](<https://switcher-webapi.figenblat.com/device_types/index.md>) | the type of the selected device | Yes | mini |
| id | string | the id of the selected device | Yes | ab1c2d |
| key | string | the login key of the selected device | No | 18 |
| ip | string | the ip address of the selected device | Yes | 10.0.0.1 |
| index | integer | the circuit number to operate | No | 0 |
| token | string | the user token from Switcher API | No | zvVvd7JxtN7CgvkD1Psujw== |
