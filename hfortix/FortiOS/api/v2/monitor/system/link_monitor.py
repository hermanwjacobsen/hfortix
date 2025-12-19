"""Monitor API - LinkMonitor operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class LinkMonitor:
    """LinkMonitor operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize LinkMonitor endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        mkey: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve per-interface statistics for active link monitors.
        
        Args:
            mkey: Name of link monitor. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.link_monitor.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params['mkey'] = mkey
        params.update(kwargs)
        return self._client.get("monitor", "/system/link-monitor", params=params)
