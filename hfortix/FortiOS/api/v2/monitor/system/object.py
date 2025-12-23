"""
FortiOS MONITOR - Monitor System Object

Monitoring endpoint for monitor system object data.

API Endpoints:
    GET    /monitor/system/object

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.object.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.object.get(
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


class Usage:
    """
    Usage Operations.

    Provides read-only access for FortiOS usage data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Usage endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        q_path: str | None = None,
        q_name: str | None = None,
        qtypes: list | None = None,
        scope: str | None = None,
        mkey: str | None = None,
        child_path: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve all objects that are currently using as well as objects that
        can use the given object.

        Args:
            q_path: The CMDB table's path (optional)
            q_name: The CMDB table's name (optional)
            qtypes: List of CMDB table qTypes (optional)
            scope: Scope of resource [vdom|global]. (optional)
            mkey: The mkey for the object (optional)
            child_path: The child path for the object (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.object.usage.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if q_path is not None:
            params["q_path"] = q_path
        if q_name is not None:
            params["q_name"] = q_name
        if qtypes is not None:
            params["qtypes"] = qtypes
        if scope is not None:
            params["scope"] = scope
        if mkey is not None:
            params["mkey"] = mkey
        if child_path is not None:
            params["child_path"] = child_path
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/object/usage", params=params
        )


class Object:
    """Object operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Object endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.usage = Usage(client)
