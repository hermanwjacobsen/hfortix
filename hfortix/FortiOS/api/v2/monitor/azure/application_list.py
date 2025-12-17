"""
Azure Application List endpoint

GET    /api/v2/monitor/azure/application-list
POST   /api/v2/monitor/azure/application-list/refresh
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["ApplicationList"]


class ApplicationList:
    """
    Azure Application List operations.

    Retrieve and refresh Azure applications for SDN connector configuration.
    """

    def __init__(self, client: "HTTPClient"):
        """
        Initialize ApplicationList endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client
        self._base_path = "azure/application-list"

    def list(self) -> dict[str, Any]:
        """
        Retrieve a list of Azure applications.

        Get a list of Azure applications that can be used for configuring
        an Azure SDN connector.

        Returns:
            dict: Response containing list of Azure applications

        Raises:
            FortinetError: If the API request fails

        Example:
            >>> apps = fgt.api.monitor.azure.application_list.list()
            >>> for app in apps.get("results", []):
            ...     print(f"{app['name']}: {app['id']}")
        """
        return self._client.get("monitor", self._base_path)

    def refresh(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        last_update_time: Optional[int] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update the Azure application list data or get refresh status.

        Triggers an update of the Azure application list from Azure services,
        or retrieves the status of an ongoing update operation.

        Args:
            data_dict: Dictionary containing body parameters
            last_update_time: Timestamp of previous update request. If not provided,
                            refreshes Azure application list data.
            **kwargs: Additional parameters

        Returns:
            dict: Response containing refresh status or confirmation

        Raises:
            FortinetError: If the API request fails

        Examples:
            >>> # Start new refresh (empty body)
            >>> result = fgt.api.monitor.azure.application_list.refresh()

            >>> # Refresh with timestamp using dict
            >>> result = fgt.api.monitor.azure.application_list.refresh(
            ...     data_dict={'last_update_time': 1234567890}
            ... )

            >>> # Refresh with timestamp using keyword
            >>> result = fgt.api.monitor.azure.application_list.refresh(
            ...     last_update_time=1234567890
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        # Map parameters
        if last_update_time is not None:
            data["last_update_time"] = last_update_time

        # Add any additional kwargs
        data.update(kwargs)

        return self._client.post("monitor", f"{self._base_path}/refresh", data=data)
