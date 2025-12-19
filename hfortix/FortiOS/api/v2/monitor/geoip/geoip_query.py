"""Monitor API - GeoipQuery operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Select:
    """Select operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Select endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        ip_addresses: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve location details for IPs queried against FortiGuard's geoip service.
        
        Args:
            ip_addresses: One or more IP address strings to query for location details. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.geoip.geoip_query.select.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if ip_addresses is not None:
            data['ip_addresses'] = ip_addresses
        data.update(kwargs)
        return self._client.post("monitor", "/geoip/geoip-query/select", data=data)


class GeoipQuery:
    """GeoipQuery operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize GeoipQuery endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.select = Select(client)
