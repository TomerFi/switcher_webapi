Notes
*****

.. hlist::
   :columns: 1

   * If you don't want to be forced to restart the container if the device's ip address changes, please consider assigning the device with a static ip address.
   * The Switcher-V2-Python repository is build with python 2.7.
   * The aioswitcher_ was tested with the Switcher V2 device by myself and with the Switcher Touch device by the community.
   * This project was intended for local usage, it's ok if you want to use it remotely, just make sure to take the proper security measures such as reverse proxy and ssl.
   * The WebAPI has a throttle mechanism to prevent overfloating the device with frequent requests, it defaults to 5 seconds throttle time.
   * Some users have been reporting lately about failures using the Switcher-V2-Python script after upgrading the device firmware to 3.0, please follow the relevant issues in the script repository before doing the same.

.. _aioswitcher: https://pypi.org/project/aioswitcher/
