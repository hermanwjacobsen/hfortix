"""
FortiOS MONITOR - Monitor System Available Interfaces

Monitoring endpoint for monitor system available interfaces data.

API Endpoints:
    GET    /monitor/system/available_interfaces

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.available_interfaces.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.available_interfaces.get(
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


class Meta:
    """
    Meta Operations.

    Provides read-only access for FortiOS meta data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Meta endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        scope: str | None = None,
        include_ha: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get metadata for the system/available-interfaces API endpoint.

        Args:
            scope: Scope of interface list [*vdom|global]. (optional)
            include_ha: Incude HA management interfaces. Will only show if
            accessing the root VDOM interfaces. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.available_interfaces.meta.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if scope is not None:
            params["scope"] = scope
        if include_ha is not None:
            params["include_ha"] = include_ha
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/available-interfaces/meta", params=params
        )


class AvailableInterfaces:
    """AvailableInterfaces operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize AvailableInterfaces endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.meta = Meta(client)

    def get(
        self,
        mkey: str | None = None,
        include_ha: bool | None = None,
        view_type: str | None = None,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a list of all interfaces along with some meta information
        regarding their availability.

        Args:
            mkey: Name of the interface. (optional)
            include_ha: Incude HA management interfaces. Will only show if
            accessing the root VDOM interfaces. (optional)
            view_type: Deprecated: Use format instead (optional)
            scope: Scope of interface list [vdom|global] (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.available_interfaces.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params["mkey"] = mkey
        if include_ha is not None:
            params["include_ha"] = include_ha
        if view_type is not None:
            params["view_type"] = view_type
        if scope is not None:
            params["scope"] = scope
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/available-interfaces", params=params
        )
