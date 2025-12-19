"""Monitor API - NetworkServiceDynamic operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class NetworkServiceDynamic:
    """NetworkServiceDynamic operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize NetworkServiceDynamic endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        mkey: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List of dynamic network service IP address and port pairs.
        
        Args:
            mkey: Name of the dynamic network service entry. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.network_service_dynamic.get(mkey='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['mkey'] = mkey
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/network-service-dynamic", params=params)
