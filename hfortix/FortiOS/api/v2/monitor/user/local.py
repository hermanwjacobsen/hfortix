"""
FortiOS MONITOR - Monitor User Local

Monitoring endpoint for monitor user local data.

API Endpoints:
    GET    /monitor/user/local

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.user.local.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.user.local.get(
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


class ChangePassword:
    """
    Changepassword Operations.

    Provides read-only access for FortiOS changepassword data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ChangePassword endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        username: str | None = None,
        new_password: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Change password for local user.

        Args:
            username: User name. (optional)
            new_password: Password. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.local.change_password.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if username is not None:
            data["username"] = username
        if new_password is not None:
            data["new_password"] = new_password
        data.update(kwargs)
        return self._client.post(
            "monitor", "/user/local/change-password", data=data
        )


class Local:
    """Local operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Local endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.change_password = ChangePassword(client)
