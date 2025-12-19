"""Monitor API - ApplicationList operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Refresh:
    """Refresh operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Refresh endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        last_update_time: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update the Azure application list data or get the status of an update.
        
        Args:
            last_update_time: Timestamp of a previous update request. If this is not provided then it will refresh the Azure application list data. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.azure.application_list.refresh.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if last_update_time is not None:
            data['last_update_time'] = last_update_time
        data.update(kwargs)
        return self._client.post("monitor", "/azure/application-list/refresh", data=data)


class ApplicationList:
    """ApplicationList operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ApplicationList endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.refresh = Refresh(client)

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve a list of Azure applications that can be used for configuring an Azure SDN connector.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.azure.application_list.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/azure/application-list", params=params)
