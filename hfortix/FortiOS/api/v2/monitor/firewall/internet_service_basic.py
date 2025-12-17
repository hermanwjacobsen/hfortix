"""Internet service basic information operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class InternetServiceBasic:
    """Internet services with basic information."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize InternetServiceBasic endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(
        self, data_dict: Optional[Dict[str, Any]] = None, id: Optional[int] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        List internet services with basic information.

        Args:
            data_dict: Optional dictionary of parameters
            id: Filter by internet service ID
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing internet services with basic info

        Example:
            >>> fgt.api.monitor.firewall.internet_service_basic.list()
            >>> fgt.api.monitor.firewall.internet_service_basic.list(id=65536)
        """
        params = data_dict.copy() if data_dict else {}
        if id is not None:
            params["id"] = id
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/internet-service-basic", params=params)

    def get(
        self, data_dict: Optional[Dict[str, Any]] = None, id: Optional[int] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Get basic information for a specific internet service.

        Args:
            data_dict: Optional dictionary of parameters
            id: Internet service ID to retrieve
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing internet service basic info

        Example:
            >>> fgt.api.monitor.firewall.internet_service_basic.get(id=65536)
        """
        params = data_dict.copy() if data_dict else {}
        if id is not None:
            params["id"] = id
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/internet-service-basic", params=params)
