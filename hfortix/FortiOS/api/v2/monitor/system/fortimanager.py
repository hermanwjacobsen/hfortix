"""
FortiOS MONITOR - Monitor System Fortimanager

Monitoring endpoint for monitor system fortimanager data.

API Endpoints:
    GET    /monitor/system/fortimanager

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.fortimanager.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.fortimanager.get(
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


class BackupAction:
    """
    Backupaction Operations.

    Provides read-only access for FortiOS backupaction data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize BackupAction endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        operation: str | None = None,
        objects: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Import or update from FortiManager objects.

        Args:
            operation: Operation to perform on the given CMDB objects
            [import|update]. (optional)
            objects: Array of CMDB tables and mkeys. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.fortimanager.backup_action.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if operation is not None:
            data["operation"] = operation
        if objects is not None:
            data["objects"] = objects
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/fortimanager/backup-action", data=data
        )


class BackupDetails:
    """BackupDetails operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize BackupDetails endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str,
        datasource: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get the properties of a FortiManager object.

        Args:
            mkey: Object name. (required)
            datasource: Object datasource. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.system.fortimanager.backup_details.get(mkey='value',
            datasource='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["mkey"] = mkey
        params["datasource"] = datasource
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/fortimanager/backup-details", params=params
        )


class BackupSummary:
    """BackupSummary operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize BackupSummary endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get FortiManager backup summary.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.fortimanager.backup_summary.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/fortimanager/backup-summary", params=params
        )


class Fortimanager:
    """Fortimanager operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Fortimanager endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.backup_action = BackupAction(client)
        self.backup_details = BackupDetails(client)
        self.backup_summary = BackupSummary(client)
