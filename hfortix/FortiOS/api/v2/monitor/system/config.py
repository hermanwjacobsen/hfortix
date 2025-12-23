"""
FortiOS MONITOR - Monitor System Config

Monitoring endpoint for monitor system config data.

API Endpoints:
    GET    /monitor/system/config

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.config.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.config.get(
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


class Backup:
    """
    Backup Operations.

    Provides read-only access for FortiOS backup data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Backup endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        destination: str | None = None,
        usb_filename: str | None = None,
        password: str | None = None,
        scope: str | None = None,
        vdom: str | None = None,
        password_mask: bool | None = None,
        file_format: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
                Backup system config
        Access Group: sysgrp.

                Args:
                    destination: Configuration file destination [file* | usb].
                    (optional)
                    usb_filename: When using 'usb' destination: the filename to
                    save to on the connected USB device. (optional)
                    password: Password to encrypt configuration data.
                    (optional)
                    scope: Specify global or VDOM only backup [global | vdom].
                    (optional)
                    vdom: If 'vdom' scope specified, the name of the VDOM to
                    backup configuration. (optional)
                    password_mask: True to replace all the secrects and
                    passwords with a mask. (optional)
                    file_format: Configuration file format [fos* | yaml].
                    (optional)
                    payload_dict: Optional dictionary of parameters
                    raw_json: Return raw JSON response if True
                    **kwargs: Additional parameters as keyword arguments

                Returns:
                    Dictionary containing API response

                Example:
                    >>> fgt.api.monitor.system.config.backup.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if destination is not None:
            data["destination"] = destination
        if usb_filename is not None:
            data["usb_filename"] = usb_filename
        if password is not None:
            data["password"] = password
        if scope is not None:
            data["scope"] = scope
        if vdom is not None:
            data["vdom"] = vdom
        if password_mask is not None:
            data["password_mask"] = password_mask
        if file_format is not None:
            data["file_format"] = file_format
        data.update(kwargs)
        return self._client.post("monitor", "/system/config/backup", data=data)


class Restore:
    """Restore operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Restore endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        source: str | None = None,
        usb_filename: str | None = None,
        config_id: int | None = None,
        password: str | None = None,
        scope: str | None = None,
        vdom: str | None = None,
        confirm_password_mask: bool | None = None,
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Restore system configuration from uploaded file or from USB.

        Args:
            source: Configuration file data source [upload | usb | revision].
            (optional)
            usb_filename: When using 'usb' source: the filename to restore from
            the connected USB device. (optional)
            config_id: When using 'revision' source: valid ID of configuration
            stored on disk to revert to. (optional)
            password: Password to decrypt configuration data. (optional)
            scope: Specify global or VDOM only restore [global | vdom].
            (optional)
            vdom: If 'vdom' scope specified, the name of the VDOM to restore
            configuration. (optional)
            confirm_password_mask: True to upload password mask config file.
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
            >>> fgt.api.monitor.system.config.restore.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if source is not None:
            data["source"] = source
        if usb_filename is not None:
            data["usb_filename"] = usb_filename
        if config_id is not None:
            data["config_id"] = config_id
        if password is not None:
            data["password"] = password
        if scope is not None:
            data["scope"] = scope
        if vdom is not None:
            data["vdom"] = vdom
        if confirm_password_mask is not None:
            data["confirm_password_mask"] = confirm_password_mask
        if file_content is not None:
            data["file_content"] = file_content
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/config/restore", data=data
        )


class RestoreStatus:
    """RestoreStatus operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize RestoreStatus endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        session_id: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Check the status of the restoring system configuration session.

        Args:
            session_id: Session ID for restoring configuration. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.system.config.restore_status.get(session_id='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["session_id"] = session_id
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/config/restore-status", params=params
        )


class UsbFilelist:
    """UsbFilelist operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize UsbFilelist endpoint.

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
        List configuration files available on connected USB drive.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.config.usb_filelist.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/config/usb-filelist", params=params
        )


class Config:
    """Config operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Config endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.backup = Backup(client)
        self.restore = Restore(client)
        self.restore_status = RestoreStatus(client)
        self.usb_filelist = UsbFilelist(client)
