Usage
*****

Once running, you can send REST requests towards the container.
With the exception of the *create_schedule* requests,
all the requests requiring input accepts it as a json body or in the form of
query parameters.

get_state
^^^^^^^^^

**URL:** */switcher/get_state*

**Method:** *GET*

**Request parameters:** *None*

**Response body example:**

.. code-block:: json

   {
     "successful": true,
     "state": "on",
     "time_left": "00:47:25",
     "auto_off": "01:30:00",
     "power_consumption": 2669,
     "electric_current": 12.3
   }


turn_on
^^^^^^^

**URL**: */switcher/turn_on*

**Method:** *POST*

**Request parameters:**

+-------------+------------+-----------------------------------------+
| Key         | Required   | Description                             |
+=============+============+=========================================+
| **minutes** | *Optional* | turn on the device with an off timer of |
|             |            | 1-180 minutes.                          |
+-------------+------------+-----------------------------------------+


**Request body example:**

.. code-block:: json

   {
     "minutes": "30"
   }

**Response body example:**

.. code-block:: json

   {
     "successful": true
   }

turn_off
^^^^^^^^

**URL:** */switcher/turn_off*

**Method:** *POST*

**Request parameters:** *None*

**Response body example:**

.. code-block:: json

   {
     "successful": true
   }

set_auto_shutdown
^^^^^^^^^^^^^^^^^

**URL:** */switcher/set_auto_shutdown*

**Method:** *POST*

**Request parameters:**

+-------------+-------------+---------------------+
| Key         | Required    | Description         |
+=============+=============+=====================+
| **hours**   | *Mandatory* | hours value 1-3.    |
+-------------+-------------+---------------------+
| **minutes** | *Mandatory* | minutes value 0-59. |
+-------------+-------------+---------------------+

.. note::

   The auto shutdown configuration value accept any total value of hours and minutes between 1 and 3 hours.

**Request body example:**

.. code-block:: json

   {
     "hours": "1",
     "minutes": "30"
   }

**Response body example:**

.. code-block:: json

   {
     "successful": true
   }

set_device_name
^^^^^^^^^^^^^^^

**URL:** */switcher/set_device_name*

**Method:** *POST*

**Request parameters:**

+----------+-------------+-------------------------------------------------+
| Key      | Required    | Description                                     |
+==========+=============+=================================================+
| **name** | *Mandatory* | device name, accepts length of 2-32 characters. |
+----------+-------------+-------------------------------------------------+

**Request body example:**

.. code-block:: json

   {
     "name": "my new device name"
   }

**Response body example:**

.. code-block:: json

   {
     "successful": true
   }

get_schedules
^^^^^^^^^^^^^

**URL:** */switcher/get_schedules*

**Method:** *GET*

**Request parameters:** *None*

**Response body example:**

.. code-block:: json

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

.. note::

   The *schedules* list can contain up to 8 schedules with the identifiers
   of 0-7 representing the actual schedule slots on the device.

enable_schedule
^^^^^^^^^^^^^^^

**URL:** */switcher/enable_schedule*

**Method:** *PATCH*

**Request parameters:**

+-------------------+-------------+-------------------------------------------+
| Key               | Required    | Description                               |
+===================+=============+===========================================+
| **schedule_data** | *Mandatory* | the *schedule_data* associated with the   |
|                   |             | chosen schedule.                          |
|                   |             |                                           |
|                   |             | retrieved with */switcher/get_schedules*. |
+-------------------+-------------+-------------------------------------------+

**Request body example:**

.. code-block:: json

   {
     "schedule_data": "0101020160a6c95c70b4c95c"
   }

**Response body example:**

.. code-block:: json

   {
     "successful": true
   }

disable_schedule
^^^^^^^^^^^^^^^^

**URL:** */switcher/disable_schedule*

**Method:** *PATCH*

**Request parameters:**

+-------------------+-------------+-------------------------------------------+
| Key               | Required    | Description                               |
+===================+=============+===========================================+
| **schedule_data** | *Mandatory* | the *schedule_data* associated with the   |
|                   |             | chosen schedule.                          |
|                   |             |                                           |
|                   |             | retrieved with */switcher/get_schedules*. |
+-------------------+-------------+-------------------------------------------+

**Request body example:**

.. code-block:: json

   {
     "schedule_data": "0101020160a6c95c70b4c95c"
   }

**Response body example:**

.. code-block:: json

   {
     "successful": true
   }

delete_schedule
^^^^^^^^^^^^^^^

**URL:** */switcher/delete_schedule*

**Method:** *DELETE*

**Request parameters:**

+-----------------+-------------+-------------------------------------------+
| Key             | Required    | Description                               |
+=================+=============+===========================================+
| **schedule_id** | *Mandatory* | the *schedule_id* associated with the     |
|                 |             | chosen schedule.                          |
|                 |             |                                           |
|                 |             | retrieved with */switcher/get_schedules*. |
+-----------------+-------------+-------------------------------------------+

**Request body example:**

.. code-block:: json

   {
     "schedule_id": "2"
   }

**Response body example:**

.. code-block:: json

   {
     "successful": true
   }

create_schedule
^^^^^^^^^^^^^^^

**URL:** */switcher/create_schedule*

**Method:** *PUT*

**Request parameters:**

+-------------------+-------------+------------------------------------------+
| Key               | Required    | Description                              |
+===================+=============+==========================================+
| **days**          | *Mandatory* | list of days for the schedule to run in. |
|                   |             |                                          |
|                   |             | (empty for non-recurring schedules).     |
+-------------------+-------------+------------------------------------------+
| **start_hours**   | *Mandatory* | start time hours value 0-23.             |
+-------------------+-------------+------------------------------------------+
| **start_minutes** | *Mandatory* | start minutes value 0-59.                |
+-------------------+-------------+------------------------------------------+
| **stop_hours**    | *Mandatory* | stop time hours value 0-23.              |
+-------------------+-------------+------------------------------------------+
| **stop_minutes**  | *Mandatory* | stop minutes value 0-59.                 |
+-------------------+-------------+------------------------------------------+

**Request body example:**

.. code-block:: json

   {
     "days": ["Monday", "Wednesday", "Friday"],
     "start_hours": "20",
     "start_minutes": "30",
     "stop_hours": "21",
     "stop_minutes": "0"
   }

**Response body example:**

.. code-block:: json

   {
     "successful": true
   }

Possible values for the *days* list:

.. hlist::

   * Sunday
   * Monday
   * Tuesday
   * Wednesday
   * Thursday
   * Friday
   * Saturday


.. note::

   Due to its complexity, the *create_schedule* request accepts its arguments
   in the form of a json body only, query parameters will not be accepted.

Exceptions
^^^^^^^^^^

Unless unhandled, all exceptions will return a json object in response body:

.. code-block:: json

   {
     "successful": false,
     "message": "the error description"
   }
