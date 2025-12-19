"""Monitor API - AppLookup operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class AppLookup:
    """AppLookup operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize AppLookup endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        hosts: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Query ISDB to resolve hosts to application control entries.
        
        Args:
            hosts: List of hosts to resolve. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.utm.app_lookup.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if hosts is not None:
            params['hosts'] = hosts
        params.update(kwargs)
        return self._client.get("monitor", "/utm/app-lookup", params=params)
