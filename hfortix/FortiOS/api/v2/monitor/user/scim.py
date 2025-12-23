"""
FortiOS MONITOR - Monitor User Scim

Monitoring endpoint for monitor user scim data.

API Endpoints:
    GET    /monitor/user/scim

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.user.scim.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.user.scim.get(
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


class Groups:
    """
    Groups Operations.

    Provides read-only access for FortiOS groups data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Groups endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        client_name: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get SCIM client group-names.

        Args:
            client_name: SCIM client name to be used to retrieve group names.
            (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.scim.groups.get(client_name='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["client_name"] = client_name
        params.update(kwargs)
        return self._client.get("monitor", "/user/scim/groups", params=params)


class Users:
    """Users operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Users endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        client_name: str,
        group_name: str | None = None,
        user_name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get SCIM client users.

        Args:
            client_name: SCIM client name to be used to retrieve group names.
            (required)
            group_name: SCIM client group name to be used to retrieve users, if
            left empty, will retrieve users from all groups. (optional)
            user_name: SCIM client user name to retrieve, if left empty, will
            retrieve all users from group. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.scim.users.get(client_name='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["client_name"] = client_name
        if group_name is not None:
            params["group_name"] = group_name
        if user_name is not None:
            params["user_name"] = user_name
        params.update(kwargs)
        return self._client.get("monitor", "/user/scim/users", params=params)


class Scim:
    """Scim operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Scim endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.groups = Groups(client)
        self.users = Users(client)
