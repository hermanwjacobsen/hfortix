"""Monitor API - ForticloudReport operations."""

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
        report_name: str,
        inline: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Download PDF report from FortiCloud.
        
        Args:
            mkey: FortiCloud Report ID. (required)
            report_name: Full filename of the report. (required)
            inline: Set to 1 to download the report inline. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.log.forticloud_report.download.get(mkey=1, report_name='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['mkey'] = mkey
        params['report_name'] = report_name
        if inline is not None:
            params['inline'] = inline
        params.update(kwargs)
        return self._client.get("monitor", "/log/forticloud-report/download", params=params)


class ForticloudReport:
    """ForticloudReport operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ForticloudReport endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.download = Download(client)
