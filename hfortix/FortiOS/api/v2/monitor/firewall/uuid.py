"""
FortiOS MONITOR - Monitor Firewall Uuid

Monitoring endpoint for monitor firewall uuid data.

API Endpoints:
    GET    /monitor/firewall/uuid

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.uuid.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.uuid.get(
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


class TypeLookup:
    """
    Typelookup Operations.

    Provides read-only access for FortiOS typelookup data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize TypeLookup resource.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        uuids: str | list[str],
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a mapping of UUIDs to their firewall object type for given
        UUIDs.

        Args:
            uuids: UUID or list of UUIDs to lookup (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary mapping UUIDs to their object types

        Example:
            >>> fgt.api.monitor.firewall.uuid.type_lookup.get(uuids='uuid1')
            >>> fgt.api.monitor.firewall.uuid.type_lookup.get(uuids=['uuid1',
            'uuid2'])
        """
        params = payload_dict.copy() if payload_dict else {}
        params["uuids"] = uuids
        params.update(kwargs)
        return self._client.get(
            "monitor", "/firewall/uuid-type-lookup", params=params
        )


class UUID:
    """UUID list and type lookup operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize UUID endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize resource endpoints
        self.type_lookup = TypeLookup(client)

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a list of all UUIDs with their object type and VDOM.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing UUID list

        Example:
            >>> fgt.api.monitor.firewall.uuid.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/firewall/uuid-list", params=params
        )
