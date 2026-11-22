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
