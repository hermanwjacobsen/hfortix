"""
FortiOS MONITOR - Monitor Network Ddns

Monitoring endpoint for monitor network ddns data.

API Endpoints:
    GET    /monitor/network/ddns

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.network.ddns.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.network.ddns.get(
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


class Lookup:
    """
    Lookup Operations.

    Provides read-only access for FortiOS lookup data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Lookup endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        domain: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Check DDNS FQDN availability.

        Args:
            domain: Filter: domain to check. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.network.ddns.lookup.get(domain='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["domain"] = domain
        params.update(kwargs)
        return self._client.get(
            "monitor", "/network/ddns/lookup", params=params
        )


class Servers:
    """Servers operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Servers endpoint.

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
        Get DDNS servers.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.network.ddns.servers.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/network/ddns/servers", params=params
        )


class Ddns:
    """Ddns operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Ddns endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.lookup = Lookup(client)
        self.servers = Servers(client)
