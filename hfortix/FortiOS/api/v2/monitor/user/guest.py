"""
FortiOS MONITOR - Monitor User Guest

Monitoring endpoint for monitor user guest data.

API Endpoints:
    GET    /monitor/user/guest

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.user.guest.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.user.guest.get(
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


class Email:
    """
    Email Operations.

    Provides read-only access for FortiOS email data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Email endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        group: str | None = None,
        guest: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Sent guest login details via email.

        Args:
            group: Guest group name. (optional)
            guest: Guest user IDs. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.guest.email.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if group is not None:
            data["group"] = group
        if guest is not None:
            data["guest"] = guest
        data.update(kwargs)
        return self._client.post("monitor", "/user/guest/email", data=data)


class Sms:
    """Sms operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Sms endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        group: str | None = None,
        guest: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Sent guest login details via SMS.

        Args:
            group: Guest group name. (optional)
            guest: Guest user IDs. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.guest.sms.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if group is not None:
            data["group"] = group
        if guest is not None:
            data["guest"] = guest
        data.update(kwargs)
        return self._client.post("monitor", "/user/guest/sms", data=data)


class Guest:
    """Guest operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Guest endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.email = Email(client)
        self.sms = Sms(client)
