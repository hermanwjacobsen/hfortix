"""
FortiOS MONITOR - Monitor System Config Revision

Monitoring endpoint for monitor system config revision data.

API Endpoints:
    GET    /monitor/system/config_revision

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.config_revision.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.config_revision.get(
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
        config_ids: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Deletes one or more system configuration revisions.

        Args:
            config_ids: List of configuration ids. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.config_revision.delete.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if config_ids is not None:
            data["config_ids"] = config_ids
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/config-revision/delete", data=data
        )


class File:
    """File operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize File endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        config_id: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Download a specific configuration revision.

        Args:
            config_id: Configuration id. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.config_revision.file.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if config_id is not None:
            params["config_id"] = config_id
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/config-revision/file", params=params
        )


class Info:
    """Info operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Info endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        config_id: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve meta information for a specific configuration revision.

        Args:
            config_id: Configuration id. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.config_revision.info.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if config_id is not None:
            params["config_id"] = config_id
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/config-revision/info", params=params
        )


class Save:
    """Save operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Save endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        comments: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create a new config revision checkpoint.

        Args:
            comments: Optional revision comments (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.config_revision.save.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if comments is not None:
            data["comments"] = comments
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/config-revision/save", data=data
        )


class UpdateComments:
    """UpdateComments operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize UpdateComments endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        config_id: int | None = None,
        comments: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Updates comments for a system configuration file.

        Args:
            config_id: Configuration id. (optional)
            comments: Configuration comments. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.config_revision.update_comments.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if config_id is not None:
            data["config_id"] = config_id
        if comments is not None:
            data["comments"] = comments
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/config-revision/update-comments", data=data
        )


class ConfigRevision:
    """ConfigRevision operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ConfigRevision endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.delete = Delete(client)
        self.file = File(client)
        self.info = Info(client)
        self.save = Save(client)
        self.update_comments = UpdateComments(client)

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Returns a list of system configuration revisions.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.config_revision.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/config-revision", params=params
        )
