"""
FortiOS MONITOR - Monitor Switch Controller Nac Device

Monitoring endpoint for monitor switch controller nac device data.

API Endpoints:
    GET    /monitor/switch_controller/nac_device

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.switch_controller.nac_device.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.switch_controller.nac_device.get(
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


class Stats:
    """
    Stats Operations.

    Provides read-only access for FortiOS stats data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Stats endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Return the current FortiSwitch matched NAC device counts and limits for
        the FortiGate.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.switch_controller.nac_device.stats.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/switch-controller/nac-device/stats", params=params
        )


class NacDevice:
    """NacDevice operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize NacDevice endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.stats = Stats(client)
