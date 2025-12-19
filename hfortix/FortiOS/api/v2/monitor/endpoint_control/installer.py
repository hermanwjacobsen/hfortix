"""Monitor API - Installer operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Download:
    """Download operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Download endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Download a FortiClient installer via FortiGuard.
        
        Args:
            mkey: Name of installer (image_id). (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.endpoint_control.installer.download.get(mkey='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['mkey'] = mkey
        params.update(kwargs)
        return self._client.get("monitor", "/endpoint-control/installer/download", params=params)


class Installer:
    """Installer operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Installer endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.download = Download(client)

    def get(
        self,
        min_version: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List available FortiClient installers.
        
        Args:
            min_version: Filter: Minimum installer version. (String of the format n[.n[.n]]). (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.endpoint_control.installer.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if min_version is not None:
            params['min_version'] = min_version
        params.update(kwargs)
        return self._client.get("monitor", "/endpoint-control/installer", params=params)
