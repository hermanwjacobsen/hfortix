"""
FortiOS MONITOR - Monitor System Password Policy Conform

Monitoring endpoint for monitor system password policy conform data.

API Endpoints:
    GET    /monitor/system/password_policy_conform

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.password_policy_conform.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.password_policy_conform.get(
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
        mkey: str | None = None,
        apply_to: str | None = None,
        password: str | None = None,
        old_password: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Check whether password conforms to the password policy.

        Args:
            mkey: User ID for password change. (optional)
            apply_to: Password Policy ID. (optional)
            password: Password. (optional)
            old_password: Old password. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.password_policy_conform.select.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data["mkey"] = mkey
        if apply_to is not None:
            data["apply_to"] = apply_to
        if password is not None:
            data["password"] = password
        if old_password is not None:
            data["old_password"] = old_password
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/password-policy-conform/select", data=data
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
