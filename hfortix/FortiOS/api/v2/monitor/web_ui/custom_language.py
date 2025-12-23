"""
FortiOS MONITOR - Monitor Web Ui Custom Language

Monitoring endpoint for monitor web ui custom language data.

API Endpoints:
    GET    /monitor/web_ui/custom_language

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.web_ui.custom_language.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.web_ui.custom_language.get(
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


class Create:
    """
    Create Operations.

    Provides read-only access for FortiOS create data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Create endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        lang_name: str | None = None,
        lang_comments: str | None = None,
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Upload custom language file to this Fortigate.

        Args:
            lang_name: Name of custom language entry. (optional)
            lang_comments: Comments of custom language entry. (optional)
            file_content: Provided when uploading a file: base64 encoded file
            data. Must not contain whitespace or other invalid base64
            characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.web_ui.custom_language.create.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if lang_name is not None:
            data["lang_name"] = lang_name
        if lang_comments is not None:
            data["lang_comments"] = lang_comments
        if file_content is not None:
            data["file_content"] = file_content
        data.update(kwargs)
        return self._client.post(
            "monitor", "/web-ui/custom-language/create", data=data
        )


class Download:
    """Download operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Download endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        lang_name: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Download a custom language file.

        Args:
            lang_name: Name of custom language entry. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.web_ui.custom_language.download.get(lang_name='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["lang_name"] = lang_name
        params.update(kwargs)
        return self._client.get(
            "monitor", "/web-ui/custom-language/download", params=params
        )


class Update:
    """Update operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Update endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkey: str | None = None,
        lang_name: str | None = None,
        lang_comments: str | None = None,
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update custom language file to this Fortigate.

        Args:
            mkey: Name of custom language entry. (optional)
            lang_name: New name of custom language entry. (optional)
            lang_comments: Comments of custom language entry. (optional)
            file_content: Provided when uploading a file: base64 encoded file
            data. Must not contain whitespace or other invalid base64
            characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.web_ui.custom_language.update.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data["mkey"] = mkey
        if lang_name is not None:
            data["lang_name"] = lang_name
        if lang_comments is not None:
            data["lang_comments"] = lang_comments
        if file_content is not None:
            data["file_content"] = file_content
        data.update(kwargs)
        return self._client.post(
            "monitor", "/web-ui/custom-language/update", data=data
        )


class CustomLanguage:
    """CustomLanguage operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize CustomLanguage endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.create = Create(client)
        self.download = Download(client)
        self.update = Update(client)
