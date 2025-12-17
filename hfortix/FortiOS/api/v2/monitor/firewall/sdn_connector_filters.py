"""SDN Fabric Connector filter operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class SdnConnectorFilters:
    """SDN Fabric Connector available filters."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize SdnConnectorFilters endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(
        self, data_dict: Optional[Dict[str, Any]] = None, connector: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        List all available filters for all SDN Fabric Connectors.

        Args:
            data_dict: Optional dictionary of parameters
            connector: Filter by connector name
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing SDN connector filters

        Example:
            >>> fgt.api.monitor.firewall.sdn_connector_filters.list()
            >>> fgt.api.monitor.firewall.sdn_connector_filters.list(connector='aws_connector')
        """
        params = data_dict.copy() if data_dict else {}
        if connector is not None:
            params["connector"] = connector
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/sdn-connector-filters", params=params)

    def get(
        self, data_dict: Optional[Dict[str, Any]] = None, connector: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Get available filters for a specific SDN Fabric Connector.

        Args:
            data_dict: Optional dictionary of parameters
            connector: Connector name to retrieve
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing SDN connector filters

        Example:
            >>> fgt.api.monitor.firewall.sdn_connector_filters.get(connector='aws_connector')
        """
        params = data_dict.copy() if data_dict else {}
        if connector is not None:
            params["connector"] = connector
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/sdn-connector-filters", params=params)
