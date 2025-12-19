"""Monitor API - Fortimanager operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class BackupAction:
    """BackupAction operations."""

    def __init__(self, client: 'HTTPClient'):
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
    ) -> dict[str, Any]:
        """
        Import or update from FortiManager objects.
        
        Args:
            operation: Operation to perform on the given CMDB objects [import|update]. (optional)
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
            data['operation'] = operation
        if objects is not None:
            data['objects'] = objects
        data.update(kwargs)
        return self._client.post("monitor", "/system/fortimanager/backup-action", data=data)


class BackupDetails:
    """BackupDetails operations."""

    def __init__(self, client: 'HTTPClient'):
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
    ) -> dict[str, Any]:
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
            >>> fgt.api.monitor.system.fortimanager.backup_details.get(mkey='value', datasource='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['mkey'] = mkey
        params['datasource'] = datasource
        params.update(kwargs)
        return self._client.get("monitor", "/system/fortimanager/backup-details", params=params)


class BackupSummary:
    """BackupSummary operations."""

    def __init__(self, client: 'HTTPClient'):
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
    ) -> dict[str, Any]:
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
        return self._client.get("monitor", "/system/fortimanager/backup-summary", params=params)


class Fortimanager:
    """Fortimanager operations."""

    def __init__(self, client: 'HTTPClient'):
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
