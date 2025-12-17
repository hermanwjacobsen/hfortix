"""Internet service lookup and matching operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class InternetService:
    """Internet service matching and lookup operations."""

    def __init__(self, client: "HTTPClient"):
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
        return self._client.get("monitor", "/firewall/internet-service-match", params=params)

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
        return self._client.get("monitor", "/firewall/internet-service-details", params=params)

    def reputation(
        self, data_dict: Optional[Dict[str, Any]] = None, ip: Optional[str] = None, **kwargs
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
        return self._client.get("monitor", "/firewall/internet-service-reputation", params=params)
