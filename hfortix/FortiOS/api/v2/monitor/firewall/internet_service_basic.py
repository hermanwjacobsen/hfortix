"""Monitor API - InternetServiceBasic operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class InternetServiceBasic:
    """InternetServiceBasic operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize InternetServiceBasic endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        ipv6_only: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List internet services with basic information.
        
        Args:
            ipv6_only: Only return IPv6 entries. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.internet_service_basic.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if ipv6_only is not None:
            params['ipv6_only'] = ipv6_only
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/internet-service-basic", params=params)
