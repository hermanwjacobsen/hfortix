"""Monitor API - Ipv4 operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Ipv4:
    """Ipv4 operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Ipv4 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        operator: str | None = None,
        ip_mask: str | None = None,
        gateway: str | None = None,
        type: str | None = None,
        origin: str | None = None,
        interface: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List all active IPv4 routing table entries.
        
        Args:
            operator: Filter logic [*and|or]. (optional)
            ip_mask: Filter: IP/netmask. (optional)
            gateway: Filter: gateway. (optional)
            type: Filter: route type. (optional)
            origin: Filter: router origin. (optional)
            interface: Filter: interface name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.router.ipv4.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if operator is not None:
            params['operator'] = operator
        if ip_mask is not None:
            params['ip_mask'] = ip_mask
        if gateway is not None:
            params['gateway'] = gateway
        if type is not None:
            params['type'] = type
        if origin is not None:
            params['origin'] = origin
        if interface is not None:
            params['interface'] = interface
        params.update(kwargs)
        return self._client.get("monitor", "/router/ipv4", params=params)
