"""
FortiOS MONITOR - Monitor Extension Controller Lan Extension Vdom

Monitoring endpoint for monitor extension controller lan extension vdom data.

API Endpoints:
    GET    /monitor/extension_controller/lan_extension_vdom

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.extension_controller.lan_extension_vdom.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.extension_controller.lan_extension_vdom.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class LanExtensionVdom:
    """
    Lanextensionvdom Operations.

    Provides read-only access for FortiOS lanextensionvdom data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize LAN Extension VDOM monitor.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get FortiGate LAN Extension VDOM status.

        Retrieves information for the FortiGate LAN Extension VDOM including
        connection status, uptime, and uplink information.

        Args:
            payload_dict: Dictionary containing parameters (alternative to
            kwargs)
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            VDOM status information with name, ip, status, uptime, port, and
            uplink fields

        Examples:
            # Get VDOM status
            status =
            fgt.api.monitor.extension_controller.lan_extension_vdom.get()

            # Get VDOM status with payload_dict
            status =
            fgt.api.monitor.extension_controller.lan_extension_vdom.get(
                payload_dict={}
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
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)

        return self._client.get(
            "monitor",
            "/extension-controller/lan-extension-vdom-status",
            params=params,
        )
