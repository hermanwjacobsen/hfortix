"""
FortiOS MONITOR - Monitor Wifi Rogue Ap

Monitoring endpoint for monitor wifi rogue ap data.

API Endpoints:
    GET    /monitor/wifi/rogue_ap

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.wifi.rogue_ap.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.wifi.rogue_ap.get(
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


class ClearAll:
    """
    Clearall Operations.

    Provides read-only access for FortiOS clearall data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ClearAll endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clear all detected rogue APs.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.rogue_ap.clear_all.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post(
            "monitor", "/wifi/rogue_ap/clear_all", data=data
        )


class SetStatus:
    """SetStatus operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize SetStatus endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        bssid: list | None = None,
        ssid: list | None = None,
        status: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Mark detected APs as rogue APs.

        Args:
            bssid: List of rogue AP MAC addresses. (optional)
            ssid: Corresponding list of rogue AP SSIDs. (optional)
            status: Status to assign matching APs
            [unclassified|rogue|accepted|suppressed]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.rogue_ap.set_status.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if bssid is not None:
            data["bssid"] = bssid
        if ssid is not None:
            data["ssid"] = ssid
        if status is not None:
            data["status"] = status
        data.update(kwargs)
        return self._client.post(
            "monitor", "/wifi/rogue_ap/set_status", data=data
        )


class RogueAp:
    """RogueAp operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize RogueAp endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.clear_all = ClearAll(client)
        self.set_status = SetStatus(client)

    def get(
        self,
        managed_ssid_only: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a list of detected rogue APs.

        Args:
            managed_ssid_only: Filter: True to include only WiFi controller
            managed SSIDs. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.rogue_ap.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if managed_ssid_only is not None:
            params["managed_ssid_only"] = managed_ssid_only
        params.update(kwargs)
        return self._client.get("monitor", "/wifi/rogue_ap", params=params)
