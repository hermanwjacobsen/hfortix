"""
FortiOS Firewall IP-MAC Binding API
IP-MAC binding configuration endpoints
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Ipmacbinding:
    """
    Firewall IP-MAC Binding API helper class
    Provides access to firewall IP-MAC binding endpoints
    """

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Ipmacbinding helper

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoint classes
        from .ipmacbinding_setting import IpmacbindingSetting
        from .ipmacbinding_table import IpmacbindingTable

        self.setting = IpmacbindingSetting(client)
        self.table = IpmacbindingTable(client)
