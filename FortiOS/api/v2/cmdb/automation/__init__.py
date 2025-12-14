"""
FortiOS CMDB - Automation API

This module provides access to FortiOS automation configuration endpoints.
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....client import FortiOS

from .setting import Setting


class Automation:
    """Automation configuration endpoints"""

    def __init__(self, client: 'FortiOS') -> None:
        """
        Initialize Automation API

        Args:
            client: FortiOS client instance
        """
        self._client = client

        # Initialize endpoint classes
        self.setting = Setting(client)
