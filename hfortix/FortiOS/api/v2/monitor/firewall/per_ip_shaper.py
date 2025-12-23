"""
FortiOS MONITOR - Monitor Firewall Per Ip Shaper

Monitoring endpoint for monitor firewall per ip shaper data.

API Endpoints:
    GET    /monitor/firewall/per_ip_shaper

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.per_ip_shaper.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.per_ip_shaper.get(
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


class Reset:
    """
    Reset Operations.

    Provides read-only access for FortiOS reset data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Reset endpoint.

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
        Reset statistics for all configured firewall per-IP traffic shapers.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.per_ip_shaper.reset.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post(
            "monitor", "/firewall/per-ip-shaper/reset", data=data
        )


class PerIpShaper:
    """PerIpShaper operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize PerIpShaper endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.reset = Reset(client)

    def get(
        self,
        shaper_name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List of statistics for configured firewall per-IP traffic shapers.

        Args:
            shaper_name: Filter the results by per-IP shaper name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.per_ip_shaper.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if shaper_name is not None:
            params["shaper_name"] = shaper_name
        params.update(kwargs)
        return self._client.get(
            "monitor", "/firewall/per-ip-shaper", params=params
        )
