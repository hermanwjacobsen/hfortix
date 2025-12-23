"""
FortiOS MONITOR - Monitor Firewall Local In

Monitoring endpoint for monitor firewall local in data.

API Endpoints:
    GET    /monitor/firewall/local_in

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.local_in.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.local_in.get(
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


class LocalIn:
    """
    Localin Operations.

    Provides read-only access for FortiOS localin data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize LocalIn endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        include_ttl: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List implicit and explicit local-in firewall policies.

        Args:
            include_ttl: Include TTL local-in policies. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.local_in.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if include_ttl is not None:
            params["include_ttl"] = include_ttl
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/local-in", params=params)
