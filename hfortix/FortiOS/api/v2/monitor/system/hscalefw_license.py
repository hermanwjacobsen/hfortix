"""
FortiOS MONITOR - Monitor System Hscalefw License

Monitoring endpoint for monitor system hscalefw license data.

API Endpoints:
    GET    /monitor/system/hscalefw_license

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.hscalefw_license.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.hscalefw_license.get(
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


class Upload:
    """
    Upload Operations.

    Provides read-only access for FortiOS upload data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Upload endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        license_key: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update Hyperscale firewall license for hardware acceleration using
        license key.

        Args:
            license_key: License key. Format:0000-0000-0000-0000-0000-0000-00.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.hscalefw_license.upload.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if license_key is not None:
            data["license_key"] = license_key
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/hscalefw-license/upload", data=data
        )


class HscalefwLicense:
    """HscalefwLicense operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize HscalefwLicense endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.upload = Upload(client)
