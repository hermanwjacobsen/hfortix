"""
FortiOS MONITOR - Monitor System Admin

Monitoring endpoint for monitor system admin data.

API Endpoints:
    GET    /monitor/system/admin

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.admin.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.admin.get(
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


class ChangeVdomMode:
    """
    Changevdommode Operations.

    Provides read-only access for FortiOS changevdommode data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ChangeVdomMode endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        vdom_mode: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Switch between VDOM modes.

        Args:
            vdom_mode: VDOM mode [no-vdom|split-vdom|multi-vdom] (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.admin.change_vdom_mode.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if vdom_mode is not None:
            data["vdom-mode"] = vdom_mode
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/admin/change-vdom-mode", data=data
        )


class Admin:
    """Admin operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Admin endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.change_vdom_mode = ChangeVdomMode(client)
