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

## Action Endpoints

### Turn On

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | /switcher/turn\_on | Turn a device on, optionally setting a timer for turning it back off automatically. |

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
| minutes | integer | No | 90 |

### Turn Off

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | /switcher/turn\_off | Turn a device off. |

**Query Params**

| Param | Type | Description | Required | Example |
| :--- | :--- | :--- | :--- | :--- |
| type | [Device Type](<https://switcher-webapi.figenblat.com/device_types/index.md>) | the type of the selected device | Yes | mini |
| id | string | the id of the selected device | Yes | ab1c2d |
| key | string | the login key of the selected device | No | 18 |
| ip | string | the ip address of the selected device | Yes | 10.0.0.1 |
| index | integer | the circuit number to operate | No | 0 |
| token | string | the user token from Switcher API | No | zvVvd7JxtN7CgvkD1Psujw== |

### Turn On Shutter Child Lock

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | /switcher/turn\_on\_shutter\_child\_lock | Turn a shutter child lock on. |

**Query Params**

| Param | Type | Description | Required | Example |
| :--- | :--- | :--- | :--- | :--- |
| type | [Device Type](<https://switcher-webapi.figenblat.com/device_types/index.md>) | the type of the selected device | Yes | mini |
| id | string | the id of the selected device | Yes | ab1c2d |
| key | string | the login key of the selected device | No | 18 |
| ip | string | the ip address of the selected device | Yes | 10.0.0.1 |
| index | integer | the circuit number to operate | No | 0 |
| token | string | the user token from Switcher API | No | zvVvd7JxtN7CgvkD1Psujw== |

### Turn Off Shutter Child Lock

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | /switcher/turn\_off\_shutter\_child\_lock | Turn a shutter child lock off. |

**Query Params**

| Param | Type | Description | Required | Example |
| :--- | :--- | :--- | :--- | :--- |
| type | [Device Type](<https://switcher-webapi.figenblat.com/device_types/index.md>) | the type of the selected device | Yes | mini |
| id | string | the id of the selected device | Yes | ab1c2d |
| key | string | the login key of the selected device | No | 18 |
| ip | string | the ip address of the selected device | Yes | 10.0.0.1 |
| index | integer | the circuit number to operate | No | 0 |
| token | string | the user token from Switcher API | No | zvVvd7JxtN7CgvkD1Psujw== |

### Turn On Light

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | /switcher/turn\_on\_light | Turn a light device on. |

**Query Params**

| Param | Type | Description | Required | Example |
| :--- | :--- | :--- | :--- | :--- |
| type | [Device Type](<https://switcher-webapi.figenblat.com/device_types/index.md>) | the type of the selected device | Yes | mini |
| id | string | the id of the selected device | Yes | ab1c2d |
| key | string | the login key of the selected device | No | 18 |
| ip | string | the ip address of the selected device | Yes | 10.0.0.1 |
| index | integer | the circuit number to operate | No | 0 |
| token | string | the user token from Switcher API | No | zvVvd7JxtN7CgvkD1Psujw== |

### Turn Off Light

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | /switcher/turn\_off\_light | Turn a light device off. |

**Query Params**

| Param | Type | Description | Required | Example |
| :--- | :--- | :--- | :--- | :--- |
| type | [Device Type](<https://switcher-webapi.figenblat.com/device_types/index.md>) | the type of the selected device | Yes | mini |
| id | string | the id of the selected device | Yes | ab1c2d |
| key | string | the login key of the selected device | No | 18 |
| ip | string | the ip address of the selected device | Yes | 10.0.0.1 |
| index | integer | the circuit number to operate | No | 0 |
| token | string | the user token from Switcher API | No | zvVvd7JxtN7CgvkD1Psujw== |

### Stop Shutter

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | /switcher/stop\_shutter | Stop a shutter device. |

**Query Params**

| Param | Type | Description | Required | Example |
| :--- | :--- | :--- | :--- | :--- |
| type | [Device Type](<https://switcher-webapi.figenblat.com/device_types/index.md>) | the type of the selected device | Yes | mini |
| id | string | the id of the selected device | Yes | ab1c2d |
| key | string | the login key of the selected device | No | 18 |
| ip | string | the ip address of the selected device | Yes | 10.0.0.1 |
| index | integer | the circuit number to operate | No | 0 |
| token | string | the user token from Switcher API | No | zvVvd7JxtN7CgvkD1Psujw== |

### Control Breeze

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| PATCH | /switcher/control\_breeze\_device | Control a breeze device. |

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
| device\_state | string | No | on |
| thermostat\_mode | string | No | auto |
| target\_temp | integer | No | 25 |
| fan\_level | string | No | low |
| thermostat\_swing | string | No | off |
| remote\_id | string | Yes | DLK65863 |

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

## Schedule Endpoints

### Get Schedules

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | /switcher/get\_schedules | Returns an array of schedule objects from a device. |

**Query Params**

| Param | Type | Description | Required | Example |
| :--- | :--- | :--- | :--- | :--- |
| type | [Device Type](<https://switcher-webapi.figenblat.com/device_types/index.md>) | the type of the selected device | Yes | mini |
| id | string | the id of the selected device | Yes | ab1c2d |
| key | string | the login key of the selected device | No | 18 |
| ip | string | the ip address of the selected device | Yes | 10.0.0.1 |
| index | integer | the circuit number to operate | No | 0 |
| token | string | the user token from Switcher API | No | zvVvd7JxtN7CgvkD1Psujw== |

**Schedule Object**

| Key | Type | Example |
| :--- | :--- | :--- |
| schedule\_id | string | 0 |
| recurring | boolean | true |
| days | \[string\] | \[FRIDAY, SUNDAY, MONDAY\] |
| start\_time | string | 23:30 |
| duration | string | 0:30:00 |
| display | string | Due next Friday at 23:00 |

### Delete a Schedule

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| DELETE | /switcher/delete\_schedule | Delete a known schedule from a device. |

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
| schedule | string | Yes | 7 |

### Create a Schedule

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | /switcher/create\_schedule | Create a new schedule on a device. |

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
| start | string | Yes | 17:00 |
| stop | string | Yes | 18:30 |
| days | \[string\] | No | \[Wednesday, Saturday\] |
