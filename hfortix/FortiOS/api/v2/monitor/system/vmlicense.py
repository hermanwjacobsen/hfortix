"""
FortiOS MONITOR - Monitor System Vmlicense

Monitoring endpoint for monitor system vmlicense data.

API Endpoints:
    GET    /monitor/system/vmlicense

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.vmlicense.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.vmlicense.get(
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
        token: str | None = None,
        proxy_url: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Download Flex-VM license and reboot immediately if successful.

        Args:
            token: VM license token. (optional)
            proxy_url: HTTP proxy URL in the form: http://user:pass@proxyip:proxyport. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.vmlicense.download.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if token is not None:
            data["token"] = token
        if proxy_url is not None:
            data["proxy_url"] = proxy_url
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/vmlicense/download", data=data
        )


class DownloadEval:
    """DownloadEval operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize DownloadEval endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        account_id: str | None = None,
        account_password: str | None = None,
        is_government: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Download Evaluation VM License and reboot immediately if successful.

        Args:
            account_id: FortiCare account email. (optional)
            account_password: FortiCare account password. (optional)
            is_government: Is the account in use by a government user?
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.vmlicense.download_eval.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if account_id is not None:
            data["account_id"] = account_id
        if account_password is not None:
            data["account_password"] = account_password
        if is_government is not None:
            data["is_government"] = is_government
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/vmlicense/download-eval", data=data
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
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update VM license using uploaded file.

        Args:
            file_content: Provided when uploading a file: base64 encoded file
            data. Must not contain whitespace or other invalid base64
            characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.vmlicense.upload.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if file_content is not None:
            data["file_content"] = file_content
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/vmlicense/upload", data=data
        )


class Vmlicense:
    """Vmlicense operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Vmlicense endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.download = Download(client)
        self.download_eval = DownloadEval(client)
        self.upload = Upload(client)
