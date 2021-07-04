# Copyright Tomer Figenblat.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Helper functions for unit testing the Switcher WebAPI.

.. codeauthor:: Tomer Figenblat <tomer.figenblat@gmail.com>

"""

from datetime import datetime
from socket import gethostbyname, gethostname

from pytz import utc


def get_local_ip_address() -> str:
    """Use for getting the local host's ip address.

    Returns:
      The local ip address.

    """
    return gethostbyname(gethostname())


def get_next_weekday(is_iso: bool = False) -> int:
    """Use for getting next day weekday.

    Args:
      is_iso: If true, Monday=1 and Sunday=7. Else Monday=0 and Sunday=6.

    Returns:
      The int value represnting the the next weekday (tomorrow).

    """
    max_day = 7 if is_iso else 6
    current_day = datetime.now(utc).isoweekday()
    if current_day < max_day:
        return current_day + 1
    return 0 if max_day == 6 else 1
