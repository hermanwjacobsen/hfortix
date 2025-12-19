"""Monitor API - AvArchive operations."""

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
        Download file quarantined by AntiVirus.
        
        Args:
            mkey: Checksum for quarantined file. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.log.av_archive.download.get(mkey='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['mkey'] = mkey
        params.update(kwargs)
        return self._client.get("monitor", "/log/av-archive/download", params=params)


class AvArchive:
    """AvArchive operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize AvArchive endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.download = Download(client)
