"""
FortiOS MONITOR - Monitor System Config Script

Monitoring endpoint for monitor system config script data.

API Endpoints:
    GET    /monitor/system/config_script

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.config_script.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.config_script.get(
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


class Delete:
    """
    Delete Operations.

    Provides read-only access for FortiOS delete data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Delete endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        id_list: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete the history of config scripts.

        Args:
            id_list: List of config script history ids to delete. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.config_script.delete.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if id_list is not None:
            data["id_list"] = id_list
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/config-script/delete", data=data
        )


class Run:
    """Run operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Run endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        remote_script: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Run remote config scripts.

        Args:
            remote_script: Name of remote config script to run. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.config_script.run.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if remote_script is not None:
            data["remote_script"] = remote_script
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/config-script/run", data=data
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
        Upload and run a new configuration script file.

        Args:
            filename: Name of configuration script file. (optional)
            file_content: Provided when uploading a file: base64 encoded file
            data. Must not contain whitespace or other invalid base64
            characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.config_script.upload.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if filename is not None:
            data["filename"] = filename
        if file_content is not None:
            data["file_content"] = file_content
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/config-script/upload", data=data
        )


class ConfigScript:
    """ConfigScript operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ConfigScript endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.delete = Delete(client)
        self.run = Run(client)
        self.upload = Upload(client)

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve the information about config scripts.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.config_script.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/config-script", params=params
        )
