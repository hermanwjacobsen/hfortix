"""
FortiOS MONITOR - Monitor User Password Policy Conform

Monitoring endpoint for monitor user password policy conform data.

API Endpoints:
    GET    /monitor/user/password_policy_conform

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.user.password_policy_conform.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.user.password_policy_conform.get(
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

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Select endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        username: str | None = None,
        password: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Check if password adheres to local user password policy.

        Args:
            username: User name. (optional)
            password: Password. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.password_policy_conform.select.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if username is not None:
            data["username"] = username
        if password is not None:
            data["password"] = password
        data.update(kwargs)
        return self._client.post(
            "monitor", "/user/password-policy-conform/select", data=data
        )


class PasswordPolicyConform:
    """PasswordPolicyConform operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize PasswordPolicyConform endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.select = Select(client)
