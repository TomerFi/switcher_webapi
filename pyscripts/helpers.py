"""Helper functions for unit testing the Switcher WebAPI."""

from datetime import datetime
from socket import gethostbyname, gethostname

from pytz import utc


def get_next_weekday(is_iso: bool = False) -> int:
    """Use for getting next day weekday."""
    max_day = 7 if is_iso else 6
    current_day = datetime.now(utc).isoweekday()
    if current_day < max_day:
        return current_day + 1
    return 0


def get_local_ip_address() -> str:
    """Use for getting the local host's ip address."""
    return gethostbyname(gethostname())
