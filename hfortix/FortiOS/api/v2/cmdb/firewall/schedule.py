"""
FortiOS Firewall Schedule API
Schedule configuration endpoints
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Schedule:
    """
    Firewall Schedule API helper class
    Provides access to firewall schedule endpoints
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Schedule helper

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoint classes
        from .schedule_group import ScheduleGroup
        from .schedule_onetime import ScheduleOnetime
        from .schedule_recurring import ScheduleRecurring

        self.group = ScheduleGroup(client)
        self.onetime = ScheduleOnetime(client)
        self.recurring = ScheduleRecurring(client)
