"""
FortiOS MONITOR - Monitor Firewall Internet Service

Monitoring endpoint for monitor firewall internet service data.

API Endpoints:
    GET    /monitor/firewall/internet_service

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.internet_service.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.internet_service.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client_interface import IHTTPClient


class InternetService:
    """
    Internetservice Operations.

    Provides read-only access for FortiOS internetservice data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize InternetService endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def match(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        ip: Optional[str] = None,
        ipv6: Optional[bool] = None,
        country: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List internet services that exist at a given IP or Subnet.

        Args:
            data_dict: Optional dictionary of parameters
            ip: IP address or subnet to match
            ipv6: Whether to match IPv6 (default: false)
            country: Country code filter
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing matching internet services

        Example:
            >>> fgt.api.monitor.firewall.internet_service.match(ip='8.8.8.8')
            >>> fgt.api.monitor.firewall.internet_service.match(ip='2001:4860:4860::8888', ipv6=True)
        """
        params = data_dict.copy() if data_dict else {}
        if ip is not None:
            params["ip"] = ip
        if ipv6 is not None:
            params["ipv6"] = ipv6
        if country is not None:
            params["country"] = country
        params.update(kwargs)
        return self._client.get(
            "monitor", "/firewall/internet-service-match", params=params
        )

    def details(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        id: Optional[int] = None,
        region: Optional[int] = None,
        city: Optional[int] = None,
        country: Optional[int] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List all details for a given Internet Service ID.

        Args:
            data_dict: Optional dictionary of parameters
            id: Internet service ID
            region: Region ID filter
            city: City ID filter
            country: Country ID filter
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing internet service details (IPs, ports, protocols)

        Example:
            >>> fgt.api.monitor.firewall.internet_service.details(id=65536)
        """
        params = data_dict.copy() if data_dict else {}
        if id is not None:
            params["id"] = id
        if region is not None:
            params["region"] = region
        if city is not None:
            params["city"] = city
        if country is not None:
            params["country"] = country
        params.update(kwargs)
        return self._client.get(
            "monitor", "/firewall/internet-service-details", params=params
        )

    def reputation(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        ip: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List internet services with reputation information that exist at a given IP.

        Args:
            data_dict: Optional dictionary of parameters
            ip: IP address to check reputation
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing internet services with reputation info

        Example:
            >>> fgt.api.monitor.firewall.internet_service.reputation(ip='8.8.8.8')
        """
        params = data_dict.copy() if data_dict else {}
        if ip is not None:
            params["ip"] = ip
        params.update(kwargs)
        return self._client.get(
            "monitor", "/firewall/internet-service-reputation", params=params
        )
