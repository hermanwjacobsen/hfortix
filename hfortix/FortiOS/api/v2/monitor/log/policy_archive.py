"""Monitor API - PolicyArchive operations."""

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
        mkey: int,
        srcip: str,
        dstip: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Download policy-based packet capture archive.
        
        Args:
            mkey: Session ID (from traffic log). (required)
            srcip: Source IP. (required)
            dstip: Destination IP. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.log.policy_archive.download.get(mkey=1, srcip='value', dstip='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['mkey'] = mkey
        params['srcip'] = srcip
        params['dstip'] = dstip
        params.update(kwargs)
        return self._client.get("monitor", "/log/policy-archive/download", params=params)


class PolicyArchive:
    """PolicyArchive operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize PolicyArchive endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.download = Download(client)
