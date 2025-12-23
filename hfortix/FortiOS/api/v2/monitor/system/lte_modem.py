"""
FortiOS MONITOR - Monitor System Lte Modem

Monitoring endpoint for monitor system lte modem data.

API Endpoints:
    GET    /monitor/system/lte_modem

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.lte_modem.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.lte_modem.get(
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


class Status:
    """
    Status Operations.

    Provides read-only access for FortiOS status data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Status endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve the LTE modem status.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.lte_modem.status.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/lte-modem/status", params=params
        )


class Upgrade:
    """Upgrade operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Upgrade endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Upgrade LTE modem firmware image on this device using uploaded files.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.lte_modem.upgrade.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/lte-modem/upgrade", data=data
        )


class Upload:
    """Upload operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Upload endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        filename: str | None = None,
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Upload the modem firmware upgrade files.

        Args:
            filename: Firmware file being uploaded. (optional)
            file_content: Provided when uploading a file: base64 encoded file
            data. Must not contain whitespace or other invalid base64
            characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.lte_modem.upload.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if filename is not None:
            data["filename"] = filename
        if file_content is not None:
            data["file_content"] = file_content
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/lte-modem/upload", data=data
        )


class LteModem:
    """LteModem operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize LteModem endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.status = Status(client)
        self.upgrade = Upgrade(client)
        self.upload = Upload(client)
