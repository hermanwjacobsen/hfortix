"""
FortiOS MONITOR - Monitor Router Sdwan

Monitoring endpoint for monitor router sdwan data.

API Endpoints:
    GET    /monitor/router/sdwan

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.router.sdwan.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.router.sdwan.get(
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


class Routes:
    """
    Routes Operations.

    Provides read-only access for FortiOS routes data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Routes endpoint.

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
        List all discovered IPv4 SD-WAN routes.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.router.sdwan.routes.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/router/sdwan/routes", params=params
        )


class RoutesStatistics:
    """RoutesStatistics operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize RoutesStatistics endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        ip_version: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve SD-WAN routes statistics, including number of IPv4 or IPv6
        SD-WAN routes.

        Args:
            ip_version: IP version [*ipv4 | ipv6 | ipboth]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.router.sdwan.routes_statistics.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if ip_version is not None:
            params["ip_version"] = ip_version
        params.update(kwargs)
        return self._client.get(
            "monitor", "/router/sdwan/routes-statistics", params=params
        )


class Routes6:
    """Routes6 operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Routes6 endpoint.

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
        List all discovered IPv6 SD-WAN routes.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.router.sdwan.routes6.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/router/sdwan/routes6", params=params
        )


class Sdwan:
    """Sdwan operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Sdwan endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.routes = Routes(client)
        self.routes_statistics = RoutesStatistics(client)
        self.routes6 = Routes6(client)
