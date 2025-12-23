"""
FortiOS MONITOR - Monitor Router Policy6

Monitoring endpoint for monitor router policy6 data.

API Endpoints:
    GET    /monitor/router/policy6

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.router.policy6.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.router.policy6.get(
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


class Policy6:
    """
    Policy6 Operations.

    Provides read-only access for FortiOS policy6 data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Policy6 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        count_only: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a list of active IPv6 policy routes.

        Args:
            count_only: Returns the number of IPv6 policy routes only.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.router.policy6.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if count_only is not None:
            params["count_only"] = count_only
        params.update(kwargs)
        return self._client.get("monitor", "/router/policy6", params=params)
