"""
FortiOS MONITOR - Monitor Log Policy Archive

Monitoring endpoint for monitor log policy archive data.

API Endpoints:
    GET    /monitor/log/policy_archive

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.log.policy_archive.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.log.policy_archive.get(
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
        srcip: str,
        dstip: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
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
            >>> fgt.api.monitor.log.policy_archive.download.get(mkey=1,
            srcip='value', dstip='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["mkey"] = mkey
        params["srcip"] = srcip
        params["dstip"] = dstip
        params.update(kwargs)
        return self._client.get(
            "monitor", "/log/policy-archive/download", params=params
        )


class PolicyArchive:
    """PolicyArchive operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize PolicyArchive endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.download = Download(client)
