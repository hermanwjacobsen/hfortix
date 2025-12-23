"""
FortiOS MONITOR - Monitor Firewall Internet Service Details

Monitoring endpoint for monitor firewall internet service details data.

API Endpoints:
    GET    /monitor/firewall/internet_service_details

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.internet_service_details.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.internet_service_details.get(
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


class InternetServiceDetails:
    """
    Internetservicedetails Operations.

    Provides read-only access for FortiOS internetservicedetails data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize InternetServiceDetails endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        id: int,
        country_id: int | None = None,
        region_id: int | None = None,
        city_id: int | None = None,
        summary_only: bool | None = None,
        ipv6_only: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List all details for a given Internet Service ID.

        Args:
            id: ID of the Internet Service to get details for. (required)
            country_id: Filter: Country ID. (optional)
            region_id: Filter: Region ID. (optional)
            city_id: Filter: City ID. (optional)
            summary_only: Only return number of entries instead of entries.
            (optional)
            ipv6_only: Only returns ipv6 entries. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.internet_service_details.get(id=1)
        """
        params = payload_dict.copy() if payload_dict else {}
        params["id"] = id
        if country_id is not None:
            params["country_id"] = country_id
        if region_id is not None:
            params["region_id"] = region_id
        if city_id is not None:
            params["city_id"] = city_id
        if summary_only is not None:
            params["summary_only"] = summary_only
        if ipv6_only is not None:
            params["ipv6_only"] = ipv6_only
        params.update(kwargs)
        return self._client.get(
            "monitor", "/firewall/internet-service-details", params=params
        )
