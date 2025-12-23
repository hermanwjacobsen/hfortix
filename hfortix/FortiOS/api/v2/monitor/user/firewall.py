"""
FortiOS MONITOR - Monitor User Firewall

Monitoring endpoint for monitor user firewall data.

API Endpoints:
    GET    /monitor/user/firewall

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.user.firewall.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.user.firewall.get(
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


class Auth:
    """
    Auth Operations.

    Provides read-only access for FortiOS auth data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Auth endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        username: str | None = None,
        ip: str | None = None,
        server: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Trigger authentication for a single firewall user.

        Args:
            username: User name. (optional)
            ip: User IP address. (optional)
            server: Name of an existing LDAP server entry. If supplied,
            authenticate that user against any matched groups on that LDAP
            server. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.firewall.auth.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if username is not None:
            data["username"] = username
        if ip is not None:
            data["ip"] = ip
        if server is not None:
            data["server"] = server
        data.update(kwargs)
        return self._client.post("monitor", "/user/firewall/auth", data=data)


class Count:
    """Count operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Count endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        ipv4: bool | None = None,
        ipv6: bool | None = None,
        include_fsso: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get the number of authenticated firewall users.

        Args:
            ipv4: Include IPv4 users (default=true). (optional)
            ipv6: Include IPv6 users (default=false). (optional)
            include_fsso: Include FSSO users (default=true). (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.firewall.count.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if ipv4 is not None:
            params["ipv4"] = ipv4
        if ipv6 is not None:
            params["ipv6"] = ipv6
        if include_fsso is not None:
            params["include_fsso"] = include_fsso
        params.update(kwargs)
        return self._client.get(
            "monitor", "/user/firewall/count", params=params
        )


class Deauth:
    """Deauth operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Deauth endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        user_type: str | None = None,
        id: int | None = None,
        ip: str | None = None,
        ip_version: str | None = None,
        method: str | None = None,
        all: bool | None = None,
        users: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Deauthenticate single, multiple, or all firewall users.

        Args:
            user_type: User type [proxy|firewall]. Required for both proxy and
            firewall users. (optional)
            id: User ID. Required for both proxy and firewall users. (optional)
            ip: User IP address. Required for both proxy and firewall users.
            (optional)
            ip_version: IP version [ip4|ip6]. Only required if user_type is
            firewall. (optional)
            method: Authentication method
            [fsso|rsso|ntlm|firewall|wsso|fsso_citrix|sso_guest]. Only required
            if user_type is firewall. (optional)
            all: Set to true to deauthenticate all users. Other parameters will
            be ignored. (optional)
            users: Array of user objects to deauthenticate. Use this to
            deauthenticate multiple users at once. Each object should include
            the above properties. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.firewall.deauth.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if user_type is not None:
            data["user_type"] = user_type
        if id is not None:
            data["id"] = id
        if ip is not None:
            data["ip"] = ip
        if ip_version is not None:
            data["ip_version"] = ip_version
        if method is not None:
            data["method"] = method
        if all is not None:
            data["all"] = all
        if users is not None:
            data["users"] = users
        data.update(kwargs)
        return self._client.post("monitor", "/user/firewall/deauth", data=data)


class Firewall:
    """Firewall operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Firewall endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.auth = Auth(client)
        self.count = Count(client)
        self.deauth = Deauth(client)

    def get(
        self,
        ipv4: bool | None = None,
        ipv6: bool | None = None,
        include_fsso: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List authenticated firewall users.

        Args:
            ipv4: Include IPv4 users (default=true). (optional)
            ipv6: Include IPv6 users (default=false). (optional)
            include_fsso: Include FSSO users (default=true). (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.firewall.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if ipv4 is not None:
            params["ipv4"] = ipv4
        if ipv6 is not None:
            params["ipv6"] = ipv6
        if include_fsso is not None:
            params["include_fsso"] = include_fsso
        params.update(kwargs)
        return self._client.get("monitor", "/user/firewall", params=params)
