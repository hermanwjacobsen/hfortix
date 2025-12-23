"""
FortiGate LAN Extension Controller Monitor API

This module provides access to FortiGate LAN Extension monitoring endpoints.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client_interface import IHTTPClient

    from .fortigate import Fortigate
    from .lan_extension_vdom_status import (
        LanExtensionVdomStatus as LanExtensionVdom,
    )


class ExtensionController:
    """
    FortiGate LAN Extension Controller monitoring.

    Provides methods to monitor FortiGate LAN Extension Connectors and VDOM
    status.

    Example usage:
        # Get FortiGate connector statistics
        stats = fgt.api.monitor.extension_controller.fortigate.stats()

        # Get LAN Extension VDOM status
        status =
        fgt.api.monitor.extension_controller.lan_extension_vdom.status()
    """

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize ExtensionController monitor.

        Args:
            client: HTTP client implementing IHTTPClient protocol for API
            communication
        """
        self._client = client
        self._fortigate: Fortigate | None = None
        self._lan_extension_vdom: LanExtensionVdom | None = None

    @property
    def fortigate(self):
        """
        Access FortiGate connector sub-endpoint.

        Returns:
            Fortigate instance
        """
        if self._fortigate is None:
            self._fortigate = Fortigate(self._client)
        return self._fortigate

    @property
    def lan_extension_vdom(self):
        """
        Access LAN Extension VDOM sub-endpoint.

        Returns:
            LanExtensionVdomStatus instance
        """
        if self._lan_extension_vdom is None:
            from .lan_extension_vdom_status import LanExtensionVdomStatus

            self._lan_extension_vdom = LanExtensionVdomStatus(self._client)
        return self._lan_extension_vdom

    def __dir__(self):
        """Return list of available attributes."""
        return ["fortigate", "lan_extension_vdom"]
