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
