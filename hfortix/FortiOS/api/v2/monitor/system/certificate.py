"""
FortiOS MONITOR - Monitor System Certificate

Monitoring endpoint for monitor system certificate data.

API Endpoints:
    GET    /monitor/system/certificate

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.certificate.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.certificate.get(
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
        type: str,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Download certificate.

        Args:
            mkey: Name of certificate. (required)
            type: Type of certificate
            [local-cer|remote-cer|local-ca|remote-ca|local-csr|crl]. (required)
            scope: Scope of certificate [vdom*|global]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.certificate.download.get(mkey='value',
            type='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["mkey"] = mkey
        params["type"] = type
        if scope is not None:
            params["scope"] = scope
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/certificate/download", params=params
        )


class ReadInfo:
    """ReadInfo operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ReadInfo endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        value: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get certificate information from a certificate string.

        Args:
            value: PEM formatted certificate. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.certificate.read_info.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if value is not None:
            data["value"] = value
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/certificate/read-info", data=data
        )


class Certificate:
    """Certificate operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Certificate endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.download = Download(client)
        self.read_info = ReadInfo(client)
