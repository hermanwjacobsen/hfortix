"""
FortiOS MONITOR - Monitor System Botnet

Monitoring endpoint for monitor system botnet data.

API Endpoints:
    GET    /monitor/system/botnet

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.botnet.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.botnet.get(
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


class Stat:
    """
    Stat Operations.

    Provides read-only access for FortiOS stat data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Stat endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve statistics for FortiGuard botnet database.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.botnet.stat.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/botnet/stat", params=params
        )


class Botnet:
    """Botnet operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Botnet endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.stat = Stat(client)

    def get(
        self,
        include_hit_only: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List all known IP-based botnet entries in FortiGuard botnet database.

        Args:
            include_hit_only: Include entries with hits only. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.botnet.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if include_hit_only is not None:
            params["include_hit_only"] = include_hit_only
        params.update(kwargs)
        return self._client.get("monitor", "/system/botnet", params=params)
