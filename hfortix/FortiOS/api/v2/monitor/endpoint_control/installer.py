"""
FortiOS MONITOR - Monitor Endpoint Control Installer

Monitoring endpoint for monitor endpoint control installer data.

API Endpoints:
    GET    /monitor/endpoint_control/installer

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.endpoint_control.installer.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.endpoint_control.installer.get(
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
        mkey: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
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
            >>>
            fgt.api.monitor.endpoint_control.installer.download.get(mkey='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["mkey"] = mkey
        params.update(kwargs)
        return self._client.get(
            "monitor", "/endpoint-control/installer/download", params=params
        )


class Installer:
    """Installer operations."""

    def __init__(self, client: "IHTTPClient"):
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
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List available FortiClient installers.

        Args:
            min_version: Filter: Minimum installer version. (String of the
            format n[.n[.n]]). (optional)
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
            params["min_version"] = min_version
        params.update(kwargs)
        return self._client.get(
            "monitor", "/endpoint-control/installer", params=params
        )
