"""Monitor API - Fortiguard operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class LiveServicesLatency:
    """LiveServicesLatency operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize LiveServicesLatency endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get latency information for live FortiGuard services.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.network.fortiguard.live_services_latency.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/network/fortiguard/live-services-latency", params=params)


class Fortiguard:
    """Fortiguard operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Fortiguard endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.live_services_latency = LiveServicesLatency(client)
