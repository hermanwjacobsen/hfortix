"""Monitor API - SdnConnectorFilters operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class SdnConnectorFilters:
    """SdnConnectorFilters operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize SdnConnectorFilters endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        connector: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List all available filters for a specified SDN Fabric Connector.
        
        Args:
            connector: Name of the SDN Fabric Connector to get the filters from. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.sdn_connector_filters.get(connector='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['connector'] = connector
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/sdn-connector-filters", params=params)
