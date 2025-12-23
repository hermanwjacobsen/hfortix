"""
FortiOS MONITOR - Monitor System Firmware

Monitoring endpoint for monitor system firmware data.

API Endpoints:
    GET    /monitor/system/firmware

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.firmware.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.firmware.get(
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


class Upgrade:
    """
    Upgrade Operations.

    Provides read-only access for FortiOS upgrade data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Upgrade endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        source: str | None = None,
        url: str | None = None,
        passphrase: str | None = None,
        force: bool | None = None,
        filename: str | None = None,
        format_partition: bool | None = None,
        ignore_invalid_signature: bool | None = None,
        file_id: str | None = None,
        ignore_admin_lockout_upon_downgrade: bool | None = None,
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Upgrade firmware image on this device.

        Args:
            source: Firmware file data source [upload|usb|fortiguard|url].
            (optional)
            url: URL where the image should be retrieved from. (optional)
            passphrase: Image encryption passphrase. (optional)
            force: Bypass signature and validity checking. (optional)
            filename: Name of file on USB disk to upgrade to, or ID from
            FortiGuard available firmware. (optional)
            format_partition: Set to true to format boot partition before
            upgrade. (optional)
            ignore_invalid_signature: Set to true to allow upgrade of firmware
            images with invalid signatures. (optional)
            file_id: File ID of the uploaded firmware image to allow upgrade of
            firmware images with invalid signatures. (optional)
            ignore_admin_lockout_upon_downgrade: Set to true to allow
            dowgrading if the firmware doesn't support safer password and there
            is at least 1 admin that will be locked out after upgrade.
            (optional)
            file_content: Provided when uploading a file: base64 encoded file
            data. Must not contain whitespace or other invalid base64
            characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.firmware.upgrade.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if source is not None:
            data["source"] = source
        if url is not None:
            data["url"] = url
        if passphrase is not None:
            data["passphrase"] = passphrase
        if force is not None:
            data["force"] = force
        if filename is not None:
            data["filename"] = filename
        if format_partition is not None:
            data["format_partition"] = format_partition
        if ignore_invalid_signature is not None:
            data["ignore_invalid_signature"] = ignore_invalid_signature
        if file_id is not None:
            data["file_id"] = file_id
        if ignore_admin_lockout_upon_downgrade is not None:
            data["ignore_admin_lockout_upon_downgrade"] = (
                ignore_admin_lockout_upon_downgrade
            )
        if file_content is not None:
            data["file_content"] = file_content
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/firmware/upgrade", data=data
        )


class UpgradePaths:
    """UpgradePaths operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize UpgradePaths endpoint.

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
        Retrieve a list of supported firmware upgrade paths.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.firmware.upgrade_paths.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/firmware/upgrade-paths", params=params
        )


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
        self.upgrade = Upgrade(client)
        self.upgrade_paths = UpgradePaths(client)

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a list of firmware images available to use for upgrade on this
        device.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.firmware.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/system/firmware", params=params)
