"""
FortiOS MONITOR - Monitor Wifi Client

Monitoring endpoint for monitor wifi client data.

API Endpoints:
    GET    /monitor/wifi/client

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.wifi.client.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.wifi.client.get(
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


class Disassociate:
    """
    Disassociate Operations.

    Provides read-only access for FortiOS disassociate data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Disassociate endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mac: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Disassociate a WiFi client from the FortiAP it's currently connected
        to.

        Args:
            mac: MAC address. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.client.disassociate.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mac is not None:
            data["mac"] = mac
        data.update(kwargs)
        return self._client.post(
            "monitor", "/wifi/client/disassociate", data=data
        )


class Client:
    """Client operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Client endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.disassociate = Disassociate(client)

    def get(
        self,
        type: str | None = None,
        with_triangulation: bool | None = None,
        with_stats: bool | None = None,
        mac: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a list of connected WiFi clients.

        Args:
            type: Request type [all*|fail-login]. (optional)
            with_triangulation: Enable to include regions of FortiAP detecting
            the client. (optional)
            with_stats: Enable to include statistics of FortiAP client.
            (optional)
            mac: WiFi client MAC address. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.client.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if type is not None:
            params["type"] = type
        if with_triangulation is not None:
            params["with_triangulation"] = with_triangulation
        if with_stats is not None:
            params["with_stats"] = with_stats
        if mac is not None:
            params["mac"] = mac
        params.update(kwargs)
        return self._client.get("monitor", "/wifi/client", params=params)
