"""Monitor API - Override operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Delete:
    """Delete operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Delete endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkey: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete a configured webfilter override.
        
        Args:
            mkey: ID of webfilter override to delete. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.webfilter.override.delete.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data['mkey'] = mkey
        data.update(kwargs)
        return self._client.post("monitor", "/webfilter/override/delete", data=data)


class Override:
    """Override operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Override endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.delete = Delete(client)

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List all administrative and user initiated webfilter overrides.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.webfilter.override.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/webfilter/override", params=params)
