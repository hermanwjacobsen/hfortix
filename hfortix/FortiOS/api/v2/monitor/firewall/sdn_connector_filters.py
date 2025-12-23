"""
FortiOS MONITOR - Monitor Firewall Sdn Connector Filters

Monitoring endpoint for monitor firewall sdn connector filters data.

API Endpoints:
    GET    /monitor/firewall/sdn_connector_filters

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.sdn_connector_filters.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.sdn_connector_filters.get(
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


class SdnConnectorFilters:
    """
    Sdnconnectorfilters Operations.

    Provides read-only access for FortiOS sdnconnectorfilters data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize SdnConnectorFilters endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        connector: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List all available filters for a specified SDN Fabric Connector.

        Args:
            connector: Name of the SDN Fabric Connector to get the filters
            from. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.firewall.sdn_connector_filters.get(connector='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["connector"] = connector
        params.update(kwargs)
        return self._client.get(
            "monitor", "/firewall/sdn-connector-filters", params=params
        )
