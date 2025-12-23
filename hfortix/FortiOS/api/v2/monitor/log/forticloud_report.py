"""
FortiOS MONITOR - Monitor Log Forticloud Report

Monitoring endpoint for monitor log forticloud report data.

API Endpoints:
    GET    /monitor/log/forticloud_report

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.log.forticloud_report.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.log.forticloud_report.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class Download:
    """
    Download Operations.

    Provides read-only access for FortiOS download data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
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
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
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
            >>> fgt.api.monitor.log.forticloud_report.download.get(mkey=1,
            report_name='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["mkey"] = mkey
        params["report_name"] = report_name
        if inline is not None:
            params["inline"] = inline
        params.update(kwargs)
        return self._client.get(
            "monitor", "/log/forticloud-report/download", params=params
        )


class ForticloudReport:
    """ForticloudReport operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ForticloudReport endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.download = Download(client)
