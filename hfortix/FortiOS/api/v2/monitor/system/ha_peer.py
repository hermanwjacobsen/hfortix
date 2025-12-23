"""
FortiOS MONITOR - Monitor System Ha Peer

Monitoring endpoint for monitor system ha peer data.

API Endpoints:
    GET    /monitor/system/ha_peer

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.ha_peer.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.ha_peer.get(
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


class Disconnect:
    """
    Disconnect Operations.

    Provides read-only access for FortiOS disconnect data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Disconnect endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        serial_no: str | None = None,
        interface: str | None = None,
        ip: str | None = None,
        mask: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update configuration of peer in HA cluster.

        Args:
            serial_no: Serial number of the HA member. (optional)
            interface: Name of the interface which should be assigned for
            management. (optional)
            ip: IP to assign to the selected interface. (optional)
            mask: Full network mask to assign to the selected interface.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.ha_peer.disconnect.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if serial_no is not None:
            data["serial_no"] = serial_no
        if interface is not None:
            data["interface"] = interface
        if ip is not None:
            data["ip"] = ip
        if mask is not None:
            data["mask"] = mask
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/ha-peer/disconnect", data=data
        )


class Update:
    """Update operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Update endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        serial_no: str | None = None,
        vcluster_id: int | None = None,
        priority: int | None = None,
        hostname: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update configuration of peer in HA cluster.

        Args:
            serial_no: Serial number of the HA member. (optional)
            vcluster_id: Virtual cluster number. (optional)
            priority: Priority to assign to HA member. (optional)
            hostname: Name to assign the HA member. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.ha_peer.update.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if serial_no is not None:
            data["serial_no"] = serial_no
        if vcluster_id is not None:
            data["vcluster_id"] = vcluster_id
        if priority is not None:
            data["priority"] = priority
        if hostname is not None:
            data["hostname"] = hostname
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/ha-peer/update", data=data
        )


class HaPeer:
    """HaPeer operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize HaPeer endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.disconnect = Disconnect(client)
        self.update = Update(client)

    def get(
        self,
        serial_no: str | None = None,
        vcluster_id: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get configuration of peer(s) in HA cluster.

        Args:
            serial_no: Serial number of the HA member. If not specified, fetch
            information for all HA members (optional)
            vcluster_id: Virtual cluster number. If not specified, fetch
            information for all active vclusters (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.ha_peer.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if serial_no is not None:
            params["serial_no"] = serial_no
        if vcluster_id is not None:
            params["vcluster_id"] = vcluster_id
        params.update(kwargs)
        return self._client.get("monitor", "/system/ha-peer", params=params)
