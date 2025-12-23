"""
FortiOS MONITOR - Monitor Wifi Firmware

Monitoring endpoint for monitor wifi firmware data.

API Endpoints:
    GET    /monitor/wifi/firmware

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.wifi.firmware.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.wifi.firmware.get(
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

    def post(
        self,
        image_id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Download FortiAP firmware from FortiGuard to the FortiGate according to
        FortiAP image ID.

        Args:
            image_id: FortiAP image ID. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.firmware.download.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if image_id is not None:
            data["image_id"] = image_id
        data.update(kwargs)
        return self._client.post(
            "monitor", "/wifi/firmware/download", data=data
        )


class Push:
    """Push operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Push endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        serial: str | None = None,
        image_id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Push FortiAP firmware to the given device.

        Args:
            serial: The target device's serial. (optional)
            image_id: FortiAP image ID. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.firmware.push.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if serial is not None:
            data["serial"] = serial
        if image_id is not None:
            data["image_id"] = image_id
        data.update(kwargs)
        return self._client.post("monitor", "/wifi/firmware/push", data=data)


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
        serials: str | None = None,
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Upload FortiAP firmware to the management FortiGate and then push to
        target FortiAPs.

        Args:
            serials: The target device's serial. (optional)
            file_content: Provided when uploading a file: base64 encoded file
            data. Must not contain whitespace or other invalid base64
            characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.firmware.upload.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if serials is not None:
            data["serials"] = serials
        if file_content is not None:
            data["file_content"] = file_content
        data.update(kwargs)
        return self._client.post("monitor", "/wifi/firmware/upload", data=data)


class Firmware:
    """Firmware operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Firmware endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.download = Download(client)
        self.push = Push(client)
        self.upload = Upload(client)

    def get(
        self,
        timeout: int | None = None,
        version: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a list of current and recommended firmware for FortiAPs in
        use.

        Args:
            timeout: FortiGuard connection timeout (defaults to 2 seconds).
            (optional)
            version: Target firmware version of the parent FortiGate.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.firmware.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if timeout is not None:
            params["timeout"] = timeout
        if version is not None:
            params["version"] = version
        params.update(kwargs)
        return self._client.get("monitor", "/wifi/firmware", params=params)
