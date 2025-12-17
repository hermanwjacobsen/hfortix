"""
FortiGate LAN Extension VDOM Monitor API

Provides access to FortiGate LAN Extension VDOM status.
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class LanExtensionVdom:
    """
    FortiGate LAN Extension VDOM monitoring.

    Provides methods to retrieve information for the FortiGate
    LAN Extension VDOM.

    Example usage:
        # Get VDOM status
        status = fgt.api.monitor.extension_controller.lan_extension_vdom.status()

        # Get VDOM status (dict)
        status = fgt.api.monitor.extension_controller.lan_extension_vdom.status(
            data_dict={}
        )
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize LAN Extension VDOM monitor.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client
        self._base_path = "/extension-controller/lan-extension-vdom-status"

    def status(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        """
        Get FortiGate LAN Extension VDOM status.

        Retrieves information for the FortiGate LAN Extension VDOM including
        connection status, uptime, and uplink information.

        Args:
            data_dict: Dictionary containing parameters (alternative to kwargs)
            **kwargs: Additional parameters as keyword arguments

        Returns:
            VDOM status information with name, ip, status, uptime, port, and uplink fields

        Examples:
            # Get VDOM status
            status = fgt.api.monitor.extension_controller.lan_extension_vdom.status()

            # Get VDOM status (dict)
            status = fgt.api.monitor.extension_controller.lan_extension_vdom.status(
                data_dict={}
            )

            # Response format:
            # {
            #     'name': 'controller1',
            #     'ip': '192.168.1.1',
            #     'status': 'EXTWS_RUN',
            #     'uptime': 7200,
            #     'port': 443,
            #     'uplink': ['port1', 'port2']
            # }
            #
            # Status values:
            # - EXTWS_RUN: Running
            # - EXTWS_SULKING: Sulking
            # - EXTWS_JOIN: Joining
            # - EXTWS_DISCOVERY: Discovery
            # - EXTWS_DTLS_SETUP: DTLS Setup
            # - EXTWS_IDLE: Idle
        """
        params = data_dict.copy() if data_dict else {}
        params.update(kwargs)

        return self._client.get("monitor", self._base_path, params=params)

    def __dir__(self):
        """Return list of available attributes."""
        return ["status"]
