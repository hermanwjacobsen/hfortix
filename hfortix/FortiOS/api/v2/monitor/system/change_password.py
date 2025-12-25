"""
FortiOS MONITOR - Monitor System Change Password

Monitoring endpoint for monitor system change password data.

API Endpoints:
    GET    /monitor/system/change_password

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.change_password.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.change_password.get(
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


class Select:
    """
    Select Operations.

    Provides read-only access for FortiOS select data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: 'IHTTPClient'):
        """
        Initialize Select endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkey: str | None = None,
        old_password: str | None = None,
        new_password: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Save admin and guest-admin passwords.

        Args:
            mkey: User ID for password change. (optional)
            old_password: Old password. (optional)
            new_password: New password. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.change_password.select.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data['mkey'] = mkey
        if old_password is not None:
            data['old_password'] = old_password
        if new_password is not None:
            data['new_password'] = new_password
        data.update(kwargs)
        return self._client.post(
            "monitor",
            "/system/change-password/select",
            data=data
        )


class ChangePassword:
    """ChangePassword operations."""

    def __init__(self, client: 'IHTTPClient'):
        """
        Initialize ChangePassword endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.select = Select(client)
