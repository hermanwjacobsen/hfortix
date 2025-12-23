"""
FortiOS MONITOR - Monitor Firewall Clearpass Address

Monitoring endpoint for monitor firewall clearpass address data.

API Endpoints:
    GET    /monitor/firewall/clearpass_address

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.clearpass_address.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.clearpass_address.get(
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


class Add:
    """
    Add Operations.

    Provides read-only access for FortiOS add data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Add endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        endpoint_ip: list | None = None,
        spt: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Add ClearPass address with SPT (System Posture Token) value.

        Args:
            endpoint_ip: Endpoint IPv4 address. (optional)
            spt: SPT value
            [healthy|checkup|transient|quarantine|infected|unknown*].
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.clearpass_address.add.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if endpoint_ip is not None:
            data["endpoint_ip"] = endpoint_ip
        if spt is not None:
            data["spt"] = spt
        data.update(kwargs)
        return self._client.post(
            "monitor", "/firewall/clearpass-address/add", data=data
        )


class Delete:
    """Delete operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Delete endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        endpoint_ip: list | None = None,
        spt: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete ClearPass address with SPT (System Posture Token) value.

        Args:
            endpoint_ip: Endpoint IPv4 address. (optional)
            spt: SPT value
            [healthy|checkup|transient|quarantine|infected|unknown*].
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.clearpass_address.delete.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if endpoint_ip is not None:
            data["endpoint_ip"] = endpoint_ip
        if spt is not None:
            data["spt"] = spt
        data.update(kwargs)
        return self._client.post(
            "monitor", "/firewall/clearpass-address/delete", data=data
        )


class ClearpassAddress:
    """ClearpassAddress operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ClearpassAddress endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.add = Add(client)
        self.delete = Delete(client)
