"""
FortiOS MONITOR - Monitor Wifi Network

Monitoring endpoint for monitor wifi network data.

API Endpoints:
    GET    /monitor/wifi/network

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.wifi.network.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.wifi.network.get(
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


class Connect:
    """
    Connect Operations.

    Provides read-only access for FortiOS connect data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Connect endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        ssid: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        When FortiWiFi is in client mode, connect to the specified network, if
        configured in the 'wifi' interface.

        Args:
            ssid: SSID of network to connect to. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.network.connect.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if ssid is not None:
            data["ssid"] = ssid
        data.update(kwargs)
        return self._client.post("monitor", "/wifi/network/connect", data=data)


class List:
    """List operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize List endpoint.

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
        When FortiWiFi is in client mode, retrieve list of local WiFi networks.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.network.list.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/wifi/network/list", params=params)


class Scan:
    """Scan operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Scan endpoint.

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
        When FortiWiFi is in client mode, start a scan for local WiFi networks.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.network.scan.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/wifi/network/scan", data=data)


class Status:
    """Status operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Status endpoint.

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
        When FortiWiFi is in client mode, retrieve status of currently
        connected WiFi network, if any.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.network.status.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/wifi/network/status", params=params
        )


class Network:
    """Network operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Network endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.connect = Connect(client)
        self.list = List(client)
        self.scan = Scan(client)
        self.status = Status(client)
