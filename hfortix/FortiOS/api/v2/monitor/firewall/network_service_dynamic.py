"""
FortiOS MONITOR - Monitor Firewall Network Service Dynamic

Monitoring endpoint for monitor firewall network service dynamic data.

API Endpoints:
    GET    /monitor/firewall/network_service_dynamic

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.network_service_dynamic.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.network_service_dynamic.get(
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


class NetworkServiceDynamic:
    """
    Networkservicedynamic Operations.

    Provides read-only access for FortiOS networkservicedynamic data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize NetworkServiceDynamic endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        mkey: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List of dynamic network service IP address and port pairs.

        Args:
            mkey: Name of the dynamic network service entry. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.firewall.network_service_dynamic.get(mkey='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["mkey"] = mkey
        params.update(kwargs)
        return self._client.get(
            "monitor", "/firewall/network-service-dynamic", params=params
        )
