Install
*******

.. code-block:: shell

   docker run -d -p 8000:8000 \
   -e CONF_DEVICE_IP_ADDR=192.168.100.157 \
   -e CONF_PHONE_ID=1234 \
   -e CONF_DEVICE_ID=ab1c2d \
   -e CONF_DEVICE_PASSWORD=12345678 \
   --name switcher_webapi tomerfi/switcher_webapi:latest"


You can also add another optional environment variable:

.. code-block:: shell

   -e CONF_THROTTLE=5.0

for setting the throttle time between consecutive requests,
this is optional and the default value is **5.0**.

Here's an example of running the container using *docker-compose* setting the
environment variables in a designated file.

.. code-block:: yaml

   # docker-compose.yml
   version: "3.7"

   services:
     switcher_api:
       image: tomerfi/switcher_webapi:latest
       container_name: "switcher_webapi"
       env_file:
         - .env_vars
       ports:
         - 8000:8000
       restart: unless-stopped

.. code-block:: ini

   # .env_vars
   CONF_DEVICE_IP_ADDR=192.168.100.157
   CONF_PHONE_ID=1234
   CONF_DEVICE_ID=ab1c2d
   CONF_DEVICE_PASSWORD=12345678
   CONF_THROTTLE=5.0
