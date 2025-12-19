"""Monitor API - HealthCheck operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class HealthCheck:
    """HealthCheck operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize HealthCheck endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        health_check_name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve health-check statistics for each SD-WAN link.
        
        Args:
            health_check_name: Health check name. If not provided, will return results of all health checks. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.virtual_wan.health_check.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if health_check_name is not None:
            params['health_check_name'] = health_check_name
        params.update(kwargs)
        return self._client.get("monitor", "/virtual-wan/health-check", params=params)
