"""Monitor API - CentralManagement operations."""

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
        skip_detect: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get Central Management status.
        
        Args:
            skip_detect: Skip sending a detect message to the central management device. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.central_management.status.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if skip_detect is not None:
            params['skip_detect'] = skip_detect
        params.update(kwargs)
        return self._client.get("monitor", "/system/central-management/status", params=params)


class CentralManagement:
    """CentralManagement operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize CentralManagement endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.status = Status(client)
