"""
FortiOS MONITOR - Monitor Vpn Ipsec

Monitoring endpoint for monitor vpn ipsec data.

API Endpoints:
    GET    /monitor/vpn/ipsec

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.vpn.ipsec.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.vpn.ipsec.get(
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


class ConnectionCount:
    """
    Connectioncount Operations.

    Provides read-only access for FortiOS connectioncount data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ConnectionCount endpoint.

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
        Return the connection counts for every ipsec tunnel.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.vpn.ipsec.connection_count.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/vpn/ipsec/connection-count", params=params
        )


class TunnelDown:
    """TunnelDown operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize TunnelDown endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        p1name: str | None = None,
        p2name: str | None = None,
        p2serial: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Bring down a specific IPsec VPN tunnel.

        Args:
            p1name: IPsec phase1 name. (optional)
            p2name: IPsec phase2 name. (optional)
            p2serial: IPsec phase2 serial. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.vpn.ipsec.tunnel_down.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if p1name is not None:
            data["p1name"] = p1name
        if p2name is not None:
            data["p2name"] = p2name
        if p2serial is not None:
            data["p2serial"] = p2serial
        data.update(kwargs)
        return self._client.post(
            "monitor", "/vpn/ipsec/tunnel_down", data=data
        )


class TunnelResetStats:
    """TunnelResetStats operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize TunnelResetStats endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        p1name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Reset statistics for a specific IPsec VPN tunnel.

        Args:
            p1name: IPsec phase1 name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.vpn.ipsec.tunnel_reset_stats.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if p1name is not None:
            data["p1name"] = p1name
        data.update(kwargs)
        return self._client.post(
            "monitor", "/vpn/ipsec/tunnel_reset_stats", data=data
        )


class TunnelUp:
    """TunnelUp operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize TunnelUp endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        p1name: str | None = None,
        p2name: str | None = None,
        p2serial: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Bring up a specific IPsec VPN tunnel.

        Args:
            p1name: IPsec phase1 name. (optional)
            p2name: IPsec phase2 name. (optional)
            p2serial: IPsec phase2 serial. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.vpn.ipsec.tunnel_up.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if p1name is not None:
            data["p1name"] = p1name
        if p2name is not None:
            data["p2name"] = p2name
        if p2serial is not None:
            data["p2serial"] = p2serial
        data.update(kwargs)
        return self._client.post("monitor", "/vpn/ipsec/tunnel_up", data=data)


class Ipsec:
    """Ipsec operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Ipsec endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.connection_count = ConnectionCount(client)
        self.tunnel_down = TunnelDown(client)
        self.tunnel_reset_stats = TunnelResetStats(client)
        self.tunnel_up = TunnelUp(client)

    def get(
        self,
        tunnel: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Return an array of active IPsec VPNs.

        Args:
            tunnel: Filter for a specific IPsec tunnel name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.vpn.ipsec.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if tunnel is not None:
            params["tunnel"] = tunnel
        params.update(kwargs)
        return self._client.get("monitor", "/vpn/ipsec", params=params)
