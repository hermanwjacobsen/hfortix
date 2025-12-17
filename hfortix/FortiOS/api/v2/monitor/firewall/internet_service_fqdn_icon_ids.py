"""Internet service FQDN icon ID mapping operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class InternetServiceFqdnIconIds:
    """Internet service FQDN icon ID mappings."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize InternetServiceFqdnIconIds endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Map of internet service FQDN icon IDs.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing internet service FQDN icon ID mappings

        Example:
            >>> fgt.api.monitor.firewall.internet_service_fqdn_icon_ids.list()
        """
        params = data_dict.copy() if data_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/firewall/internet-service-fqdn-icon-ids", params=params
        )
