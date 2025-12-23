"""
FortiOS MONITOR - Monitor Azure Application List

Monitoring endpoint for monitor azure application list data.

API Endpoints:
    GET    /monitor/azure/application_list

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.azure.application_list.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.azure.application_list.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class Refresh:
    """
    Refresh Operations.

    Provides read-only access for FortiOS refresh data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
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
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update the Azure application list data or get the status of an update.

        Args:
            last_update_time: Timestamp of a previous update request. If this
            is not provided then it will refresh the Azure application list
            data. (optional)
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
            data["last_update_time"] = last_update_time
        data.update(kwargs)
        return self._client.post(
            "monitor", "/azure/application-list/refresh", data=data
        )


class ApplicationList:
    """ApplicationList operations."""

    def __init__(self, client: "IHTTPClient"):
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
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a list of Azure applications that can be used for configuring
        an Azure SDN connector.

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
        return self._client.get(
            "monitor", "/azure/application-list", params=params
        )
