"""Monitor API - IslLockdown operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Status:
    """Status operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Status endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        fortilink: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get current status of ISL lockdown.
        
        Args:
            fortilink: FortiLink interface name. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.switch_controller.isl_lockdown.status.get(fortilink='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['fortilink'] = fortilink
        params.update(kwargs)
        return self._client.get("monitor", "/switch-controller/isl-lockdown/status", params=params)


class Update:
    """Update operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Update endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        fortilink: str | None = None,
        status: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Enable/disable ISL lockdown.
        
        Args:
            fortilink: FortiLink interface name. (optional)
            status: To enable or disable lockdown. [enable|disable] (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.switch_controller.isl_lockdown.update.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if fortilink is not None:
            data['fortilink'] = fortilink
        if status is not None:
            data['status'] = status
        data.update(kwargs)
        return self._client.post("monitor", "/switch-controller/isl-lockdown/update", data=data)


class IslLockdown:
    """IslLockdown operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize IslLockdown endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.status = Status(client)
        self.update = Update(client)
