"""
FortiOS MONITOR - Monitor Router Bgp

Monitoring endpoint for monitor router bgp data.

API Endpoints:
    GET    /monitor/router/bgp

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.router.bgp.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.router.bgp.get(
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


class ClearSoftIn:
    """
    Clearsoftin Operations.

    Provides read-only access for FortiOS clearsoftin data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ClearSoftIn endpoint.

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
        Inbound soft-reconfiguration for BGP peers.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.router.bgp.clear_soft_in.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post(
            "monitor", "/router/bgp/clear-soft-in", data=data
        )


class ClearSoftOut:
    """ClearSoftOut operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ClearSoftOut endpoint.

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
        Outbound soft-reconfiguration for BGP peers.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.router.bgp.clear_soft_out.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post(
            "monitor", "/router/bgp/clear-soft-out", data=data
        )


class Neighbors:
    """Neighbors operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Neighbors endpoint.

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
        List all discovered BGP neighbors.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.router.bgp.neighbors.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/router/bgp/neighbors", params=params
        )


class NeighborsStatistics:
    """NeighborsStatistics operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize NeighborsStatistics endpoint.

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
        Retrieve BGP neighbors statistics, including number of IPv4 or IPv6 BGP
        neighbors.

        Args:
            ip_version: IP version [*ipv4 | ipv6 | ipboth]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.router.bgp.neighbors_statistics.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if ip_version is not None:
            params["ip_version"] = ip_version
        params.update(kwargs)
        return self._client.get(
            "monitor", "/router/bgp/neighbors-statistics", params=params
        )


class Neighbors6:
    """Neighbors6 operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Neighbors6 endpoint.

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
        List all discovered IPv6 BGP neighbors.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.router.bgp.neighbors6.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/router/bgp/neighbors6", params=params
        )


class Paths:
    """Paths operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Paths endpoint.

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
        List all discovered BGP paths.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.router.bgp.paths.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/router/bgp/paths", params=params)


class PathsStatistics:
    """PathsStatistics operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize PathsStatistics endpoint.

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
        Retrieve BGP paths statistics, including number of IPv4 or IPv6 BGP
        paths.

        Args:
            ip_version: IP version [*ipv4 | ipv6 | ipboth]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.router.bgp.paths_statistics.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if ip_version is not None:
            params["ip_version"] = ip_version
        params.update(kwargs)
        return self._client.get(
            "monitor", "/router/bgp/paths-statistics", params=params
        )


class Paths6:
    """Paths6 operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Paths6 endpoint.

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
        List all discovered IPv6 BGP paths.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.router.bgp.paths6.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/router/bgp/paths6", params=params)


class SoftResetNeighbor:
    """SoftResetNeighbor operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize SoftResetNeighbor endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        ip: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        BGP Neighbor soft reset.

        Args:
            ip: IPv4 or IPv6 address of neighbor to perform soft reset on.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.router.bgp.soft_reset_neighbor.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if ip is not None:
            data["ip"] = ip
        data.update(kwargs)
        return self._client.post(
            "monitor", "/router/bgp/soft-reset-neighbor", data=data
        )


class Bgp:
    """Bgp operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Bgp endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.clear_soft_in = ClearSoftIn(client)
        self.clear_soft_out = ClearSoftOut(client)
        self.neighbors = Neighbors(client)
        self.neighbors_statistics = NeighborsStatistics(client)
        self.neighbors6 = Neighbors6(client)
        self.paths = Paths(client)
        self.paths_statistics = PathsStatistics(client)
        self.paths6 = Paths6(client)
        self.soft_reset_neighbor = SoftResetNeighbor(client)
