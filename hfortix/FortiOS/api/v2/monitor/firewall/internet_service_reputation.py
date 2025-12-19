"""Monitor API - InternetServiceReputation operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class InternetServiceReputation:
    """InternetServiceReputation operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize InternetServiceReputation endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        ip: str,
        is_ipv6: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List internet services with reputation information that exist at a given IP.
        
        Args:
            ip: IP (in dot-decimal notation). (required)
            is_ipv6: Whether IP is IPv6. If not provided, will determine IP version based on given IP, but setting is_ipv6 flag is recommended. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.internet_service_reputation.get(ip='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['ip'] = ip
        if is_ipv6 is not None:
            params['is_ipv6'] = is_ipv6
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/internet-service-reputation", params=params)
